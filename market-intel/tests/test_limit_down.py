from __future__ import annotations

from sip.schema import CandidateRow
from sip.tier import run_pipeline


def _cfg():
    return {
        "open": {"floors": {"price_min": 0, "turnover_min": 0, "mcap_min": 0}},
        "day_move_hard": 5.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
        "tech_watch_rvol_min": 1.0,
        "tech_watch_rvol_max": 2.0,
        "soft_a_requires_catalyst": True,
        "catalyst_min_score": 1,
    }


def _row(**kwargs) -> CandidateRow:
    base = dict(
        ticker="9999",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-9.9,
        dollar_vol=80_000_000.0,
        rvol=0.8,
        catalyst=None,
        catalyst_time=None,
        flags=["LIMIT_DOWN"],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
        tier=None,
        mops_materiality=None,
    )
    base.update(kwargs)
    return CandidateRow(**base)


def test_limit_down_with_material_is_c_never_soft_a_or_a() -> None:
    result = run_pipeline(
        [
            _row(
                ticker="2467",
                catalyst="股份交換案擬增資發行新股",
                catalyst_time="09:30",
                rvol=0.8,
                mops_materiality=2,
            )
        ],
        _cfg(),
        "open",
    )
    assert result[0].tier == "C"


def test_limit_down_without_catalyst_is_c() -> None:
    result = run_pipeline([_row(rvol=0.5)], _cfg(), "open")
    assert result[0].tier == "C"


def test_limit_down_never_a_or_soft_a_or_tech_watch() -> None:
    for rvol in (None, 0.5, 1.2, 2.5):
        result = run_pipeline(
            [
                _row(
                    catalyst="Q3 EPS / 合併財務報告",
                    mops_materiality=2,
                    rvol=rvol,
                    chg_pct=-9.9,
                )
            ],
            _cfg(),
            "open",
        )
        assert result[0].tier == "C"
        assert result[0].tier not in {"A", "Soft-A", "TECH_WATCH"}
