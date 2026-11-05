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
    }


def test_limit_down_with_material_is_soft_a_never_a() -> None:
    row = CandidateRow(
        ticker="2467",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-9.9,
        dollar_vol=80_000_000.0,
        rvol=0.8,
        catalyst="股份交換案擬增資發行新股",
        catalyst_time="09:30",
        flags=["LIMIT_DOWN"],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
        mops_materiality=2,
    )
    result = run_pipeline([row], _cfg(), "open")
    assert result[0].tier == "Soft-A"


def test_limit_down_without_catalyst_not_a_or_soft_a() -> None:
    row = CandidateRow(
        ticker="9999",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-9.9,
        dollar_vol=80_000_000.0,
        rvol=0.5,
        catalyst=None,
        catalyst_time=None,
        flags=["LIMIT_DOWN"],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
    )
    result = run_pipeline([row], _cfg(), "open")
    assert result[0].tier in {"TECH_WATCH", "C"}
    assert result[0].tier not in {"A", "Soft-A"}
