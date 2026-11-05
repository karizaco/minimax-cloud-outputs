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
                catalyst="order",
                rvol=0.8,
            ),
            row(
                "1003",
                chg_pct=6.0,
                dollar_vol=33_000_000.0,
                catalyst="order",
                rvol=None,
            ),
            row(
                "1004",
                chg_pct=6.0,
                dollar_vol=34_000_000.0,
                catalyst="order",
                rvol=2.0,
            ),
        ],
        cfg,
        "open",
    )

    assert isinstance(result, list)
    assert all(isinstance(item, CandidateRow) for item in result)

    by_ticker = {item.ticker: item for item in result}
    assert by_ticker["1001"].tier != "Soft-A"
    assert by_ticker["1002"].tier == "Soft-A"
    assert by_ticker["1003"].tier == "Soft-A"
    assert by_ticker["1004"].tier == "A"
    assert by_ticker["1002"].catalyst == "order"


def test_a_requires_catalyst_elevated_rvol_and_material_move() -> None:
    cfg = load_market("taiwan")

    result = run_pipeline(
        [
            row(
                "2001",
                chg_pct=4.5,
                dollar_vol=31_000_000.0,
                catalyst="news",
                rvol=2.0,
            ),
            row(
                "2002",
                chg_pct=3.9,
                dollar_vol=32_000_000.0,
                catalyst="news",
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
                catalyst="news",
                rvol=1.4,
            ),
        ],
        cfg,
        "open",
    )

    by_ticker = {item.ticker: item for item in result}
    assert by_ticker["2001"].tier == "A"
    assert by_ticker["2002"].tier != "A"
    assert by_ticker["2003"].tier != "A"
    assert by_ticker["2004"].tier != "A"


def test_pipeline_sorts_by_tier_then_dollar_volume_descending() -> None:
    cfg = load_market("taiwan")

    result = run_pipeline(
        [
            row(
                "1001",
                chg_pct=6.0,
                dollar_vol=31_000_000.0,
                catalyst="news",
                rvol=2.0,
            ),
            row(
                "1002",
                chg_pct=6.0,
                dollar_vol=33_000_000.0,
                catalyst="news",
                rvol=2.0,
            ),
            row(
                "1003",
                chg_pct=3.5,
                dollar_vol=32_000_000.0,
                catalyst="order",
                rvol=0.8,
            ),
            row(
                "1004",
                chg_pct=3.5,
                dollar_vol=34_000_000.0,
                catalyst="order",
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
                chg_pct=3.5,
                dollar_vol=32_000_000.0,
                catalyst="order",
                rvol=0.8,
            ),
            row(
                "1003",
                chg_pct=9.0,
                dollar_vol=100.0,
                catalyst="news",
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
