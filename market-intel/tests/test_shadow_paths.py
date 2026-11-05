from __future__ import annotations

from pathlib import Path

import pytest

from sip.paths import assert_safe_out_path
from sip.shadow import run_shadow


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "taiwan-2026-11-05-open"


def test_run_shadow_returns_paths_and_code(tmp_path: Path) -> None:
    paths, code = run_shadow(
        "taiwan",
        "open",
        "2026-11-05",
        FIXTURES,
        out_root=tmp_path,
    )
    assert isinstance(paths, dict)
    assert isinstance(code, int)
    assert code == 0
    assert all(isinstance(path, Path) for path in paths.values())
    for path in paths.values():
        assert path.exists()
        assert tmp_path in path.parents or path.parent == tmp_path


def test_rejects_live_taiwan_in_play_root() -> None:
    with pytest.raises(SystemExit) as exc:
        assert_safe_out_path("/home/box/taiwan-in-play")
    assert exc.value.code == 2
