---
date: 2026-11-09
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-09
focus_dir_date: 2026-11-06
screen_data_date: 2026-11-05
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars, interval=5m&range=1mo&includePrePost=false (session volume and the 09:45 ET price) + TradingView america scanner average_volume_10d_calc (denominator only) + Nasdaq /historical (consolidated daily volume for the prior-10 scale factor) + Nasdaq /chart (independent 09:45 ET price print) + Cboe delayed-quote CDN (independent earlier-volume and price cross-check) + bridge market-recap get_quotes (live price/volume corroboration) + cron #08 pre-market-gapper.csv (pre-market exclusion cross-check)
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET - 15 of 390 session minutes - and is compared with the SAME clock window on the prior 10 sessions, then scaled to full-day units by the prior-10 mean consolidated daily volume divided by TV average_volume_10d_calc. The earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 5-minute window; the Cboe delayed snapshot (own timestamp 09:34:20-09:36:40 ET) is the independent corroboration of that slot.
metric_def: rvol_tod_normalised = (cumulative volume 09:30 -> the fire's bar, today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 sessions) x (mean full-day volume across those prior 10 sessions / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the fire bar / TV average_volume_10d_calc (reference only, never bucketed); rvol_prev = the same formula over the 09:30-09:35 ET slot against the prior-10 mean of that slot; rvol_at_09_38 = the raw cumulative ratio at the earlier snapshot
bucket_rule: rvol_tod_normalised >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's published reading.
pm_source_status: not_subtracted
cross_check_source: same_series_truncated
status: ok
upstream: daily-screens/2026-11-06/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-09 09:45 ET (cron #07)

## TL;DR

- **1 of 12** focus names are in the **RVOL Required** bucket (rvol_now >= 1.5): WRBY 2.39x. **Near misses: 2** (XERS 1.42x, ACHC 1.35x).
- **Alerts: 0.** The reason matters more than the count: the roster turned over again - only 2 of 12 names (VRDN, XNCR) have a prior-session reading in `daily-screens/2026-11-06/focus-rvol-snapshot.csv`, and both sit far below the bar. The one Required name (**WRBY**) has **no prior reading at all**, so its 2.39x is a LEVEL, not a crossing - it carries tier WATCH, not ALERT.
- **The caveat that changes how this reads:** the universe is **Friday's** sweep (`daily-screens/2026-11-06/focus.md`, session data 2026-11-05); Monday's own sweep fires at 18:30 ET, after this artifact. So this ranks a Friday-list against Monday tape, and 9 of the 12 names have never been RVOL-ranked before - only MRNA (ranked 2026-11-03 and 11-04) and the two carry-over names, VRDN and XNCR, have a published reading behind them.
- **The burst came after the open.** WRBY's first 5-minute bar (142,539 shares) is only 0.93x its own prior-10 mean for the same bar - normal - while its 09:35 bar printed 294,588 shares, **8.2x** its prior-10 mean for that bar. The 09:45 price was 28.76 vs a +12.9% move on the prior close, and the bridge tape corroborates the volume (987,219 shares cumulative at 09:56 ET vs Yahoo's 939,920 through the 09:55 bar, 0.95x).
- **The trend is a level comparison, not a same-length one.** rvol_now is a 15-minute window and rvol_prev a 5-minute slot, each normalised against its own history - the same construction the 2026-11-06 artifact used, so the two are comparable, but the deltas are larger than a like-for-like comparison would give.

## Universe

12 names from `daily-screens/2026-11-06/focus.md` - the most recent completed 18:30 ET sweep (Fri 2026-11-06, 12 names). `focus_dir_date` = 2026-11-06; the sweep's own screen data date = **2026-11-05** (shibui T+1), read from the focus.md header, not inferred from the folder name. `lag_sessions` = **1** trading session - the normal Monday case, because cron #09 runs at 18:30 ET and had not yet fired when this artifact was written (the `daily-screens/2026-11-09/` directory holds only cron #08's pre-market output). All 12 names were priced (no `no_intraday_bars`).

