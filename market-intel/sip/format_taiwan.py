"""Taiwan-market formatting helpers for SIP outputs."""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from typing import Any


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


def display_ticker(row: Mapping[str, Any]) -> str:
    """Return a bare four-digit ticker, or an XXXX.TPEX symbol."""
    ticker = str(_first(row, "ticker", "symbol", "code", default="")).strip().upper()
    if ticker.endswith(".TPEX"):
        return ticker
    digits = "".join(character for character in ticker if character.isdigit())
    if len(digits) == 4:
        return digits
    return ticker


def format_move(value: Any) -> str:
    """Format a percentage move with an explicit sign."""
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
    """Format relative volume."""
    number = _number(value)
    return f"{number:.1f}x"


def format_turnover_usd(twd: Any, fx: Any) -> str:
    """Convert TWD turnover to US dollars and format it compactly."""
    twd_value = _number(twd)
    rate = _number(fx)
    if rate <= 0:
        return "US$0"

    usd = twd_value / rate
    absolute = abs(usd)
    sign = "-" if usd < 0 else ""

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


def _rows(
    rows_by_tier: Mapping[str, Sequence[Mapping[str, Any]]]
    | Sequence[Mapping[str, Any]],
) -> list[tuple[str, Mapping[str, Any]]]:
    if isinstance(rows_by_tier, Mapping):
        candidates = rows_by_tier.get("candidates")
        if isinstance(candidates, list):
            result: list[tuple[str, Mapping[str, Any]]] = []
            for row in candidates:
                if isinstance(row, Mapping):
                    tier = str(row.get("tier", "Tier 1"))
                    result.append((tier, row))
            return result

        result = []
        for tier, rows in rows_by_tier.items():
            for row in rows or []:
                result.append((str(tier), row))
        return result

    result = []
    for row in rows_by_tier or []:
        tier = str(row.get("tier", "Tier 1"))
        result.append((tier, row))
    return result


def render_chat(
    rows_by_tier: Mapping[str, Sequence[Mapping[str, Any]]]
    | Sequence[Mapping[str, Any]],
    *,
    skipped: Sequence[Any] | None = None,
    header: str = "",
) -> str:
    """Render SIP chat tables using the locked Taiwan-market columns."""
    lines: list[str] = []
    if header:
        lines.extend([str(header).strip(), ""])

    groups: dict[str, list[Mapping[str, Any]]] = {}
    for tier, row in _rows(rows_by_tier):
        groups.setdefault(tier, []).append(row)

    for tier, rows in groups.items():
        if not rows:
            continue
        lines.append(f"### {tier}")
        lines.append("")
        lines.append("| Ticker | Last | Move | RelVol | Turnover |")
        lines.append("|---|---:|---:|---:|---:|")
        for row in rows:
            ticker = display_ticker(row)
            last = _number(_first(row, "last", "price", default=0))
            move = _first(row, "chg_pct", "change_pct", "move", default=0)
            rvol = _first(row, "rvol", "relative_volume", default=0)
            twd = _first(
                row,
                "turnover_twd",
                "twd_turnover",
                "turnover",
                "dollar_vol",
                default=0,
            )
            fx = _first(row, "fx", "fx_rate", default=32.824)
            lines.append(
                f"| {ticker} | {last:.1f} | {format_move(move)} | "
                f"{format_rvol(rvol)} | {format_turnover_usd(twd, fx)} |"
            )
        lines.append("")

    if skipped:
        lines.append("### Skipped")
        lines.append("")
        for item in skipped:
            if isinstance(item, Mapping):
                ticker = display_ticker(item)
                reason = _first(item, "reason", "status", default="skipped")
                lines.append(f"- {ticker}: {reason}")
            else:
                lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _source_rows(run_dict: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    for key in ("rows", "results", "candidates", "stocks", "data"):
        value = run_dict.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, Mapping)]
    if isinstance(run_dict.get("items"), list):
        return [row for row in run_dict["items"] if isinstance(row, Mapping)]
    return []


def render_digest(run_dict: Mapping[str, Any]) -> str:
    """Render a fuller SIP digest, including source-health information."""
    rows = _source_rows(run_dict)
    lines = ["# SIP Market Digest", ""]

    metadata = (
        run_dict.get("metadata")
        if isinstance(run_dict.get("metadata"), Mapping)
        else {}
    )
    as_of = _first(
        metadata,
        "as_of",
        "timestamp",
        default=_first(run_dict, "as_of", "timestamp", default=""),
    )
    if as_of:
        lines.extend([f"As of: {as_of}", ""])

    lines.extend(["## Movers", ""])
    if rows:
        lines.append("| Ticker | Last | Move | RelVol | Turnover |")
        lines.append("|---|---:|---:|---:|---:|")
        for row in rows:
            fx = _first(
                row,
                "fx",
                "fx_rate",
                default=_first(metadata, "fx", "fx_rate", default=32.824),
            )
            twd = _first(
                row,
                "turnover_twd",
                "twd_turnover",
                "turnover",
                "dollar_vol",
                default=0,
            )
            lines.append(
                f"| {display_ticker(row)} | "
                f"{_number(_first(row, 'last', 'price', default=0)):.1f} | "
                f"{format_move(_first(row, 'chg_pct', 'change_pct', 'move', default=0))} | "
                f"{format_rvol(_first(row, 'rvol', 'relative_volume', default=0))} | "
                f"{format_turnover_usd(twd, fx)} |"
            )
    else:
        lines.append("No candidate rows were available.")
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

    return "\n".join(lines).rstrip() + "\n"
