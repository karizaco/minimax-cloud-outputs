from pathlib import Path

from sip.compare import compare


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
