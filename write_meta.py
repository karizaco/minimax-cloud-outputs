#!/usr/bin/env python3
"""Write the run metadata sidecar for the EOD snapshot."""
from __future__ import annotations

import csv
import json
import os
import subprocess
from datetime import datetime, timezone

OUT_ROOT = "/workspace/us-eod"
DATA = "/workspace/data"
DATE = "2026-10-20"
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]
LABEL = {"us": "US", "au": "AU", "jp": "JP", "tw": "TW", "ca": "CA",
         "eu-de": "EU-DE", "eu-fr": "EU-FR", "eu-it": "EU-IT", "eu-es": "EU-ES",
         "eu-nl": "EU-NL", "eu-be": "EU-BE", "eu-at": "EU-AT", "eu-pt": "EU-PT",
         "eu-ie": "EU-IE", "eu-fi": "EU-FI", "eu-dk": "EU-DK", "eu-gr": "EU-GR"}


def et_now():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"],
                          env={**os.environ, "TZ": "America/New_York"},
                          capture_output=True, text=True).stdout.strip()


def main():
    verify = json.load(open(f"{DATA}/_yahoo_verify.json"))
    qa = json.load(open(f"{DATA}/_qa_summary.json"))
    lines = []
    A = lines.append
    A("# EOD market snapshot — 2026-10-20 (run metadata)")
    A("")
    A(f"- Cron: #20 `eod-watchlist-csv-snapshot` (16:00 ET weekdays)")
    A(f"- Captured: {et_now()} (screener pull 10:03–10:31 ET)")
    A("- Window check: PASS (2026-10-20 = Tuesday, weekday)")
    A("- Primary source: TradingView screener (`scanner.tradingview.com/{market}/scan`),")
    A("  type=stock, US excludes OTC, intl filtered by issuer country")
    A("- Cross-check source: Yahoo Finance (`/v7/finance/spark`, `/v8/finance/chart`)")
    A("- MCP note: `mcp__shibui-finance__*`, `mcp__tradingview_advanced__*` and")
    A("  `mcp__yahoo_finance__*` are not bound in this Cloud session; the same")
    A("  upstream APIs were called directly over HTTPS instead.")
    A("")
    A("## Coverage")
    A("")
    A("| region | rows | file |")
    A("|---|---:|---|")
    total = 0
    for region in ["us"] + INTL:
        p = (f"{OUT_ROOT}/{DATE}.csv" if region == "us"
             else f"{OUT_ROOT}/{region}/{DATE}.csv")
        with open(p, newline="", encoding="utf-8") as fh:
            n = sum(1 for _ in csv.DictReader(fh))
        total += n
        rel = p.replace(f"{OUT_ROOT}/", "")
        A(f"| {LABEL[region]} | {n:,} | `{rel}` |")
    A(f"| **total** | **{total:,}** | 17 files |")
    A("")
    A("## Lag / data freshness")
    A("")
    A("- US cash close (16:00 ET) had **not** happened at capture time: the US")
    A("  rows are an intraday snapshot, not settled closes.")
    A("- TradingView's US stream measured **~45-60 min behind the live tape**")
    A("  (matched TV close against Yahoo 5-minute bars on NVDA/AAPL/MSFT/GOOG*,")
    A("  median 45 min). TV reports `update_mode=delayed_streaming_900`.")
    A("- Closed markets agree with Yahoo to **<0.001 pp** median |Δ change|")
    A("  (AU 0.0003, JP 0.0002, TW 0.0002) — confirms the capture is final for those.")
    A("- EU + US (open at capture) show 0.2-1.6 pp median |Δ| vs Yahoo live,")
    A("  consistent with the feed lag rather than a data error.")
    A("")
    A("## Verification (Yahoo vs TradingView, 80-name sample per region)")
    A("")
    A("| region | matched | same entity | median |Δchg| pp | >1pp |")
    A("|---|---:|---:|---:|---:|")
    for region in ["us"] + INTL:
        v = verify.get(region)
        if not v:
            continue
        A(f"| {LABEL[region]} | {v['matched']}/{v['checked']} | "
          f"{v['matched_same_entity']} | {v['median_abs_change_diff_pp']} | "
          f"{v['n_over_1pp']} |")
    A("")
    A("## Known caveats")
    A("")
    A("- `eu-de` has 1 row with inconsistent OHLC (`LSX:A25429`, SQD.AI Strategies")
    A("  AG) — upstream screener quirk on an illiquid instrument; left as-is")
    A("  rather than back-filled (no invented values).")
    A("- Extreme movers are dominated by sub-$100M micro-caps with near-zero")
    A("  volume (single-print ±50-300% swings). Use a market-cap floor before")
    A("  reading the movers list.")
    A("- Cross-listed issuers appear in more than one region file with different")
    A("  change_pct (known skill limitation; no cross-file dedupe).")
    A("- Blank `pe_ratio` = negative/absent earnings; blank `market_cap` = no")
    A("  market cap reported (105 US, 125 CA, ~5 elsewhere). 6 blank `change_pct`")
    A("  cells were filled from Yahoo Finance.")
    A("- No prior-day archive exists in this sandbox, so movers-mode forward-fill")
    A("  was not applied — every region is a full refresh.")
    A("")
    out = f"{OUT_ROOT}/{DATE}.meta.md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    main()
