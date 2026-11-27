---
date: 2026-11-20
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-20
focus_dir_date: 2026-11-19
screen_data_date: 2026-11-18
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1945
wider_universe_source: focus+master+17
wider_universe_size: 1933
wider_shown: 25
elapsed_minutes: 9935
elapsed_minutes_note: the minutes between the 2026-11-20 09:45 ET fire and this rebuild - the engine's own hardcoded 15 is its nominal fire duration and does not describe a reconstruction
session_fraction: 0.0385
source: Yahoo chart API 5m bars (interval=5m&range=1mo, regular session only) for the session volume, the 09:45 close and the prior-10 same-window baseline; Yahoo chart API 1d bars (range=3mo) for the prior-10 full-day volume; **the denominator was RECONSTRUCTED as of the fire** (see `denominator_source`) instead of pulled live, because this is a reconstruction of the 2026-11-20 fire produced on 2026-11-27; Yahoo chart API 5m bars with includePrePost=true for the published rows only, to measure the pre-market share
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean full-day volume divided by the average_volume_10d_calc denominator (reconstructed as of the fire - see denominator_source). The earlier reading is the same metric over the 09:30-09:35 slot, against the prior-10 mean of that same slot, on the same denominator.
metric_def: rvol_tod_normalised = (cumulative volume 09:30 -> the fire's bar, today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 sessions) x (mean full-day volume across those prior 10 sessions / average_volume_10d_calc, reconstructed as of the fire); rvol_intraday_live = cumulative session volume to the fire bar / average_volume_10d_calc (reference only, never bucketed); rvol_prev = the same formula over the earlier cross-check snapshot's window against the prior-10 mean of that same window; rvol_at_09_38 = the raw cumulative ratio at that earlier snapshot; pm_share_pct = pre-market volume before 09:30 as a percentage of the session volume
bucket_rule: rvol_now >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's reading of the same metric.
pm_source_status: not_subtracted
cross_check_source: same_series_truncated
status: ok
status_artifact: late reconstruction
reconstruction: late reconstruction - a delayed replay of the 2026-11-20 09:45 ET fire, rebuilt on 2026-11-27 from the archival sources; the fire itself never executed
denominator_source: RECONSTRUCTED as of the fire, not pulled live. TradingView's average_volume_10d_calc at a 09:45 ET pull is the mean of the last ten sessions with the current session counted at its partial (09:30-09:45) volume, so it is reconstructed here as (the 9 most recent completed sessions' daily volume + the fire day's 09:30-09:45 volume) / 10 from Yahoo's own daily and 5-minute bars. Calibrated on 2026-11-27 against the denominators recorded in four published artifacts (11-19, 11-23, 11-24, 11-25): median error 0.494%, p90 1.479%, max 8.458%
reconstructed_at: 2026-11-27
reconstruction_basis: daily-screens/2026-11-19/focus.md (the upstream roster, unchanged on disk) + Yahoo 5m/1d bars addressed to the fire date
upstream: /workspace/daily-screens/2026-11-19/focus.md
names_unpriced: 344
published_rows: 223
selectivity: broad_tape
universe_median_rvol: 1.4899
universe_p90_rvol: 3.0521
universe_share_ge_1_5_pct: 49.22
universe_crossings: 579
---

# Focus RVOL snapshot - 2026-11-20 09:45 ET (cron #07)

## TL;DR
- **1601 of 1945** names scored (12 focus + 1933 wider union); **223 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 29 of 223 published** (194 Liquid); **191 near misses**; **13 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **49.22% of the 1601 scored names cleared the 1.5x bar** (median 1.4899x, p90 3.0521x) and there were **579 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: SFNC (ACCELERATING), GLOB (ACCELERATING), WTS (ACCELERATING), SNDK (ACCELERATING), PYXS (ACCELERATING), MRX (DECELERATING), GAP (DECELERATING), ERAS (DECELERATING), WRD (DECELERATING), ESTC (DECELERATING), FSCO (DECELERATING), UDR (DECELERATING), CCC (DECELERATING).** **5 are still building and 8 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **41 building vs 132 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME reconstructed denominator as today's reading**, so both sides of each crossing are one scale. The denominator is a rolling average and moves between pulls, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.
- This artifact is a **late reconstruction** - a delayed replay of the 2026-11-20 09:45 ET fire, produced on 2026-11-27. That fire never executed (the platform created the session but the routine's first step never ran, so no model call, no artifact and no commit), so the snapshot window (09:30-09:45 ET) was rebuilt from Yahoo's 5-minute and daily bars, and the denominator was reconstructed as of the fire rather than pulled live. Calibrated against four published artifacts, the reconstruction reproduces a live fire's numbers to a 0.8% median (rvol_now). Two limits stand: Yahoo has revised some thin names' intraday bars since the fire (SMTC on 2026-11-25 changed 60%), and a name that was a crossing can sit outside the published top-25 table when more names price than they did at the fire.

## Universe
- focus roster: 12 names
- wider union: 1933 names from focus+master+17
- scored: 1601; unscored: 344; published rows: 223
- **the scored universe's distribution** (the context for every count below): median 1.4899x, p75 2.1545x, p90 3.0521x, p99 7.4307x; 61.15% at or above 1.275x, **49.22% at or above 1.5x**, 28.98% at or above 2x, 10.49% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GNRC | 201.33 | 0.0816 | 1.7630 | 2.0974 | 0.0480 | DECELERATING | 1.7007 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OKTA | 196.26 | 0.104 | 1.5956 | 1.7784 | 0.0613 | DECELERATING | 4.2992 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TENB | 43.06 | 0.0783 | 1.5608 | 1.6888 | 0.0530 | DECELERATING | 2.8471 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PANW | 347.99 | 0.156 | 1.5130 | 1.4397 | 0.0950 | ACCELERATING | 4.8693 | recomputed_same_feed | 5.5985 | 15.37 | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NTSK | 23.35 | 0.0813 | 1.4999 | 1.2559 | 0.0347 | ACCELERATING | 4.8030 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FSLY | 15.90 | 0.102 | 1.4994 | 1.2744 | 0.0602 | ACCELERATING | 1.2904 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| QLYS | 188.18 | 0.0701 | 1.3696 | 1.8582 | 0.0565 | DECELERATING | 1.9139 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NUAI | 3.80 | 0.154 | 1.3019 | 1.7911 | 0.1185 | DECELERATING | 1.6584 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ATEN | 31.67 | 0.064 | 1.2998 | 1.5138 | 0.0442 | DECELERATING | 3.0655 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SAIL | 21.05 | 0.0675 | 1.1750 | 1.2915 | 0.0471 | DECELERATING | 3.5201 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BRBR | 15.28 | 0.0522 | 1.0380 | 1.2869 | 0.0326 | DECELERATING | 2.7245 | recomputed_same_feed | 3.2291 | 18.51 | Liquid | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| S | 23.03 | 0.046 | 0.8988 | 0.7164 | 0.0210 | ACCELERATING | 2.1065 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CCC | 7.68 | 1.25 | 15.5273 | 61.8344 | 0.8915 | DECELERATING | 0.1654 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SVRA | 4.29 | 0.818 | 14.1658 | 18.7278 | 0.6411 | DECELERATING | 2.0259 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GTES | 23.72 | 0.168 | 13.0397 | 1.4347 | 0.0089 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ROST | 213.17 | 0.539 | 12.4197 | 17.4083 | 0.4033 | DECELERATING | 1.6807 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GAP | 21.66 | 0.417 | 11.5668 | 12.4807 | 0.2104 | DECELERATING | 1.4165 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GLOB | 40.15 | 0.346 | 11.1626 | 8.1493 | 0.1528 | ACCELERATING | 0.6491 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AGYS | 113.41 | 0.636 | 10.7921 | 3.3719 | 0.1256 | ACCELERATING | 1.5652 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GVA | 115.35 | 0.334 | 10.7714 | 6.6417 | 0.0838 | ACCELERATING | 1.9696 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WRD | 3.12 | 0.58 | 10.3423 | 12.3991 | 0.3663 | DECELERATING | 1.3738 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SLG | 45.97 | 0.176 | 9.9723 | 11.1690 | 0.1226 | DECELERATING | 1.6247 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SFNC | 22.17 | 0.286 | 9.4876 | 5.5003 | 0.0799 | ACCELERATING | 0.7807 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BVN | 19.43 | 0.269 | 9.3802 | 15.9102 | 0.2210 | DECELERATING | 1.5146 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| UDR | 35.94 | 0.189 | 8.6316 | 23.3953 | 0.1783 | DECELERATING | 0.5971 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FSCO | 4.90 | 0.639 | 8.4967 | 17.6355 | 0.5228 | DECELERATING | 0.5465 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MRX | 58.38 | 0.206 | 8.3655 | 8.7279 | 0.1171 | DECELERATING | 1.2725 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ESTC | 76.31 | 0.308 | 7.4355 | 10.9893 | 0.2235 | DECELERATING | 1.0958 | recomputed_same_feed | 1.4470 | 32.05 | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PYXS | 1.82 | 0.237 | 7.4307 | 7.3692 | 0.1394 | ACCELERATING | 1.3879 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WTS | 356.77 | 0.27 | 7.4077 | 4.8554 | 0.0713 | ACCELERATING | 0.7489 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ERAS | 13.95 | 0.295 | 7.0482 | 8.6263 | 0.1685 | DECELERATING | 0.4826 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CX | 9.39 | 0.174 | 6.8587 | 2.5608 | 0.0301 | ACCELERATING | 1.5510 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BSP | 42.99 | 0.447 | 6.7549 | 9.0564 | 0.2878 | DECELERATING | 1.6658 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RUSHA | 44.89 | 0.124 | 6.6274 | 10.6996 | 0.1129 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SCI | 71.31 | 0.113 | 6.5864 | 3.0000 | 0.0307 | ACCELERATING | n/a | unavailable | 10.2052 | 25.28 | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNDK | 86.06 | 0.149 | 6.5404 | 6.4443 | 0.0972 | ACCELERATING | 1.1279 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EVH | 3.98 | 0.261 | 6.4776 | 4.4271 | 0.1108 | ACCELERATING | 2.5645 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-20 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 1945
- focus roster size: 12
- wider universe size: 1933
- scored: 1601; unpriced: 344; published rows: 223
- Required count: 29 (of 223 published)
- Liquid count: 194
- NEAR MISS count: 191 (41 building, 132 fading)
- alert count: 13 (5 building, 8 fading)
- crossings: 13 published; **579 across all 1601 scored names**
- universe distribution: median 1.4899x, p90 3.0521x; 49.22% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **SFNC** - 9.4876x now vs 0.7807x on the prior session (recomputed_same_feed), close 22.17 - RVOL building 5.5003x -> 9.4876x, accumulation
- **GLOB** - 11.1626x now vs 0.6491x on the prior session (recomputed_same_feed), close 40.15 - RVOL building 8.1493x -> 11.1626x, accumulation
- **WTS** - 7.4077x now vs 0.7489x on the prior session (recomputed_same_feed), close 356.77 - RVOL building 4.8554x -> 7.4077x, accumulation
- **SNDK** - 6.5404x now vs 1.1279x on the prior session (recomputed_same_feed), close 86.06 - RVOL building 6.4443x -> 6.5404x, accumulation
- **PYXS** - 7.4307x now vs 1.3879x on the prior session (recomputed_same_feed), close 1.82 - RVOL building 7.3692x -> 7.4307x, accumulation
- **MRX** - 8.3655x now vs 1.2725x on the prior session (recomputed_same_feed), close 58.38 - RVOL fading 8.7279x -> 8.3655x, distribution
- **GAP** - 11.5668x now vs 1.4165x on the prior session (recomputed_same_feed), close 21.66 - RVOL fading 12.4807x -> 11.5668x, distribution
- **ERAS** - 7.0482x now vs 0.4826x on the prior session (recomputed_same_feed), close 13.95 - RVOL fading 8.6263x -> 7.0482x, distribution
- **WRD** - 10.3423x now vs 1.3738x on the prior session (recomputed_same_feed), close 3.12 - RVOL fading 12.3991x -> 10.3423x, distribution
- **ESTC** - 7.4355x now vs 1.0958x on the prior session (recomputed_same_feed), close 76.31 - RVOL fading 10.9893x -> 7.4355x, distribution
- **FSCO** - 8.4967x now vs 0.5465x on the prior session (recomputed_same_feed), close 4.90 - RVOL fading 17.6355x -> 8.4967x, distribution
- **UDR** - 8.6316x now vs 0.5971x on the prior session (recomputed_same_feed), close 35.94 - RVOL fading 23.3953x -> 8.6316x, distribution
- **CCC** - 15.5273x now vs 0.1654x on the prior session (recomputed_same_feed), close 7.68 - RVOL fading 61.8344x -> 15.5273x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 41 building against 132 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| VSH | 1.4736 | 2.3718 | 0.1241 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NLY | 1.4172 | 0.9689 | 0.7008 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BEPC | 1.4271 | 1.4980 | 0.7133 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| USFD | 1.3192 | 0.8036 | 0.6187 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDWR | 1.4136 | 3.2282 | 0.7350 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STAG | 1.4724 | 0.7875 | 0.8737 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CHAT | 1.3298 | 1.2844 | 0.7665 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AEG | 1.3596 | 1.8737 | 0.7990 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DKS | 1.3077 | 1.6756 | 0.7621 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VMET | 1.3236 | 0.5252 | 0.8170 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BMRN | 1.3484 | 2.2598 | 0.8546 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SMWB | 1.3069 | 2.1136 | 0.8170 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETSY | 1.3239 | 1.0624 | 0.8637 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HRL | 1.3644 | 0.6445 | 0.9265 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SKM | 1.4564 | 1.9414 | 1.0450 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TTMI | 1.4585 | 1.2184 | 1.0771 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NLST | 1.4136 | 0.8921 | 1.0370 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VFS | 1.4513 | 0.8930 | 1.0829 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMC | 1.4929 | 1.6503 | 1.1341 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAX | 1.3793 | 0.4335 | 1.0730 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| USAS | 1.4737 | 0.6881 | 1.1726 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NBIX | 1.3220 | 1.8667 | 1.0212 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LAZ | 1.3715 | 2.2356 | 1.0829 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GLAD | 1.3331 | 2.5954 | 1.0663 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EWY | 1.4985 | 0.9019 | 1.2517 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NTSK | 1.4999 | 4.8030 | 1.2559 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FSLY | 1.4994 | 1.2904 | 1.2744 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTRG | 1.3529 | 0.6280 | 1.1309 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CROX | 1.3924 | 0.6155 | 1.1772 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BB | 1.3976 | 1.0598 | 1.1846 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| POET | 1.4578 | 0.9151 | 1.2503 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DELL | 1.4058 | 0.9410 | 1.2310 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RIVN | 1.4846 | 0.5676 | 1.3372 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XEL | 1.4430 | 1.3626 | 1.2965 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MP | 1.3147 | 0.8640 | 1.1798 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASX | 1.4846 | 1.7714 | 1.3746 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RBRK | 1.4996 | 4.8486 | 1.4047 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FIS | 1.4143 | 0.7274 | 1.3245 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CIBR | 1.4239 | 3.6588 | 1.3483 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SNOW | 1.2843 | 2.6403 | 1.2169 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SOXX | 1.2967 | 0.8478 | 1.2393 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TER | 1.4936 | 0.7407 | 1.4439 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NOW | 1.4319 | 1.1838 | 1.3884 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PENG | 1.3358 | 1.2022 | 1.2923 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| YPF | 1.4095 | 0.5635 | 1.3782 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NNE | 1.4537 | 0.9819 | 1.4235 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HL | 1.3097 | 0.6911 | 1.2816 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PICS | 1.4302 | 0.3889 | 1.4074 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IREN | 1.4502 | 1.2423 | 1.4295 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STZ | 1.4926 | 0.8698 | 1.4797 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LKNCY | 1.3277 | 0.7773 | 1.3215 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETHE | 1.3047 | 0.5192 | 1.2988 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WRB | 1.4848 | 0.4082 | 1.4922 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PFE | 1.2987 | 0.7153 | 1.3079 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVAX | 1.4846 | 0.7894 | 1.4963 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CALM | 1.3381 | 1.0750 | 1.3526 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRCL | 1.4418 | 1.2401 | 1.4654 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CBSH | 1.4413 | 1.1032 | 1.4701 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSSI | 1.4074 | 0.5602 | 1.4469 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LAMR | 1.2985 | 0.7337 | 1.3724 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PATH | 1.4283 | 1.1019 | 1.5124 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MRVL | 1.3785 | 0.8186 | 1.4644 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBAI | 1.4212 | 1.4872 | 1.5159 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INTC | 1.2965 | 1.1192 | 1.3914 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DNN | 1.3982 | 1.2058 | 1.4939 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSEM | 1.4399 | 1.0412 | 1.5398 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMD | 1.3925 | 0.6994 | 1.4979 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ANET | 1.4204 | 0.8674 | 1.5421 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STRL | 1.3243 | 0.9123 | 1.4496 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KEEL | 1.4885 | 0.9555 | 1.6192 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| YSS | 1.4429 | 1.4156 | 1.5857 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STX | 1.3013 | 1.3276 | 1.4487 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ANTW | 1.2912 | 5.4781 | 1.4449 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RMD | 1.3524 | 1.8423 | 1.5081 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IONQ | 1.3401 | 1.4547 | 1.4963 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LOGI | 1.3233 | 1.1776 | 1.4810 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASAN | 1.2764 | 0.6349 | 1.4370 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HIVE | 1.3831 | 0.7312 | 1.5454 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PLAB | 1.4498 | 0.6075 | 1.6193 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VKTX | 1.2952 | 1.1708 | 1.4648 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORCL | 1.3665 | 1.3532 | 1.5423 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZM | 1.4660 | 5.1228 | 1.6421 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VICR | 1.3448 | 0.7425 | 1.5249 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GEMI | 1.3507 | 1.6301 | 1.5529 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FICO | 1.3388 | 0.2965 | 1.5412 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MCD | 1.2988 | 0.8175 | 1.5017 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ATEN | 1.2998 | 3.0655 | 1.5138 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARHS | 1.4301 | 0.2913 | 1.6443 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BFLY | 1.3733 | 0.9493 | 1.5886 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGL | 1.3910 | 1.7163 | 1.6076 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VTRS | 1.4426 | 0.6679 | 1.6595 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HIMX | 1.4702 | 1.3422 | 1.6899 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLB | 1.4475 | 0.6001 | 1.6733 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NCNO | 1.4327 | 0.5550 | 1.6598 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XYZ | 1.4495 | 0.5487 | 1.6888 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SANA | 1.3185 | 0.9134 | 1.5589 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UAMY | 1.3074 | 0.6117 | 1.5567 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVAV | 1.4954 | 1.2293 | 1.7513 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RUN | 1.2826 | 0.4345 | 1.5401 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAT | 1.3274 | 0.9062 | 1.5950 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CVLT | 1.3385 | 0.5601 | 1.6100 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BETR | 1.3094 | 0.3709 | 1.5869 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IHG | 1.4036 | 0.6339 | 1.6838 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OKLO | 1.4969 | 0.7259 | 1.7779 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRM | 1.3720 | 1.5241 | 1.6780 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPCX | 1.4989 | 0.9619 | 1.8121 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SMG | 1.4626 | 0.8865 | 1.7826 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PEP | 1.4764 | 1.6096 | 1.7991 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CVS | 1.2778 | 0.5967 | 1.6095 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORC | 1.4523 | 1.7162 | 1.7914 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BOOT | 1.3013 | 1.1401 | 1.6426 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RIG | 1.4954 | 0.5557 | 1.8454 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OR | 1.4263 | 0.6287 | 1.7894 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FLUT | 1.3368 | 1.0686 | 1.7016 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CVX | 1.3441 | 3.9792 | 1.7091 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FCEL | 1.4865 | 1.0058 | 1.8721 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARM | 1.4691 | 0.5836 | 1.8802 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLMN | 1.3609 | 0.9932 | 1.7768 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BJRI | 1.4172 | 0.4321 | 1.8346 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMG | 1.4236 | 0.6060 | 1.8512 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RXST | 1.4511 | 0.2287 | 1.8798 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CSCO | 1.3839 | 0.7965 | 1.8138 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMB | 1.3774 | 1.1302 | 1.8125 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QXO | 1.2819 | 1.1308 | 1.7230 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STWD | 1.3871 | 0.8581 | 1.8285 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RNR | 1.4020 | 1.0386 | 1.8441 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EDU | 1.3111 | 0.4400 | 1.7625 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FRSH | 1.4797 | 0.6516 | 1.9343 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KRC | 1.3993 | 2.0944 | 1.8685 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DC | 1.3941 | 1.5869 | 1.8644 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADSK | 1.4899 | 0.6617 | 1.9669 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALLE | 1.3123 | 0.8173 | 1.7977 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QLYS | 1.3696 | 1.9139 | 1.8582 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NUAI | 1.3019 | 1.6584 | 1.7911 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EWTX | 1.2772 | 0.2315 | 1.7693 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UTI | 1.4043 | 9.6322 | 1.9073 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ROL | 1.4593 | 0.6269 | 1.9643 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FTS | 1.3906 | 1.1614 | 1.8986 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FFIV | 1.4211 | 1.0929 | 1.9320 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AXON | 1.3067 | 0.7623 | 1.8306 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SBH | 1.4410 | 0.4635 | 1.9672 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RLI | 1.4844 | n/a | 2.0132 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UA | 1.3791 | 0.7299 | 1.9085 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AI | 1.3220 | 1.9650 | 1.8568 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| REAL | 1.4892 | 0.8267 | 2.0269 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLPT | 1.4608 | 1.7720 | 2.0113 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EMA | 1.4707 | 0.6735 | 2.0228 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CL | 1.3895 | 1.2518 | 1.9482 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GO | 1.4817 | 0.4799 | 2.0470 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PWR | 1.3816 | 0.4383 | 1.9542 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TLRY | 1.4841 | 1.0608 | 2.0571 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAR | 1.3661 | 1.3204 | 1.9488 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORKA | 1.3586 | 1.3545 | 1.9477 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| POWW | 1.4085 | 1.9805 | 2.0055 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZYME | 1.4990 | 0.5344 | 2.0968 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRSP | 1.3701 | 1.2103 | 1.9739 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CD | 1.3485 | 1.5995 | 1.9571 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAI | 1.4041 | 1.0825 | 2.0522 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BTU | 1.3543 | 0.2594 | 2.0073 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KOD | 1.3223 | 1.0539 | 1.9783 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FOSL | 1.2820 | 0.1816 | 1.9398 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GAU | 1.3911 | 0.1781 | 2.0599 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OMDA | 1.3216 | 0.7377 | 1.9921 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ULTA | 1.4306 | n/a | 2.1055 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OWL | 1.3410 | 0.7206 | 2.0427 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HLT | 1.4399 | 2.4115 | 2.1544 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RYN | 1.3624 | 0.4890 | 2.0973 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBW | 1.3303 | 0.4614 | 2.0795 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PBF | 1.4681 | 0.8797 | 2.2650 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NRIX | 1.2940 | 0.5726 | 2.1010 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FMCC | 1.2992 | n/a | 2.1098 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UIS | 1.3860 | 0.2524 | 2.2186 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QDEL | 1.4752 | 0.7098 | 2.3136 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIGA | 1.4762 | 0.3593 | 2.3776 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IRS | 1.4651 | 0.5545 | 2.3922 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVBH | 1.4758 | 2.0620 | 2.4463 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ELVA | 1.3740 | 2.2584 | 2.3611 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SRRK | 1.2892 | 0.6206 | 2.3165 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CDRE | 1.4240 | n/a | 2.4631 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BKV | 1.3034 | 0.5075 | 2.3448 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LTH | 1.4436 | 0.5528 | 2.5811 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| R | 1.4788 | 3.0080 | 2.7011 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EW | 1.4517 | 0.7525 | 2.6865 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PHAT | 1.4559 | 1.1837 | 2.7234 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FET | 1.4153 | 1.1570 | 2.7056 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RARE | 1.3934 | 0.6869 | 2.6870 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RPAY | 1.4546 | 0.1979 | 3.1403 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LOCO | 1.3017 | 0.3828 | 3.3185 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRVI | 1.3637 | 0.3381 | 3.5083 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MNRO | 1.4385 | 0.2276 | 3.7466 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INTA | 1.2989 | 0.6672 | 3.7551 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **10 entered**, **136 left**, **2 stayed**.

- entered: ATEN, FSLY, GNRC, NTSK, NUAI, OKTA, QLYS, S, SAIL, TENB
- left: ABR, ADC, ADUR, AFL, AGX, ALAB, ALM, ALMS, AMBA, AMC, AMGN, AMZN, ARCO, ARM, ASH, ASTL, ATEYY, AUR, AYI, BBAI, BBWI, BHP, BIO, BL, CAG, CBAN, CCJ, CGBD, CMP, CNQ, COCO, CP, CPNG, CRI, CRML, CRSP, CTAS, CTKB, DEO, DMC, DOC, DRD, DRH, ECL, ENR, ESTC, ETSY, EWW, FMS, FTNT, GEHC, GGN, GH, GL, GNR, GOOGL, HACK, HDB, HLIT, HPE, HPQ, HR, HSY, HYMC, ICLR, IHAK, IONQ, JMIA, KLAC, KOS, KR, LIN, LUMN, MA, MAR, MDGL, MKL, MLM, MPC, MTZ, MYRG, NCLD, NEXN, NRXP, OFG, OLLI, ORKA, PACB, PBF, PCG, PLTR, PONY, PRAX, PSLV, PURR, QCOM, RARE, RBLX, RCEL, RGEN, RH, RLX, RYTM, SA, SAFE, SCI, SCOP, SFM, SHAZ, SKYA, SLS, SLVP, SNAP, SPOT, SPWR, STLA, STTK, SVIX, TDOC, TEAM, TFPM, THC, TRIN, TRV, TSM, TWI, UMC, UNP, V, VIK, WHR, WSM, WWD, WWW, XEL, YALA
- stayed: BRBR, PANW

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 2 of 12 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 373.4s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: `average_volume_10d_calc` RECONSTRUCTED as of the fire (not pulled live - see `denominator_source`): the 9 most recent completed sessions' daily volume plus the fire day's 09:30-09:45 volume, over 10. ONE denominator set used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- Denominator: RECONSTRUCTED as of the fire, not pulled live (see `denominator_source`) - one denominator set used for BOTH sides of every crossing, so both sides stay on one scale
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1601 of 1945 candidates
- unpriced names: 344 of 1945 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 223 published rows - not_subtracted 223; 223 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **Late reconstruction (delayed replay).** This file was produced on 2026-11-27, not at the 2026-11-20 09:45 ET fire. The fire never executed, so the whole artifact is rebuilt from archival sources: the session window, the prior-10 same-window baseline, the prior-10 full-day volume and the close come from Yahoo's bars addressed to the fire date, and the denominator is reconstructed as of the fire (see `denominator_source`). The pre-market share is `not_subtracted`: the live pre-market counters cannot be replayed for a past session, exactly as on the 2026-11-05 reconstruction.
- **344 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone. The reconstructed denominator carries its own error (median 0.494% against four published artifacts, p90 1.479%, max 8.458% on thin names), which is inside that flip band for the thinnest names.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
