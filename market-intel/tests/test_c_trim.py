from sip.tier import run_pipeline


def test_large_c_residual_pool_is_trimmed():
    rows = []
    for i in range(288):
        rows.append(
            {
                "ticker": str(i),
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
        )
    rows[0]["flags"] = ["LIMIT_UP"]
    result = run_pipeline(
        rows,
        {"digest_top_n": {"C": 5}, "engine_top_n": {"C": 5}},
        "open",
    )
    c_rows = [row for row in result if row.tier == "C"]
    assert len(c_rows) <= 5
    assert {row.ticker for row in c_rows} == {"0"}
    assert any(row.ticker == "0" for row in result)


def test_limit_up_c_is_kept_and_residual_c_is_dropped():
    rows = [
        {
            "ticker": "6538",
            "venue": "TWSE",
            "instrument_type": "common",
            "last": 100,
            "chg_pct": 1.0,
            "dollar_vol": 50_000_000,
            "rvol": 0.5,
            "catalyst": None,
            "catalyst_time": None,
            "flags": ["LIMIT_UP"],
            "source": "test",
            "asof": "2026-11-09",
            "tier": None,
        },
        {
            "ticker": "9999",
            "venue": "TWSE",
            "instrument_type": "common",
            "last": 100,
            "chg_pct": 1.0,
            "dollar_vol": 40_000_000,
            "rvol": 0.5,
            "catalyst": None,
            "catalyst_time": None,
            "flags": [],
            "source": "test",
            "asof": "2026-11-09",
            "tier": None,
        },
    ]
    result = run_pipeline(
        rows,
        {"digest_top_n": {"C": 5}, "engine_top_n": {"C": 5}},
        "open",
    )
    assert [row.ticker for row in result if row.tier == "C"] == ["6538"]


def test_material_c_cap_is_applied_by_dollar_volume():
    rows = []
    for i in range(8):
        rows.append(
            {
                "ticker": str(i),
                "venue": "TWSE",
                "instrument_type": "common",
                "last": 100,
                "chg_pct": 1.0,
                "dollar_vol": 10_000_000 + i,
                "rvol": 0.5,
                "catalyst": None,
                "catalyst_time": None,
                "flags": ["LIMIT_UP"],
                "source": "test",
                "asof": "2026-11-09",
                "tier": None,
            }
        )
    result = run_pipeline(
        rows,
        {"digest_top_n": {"C": 8}, "engine_top_n": {"C": 3}},
        "open",
    )
    c_rows = [row for row in result if row.tier == "C"]
    assert len(c_rows) == 3
    assert {row.ticker for row in c_rows} == {"5", "6", "7"}


def test_limit_up_without_catalyst_stays_c_in_tech_watch_rvol_band():
    rows = [
        {
            "ticker": "LIMITUP",
            "venue": "TWSE",
            "instrument_type": "common",
            "last": 100,
            "chg_pct": 10.0,
            "dollar_vol": 3_000_000_000,
            "rvol": 0.5,
            "catalyst": None,
            "catalyst_time": None,
            "flags": ["LIMIT_UP"],
            "source": "test",
            "asof": "2026-11-09",
            "tier": None,
        },
        {
            "ticker": "LIQUID",
            "venue": "TWSE",
            "instrument_type": "common",
            "last": 100,
            "chg_pct": 3.5,
            "dollar_vol": 3_000_000_000,
            "rvol": 0.3,
            "catalyst": None,
            "catalyst_time": None,
            "flags": [],
            "source": "test",
            "asof": "2026-11-09",
            "tier": None,
        },
    ]

    result = run_pipeline(
        rows,
        {
            "tech_watch_rvol_min": 0.3,
            "tech_watch_rvol_max": 2.0,
            "tech_watch_liquid_turnover_min": 2_500_000_000,
            "tech_watch_move_min": 2.0,
            "digest_top_n": {"C": 8},
            "engine_top_n": {"C": 8},
        },
        "open",
    )

    tiers = {row.ticker: row.tier for row in result}
    assert tiers["LIMITUP"] == "C"
    assert tiers["LIQUID"] == "TECH_WATCH"
