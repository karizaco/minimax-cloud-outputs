from __future__ import annotations

from sip.format_taiwan import render_digest


def test_render_digest_respects_digest_top_n() -> None:
    rows = [
        {
            "ticker": str(1000 + i),
            "venue": "TWSE",
            "tier": "TECH_WATCH",
            "last": 10,
            "chg_pct": -4.0,
            "rvol": 1.1,
            "dollar_vol": 50_000_000 - i,
            "catalyst": None,
            "company_en": f"Co{i}",
        }
        for i in range(20)
    ]
    md = render_digest(
        {"date": "2026-11-05", "slot": "open", "candidates": rows, "fx": 32.0},
        top_n={"TECH_WATCH": 8, "A": 10, "Soft-A": 10, "B": 10, "C": 5},
    )
    # header + sep + 8 data rows under TECH_WATCH
    section = md.split("## TECH_WATCH")[1].split("## ")[0]
    data_rows = [ln for ln in section.splitlines() if ln.startswith("|") and "Ticker" not in ln and "---" not in ln]
    assert len(data_rows) == 8
