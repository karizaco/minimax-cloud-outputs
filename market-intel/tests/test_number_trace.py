from sip.number_trace import check_chat


def test_check_chat_accepts_run_and_chat() -> None:
    run = {
        "date": "2026-01-01",
        "slot": "open",
        "fx": 32.824,
        "candidates": [
            {
                "ticker": "2330",
                "display_ticker": "2330",
                "venue": "TWSE",
                "instrument_type": "common",
                "last": 1000.0,
                "chg_pct": 5.25,
                "dollar_vol": 100_000_000.0,
                "usd_turnover": 3_046_930.0,
                "rvol": 1.75,
                "catalyst": "AI demand",
                "catalyst_time": "09:30",
                "flags": [],
                "source": "test",
                "asof": "2026-01-01T09:35:00+08:00",
                "tier": "A",
            }
        ],
    }
    chat = """
2330 台積電 | 1000.0 | +5.25% | RVOL 1.75 | 3.05M USD
AI demand at 09:30
"""

    result = check_chat(run, chat)
    if isinstance(result, tuple):
        ok, _report = result
    else:
        ok = result if isinstance(result, bool) else bool(result.get("ok"))

    assert ok
