#!/usr/bin/env python3
"""Cloud re-implementation of cron #9 data fetch.

Tier-2 fallback: TradingView public scanner (POST /america/scan).
The MCP tier (shibui-finance, tradingview, tradingview-advanced, financekit, yahoo-finance)
is provably unbound in this Cloud session, so this script is the working data path.

Paging lesson (2026-10-26): sorting by `market_cap_basic` is UNSTABLE here because that
column is NULL for every ETF/fund, and rows shift between pages -- the first run lost ~117
stocks and every major index ETF (SPY/QQQ/IWM) and duplicated ~1,650 rows. Fix: sort by
`name` (a near-total order), page with an overlap, dedupe by full ticker id, and report
unique-vs-totalCount coverage per type.
"""
import json
import subprocess
import sys
import time

SCAN_URL = "https://scanner.tradingview.com/america/scan"
UA = "Mozilla/5.0"

COLUMNS = [
    "name", "description", "type", "exchange", "country", "currency", "sector", "industry",
    "close", "open", "high", "low", "volume", "change", "change_abs", "pricescale",
    "market_cap_basic", "price_earnings_ttm", "price_book_ratio", "dividend_yield_recent",
    "average_volume_10d_calc", "average_volume_30d_calc", "relative_volume_10d_calc",
    "ATR", "RSI", "VWMA",
    "SMA20", "SMA50", "SMA150", "SMA200", "EMA20", "EMA50",
    "Perf.5D", "Perf.W", "Perf.1M", "Perf.3M", "Perf.6M", "Perf.Y",
    "High.1M", "Low.1M", "High.3M", "Low.3M", "High.6M", "Low.6M", "High.5D", "Low.5D",
    "Volatility.D", "Volatility.M",
    "Recommend.All", "Recommend.MA",
    "earnings_per_share_diluted_yoy_growth_ttm", "beta_1_year",
    "update_mode", "index",
]

PAGE = 2000
STEP = 1500  # overlap so boundary drift cannot drop rows


def scan(payload, tries=3):
    body = json.dumps(payload)
    for i in range(tries):
        p = subprocess.run(
            ["curl", "-s", "--max-time", "90", "-X", "POST", SCAN_URL,
             "-H", f"User-Agent: {UA}",
             "-H", "Content-Type: application/json",
             "--data-binary", body],
            capture_output=True, text=True,
        )
        if p.returncode == 0 and p.stdout.strip():
            try:
                return json.loads(p.stdout)
            except json.JSONDecodeError:
                pass
        time.sleep(1.0 + i)
    return None


def fetch_type(t, rows, seen):
    lo = 0
    total = None
    while True:
        payload = {
            "filter": [{"left": "type", "operation": "equal", "right": t}],
            "options": {"lang": "en"},
            "symbols": {"query": {"types": []}, "tickers": []},
            "columns": COLUMNS,
            "sort": {"sortBy": "name", "sortOrder": "asc"},
            "range": [lo, lo + PAGE - 1],
        }
        r = scan(payload)
        if not r or "data" not in r:
            print(f"  !! scan failed for type={t} at lo={lo}", file=sys.stderr)
            break
        batch = r["data"]
        total = r.get("totalCount", total)
        new = 0
        for row in batch:
            if row["s"] in seen:
                continue
            seen.add(row["s"])
            rows.append(row)
            new += 1
        print(f"  type={t} lo={lo} got={len(batch)} new={new} cum={len(rows)} total={total}",
              file=sys.stderr)
        lo += STEP
        if total is not None and lo >= total:
            break
        if not batch:
            break
    return total


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/data/tv_universe_raw.json"
    rows, seen = [], set()
    coverage = {}
    for t in ("stock", "fund", "dr"):
        coverage[t] = fetch_type(t, rows, seen)
    uniq_ids = len(seen)
    tot_reported = sum(v for v in coverage.values() if v)
    print(f"TOTAL_ROWS={len(rows)} UNIQUE_IDS={uniq_ids} REPORTED_SUM={tot_reported} "
          f"coverage={uniq_ids/tot_reported*100:.3f}%", file=sys.stderr)
    with open(out_path, "w") as f:
        json.dump({"columns": COLUMNS, "reported_by_type": coverage,
                   "total_reported": tot_reported, "rows": rows}, f)
    print(f"wrote {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
