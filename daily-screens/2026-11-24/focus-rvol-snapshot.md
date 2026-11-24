---
date: 2026-11-24
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-24
focus_dir_date: 2026-11-23
screen_data_date: 2026-11-20
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 3154
wider_universe_source: focus+master+17
wider_universe_size: 3142
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
pm_source_status: partial
cross_check_source: same_series_truncated
status: ok
upstream: /workspace/daily-screens/2026-11-23/focus.md
names_unpriced: 806
published_rows: 183
selectivity: broad_tape
universe_median_rvol: 0.7808
universe_p90_rvol: 1.9057
universe_share_ge_1_5_pct: 16.35
universe_crossings: 189
---

# Focus RVOL snapshot - 2026-11-24 09:45 ET (cron #07)

## TL;DR
- **2348 of 3154** names scored (12 focus + 3142 wider union); **183 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 27 of 183 published** (156 Liquid); **147 near misses**; **12 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **16.35% of the 2348 scored names cleared the 1.5x bar** (median 0.7808x, p90 1.9057x) and there were **189 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: EMBC (ACCELERATING), PINS (ACCELERATING), BBIO (ACCELERATING), TNGX (ACCELERATING), PRTA (ACCELERATING), CMP (ACCELERATING), KVYO (DECELERATING), MDT (DECELERATING), BILI (DECELERATING), INSM (DECELERATING), FTI (DECELERATING), VFF (DECELERATING).** **6 are still building and 6 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **84 building vs 52 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 3142 names from focus+master+17
- scored: 2348; unscored: 806; published rows: 183
- **the scored universe's distribution** (the context for every count below): median 0.7808x, p75 1.2089x, p90 1.9057x, p99 6.788x; 22.61% at or above 1.275x, **16.35% at or above 1.5x**, 9.07% at or above 2x, 4.05% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SNDK | 80.51 | 0.155 | 6.7880 | 6.8381 | 0.1031 | DECELERATING | 13.2632 | recomputed_same_feed | 13.1681 | -0.72 | RVOL Required | WATCH | 6776633 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KVYO | 23.39 | 0.12 | 2.2219 | 3.0496 | 0.0867 | DECELERATING | 1.3786 | recomputed_same_feed | 1.3471 | -1.22 | RVOL Required | ALERT | 105487 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NTLA | 9.91 | 0.0735 | 1.1818 | 0.9615 | 0.0310 | ACCELERATING | 1.4973 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 9597 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INTC | 56.69 | 0.137 | 1.1572 | 1.2768 | 0.0969 | DECELERATING | 1.8098 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 6671463 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IREN | 13.24 | 0.138 | 0.8403 | 0.7881 | 0.0862 | ACCELERATING | 2.8745 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 3830595 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CBLL | 29.28 | 0.0517 | 0.8314 | 0.5088 | 0.0123 | ACCELERATING | 4.1612 | recomputed_same_feed | 5.0129 | 20.47 | Liquid | WATCH | 607 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NVDA | 154.86 | 0.15 | 0.7786 | 0.7743 | 0.1030 | STABLE | 2.4431 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 26421570 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NOK | 7.35 | 0.12 | 0.7611 | 0.5389 | 0.0646 | ACCELERATING | 1.5566 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 2357607 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GPN | 92.41 | 0.018 | 0.5380 | 0.7253 | 0.0104 | DECELERATING | 1.3533 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 10457 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PLMR | 165.78 | 0.0123 | 0.2269 | 0.1646 | 0.0050 | ACCELERATING | 2.4315 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 445 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HTFL | 48.18 | 0.0114 | 0.1721 | 0.3342 | 0.0076 | DECELERATING | 0.6344 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 3668 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INSM | 170.35 | 4.72 | 83.7119 | 88.5017 | 3.7970 | DECELERATING | 0.4398 | recomputed_same_feed | 0.7086 | 61.07 | RVOL Required | ALERT | 19357379 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VFF | 2.15 | 2.14 | 40.2627 | 95.2369 | 2.1261 | DECELERATING | 1.3605 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 3394812 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EMBC | 7.60 | 0.975 | 29.9199 | 19.4025 | 0.3667 | ACCELERATING | 0.6785 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 48400 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ANF | 171.62 | 0.888 | 19.5407 | 23.8671 | 0.5330 | DECELERATING | 2.5664 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 260187 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| COGT | 32.69 | 0.753 | 19.4002 | 20.8336 | 0.4237 | DECELERATING | 2.1386 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 88641 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TEX | 60.29 | 0.4 | 18.5532 | 14.1722 | 0.1478 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 2707 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FTI | 58.81 | 0.407 | 16.6036 | 31.4342 | 0.3955 | DECELERATING | 0.8092 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1209210 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FLNC | 4.02 | 1.37 | 14.1086 | 15.5407 | 1.0004 | DECELERATING | 1.7179 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 4605865 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SPRX | 30.22 | 1.25 | 13.5641 | 26.8965 | 1.0116 | DECELERATING | 2.3662 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DY | 186.65 | 0.473 | 11.8894 | 10.2068 | 0.2046 | ACCELERATING | 1.6137 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 14658 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SJM | 129.00 | 0.292 | 11.7884 | 16.5144 | 0.2381 | DECELERATING | 1.7880 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 57062 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STOK | 29.61 | 0.321 | 10.6333 | 13.6064 | 0.2658 | DECELERATING | 1.5302 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BURL | 255.69 | 0.386 | 9.7732 | 16.9653 | 0.3018 | DECELERATING | 1.9970 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 311420 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CTA | 24.94 | 0.392 | 9.4646 | 7.8628 | 0.1655 | ACCELERATING | 2.2848 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PINS | 19.07 | 0.34 | 8.9084 | 5.6685 | 0.0934 | ACCELERATING | 1.3139 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 23927 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MLTX | 12.70 | 0.288 | 8.6439 | 1.3254 | 0.0166 | ACCELERATING | 5.2297 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 4403 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CMP | 22.83 | 0.239 | 8.6389 | 8.5303 | 0.1272 | ACCELERATING | 0.9276 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1003 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ICUI | 176.45 | 0.278 | 7.8307 | 14.6120 | 0.2223 | DECELERATING | 1.5466 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 8069 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TGLS | 53.99 | 0.21 | 7.5993 | 11.0132 | 0.1530 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 333 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SPYM | 84.48 | 0.555 | 7.5026 | 12.4245 | 0.5261 | DECELERATING | 3.0764 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TNGX | 24.82 | 0.302 | 7.3242 | 6.2608 | 0.1239 | ACCELERATING | 1.4800 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 9716 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BBIO | 83.24 | 0.586 | 7.0526 | 4.0623 | 0.1977 | ACCELERATING | 0.8615 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 9902 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BILI | 11.07 | 0.706 | 6.8265 | 8.4564 | 0.4857 | DECELERATING | 1.3365 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 840509 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MDT | 99.86 | 0.333 | 6.5289 | 7.6459 | 0.2151 | DECELERATING | 1.4810 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 155316 | measured_from_nasdaq | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PRTA | 8.82 | 0.21 | 6.3496 | 5.5910 | 0.1117 | ACCELERATING | 1.1869 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-24 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 3154
- focus roster size: 12
- wider universe size: 3142
- scored: 2348; unpriced: 806; published rows: 183
- Required count: 27 (of 183 published)
- Liquid count: 156
- NEAR MISS count: 147 (84 building, 52 fading)
- alert count: 12 (6 building, 6 fading)
- crossings: 12 published; **189 across all 2348 scored names**
- universe distribution: median 0.7808x, p90 1.9057x; 16.35% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **EMBC** - 29.9199x now vs 0.6785x on the prior session (recomputed_same_feed), close 7.60 - RVOL building 19.4025x -> 29.9199x, accumulation
- **PINS** - 8.9084x now vs 1.3139x on the prior session (recomputed_same_feed), close 19.07 - RVOL building 5.6685x -> 8.9084x, accumulation
- **BBIO** - 7.0526x now vs 0.8615x on the prior session (recomputed_same_feed), close 83.24 - RVOL building 4.0623x -> 7.0526x, accumulation
- **TNGX** - 7.3242x now vs 1.4800x on the prior session (recomputed_same_feed), close 24.82 - RVOL building 6.2608x -> 7.3242x, accumulation
- **PRTA** - 6.3496x now vs 1.1869x on the prior session (recomputed_same_feed), close 8.82 - RVOL building 5.5910x -> 6.3496x, accumulation
- **CMP** - 8.6389x now vs 0.9276x on the prior session (recomputed_same_feed), close 22.83 - RVOL building 8.5303x -> 8.6389x, accumulation
- **KVYO** - 2.2219x now vs 1.3786x on the prior session (recomputed_same_feed), close 23.39 - RVOL fading 3.0496x -> 2.2219x, distribution
- **MDT** - 6.5289x now vs 1.4810x on the prior session (recomputed_same_feed), close 99.86 - RVOL fading 7.6459x -> 6.5289x, distribution
- **BILI** - 6.8265x now vs 1.3365x on the prior session (recomputed_same_feed), close 11.07 - RVOL fading 8.4564x -> 6.8265x, distribution
- **INSM** - 83.7119x now vs 0.4398x on the prior session (recomputed_same_feed), close 170.35 - RVOL fading 88.5017x -> 83.7119x, distribution
- **FTI** - 16.6036x now vs 0.8092x on the prior session (recomputed_same_feed), close 58.81 - RVOL fading 31.4342x -> 16.6036x, distribution
- **VFF** - 40.2627x now vs 1.3605x on the prior session (recomputed_same_feed), close 2.15 - RVOL fading 95.2369x -> 40.2627x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 84 building against 52 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| LBRX | 1.3921 | 0.7409 | 0.0360 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVA | 1.4090 | 2.1526 | 0.0739 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMRC | 1.4039 | 1.3434 | 0.1040 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VOX | 1.3389 | 1.3399 | 0.0902 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ESTA | 1.3018 | 2.0020 | 0.0611 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDVY | 1.4971 | 2.0841 | 0.3062 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SWIM | 1.4733 | 0.3554 | 0.4069 | ACCELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WH | 1.3812 | n/a | 0.3350 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TARS | 1.4035 | 0.4543 | 0.3767 | ACCELERATING | 13.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARTY | 1.4860 | 2.0615 | 0.5163 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGIO | 1.4665 | 0.8733 | 0.4992 | ACCELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PHAT | 1.3027 | 1.6486 | 0.3554 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DFAE | 1.3968 | 9.1803 | 0.5072 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UPB | 1.3456 | 8.6565 | 0.4586 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IRON | 1.4320 | 1.7416 | 0.5511 | ACCELERATING | 15.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPMD | 1.4472 | 2.6242 | 0.6366 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSEC | 1.3552 | 2.1300 | 0.5625 | ACCELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AOA | 1.3167 | n/a | 0.5264 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RCKT | 1.4407 | 1.6959 | 0.6893 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PTCT | 1.3049 | 1.6330 | 0.5587 | ACCELERATING | 9.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RXST | 1.2774 | 2.0418 | 0.5416 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EWW | 1.2813 | 1.9609 | 0.5461 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AIG | 1.3218 | n/a | 0.6374 | ACCELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EGP | 1.2814 | 2.3954 | 0.6155 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ELMT | 1.4595 | 1.5473 | 0.8287 | ACCELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MDY | 1.4937 | 2.4157 | 0.8791 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EXLS | 1.3631 | 1.0033 | 0.7599 | ACCELERATING | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VOYG | 1.3812 | 3.2942 | 0.7988 | ACCELERATING | 7.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PTEN | 1.4477 | 0.9732 | 0.8664 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVAX | 1.4685 | 1.4197 | 0.9162 | ACCELERATING | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETY | 1.2778 | 0.9185 | 0.7280 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RPD | 1.4753 | 0.8600 | 0.9276 | ACCELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMPS | 1.3755 | 1.0508 | 0.8605 | ACCELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BTX | 1.4867 | 1.3475 | 0.9928 | ACCELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FIDU | 1.3044 | 1.5384 | 0.8223 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OEF | 1.3949 | 1.9833 | 0.9232 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASHR | 1.4995 | 2.3616 | 1.0329 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WCLD | 1.4042 | 0.6670 | 0.9391 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KR | 1.4245 | 0.9054 | 0.9698 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VTWO | 1.3881 | 2.8917 | 0.9577 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TPL | 1.3237 | 2.2592 | 0.9119 | ACCELERATING | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPTM | 1.3674 | 2.2548 | 0.9724 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XYL | 1.3207 | 1.0076 | 0.9323 | ACCELERATING | 2.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALKS | 1.4927 | 0.5133 | 1.1063 | ACCELERATING | 9.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVR | 1.3121 | 3.9434 | 0.9276 | ACCELERATING | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FICO | 1.3428 | 1.0621 | 0.9833 | ACCELERATING | 13.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SCHG | 1.2913 | 2.6055 | 0.9331 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VMC | 1.3573 | 1.3332 | 0.9996 | ACCELERATING | 28.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FUBO | 1.4563 | 1.2404 | 1.1085 | ACCELERATING | 8.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CNH | 1.2905 | 1.0467 | 0.9464 | ACCELERATING | 0.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INTU | 1.4985 | 1.6214 | 1.1562 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GNRC | 1.4052 | 1.5626 | 1.0764 | ACCELERATING | 2.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NCLD | 1.3719 | 2.0858 | 1.0461 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QTOP | 1.4928 | 5.4592 | 1.1923 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DKNG | 1.2812 | 1.1855 | 0.9867 | ACCELERATING | 3.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GDRX | 1.3225 | 2.6224 | 1.0302 | ACCELERATING | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TEM | 1.3028 | 1.6803 | 1.0134 | ACCELERATING | 6.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMBA | 1.2831 | 2.9484 | 1.0230 | ACCELERATING | 18.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIRI | 1.3813 | 1.3306 | 1.1305 | ACCELERATING | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IWF | 1.4501 | 1.8739 | 1.2015 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ERIC | 1.4752 | 2.2051 | 1.2440 | ACCELERATING | 8.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WGMI | 1.4677 | 1.3120 | 1.2491 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INVH | 1.3691 | 1.3693 | 1.1537 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QNDX | 1.4286 | 3.3374 | 1.2150 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KNX | 1.3777 | 0.9812 | 1.1668 | ACCELERATING | 19.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRWD | 1.4999 | 6.1245 | 1.2908 | ACCELERATING | 16.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CGBL | 1.4751 | 1.9605 | 1.2781 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ON | 1.3636 | 3.1365 | 1.1748 | ACCELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVOL | 1.3699 | 3.0808 | 1.1942 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VOO | 1.4093 | 2.6886 | 1.2379 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SRPT | 1.3101 | 2.4334 | 1.1460 | ACCELERATING | 3.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MMYT | 1.4551 | 0.4543 | 1.3078 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MEDP | 1.4992 | 1.1336 | 1.3571 | ACCELERATING | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INTR | 1.3003 | 1.8392 | 1.1585 | ACCELERATING | 14.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HIMX | 1.4512 | 3.0821 | 1.3276 | ACCELERATING | 6.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVCO | 1.3171 | 2.4794 | 1.1936 | ACCELERATING | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SMH | 1.2778 | 2.8337 | 1.1753 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NKE | 1.3340 | 1.1882 | 1.2462 | ACCELERATING | 16.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BAX | 1.2994 | 0.9414 | 1.2118 | ACCELERATING | 2.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FCEL | 1.3043 | 2.7920 | 1.2195 | ACCELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMO | 1.3778 | 0.6892 | 1.3127 | ACCELERATING | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MU | 1.3123 | 2.3127 | 1.2578 | ACCELERATING | 27.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PENG | 1.3361 | 2.1332 | 1.2855 | ACCELERATING | 14.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VOD | 1.4507 | 2.8751 | 1.4005 | ACCELERATING | 16.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PLAB | 1.4816 | 2.2245 | 1.4360 | STABLE | 11.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BKNG | 1.2948 | 1.7983 | 1.2533 | STABLE | 4.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AOD | 1.4687 | 1.3150 | 1.4362 | STABLE | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLDX | 1.2840 | 2.3706 | 1.2554 | STABLE | 8.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVBH | 1.4808 | 1.9751 | 1.4852 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BMA | 1.4208 | 0.8291 | 1.4372 | STABLE | 21.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HBM | 1.4637 | 1.6551 | 1.4876 | STABLE | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IFF | 1.4834 | 2.4945 | 1.5187 | STABLE | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETHA | 1.3160 | 1.9550 | 1.3586 | STABLE | 29.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| REXC | 1.3358 | n/a | 1.3812 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IMRX | 1.4350 | 0.4311 | 1.4846 | STABLE | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JKS | 1.3112 | 1.5206 | 1.3627 | DECELERATING | 11.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAA | 1.3229 | 2.3186 | 1.3845 | DECELERATING | 5.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INFY | 1.3106 | 3.1831 | 1.3726 | DECELERATING | 1.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IOT | 1.3655 | 1.5480 | 1.4455 | DECELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IBKR | 1.4750 | 2.7282 | 1.5598 | DECELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZS | 1.4448 | 14.8931 | 1.5311 | DECELERATING | 11.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LEU | 1.3284 | 2.2967 | 1.4201 | DECELERATING | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DBO | 1.3855 | 1.1868 | 1.4803 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBD | 1.4825 | 0.6866 | 1.5881 | DECELERATING | 16.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MCHP | 1.3351 | 2.1987 | 1.4471 | DECELERATING | 6.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HPQ | 1.3118 | 1.6996 | 1.4378 | DECELERATING | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JEPQ | 1.3950 | 3.1183 | 1.5253 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLDP | 1.4806 | 1.2430 | 1.6219 | DECELERATING | 23.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PB | 1.3074 | n/a | 1.4607 | DECELERATING | 14.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GPIX | 1.2827 | 2.3105 | 1.4381 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DTCR | 1.3874 | 1.0750 | 1.5624 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STE | 1.3299 | n/a | 1.5107 | DECELERATING | 7.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RMBS | 1.2943 | 2.1492 | 1.4862 | DECELERATING | 16.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XPEV | 1.2901 | 1.5715 | 1.4918 | DECELERATING | 17.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDY | 1.4065 | 1.3018 | 1.6155 | DECELERATING | 20.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ABUS | 1.3450 | 0.8245 | 1.5756 | DECELERATING | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EH | 1.3019 | 1.8229 | 1.5442 | DECELERATING | 13.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BELFB | 1.2932 | 1.3025 | 1.5368 | DECELERATING | 37.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MSGK | 1.3993 | n/a | 1.6585 | DECELERATING | 26.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PAGP | 1.2920 | 1.2203 | 1.5579 | DECELERATING | 2.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OUNZ | 1.3295 | 2.3010 | 1.6235 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VLRS | 1.2920 | n/a | 1.5936 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ACMR | 1.4378 | 1.5265 | 1.7418 | DECELERATING | 18.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETW | 1.3194 | 2.6276 | 1.6246 | DECELERATING | 5.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HYLN | 1.3895 | 1.5361 | 1.7026 | DECELERATING | 13.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PBF | 1.3591 | 1.8382 | 1.6854 | DECELERATING | 10.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LTBR | 1.3255 | 2.1794 | 1.6608 | DECELERATING | 18.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GEMI | 1.2751 | 0.9659 | 1.6198 | DECELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BST | 1.3553 | 4.9677 | 1.7134 | DECELERATING | 39.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XRAY | 1.3963 | 0.9681 | 1.7808 | DECELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMB | 1.3406 | 0.7231 | 1.7948 | DECELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ROP | 1.3070 | 1.2687 | 1.7692 | DECELERATING | 30.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PRAX | 1.4958 | 1.1825 | 1.9894 | DECELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NWPX | 1.4494 | n/a | 1.9482 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARWR | 1.3488 | 0.6179 | 1.8552 | DECELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PTON | 1.3978 | 2.3115 | 1.9068 | DECELERATING | 8.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KWEB | 1.4408 | 1.0712 | 1.9564 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSI | 1.3424 | 2.5503 | 1.8965 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UPS | 1.2920 | 1.2008 | 1.9067 | DECELERATING | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BAM | 1.3434 | 2.0494 | 1.9903 | DECELERATING | 0.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XSD | 1.2751 | 1.9058 | 1.9253 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NSLR | 1.4881 | 1.5602 | 2.1744 | DECELERATING | 22.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XMMO | 1.2773 | 1.0515 | 1.9768 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FWDI | 1.3656 | 2.9800 | 2.0810 | DECELERATING | 33.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ROCQ | 1.3344 | 1.6854 | 2.1473 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DAPP | 1.3096 | n/a | 2.2577 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRFK | 1.4318 | n/a | 2.5409 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **8 entered**, **236 left**, **3 stayed**.

