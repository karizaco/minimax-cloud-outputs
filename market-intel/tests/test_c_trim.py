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
