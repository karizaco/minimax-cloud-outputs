from __future__ import annotations

import json
from pathlib import Path

import pytest

from sip.draft_mmx import _normalize_rvol_draft, draft_chat


def test_draft_chat_returns_nonzero_when_mmx_fails(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    run_json = tmp_path / "run.json"
    run_json.write_text(json.dumps({"date": "2026-11-05", "slot": "AM",
                                    "rows": [], "candidates": []}),
                        encoding="utf-8")
    out_chat = tmp_path / "x.chat.md"

    def fail_run(*args: object, **kwargs: object) -> None:
        raise RuntimeError("mmx failed")

    monkeypatch.setattr("subprocess.run", fail_run)
    assert draft_chat(run_json, out_chat) != 0


def test_failed_draft_body_and_usage_are_retained(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    run_json = tmp_path / "run.json"
    run_json.write_text(json.dumps({"date": "2026-11-05", "slot": "AM",
                                    "candidates": [{"ticker": "2330",
                                                    "last": 100.0,
                                                    "rvol": 1.2,
                                                    "chg_pct": 1.0}]}),
                        encoding="utf-8")
    out_chat = tmp_path / "x.chat.md"
    out_chat.write_text("deterministic chat\n", encoding="utf-8")
    mmx = tmp_path / "mmx.py"
    mmx.write_text("", encoding="utf-8")

    def fake_run(command: list[str], **kwargs: object):
        generated = Path(command[command.index("--out") + 1])
        generated.write_text("RelVol 5.01\n", encoding="utf-8")
        return type("Completed", (), {
            "returncode": 0,
            "stdout": '{"tokens_out": 17, "lane": "bulk", "model": "test"}\n',
            "stderr": "",
        })()

    monkeypatch.setattr("subprocess.run", fake_run)
    assert draft_chat(run_json, out_chat, mmx_bin=mmx) == 5
    assert out_chat.read_text(encoding="utf-8") == "deterministic chat\n"
    assert "RelVol 5.01" in (tmp_path / "x.chat.md.failed.md").read_text(encoding="utf-8")
    meta = json.loads((tmp_path / "x.chat.md.failed.meta.json").read_text(encoding="utf-8"))
    assert meta["tokens_out"] == 17


def test_bare_chinese_rvol_is_normalized_and_published(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    run_json = tmp_path / "run.json"
    run_json.write_text(json.dumps({"date": "2026-11-05", "slot": "AM",
                                    "candidates": [{"ticker": "2330",
                                                    "last": 100.0,
                                                    "rvol": 5.009524452716406,
                                                    "chg_pct": 1.0}]}),
                        encoding="utf-8")
    out_chat = tmp_path / "x.chat.md"
    mmx = tmp_path / "mmx.py"
    mmx.write_text("", encoding="utf-8")

    def fake_run(command: list[str], **kwargs: object):
        generated = Path(command[command.index("--out") + 1])
        generated.write_text("相對成交量 **5.01**\n", encoding="utf-8")
        return type("Completed", (), {"returncode": 0, "stdout": "", "stderr": ""})()

    monkeypatch.setattr("subprocess.run", fake_run)
    assert draft_chat(run_json, out_chat, mmx_bin=mmx) == 0
    published = out_chat.read_text(encoding="utf-8")
    assert "5.0x" in published or "5.01x" in published
    assert "5.01" not in published

def _rvol_run_data() -> dict:
    return {"candidates": [{"ticker": "2330", "rvol": 5.009524452716406}]}


def test_rvol_normalizer_leaves_unit_bearing_tokens_unchanged() -> None:
    run_data = _rvol_run_data()
    for content in (
        "RelVol 5.01x",
        "RelVol5.01x",
        "RelVol 5.01%",
        "成長 5.01%",
    ):
        assert _normalize_rvol_draft(content, run_data) == content


def test_rvol_normalizer_rewrites_only_grounded_bare_tokens() -> None:
    run_data = _rvol_run_data()
    assert _normalize_rvol_draft("RelVol 5.01", run_data) == "RelVol 5.0x"
    assert _normalize_rvol_draft("RelVol 5.01 and 99.9%", run_data) == "RelVol 5.0x and 99.9%"

    normalized = _normalize_rvol_draft("相對成交量 **5.01**", run_data)
    assert normalized == "相對成交量 **5.0x**"
    assert "**5.0x****" not in normalized


def test_draft_chat_does_not_publish_when_other_offender_remains(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    run_json = tmp_path / "run.json"
    run_json.write_text(json.dumps({"date": "2026-11-05", "slot": "AM",
                                    "candidates": [{"ticker": "2330",
                                                    "last": 100.0,
                                                    "rvol": 5.009524452716406,
                                                    "chg_pct": 1.0}]}),
                        encoding="utf-8")
    out_chat = tmp_path / "x.chat.md"
    out_chat.write_text("deterministic chat\n", encoding="utf-8")
    mmx = tmp_path / "mmx.py"
    mmx.write_text("", encoding="utf-8")

    def fake_run(command: list[str], **kwargs: object):
        generated = Path(command[command.index("--out") + 1])
        generated.write_text("RelVol 5.01x and 99.9%\n", encoding="utf-8")
        return type("Completed", (), {"returncode": 0, "stdout": "", "stderr": ""})()

    monkeypatch.setattr("subprocess.run", fake_run)
    assert draft_chat(run_json, out_chat, mmx_bin=mmx) == 5
    assert out_chat.read_text(encoding="utf-8") == "deterministic chat\n"
    failed = (tmp_path / "x.chat.md.failed.md").read_text(encoding="utf-8")
    assert "RelVol 5.01x" in failed
    assert "99.9%" in failed
