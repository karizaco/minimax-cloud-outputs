from __future__ import annotations

from sip.shadow import _candidate_count


def test_candidate_count_uses_cmoney_raw_universe_count() -> None:
    source_health = [
        {"source": "cmoney", "status": "ok", "count": 565},
        {"source": "schema", "status": "ok", "count": 3},
    ]

    assert _candidate_count(source_health) == 565


def test_candidate_count_does_not_use_generic_source_count() -> None:
    source_health = [
        {"source": "other", "status": "ok", "count": 42},
        {"source": "schema", "status": "ok", "count": 3},
    ]

    assert _candidate_count(source_health) is None
