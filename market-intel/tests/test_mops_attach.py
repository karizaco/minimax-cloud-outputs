import json
from pathlib import Path

from sip.config import load_market
from sip.markets.taiwan.adapter import build_candidates
from sip.markets.taiwan.parse import parse_twse_ap04
from sip.shadow import _candidate_to_row
from sip.tier import run_pipeline


def _write_fixtures(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)

    cands = [
        {
            "ticker": "3019",
            "name": "Soft mover",
            "board": "TWSE",
            "price": 100.0,
            "chg": 6.0,
            "rv": 0.8,
            "turn": 40_000_000,
        },
        {
            "ticker": "1815",
            "name": "Elevated mover",
            "board": "TWSE",
            "price": 100.0,
            "chg": 6.0,
            "rv": 2.0,
            "turn": 40_000_000,
        },
    ]
    mops = {
        "items": [
            {
                "ticker": "3019",
                "headline": "Major acquisition announcement",
                "time": "09:15",
            },
            {
                "ticker": "1815",
                "headline": "Quarterly earnings release",
                "time": "09:20",
            },
        ]
    }

    (directory / "cands.json").write_text(
        json.dumps(cands),
        encoding="utf-8",
    )
    (directory / "mops_items.json").write_text(
        json.dumps(mops),
        encoding="utf-8",
    )


def _write_mover(directory: Path, ticker: str = "6538") -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "cands.json").write_text(
        json.dumps(
            [
                {
                    "ticker": ticker,
                    "name": "Test mover",
                    "price": 100,
                    "chg": 6.1,
                    "rv": 1.2,
                    "turn": 40_000_000,
                }
            ]
        ),
        encoding="utf-8",
    )


