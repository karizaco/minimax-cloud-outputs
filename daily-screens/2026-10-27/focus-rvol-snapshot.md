---
date: 2026-10-27
cron: "#7 stock-screener-focus-rvol-09:45"
fire_time_et: "2026-10-27 09:45 ET"
data_date: 2026-10-26
source: "yahoo_finance_chart_api (5m intraday) + tradingview_public_scanner (average_volume_10d_calc denominator)"
method: intraday_rvol_yahoo_5m
status: ok
upstream_focus_md: /workspace/daily-screens/2026-10-26/focus.md
upstream_cron_date: 2026-10-26
capture_window_et: "09:47:00 - 09:48:23"
rvol_required_count: 0
liquid_count: 12
no_data_count: 0
alert_emitted: false
---

# Focus RVOL snapshot — 2026-10-27 09:45 ET

**The RVOL Required bucket is empty, and this one is a real read rather than a clock artifact.** The contract metric
normalizes cumulative volume-to-date against a *full day's* average volume, so at capture only 18.4 minutes (4.7%) of
the 390-minute regular session had elapsed — a raw RVOL of 3.0 was arithmetically out of reach. The
pace-adjusted column below exists to test whether the empty bucket is hiding anything, and it is not: the strongest
name, **CSCO at 1.92× full-day pace**, is still well under the 3.0 bar, and no symbol reaches 3.0 on either the
contract metric or the pace-adjusted one.

**The focus list is one session old, and it is the freshest one that can exist.** It comes from the 2026-10-26
18:30 sweep, whose data date is the settled **2026-10-26 close** (Monday). Today's sweep has not run yet — it fires
at 18:30 ET — so the list reflects yesterday's close, not this morning. Note that the 2026-10-26 directory also
contains a `focus-rvol-snapshot.md` written by *yesterday's* 09:45 run, which measured a different list (the
2026-10-23 sweep, data date 2026-10-22). This artifact is the 2026-10-27 one.

## Snapshot

| Symbol | Close | RVOL | Bucket | Data timestamp (ET) |
| --- | ---: | ---: | --- | --- |
| CSCO | 110.56 | 0.0903 | Liquid | 2026-10-27 09:48:19 |
| TENB | 47.46 | 0.0779 | Liquid | 2026-10-27 09:48:10 |
| NXPI | 250.25 | 0.0713 | Liquid | 2026-10-27 09:48:04 |
| SDGR | 25.10 | 0.0645 | Liquid | 2026-10-27 09:48:08 |
| ORKA | 92.58 | 0.0636 | Liquid | 2026-10-27 09:47:56 |
| ADI | 418.02 | 0.0627 | Liquid | 2026-10-27 09:48:15 |
| P | 133.76 | 0.0571 | Liquid | 2026-10-27 09:47:54 |
| OKTA | 220.51 | 0.0544 | Liquid | 2026-10-27 09:48:21 |
| PENG | 57.35 | 0.0495 | Liquid | 2026-10-27 09:48:23 |
| RNG | 85.89 | 0.0443 | Liquid | 2026-10-27 09:47:47 |
| FIGS | 20.23 | 0.0350 | Liquid | 2026-10-27 09:48:17 |
| HEI | 309.14 | 0.0116 | Liquid | 2026-10-27 09:47:00 |

Sorted by RVOL descending. Closes are live regular-session prints from Yahoo's chart payload; every data timestamp is
the payload's own quote stamp, not the cron's fire time. All 12 focus names returned intraday bars — there is no
`no_intraday_bars` symbol in this run.

## Counts

| Bucket | Count | Tickers |
| --- | ---: | --- |
| RVOL Required (RVOL >= 3) | 0 | — |
| Liquid (RVOL < 3) | 12 | CSCO, TENB, NXPI, SDGR, ORKA, ADI, P, OKTA, PENG, RNG, FIGS, HEI |
| No data | 0 | — |
| **Total focus names** | **12** | |

**Alert: none.** No ticker crossed from below 1 to above 3. The upstream prior RVOLs (`rvol10` in the 2026-10-26
`focus.csv`, data date 2026-10-26 close) were P 1.01, ORKA 2.43, TENB 1.64, NXPI 1.12, ADI 1.01, HEI 1.24, CSCO 1.37,
RNG 1.36, OKTA 0.73, FIGS 0.44, SDGR 0.77, PENG 0.66 — every one of them below 3.0, and no current reading is close
to 3.0 either, so no crossing occurred on either side of the bar.

## Supplementary — pace-adjusted RVOL (NOT the contract metric)

The contract RVOL is cumulative-volume-to-full-day-average. Dividing it by the fraction of the session elapsed
(4.4–4.7% at capture) converts it to a full-day pace, which is what the 3.0 threshold was designed to express. The
right-hand column substitutes Yahoo's own trailing 10-session average volume for the TV denominator, to size the
denominator's effect (see Method).

| Symbol | RVOL (contract) | Session elapsed | Pace-adjusted RVOL | RVOL on Yahoo denominator | Pace vs 3.0 |
| --- | ---: | ---: | ---: | ---: | --- |
| CSCO | 0.0903 | 4.7% | 1.92 | 0.0837 | below |
| TENB | 0.0779 | 4.7% | 1.67 | 0.0733 | below |
| NXPI | 0.0713 | 4.7% | 1.54 | 0.0663 | below |
| SDGR | 0.0645 | 4.7% | 1.39 | 0.0594 | below |
| ORKA | 0.0636 | 4.7% | 1.38 | 0.0605 | below |
| ADI | 0.0627 | 4.7% | 1.34 | 0.0585 | below |
| P | 0.0571 | 4.6% | 1.24 | 0.0518 | below |
| OKTA | 0.0544 | 4.7% | 1.16 | 0.0510 | below |
| PENG | 0.0495 | 4.7% | 1.05 | 0.0454 | below |
| RNG | 0.0443 | 4.4% | 0.97 | 0.0407 | below |
| FIGS | 0.0350 | 4.7% | 0.75 | 0.0292 | below |
| HEI | 0.0116 | 4.4% | 0.27 | 0.0104 | below |

