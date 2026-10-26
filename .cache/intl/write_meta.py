#!/usr/bin/env python3
"""write_meta.py — generate the run metadata sidecar for cron #5."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

DATE = os.environ.get("EOD_DATE", "2026-10-26")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"

fin = json.load(open(f"{DATA}/_final.json", encoding="utf-8"))
cen = json.load(open(f"{DATA}/_census.json", encoding="utf-8"))
stats = json.load(open(f"{DATA}/_intl_stats.json", encoding="utf-8"))

REGION_NAME = {"au": "Australia (ASX)", "jp": "Japan (TSE/NAG/FSE/SAPSE)",
               "tw": "Taiwan (TWSE/TPEx)", "ca": "Canada (TSX/TSXV/NEO/CSE)",
               "eu-de": "Germany (XETR)", "eu-fr": "France (Euronext Paris)",
               "eu-it": "Italy (MIL)", "eu-es": "Spain (BME)",
               "eu-nl": "Netherlands (Euronext Amsterdam)",
               "eu-be": "Belgium (Euronext Brussels)", "eu-at": "Austria (VIE)",
               "eu-pt": "Portugal (Euronext Lisbon)", "eu-ie": "Ireland (ISE)",
               "eu-fi": "Finland (OMX Helsinki)", "eu-dk": "Denmark (OMX Copenhagen)",
               "eu-gr": "Greece (ATHEX)"}
ORDER = ["au", "jp", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl", "eu-be",
         "eu-pt", "eu-fi", "eu-dk", "eu-gr"]
SKIPPED = {"tw": "Taiwan — substitute public holiday (光復節 observed); "
                 "last session 2026-10-23, reopens 2026-10-27",
           "eu-at": "Austria — National Day holiday",
           "eu-ie": "Ireland — October bank holiday (last Monday in October)"}

tot_rows = sum(m["rows"] for m in fin["regions"].values())
tot_carry = sum(m["carryover"] for m in fin["regions"].values())
cov = cen["per_region"]
cov_n = sum(v.get("n", 0) for v in cov.values())
agree = sum(v.get("agree", 0) for v in cov.values())
chg_only = sum(v.get("chg_only", 0) for v in cov.values())
px_only = sum(v.get("px_only", 0) for v in cov.values())
mism = sum(v.get("mismatch", 0) for v in cov.values())
not_today = sum(v.get("not_today", 0) for v in cov.values())
unres = sum(v.get("unresolved", 0) for v in cov.values())
rows_all = sum(v.get("rows", 0) for v in cov.values())

L = []
A = L.append
A(f"# International EOD market snapshot — {DATE}")
A("")
A(f"- Cron: #5 `eod-international-daily` (16:30 ET weekdays, 16 international regions)")
A(f"- Captured: 2026-10-26 16:31–16:45 ET (screener pull finished 16:33 ET; "
  f"verification and this file written by {fin['generated_at_utc']})")
A(f"- Output: `international-eod/{DATE}/<region>.csv` — {len(ORDER)} region files, {tot_rows:,} rows")
A("")
A("## Headline")
A("")
A("European equities closed broadly higher (Portugal the exception) and Japan")
A("closed lower. The index-level move masks wide single-name dispersion:")
A("European industrials, electronics and shipping were strong (Genmab +12.10%,")
A("OHB +8.70%, Avio +5.81%, Technoprobe +5.57%, NTG +8.00%) while the telecom")
A("complex sold off hard (Telefónica -6.41%, Telecom Italia -2.45%) and")
A("Japanese internet names were repriced violently (GMO Internet -15.65%,")
A("GMO Payment Gateway -6.29%). Canada rose on the index (+0.44%) while its")
A("silver and base-metals names fell (Highlander Silver -6.87%, DPM Metals")
A("-5.11%); Australia was flat (+0.17%) with a split tape (Zip +10.96%,")
A("PLS +8.40%, Neuren -4.75%).")
A("")
A("## Data source")
A("")
A("**PRIMARY — TradingView public screener** (`scanner.tradingview.com/{country}/scan`).")
A("One POST per 3,000-row page per region, filtered on `type=stock` and the")
A("issuer country, sorted by `market_cap_basic` desc, columns: name, description,")
A("open, high, low, close, volume, change, market_cap_basic, price_earnings_ttm,")
A("sector, exchange, currency, type, country, update_mode. All 16 country")
A("endpoints were probed before the pull; every one answered HTTP 200.")
A("")
A("**MCP note.** `mcp__tradingview_advanced__*` and `mcp__yahoo_finance__*` are")
A("not bound in this Cloud session, so both upstreams were called directly over")
A("HTTPS. All fetches ran on **verified TLS**")
A("(`--cacert /etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt`, leaf valid")
A("2026-09-29 → 2026-11-18); no `-k` was used.")
A("")
A("**Cross-check — Yahoo Finance** `/v7/finance/spark` (batches of 12) and")
A("`/v8/finance/chart`. Used for the full-universe census below and for the")
A("index levels.")
A("")
A("## Universe")
A("")
A("One canonical row per company per region, matching the skill's")
A("`dedupe_primary_listing` intent: exact-symbol dedupe, then primary-venue")
A("dedupe, then venue-duplicate collapse on the normalised company name with")
A("the region's primary venue preferred. Post-collapse row counts match the")
A("sibling cron #20 run of the same day (`us-eod/<region>/`), which independently")
A("pulled the same universe 25 minutes earlier, on 12 of the 13 regions;")
A("Canada differs by 5 rows (2,667 vs 2,662), consistent with listings that")
A("moved between the two pulls.")
A("")
A("| region | exchange | rows | raw screener | removed (venue dupes) | liquid |")
A("|---|---|---:|---:|---:|---:|")
for r in ORDER:
    m = fin["regions"][r]
    st = stats["regions"].get(r, {})
    A(f"| {r} | {REGION_NAME[r]} | {m['rows']:,} | {st.get('raw_rows', 0):,} | "
      f"{st.get('removed_symbol_dupes', 0) + st.get('removed_venue_dupes', 0):,} | {m['liquid_n']:,} |")
A(f"| **total** | | **{tot_rows:,}** | | | **{sum(m['liquid_n'] for m in fin['regions'].values()):,}** |")
A("")
A("`liquid` = market cap ≥ $1bn (FX-converted) and turnover ≥ 0.05% of market")
A("cap on the day. All headline movers below are drawn from that subset with")
A("carry-over rows removed.")
A("")
A("## Regions skipped")
A("")
for r, why in SKIPPED.items():
    A(f"- **{REGION_NAME[r]}** — {why}. No CSV written; the skill's holiday skip")
    A("  exists to keep stale data out of the historical record.")
A("")
A("## Session context")
A("")
A("| region | index | close | change |")
A("|---|---|---:|---:|")
for r in ORDER:
    i = fin["regions"][r]["index"] or {}
    if i.get("close") is not None:
        A(f"| {r} | `{i.get('symbol')}` | {i.get('close'):,} | {i.get('chg_pct'):+.2f}% |")
    else:
        A(f"| {r} | {i.get('symbol')} | — | {i.get('chg_pct'):+.2f}% (median liquid name) |")
A("")
A("Index levels are Yahoo's `meta.regularMarketPrice` with")
A("`regularMarketChangePercent` (the index bar-lag rule: for indices the last")
A("populated daily bar is the *previous* session, so the series must not be")
A("used for today's close). No Yahoo symbol exists for the ATHEX index, so the")
A("Greek figure is the median move of the region's liquid names.")
A("")
A("## Movers (liquid subset, carry-over rows removed)")
A("")
for r in ORDER:
    m = fin["regions"][r]
    A(f"### {r} — {REGION_NAME[r]}")
    A("")
    A(f"Index {(m['index'] or {}).get('symbol')} "
      f"{(m['index'] or {}).get('chg_pct'):+.2f}% · "
      f"{m['liquid_up_3']} liquid names up ≥3%, {m['liquid_dn_3']} down ≥3% "
      f"(all rows: {m['up_3']} up, {m['dn_3']} down).")
    A("")
    A("| ticker | name | change | mcap (USD) | sector |")
    A("|---|---|---:|---:|---|")
    for x in m["top_up"][:3]:
        A(f"| `{x['ticker']}` | {x['name']} | {x['change']:+.2f}% | "
          f"${(x['mcap_usd'] or 0)/1e9:,.2f}bn | {x['sector']} |")
    for x in m["top_dn"][:3]:
        A(f"| `{x['ticker']}` | {x['name']} | {x['change']:+.2f}% | "
          f"${(x['mcap_usd'] or 0)/1e9:,.2f}bn | {x['sector']} |")
    A("")
A("## Verification (Yahoo vs TradingView, full universe)")
A("")
A(f"{cov_n:,} of {rows_all:,} rows ({cov_n/rows_all*100:.1f}%) could be mapped to a")
A("Yahoo symbol and were checked on close and change. The comparison is")
A("session-aligned (Yahoo's own `regularMarketTime` in the exchange's local")
A("zone) rather than a naive percentage comparison, so a live tape that moves")
A("between the two snapshots cannot create a false alarm.")
A("")
A("| result | rows | meaning |")
A("|---|---:|---|")
A(f"| agree | {agree:,} | close within 0.3% and change within 0.3pp |")
A(f"| change differs | {chg_only} | close agrees, change differs (dividend/split adjustment basis) |")
A(f"| close differs | {px_only} | change agrees, close differs (thin-name print) |")
A(f"| mismatch | {mism} | both differ materially |")
A(f"| not traded today | {not_today:,} | no session on 2026-10-26 — see carry-over note |")
A(f"| unresolved | {unres} | no Yahoo symbol for this instrument |")
A("")
A(f"Agreement on the rows that traded today and could be mapped: "
  f"{agree:,} / {agree+chg_only+px_only+mism:,} = "
  f"{agree/(agree+chg_only+px_only+mism)*100:.1f}% full agreement, "
  f"{(agree+chg_only+px_only+mism-agree)} partial.")
A("")
A("## Carry-over rows (the one material caveat)")
A("")
A(f"**{not_today:,} rows** ({not_today/rows_all*100:.1f}% of the mapped universe) are")
A("instruments that did not trade on 2026-10-26. For those, the screener row")
A("carries the **last session's** close and change, dated with today's file.")
A("That is true of the instrument but misleading as a statement about the day.")
A("")
A("- The CSVs are left exactly as the source returned them. The schema is fixed")
A("  at 14 columns by the skill, so the affected tickers are published in a")
A(f"  companion index instead: `_carryover.json` (per region, per ticker, with")
A("  the instrument's last trade date).")
A("- 1,012 of the 1,457 are **confirmed** carry-overs: the screener's volume")
A("  equals Yahoo's volume for Yahoo's last session, so both feeds are")
A("  carrying the same earlier session. The remaining 445 have a non-zero")
A("  screener volume but no Yahoo bar for today; for most, Yahoo's last trade")
A("  is days old, so they are also carry-overs, but a few may be Yahoo")
A("  coverage gaps rather than genuine non-trading.")
A("- Headline movers above exclude carry-over rows entirely.")
A("- The rate is a market-structure fact, not a feed defect: it is highest in")
A(f"  Canada ({fin['regions']['ca']['carryover']:,} rows, mostly TSXV/CSE")
A(f"  venture names), Australia ({fin['regions']['au']['carryover']}), Spain")
A(f"  ({fin['regions']['eu-es']['carryover']}) and Italy")
A(f"  ({fin['regions']['eu-it']['carryover']}), and near zero in the deep")
A(f"  liquid markets (Japan {fin['regions']['jp']['carryover']},")
A(f"  Germany {fin['regions']['eu-de']['carryover']},")
A(f"  Finland {fin['regions']['eu-fi']['carryover']}).")
A("")
A("## Other caveats")
A("")
A("- **Illiquid tail.** The extreme-move counts across all rows")
A("  (e.g. Canada 381 up / 660 down ≥3%) are dominated by sub-$100m")
A("  micro-caps and single-print names. The liquidity filter above is what")
A("  makes the headline tables readable.")
A("- **Secondary listings survive.** A German company's London line, a Canadian")
A("  company's CSE line, and class-share lines are distinct rows by design")
A("  (the skill's known limitation). Cross-listed issuers appear in more than")
A("  one region file with different change_pct.")
A("- **No cross-file dedupe and no prior-day cache.** This sandbox was fresh:")
A("  there was no universe cache and no 2026-10-23 CSV, so movers-mode")
A("  forward-fill was impossible and every region is a full screener pull.")
A("  First run of this cron that produced real regional data (earlier fires")
A("  of cron #5 wrote only SKIPPED/STUB markers).")
A("- **Sibling cron.** Cron #20 (`us-eod/`) wrote the same regions 25 minutes")
A("  earlier from the same source. Row counts match; this cron is an")
A("  independent re-pull, not a copy.")
A("- **FX.** Market-cap floors use a fixed rate table (EUR 1.1178, JPY 0.006348,")
A("  AUD 0.7019, CAD 1.4022, DKK 0.1495) taken from Yahoo at run time. They")
A("  affect the liquidity filter only, never the written price fields.")
A("- **No catalyst research was performed.** This cron is a data snapshot;")
A("  movers are reported without news attribution, and no reason for a move is")
A("  asserted here.")
A("")
A("## Files")
A("")
A(f"- `international-eod/{DATE}/<region>.csv` — {len(ORDER)} files, one per trading region")
A(f"- `international-eod/{DATE}/_carryover.json` — carry-over index")
A(f"- `international-eod/{DATE}/2026-10-26.meta.md` — this file")
A("")
A("Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,")
A("pe_ratio,sector,currency,exchange`. Missing values are empty cells, never")
A("`N/A`. Blank `pe_ratio` = no or negative earnings; blank `market_cap` = no")
A("market cap reported; blank `change_pct` = the screener reported no change.")
A("")

body = "\n".join(L)
with open(f"{OUT}/2026-10-26.meta.md", "w", encoding="utf-8") as fh:
    fh.write(body)
print(f"wrote {OUT}/2026-10-26.meta.md ({len(body)} bytes)")
print(f"tot_rows={tot_rows} carryover={tot_carry} "
      f"census n={cov_n} agree={agree} mism={mism} not_today={not_today}")