def test_mops_catalysts_are_attached_and_tiered(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_fixtures(fixtures)

    result = build_candidates(fixtures, slot="open")

    candidates = {item["ticker"]: item for item in result["candidates"]}
    assert candidates["3019"]["catalyst"] == "Major acquisition announcement"
    assert candidates["1815"]["catalyst"] == "Quarterly earnings release"
    assert candidates["3019"]["catalyst_time"] == "09:15"
    assert candidates["1815"]["catalyst_time"] == "09:20"

    cfg = load_market("taiwan")
    rows = [_candidate_to_row(c) for c in result["candidates"]]
    tiered = run_pipeline(rows, cfg, "open")
    by_ticker = {item.ticker: item for item in tiered}

    assert by_ticker["3019"].tier == "Soft-A"
    assert by_ticker["1815"].tier == "A"
    assert by_ticker["3019"].catalyst == "Major acquisition announcement"
    assert by_ticker["1815"].catalyst == "Quarterly earnings release"


def test_missing_mops_is_coverage_failed(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    fixtures.mkdir()
    (fixtures / "cands.json").write_text(
        json.dumps(
            [
                {
                    "ticker": "6538",
                    "name": "倉和",
                    "price": 100,
                    "chg": 6.1,
                    "rv": 1.2,
                    "turn": 40_000_000,
                }
            ]
        ),
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    mops_health = next(
        item for item in result["source_health"] if item["source"] == "mops"
    )
    assert mops_health["status"] in {"coverage_failed", "missing"}
    assert "mops_items.json" in mops_health["detail"]
    assert "mops-browser.txt" in mops_health["detail"]
    assert "twse-ap04.json" in mops_health["detail"]


def test_mops_browser_text_is_discovered_and_attached(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_mover(fixtures)
    (fixtures / "mops-browser.txt").write_text(
        "11/06 17:47 | 6538 | 倉和 | 公告本公司董事會通過民國115年度第3季合併財務報告\n",
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    candidate = next(item for item in result["candidates"] if item["ticker"] == "6538")
    assert candidate["catalyst"] == "公告本公司董事會通過民國115年度第3季合併財務報告"
    assert candidate["catalyst_time"] == "11/06 17:47"
    mops_health = next(
        item for item in result["source_health"] if item["source"] == "mops"
    )
    assert mops_health["status"] == "ok"
    assert mops_health["count"] == 1


def test_twse_ap04_trailing_space_keys_and_readable_time(tmp_path: Path) -> None:
    payload = [
        {
            "發言日期": "1151109",
            "發言時間": "163201",
            "公司代號": "2308",
            "公司名稱": "台達電",
            "主旨 ": "發布本公司115年10月份業績資料",
            "說明": "補充說明",
        }
    ]
    rows = parse_twse_ap04(payload)
    assert rows[0]["ticker"] == "2308"
    assert rows[0]["headline"] == "發布本公司115年10月份業績資料"
    assert rows[0]["catalyst_time"] == "11/09 16:32"


def test_twse_ap04_material_headline_is_attached(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_mover(fixtures, "2308")
    (fixtures / "twse-ap04.json").write_text(
        json.dumps(
            [
                {
                    "發言日期": "1151109",
                    "發言時間": "163201",
                    "公司代號": "2308",
                    "公司名稱": "台達電",
                    "主旨 ": "公告115年第三季營收及重大收購案",
                }
            ]
        ),
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    candidate = next(item for item in result["candidates"] if item["ticker"] == "2308")
    assert candidate["catalyst"] == "公告115年第三季營收及重大收購案"
    assert candidate["catalyst_time"] == "11/09 16:32"


def test_mops1_shell_only_is_coverage_failed(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_mover(fixtures)
    (fixtures / "mops1.html").write_text(
        '<html><body><form><div id="table01"></div></form></body></html>',
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    health = next(item for item in result["source_health"] if item["source"] == "mops")
    assert health["status"] == "coverage_failed"
    assert health.get("count", 0) == 0


def test_mops1_shell_does_not_hide_twse_ap04_coverage(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_mover(fixtures, "2308")
    (fixtures / "mops1.html").write_text(
        '<html><body><div id="table01"></div></body></html>',
        encoding="utf-8",
    )
    (fixtures / "twse-ap04.json").write_text(
        json.dumps(
            [
                {
                    "發言日期": "1151110",
                    "發言時間": "090000",
                    "公司代號": "2308",
                    "主旨 ": "公告本公司營收資料",
                }
            ]
        ),
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    health = next(item for item in result["source_health"] if item["source"] == "mops")
    assert health["status"] == "ok"
    assert health["count"] == 1


def test_mops1_real_rows_are_accepted_and_attached(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    _write_mover(fixtures)
    (fixtures / "mops1.html").write_text(
        """<table>
        <tr><th>公司代號</th><th>主旨</th></tr>
        <tr><td>6538</td><td>公告重大收購案</td></tr>
        </table>""",
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    candidate = next(item for item in result["candidates"] if item["ticker"] == "6538")
    assert candidate["catalyst"] == "公告重大收購案"
    health = next(item for item in result["source_health"] if item["source"] == "mops")
    assert health["status"] == "ok"
    assert health["count"] == 1


def test_mops_browser_and_twse_ap04_are_merged(tmp_path: Path) -> None:
    fixtures = tmp_path / "fixtures"
    fixtures.mkdir()
    (fixtures / "cands.json").write_text(
        json.dumps(
            [
                {"ticker": "6538", "price": 100, "chg": 6.1, "rv": 1.2, "turn": 40_000_000},
                {"ticker": "2308", "price": 100, "chg": 6.1, "rv": 1.2, "turn": 40_000_000},
            ]
        ),
        encoding="utf-8",
    )
    (fixtures / "mops-browser.txt").write_text(
        "11/06 17:47 | 6538 | 倉和 | 公告董事會通過收購案\n",
        encoding="utf-8",
    )
    (fixtures / "twse-ap04.json").write_text(
        json.dumps(
            [
                {
                    "發言日期": "1151110",
                    "發言時間": "090000",
                    "公司代號": "2308",
                    "主旨 ": "公告本公司營收資料",
                }
            ]
        ),
        encoding="utf-8",
    )

    result = build_candidates(fixtures, slot="open")
    candidates = {item["ticker"]: item for item in result["candidates"]}
    assert candidates["6538"]["catalyst"] == "公告董事會通過收購案"
    assert candidates["2308"]["catalyst"] == "公告本公司營收資料"
    health = next(item for item in result["source_health"] if item["source"] == "mops")
    assert health["status"] == "ok"
    assert health["count"] == 2
