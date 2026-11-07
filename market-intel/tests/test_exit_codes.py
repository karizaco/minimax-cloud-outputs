from __future__ import annotations

from pathlib import Path

import pytest

from sip.cli import main as cli_main
from sip.paths import assert_safe_out_path


def test_unsafe_output_path_exits_with_code_2() -> None:
    with pytest.raises(SystemExit) as exc:
        assert_safe_out_path("/home/box/taiwan-in-play/x")
    assert exc.value.code == 2


def test_unsafe_live_root_rejected() -> None:
    with pytest.raises(SystemExit) as exc:
        assert_safe_out_path("/home/box/taiwan-in-play")
    assert exc.value.code == 2


def test_cli_returns_nonzero_for_missing_input(tmp_path: Path) -> None:
    code = cli_main(
        [
            "shadow",
            "--market",
            "taiwan",
            "--slot",
            "open",
            "--date",
            "2026-11-05",
            "--fixtures",
            str(tmp_path / "missing-fixtures"),
            "--out-root",
            str(tmp_path),
        ]
    )
    assert code != 0
