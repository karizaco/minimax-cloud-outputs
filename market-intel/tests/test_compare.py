from pathlib import Path

from sip.compare import compare, parse_tier_tables


def test_compare_shadow_and_live_markdown_digests(tmp_path: Path) -> None:
    shadow = tmp_path / "shadow.md"
    live = tmp_path / "live.md"

    shadow.write_text(
        """
# Shadow digest

## A

| Ticker | Price | Change | Turnover | Catalyst | Why |
|---|---|---:|---:|---|---|
| `2330` | 1,000 | 6.0% | 500M | earnings | order strength |
| `2317` | 1,100 | 7.0% | 700M | demand | capacity expansion |

## B

| Ticker | Price | Change | Turnover |
|---|---|---:|---:|
| `1101` | 50 | 2.0% | 200M |
""".strip(),
        encoding="utf-8",
    )

    live.write_text(
        """
# Live digest

## A

| Ticker | Price | Change | Turnover | Catalyst | Why |
|---|---|---:|---:|---|---|
| `2330` | 1,010 | 6.2% | 520M | earnings | order strength |
| `2454` | 1,800 | 8.0% | 900M | demand | new product |

## Soft-A (`SOFT_A`)

| Ticker | Price | Change | Turnover | Catalyst |
|---|---|---:|---:|---|
| `2317` | 1,090 | 6.0% | 600M | demand |
""".strip(),
        encoding="utf-8",
    )

    result = compare(shadow, live)

    assert isinstance(result, dict)
    assert result["tiers"]["A"]["both"] == ["2330"]
    assert result["tiers"]["A"]["only_shadow"] == ["2317"]
    assert result["tiers"]["A"]["only_live"] == ["2454"]
    assert result["tiers"]["Soft-A"]["only_live"] == ["2317"]
    assert result["tiers"]["B"]["only_shadow"] == ["1101"]
    assert result["summary"]["both"] == 1
    assert result["summary"]["only_shadow"] == 2
    assert result["summary"]["only_live"] == 2


def test_parse_real_live_excerpt_and_multiline_catalyst() -> None:
    fixture = (
        Path(__file__).resolve().parent / "fixtures" / "nov09_live_excerpt.md"
    )
    parsed = parse_tier_tables(fixture)

    assert parsed["Soft-A"] == [
        "6669",
        "8039",
        "6538.TPEX",
        "7769",
        "8069.TPEX",
        "6919",
    ]
    assert parsed["TECH_WATCH"] == [
        "2330",
        "2454",
        "2308",
        "3037",
        "2383",
        "2303",
        "2408",
        "3443",
        "2344",
    ]
    assert parsed["B"] == ["3363.TPEX", "3605", "6443"]
    assert parsed["C"] == [
        "1303",
        "2327",
        "3105.TPEX",
        "1802",
        "2492",
        "6488.TPEX",
        "6770",
    ]
    assert "6456" not in parsed["C"]
    assert "故公布相關財務業務" not in parsed["Soft-A"]


def test_multiline_catalyst_continuation_is_not_a_ticker() -> None:
    markdown = """
## Soft-A (SOFT_A)
| Ticker | Company | Catalyst |
|---|---|---|
| 6669 | Wiwynn | MOPS 11/06 evening: Q3 results; board approved cash raise
故公布相關財務業務與現金增資安排
| 8039 | Taiflex | E Ink release |
"""
    parsed = parse_tier_tables(markdown)
    assert parsed["Soft-A"] == ["6669", "8039"]
