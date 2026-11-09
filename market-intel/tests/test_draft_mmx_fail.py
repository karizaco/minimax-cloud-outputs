from __future__ import annotations

import json
from pathlib import Path

import pytest

from sip.draft_mmx import draft_chat


def test_draft_chat_returns_nonzero_when_mmx_fails(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    run_json = tmp_path / "run.json"
    run_json.write_text(
        json.dumps(
            {
                "date": "2026-11-05",
                "slot": "AM",
                "rows": [],
                "candidates": [],
            }
        ),
        encoding="utf-8",
    )
    out_chat = tmp_path / "x.chat.md"

    def fail_run(*args: object, **kwargs: object) -> None:
        raise RuntimeError("mmx failed")

    monkeypatch.setattr("subprocess.run", fail_run)

    exit_code = draft_chat(run_json, out_chat)

    assert exit_code != 0
