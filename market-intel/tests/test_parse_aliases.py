from __future__ import annotations

import pytest

from sip.markets.taiwan.parse import (
    ParseError,
    _row_from_yahoo,
    parse_fx_json,
    parse_tv_dump,
)


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"rates": {"USDTWD": 32.7}}, 32.7),
        ({"rates": {"USD/TWD": 32.7}}, 32.7),
        ({"rates": {"TWD=X": 32.7}}, 32.7),
        ({"base_code": "USD", "rates": {"TWD": 32.7}}, 32.7),
        ({"baseCode": "USD", "rates": {"TWD": 32.7}}, 32.7),
    ],
)
def test_parse_fx_rates_map_aliases(payload: dict, expected: float) -> None:
    assert parse_fx_json(payload) == expected


@pytest.mark.parametrize("key", ["usd_twd", "usdTwd", "USD_TWD", "rate", "price", "value"])
def test_parse_fx_top_level_aliases(key: str) -> None:
    assert parse_fx_json({key: 32.7}) == 32.7


@pytest.mark.parametrize("symbol", ["USDTWD", "USD/TWD", "TWD=X", "TWD"])
def test_parse_fx_list_symbol_aliases(symbol: str) -> None:
    assert parse_fx_json([{"symbol": symbol, "rate": 32.7}]) == 32.7


def test_parse_fx_rejects_unrelated_rate() -> None:
    with pytest.raises(ParseError, match="USD/TWD rate not found"):
        parse_fx_json({"rates": {"EURUSD": 1.1}})


@pytest.mark.parametrize(
    "alias", ["changePercent", "change_percent", "chg", "pc", "change_pct"]
)
def test_parse_tv_change_aliases(alias: str) -> None:
    rows = parse_tv_dump([{"symbol": "2308", alias: 6.2}])
    assert rows[0]["changePercent"] == 6.2


def test_yahoo_regular_market_day_range_aliases() -> None:
    row = _row_from_yahoo(
        {
            "symbol": "2308",
            "regularMarketDayHigh": 1276.0,
            "regularMarketDayLow": 1270.0,
        }
    )
    assert row["dayHigh"] == 1276.0
    assert row["dayLow"] == 1270.0


def test_yahoo_high_low_aliases_are_additive() -> None:
    row = _row_from_yahoo(
        {
            "symbol": "2308",
            "high": 1276.0,
            "low": 1270.0,
        }
    )
    assert row["dayHigh"] == 1276.0
    assert row["dayLow"] == 1270.0
