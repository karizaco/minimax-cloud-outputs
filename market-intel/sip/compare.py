from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


def _read_markdown(value: str | Path) -> str:
    if isinstance(value, Path):
        return value.read_text(encoding="utf-8")

    try:
        path = Path(value)
        if path.is_file():
            return path.read_text(encoding="utf-8")
    except (OSError, ValueError):
        pass

    return value


def _normalize_tier(title: str) -> str | None:
    value = re.sub(r"`[^`]*`", "", title).strip()
    value = re.sub(r"\s*\([^)]*\)\s*", "", value).strip()
    upper = value.upper().replace("_", "-")
    if upper.startswith("SOFT-A"):
        return "Soft-A"
    if upper.startswith("TECH-WATCH") or upper.startswith("TECH WATCH"):
        return "TECH_WATCH"
    if upper.startswith("TIER A") or upper == "A":
        return "A"
    if upper.startswith("TIER B") or upper == "B":
        return "B"
    if upper.startswith("TIER C") or upper == "C":
        return "C"
    return None


def parse_tier_tables(md: str | Path) -> dict[str, list[str]]:
    text = _read_markdown(md)
    tiers: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    in_table = False
    ticker_column = 0

    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if heading:
            current = _normalize_tier(heading.group(1))
            in_table = False
            ticker_column = 0
            continue

        if "|" not in line:
            in_table = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            in_table = True
            continue
        if not in_table or current is None:
            continue

        header = [re.sub(r"[`*\[\]]", "", cell).strip().lower() for cell in cells]
        if "ticker" in header or "symbol" in header:
            ticker_column = header.index("ticker") if "ticker" in header else header.index("symbol")
            continue
        if ticker_column >= len(cells):
            ticker_column = 0

        ticker = re.sub(r"[`*\[\]]", "", cells[ticker_column]).strip()
        if not ticker or re.fullmatch(r"(?:ticker|symbol)", ticker, re.I):
            continue
        tiers[current].append(ticker)
    return dict(tiers)


def _presence(text: str, ticker: str) -> tuple[bool, bool]:
    lines = text.splitlines()
    positions = [i for i, line in enumerate(lines) if ticker.lower() in line.lower()]
    catalyst = False
    why = False
    for position in positions:
        window = "\n".join(lines[position : position + 8]).lower()
        catalyst |= bool(re.search(r"catalyst", window))
        why |= bool(re.search(r"\bwhy\b|reason", window))
    return catalyst, why


def compare(shadow_md: str | Path, live_md: str | Path) -> dict:
    shadow_path = Path(shadow_md)
    live_path = Path(live_md)
    shadow_text = shadow_path.read_text(encoding="utf-8")
    live_text = live_path.read_text(encoding="utf-8")

    shadow = parse_tier_tables(shadow_text)
    live = parse_tier_tables(live_text)
    tier_names = sorted(set(shadow) | set(live))

    tiers: dict[str, dict[str, list[str]]] = {}
    presence: dict[str, dict[str, dict[str, bool]]] = {}
    for tier in tier_names:
        shadow_tickers = shadow.get(tier, [])
        live_tickers = live.get(tier, [])
        shadow_set, live_set = set(shadow_tickers), set(live_tickers)
        tiers[tier] = {
            "only_shadow": sorted(shadow_set - live_set),
            "only_live": sorted(live_set - shadow_set),
            "both": sorted(shadow_set & live_set),
        }

        tier_presence: dict[str, dict[str, bool]] = {}
        for ticker in tiers[tier]["both"]:
            shadow_catalyst, shadow_why = _presence(shadow_text, ticker)
            live_catalyst, live_why = _presence(live_text, ticker)
            tier_presence[ticker] = {
                "shadow_catalyst": shadow_catalyst,
                "live_catalyst": live_catalyst,
                "catalyst_diff": shadow_catalyst != live_catalyst,
                "shadow_why": shadow_why,
                "live_why": live_why,
                "why_diff": shadow_why != live_why,
            }
        presence[tier] = tier_presence

    summary = {
        "only_shadow": sum(len(v["only_shadow"]) for v in tiers.values()),
        "only_live": sum(len(v["only_live"]) for v in tiers.values()),
        "both": sum(len(v["both"]) for v in tiers.values()),
        "catalyst_diffs": sum(
            item["catalyst_diff"]
            for tier in presence.values()
            for item in tier.values()
        ),
        "why_diffs": sum(
            item["why_diff"]
            for tier in presence.values()
            for item in tier.values()
        ),
    }
    return {
        "shadow": str(shadow_path),
        "live": str(live_path),
        "tiers": tiers,
        "presence": presence,
        "summary": summary,
    }


def print_report(result: dict) -> None:
    print("Shadow comparison")
    for tier, values in result["tiers"].items():
        print(f"\n[{tier}]")
        print("  only shadow:", ", ".join(values["only_shadow"]) or "-")
        print("  only live:  ", ", ".join(values["only_live"]) or "-")
        print("  both:       ", ", ".join(values["both"]) or "-")
        for ticker, flags in result.get("presence", {}).get(tier, {}).items():
            if flags["catalyst_diff"] or flags["why_diff"]:
                print(
                    f"  {ticker}: catalyst shadow={flags['shadow_catalyst']} "
                    f"live={flags['live_catalyst']}; why shadow={flags['shadow_why']} "
                    f"live={flags['live_why']}"
                )
    print("\nSummary:", result["summary"])
