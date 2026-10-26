---
date: 2026-10-26
cron: "#7 stock-screener-focus-rvol-09:45"
fire_time_et: "2026-10-26 09:45 ET"
data_date: 2026-10-22
upstream_focus_md: /workspace/daily-screens/2026-10-23/focus.md
upstream_cron_date: 2026-10-23
upstream_generated: "2026-10-23T11:39Z"
source: "yahoo_finance_chart_api (5m intraday) + tradingview_public_scanner (average_volume_10d_calc denominator)"
method: intraday_rvol_yahoo_5m
status: ok
rvol_required_count: 0
liquid_count: 4
no_data_count: 1
alert_emitted: false
---

# Focus RVOL snapshot — 2026-10-26 09:45 ET

**Empty "RVOL Required" bucket — and that is the expected result at 09:45, not a quiet tape.** The contract metric
normalizes cumulative volume-to-date against a *full day's* average volume, and only 21 minutes (5.4%) of the
390-minute regular session had elapsed when the data was captured. A cumulative-to-full-day ratio of 3.0 is
arithmetically unreachable before roughly 10:30 ET. The supplementary pace-adjusted column below shows which names
are actually trading at a 3x-or-better full-day pace: **MRNA (4.08x)** and **CD (3.30x)**.

**The focus list is two sessions stale.** It comes from the 2026-10-23 sweep, whose data date is **2026-10-22**
(Thursday). The 2026-10-23 session has since closed and today's session is in progress, so these are names that were
hot on 10-22 — not a list built for this morning. The 2026-10-24 sweep produced no `focus.md`, and today's 18:30
sweep has not run yet.

## Snapshot

| Symbol | Close | RVOL | Bucket | Data timestamp (ET) |
| --- | ---: | ---: | --- | --- |
| MRNA | 198.50 | 0.2251 | Liquid | 2026-10-26 09:51:32 |
| CD | 9.075 | 0.1780 | Liquid | 2026-10-26 09:51:03 |
| KOD | 89.50 | 0.0336 | Liquid | 2026-10-26 09:51:29 |
| XLAB | 3.361 | 0.0188 | Liquid | 2026-10-26 09:51:01 |
| TJGC | — | — | no_data | no intraday bars |

Sorted by RVOL descending. Closes are live regular-session prints; every data timestamp is the payload's own quote
stamp, not the cron's fire time.

## Counts

| Bucket | Count | Tickers |
| --- | ---: | --- |
| RVOL Required (RVOL >= 3) | 0 | — |
| Liquid (RVOL < 3) | 4 | MRNA, CD, KOD, XLAB |
| No data | 1 | TJGC |
| **Total focus names** | **5** | |

**Alert:** none. No ticker crossed from below 1 to above 3. The upstream prior RVOLs were XLAB 2.51, MRNA 2.50,
KOD 0.43, TJGC 1.18, CD 0.74 — all below the 3.0 threshold, and no current reading exceeded it either, so no
crossing occurred on either side of the bar.

## Supplementary — pace-adjusted RVOL (NOT the contract metric)

The contract RVOL is cumulative-volume-to-full-day-average. Dividing it by the fraction of the session elapsed
(5.4% at capture) converts it to a full-day pace, which is what the 3.0 threshold was designed to express.

| Symbol | RVOL (contract) | Session elapsed | Pace-adjusted RVOL | Pace vs 3.0 |
| --- | ---: | ---: | ---: | --- |
| MRNA | 0.2251 | 5.5% | 4.08 | above |
| CD | 0.1780 | 5.4% | 3.30 | above |
| KOD | 0.0336 | 5.5% | 0.61 | below |
| XLAB | 0.0188 | 5.4% | 0.35 | below |

This table is context for reading the empty bucket. It was **not** used for bucketing, and no name was reclassified
on the basis of it.

## Method

- **Numerator (intraday):** Yahoo Finance chart API, `interval=5m`, `range=1d`, one request per symbol against
  `query1.finance.yahoo.com/v8/finance/chart/<SYM>`. Bars were filtered to the regular session
  (09:30–16:00 ET, session date 2026-10-26). Cumulative volume is the sum of every bar's volume, including the
  still-forming 09:50 bar.
- **Denominator:** TradingView public scanner (`POST scanner.tradingview.com/america/scan`), column
  `average_volume_10d_calc`, pulled live at ~09:55 ET, as the cron spec requires.
- **Bar hygiene:** `includePrePost=false` was sent, so no pre-market bars were present; 0 bars were dropped as
  future-dated and 0 as outside the session. The trailing bar Yahoo stamps with the quote time carried volume 0,
  so it did not distort any cumulative figure. The last fully closed 5-minute bar in every payload started at
  09:45:00. Data was captured between 09:51:01 and 09:51:32 ET.
- **Denominator validation:** TV's `average_volume_10d_calc` was cross-checked against Yahoo's own trailing
  10-session average, computed from 1-day bars. Agreement was XLAB 0.999x, MRNA 1.057x, KOD 1.125x, CD 1.133x —
  TV's column is the tighter, more conservative denominator for two names (KOD, CD), so those RVOLs are mildly
  overstated relative to a Yahoo-computed denominator.
- **Prior-RVOL reference for the crossing test:** taken from the upstream `focus.md` RVOL column (data date
  2026-10-22).
- **Not used:** the `mcp__tradingview__*`, `mcp__tradingview_advanced__*` and `mcp__yahoo_finance__*` servers
  remain absent in Cloud sessions, so the skill's step-7 `coin_analysis` path was not available and the documented
  Yahoo path was used instead. The TV scanner's live quote fields (`close`, `volume`, `relative_volume_10d_calc`)
  were **not** used for prices or volumes — TV's quote stream lagged Yahoo by several minutes in this run — and
  `relative_volume_10d_calc` was not used for any bucket.

## Degradation and gaps

1. **TJGC — `no_intraday_bars`.** Not a fetch failure and not a substituted daily value. Yahoo returned HTTP 200
   with **zero** timestamps for `range=1d`; a `range=5d` probe returned exactly one bar, stamped 2026-10-22 16:00
   (the prior session's close); Yahoo's `regularMarketTime` for the symbol is 2026-10-22 16:00; and the TV
   scanner's TJGC row was byte-identical across two pulls nine minutes apart. TJGC has not traded today as of
   09:51 ET and both vendors are carrying the 2026-10-22 close ($31.89). It is excluded from both buckets.
2. **Yahoo API access required a cookie + crumb handshake.** Every unauthenticated chart request returned
   HTTP 429 (`query1` and `query2` alike), including single-symbol probes. A `fc.yahoo.com` cookie jar plus
   `/v1/test/getcrumb` crumb returned HTTP 200. The crumb-based path succeeded for all five symbols on the first
   attempt; the 429 retry ladder was not needed once the crumb was in place. Recorded because the next scheduled
   run will hit the same wall.
3. **Upstream focus list is two sessions stale** (data date 2026-10-22 vs fire date 2026-10-26), as described in
   the header. The upstream sweep itself ran degraded — its header records `_source=tv_fallback+yahoo_verify`,
   since the MCP tier was also unconnected in that Cloud session — and its closes were confirmed against Yahoo's
   2026-10-22 session close for all five names.
4. **No degradation of the contract metric.** The primary intraday path was used, so `status` is `ok`; the
   `degraded_daily_rvol_proxy` state was not entered at any point.

## Files

- This artifact: `/workspace/daily-screens/2026-10-26/focus-rvol-snapshot.md`
- Parser and raw captures: `/workspace/parse_rvol.py`, `/workspace/data/rvol/` (intermediates, git-ignored)
