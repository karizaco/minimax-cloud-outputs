from __future__ import annotations

import json
from pathlib import Path

from sip.cli import main


def _write_run_and_chat(tmp_path: Path, run: dict, chat: str) -> tuple[Path, Path]:
    run_path = tmp_path / "run.json"
    chat_path = tmp_path / "chat.md"
    run_path.write_text(json.dumps(run), encoding="utf-8")
    chat_path.write_text(chat, encoding="utf-8")
    return run_path, chat_path


def test_cli_passes_explicit_fx_rate_to_number_trace(tmp_path: Path) -> None:
    run_path, chat_path = _write_run_and_chat(
        tmp_path,
        {"date": "2026-11-10"},
        "匯率 32.780875",
    )

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


def test_cli_without_fx_uses_verified_run_fx(tmp_path: Path) -> None:
    run_path, chat_path = _write_run_and_chat(
        tmp_path,
        {"fx": 32.780875},
        "匯率 32.780875",
    )

    code = main(
        [
            "check-numbers",
            "--run",
            str(run_path),
            "--chat",
            str(chat_path),
        ]
    )

    assert code == 0


def test_cli_without_fx_does_not_inject_default_fx(tmp_path: Path) -> None:
    run_path, chat_path = _write_run_and_chat(
        tmp_path,
        {"fx": 32.780875},
        "匯率 32.824",
    )

    code = main(
        [
            "check-numbers",
            "--run",
            str(run_path),
            "--chat",
            str(chat_path),
        ]
    )

    assert code == 5


def test_cli_without_fx_and_without_run_fx_does_not_inject_default(tmp_path: Path) -> None:
    run_path, chat_path = _write_run_and_chat(
        tmp_path,
        {"date": "2026-11-10"},
        "匯率 32.824",
    )

    code = main(
        [
            "check-numbers",
            "--run",
            str(run_path),
            "--chat",
            str(chat_path),
        ]
    )

    assert code == 5
