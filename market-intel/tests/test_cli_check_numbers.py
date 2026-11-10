from __future__ import annotations

import json
from pathlib import Path

from sip.cli import main


def test_cli_passes_fx_rate_to_number_trace(tmp_path: Path) -> None:
    run_path = tmp_path / "run.json"
    chat_path = tmp_path / "chat.md"
    run_path.write_text(json.dumps({"date": "2026-11-10"}), encoding="utf-8")
    chat_path.write_text("匯率 32.780875", encoding="utf-8")

    code = main(
        [
            "check-numbers",
            "--run",
            str(run_path),
            "--chat",
            str(chat_path),
            "--fx",
            "32.780875",
        ]
    )

    assert code == 0