## Table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WRBY | 28.76 | 0.1251 | 2.39 | 0.90 | 0.0331 | ACCELERATING (+1.48) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XERS | 15.38 | 0.1043 | 1.42 | 1.63 | 0.0713 | DECELERATING (-0.22) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ACHC | 38.49 | 0.0501 | 1.35 | 1.46 | 0.0290 | DECELERATING (-0.11) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| APP | 404.57 | 0.1061 | 0.89 | 0.72 | 0.0519 | ACCELERATING (+0.17) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| JOBY | 5.88 | 0.0996 | 0.83 | 0.85 | 0.0654 | STABLE (-0.02) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| U | 53.90 | 0.1001 | 0.73 | 0.66 | 0.0676 | ACCELERATING (+0.07) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MRNA | 260.48 | 0.0988 | 0.65 | 0.63 | 0.0583 | STABLE (+0.02) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VRDN | 29.02 | 0.0470 | 0.61 | 0.49 | 0.0172 | ACCELERATING (+0.12) | 0.1336 | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RUN | 9.98 | 0.0798 | 0.60 | 0.36 | 0.0332 | ACCELERATING (+0.24) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FUN | 10.28 | 0.0349 | 0.52 | 0.43 | 0.0173 | ACCELERATING (+0.09) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SEZL | 153.00 | 0.0401 | 0.41 | 0.27 | 0.0159 | ACCELERATING (+0.14) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XNCR | 36.04 | 0.0490 | 0.31 | 0.28 | 0.0355 | STABLE (+0.03) | 0.1335 | Liquid | - | 0 | not_subtracted | 2026-11-09 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts

- Universe size: **12**
- RVOL Required (rvol_now >= 1.5): **1** (WRBY)
- Liquid: **11**
- NEAR MISS (1.275-1.5): **2** (XERS, ACHC)
- Alerts: **0**
- Crossings proven: **0**
- UNADJUSTED rows (pre-market not subtracted): **0**

## Alerts

**none** - and the reason matters. `daily-screens/2026-11-06/focus-rvol-snapshot.csv` published an `rvol_now` for 12 names (CRCT, OUST, XYZ, ENOV, DUOL, YOU, HELE, KD, LIVN, ARRY, VRDN, XNCR) and **only VRDN and XNCR are in today's universe** - a 10-name turnover for the second session running. VRDN (0.1336) and XNCR (0.1335) are both far below the bar, so neither can be a crossing. **WRBY at 2.39x has no prior-session reading at all**, so it is a LEVEL, not a crossing, and carries tier WATCH.

## Near misses

- **XERS** - rvol_now **1.42x** (prior-session reading n/a; earlier-slot reading 1.63x, trend DECELERATING -0.22). To turn into an alert it needs rvol_now >= 1.5 while prev_session_rvol stays below 1.5 - and today it has no prior-session reading, so the first session that can prove the crossing is the next one, when today's CSV becomes its baseline.
- **ACHC** - rvol_now **1.35x** (prior-session reading n/a; earlier-slot reading 1.46x, trend DECELERATING -0.11). To turn into an alert it needs rvol_now >= 1.5 while prev_session_rvol stays below 1.5 - and today it has no prior-session reading, so the first session that can prove the crossing is the next one, when today's CSV becomes its baseline.

## Universe change

Versus the previous sweep (`daily-screens/2026-11-05/focus.md`, 12 names):

- Entered (10): RUN, SEZL, XERS, ACHC, MRNA, APP, U, FUN, JOBY, WRBY
- Left (10): ARRY, CRCT, DUOL, ENOV, HELE, KD, LIVN, OUST, XYZ, YOU
- Overlap: **2** (VRDN, XNCR) - and those two are exactly the names that carry a prior-session RVOL reading, which is why the alert tier is empty while the RVOL Required bucket is not.

## Method

