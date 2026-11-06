---
date: 2026-11-06
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-06
focus_dir_date: 2026-11-05
screen_data_date: 2026-11-04
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: StockTwits chart_data (period 1D 5-minute bars and 1W 30-minute bars, regular session only) for today and the prior-session feed bridge; polygon/Massive 5-minute aggregates via the Pipeworx gateway for the prior-10 baseline; Nasdaq /chart + /historical (consolidated price at 09:45 ET and consolidated daily volume) as the independent price and daily-volume checks; Cboe delayed-quote CDN (09:31 ET regular-session snapshot) as the independent volume cross-check; TradingView america scanner (average_volume_10d_calc, denominator only)
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET (15 of 390 session minutes). The Yahoo chart API (the contract's primary intraday path) hard-429s from this egress and polygon/Massive publishes no session for 2026-11-06, so today's window comes from the StockTwits intraday feed (regular session only) and the prior-10 baseline from polygon 5-minute aggregates. The StockTwits feed publishes volume for the 09:30 and 09:35 bars but not for the 09:40 bar, so the 09:30-09:45 window is reconstructed from the feed's complete 09:30-10:00 30-minute bar by subtracting the 09:45-10:00 tail, whose share is taken from the name's own prior-10 profile (per-name band published in the CSV). The two feeds are bridged by f30 = mean over the prior sessions of StockTwits' 09:30-10:00 bar divided by polygon's 09:30-10:00 sum, so the window comparison is like-for-like. Scale factor: prior-10 mean consolidated daily volume (Nasdaq /historical) divided by TV average_volume_10d_calc (the only TV field used). rvol_intraday_live = consolidated-equivalent window volume / TV average_volume_10d_calc (reference only - never bucket on it). rvol_prev is the same metric at the earlier 09:30-09:35 ET snapshot, normalised against the prior-10 mean of that SAME 5-minute window; rvol_at_09_38 is the raw un-normalised cumulative ratio at that earlier snapshot. Pre-market prints are excluded by construction (both intraday feeds are regular-session only), so pm_vol = 0 and pm_vol_source = not_subtracted. Trend epsilon: |delta| <= 0.05 = STABLE.
metric_def: rvol_tod_normalised = (today's 09:30-09:45 ET window volume / (f30 x prior-10 mean same-window volume)) x (prior-10 mean consolidated daily volume / TV average_volume_10d_calc); rvol_intraday_live = consolidated-equivalent window volume / TV average_volume_10d_calc; rvol_prev = the same formula over the 09:30-09:35 ET window
bucket_rule: rvol_tod_normalised >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's published reading.
pm_source_status: not_subtracted
cross_check_source: same_series_truncated
status: ok
upstream: daily-screens/2026-11-05/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-06 09:45 ET (cron #07)

## TL;DR

- **2 of 12** focus names are in the **RVOL Required** bucket (rvol_now >= 1.5): CRCT 2.12x, OUST 1.92x.
- **Near misses: 0.** **Alerts: 0** - yesterday's snapshot published no rvol_now for any of today's 12 names (the roster turned over completely again), so no crossing can be claimed; the names above the bar carry tier WATCH, not ALERT.
- **The caveat that changes how this reads:** the contract's primary intraday path (Yahoo chart) hard-429s from this egress and polygon/Massive has not published 2026-11-06 at all, so today's window was rebuilt from the StockTwits intraday feed. Its 09:40 bar carries no volume, so the 09:30-09:45 window is reconstructed from the feed's complete 09:30-10:00 bar; the estimate is tight for 7 of 12 names (band <= 13%: CRCT, ENOV, DUOL, YOU, KD, LIVN, XNCR) and wide for OUST (1.48-2.88x), which straddles the 1.5x bar.
- **Both Required names are front-loaded, not accumulating.** CRCT ran 4.70x its own 5-minute norm in the first bar and only 2.12x its 15-minute norm - the opening burst is fading into the tape. Same story for OUST (2.76x -> 1.92x). A Required reading here is an opening-auction spike, not sustained demand.
- The price is the 09:45 ET print; Nasdaq's independent consolidated 09:45 ET print agrees within 0.25% on 5 of 12 names (worst: ENOV 1.9%).

## Universe

12 names from `daily-screens/2026-11-05/focus.md` - the most recent completed 18:30 ET sweep (Thu 2026-11-05, 12 names). `focus_dir_date` = 2026-11-05; the sweep's own screen data date = **2026-11-04** (shibui T+1), read from the focus.md header, not inferred from the folder name. `lag_sessions` = **1** trading session - the normal weekday T+1 ingest, not a degradation. All 12 names were priced (no `no_intraday_bars`).

## Table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRCT | 8.98 | 0.1145 | 2.1246 | 4.6953 | 0.1002 | DECELERATING (-2.57) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OUST | 33.315 | 0.0971 | 1.9226 | 2.7612 | 0.0632 | DECELERATING (-0.84) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XYZ | 85.27 | 0.0368 | 0.6824 | 0.9823 | 0.0281 | DECELERATING (-0.30) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ENOV | 27.03 | 0.0186 | 0.6480 | 1.3997 | 0.0165 | DECELERATING (-0.75) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DUOL | 156.045 | 0.0288 | 0.4968 | 0.7748 | 0.0258 | DECELERATING (-0.28) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| YOU | 55.82 | 0.0180 | 0.3941 | 0.9226 | 0.0173 | DECELERATING (-0.53) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HELE | 37.06 | 0.0149 | 0.3067 | 0.6458 | 0.0122 | DECELERATING (-0.34) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KD | 15.69 | 0.0156 | 0.3049 | 0.5949 | 0.0133 | DECELERATING (-0.29) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LIVN | 90.47 | 0.0069 | 0.1361 | 0.2832 | 0.0069 | DECELERATING (-0.15) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ARRY | 5.54 | 0.0137 | 0.1336 | 0.1532 | 0.0090 | STABLE (-0.02) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VRDN | 28.07 | 0.0092 | 0.1336 | 0.2755 | 0.0076 | DECELERATING (-0.14) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XNCR | 34.21 | 0.0043 | 0.1335 | 0.2691 | 0.0041 | DECELERATING (-0.14) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-06 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts

- Universe size: **12**
- RVOL Required (rvol_now >= 1.5): **2** (CRCT, OUST)
- Liquid: **10**
- NEAR MISS (1.275-1.5): **0**
- Alerts: **0**
- Crossings proven: **0**
- UNADJUSTED rows (pre-market not subtracted): **0**

## Alerts

**none** - and the reason matters: `daily-screens/2026-11-05/focus-rvol-snapshot.csv` published an `rvol_now` for 12 names (FN, EVER, APLD, AEHR, CIFR, AEIS, ECG, CLSK, FISV, BETA, CORZ, FRVO) and **none of them is in today's universe**. The roster turned over completely for the second session running, so `prev_session_rvol` is `n/a` on every row and a crossing cannot be claimed for anyone. CRCT and OUST are above the 1.5x bar as LEVELS, not as crossings, and are reported as tier WATCH.

## Near misses

**none** - no name sits in the 1.275-1.5x band. The closest miss below the band is XYZ at 0.68x; the closest above it is OUST at 1.92x (band 1.48-2.88x). Any of them turning into an alert needs rvol_now >= 1.5 while prev_session_rvol stays below 1.5 - and on 2026-11-07 the baseline will exist only for names that are in tomorrow's roster AND in today's.

## Universe change

Versus the previous sweep (`daily-screens/2026-11-04/focus.md`, 12 names):

- Entered (12): ARRY, CRCT, DUOL, ENOV, HELE, KD, LIVN, OUST, VRDN, XNCR, XYZ, YOU
- Left (12): AEHR, AEIS, APLD, BETA, CIFR, CLSK, CORZ, ECG, EVER, FISV, FN, FRVO
- Overlap: **0** - complete turnover for the second session running, which is why the previous session's baseline covers none of today's names.

## Method

- Metric: `rvol_tod_normalised` (time-of-day-normalised). Today's window is 09:30-09:45 ET - 15 of 390 session minutes - and is compared with the SAME clock window on the prior 10 sessions (2026-10-23 to 2026-11-05), then scaled to full-day units.
- Today's volume: StockTwits `chart_data` period 1D (5-minute bars, 78 per symbol, regular session only - the first bar is stamped 09:30 ET and the last 16:00 ET) and period 1W (30-minute bars, 09:30-10:00 plus the rest of the session). The feed publishes volume for the 09:30 and 09:35 bars and **zero for the 09:40 and 09:45 bars** on every symbol, so the 09:30-09:45 window is reconstructed from the complete 09:30-10:00 30-minute bar minus the 09:45-10:00 tail, whose share comes from the name's own prior-10 profile. Per-name bands (rvol_lo / rvol_hi in the CSV): 7 of 12 names are within 13%; OUST 1.48-2.88x, ARRY 0.10-0.16x, HELE 0.26-0.38x, VRDN 0.12-0.16x are wide.
- Prior sessions: polygon/Massive 5-minute aggregates via the Pipeworx gateway, 2026-10-19 to 2026-11-07 (13 sessions available; the most recent 10 are used), regular-session 09:30-16:00 sums for full-day volume and the same-window sums for the baseline. **polygon has no session for 2026-11-06** - the `to` bound is exclusive and the upstream has not published today - so it cannot supply the fire window at all.
- Cross-feed bridge: `f30` = mean over the prior sessions of StockTwits' 09:30-10:00 bar divided by polygon's 09:30-10:00 sum; per name 0.69-0.94. It is applied so today's window is compared with the baseline like-for-like.
- Scale factor: prior-10 mean consolidated daily volume (Nasdaq `/historical`) divided by TV `average_volume_10d_calc` (the only TV field used; TV's live columns lag the session and are never used for a live field). The factor lands at 1.03-1.08 for all 12 names - a name at its own normal pace prints ~1.0x, which is the sanity check that the two volume bases agree.
- Independent checks: the Cboe delayed-quote CDN (consolidated regular-session-only volume, snapshot 09:30:11-09:31:22 ET) sits at or below the StockTwits 09:30 bar on 11 of 12 names and within 0.03% on the twelfth (HELE 6,776 vs 6,774) - the independent consolidated tape confirms today's opening volume without contradicting it; Nasdaq `/chart` supplies a consolidated price at 09:45 ET (agrees with the StockTwits 09:40-bar close within 0.25% on 5 of 12 names - YOU 0.01%, KD 0.06%, CRCT 0.22%, HELE 0.23%, ARRY 0.23% - and within 1% on 11 of 12, worst ENOV 1.89%) and a cumulative session volume at 10:01 ET.
- Cross-check snapshot: the earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 5-minute window (`cross_check_source: same_series_truncated`). The Cboe snapshot was 09:31 ET - earlier than the fire - but it covers only ~77 seconds of session, too short to normalise against a prior-10 mean without inventing the shape of the minute, so it is used as the independent volume check instead. The column keeps the contract's fixed name `rvol_at_09_38`; today's earlier snapshot is the 09:30-09:35 ET slot.
- Pre-market: excluded by construction (both intraday feeds are regular-session only), so `pm_vol` = 0 and `pm_vol_source` = `not_subtracted`; no dependency on cron #08. Checked explicitly: XYZ's pre-market volume (205,714 shares, cron #08) cannot be inside its 145,702-share 09:30 bar, which proves the feed excludes it.
- Trend: `ACCELERATING` / `STABLE` / `DECELERATING` with the numeric delta; |delta| <= 0.05 is STABLE. Each reading is normalised against its own prior-10 mean for its own window, so a negative delta means today's volume arrived MORE front-loaded than that name's own history - the opening burst is fading, not building.
- Tier vocabulary: `ALERT` = a proven crossing; `NEAR MISS` = 1.275-1.5x; `WATCH` = at or above 1.0x but not an alert, which includes names above the 1.5x bar with no prior-session baseline; `-` = below 1.0x; `UNADJUSTED` = pre-market not subtracted (0 rows today).

## Source health

| source | url / query | status |
|---|---|---|
| Yahoo chart API (contract's primary intraday path) | query1/query2 /v8/finance/chart, interval=5m, range=1mo | failed: HTTP 429 on every request, cookie+crumb handshake returns `Too Many Requests` on both hosts - replaced by the two feeds below |
| polygon / Massive aggregates (Pipeworx gateway) | polygon-io `aggregates`, 5m, 2026-10-19..2026-11-07 | ok 12/12 symbols for the prior sessions; **no session published for 2026-11-06** |
| StockTwits chart_data 1D (today, 5m bars) | stocktwits `chart_data` period 1D | ok 12/12, 78 bars each; volume published for the 09:30 and 09:35 bars only, zero for 09:40/09:45 |
| StockTwits chart_data 1W (30-min bars) | stocktwits `chart_data` period 1W | ok 12/12 (5 sessions each + today's 09:30-10:00 bar); OUST's 30-minute bar is missing from the feed |
| TradingView america scanner | POST scanner.tradingview.com/america/scan, `average_volume_10d_calc` | ok, 19,929 rows, 12/12 matched (a ticker filter returns 0 rows on this endpoint) |
| Nasdaq /chart (price at 09:45 ET) | api.nasdaq.com/api/quote/{SYM}/chart | ok 12/12 |
| Nasdaq /historical (consolidated daily volume) | api.nasdaq.com/api/quote/{SYM}/historical | ok 12/12 - CRCT 11-05 = 3,659,459, identical to the StockTwits daily series |
| Cboe delayed-quote CDN | cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json | ok 12/12, snapshot 09:30:54-09:31:22 ET (regular session only) - independent volume cross-check |
| bridge market-recap get_quotes | Pipeworx gateway | ok, market_state open, as_of stamped (used as a price/volume probe) |
| MCP availability probe | probe_mcp.py | catalog_ok, finance_tools=0 - the mcp__* names are absent, the servers are reached over the bridge |

## Degradation / caveats

- **Yahoo was unavailable and polygon had no session for today.** The contract's primary intraday source returned HTTP 429 from this egress all session, and the consolidated 5-minute feed had published nothing for 2026-11-06 by the end of the run. Today's window therefore comes from the StockTwits intraday feed, bridged to the polygon baseline by a measured per-name factor.
- **The fire window is reconstructed, not read.** The feed publishes no volume for the 09:40 bar, so the 09:30-09:45 window was rebuilt from the feed's complete 09:30-10:00 bar minus a profile-estimated 09:45-10:00 tail. For 7 of 12 names the resulting band is <= 13% of the value and cannot change a bucket. For **OUST the band is 1.48-2.88x** (the 30-minute bar was missing from the feed, so its window was scaled from the published 5-minute bars) - OUST's RVOL Required placement is the least certain number in this artifact, and it straddles the 1.5x bar.
- **No alert baseline.** The previous session's snapshot shares no ticker with today's universe, so `prev_session_rvol` is `n/a` on every row, the alert tier is empty, and no crossing is claimed. The 1.5x names are LEVELS, not crossings.
- **The trend compares two different window lengths** (the earlier reading is the 5-minute 09:30-09:35 slot, the fire reading is the 15-minute 09:30-09:45 window). Each is normalised against its own prior-10 mean, so a negative delta genuinely means front-loading, but the magnitude is amplified relative to the previous session's published deltas - the two `rvol_now` / `rvol_prev` numbers are the real data, the delta is directional.
- **rvol_prev is on the 5-minute slot, not the contract's 09:38 stamp.** The column name is fixed by the contract; today's earlier snapshot is the 09:30-09:35 ET slot.
- **In-progress bars dropped.** No bar stamped after 09:40 ET contributes any volume, and the feed's zero-volume trailing bars were excluded.
- `rvol_intraday_live` is published for reference only and is mechanically tiny at 09:45 (15 of 390 session minutes). Never bucket on it.