- entered: GPN, HTFL, INTC, IREN, NOK, NTLA, NVDA, PLMR
- left: AAL, ABCL, ABVX, ACHR, AEHR, AEM, AESI, AGI, AGLT, ALM, AMBA, AMD, AMPX, AOD, APP, ASB, AVBH, AVPT, AWK, B, BB, BCAX, BELFB, BEN, BETR, BHC, BIDU, BJ, BKKT, BKSY, BLDP, BLK, BRX, BSM, BSP, BST, BWXT, CAG, CAPR, CECO, CELH, CGAU, CHAT, CIEN, CINF, CLM, CMCO, CNP, COCO, COHU, CPNG, CRBG, CRK, CRWD, CSX, CVS, CXT, DFTX, DISK, DPC, EMPD, EMR, EQX, ESLT, ETN, EVGO, EWT, EXG, FAST, FDMT, FIS, FLO, FNV, FPI, FSLR, FSLY, FTK, FTS, GAP, GAU, GBCI, GFI, GGN, GILD, GLUE, GM, GNRC, GRAB, GSL, HBAN, HBNC, HLIT, HOMB, HOS, HPE, HR, HRI, IDCC, INDI, INO, INSM, INVH, IRTC, ITW, IVR, JBLU, JD, JKHY, JKS, KD, KHC, KKR, KMX, KNSL, KYMR, L, LASR, MA, MAGN, MATW, MEC, MET, MFG, MKC, MRNA, MXL, NAMS, NATL, NAVN, NCLH, NEXA, NEXT, NI, NKTR, NN, NRGV, NTAP, NTSK, NUAI, NVA, NVMI, NWCL, NXG, NXPI, OABI, OBIO, OKTA, ONDS, OSK, OTIS, P, PANW, PCG, PDD, PIPR, PRLB, PSI, PSUS, PURR, PYPL, QNT, QUBT, RDDT, RDY, RIG, RLI, ROP, RSI, RVI, RVII, RYAM, RYTM, S, SAIL, SBSW, SBUX, SCCO, SCHW, SEZL, SFM, SHW, SIRI, SMHX, SNEX, SNN, SOUN, SPCX, SSB, SSMR, SSP, SSYS, STX, SUPX, SVM, SWKS, SYM, T, TDY, TENX, TIGR, TKR, TLRY, TMC, TMDX, TMQ, TOYO, TRLV, TRNS, TRU, TRV, TS, TU, TW, TXG, UBS, UL, UPB, UPBD, UPWK, USAR, VCX, VRDN, VST, VZ, WAT, WDAY, WGMI, WMB, WMT, WTFC, WTW, WWD, XP, ZCSH, ZS, ZWS
- stayed: CBLL, KVYO, SNDK

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 3 of 11 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 516.7s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 2348 of 3154 candidates
- unpriced names: 806 of 3154 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 183 published rows - measured_from_nasdaq 127, not_subtracted 56; 56 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **806 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
