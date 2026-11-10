"""Parsers for Taiwan market public-data pages."""

from __future__ import annotations

import html as html_module
import json
import re
from html.parser import HTMLParser
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


def _normalized_key(value: Any) -> str:
    return re.sub(r"\s+", "", str(value))


def _first(data: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    """Return the first present value, tolerating whitespace around JSON keys."""
    for key in keys:
        if key in data and data[key] is not None:
            return data[key]
    normalized = {_normalized_key(key): value for key, value in data.items()}
    for key in keys:
        value = normalized.get(_normalized_key(key))
        if value is not None:
            return value
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
        "previousClose": _number(_first(data, "previousClose", "pc")),
        "dayHigh": _number(_first(data, "dayHigh", "regularMarketDayHigh", "high")),
        "dayLow": _number(_first(data, "dayLow", "regularMarketDayLow", "low")),
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


def parse_mops_browser_text(text: str) -> list[dict[str, Any]]:
    """Parse MOPS browser pipe text into catalyst rows."""
    rows: list[dict[str, Any]] = []
    pattern = re.compile(
        r"^(?P<time>\d{1,2}/\d{1,2}(?:\s+\d{1,2}:\d{2})?)\s*\|\s*"
        r"(?P<ticker>\d{4})\s*\|\s*(?P<company>[^|]+?)\s*\|\s*"
        r"(?P<headline>.+?)\s*$"
    )
    for raw_line in str(text or "").splitlines():
        match = pattern.match(raw_line.strip())
        if not match:
            continue
        values = match.groupdict()
        headline = values["headline"].strip()
        company = values["company"].strip()
        if not headline or not company:
            continue
        ticker = values["ticker"]
        rows.append(
            {
                "ticker": ticker,
                "code": ticker,
                "headline": headline,
                "catalyst": headline,
                "time": values["time"],
                "catalyst_time": values["time"],
                "raw": {**values, "company": company},
            }
        )
    return rows


def _readable_twse_time(item: Mapping[str, Any]) -> str:
    date = str(_first(item, "發言日期", default="")).strip()
    clock = str(_first(item, "發言時間", default="")).strip()
    if re.fullmatch(r"\d{7}", date) and re.fullmatch(r"\d{4,6}", clock):
        month = date[3:5]
        day = date[5:7]
        hour = clock[0:2]
        minute = clock[2:4]
        return f"{month}/{day} {hour}:{minute}"
    return ""


def parse_mops_items(
    json_obj_or_list: Any,
) -> list[dict[str, Any]]:
    source = "mops"
    if isinstance(json_obj_or_list, (str, bytes)):
        try:
            payload = json.loads(json_obj_or_list)
        except (ValueError, json.JSONDecodeError) as exc:
            text = json_obj_or_list.decode("utf-8", errors="replace") if isinstance(
                json_obj_or_list, bytes
            ) else json_obj_or_list
            if "|" in text and re.search(
                r"^\s*\d{1,2}/\d{1,2}(?:\s+\d{1,2}:\d{2})?\s*\|",
                text,
                re.MULTILINE,
            ):
                return parse_mops_browser_text(text)
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
            _first(
                item,
                "ticker",
                "code",
                "sym",
                "symbol",
                "公司代號",
                default="",
            )
        ).strip()
        headline = str(
            _first(
                item,
                "catalyst",
                "headline",
                "subject",
                "subj",
                "title",
                "主旨",
                default="",
            )
        ).strip()
        if not headline:
            explanation = str(_first(item, "說明", default="")).strip()
            headline = explanation.splitlines()[0].strip() if explanation else ""
        if not ticker and not headline:
            continue
        readable_time = _readable_twse_time(item)
        fallback_time = str(
            _first(
                item,
                "catalyst_time",
                "time",
                "發言時間",
                "datetime",
                default="",
            )
        ).strip()
        catalyst_time = readable_time or fallback_time
        result.append(
            {
                "ticker": _symbol_code(ticker),
                "code": _symbol_code(ticker),
                "headline": headline,
                "catalyst": headline,
                "time": catalyst_time,
                "catalyst_time": catalyst_time,
                "raw": dict(item),
            }
        )
    return result


def parse_twse_ap04(json_obj_or_list: Any) -> list[dict[str, Any]]:
    """Parse TWSE OpenAPI AP04 material-information filings."""
    return parse_mops_items(json_obj_or_list)


class _MopsTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._row is not None and self._cell is not None:
            value = re.sub(r"\s+", " ", "".join(self._cell)).strip()
            self._row.append(value)
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if any(self._row):
                self.rows.append(self._row)
            self._row = None


def parse_mops_html(html: str) -> list[dict[str, Any]]:
    """Parse only MOPS HTML table rows that contain both a code and a subject."""
    parser = _MopsTableParser()
    try:
        parser.feed(str(html or ""))
        parser.close()
    except Exception as exc:
        raise ParseError("mops_html", f"invalid HTML: {exc}") from exc

    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for cells in parser.rows:
        code_index = next(
            (
                index
                for index, cell in enumerate(cells)
                if re.fullmatch(r"\d{4}", cell.strip())
            ),
            None,
        )
        if code_index is None:
            continue
        ticker = cells[code_index].strip()
        subject_candidates = [
            cell.strip()
            for index, cell in enumerate(cells)
            if index != code_index
            and cell.strip()
            and not re.fullmatch(r"\d{4}", cell.strip())
        ]
        if not subject_candidates:
            continue
        headline = subject_candidates[-1]
        identity = (ticker, headline)
        if identity in seen:
            continue
        seen.add(identity)
        rows.append(
            {
                "ticker": ticker,
                "code": ticker,
                "headline": headline,
                "catalyst": headline,
                "time": "",
                "catalyst_time": "",
                "raw": {"cells": cells},
            }
        )
    return rows


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
        base_code = str(obj.get("base_code") or obj.get("baseCode") or "").upper()
        for key in ("usd_twd", "usdTwd", "USD_TWD", "rate", "price", "value"):
            if key in obj:
                value = _number(obj[key])
                if value is not None:
                    return value
        rates = _first(obj, "rates", "quotes", "data")
        if isinstance(rates, Mapping):
            if base_code == "USD":
                value = _number(rates.get("TWD"))
                if value is not None:
                    return value
            for key in ("USDTWD", "USD/TWD", "TWD=X", "TWD"):
                value = _number(rates.get(key))
                if value is not None:
                    return value
    elif isinstance(obj, list):
        for item in obj:
            if not isinstance(item, Mapping):
                continue
            symbol = str(_first(item, "symbol", "currency", default="")).upper()
            if symbol in {"USDTWD", "USD/TWD", "TWD=X", "TWD"}:
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
            obj, "candidates", "rows", "items", "data", default=[]
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
                    _first(
                        item,
                        "changePercent",
                        "change_percent",
                        "chg",
                        "pc",
                        "change_pct",
                    )
                ),
                "volume": _integer(_first(item, "volume", "vol")),
                "turnover": _number(_first(item, "turnover", "turn")),
                "raw": dict(item),
            }
        )
    return result
