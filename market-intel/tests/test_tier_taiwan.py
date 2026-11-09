from sip.config import load_market
from sip.schema import CandidateRow, TIER_ORDER
from sip.tier import run_pipeline


def row(
    ticker: str,
    *,
    chg_pct: float,
    dollar_vol: float,
    catalyst: str | None,
    rvol: float | None = 2.0,
    tier: str | None = None,
    mops_materiality: int | None = None,
) -> CandidateRow:
    return CandidateRow(
        ticker=ticker,
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=chg_pct,
        dollar_vol=dollar_vol,
        rvol=rvol,
        catalyst=catalyst,
        catalyst_time="09:30" if catalyst else None,
        flags=[],
        source="test",
        asof="2026-01-01T09:35:00+08:00",
        tier=tier,
        mops_materiality=mops_materiality,
    )


def test_soft_a_requires_catalyst_and_soft_rvol() -> None:
    cfg = load_market("taiwan")

    result = run_pipeline(
        [
            row(
                "1001",
                chg_pct=6.0,
                dollar_vol=31_000_000.0,
                catalyst=None,
                rvol=0.8,
            ),
            row(
                "1002",
                chg_pct=6.0,
                dollar_vol=32_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=0.8,
            ),
            row(
                "1003",
                chg_pct=6.0,
                dollar_vol=33_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=None,
            ),
            row(
                "1004",
                chg_pct=6.0,
                dollar_vol=34_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
        ],
        cfg,
        "open",
    )

    assert isinstance(result, list)
    assert all(isinstance(item, CandidateRow) for item in result)

    by_ticker = {item.ticker: item for item in result}
    assert "1001" not in by_ticker or by_ticker["1001"].tier != "Soft-A"
    assert by_ticker["1002"].tier == "Soft-A"
    assert by_ticker["1003"].tier == "Soft-A"
    assert by_ticker["1004"].tier == "A"
    assert "Q3" in (by_ticker["1002"].catalyst or "")


def test_a_requires_catalyst_elevated_rvol_and_material_move() -> None:
    cfg = load_market("taiwan")

    result = run_pipeline(
        [
            row(
                "2001",
                chg_pct=4.5,
                dollar_vol=31_000_000.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
            row(
                "2002",
                chg_pct=3.9,
                dollar_vol=32_000_000.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
            row(
                "2003",
                chg_pct=4.5,
                dollar_vol=33_000_000.0,
                catalyst=None,
                rvol=2.0,
            ),
            row(
                "2004",
                chg_pct=4.5,
                dollar_vol=34_000_000.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=1.4,
            ),
        ],
        cfg,
        "open",
    )

    by_ticker = {item.ticker: item for item in result}
    assert by_ticker["2001"].tier == "A"
    assert "2002" not in by_ticker or by_ticker["2002"].tier != "A"
    assert "2003" not in by_ticker or by_ticker["2003"].tier != "A"
    assert "2004" not in by_ticker or by_ticker["2004"].tier != "A"


def test_soft_a_hard_move_floor_and_limit_up_buyback() -> None:
    cfg = load_market("taiwan")
    catalyst = "Q3 EPS / 合併財務報告"

    below = run_pipeline(
        [row("2101", chg_pct=3.9, dollar_vol=31_000_000.0, catalyst=catalyst, mops_materiality=2, rvol=0.5)],
        cfg,
        "open",
    )
    assert all(item.tier != "Soft-A" for item in below)

    at_floor = run_pipeline(
        [row("2102", chg_pct=4.0, dollar_vol=31_000_000.0, catalyst=catalyst, mops_materiality=2, rvol=0.5)],
        cfg,
        "open",
    )
    assert at_floor[0].tier == "Soft-A"

    limit_up = run_pipeline(
        [row("2103", chg_pct=9.5, dollar_vol=31_000_000.0, catalyst="庫藏股買回", mops_materiality=1, rvol=0.5)],
        cfg,
        "open",
    )
    assert limit_up[0].tier == "Soft-A"


def test_liquid_tech_watch_band_and_move_floor() -> None:
    cfg = load_market("taiwan")

    liquid = run_pipeline(
        [
            row(
                "2201",
                chg_pct=3.5,
                dollar_vol=2_870_000_000,
                catalyst=None,
                rvol=0.307,
            )
        ],
        cfg,
        "open",
    )
    assert liquid[0].tier == "TECH_WATCH"

    below_rvol = run_pipeline(
        [
            row(
                "2202",
                chg_pct=3.5,
                dollar_vol=2_870_000_000,
                catalyst=None,
                rvol=0.25,
            )
        ],
        cfg,
        "open",
    )
    assert all(item.tier != "TECH_WATCH" for item in below_rvol)

    thin = run_pipeline(
        [
            row(
                "2203",
                chg_pct=2.4,
                dollar_vol=2_499_999_999,
                catalyst=None,
                rvol=0.3,
            )
        ],
        cfg,
        "open",
    )
    assert all(item.tier != "TECH_WATCH" for item in thin)

    above_band = run_pipeline(
        [
            row(
                "2204",
                chg_pct=3.5,
                dollar_vol=2_870_000_000,
                catalyst=None,
                rvol=2.0,
            )
        ],
        cfg,
        "open",
    )
    assert above_band[0].tier == "B"


def test_pipeline_sorts_by_tier_then_dollar_volume_descending() -> None:
    cfg = load_market("taiwan")

    result = run_pipeline(
        [
            row(
                "1001",
                chg_pct=6.0,
                dollar_vol=31_000_000.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
            row(
                "1002",
                chg_pct=6.0,
                dollar_vol=33_000_000.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
            row(
                "1003",
                chg_pct=3.5,
                dollar_vol=32_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=0.8,
            ),
            row(
                "1004",
                chg_pct=3.5,
                dollar_vol=34_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=0.8,
            ),
        ],
        cfg,
        "open",
    )

    tier_order = {name: index for index, name in enumerate(TIER_ORDER)}
    expected = sorted(
        result,
        key=lambda item: (
            tier_order.get(item.tier or "C", len(tier_order)),
            -item.dollar_vol,
        ),
    )
    assert result == expected

    for tier in {item.tier for item in result if item.tier}:
        tier_rows = [item for item in result if item.tier == tier]
        volumes = [item.dollar_vol for item in tier_rows]
        assert volumes == sorted(volumes, reverse=True)


def test_pipeline_drops_rows_below_floors() -> None:
    cfg = load_market("taiwan")
    cfg["open"]["floors"]["price_min"] = 50.0
    cfg["open"]["floors"]["turnover_min"] = 1_000_000.0

    result = run_pipeline(
        [
            row(
                "1001",
                chg_pct=6.0,
                dollar_vol=31_000_000.0,
                catalyst=None,
                rvol=0.8,
            ),
            row(
                "1002",
                chg_pct=5.0,
                dollar_vol=32_000_000.0,
                catalyst="Q3 EPS beat / 合併財務報告",
                mops_materiality=2,
                rvol=0.8,
            ),
            row(
                "1003",
                chg_pct=9.0,
                dollar_vol=100.0,
                catalyst="Q3 EPS / 合併財務報告",
                mops_materiality=2,
                rvol=2.0,
            ),
        ],
        cfg,
        "open",
    )

    assert isinstance(result, list)
    assert result
    assert all(item.last >= 50.0 for item in result)
    assert all(item.dollar_vol >= 1_000_000.0 for item in result)
    assert "1003" not in {item.ticker for item in result}
    assert any(item.tier != "C" for item in result)
