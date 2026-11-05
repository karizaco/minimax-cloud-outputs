from pathlib import Path

from sip.shadow import run_shadow


FIXTURES = Path(__file__).parent / "fixtures" / "taiwan-2026-11-05-open"


def test_shadow_writes_expected_paths(tmp_path: Path) -> None:
    out_root = tmp_path / "out"
    outside = tmp_path / "outside"
    outside.mkdir()

    paths = run_shadow(
        market="taiwan",
        slot="open",
        date="2026-01-01",
        fixtures_dir=FIXTURES,
        out_root=out_root,
    )

    assert set(paths) == {"json", "md", "chat"}
    assert paths["json"].name.endswith("-open.json")
    assert paths["md"].name.endswith("-open.md")
    assert paths["chat"].name.endswith("-open.chat.md")

    assert paths["json"] == out_root / "2026-01-01-open.json"
    assert paths["md"] == out_root / "2026-01-01-open.md"
    assert paths["chat"] == out_root / "2026-01-01-open.chat.md"

    assert sorted(path.name for path in out_root.iterdir()) == [
        "2026-01-01-open.chat.md",
        "2026-01-01-open.json",
        "2026-01-01-open.md",
    ]
    assert list(outside.iterdir()) == []
