from __future__ import annotations

from sip.config import load_market
from sip.format_taiwan import render_digest


def _rows(tier: str, count: int):
    return [
        {
            "ticker": f"{tier}{i}",
            "venue": "TWSE",
            "tier": tier,
            "last": 10,
            "chg_pct": -4.0,
            "rvol": 1.1,
            "dollar_vol": 100_000_000 - i,
            "catalyst": None,
            "company_en": f"Co{i}",
        }
        for i in range(count)
    ]


def _section_rows(markdown: str, heading: str):
    section = markdown.split(f"## {heading}")[1].split("## ")[0]
    return [
        line
        for line in section.splitlines()
        if line.startswith("|")
        and "Ticker" not in line
        and "---" not in line
    ]


def test_render_digest_respects_digest_top_n() -> None:
    rows = _rows("TECH_WATCH", 20)
    md = render_digest(
        {"date": "2026-11-05", "slot": "open", "candidates": rows, "fx": 32.0},
        top_n={"TECH_WATCH": 8, "A": 10, "Soft-A": 10, "B": 10, "C": 5},
    )
    assert len(_section_rows(md, "TECH_WATCH")) == 8


def test_default_digest_tech_watch_cap_is_ten() -> None:
    cfg = load_market("taiwan")
    rows = _rows("TECH_WATCH", 20)
    md = render_digest(
        {"date": "2026-11-05", "slot": "open", "candidates": rows, "fx": 32.0},
        top_n=cfg["digest_top_n"],
    )
    assert len(_section_rows(md, "TECH_WATCH")) == 10


def test_chat_soft_a_cap_matches_digest_cap() -> None:
    cfg = load_market("taiwan")
    assert cfg["digest_top_n"]["Soft-A"] == 8
    assert cfg["chat_top_n"]["Soft-A"] == 8


def test_c_render_lists_all_rows_when_no_count_cap_is_supplied() -> None:
    rows = _rows("C", 12)
    md = render_digest(
        {"date": "2026-11-05", "slot": "open", "candidates": rows, "fx": 32.0},
        top_n={"A": 10, "Soft-A": 8, "TECH_WATCH": 10, "B": 10},
    )
    assert len(_section_rows(md, "Tier C")) == 12
