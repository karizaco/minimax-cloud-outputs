from sip.schema import CandidateRow, validate_row


def make_row() -> CandidateRow:
    return CandidateRow(
        ticker="2330",
        venue="TWSE",
        instrument_type="common",
        last=1050.0,
        chg_pct=2.5,
        dollar_vol=1_250_000_000.0,
        rvol=1.8,
        catalyst="AI demand",
        catalyst_time="09:30",
        flags=["active"],
        source="test",
        asof="2026-01-01T09:35:00+08:00",
        tier="A",
        company_en="Taiwan Semiconductor Manufacturing Co.",
        company_zh="台積電",
        board="TWSE",
        mcap_twd=27_000_000_000_000.0,
        usd_turnover=38_000_000.0,
        display_ticker="2330",
        why="Momentum with institutional participation",
    )


def test_candidate_row_roundtrip() -> None:
    row = make_row()
    data = row.asdict()

    restored = CandidateRow.from_dict(data)

    assert restored == row
    assert restored.asdict() == data


def test_candidate_row_uses_real_schema_fields() -> None:
    row = make_row()

    validate_row(row)

    assert row.ticker == "2330"
    assert row.venue == "TWSE"
    assert row.instrument_type == "common"
    assert row.last == 1050.0
    assert row.chg_pct == 2.5
    assert row.dollar_vol == 1_250_000_000.0
    assert row.rvol == 1.8
