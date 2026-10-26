#!/usr/bin/env python3
"""Cron #25 ntrt-gap-brief — TradingView public screener fetch (Mode B).

Replaces the local Windows helper `ntrt_probe.py` probe (backend unreachable)
and the absent `mcp__tradingview_advanced__screen_stocks` MCP tool.

Cloud adaptations:
  * MCP tier is absent -> the PUBLIC scanner endpoint is the working path.
  * `markets` in the body is a placeholder; the endpoint PATH selects the market.
  * `premarket_change_percent` (MCP field name) -> `premarket_change` (public column).
    Verified equal: premarket_change == premarket_change_abs / close * 100.
  * Volume floor 10,000 (shared-repo lesson) to drop stale-reference rows.
  * No audit-log write on Cloud.

Writes raw JSON to /workspace/ntrt/_raw/ and a normalised row set to
/workspace/ntrt/_raw/screen_rows.json
"""
from __future__ import annotations

import json
import ssl
import time
import urllib.request
from pathlib import Path

RAW = Path("/workspace/ntrt/_raw")
RAW.mkdir(parents=True, exist_ok=True)

SCANNER = "https://scanner.tradingview.com/america/scan"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

COLUMNS = [
    "name", "description", "close", "change", "premarket_close", "premarket_open",
    "premarket_change", "premarket_change_abs", "premarket_volume",
    "market_cap_basic", "sector", "industry", "exchange", "country", "volume",
    "average_volume_30d_calc", "relative_volume_10d_calc", "Perf.W", "update_mode",
]
COL_IDX = {c: i for i, c in enumerate(COLUMNS)}

# Static filters. type=stock drops ETFs; exchange not_in_range OTC drops OTC shells.
BASE_FILTERS = [
    {"left": "type", "operation": "equal", "right": "stock"},
    {"left": "exchange", "operation": "not_in_range", "right": ["OTC"]},
    {"left": "market_cap_basic", "operation": "egreater", "right": 200000000},
    {"left": "volume", "operation": "egreater", "right": 10000},
]


def post(payload: dict, attempt: int = 0):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        SCANNER, data=body,
        headers={"Content-Type": "application/json", "User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            return json.loads(r.read().decode())
    except Exception as e:  # noqa: BLE001
        if attempt >= 2:
            return {"_error": f"{type(e).__name__}: {e}"}
        time.sleep(2 + 2 * attempt)
        return post(payload, attempt + 1)


def scan(name: str, filters: list, sort_by: str, order: str, n: int = 30):
    payload = {
        "filter": BASE_FILTERS + filters,
        "options": {"lang": "en"},
        "markets": ["america"],
        "symbols": {"query": {"types": []}, "tickers": []},
        "columns": COLUMNS,
        "sort": {"sortBy": sort_by, "sortOrder": order},
        "range": [0, n],
    }
    res = post(payload)
    (RAW / f"{name}.json").write_text(json.dumps(res, indent=1))
    if "_error" in res:
        print(f"[{name}] ERROR {res['_error']}")
        return []
    print(f"[{name}] totalCount={res.get('totalCount')} returned={len(res.get('data', []))}")
    return res.get("data", [])


def count_only(name: str, filters: list):
    """Universe count for coverage statistics (no sort needed)."""
    payload = {
        "filter": BASE_FILTERS + filters,
        "options": {"lang": "en"},
        "markets": ["america"],
        "symbols": {"query": {"types": []}, "tickers": []},
        "columns": ["name"],
        "range": [0, 0],
    }
    res = post(payload)
    (RAW / f"{name}.json").write_text(json.dumps(res, indent=1))
    n = res.get("totalCount", 0) if "_error" not in res else -1
    print(f"[{name}] totalCount={n} {'ERR ' + res['_error'] if '_error' in res else ''}")
    return n


def norm(rows):
    out = []
    for r in rows:
        d = r["d"]
        g = lambda c: d[COL_IDX[c]]  # noqa: E731
        try:
            pmc = g("premarket_change")
        except Exception:  # noqa: BLE001
            pmc = None
        if pmc is None:
            continue
        out.append({
            "symbol": r["s"],
            "ticker": g("name"),
            "name": g("description"),
            "close": g("close"),
            "day_change_pct": g("change"),
            "premarket_close": g("premarket_close"),
            "premarket_open": g("premarket_open"),
            "premarket_change_pct": pmc,
            "premarket_change_abs": g("premarket_change_abs"),
            "premarket_volume": g("premarket_volume"),
            "market_cap": g("market_cap_basic"),
            "sector": g("sector"),
            "industry": g("industry"),
            "exchange": g("exchange"),
            "country": g("country"),
            "volume": g("volume"),
            "avg_volume_30d": g("average_volume_30d_calc"),
            "relative_volume_10d": g("relative_volume_10d_calc"),
            "perf_week_pct": g("Perf.W"),
            "update_mode": g("update_mode"),
        })
    return out


def is_pseudo(ticker: str, name: str) -> bool:
    """Preferred shares, warrants, rights — not common equity gappers."""
    t = (ticker or "").upper()
    n = (name or "").lower()
    if "/" in t:                      # COF/PK and other preferred
        return True
    if n.startswith("warrant") or " warrant" in n or n.endswith(" warrant"):
        return True
    if n.startswith("right"):
        return True
    if t.endswith("W") and not t.endswith("UW"):   # PSNYW style warrants
        return True
    if t.endswith("WS") or t.endswith("WT"):
        return True
    return False


def main():
    up = scan("pass_up", [{"left": "premarket_change", "operation": "egreater", "right": 3}],
              "premarket_change", "desc", 30)
    down = scan("pass_down", [{"left": "premarket_change", "operation": "eless", "right": -3}],
                "premarket_change", "asc", 30)

    # Coverage denominators: how many names actually carry a premarket print.
    n_with_pm = count_only("count_with_premarket", [
        {"left": "premarket_change", "operation": "greater", "right": -100},
        {"left": "premarket_change", "operation": "less", "right": 100},
    ])
    n_all = count_only("count_universe", [])

    rows = norm(up) + norm(down)
    dropped = [r for r in rows if is_pseudo(r["ticker"], r["name"])]
    rows = [r for r in rows if not is_pseudo(r["ticker"], r["name"])]
    rows.sort(key=lambda r: -abs(r["premarket_change_pct"]))

    payload = {
        "fetched_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "universe_after_base_filters": n_all,
        "universe_with_premarket_print": n_with_pm,
        "rows": rows,
        "dropped_non_common_equity": [{"ticker": r["ticker"], "name": r["name"]} for r in dropped],
    }
    (RAW / "screen_rows.json").write_text(json.dumps(payload, indent=1))
    print(f"rows kept={len(rows)} dropped_pseudo={len(dropped)}")
    for r in rows[:24]:
        print(f"  {r['ticker']:<7} {r['premarket_change_pct']:>8.2f}%  mc=${(r['market_cap'] or 0)/1e9:.2f}B "
              f"pmvol={r['premarket_volume']} vol={r['volume']} | {r['name'][:44]}")


if __name__ == "__main__":
    main()
