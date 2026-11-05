"""Parsers for Taiwan market public-data pages."""

from __future__ import annotations

import html as html_module
import json
import re
from typing import Any, Iterable, Mapping


class ParseError(ValueError):
    def __init__(self, source: str, reason: str):
        self.source = source
        self.reason = reason
        super().__init__(f"{source}: {reason}")


def _number(value: Any, default: float | None = None) -> float | None:
    if value is None or value == "":
        return default
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "")
    text = re.sub(r"^[+]", "", text)
    text = re.sub(r"%$", "", text)
    percent = text.endswith("%")
    if percent:
        text = text[:-1]
    try:
        return float(text)
    except ValueError:
        return default


def _integer(value: Any, default: int | None = None) -> int | None:
    number = _number(value)
    return int(number) if number is not None else default


def _first(data: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    for key in keys:
        if key in data and data[key] is not None:
            return data[key]
    return default


def _json_objects(text: str) -> list[dict[str, Any]]:
    """Extract JSON objects from JS/HTML without requiring a page-specific schema."""
    objects: list[dict[str, Any]] = []
    decoder = json.JSONDecoder()

    for match in re.finditer(r"[\[{]", text):
        try:
            value, _ = decoder.raw_decode(text[match.start():])
        except (ValueError, json.JSONDecodeError):
            continue
        if isinstance(value, dict):
            objects.append(value)
        elif isinstance(value, list):
            objects.extend(item for item in value if isinstance(item, dict))

    return objects


def _symbol_code(symbol: Any) -> str:
    return str(symbol or "").strip().split(".")[0]


def _row_from_yahoo(data: Mapping[str, Any]) -> dict[str, Any]:
    symbol = str(_first(data, "symbol", "rowId", "ticker", default="")).strip()
    return {
        "symbol": symbol,
        "name": str(_first(data, "name", "symbolName", "shortName", default="")).strip(),
        "price": _number(_first(data, "price", "regularMarketPrice")),
        "changePercent": _number(
            _first(data, "changePercent", "change_pct", "regularMarketChangePercent")
        ),
        "turnoverK": _number(_first(data, "turnoverK", "turnover")),
        "volume": _integer(_first(data, "volume", "volK", "regularMarketVolume")),
        "limitUp": bool(_first(data, "limitUp", default=False)),
        "limitDown": bool(_first(data, "limitDown", default=False)),
        "previousClose": _number(_first(data, "previousClose")),
        "dayHigh": _number(_first(data, "dayHigh", "regularMarketDayHigh")),
        "dayLow": _number(_first(data, "dayLow", "regularMarketDayLow")),
    }


def parse_yahoo_rank_html(
    html: str,
    *,
    allow_empty: bool = False,
) -> list[dict[str, Any]]:
    source = "yahoo_rank"
    if not html or not html.strip():
        if allow_empty:
            return []
        raise ParseError(source, "empty document")

    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for data in _json_objects(html):
        symbol = _first(data, "symbol", "rowId")
        if not symbol or not any(
            key in data
            for key in ("price", "changePercent", "turnoverK", "regularMarketPrice")
        ):
            continue
        row = _row_from_yahoo(data)
        identity = row["symbol"]
        if identity and identity not in seen:
            seen.add(identity)
            rows.append(row)

    if rows:
        return rows
    if allow_empty or len(html) <= 500:
        return []
    raise ParseError(source, "page shell contained no rank rows")


def parse_cmoney_change_up_html(
    html: str,
    *,
    allow_empty: bool = False,
) -> list[dict[str, Any]]:
    source = "cmoney_change_up"
    if not html or not html.strip():
        if allow_empty:
            return []
        raise ParseError(source, "empty document")

    rows: list[dict[str, Any]] = []
    for data in _json_objects(html):
        code = _first(data, "code", "ticker", "symbol")
        if not code:
            continue
        symbol = str(code).strip()
        rows.append(
            {
                "symbol": symbol,
                "code": _symbol_code(symbol),
                "name": str(_first(data, "name", "companyName", default="")).strip(),
                "price": _number(_first(data, "price", "close")),
                "changePercent": _number(
                    _first(data, "changePercent", "change_pct", "pc", "change")
                ),
                "previousClose": _number(_first(data, "previousClose", "pc")),
                "volume": _integer(_first(data, "volume", "vol")),
                "turnover": _number(_first(data, "turnover", "turn")),
            }
        )

    if rows:
        return rows
    if allow_empty or len(html) <= 500:
        return []
    raise ParseError(source, "page shell contained no change rows")


def parse_mops_items(
    json_obj_or_list: Any,
) -> list[dict[str, Any]]:
    source = "mops"
    if isinstance(json_obj_or_list, (str, bytes)):
        try:
            payload = json.loads(json_obj_or_list)
        except (ValueError, json.JSONDecodeError) as exc:
            raise ParseError(source, f"invalid JSON: {exc}") from exc
    else:
        payload = json_obj_or_list

    if isinstance(payload, Mapping):
        items = _first(payload, "items", "data", "result", default=[])
    else:
        items = payload
    if items is None:
        items = []
    if not isinstance(items, list):
        raise ParseError(source, "items are not a list")

    result: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, Mapping):
            continue
        ticker = str(
            _first(item, "ticker", "code", "symbol", "公司代號", default="")
        ).strip()
        headline = str(
            _first(item, "headline", "subject", "subj", "title", "主旨", default="")
        ).strip()
        if not ticker and not headline:
            continue
        result.append(
            {
                "ticker": _symbol_code(ticker),
                "headline": headline,
                "time": str(
                    _first(item, "time", "發言時間", "datetime", default="")
                ).strip(),
                "raw": dict(item),
            }
        )
    return result


