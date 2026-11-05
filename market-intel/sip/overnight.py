from __future__ import annotations

from typing import Any, Iterable

from .schema import CandidateRow


def parse_overnight_carry(
    section: str | dict[str, Any] | list[Any],
) -> list[dict[str, Any]]:
    if isinstance(section, dict):
        raw = section.get("rows", section.get("tickers", []))
    else:
        raw = section

    if isinstance(section, str):
        raw = [
            token
            for token in section.replace(",", " ").split()
            if token
        ]

    if not isinstance(raw, list):
        return []

    result: list[dict[str, Any]] = []
    for item in raw:
        if isinstance(item, str):
            result.append({"ticker": item.upper(), "age_sessions": 0})
        elif isinstance(item, dict) and item.get("ticker"):
            entry = dict(item)
            entry["ticker"] = str(entry["ticker"]).upper()
            try:
                entry["age_sessions"] = int(entry.get("age_sessions", 0))
            except (TypeError, ValueError):
                entry["age_sessions"] = 0
            result.append(entry)
    return result


def promote_if_clears(
    carry: Iterable[dict[str, Any]],
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any] | None = None,
) -> list[CandidateRow]:
    """Promote carried candidates only when their current row clears the floors."""
    config = cfg or {}
    floors = config.get("floors", config)
    if not isinstance(floors, dict):
        floors = {}

    price_min = float(floors.get("price_min", 0))
    turnover_min = float(floors.get("turnover_min", 0))
    mcap_min = float(floors.get("mcap_min", 0))

    carried = {
        str(item.get("ticker", "")).upper()
        for item in carry
        if item.get("ticker")
    }

    result: list[CandidateRow] = []
    for row in rows:
        if row.ticker.upper() not in carried:
            continue

        mcap_floor_ok = row.mcap_twd is None or row.mcap_twd >= mcap_min
        turnover_ok = row.dollar_vol >= turnover_min
        if row.last >= price_min and (mcap_floor_ok or turnover_ok):
            result.append(row)

    return result
