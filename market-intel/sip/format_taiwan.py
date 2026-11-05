"""Taiwan-market formatting helpers for SIP outputs."""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from typing import Any

_TIER_NAMES = ("Tier A", "Soft-A", "TECH_WATCH", "Tier B", "Tier C")
_TIER_KEYS = ("A", "Soft-A", "TECH_WATCH", "B", "C")


def _number(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return default
    return result if math.isfinite(result) else default


def _first(row: Mapping[str, Any], *keys: str, default: Any = "") -> Any:
    for key in keys:
        if key in row and row[key] is not None:
            return row[key]
    return default


def _tier_name(tier: str) -> str:
    value = str(tier).strip()
    upper = value.upper()
    if upper == "A" or upper.startswith("TIER A"):
        return "A"
    if upper.startswith("SOFT-A") or upper.startswith("SOFT_A"):
        return "Soft-A"
    if upper.startswith("TECH_WATCH"):
        return "TECH_WATCH"
    if upper.startswith("B") or upper.startswith("TIER B"):
        return "B"
    return "C"


def _tier_heading(tier: str) -> str:
    return {
        "A": "Tier A",
        "Soft-A": "Soft-A",
        "TECH_WATCH": "TECH_WATCH",
        "B": "Tier B",
        "C": "Tier C",
    }[_tier_name(tier)]


def display_ticker(row: Mapping[str, Any]) -> str:
    explicit = str(_first(row, "display_ticker", default="")).strip().upper()
    if explicit:
        return explicit
    ticker = str(_first(row, "symbol", "ticker", "code", default="")).strip().upper()
    if ticker.endswith(".TPEX"):
        return ticker
    if ticker.endswith(".TWO"):
        return f"{ticker[:-4]}.TPEX"
    if ticker.endswith(".TW"):
        return ticker[:-3]
    digits = "".join(character for character in ticker if character.isdigit())
    if len(digits) == 4:
        venue = str(_first(row, "venue", "board", default="")).strip().upper()
        if venue in {"TPEX", "TPE", "OTC", "上櫃"}:
            return f"{digits}.TPEX"
        return digits
    return ticker


def format_move(value: Any) -> str:
    number = _number(value)
    sign = "+" if number > 0 else ""
    if number == 0:
        return "0%"
    if abs(number) < 1:
        text = f"{number:.1f}"
    else:
        text = f"{number:.1f}".rstrip("0").rstrip(".")
    return f"{sign}{text}%"


def format_rvol(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"{_number(value):.1f}x"


def format_twd(value: Any) -> str:
    number = _number(value)
    if abs(number) >= 1_000_000_000:
        return f"TWD {number / 1_000_000_000:.1f}bn".replace(".0bn", "bn")
    if abs(number) >= 1_000_000:
        return f"TWD {number / 1_000_000:.1f}m".replace(".0m", "m")
    if abs(number) >= 1_000:
        return f"TWD {number / 1_000:.0f}k"
    return f"TWD {number:.0f}"


def format_turnover_usd(twd: Any, fx: Any) -> str:
    twd_value = _number(twd)
    rate = _number(fx)
    if rate <= 0:
        return "US$0"
    absolute = abs(twd_value / rate)
    sign = "-" if twd_value < 0 else ""
    if absolute >= 1_000_000_000:
        amount = absolute / 1_000_000_000
        return f"{sign}US${amount:.1f}bn".replace(".0bn", "bn")
    if absolute >= 1_000_000:
        amount = absolute / 1_000_000
        return f"{sign}US${amount:.1f}m".replace(".0m", "m")
    if absolute >= 1_000:
        amount = absolute / 1_000
        return f"{sign}US${amount:.0f}k"
    return f"{sign}US${absolute:.0f}"


def _company(row: Mapping[str, Any]) -> str:
    english = str(_first(row, "company_en", "english_name", "en", default="")).strip()
    chinese = str(_first(row, "company_zh", "name", default="")).strip()
    if english and chinese:
        return f"{english} ({chinese})"
    return english or chinese or "—"


def _catalyst(row: Mapping[str, Any]) -> str:
    return str(_first(row, "catalyst", "why", default="—") or "—").replace("|", "\\|")


def _rows(rows_by_tier: Mapping[str, Sequence[Mapping[str, Any]]] | Sequence[Mapping[str, Any]]) -> list[tuple[str, Mapping[str, Any]]]:
    if isinstance(rows_by_tier, Mapping):
        candidates = rows_by_tier.get("candidates")
        if isinstance(candidates, list):
            return [
                (str(row.get("tier", "C")), row)
                for row in candidates
                if isinstance(row, Mapping)
            ]
        result: list[tuple[str, Mapping[str, Any]]] = []
        for tier, rows in rows_by_tier.items():
            for row in rows or []:
                result.append((str(tier), row))
        return result
    return [
        (str(row.get("tier", "C")), row)
        for row in rows_by_tier or []
    ]


def _turnover(row: Mapping[str, Any]) -> float:
    return _number(
        _first(
            row,
            "turnover_twd",
            "twd_turnover",
            "turnover",
            "dollar_vol",
            default=0,
        )
    )


def _is_material_c(row: Mapping[str, Any], midday_turnover_floor: float) -> bool:
    flags = {str(flag).upper() for flag in _first(row, "flags", default=[]) or []}
    if flags & {"LIMIT_UP", "LIMIT_DOWN", "HALT", "HALTED", "FRESH_HALT", "FRESH_HALTED"}:
        return True
    return _turnover(row) >= midday_turnover_floor


def _top_n(rows: Sequence[Mapping[str, Any]], limit: Any) -> list[Mapping[str, Any]]:
    try:
        count = int(limit)
    except (TypeError, ValueError):
        return list(rows)
    if count < 0:
        return list(rows)
    return sorted(
        rows,
        key=lambda row: (-_turnover(row), str(_first(row, "ticker", "symbol", default=""))),
    )[:count]


def render_chat(
    rows_by_tier: Mapping[str, Sequence[Mapping[str, Any]]] | Sequence[Mapping[str, Any]],
    *,
    skipped: Sequence[Any] | None = None,
    header: str = "",
    fx: Any = None,
    top_n: Mapping[str, Any] | None = None,
    midday_turnover_floor: float = 100_000_000,
) -> str:
    lines: list[str] = []
    if header:
        lines.extend([str(header).strip(), ""])
    groups: dict[str, list[Mapping[str, Any]]] = {name: [] for name in _TIER_KEYS}
    for tier, row in _rows(rows_by_tier):
        groups.setdefault(_tier_name(tier), []).append(row)
    limits = top_n or {}
    for tier in _TIER_KEYS:
        rows = list(groups.get(tier, []))
        if tier == "C":
            rows = [row for row in rows if _is_material_c(row, midday_turnover_floor)]
        rows = _top_n(rows, limits.get(tier, len(rows)))
        if not rows:
            continue
        lines.extend([f"## {_tier_heading(tier)}", ""])
        if tier in {"A", "Soft-A"}:
            lines.append("| Ticker | Company | Move | RelVol | Turnover | Catalyst |")
            lines.append("|---|---|---:|---:|---:|---|")
        else:
            lines.append("| Ticker | Company | Move | RelVol | Turnover |")
            lines.append("|---|---|---:|---:|---:|")
        for row in rows:
            values = [
                display_ticker(row),
                _company(row),
                format_move(_first(row, "chg_pct", "change_pct", "move", default=0)),
                format_rvol(_first(row, "rvol", "relative_volume", default=None)),
                format_turnover_usd(
                    _first(row, "turnover_twd", "twd_turnover", "turnover", "dollar_vol", default=0),
                    _first(row, "fx", "fx_rate", default=fx),
                ),
            ]
            if tier in {"A", "Soft-A"}:
                values.append(_catalyst(row))
            lines.append("| " + " | ".join(values) + " |")
        lines.append("")
    if skipped:
        details: list[str] = []
        for item in skipped:
            if isinstance(item, Mapping):
                ticker = display_ticker(item)
                reason = _first(item, "reason", "status", default="skipped")
                details.append(f"{ticker}: {reason}" if ticker else str(reason))
            else:
                details.append(str(item))
        lines.append("⚠️ Skipped: " + "; ".join(details))
    return "\n".join(lines).rstrip() + "\n"


def _source_rows(run_dict: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    for key in ("candidates", "rows", "results", "stocks", "data"):
        value = run_dict.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, Mapping)]
    return []


def render_digest(
    run_dict: Mapping[str, Any],
    *,
    top_n: Mapping[str, Any] | None = None,
) -> str:
    rows = _source_rows(run_dict)
    metadata = run_dict.get("metadata") if isinstance(run_dict.get("metadata"), Mapping) else {}
    fx = _first(run_dict, "fx", "fx_rate", default=_first(metadata, "fx", "fx_rate", default=None))
    date = _first(run_dict, "date", default=_first(metadata, "date", default=""))
    slot = _first(run_dict, "slot", default=_first(metadata, "slot", default=""))

    limits = top_n or {}
    if not limits:
        for key in ("digest_top_n", "chat_top_n"):
            value = run_dict.get(key, metadata.get(key) if isinstance(metadata, Mapping) else None)
            if isinstance(value, Mapping):
                limits = value
                break

    lines = ["# SIP Market Digest", ""]
    header_bits = []
    if date:
        header_bits.append(f"Date: {date}")
    if slot:
        header_bits.append(f"Slot: {slot}")
    if fx:
        header_bits.append(f"FX: {fx} TWD/USD")
    if header_bits:
        lines.extend([" | ".join(header_bits), ""])

    groups: dict[str, list[Mapping[str, Any]]] = {name: [] for name in _TIER_KEYS}
    for row in rows:
        groups.setdefault(_tier_name(str(row.get("tier", "C"))), []).append(row)

    for tier in _TIER_KEYS:
        tier_rows = _top_n(groups.get(tier, []), limits.get(tier, len(groups.get(tier, []))))
        if not tier_rows:
            continue
        lines.extend([f"## {_tier_heading(tier)}", ""])
        if tier in {"A", "Soft-A"}:
            lines.append("| Ticker | Company | Board | Price | Chg% | RVol | TWD | US$ | Catalyst |")
            lines.append("|---|---|---|---:|---:|---:|---:|---:|---|")
        else:
            lines.append("| Ticker | Company | Board | Price | Chg% | RVol | TWD | US$ | Why |")
            lines.append("|---|---|---|---:|---:|---:|---:|---:|---|")
        for row in tier_rows:
            twd = _first(row, "turnover_twd", "twd_turnover", "turnover", "dollar_vol", default=0)
            row_fx = _first(row, "fx", "fx_rate", default=fx)
            values = [
                display_ticker(row),
                _company(row),
                str(_first(row, "board", "venue", default="—")),
                f"{_number(_first(row, 'last', 'price', default=0)):.2f}",
                format_move(_first(row, "chg_pct", "change_pct", "move", default=0)),
                format_rvol(_first(row, "rvol", "relative_volume", default=None)),
                format_twd(twd),
                format_turnover_usd(twd, row_fx),
                _catalyst(row),
            ]
            lines.append("| " + " | ".join(values) + " |")
        lines.append("")

    skipped = run_dict.get("skipped")
    if skipped:
        lines.extend(["## ⚠️ Skipped", ""])
        for item in skipped:
            if isinstance(item, Mapping):
                ticker = display_ticker(item)
                reason = _first(item, "reason", "status", default="skipped")
                lines.append(f"- {ticker}: {reason}")
            else:
                lines.append(f"- {item}")
        lines.append("")

    source_health = run_dict.get("source_health")
    if source_health is None:
        source_health = run_dict.get("health", {})
    lines.extend(["## Source health", ""])
    if isinstance(source_health, Mapping) and source_health:
        lines.append("| Source | Status | Detail |")
        lines.append("|---|---|---|")
        for source, detail in source_health.items():
            if isinstance(detail, Mapping):
                status = _first(detail, "status", "state", default="unknown")
                message = _first(detail, "detail", "message", "error", default="")
            else:
                status = "ok" if detail in (True, "ok", "healthy") else str(detail)
                message = ""
            lines.append(f"| {source} | {status} | {message} |")
    elif isinstance(source_health, list) and source_health:
        lines.append("| Source | Status | Detail |")
        lines.append("|---|---|---|")
        for detail in source_health:
            if isinstance(detail, Mapping):
                source = _first(detail, "source", "name", default="unknown")
                status = _first(detail, "status", "state", default="unknown")
                message = _first(detail, "detail", "message", "error", default="")
            else:
                source, status, message = "unknown", str(detail), ""
            lines.append(f"| {source} | {status} | {message} |")
    else:
        lines.append("No source-health details were provided.")

    if fx:
        lines.extend(["", "## FX", "", f"USD/TWD: {fx}"])
    return "\n".join(lines).rstrip() + "\n"