def _parse_roster(payload: Any, source: str) -> dict[str, dict[str, Any]]:
    if isinstance(payload, (str, bytes)):
        try:
            payload = json.loads(payload)
        except (ValueError, json.JSONDecodeError) as exc:
            raise ParseError(source, f"invalid JSON: {exc}") from exc

    if isinstance(payload, Mapping):
        items = _first(payload, "items", "data", "result", "companies", default=payload)
        if isinstance(items, Mapping):
            result: dict[str, dict[str, Any]] = {}
            for code, value in items.items():
                if isinstance(value, Mapping):
                    result[_symbol_code(code)] = dict(value)
                elif value:
                    result[_symbol_code(code)] = {"english_name": str(value)}
            return result
    else:
        items = payload

    if not isinstance(items, list):
        raise ParseError(source, "roster is not a list")
    result = {}
    for item in items:
        if not isinstance(item, Mapping):
            continue
        code = _symbol_code(
            _first(item, "code", "ticker", "symbol", "公司代號", default="")
        )
        if code:
            result[code] = dict(item)
    return result


def parse_twse_roster(payload: Any) -> dict[str, dict[str, Any]]:
    return _parse_roster(payload, "twse_roster")


def parse_tpex_roster(payload: Any) -> dict[str, dict[str, Any]]:
    return _parse_roster(payload, "tpex_roster")


def parse_fx_json(obj: Any) -> float:
    source = "fx"
    if isinstance(obj, (str, bytes)):
        try:
            obj = json.loads(obj)
        except (ValueError, json.JSONDecodeError) as exc:
            raise ParseError(source, f"invalid JSON: {exc}") from exc

    if isinstance(obj, Mapping):
        for key in ("usd_twd", "usdTwd", "USD_TWD", "rate", "price", "value"):
            if key in obj:
                value = _number(obj[key])
                if value is not None:
                    return value
        rates = _first(obj, "rates", "quotes", "data")
        if isinstance(rates, Mapping):
            for key in ("USDTWD", "USD/TWD", "TWD=X"):
                value = _number(rates.get(key))
                if value is not None:
                    return value
    elif isinstance(obj, list):
        for item in obj:
            if not isinstance(item, Mapping):
                continue
            symbol = str(_first(item, "symbol", "currency", default="")).upper()
            if symbol in {"USDTWD", "USD/TWD", "TWD=X"}:
                value = _number(_first(item, "rate", "price", "value"))
                if value is not None:
                    return value

    raise ParseError(source, "USD/TWD rate not found")


def parse_tv_dump(obj: Any) -> list[dict[str, Any]]:
    source = "tradingview"
    if isinstance(obj, (str, bytes)):
        try:
            obj = json.loads(obj)
        except (ValueError, json.JSONDecodeError) as exc:
            raise ParseError(source, f"invalid JSON: {exc}") from exc

    if isinstance(obj, Mapping):
        candidates = _first(
            obj,
            "candidates",
            "rows",
            "items",
            "data",
            default=[],
        )
    else:
        candidates = obj
    if candidates is None:
        candidates = []
    if not isinstance(candidates, list):
        raise ParseError(source, "candidates are not a list")

    result: list[dict[str, Any]] = []
    for item in candidates:
        if not isinstance(item, Mapping):
            continue
        symbol = str(
            _first(item, "symbol", "sym", "ticker", "code", default="")
        ).strip()
        if not symbol:
            continue
        result.append(
            {
                "symbol": symbol,
                "code": _symbol_code(symbol),
                "name": str(_first(item, "name", default="")).strip(),
                "price": _number(_first(item, "price", "close")),
                "changePercent": _number(
                    _first(item, "changePercent", "change_percent", "chg", "pc")
                ),
                "volume": _integer(_first(item, "volume", "vol")),
                "turnover": _number(_first(item, "turnover", "turn")),
                "raw": dict(item),
            }
        )
    return result