This table is context for reading the empty bucket. It was **not** used for bucketing, and no name was reclassified
on the basis of it. Its purpose is to show that the empty bucket is not a timing artifact: the leader is 1.92× pace,
not 3.0× pace.

## Method

- **Numerator (intraday):** Yahoo Finance chart API, `interval=5m`, `range=1d`, one request per symbol against
  `query1.finance.yahoo.com/v8/finance/chart/<SYM>`. Bars were filtered to the regular session
  (09:30–16:00 ET, session date 2026-10-27). Cumulative volume is the sum of every bar's volume.
- **Denominator:** TradingView public scanner (`POST scanner.tradingview.com/america/scan`), column
  `average_volume_10d_calc`, pulled live at ~09:48 ET, as the cron spec requires. One batched POST covered all
  12 names (`totalCount` = 12, all 12 matched by ticker).
- **Bar hygiene:** `includePrePost=false` was sent, so no pre-market bars were present; **0** bars were dropped as
  future-dated and **0** as outside the session. Every payload contained 5 bars: four complete 5-minute bars
  (09:30, 09:35, 09:40, 09:45) plus one in-progress bar that Yahoo stamps with the quote time and that carries
  **volume 0**. Hand-verified on the raw ladder for P, CSCO, HEI and ADI: the in-progress bar contributes nothing to
  the cumulative sum, so no partial volume is double-counted. Data was captured between 09:47:00 and 09:48:23 ET.
- **Denominator validation:** TV's `average_volume_10d_calc` was cross-checked against Yahoo's own trailing
  10-session average volume, computed from 1-day bars over the 10 completed sessions ending 2026-10-26. TV's column
  is **consistently lower** than Yahoo's — the ratio ran 0.835 (FIGS) to 0.951 (ORKA), median 0.925 — so TV is the
  tighter, more conservative denominator, and the contract RVOLs are overstated by roughly 5–20% relative to a
  Yahoo-computed denominator. The direction of the bias is stated because it inflates RVOL; it does not change any
  bucket, since no name is near 3.0 under either denominator.
- **Prior-RVOL reference for the crossing test:** the upstream `focus.csv` `rvol10` column (data date 2026-10-26).
  Caveat: that column is a *daily* relative volume (settled full-day volume against its 10-day average), whereas
  today's reading is intraday cumulative-to-date, so the two are not strictly the same metric. The comparison is
  nonetheless unambiguous in this run — the largest prior value was 2.43 and the largest current value is 0.0903,
  and no name crosses the 3.0 bar under either the contract metric, the pace-adjusted metric, or the daily-prior
  metric.
- **Not used:** the `mcp__tradingview__*`, `mcp__tradingview_advanced__*` and `mcp__yahoo_finance__*` servers
  remain absent in Cloud sessions, so the skill's step-7 `coin_analysis` path was not available and the documented
  Yahoo path was used instead. The TV scanner's live quote fields (`close`, `volume`, `relative_volume_10d_calc`)
  were **not** used for prices or volumes — TV's quote stream lagged Yahoo in this run (ADI read 413.68 on TV
  against Yahoo's 418.02) — and `relative_volume_10d_calc` was not used for any bucket.

## Degradation and gaps

1. **No degradation of the contract metric.** The primary intraday path was used end to end, so `status` is `ok`;
   the `degraded_daily_rvol_proxy` state was not entered at any point. The TV scanner's
   `relative_volume_10d_calc` column was not substituted for anything.
2. **Yahoo API access required a cookie + crumb handshake.** Every unauthenticated chart request returns HTTP 429
   from this sandbox. A `fc.yahoo.com` cookie jar (its 404 response still sets the jar) plus an 11-character crumb
   from `/v1/test/getcrumb` returned HTTP 200 for all 12 symbols on the first attempt; the 429 retry ladder was
   never needed. Recorded because the next scheduled run will hit the same wall.
3. **Two TradingView scanner request-shape gotchas were hit and fixed** (both would silently corrupt a run):
   an `active_symbol` filter is rejected with HTTP 400, and the response carries **no `columns` array** — each row
   is a positional `d` array matching the requested column order, so parsing it as though `columns` were present
   collapses all 12 rows into a single empty record and yields 11 `null` denominators. The scanner payload was
   re-parsed positionally and re-validated (`totalCount` = 12).
4. **The focus list is one session old** (data date 2026-10-26 vs fire date 2026-10-27), as described in the
   header. This is the normal T+1 lag for a list produced by the 18:30 ET sweep, not a failure. The upstream sweep
   itself ran on the tier-2 fallback path (its own header records the MCP tier unbound) and reported **no session
   lag** — every price in it is the settled 2026-10-26 close.
5. **HEI's tape is thin.** Its 09:30 bar carried volume 0 in the verification pull and its cumulative volume at
   capture was 5,048 shares — 1.2% of a full day's average, 0.27× full-day pace. That is a real reading of a quiet
   name, not a fetch failure.
6. **No `no_data` symbols and no fetch errors.** All 12 chart requests returned HTTP 200 with live bars, and the
   Yahoo error list for this run is empty.

## Files

- This artifact: `/workspace/daily-screens/2026-10-27/focus-rvol-snapshot.md`
- Fetch + parse script: `/workspace/parse_rvol.py`
- QC script (bar ladder + denominator cross-check): `/workspace/qc_rvol.py`
- Raw captures: `/workspace/data/rvol/` (intermediates, git-ignored)
