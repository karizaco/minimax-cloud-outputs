"""Taiwan ticker naming utilities."""

from __future__ import annotations

from typing import Any, Iterable, Mapping

TWSE_ROSTER: dict[str, dict[str, str]] = {}
TPEX_ROSTER: dict[str, dict[str, str]] = {}


def _code(value: Any) -> str:
    return str(value or "").strip().split(".")[0].upper()


def display_ticker(code: Any, venue: str | None = None) -> str:
    """Return a bare TWSE ticker or a ``.TPEX`` OTC ticker."""
    ticker = _code(code)
    if not ticker:
        return ""
    venue = (venue or "").strip().upper()
    if venue in {"TPEX", "OTC", "上櫃", "TPEX.TWO"}:
        return f"{ticker}.TPEX"
    return ticker


def yahoo_symbol(code: Any, venue: str | None = None) -> str:
    """Return the Yahoo Finance symbol for a Taiwan security."""
    ticker = _code(code)
    if not ticker:
        return ""
    venue = (venue or "").strip().upper()
    if venue in {"TPEX", "OTC", "上櫃", "TWO"}:
        return f"{ticker}.TWO"
    if venue in {"TWSE", "TAI", "上市", "TW"}:
        return f"{ticker}.TW"
    if ticker.endswith(".TWO"):
        return ticker
    if ticker.endswith(".TW"):
        return ticker
    return f"{ticker}.TW"


def _english(roster: Mapping[str, Any], code: Any) -> str:
    ticker = _code(code)
    item = roster.get(ticker, roster.get(ticker.lower()))
    if isinstance(item, Mapping):
        for key in ("english_name", "english", "en", "name_en"):
            value = item.get(key)
            if value:
                return str(value).strip()
    if isinstance(item, str):
        return item.strip()
    return ""


def english_name(code: Any, venue: str | None = None) -> str:
    """Look up an English company name in the TWSE or TPEX roster."""
    ticker = _code(code)
    venue = (venue or "").strip().upper()
    if venue in {"TPEX", "OTC", "上櫃", "TWO"}:
        return _english(TPEX_ROSTER, ticker)
    if venue in {"TWSE", "TAI", "上市", "TW"}:
        return _english(TWSE_ROSTER, ticker)
    return _english(TWSE_ROSTER, ticker) or _english(TPEX_ROSTER, ticker)


def register_roster(
    venue: str,
    roster: Mapping[str, Any] | Iterable[Mapping[str, Any]],
) -> None:
    """Register roster data, accepting either a mapping or an iterable."""
    target = TPEX_ROSTER if venue.upper() in {"TPEX", "OTC", "上櫃"} else TWSE_ROSTER
    if isinstance(roster, Mapping):
        target.update(roster)
        return
    for item in roster:
        if not isinstance(item, Mapping):
            continue
        code = _code(item.get("code") or item.get("ticker") or item.get("symbol"))
        if code:
            target[code] = dict(item)
