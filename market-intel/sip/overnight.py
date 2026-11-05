from __future__ import annotations

from typing import Any, Iterable

from .schema import CandidateRow


def parse_overnight_carry(section: str | dict[str, Any] | list[Any]) -> list[dict[str, Any]]:
    if isinstance(section, dict):
        raw = section.get("rows", section.get("tickers", []))
    else:
        raw = section
    if not isinstance(raw, list):
        return []
    result = []
    for item in raw:
        if isinstance(item, str):
            result.append({"ticker": item.upper(), "age_sessions": 0})
        elif isinstance(item, dict) and item.get("ticker"):
            result.append(dict(item))
    return result


def promote_if_clears(
    carry: Iterable[dict[str, Any]],
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any] | None = None,
) -> list[CandidateRow]:
    """Promote carried candidates only when their current row clears the supplied floors."""
    cfg = cfg or {}
    result = []
    floors = cfg.get("floors", cfg)
    price_min = float(floors.get("price_min", 0))
    turnover_min = float(floors.get("turnover_min", 0))
    for row in rows:
        if row.last >= price_min and row.dollar_vol >= turnover_min:
            result.append(row)
    return result
