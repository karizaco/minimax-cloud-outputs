from pathlib import Path

from sip.markets.taiwan.adapter import build_candidates


FIXTURES = Path(__file__).parent / "fixtures" / "taiwan-2026-11-05-open"


def test_build_candidates_from_fixtures() -> None:
    result = build_candidates(fixtures_dir=FIXTURES)

    assert result["candidates"]
    assert result["source_health"]
    assert isinstance(result["meta"], dict)

    first = result["candidates"][0]
    assert first["ticker"]
    assert first["venue"] in {"TWSE", "TPEx"}
    assert first.get("last", first.get("price")) is not None
