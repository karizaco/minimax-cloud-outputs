---
date: 2026-11-17
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-17
focus_dir_date: 2026-11-16
screen_data_date: 2026-11-13
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 2304
wider_universe_source: focus+master+17
wider_universe_size: 2292
wider_shown: 25
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars (interval=5m&range=1mo, regular session only) for the session volume, the 09:45 close and the prior-10 same-window baseline; Yahoo chart API 1d bars (range=3mo) for the prior-10 full-day volume; TradingView america scanner average_volume_10d_calc for the denominator (ONE pull, used for BOTH sides of every crossing); Yahoo chart API 5m bars with includePrePost=true for the published rows only, to measure the pre-market share
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean full-day volume divided by TV average_volume_10d_calc. The earlier reading is the same metric over the 09:30-09:35 slot, against the prior-10 mean of that same slot, on the same denominator.
metric_def: rvol_tod_normalised = (cumulative volume 09:30 -> the fire's bar, today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 sessions) x (mean full-day volume across those prior 10 sessions / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the fire bar / TV average_volume_10d_calc (reference only, never bucketed); rvol_prev = the same formula over the earlier cross-check snapshot's window against the prior-10 mean of that same window; rvol_at_09_38 = the raw cumulative ratio at that earlier snapshot; pm_share_pct = pre-market volume before 09:30 as a percentage of the session volume
bucket_rule: rvol_now >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's reading of the same metric.
pm_source_status: measured_from_series
cross_check_source: same_series_truncated
status: ok
upstream: /workspace/daily-screens/2026-11-16/focus.md
names_unpriced: 460
published_rows: 108
selectivity: broad_tape
universe_median_rvol: 0.6094
universe_p90_rvol: 1.4264
universe_share_ge_1_5_pct: 9.11
universe_crossings: 111
---

# Focus RVOL snapshot - 2026-11-17 09:45 ET (cron #07)

## TL;DR
- **1844 of 2304** names scored (12 focus + 2292 wider union); **108 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 26 of 108 published** (82 Liquid); **72 near misses**; **14 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **9.11% of the 1844 scored names cleared the 1.5x bar** (median 0.6094x, p90 1.4264x) and there were **111 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: PSIX (ACCELERATING), GFF (ACCELERATING), PICS (ACCELERATING), FR (ACCELERATING), PONY (ACCELERATING), CPRI (ACCELERATING), BBIO (DECELERATING), RNA (DECELERATING), OMER (DECELERATING), DUOT (DECELERATING), ED (DECELERATING), RCAT (DECELERATING), KLAR (DECELERATING), GLAS (DECELERATING).** **6 are still building and 8 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **30 building vs 37 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 2292 names from focus+master+17
- scored: 1844; unscored: 460; published rows: 108
- **the scored universe's distribution** (the context for every count below): median 0.6094x, p75 0.9178x, p90 1.4264x, p99 4.7937x; 13.02% at or above 1.275x, **9.11% at or above 1.5x**, 4.5% at or above 2x, 2.49% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CPRI | 18.99 | 0.292 | 6.2435 | 5.2542 | 0.1240 | ACCELERATING | 0.6909 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 36541 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ALM | 8.53 | 0.0999 | 1.2139 | 0.9473 | 0.0463 | ACCELERATING | 1.1139 | recomputed_same_feed | 1.3273 | 19.16 | Liquid | WATCH | 64152 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CGON | 77.96 | 0.0877 | 0.9604 | 0.4730 | 0.0276 | ACCELERATING | 28.0628 | recomputed_same_feed | 43.5018 | 55.02 | Liquid | WATCH | 4512 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VKTX | 27.11 | 0.0393 | 0.7133 | 0.8426 | 0.0241 | DECELERATING | 1.4231 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 15777 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SENS | 11.14 | 0.0789 | 0.6094 | 0.6779 | 0.0458 | DECELERATING | 0.5099 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 8148 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FOUR | 41.30 | 0.025 | 0.5719 | 0.6367 | 0.0131 | DECELERATING | 0.5715 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1385 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TNDM | 18.16 | 0.0278 | 0.5103 | 0.6611 | 0.0174 | DECELERATING | 0.3835 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 9098 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CBRS | 102.52 | 0.0734 | 0.4973 | 0.4606 | 0.0423 | STABLE | 0.9648 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 256819 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ALNY | 158.79 | 0.0165 | 0.3024 | 0.3400 | 0.0100 | STABLE | 0.5398 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 3280 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MOD | 134.03 | 0.0239 | 0.1830 | 0.1906 | 0.0158 | STABLE | 0.4137 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 8875 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| U | 51.41 | 0.0223 | 0.1613 | 0.1327 | 0.0134 | STABLE | 0.2732 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 108018 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NSIT | 154.96 | 1.37 | 28.3830 | 44.2431 | 1.1727 | DECELERATING | 3.7761 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 685422 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ABX | 5.91 | 0.413 | 11.3125 | 3.7813 | 0.0886 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 7505 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AS | 31.60 | 0.469 | 11.2405 | 9.6779 | 0.2201 | ACCELERATING | 1.5232 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1001509 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OMER | 13.85 | 0.493 | 10.3090 | 11.1855 | 0.2838 | DECELERATING | 0.3460 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 40064 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GLAS | 1.66 | 1.01 | 10.2724 | 16.6104 | 0.6682 | DECELERATING | 0.6565 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1791471 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RCAT | 2.57 | 0.895 | 9.1947 | 12.4162 | 0.6980 | DECELERATING | 0.7471 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 3460519 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GLSI | 17.71 | 0.66 | 9.0973 | 12.2814 | 0.3846 | DECELERATING | 2.1291 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 21899 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DUOT | 3.97 | 0.439 | 8.6874 | 9.9688 | 0.2875 | DECELERATING | 0.6227 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 55747 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PICS | 5.34 | 0.414 | 7.6289 | 5.9221 | 0.1662 | ACCELERATING | 0.3842 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 34229 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KLAR | 14.34 | 0.455 | 7.2471 | 11.3748 | 0.3043 | DECELERATING | 0.7516 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1143821 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BBIO | 75.03 | 0.329 | 6.9713 | 7.0688 | 0.2025 | DECELERATING | 0.2939 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 525370 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ED | 120.34 | 0.211 | 6.9051 | 9.3595 | 0.1328 | DECELERATING | 0.4803 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 29731 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ADIG | 9.87 | 0.167 | 6.0249 | 6.0698 | 0.0811 | STABLE | 1.7243 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 22307 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HXL | 77.62 | 0.122 | 5.9770 | 0.4993 | 0.0054 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NRIM | 23.42 | 0.193 | 5.9131 | 3.4649 | 0.0457 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PKX | 48.26 | 0.352 | 5.2833 | 8.1846 | 0.3429 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 130 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FR | 55.03 | 0.0467 | 5.2485 | 3.7925 | 0.0187 | ACCELERATING | 0.6751 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 5951 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GFF | 108.39 | 0.136 | 4.7937 | 1.8500 | 0.0285 | ACCELERATING | 0.8076 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 400 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DCOM | 41.69 | 0.176 | 4.4651 | 0.4430 | 0.0109 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 680 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RNA | 6.84 | 0.153 | 4.4524 | 4.8406 | 0.1051 | DECELERATING | 0.2200 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 302 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PSIX | 34.38 | 0.309 | 4.3183 | 1.0231 | 0.0380 | ACCELERATING | 1.0702 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 101 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PRAX | 314.43 | 0.162 | 4.2821 | 4.5920 | 0.0593 | DECELERATING | 1.8145 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1617 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CANG | 1.53 | 0.729 | 4.1447 | 2.3540 | 0.2723 | ACCELERATING | 1.6761 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 95864 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PONY | 3.88 | 0.415 | 3.7959 | 2.7383 | 0.1757 | ACCELERATING | 0.5874 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 32398 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WWD | 315.73 | 0.0944 | 3.7591 | 4.8875 | 0.0595 | DECELERATING | 1.8920 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 191 | measured_from_nasdaq | 2026-11-17 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 2304
- focus roster size: 12
- wider universe size: 2292
- scored: 1844; unpriced: 460; published rows: 108
- Required count: 26 (of 108 published)
- Liquid count: 82
- NEAR MISS count: 72 (30 building, 37 fading)
- alert count: 14 (6 building, 8 fading)
- crossings: 14 published; **111 across all 1844 scored names**
- universe distribution: median 0.6094x, p90 1.4264x; 9.11% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **PSIX** - 4.3183x now vs 1.0702x on the prior session (recomputed_same_feed), close 34.38 - RVOL building 1.0231x -> 4.3183x, accumulation
- **GFF** - 4.7937x now vs 0.8076x on the prior session (recomputed_same_feed), close 108.39 - RVOL building 1.8500x -> 4.7937x, accumulation
- **PICS** - 7.6289x now vs 0.3842x on the prior session (recomputed_same_feed), close 5.34 - RVOL building 5.9221x -> 7.6289x, accumulation
- **FR** - 5.2485x now vs 0.6751x on the prior session (recomputed_same_feed), close 55.03 - RVOL building 3.7925x -> 5.2485x, accumulation
- **PONY** - 3.7959x now vs 0.5874x on the prior session (recomputed_same_feed), close 3.88 - RVOL building 2.7383x -> 3.7959x, accumulation
- **CPRI** - 6.2435x now vs 0.6909x on the prior session (recomputed_same_feed), close 18.99 - RVOL building 5.2542x -> 6.2435x, accumulation
- **BBIO** - 6.9713x now vs 0.2939x on the prior session (recomputed_same_feed), close 75.03 - RVOL fading 7.0688x -> 6.9713x, distribution
- **RNA** - 4.4524x now vs 0.2200x on the prior session (recomputed_same_feed), close 6.84 - RVOL fading 4.8406x -> 4.4524x, distribution
- **OMER** - 10.3090x now vs 0.3460x on the prior session (recomputed_same_feed), close 13.85 - RVOL fading 11.1855x -> 10.3090x, distribution
- **DUOT** - 8.6874x now vs 0.6227x on the prior session (recomputed_same_feed), close 3.97 - RVOL fading 9.9688x -> 8.6874x, distribution
- **ED** - 6.9051x now vs 0.4803x on the prior session (recomputed_same_feed), close 120.34 - RVOL fading 9.3595x -> 6.9051x, distribution
- **RCAT** - 9.1947x now vs 0.7471x on the prior session (recomputed_same_feed), close 2.57 - RVOL fading 12.4162x -> 9.1947x, distribution
- **KLAR** - 7.2471x now vs 0.7516x on the prior session (recomputed_same_feed), close 14.34 - RVOL fading 11.3748x -> 7.2471x, distribution
- **GLAS** - 10.2724x now vs 0.6565x on the prior session (recomputed_same_feed), close 1.66 - RVOL fading 16.6104x -> 10.2724x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 30 building against 37 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| URNJ | 1.4762 | 0.4187 | 0.0756 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSB | 1.4541 | 0.3565 | 0.3546 | ACCELERATING | 3.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EQPT | 1.3990 | 0.9446 | 0.4495 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EAF | 1.4921 | 0.5606 | 0.6068 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HODL | 1.4982 | 3.1235 | 0.6748 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STCE | 1.3999 | n/a | 0.6325 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CROX | 1.3017 | 1.5791 | 0.6275 | ACCELERATING | 3.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OLMA | 1.4783 | 1.9898 | 0.8298 | ACCELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GLND | 1.3161 | 1.1999 | 0.6721 | ACCELERATING | 8.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BITO | 1.3604 | 1.2621 | 0.8311 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CNOB | 1.4685 | n/a | 0.9758 | ACCELERATING | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PICK | 1.3029 | 0.4683 | 0.8295 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FFIN | 1.3330 | n/a | 0.9010 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HYMC | 1.3392 | 1.2701 | 0.9281 | ACCELERATING | 13.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CDE | 1.3601 | 1.1063 | 1.0222 | ACCELERATING | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSTK | 1.3125 | 0.6130 | 1.0003 | ACCELERATING | 10.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIGI | 1.4542 | 0.4396 | 1.1495 | ACCELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ROST | 1.2906 | 1.0085 | 0.9892 | ACCELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INFQ | 1.2879 | 0.6497 | 1.0087 | ACCELERATING | 12.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KVYO | 1.3599 | 0.7100 | 1.0846 | ACCELERATING | 4.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INOD | 1.3499 | 0.6038 | 1.1086 | ACCELERATING | 10.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ELE | 1.2885 | 0.7238 | 1.0759 | ACCELERATING | 18.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WNTR | 1.2875 | 1.4464 | 1.0770 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IBCP | 1.2800 | 1.2241 | 1.0945 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CPNG | 1.4782 | 0.3161 | 1.3225 | ACCELERATING | 6.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UNH | 1.4030 | 0.7272 | 1.2593 | ACCELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| H | 1.4363 | n/a | 1.3198 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FHN | 1.3696 | 0.8455 | 1.2698 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LH | 1.2852 | 0.5811 | 1.1946 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FSCO | 1.3815 | 0.5636 | 1.2927 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FPS | 1.3646 | 0.5312 | 1.3394 | STABLE | 12.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SA | 1.4182 | 1.3337 | 1.4140 | STABLE | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FLO | 1.3917 | 1.3825 | 1.3989 | STABLE | 3.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STLA | 1.3586 | 1.4469 | 1.3858 | STABLE | 37.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTFC | 1.3294 | n/a | 1.3675 | STABLE | 24.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SFBS | 1.4022 | 0.5610 | 1.4612 | DECELERATING | 31.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSEC | 1.3704 | 0.9050 | 1.4344 | DECELERATING | 2.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FSOL | 1.3417 | 1.9174 | 1.4068 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AAOI | 1.3734 | 0.5222 | 1.4671 | DECELERATING | 31.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADAM | 1.4942 | 0.7606 | 1.5954 | DECELERATING | 3.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OI | 1.2833 | 0.8160 | 1.3984 | DECELERATING | 2.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSNY | 1.3795 | 9.4111 | 1.4976 | DECELERATING | 13.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AEIS | 1.2874 | 0.7590 | 1.4252 | DECELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BXDC | 1.3492 | 15.6456 | 1.4921 | DECELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBWI | 1.2840 | 1.9279 | 1.4504 | DECELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PATH | 1.3140 | 0.8145 | 1.5033 | DECELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSIG | 1.3522 | 0.5384 | 1.5479 | DECELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BFLY | 1.2967 | 1.0221 | 1.4935 | DECELERATING | 16.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XP | 1.3040 | 0.6201 | 1.5045 | DECELERATING | 8.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VPG | 1.3129 | 0.9771 | 1.5293 | DECELERATING | 9.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GOOD | 1.3709 | 0.4079 | 1.5921 | DECELERATING | 3.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BMI | 1.3723 | n/a | 1.6016 | DECELERATING | 30.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMH | 1.4237 | 0.8436 | 1.6668 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGNC | 1.4831 | 0.8458 | 1.7271 | DECELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DBO | 1.4721 | 0.4613 | 1.7243 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OILK | 1.3301 | 0.3686 | 1.5914 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ACRS | 1.2960 | 29.8522 | 1.5697 | DECELERATING | 11.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RYDE | 1.4228 | 1.7370 | 1.7017 | DECELERATING | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BYD | 1.3069 | n/a | 1.6216 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RCI | 1.4356 | 1.8601 | 1.7517 | DECELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTW | 1.4938 | 1.3568 | 1.8316 | DECELERATING | 16.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FWDI | 1.3030 | 2.6038 | 1.7202 | DECELERATING | 30.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MPLT | 1.2998 | n/a | 1.7416 | DECELERATING | 19.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MBX | 1.3405 | n/a | 1.7925 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAPR | 1.2859 | 1.1709 | 1.7673 | DECELERATING | 28.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WWW | 1.3378 | 4.0426 | 1.8407 | DECELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LTBR | 1.3459 | 1.1963 | 1.8794 | DECELERATING | 8.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SILJ | 1.4631 | 1.3200 | 2.0719 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMC | 1.4347 | 1.1639 | 2.0790 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TD | 1.4113 | 0.3092 | 2.1173 | DECELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CVBF | 1.3481 | n/a | 2.0739 | DECELERATING | 27.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVBH | 1.4264 | 2.0239 | 2.2565 | DECELERATING | 2.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **9 entered**, **98 left**, **2 stayed**.

- entered: ALNY, CBRS, CPRI, FOUR, MOD, SENS, TNDM, U, VKTX
- left: ACHR, ALEC, ALNT, AMBQ, AMD, AMPG, ANET, ARKB, ATAT, BCSF, BHYP, BITO, BKKT, BLOX, BRUN, CCOI, CDZI, CHA, CL, COHU, CRCL, CRSR, DFTX, DLB, DPC, DX, ENGN, ETHE, FIGR, FMC, GEV, HL, HLF, HODL, HOOD, HPP, HUBS, HYMC, INBX, IRTC, JNJ, KLC, KMI, KNSA, KODK, LAES, LEVI, LFMD, LMND, LUMN, LUNR, MGNX, MPT, MPWR, MRAM, MSBT, MWH, NRR, NUAI, OGN, OKE, ONTO, OVV, PAAS, PANL, PATH, PEP, PSNY, PSQL, PUBM, Q, QNT, RMIX, S, SBC, SBUX, SGML, SKHY, SLS, SMMT, SOXQ, SOXX, SPCE, SPRX, STGW, STLN, SVM, SYM, TJX, TNXP, UPS, URGN, VELO, VIAV, VSXY, WTW, WWW, YMM
- stayed: ALM, CGON

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 2 of 11 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 755.0s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1844 of 2304 candidates
- unpriced names: 460 of 2304 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero

## Degradation / caveats
- **460 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
