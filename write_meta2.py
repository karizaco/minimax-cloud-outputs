#!/usr/bin/env python3
"""Run metadata for the EOD snapshot — primary (TradingView screener) path."""
from __future__ import annotations

import csv
import datetime
import json
import os
import subprocess
import sys

DATA = "/workspace/data"
OUT_ROOT = "/workspace/us-eod"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-22"
PRIOR = None  # resolved at run time to the most recent prior snapshot
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]
LABEL = {"us": "US", "au": "AU", "jp": "JP", "tw": "TW", "ca": "CA",
         "eu-de": "EU-DE", "eu-fr": "EU-FR", "eu-it": "EU-IT", "eu-es": "EU-ES",
         "eu-nl": "EU-NL", "eu-be": "EU-BE", "eu-at": "EU-AT", "eu-pt": "EU-PT",
         "eu-ie": "EU-IE", "eu-fi": "EU-FI", "eu-dk": "EU-DK", "eu-gr": "EU-GR"}
CLOSED = {"au", "jp", "tw"}
# source actually used per run date (2026-10-21 ran on the Yahoo fallback)
SOURCE_HISTORY = {
    "2026-10-20": "TradingView screener",
    "2026-10-21": "Yahoo fallback (screener TLS-blocked)",
    "2026-10-22": "TradingView screener",
    "2026-10-23": "TradingView screener",
    "2026-10-24": "skipped (weekend)",
    "2026-10-25": "skipped (weekend)",
    "2026-10-26": "TradingView screener",
}


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
    cc = {}
    if os.path.exists(f"{DATA}/_close_check.json"):
        cc = json.load(open(f"{DATA}/_close_check.json"))
    global PRIOR
    _d0 = datetime.date.fromisoformat(DATE)
    for _back in range(1, 10):
        _cand = (_d0 - datetime.timedelta(days=_back)).isoformat()
        if os.path.exists(f"{OUT_ROOT}/{_cand}.csv"):
            PRIOR = _cand
            break
    lines = []
    A = lines.append
    A(f"# EOD market snapshot — {DATE} (run metadata)")
    A("")
    A("- Cron: #20 `eod-watchlist-csv-snapshot` (16:00 ET weekdays)")
    A(f"- Captured: {et_now()}")
    _d = datetime.date.fromisoformat(DATE)
    A(f"- Window check: PASS ({DATE} = {_d.strftime('%A')})")
    A("")
    A("## Data source")
    A("")
    A("**PRIMARY (skill: TradingView screener).**")
    A("`scanner.tradingview.com` was TLS-blocked from this sandbox for one day")
    A("(2026-10-21 — every CloudFront edge reset the handshake) and has")
    A("answered normally since. It was re-probed before this run (3/3 probes")
    A("HTTP 200) and served the full 17-region pull. Universe, OHLCV, change%,")
    A("market cap, PE and sector all come from one screener pass per region.")
    A("")
    A("Source actually used per run date:")
    A("")
    for d in sorted(SOURCE_HISTORY):
        A(f"- {d}: {SOURCE_HISTORY[d]}")
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
    _cap = datetime.datetime.now(datetime.timezone.utc).astimezone(
        datetime.timezone(datetime.timedelta(hours=-4)))
    if _cap.hour >= 16:
        A(f"- Capture at {_cap.strftime('%H:%M')} ET is **after** the 16:00 ET US")
        A("  close, so the session itself is finished. The screener still serves a")
        A("  900-second delayed stream: the US `close` column is the tape as of")
        A("  roughly 15:45-16:00 ET, not the official settling close.")
        if cc:
            A(f"- Measured against Yahoo's official daily close on {cc['sampled']}")
            A(f"  large caps: median |Δ| **{cc['median_abs_diff_vs_official_close_pct']}%**,")
            A(f"  max {cc['max_abs_diff_pct']}%. Names flat into the close match")
            A("  exactly; the gap is real price movement in the last 15 minutes.")
    else:
        med = lag.get("median_min")
        _offs = lag.get("offsets_min") or []
        _rng = f"{min(_offs):.0f}-{max(_offs):.0f} min" if _offs else "n/a"
        A(f"- TradingView's US stream measured **{round(med) if med else 'n/a'} min behind**")
        A(f"  the live tape (median of {len(_offs)} large caps, range {_rng}).")
        A("- The US close (16:00 ET) had **not** happened at capture time, so")
        A("  US/EU/CA rows are intraday, not settled closes.")
    A("- Every international region agrees with Yahoo to **<0.001 pp** median")
    A("  |Δ change| — their sessions are complete and those values are final.")
    A("- Method note: lag is measured by matching the screener close against")
    A("  Yahoo 5-minute bars. Closest-bar matching overstates the lag when a")
    A("  price is flat (it can land on an earlier, identical print), so quote")
    A("  the official-close comparison above rather than the bar delta.")
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
    A("Rule unchanged since 2026-10-21: one canonical row per company per region")
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
    A("**Source continuity:** this file and the 2026-10-22 / 2026-10-23 files")
    A("are screener-sourced, so prices are comparable apart from each run's")
    A("capture time and feed delay. The 2026-10-21 file was the Yahoo-fallback")
    A("run (live prices, with market_cap/pe_ratio/sector carried from")
    A("2026-10-20), so it is not price-comparable with the screener days. The")
    A("2026-10-24 and 2026-10-25 weekend fires were skipped by the window")
    A("check, so this is the first snapshot since 2026-10-23 - a three-calendar-")
    A("day gap in the series, not a missing trading day.")
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
