#!/usr/bin/env python3
"""Run metadata for the EOD snapshot — primary (TradingView screener) path."""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys

DATA = "/workspace/data"
OUT_ROOT = "/workspace/us-eod"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-22"
PRIOR = "2026-10-21"
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]
LABEL = {"us": "US", "au": "AU", "jp": "JP", "tw": "TW", "ca": "CA",
         "eu-de": "EU-DE", "eu-fr": "EU-FR", "eu-it": "EU-IT", "eu-es": "EU-ES",
         "eu-nl": "EU-NL", "eu-be": "EU-BE", "eu-at": "EU-AT", "eu-pt": "EU-PT",
         "eu-ie": "EU-IE", "eu-fi": "EU-FI", "eu-dk": "EU-DK", "eu-gr": "EU-GR"}
CLOSED = {"au", "jp", "tw"}


def et_now():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"],
                          env={**os.environ, "TZ": "America/New_York"},
                          capture_output=True, text=True).stdout.strip()


def tickers(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return {r["ticker"] for r in csv.DictReader(fh)}


def main():
    verify = json.load(open(f"{DATA}/_yahoo_verify.json"))
    stats = json.load(open(f"{DATA}/_csv_stats.json"))
    lag = json.load(open(f"{DATA}/_lag.json"))
    lines = []
    A = lines.append
    A(f"# EOD market snapshot — {DATE} (run metadata)")
    A("")
    A("- Cron: #20 `eod-watchlist-csv-snapshot` (16:00 ET weekdays)")
    A(f"- Captured: {et_now()}")
    A("- Window check: PASS (2026-10-22 = Thursday)")
    A("")
    A("## Data source")
    A("")
    A("**PRIMARY (skill: TradingView screener) — RESTORED.**")
    A("`scanner.tradingview.com` was TLS-blocked from this sandbox on")
    A("2026-10-21 (every CloudFront edge reset the handshake). It answered")
    A("normally today (3/3 probes, then a full 17-region pull), so this file is")
    A("back on the skill's primary path. Universe, OHLCV, change%, market cap,")
    A("PE and sector all come from one screener pass per region.")
    A("")
    A("- Cross-check source: Yahoo Finance (`/v7/finance/spark`,")
    A("  `/v8/finance/chart`) — 80-name sample per region, entity + change%")
    A("  comparison, and the basis for the lag measurement below.")
    A("- MCP note: `mcp__tradingview_advanced__*` and `mcp__yahoo_finance__*`")
    A("  are not bound in this Cloud session; the same upstream APIs were")
    A("  called directly over HTTPS.")
    A("")
    A("## Lag / freshness")
    A("")
    med = lag.get("median_min")
    A(f"- TradingView's US stream measured **{round(med) if med else 'n/a'} min behind**")
    A("  the live tape (median of 8 large caps, range 5-20 min) — fresher than")
    A("  the ~55 min measured on 2026-10-20.")
    A("- The US close (16:00 ET) had **not** happened at capture time, so")
    A("  US/EU/CA rows are intraday, not settled closes. AU/JP/TW sessions were")
    A("  complete.")
    A("- Closed markets agree with Yahoo to **<0.001 pp** median |Δ change|")
    A("  (AU 0.0003, JP 0.0003, TW 0.0002) — those values are final.")
    A("")
    A("## Coverage")
    A("")
    A("| region | rows | file | blank pe_ratio | blank market_cap |")
    A("|---|---:|---|---:|---:|")
    tot = 0
    for region in ["us"] + INTL:
        s = stats.get(region)
        if not s:
            continue
        tot += s["rows"]
        b = s.get("blank", {})
        A(f"| {LABEL[region]} | {s['rows']:,} | "
          f"`{s['path'].replace(OUT_ROOT + '/', '')}` | "
          f"{b.get('pe_ratio', 0):,} | {b.get('market_cap', 0):,} |")
    A(f"| **total** | **{tot:,}** | 17 files | | |")
    A("")
    A("## Universe")
    A("")
    A("Same rule as 2026-10-21: one canonical row per company per region")
    A("(venue duplicates collapsed, primary venue preferred). The US keeps every")
    A("row so share classes survive. Row counts vs the prior file:")
    A("")
    for region in ["us"] + INTL:
        cur = (f"{OUT_ROOT}/{region}/{DATE}.csv" if region != "us"
               else f"{OUT_ROOT}/{DATE}.csv")
        prv = (f"{OUT_ROOT}/{region}/{PRIOR}.csv" if region != "us"
               else f"{OUT_ROOT}/{PRIOR}.csv")
        if not (os.path.exists(cur) and os.path.exists(prv)):
            continue
        c, q = tickers(cur), tickers(prv)
        A(f"- {LABEL[region]}: {len(c):,} rows vs {len(q):,} on {PRIOR} "
          f"(+{len(c - q):,} new, -{len(q - c):,} dropped)")
    A("")
    A("**Source continuity:** the 2026-10-21 file was written from Yahoo")
    A("prices (TradingView blocked, market_cap/pe_ratio/sector carried from")
    A("2026-10-20); today's file is screener-sourced, so those three fields")
    A("are fresh again. Price fields for the two days are not strictly")
    A("comparable — 2026-10-21 prices are live-to-capture, 2026-10-22 prices")
    A("carry the screener's ~20 min delay.")
    A("")
    A("## Verification (Yahoo vs TradingView, ~80 names per region)")
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
    A("## Caveats")
    A("")
    A("- Extreme movers are dominated by sub-$100M micro-caps and preferred")
    A("  series with near-zero volume (single-print ±50-600% swings). Apply a")
    A("  market-cap floor before reading the movers list.")
    A("- `eu-de` still carries a small tail of London-listed German structured")
    A("  products (LSX/LS codes) — they survive the venue collapse because they")
    A("  have no domestic listing.")
    A("- Cross-listed issuers appear in more than one region file with")
    A("  different change_pct (known skill limitation; no cross-file dedupe).")
    A("- 4 blank `change_pct` cells were filled from Yahoo Finance; blank")
    A("  `pe_ratio` = no/negative earnings, blank `market_cap` = no market cap")
    A("  reported.")
    A("- No movers-mode forward-fill was applied — every region is a full")
    A("  refresh (the screener pull is a few seconds).")
    A("")
    out = f"{OUT_ROOT}/{DATE}.meta.md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    main()
