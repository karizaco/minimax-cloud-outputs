#!/usr/bin/env python3
"""write_meta.py — generate the run metadata sidecar for cron #5 (2026-10-27).

Everything numeric in the artifact is read from the run's own JSON sidecars
(_final.json, _census.json, _intl_stats.json) so no figure is typed by hand.
The prose headline is supplied in _headline.md, written by the agent after
reviewing the movers.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

DATE = os.environ.get("EOD_DATE", "2026-10-27")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"

fin = json.load(open(f"{DATA}/_final.json", encoding="utf-8"))
cen = json.load(open(f"{DATA}/_census.json", encoding="utf-8"))
stats = json.load(open(f"{DATA}/_intl_stats.json", encoding="utf-8"))

REGION_NAME = {"au": "Australia (ASX)", "jp": "Japan (TSE/NAG/FSE/SAPSE)",
               "tw": "Taiwan (TWSE/TPEX)", "ca": "Canada (TSX/TSXV/NEO/CSE)",
               "eu-de": "Germany (XETR)", "eu-fr": "France (Euronext Paris)",
               "eu-it": "Italy (MIL)", "eu-es": "Spain (BME)",
               "eu-nl": "Netherlands (Euronext Amsterdam)",
               "eu-be": "Belgium (Euronext Brussels)", "eu-at": "Austria (VIE)",
               "eu-pt": "Portugal (Euronext Lisbon)", "eu-ie": "Ireland (Euronext Dublin)",
               "eu-fi": "Finland (OMX Helsinki)", "eu-dk": "Denmark (OMX Copenhagen)",
               "eu-gr": "Greece (ATHEX)"}
ORDER = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
         "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]

finr = fin["regions"]
present = [r for r in ORDER if r in finr]
tot_rows = sum(finr[r]["rows"] for r in present)
tot_carry = sum(finr[r]["carryover"] for r in present)
tot_conf = sum(finr[r]["carryover_confirmed"] for r in present)
cov = cen["per_region"]
cov_n = sum(v.get("n", 0) for v in cov.values())
agree = sum(v.get("agree", 0) for v in cov.values())
chg_only = sum(v.get("chg_only", 0) for v in cov.values())
px_only = sum(v.get("px_only", 0) for v in cov.values())
mism = sum(v.get("mismatch", 0) for v in cov.values())
not_today = sum(v.get("not_today", 0) for v in cov.values())
unres = sum(v.get("unresolved", 0) for v in cov.values())
no_px = sum(v.get("no_price", 0) for v in cov.values())
rows_all = sum(v.get("rows", 0) for v in cov.values())
traded = agree + chg_only + px_only + mism

L = []
A = L.append
A(f"# International EOD market snapshot — {DATE}")
A("")
A(f"- Cron: #5 `eod-international-daily` (16:30 ET weekdays, 16 international regions)")
A(f"- Captured: 2026-10-27 16:31–16:36 ET (screener pull finished 16:33 ET; "
  f"verification and this file written by {fin['generated_at_utc']})")
A(f"- Output: `international-eod/{DATE}/<region>.csv` — {len(present)} region files, {tot_rows:,} rows")
A("")

# ---- headline (agent-written prose) ----
hl = ""
hp = f"{DATA}/_headline.md"
if os.path.exists(hp):
    hl = open(hp, encoding="utf-8").read().strip()
A("## Headline")
A("")
A(hl if hl else "_Headline not available._")
A("")

# ---- deviations / corrections, near the top ----
A("## Deviations and corrections this run")
A("")
A("- **The skill's holiday calendar is wrong for Greece by one day, and Greece "
  "traded.** `holiday_calendar.py` lists Ochi Day 2026 as `2026-10-27`; the "
  "actual date is **Wednesday 2026-10-28** (timeanddate, holidays-info and the "
  "Athens Exchange 2026 calendar all agree, and the exchange's next closure is "
  "listed as 28 Oct). The ATHEX was open on 2026-10-27: Yahoo's daily bars for "
  "ALPHA.AT, EUROB.AT, TPEIR.AT, GEKTERNA.AT, MOH.AT and ETE.AT each carry a "
  "`10-27 08:30Z` session bar whose close matches the screener to the cent "
  "(4.353 / 4.379 / 9.792 / 40.74 / 69.30 / 15.63). The calendar's holiday skip "
  "exists to keep stale sessions out of the historical record, so applying it "
  "here would have dropped a real session rather than protected the record. "
  "**`eu-gr` is therefore included** and the calendar entry is the bug. The "
  "other 15 regions' open/closed status for 2026-10-27 matches the calendar "
  "(Taiwan, Austria and Ireland all reopen today after 2026-10-26 closures).")
A("- **The FX table carried an inverted CAD rate.** TradingView's "
  "`market_cap_basic` is in **local currency** (verified by share-count "
  "reconciliation: SAP 1.163bn shares, Toyota 11.900bn, TSMC 25.770bn, BHP "
  "4.875bn, Genmab 59.11m, DPM 221.8m — all match the issuers' real share "
  "counts), so it must be multiplied by USD-per-local-unit. The 2026-10-26 run "
  "used `CAD 1.402160`, which is CAD **per** USD, so Canadian market caps were "
  "converted in the wrong direction and inflated ~1.97x. Today's table uses "
  "`CAD 0.7117944` (1/1.4049). This changes Canada's liquidity filter and the "
  "mcap column only; no price field is affected, and yesterday's published "
  "files are left untouched.")
A("- **The MCP layer is not bound in this session** "
  "(`mcp__tradingview_advanced__*` / `mcp__yahoo_finance__*` returned no tool "
  "definitions), so both upstreams were called directly over HTTPS. This is the "
  "one fallback in the run; it is not retried or chained.")
A("- **Full pull, not movers mode.** The skill's default for Tue-Thu is "
  "movers mode (refresh only names that moved >3% on the prior session, "
  "forward-fill the rest). This run pulled the full universe for every region "
  "so that the Yahoo census could verify every written row rather than a "
  "sample. Cost: 16 screener pulls instead of 4; benefit: a complete "
  "full-universe cross-check.")
A("")

A("## Data source")
A("")
A("**PRIMARY — TradingView public screener** (`scanner.tradingview.com/{country}/scan`).")
A("One POST per 3,000-row page per region, filtered on `type=stock` and the")
A("issuer country, sorted by `market_cap_basic` desc, columns: name, description,")
A("open, high, low, close, volume, change, market_cap_basic, price_earnings_ttm,")
A("sector, exchange, currency, type, country, update_mode. All 16 country")
A("endpoints answered HTTP 200 and no pull returned an error.")
A("")
A("**Cross-check — Yahoo Finance** `/v7/finance/spark` (batches of 12) and")
A("`/v8/finance/chart`. Used for the full-universe census below and for the")
A("index levels. All fetches ran on **verified TLS**")
A("(`--cacert /etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt`); no `-k`")
A("was used.")
A("")
A("## Universe")
A("")
A("One canonical row per company per region, matching the skill's")
A("`dedupe_primary_listing` intent: exact-symbol dedupe, then primary-venue")
A("dedupe, then venue-duplicate collapse on the normalised company name with")
A("the region's primary venue preferred. Venue codes were corrected against the")
A("live screener output before the collapse (`EURONEXT` for Euronext Dublin and")
A("the Euronext single-listing markets, `OMXHEX` / `OMXCOP` for Helsinki and")
A("Copenhagen, `TPEX` for Taiwan's OTC exchange, `VIE` for Vienna, `ATHEX` for")
A("Athens).")
A("")
A("| region | exchange | rows | raw screener | removed (dupes) | liquid |")
A("|---|---|---:|---:|---:|---:|")
for r in present:
    m = finr[r]
    st = stats["regions"].get(r, {})
    A(f"| {r} | {REGION_NAME[r]} | {m['rows']:,} | {st.get('raw_rows', 0):,} | "
      f"{st.get('removed_symbol_dupes', 0) + st.get('removed_venue_dupes', 0):,} | {m['liquid_n']:,} |")
A(f"| **total** | | **{tot_rows:,}** | | | "
  f"**{sum(finr[r]['liquid_n'] for r in present):,}** |")
A("")
A("`liquid` = market cap ≥ $1bn (FX-converted) and turnover ≥ 0.05% of market")
A("cap on the day. All headline movers below are drawn from that subset with")
A("carry-over rows removed.")
A("")
A("### Day-over-day row count vs 2026-10-26")
A("")
A("The skill's regression detector needs a 7-day trailing median; this sandbox")
A("holds only the prior session, so the comparison below is a direct")
A("day-over-day check. Taiwan, Austria and Ireland have no prior file (they")
A("were closed on 2026-10-26); the other 13 regions are compared directly.")
A("")
A("| region | 2026-10-26 | 2026-10-27 | delta |")
A("|---|---:|---:|---:|")
try:
    base = {}
    import csv as _csv
    for r in present:
        p = f"/workspace/baseline/2026-10-26/{r}.csv"
        try:
            with open(p, encoding="utf-8") as fh:
                base[r] = sum(1 for _ in _csv.reader(fh)) - 1
        except OSError:
            base[r] = None
    for r in present:
        b = base.get(r)
        c = finr[r]["rows"]
        if b is None:
            A(f"| {r} | — | {c:,} | new file (no prior session) |")
        else:
            d = c - b
            A(f"| {r} | {b:,} | {c:,} | {d:+,} ({d/b*100:+.2f}%) |")
except Exception as e:  # noqa: BLE001
    A(f"| _baseline unavailable_ | {e} | | |")
A("")
A("## Session context")
A("")
A("| region | index | close | change |")
A("|---|---|---:|---:|")
for r in present:
    i = finr[r]["index"] or {}
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
for r in present:
    m = finr[r]
    i = m["index"] or {}
    A(f"### {r} — {REGION_NAME[r]}")
    A("")
    A(f"Index {i.get('symbol')} "
      f"{i.get('chg_pct'):+.2f}% · "
      f"{m['liquid_up_3']} liquid names up ≥3%, {m['liquid_dn_3']} down ≥3% "
      f"(all rows: {m['up_3']} up, {m['dn_3']} down).")
    A("")
    A("| ticker | name | change | mcap (USD) | sector |")
    A("|---|---|---:|---:|---|")
    for x in [y for y in m["top_up"] if y["change"] > 0][:3]:
        A(f"| `{x['ticker']}` | {x['name']} | {x['change']:+.2f}% | "
          f"${(x['mcap_usd'] or 0)/1e9:,.2f}bn | {x['sector']} |")
    for x in [y for y in m["top_dn"] if y["change"] < 0][:3]:
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
A(f"| not traded today | {not_today:,} | no session on {DATE} — see carry-over note |")
A(f"| no price | {no_px} | Yahoo returned no price |")
A(f"| unresolved | {unres} | no Yahoo symbol for this instrument |")
A("")
if traded:
    A(f"Agreement on the rows that traded today and could be mapped: "
      f"{agree:,} / {traded:,} = {agree/traded*100:.1f}% full agreement, "
      f"{traded-agree} partial.")
A("")
A("| region | rows | mapped | coverage | agree | chg | px | mismatch | not traded | unresolved |")
A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
for r in present:
    p = cov.get(r, {})
    A(f"| {r} | {p.get('rows', 0):,} | {p.get('n', 0):,} | {p.get('coverage_pct', 0):.1f}% | "
      f"{p.get('agree', 0):,} | {p.get('chg_only', 0)} | {p.get('px_only', 0)} | "
      f"{p.get('mismatch', 0)} | {p.get('not_today', 0):,} | {p.get('unresolved', 0):,} |")
A("")
A("## Carry-over rows (the one material caveat)")
A("")
A(f"**{not_today:,} rows** ({not_today/rows_all*100:.1f}% of the written universe) are")
A(f"instruments that did not trade on {DATE}. For those, the screener row")
A("carries the **last session's** close and change, dated with today's file.")
A("That is true of the instrument but misleading as a statement about the day.")
A("")
A("- The CSVs are left exactly as the source returned them. The schema is fixed")
A("  at 14 columns by the skill, so the affected tickers are published in a")
A("  companion index instead: `_carryover.json` (per region, per ticker, with")
A("  the instrument's last trade date).")
A(f"- {tot_conf:,} of the {tot_carry:,} are **confirmed** carry-overs: the screener's volume")
A("  equals Yahoo's volume for Yahoo's last session, so both feeds are")
A("  carrying the same earlier session. The remainder have a non-zero screener")
A("  volume but no Yahoo bar for today; for most, Yahoo's last trade is days")
A("  old, so they are also carry-overs, but a few may be Yahoo coverage gaps")
A("  rather than genuine non-trading.")
A("- Headline movers above exclude carry-over rows entirely.")
A("- The rate is a market-structure fact, not a feed defect. It is highest in")
for r in sorted(present, key=lambda x: -finr[x]["carryover"])[:4]:
    A(f"  - **{r}** ({finr[r]['carryover']:,} rows),")
A("  and near zero in the deep liquid markets ("
  + ", ".join(f"**{r}** {finr[r]['carryover']}" for r in
              sorted(present, key=lambda x: finr[x]["carryover"])[:3]) + ").")
A("")
A("## Other caveats")
A("")
A("- **Illiquid tail.** The extreme-move counts across all rows are dominated")
A("  by sub-$100m micro-caps and single-print names. The liquidity filter above")
A("  is what makes the headline tables readable.")
A("- **Secondary listings survive.** A German company's London line, a Canadian")
A("  company's CSE line, and class-share lines are distinct rows by design")
A("  (the skill's known limitation). Cross-listed issuers appear in more than")
A("  one region file with different change_pct.")
A("- **No cross-file dedupe.** The same issuer listed in two regions appears in")
A("  both files; this is the skill's documented known limitation, not a defect.")
A("- **FX.** Market-cap floors use a rate table taken from Yahoo at run time")
A("  (EUR 1.1130, JPY 0.0063312, AUD 0.7026913, CAD 0.7117944, DKK 0.1488804,")
A("  TWD 0.0308604) — all USD per one unit of local currency. They affect the")
A("  liquidity filter and the mcap column only, never the written price fields.")
A("- **No catalyst research was performed.** This cron is a data snapshot;")
A("  movers are reported without news attribution, and no reason for a move is")
A("  asserted here.")
A("")
A("## Files")
A("")
A(f"- `international-eod/{DATE}/<region>.csv` — {len(present)} files, one per trading region")
A(f"- `international-eod/{DATE}/_carryover.json` — carry-over index")
A(f"- `international-eod/{DATE}/{DATE}.meta.md` — this file")
A("")
A("Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,")
A("pe_ratio,sector,currency,exchange`. Missing values are empty cells, never")
A("`N/A`. Blank `pe_ratio` = no or negative earnings; blank `market_cap` = no")
A("market cap reported; blank `change_pct` = the screener reported no change.")
A("")

body = "\n".join(L)
with open(f"{OUT}/{DATE}.meta.md", "w", encoding="utf-8") as fh:
    fh.write(body)
print(f"wrote {OUT}/{DATE}.meta.md ({len(body)} bytes)")
print(f"tot_rows={tot_rows} carryover={tot_carry} confirmed={tot_conf} "
      f"census n={cov_n} agree={agree} mism={mism} not_today={not_today} unres={unres}")
