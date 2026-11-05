from __future__ import annotations

import json
from pathlib import Path

from sip.number_trace import check_chat


def _run(*, last: float = 100.0, chg_pct: float = 5.0) -> dict:
    return {
        "date": "2026-11-05",
        "slot": "open",
        "candidates": [
            {
                "ticker": "2330",
                "venue": "TWSE",
                "instrument_type": "common",
                "last": last,
                "chg_pct": chg_pct,
                "dollar_vol": 50_000_000.0,
                "rvol": 1.2,
                "catalyst": None,
                "flags": [],
                "source": "test",
                "asof": "2026-11-05T09:30:00+08:00",
                "tier": "B",
            }
        ],
    }


def test_signed_change_is_accepted() -> None:
    result = check_chat(_run(chg_pct=2.5), "# Picks\n\n- 2330: +2.5%\n")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_negative_percent_does_not_match_positive() -> None:
    result = check_chat(_run(chg_pct=5.0), "# Picks\n\n- 2330: -5%\n")
    assert result["ok"] is False
    assert result["offenders"]


def test_garbage_number_is_rejected() -> None:
    chat = "99.9% on US$777m, 12.3x, 1,234.5"
    result = check_chat(_run(last=100.0, chg_pct=1.0), chat)
    assert result["ok"] is False
    assert len(result["offenders"]) >= 3