- Metric: `rvol_tod_normalised` (time-of-day-normalised). Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 sessions, then scaled to full-day units by the prior-10 mean consolidated daily volume / TV `average_volume_10d_calc` (the only TV field used; TV's live columns lag the session and are never used for a live field).
- Today's volume and the 09:45 ET price: Yahoo chart API, `interval=5m&range=1mo&includePrePost=false` - one call per symbol, 12/12 ok. Bars are stamped at interval start, so the last COMPLETED bar at the 09:45 fire is the one stamped 09:40 and the volume window is 09:30 + 09:35 + 09:40. Bars stamped after 09:40 (09:45, 09:50, 09:55) and the zero-volume in-progress bar were dropped.
- Prior sessions: the same Yahoo 5-minute series, `range=1mo` (22 sessions fetched), plus Nasdaq `/historical` for the consolidated daily volume that carries the scale factor. A prior session enters the baseline **only if its 09:30/09:35/09:40 bars are all present AND non-zero** and a consolidated daily print exists - Yahoo's series has zero-volume or missing opening bars on a few sessions (ACHC 2026-10-26 and 2026-10-30, SEZL 2026-10-12/10-28, WRBY 2026-10-13/10-28, XNCR 2026-10-29 and others), and an incomplete opening bar would deflate the baseline and inflate the name's rvol. Clean sessions only, 10 per name, 2026-10-26 to 2026-11-06 for 9 of 12 names (ACHC and SEZL reach back to 2026-10-22, WRBY to 2026-10-23) - the exact window is published per row as `baseline_first`/`baseline_last`.
- Scale factor: prior-10 mean consolidated daily volume (Nasdaq `/historical`) / TV `average_volume_10d_calc`. It lands at 1.00-1.15 for 11 of 12 names (XNCR 1.62 - its trailing-10 window contains an 8.9M-share session on 2026-10-26, which lifts the mean; on a 9-session mean it would be 1.11 and XNCR's rvol_now 0.21x instead of 0.31x - still Liquid either way). The factor runs ~5% above 1.0 because TV's `average_volume_10d_calc` is a trailing-10 average that includes TODAY'S partial volume and drops the oldest completed session (verified: TV's value matches the mean of the last 9 completed sessions plus today's partial to within +0.4% to +1.4%, and misses the 10 completed-session mean by +2% to +7%), so rvol_now is correspondingly ~5% higher than a completed-session basis. The same convention was used on 2026-11-06, so the two artifacts are comparable.
- Independent checks: the Cboe delayed-quote CDN (consolidated, regular-session only) gives an independent earlier snapshot at its own timestamps 09:34:20-09:36:40 ET with volume 0.57-1.07x the corresponding Yahoo 09:30 bar (mean 0.75) and a price inside Yahoo's 09:30-bar close on all 12 names (exact on RUN, SEZL, WRBY, XNCR; worst 0.66% on VRDN). Nasdaq `/chart` gives an independent consolidated 09:45 ET print, within 0.55% of the Yahoo bar close on 9 of 12 names - and on **U, FUN and JOBY the Nasdaq 9:45 print sits OUTSIDE the range of its own neighbouring minute prints**, so it is an outlier tick and the Yahoo bar close is the number published. The bridge `market-recap` quote corroborates today's cumulative volume (Yahoo/bridge = 0.94-1.00 at 09:56 ET) and market_state=open.
- Cross-check snapshot: the earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 5-minute window (`cross_check_source: same_series_truncated`) - the same construction the 2026-11-06 artifact used, which keeps the trend column comparable across the two published artifacts. Cboe IS reachable and IS earlier than the fire (its snapshot falls inside the 09:30 bar for 11 of 12 names), but it is a mid-bar, cross-feed count whose basis differs from the Yahoo series by 0.57-1.07x (mean 0.75) - the opening auction print is counted differently - so it is published as the independent corroboration of that slot (volume, timestamp, price, raw ratio) rather than used as the metric's numerator, which would import a per-name basis error of up to +-40% into rvol_prev.
- Pre-market: excluded by construction (Yahoo `includePrePost=false`; every session's first bar is stamped 09:30 ET and the last 15:55 ET, so no extended-hours bar exists in the series), so `pm_vol` = 0 and `pm_vol_source` = `not_subtracted`; no dependency on cron #08. Verified structurally: across the 12 symbols and 22 fetched sessions, 19,680 bars were examined and **not one** is stamped outside 09:30-15:55 ET, so a pre-market print cannot be inside any bar. Cross-checked against cron #08's pre-market volumes (741 to 434,125 shares, all well below the corresponding regular-session bar), which are consistent with those prints never entering the session bars.
- Trend: `ACCELERATING` / `STABLE` / `DECELERATING` with the numeric delta; |delta| <= 0.05 is STABLE. Each reading is normalised against its own prior-10 mean for its own window, so a negative delta means today's volume arrived MORE front-loaded than that name's own history.
- Tier vocabulary: `ALERT` = a proven crossing; `NEAR MISS` = 1.275-1.5x; `WATCH` = at or above 1.0x but not an alert, which includes names above the 1.5x bar with no prior-session baseline; `-` = below 1.0x; `UNADJUSTED` = pre-market not subtracted (0 rows today).

## Source health

| source | url / query | status |
|---|---|---|
| Yahoo chart API (contract's primary intraday path) | query1 /v8/finance/chart, interval=5m, range=1mo, includePrePost=false | ok 12/12 symbols, 1 call each, 22 sessions each |
| TradingView america scanner | POST scanner.tradingview.com/america/scan, `average_volume_10d_calc` | ok, 20,000 of 20,041 rows retrieved (the last 41 rows were outside the requested range), 12/12 matched |
| Nasdaq /historical | api.nasdaq.com/api/quote/{SYM}/historical, 2026-10-19..2026-11-06 | ok 12/12 symbols, 14 rows each - consolidated daily volume for the scale factor |
| Nasdaq /chart | api.nasdaq.com/api/quote/{SYM}/chart | ok 12/12 - independent 09:45 ET print (3 outlier ticks rejected) |
| Cboe delayed-quote CDN | cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json | ok 12/12, snapshots 09:34:20-09:36:40 ET, regular session only - independent earlier-volume and price check |
| bridge market-recap get_quotes | Pipeworx gateway | ok, 12/12 found, market_state=open, as_of stamped (live price/volume corroboration) |
| cron #08 pre-market-gapper.csv | daily-screens/2026-11-09/pre-market-gapper.csv | ok, 12/12 tickers with pm_volume - used only to prove pre-market exclusion |
| MCP availability probe | probe_mcp.py | catalog_ok total=135 finance_tools=0; the mcp__* finance tools are absent and the servers are reached over the MCP-over-HTTP bridge |

## Degradation / caveats

- **The universe is Friday's.** `daily-screens/2026-11-06/focus.md` is the newest focus list on the outputs branch; Monday's sweep (#09, 18:30 ET) had not fired. `focus_dir_date` 2026-11-06, screen data date 2026-11-05, `lag_sessions` 1 - the normal Monday case, not a degradation. The roster turnover is the real limitation: 10 of 12 names have no prior-session RVOL reading, so no crossing can be proven and the alert tier is empty by construction rather than by calm tape.
- **The trend column compares different window lengths.** rvol_now is a 15-minute window, rvol_prev a 5-minute slot, each normalised against its own history. The delta is directional, not a like-for-like magnitude - this is the same construction as the 2026-11-06 artifact, so the two published trend columns are comparable with each other but neither is a clean acceleration rate.
- **The daily factor runs ~5% high.** TV's `average_volume_10d_calc` is a trailing-10 average that includes today's partial volume and drops the oldest completed session, so the factor sits at 1.00-1.15 instead of ~1.0 and rvol_now is ~5% higher than a completed-session basis would give. Unchanged from 2026-11-06, so the series stays comparable; XNCR is the one name where it matters (1.62x because of the 2026-10-26 8.9M-share session inside its trailing-10 window).
- **Yahoo's 5-minute series undercounts the consolidated tape on full days** (its 78-bar sum runs 0.52-1.47x Nasdaq's consolidated daily volume, mean ~0.85, with the gap widest on high-volume days) - the closing auction consolidates after the last 5-minute bar. This does not affect the window ratio (today's window and the prior-10 window means come from the same feed) but it is why the scale factor uses Nasdaq's settled consolidated daily volume rather than the Yahoo bar sum. The same gap means the prior-session baseline is measured on a slightly thinner tape than Nasdaq's daily print - which is exactly what the daily factor's ~5% offset corrects.
- **Three prior sessions carry broken opening bars** (ACHC 2026-10-26 and 2026-10-30, SEZL 2026-10-28, WRBY 2026-10-28 and others). They are excluded from the baseline rather than used with a zero, because a zero opening bar deflates the baseline mean and would inflate that name's rvol_now by a multiple of the share of the window it represents. For ACHC the effect is material and is published: the clean-window baseline gives 1.35x where a naive one gives 1.44x - both inside the NEAR MISS band, so the tier is unchanged, but the number moves.
- **In-progress and later bars dropped.** No bar stamped after 09:40 ET contributes any volume, and the zero-volume trailing bars were excluded. The fire snapshot is reconstructed at the 09:45 ET stamp from bars that had already closed.
- **rvol_intraday_live** is published for reference only and is mechanically tiny at 09:45 (15 of 390 session minutes). Never bucket on it.
- The 2026-11-06 artifact's rvol_now was rebuilt from the same feed for 12 of its names and reproduced within a mean 34% absolute difference, with the largest gaps on the low-RVOL names (ARRY +93%, XYZ +76%, KD +49%, HELE +39%) and on XNCR (-47%). The published 11-06 numbers came from a different, partly-reconstructed feed (StockTwits 5-minute bars with zero-volume 09:40/09:45 bars, bridged to a polygon baseline), so today's figures are on a cleaner basis but are NOT a drop-in replacement of that artifact's column; both are usable for the crossing test only because the 1.5x bar is far from any disagreement.
