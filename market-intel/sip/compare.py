from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


_TICKER_RE = re.compile(
    r"^\d{4}(?:\.(?:TPEX|TW|TWO))?$",
    re.IGNORECASE,
)

_PROSE_TICKER_RE = re.compile(
    r"^(?P<ticker>\d{4}(?:\.(?:TPEX|TW|TWO))?)\s+"
    r"[^\n|]*\([^\n|]*\)",
    re.IGNORECASE,
)

_NOTE_PREFIX_RE = re.compile(
    r"^\s*(?:also\b|negative\s+note\s*:|note\s*:|notes\s*:)",
    re.IGNORECASE,
)


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


def _normalize_ticker(value: str) -> str:
    ticker = str(value or "").strip()
    ticker = ticker.replace("`", "").replace("*", "")
    ticker = ticker.replace("[", "").replace("]", "")
    return ticker.upper()


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


def _valid_ticker(value: str) -> bool:
    return bool(_TICKER_RE.fullmatch(_normalize_ticker(value)))


def _prose_tickers(line: str) -> list[str]:
    """Parse CODE Name (…) entries at the start of pipe-separated segments."""
    tickers: list[str] = []
    for segment in line.split("|"):
        match = _PROSE_TICKER_RE.match(segment.strip())
        if not match:
            continue
        ticker = _normalize_ticker(match.group("ticker"))
        if _valid_ticker(ticker):
            tickers.append(ticker)
    return tickers


def parse_tier_tables(md: str | Path) -> dict[str, list[str]]:
    text = _read_markdown(md)
    tiers: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    in_table = False
    ticker_column = 0
    catalyst_column: int | None = None
    prose_active = False

    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if heading:
            current = _normalize_tier(heading.group(1))
            in_table = False
            ticker_column = 0
            catalyst_column = None
            prose_active = current is not None
            continue

        if current is None:
            continue

        if _NOTE_PREFIX_RE.match(line):
            prose_active = False
            in_table = False
            continue

        if "|" not in line:
            if in_table:
                continue
            in_table = False
            if prose_active and line.strip():
                for ticker in _prose_tickers(line):
                    tiers[current].append(ticker)
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            in_table = True
            continue

        if in_table:
            header = [
                re.sub(r"[`*\[\]]", "", cell).strip().lower()
                for cell in cells
            ]
            if "ticker" in header or "symbol" in header:
                ticker_column = (
                    header.index("ticker")
                    if "ticker" in header
                    else header.index("symbol")
                )
                catalyst_column = (
                    header.index("catalyst")
                    if "catalyst" in header
                    else None
                )
                continue

            if ticker_column >= len(cells):
                ticker_column = 0

            ticker = _normalize_ticker(cells[ticker_column])
            if not _valid_ticker(ticker):
                continue
            tiers[current].append(ticker)
            continue

        if prose_active:
            for ticker in _prose_tickers(line):
                tiers[current].append(ticker)

    return dict(tiers)


def _table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if "|" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or all(
            re.fullmatch(r":?-{3,}:?", cell) for cell in cells
        ):
            continue
        rows.append(cells)
    return rows


def _presence(text: str, ticker: str) -> tuple[bool, bool]:
    wanted = _normalize_ticker(ticker)
    rows = _table_rows(text)
    catalyst = False
    why = False

    for index, cells in enumerate(rows):
        header = [
            re.sub(r"[`*\[\]]", "", cell).strip().lower()
            for cell in cells
        ]
        has_header = "ticker" in header or "symbol" in header
        if has_header:
            ticker_column = (
                header.index("ticker")
                if "ticker" in header
                else header.index("symbol")
            )
            catalyst_column = (
                header.index("catalyst") if "catalyst" in header else None
            )
        else:
            ticker_column = 0
            catalyst_column = None

        if ticker_column >= len(cells):
            continue

        cell_ticker = _normalize_ticker(cells[ticker_column])
        if cell_ticker != wanted or not _valid_ticker(cell_ticker):
            continue

        if catalyst_column is not None and catalyst_column < len(cells):
            catalyst_value = cells[catalyst_column].strip()
            catalyst = catalyst_value.lower() not in {"", "-", "—", "n/a", "na"}
        else:
            catalyst = bool(cells) and cells[-1].strip().lower() not in {
                "",
                "-",
                "—",
                "n/a",
                "na",
            }

        window = " ".join(cells).lower()
        why = why or bool(re.search(r"\bwhy\b|reason", window))
        if index + 1 < len(rows):
            continue

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
