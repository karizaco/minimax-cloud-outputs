from sip.tier import run_pipeline


def _row(ticker: str, **kwargs):
    row = {
        "ticker": ticker,
        "venue": "TWSE",
        "instrument_type": "common",
        "last": 100,
        "chg_pct": 1.0,
        "dollar_vol": 50_000_000,
        "rvol": 0.5,
        "catalyst": None,
        "catalyst_time": None,
        "flags": [],
        "source": "test",
        "asof": "2026-11-09",
        "tier": None,
    }
    row.update(kwargs)
    return row


def test_many_residual_unflagged_c_rows_are_dropped():
    rows = [_row(str(i)) for i in range(288)]
    rows[0]["flags"] = ["LIMIT_UP"]
    rows[0]["usd_turnover"] = 50_000_000

    result = run_pipeline(rows, {"c_limit_usd_min": 50_000_000}, "open")

    c_rows = [row for row in result if row.tier == "C"]
    assert [row.ticker for row in c_rows] == ["0"]


def test_all_daily_limits_above_usd_floor_are_kept_without_count_cap():
    rows = []
    for i in range(8):
        rows.append(
            _row(
                str(i),
                dollar_vol=50_000_000 + i,
                flags=["LIMIT_UP"],
                usd_turnover=50_000_000 + i,
            )
        )

    result = run_pipeline(
        rows,
        {
            "c_limit_usd_min": 50_000_000,
            "engine_top_n": {"C": 3},
            "digest_top_n": {"C": 3},
        },
        "open",
    )

    c_rows = [row for row in result if row.tier == "C"]
    assert len(c_rows) == 8
    assert [row.ticker for row in c_rows] == [str(i) for i in range(7, -1, -1)]


def test_daily_limit_below_usd_floor_is_dropped():
    rows = [
        _row(
            "LARGE",
            dollar_vol=60_000_000,
            flags=["LIMIT_UP"],
            usd_turnover=50_000_000,
        ),
        _row(
            "SMALL",
            dollar_vol=49_999_999,
            flags=["LIMIT_UP"],
            usd_turnover=49_999_999,
        ),
    ]

    result = run_pipeline(
        rows,
        {"c_limit_usd_min": 50_000_000},
        "open",
    )

    assert [row.ticker for row in result if row.tier == "C"] == ["LARGE"]


def test_daily_limit_uses_recorded_usd_turnover():
    result = run_pipeline(
        [_row("FX", dollar_vol=1_600_000_000, usd_turnover=50_000_000, flags=["LIMIT_UP"])],
        {"c_limit_usd_min": 50_000_000},
        "open",
    )
    assert [row.ticker for row in result if row.tier == "C"] == ["FX"]


def test_daily_limit_falls_back_to_positive_session_fx():
    result = run_pipeline(
        [_row("FX", dollar_vol=1_600_000_000, flags=["LIMIT_UP"])],
        {"c_limit_usd_min": 50_000_000, "fx": 32.0},
        "open",
    )
    assert [row.ticker for row in result if row.tier == "C"] == ["FX"]


def test_daily_limit_without_fx_or_usd_turnover_fails_closed():
    result = run_pipeline(
        [_row("NOFX", dollar_vol=10_000_000_000, flags=["LIMIT_UP"])],
        {"c_limit_usd_min": 50_000_000},
        "open",
    )
    assert not [row for row in result if row.tier == "C"]


def test_limit_up_without_catalyst_stays_c_in_tech_watch_rvol_band():
    rows = [
        _row(
            "LIMITUP",
            chg_pct=10.0,
            dollar_vol=3_000_000_000,
            rvol=0.5,
            flags=["LIMIT_UP"],
            usd_turnover=3_000_000_000,
        ),
        _row(
            "LIQUID",
            chg_pct=3.5,
            dollar_vol=3_000_000_000,
            rvol=0.3,
        ),
    ]

    result = run_pipeline(
        rows,
        {
            "tech_watch_rvol_min": 0.3,
            "tech_watch_rvol_max": 2.0,
            "tech_watch_liquid_turnover_min": 2_500_000_000,
            "tech_watch_move_min": 2.0,
            "c_limit_usd_min": 50_000_000,
        },
        "open",
    )

    tiers = {row.ticker: row.tier for row in result}
    assert tiers["LIMITUP"] == "C"
    assert tiers["LIQUID"] == "TECH_WATCH"
