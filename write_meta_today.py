#!/usr/bin/env python3
"""Run metadata for the 2026-10-21 EOD snapshot (Yahoo fallback path)."""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

DATA = "/workspace/data"
DATA2 = "/workspace/data2"
OUT_ROOT = "/workspace/us-eod"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-21"
PRIOR = "2026-10-20"
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
    stats = json.load(open(f"{DATA2}/_assemble_stats.json"))
    stale = json.load(open(f"{DATA2}/_stale_bars.json"))
    lines = []
    A = lines.append
    A(f"# EOD market snapshot — {DATE} (run metadata)")
    A("")
    A("- Cron: #20 `eod-watchlist-csv-snapshot` (16:00 ET weekdays)")
    A(f"- Captured: {et_now()} (window check PASS — weekday)")
    A("- Window check: PASS (2026-10-21 = Wednesday)")
    A("")
    A("## Data source — DEGRADED (fallback path, single branch, then stop)")
    A("")
    A("**PRIMARY (skill: TradingView screener) UNAVAILABLE.**")
    A("`scanner.tradingview.com` resets the TLS handshake from this sandbox on")
    A("every edge (18.165.83.23 / .27 / .74 / .125): `SSL_ERROR_SYSCALL`,")
    A("curl exit 000. `www.tradingview.com` still returns 200, so it is the")
    A("scanner host that is blocked, not the network. Yahoo's authenticated")
    A("endpoints (quote / quoteSummary) are blocked too — `fc.yahoo.com` and")
    A("`finance.yahoo.com` are unreachable, so no cookie/crumb.")
    A("")
    A("**FALLBACK USED (Yahoo unauthenticated chart API):**")
    A("")
    A("| field | source | freshness |")
    A("|---|---|---|")
    A("| open, high, low, close, volume, change_pct | Yahoo `/v8/finance/chart` | live (no delay) |")
    A("| market_cap, pe_ratio, sector | carried forward from 2026-10-20 file | 1d / 30d per skill cache TTL |")
    A("| ticker, name, currency, exchange | cached universe (TV pull of 2026-10-20) | 7d universe-cache TTL |")
    A("")
    A("- US close (16:00 ET) had **not** happened at capture time — US/EU/CA")
    A("  rows are intraday, not settled closes. AU/JP/TW sessions were complete.")
    A("- Every row's Yahoo daily bar was checked against its local session date;")
    A(f"  {len(stale)} rows whose last bar predates the {DATE} session were written")
    A("  with empty price fields rather than stale prices.")
    A("")
    A("## Coverage")
    A("")
    A("| region | rows | fresh price | stale bar | no data | file |")
    A("|---|---:|---:|---:|---:|---|")
    tot = fresh = 0
    for region in ["us"] + INTL:
        s = stats.get(region)
        if not s:
            continue
        tot += s["rows"]
        fresh += s["fresh"]
        A(f"| {LABEL[region]} | {s['rows']:,} | {s['fresh']:,} | {s['stale_bar']} | "
          f"{s['no_data']} | `{s['file'].replace(OUT_ROOT + '/', '')}` |")
    A(f"| **total** | **{tot:,}** | **{fresh:,}** | | | 17 files |")
    A("")
    A("## Universe change vs 2026-10-20")
    A("")
    A("Venue-duplicate rows were collapsed per region (one canonical row per")
    A("company per region, primary venue preferred) because the 2026-10-20 pull")
    A("kept every venue a German issuer lists on (XETR + SWB + HAM + LSX + ...,")
    A("the same issuer under different symbols). This is the skill's dedupe")
    A("intent (one row per underlying company) applied to issuers whose symbol")
    A("differs across venues. The US keeps every row (no US venue priority map,")
    A("so share classes are not collapsed).")
    A("")
    for region in ["us"] + INTL:
        cur = (f"{OUT_ROOT}/{region}/{DATE}.csv" if region != "us"
               else f"{OUT_ROOT}/{DATE}.csv")
        prv = (f"{OUT_ROOT}/{region}/{PRIOR}.csv" if region != "us"
               else f"{OUT_ROOT}/{PRIOR}.csv")
        if not (os.path.exists(cur) and os.path.exists(prv)):
            continue

        def tickers(p):
            with open(p, newline="", encoding="utf-8") as fh:
                return {r["ticker"] for r in csv.DictReader(fh)}
        c, q = tickers(cur), tickers(prv)
        A(f"- {LABEL[region]}: {len(c):,} rows vs {len(q):,} prior "
          f"(+{len(c - q):,} new, -{len(q - c):,} dropped)")
    A("")
    A("## Quality control")
    A("")
    prices = json.load(open(f"{DATA2}/yahoo_prices_{DATE}.json", encoding="utf-8"))
    ok = [r for r in prices.values() if r["status"] == "ok"]
    nod = len(prices) - len(ok)
    same = 0
    for r in ok:
        c, pr = r.get("close"), r.get("price")
        if c is not None and pr is not None and \
                abs(c - pr) <= max(1e-6, 0.0005 * abs(pr)):
            same += 1
    A(f"- **{len(ok):,} of {len(prices):,}** universe rows priced from Yahoo "
      f"({100*len(ok)/len(prices):.1f}%); {nod} have no Yahoo equivalent "
      "(Nagoya/Sapporo/Fukuoka listings, TSXV/CSE micro-caps, Canadian")
    A("  preferred series) and carry empty price fields. 899 of the priced")
    A("  rows had a bar from a prior session (no trade today) and were blanked,")
    A("  leaving **17,037 rows (91.7%)** carrying a 2026-10-21 price.")
    A("- **OHLC sanitizer**: 867 fields (759 `open`, 46 `high`, 62 `low`) were")
    A("  blanked across 861 rows where Yahoo's own bar contradicted itself —")
    A("  a stale `open` (often the prior close) and, for thin names, a stale")
    A("  day high/low. The bar `close` is Yahoo's live")
    A(f"  price and matches `regularMarketPrice` on {same:,}/{len(ok):,} rows, so")
    A("  the contradictory side was dropped, never the close. No value was")
    A("  invented or back-filled.")
    A("- **Symbol repair pass**: 1,193 rows recovered with alternative Yahoo")
    A("  symbol forms (`JPM/PC`->`JPM-PC`, `NOVO_B.CO`->`NOVO-B.CO`,")
    A("  `GRF.P.MC`->`GRF-P.MC`, Frankfurt `.F` for German alternative venues,")
    A("  class-preserving Canadian forms).")
    A("- **Identity fix**: 204 Canadian preferred rows had resolved to the")
    A("  COMMON share in the first pass (TSX:RY.PR.S -> RY.TO). They were")
    A("  re-resolved with class-preserving symbols only; where Yahoo carries")
    A("  no preferred, the price is blank rather than the common share's.")
    A("- **899 rows** whose last Yahoo daily bar predates the 2026-10-21")
    A("  session (no trade yet today — mostly preferreds and micro-caps) are")
    A("  written with empty price fields instead of yesterday's price.")
    A("- **Mover spot-check**: the six largest US gainers and four losers were")
    A("  re-queried from Yahoo after the run — names match the universe rows")
    A("  and % changes agree within ~1pp (live drift between capture and")
    A("  re-check).")
    A("")
    A("## Caveats")
    A("")
    A("- Ticker `EXCHANGE:SYMBOL` prefixes stay in TradingView form so the")
    A("  archive is comparable with prior days; the price data behind them is")
    A("  Yahoo's. `exchange` is the TV venue code, `currency` is Yahoo's.")
    A("- `market_cap` / `pe_ratio` / `sector` are one day older than the prices")
    A("  (Yahoo quote/quoteSummary is blocked, so they are carried forward).")
    A("- No new listings can appear in this file: the universe is yesterday's")
    A("  cached pull (7-day TTL), because the screener is unreachable.")
    A("- Movers-mode forward-fill was not applied — this run is a full price")
    A("  refresh for every symbol Yahoo could resolve.")
    A("")
    out = f"{OUT_ROOT}/{DATE}.meta.md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    main()
