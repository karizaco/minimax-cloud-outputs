---
date: 2026-11-19
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-19
focus_dir_date: 2026-11-18
screen_data_date: 2026-11-17
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1822
wider_universe_source: focus+master+17
wider_universe_size: 1810
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
upstream: /workspace/daily-screens/2026-11-18/focus.md
names_unpriced: 320
published_rows: 138
selectivity: broad_tape
universe_median_rvol: 0.8129
universe_p90_rvol: 2.1003
universe_share_ge_1_5_pct: 19.31
universe_crossings: 185
---

# Focus RVOL snapshot - 2026-11-19 09:45 ET (cron #07)

## TL;DR
- **1502 of 1822** names scored (12 focus + 1810 wider union); **138 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 27 of 138 published** (111 Liquid); **102 near misses**; **23 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **19.31% of the 1502 scored names cleared the 1.5x bar** (median 0.8129x, p90 2.1003x) and there were **185 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: GL (ACCELERATING), CPNG (ACCELERATING), RLX (ACCELERATING), ATEYY (ACCELERATING), BIO (ACCELERATING), WWD (ACCELERATING), OFG (ACCELERATING), SCI (ACCELERATING), MPC (ACCELERATING), DMC (ACCELERATING), WSM (ACCELERATING), PANW (ACCELERATING), AMBA (DECELERATING), SPOT (DECELERATING), HSY (DECELERATING), SA (DECELERATING), SKYA (DECELERATING), BBWI (DECELERATING), AFL (DECELERATING), HACK (DECELERATING), CTKB (DECELERATING), ICLR (DECELERATING), STTK (DECELERATING).** **12 are still building and 11 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **58 building vs 34 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 1810 names from focus+master+17
- scored: 1502; unscored: 320; published rows: 138
- **the scored universe's distribution** (the context for every count below): median 0.8129x, p75 1.3028x, p90 2.1003x, p99 6.6914x; 26.1% at or above 1.275x, **19.31% at or above 1.5x**, 11.32% at or above 2x, 5.46% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SLS | 15.82 | 0.648 | 4.4493 | 6.3996 | 0.5368 | DECELERATING | 2.2419 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 8221341 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BRBR | 14.25 | 0.149 | 3.2291 | 2.3655 | 0.0582 | ACCELERATING | 15.9599 | recomputed_same_feed | 19.8105 | 34.91 | RVOL Required | WATCH | 7599 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ENR | 26.83 | 0.0591 | 1.4378 | 0.7455 | 0.0205 | ACCELERATING | 3.9745 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 775 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| YALA | 5.84 | 0.0706 | 1.0812 | 0.9639 | 0.0318 | ACCELERATING | 3.5132 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 200 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ALAB | 234.54 | 0.108 | 1.0183 | 1.0877 | 0.0734 | DECELERATING | 1.4737 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 153721 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RYTM | 118.12 | 0.057 | 0.9057 | 0.2712 | 0.0114 | ACCELERATING | 0.4429 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 2412 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VIK | 98.72 | 0.0558 | 0.8202 | 1.1029 | 0.0334 | DECELERATING | 1.8621 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 799 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNAP | 5.52 | 0.0588 | 0.6891 | 0.4214 | 0.0231 | ACCELERATING | 2.0673 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 247940 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RARE | 17.58 | 0.0236 | 0.6706 | 1.2017 | 0.0148 | DECELERATING | 2.3908 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 9004 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SHAZ | 23.51 | 0.0728 | 0.6545 | 0.6119 | 0.0441 | STABLE | 0.6338 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 47735 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LUMN | 4.32 | 0.0268 | 0.5706 | 0.2984 | 0.0071 | ACCELERATING | 0.6978 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 28050 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ARM | 187.97 | 0.075 | 0.5575 | 0.5942 | 0.0484 | STABLE | 1.0606 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 95935 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GL | 154.80 | 0.493 | 16.9798 | 1.2435 | 0.0190 | ACCELERATING | 1.3898 | recomputed_same_feed | 1.4644 | 8.07 | RVOL Required | ALERT | 467 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STTK | 4.45 | 0.348 | 14.0963 | 25.4189 | 0.3288 | DECELERATING | 0.4622 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 216 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SKYA | 4.18 | 0.259 | 13.7949 | 17.0941 | 0.1805 | DECELERATING | 1.4267 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 228241 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DRH | 14.35 | 0.237 | 12.6422 | 10.4124 | 0.1132 | ACCELERATING | 1.6095 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 101910 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WWD | 342.67 | 0.335 | 11.0110 | 7.4635 | 0.1146 | ACCELERATING | 1.0273 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 3605 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SCI | 70.33 | 0.175 | 10.2052 | 7.3932 | 0.0756 | ACCELERATING | 1.4526 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CPNG | 14.84 | 0.553 | 9.1533 | 1.5626 | 0.0478 | ACCELERATING | 0.4101 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 44408 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DMC | 25.24 | 0.321 | 8.5221 | 7.4443 | 0.1487 | ACCELERATING | 1.0490 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1146 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MPC | 371.40 | 0.493 | 8.3354 | 7.1966 | 0.2166 | ACCELERATING | 1.3697 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 403662 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HACK | 125.71 | 0.773 | 8.1319 | 12.0075 | 0.6568 | DECELERATING | 0.5216 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CTKB | 6.11 | 0.273 | 7.9265 | 12.0039 | 0.2563 | DECELERATING | 0.5617 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2800 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SA | 22.37 | 0.562 | 7.8145 | 9.8782 | 0.4194 | DECELERATING | 1.3391 | recomputed_same_feed | 1.4308 | 18.18 | RVOL Required | ALERT | 138601 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RLX | 1.45 | 0.185 | 7.3891 | 1.0696 | 0.0146 | ACCELERATING | 0.9320 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 180 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| JMIA | 2.41 | 0.732 | 7.1010 | 6.1310 | 0.3124 | ACCELERATING | 14.5332 | recomputed_same_feed | 27.9928 | 104.95 | RVOL Required | WATCH | 221427 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ATEYY | 172.24 | 0.0456 | 6.8513 | 2.4287 | 0.0073 | ACCELERATING | 0.4602 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SPOT | 595.96 | 0.385 | 6.6914 | 7.0191 | 0.2073 | DECELERATING | 0.9064 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 4126 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AFL | 124.52 | 0.234 | 6.6861 | 10.4243 | 0.2203 | DECELERATING | 0.8666 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 389 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AMBA | 61.50 | 0.343 | 6.4349 | 6.6604 | 0.2325 | DECELERATING | 0.4399 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 134636 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BIO | 379.40 | 0.446 | 6.4270 | 2.3873 | 0.0982 | ACCELERATING | 0.4133 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BBWI | 18.23 | 0.234 | 6.4098 | 9.9176 | 0.1554 | DECELERATING | 0.9721 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 437347 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ICLR | 195.47 | 0.238 | 6.2982 | 11.1496 | 0.2193 | DECELERATING | 0.9498 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 129130 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WSM | 241.75 | 0.302 | 6.0892 | 5.1208 | 0.1260 | ACCELERATING | 0.6832 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 45427 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OFG | 49.88 | 0.173 | 5.9231 | 3.0193 | 0.0620 | ACCELERATING | 1.0530 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 11842 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HSY | 172.06 | 0.226 | 5.8609 | 6.4965 | 0.1238 | DECELERATING | 1.4846 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 628 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PANW | 365.53 | 0.483 | 5.5985 | 5.2751 | 0.2848 | ACCELERATING | 0.9496 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 699264 | measured_from_nasdaq | 2026-11-19 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 1822
- focus roster size: 12
- wider universe size: 1810
- scored: 1502; unpriced: 320; published rows: 138
- Required count: 27 (of 138 published)
- Liquid count: 111
- NEAR MISS count: 102 (58 building, 34 fading)
- alert count: 23 (12 building, 11 fading)
- crossings: 23 published; **185 across all 1502 scored names**
- universe distribution: median 0.8129x, p90 2.1003x; 19.31% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **GL** - 16.9798x now vs 1.3898x on the prior session (recomputed_same_feed), close 154.80 - RVOL building 1.2435x -> 16.9798x, accumulation
- **CPNG** - 9.1533x now vs 0.4101x on the prior session (recomputed_same_feed), close 14.84 - RVOL building 1.5626x -> 9.1533x, accumulation
- **RLX** - 7.3891x now vs 0.9320x on the prior session (recomputed_same_feed), close 1.45 - RVOL building 1.0696x -> 7.3891x, accumulation
- **ATEYY** - 6.8513x now vs 0.4602x on the prior session (recomputed_same_feed), close 172.24 - RVOL building 2.4287x -> 6.8513x, accumulation
- **BIO** - 6.4270x now vs 0.4133x on the prior session (recomputed_same_feed), close 379.40 - RVOL building 2.3873x -> 6.4270x, accumulation
- **WWD** - 11.0110x now vs 1.0273x on the prior session (recomputed_same_feed), close 342.67 - RVOL building 7.4635x -> 11.0110x, accumulation
- **OFG** - 5.9231x now vs 1.0530x on the prior session (recomputed_same_feed), close 49.88 - RVOL building 3.0193x -> 5.9231x, accumulation
- **SCI** - 10.2052x now vs 1.4526x on the prior session (recomputed_same_feed), close 70.33 - RVOL building 7.3932x -> 10.2052x, accumulation
- **MPC** - 8.3354x now vs 1.3697x on the prior session (recomputed_same_feed), close 371.40 - RVOL building 7.1966x -> 8.3354x, accumulation
- **DMC** - 8.5221x now vs 1.0490x on the prior session (recomputed_same_feed), close 25.24 - RVOL building 7.4443x -> 8.5221x, accumulation
- **WSM** - 6.0892x now vs 0.6832x on the prior session (recomputed_same_feed), close 241.75 - RVOL building 5.1208x -> 6.0892x, accumulation
- **PANW** - 5.5985x now vs 0.9496x on the prior session (recomputed_same_feed), close 365.53 - RVOL building 5.2751x -> 5.5985x, accumulation
- **AMBA** - 6.4349x now vs 0.4399x on the prior session (recomputed_same_feed), close 61.50 - RVOL fading 6.6604x -> 6.4349x, distribution
- **SPOT** - 6.6914x now vs 0.9064x on the prior session (recomputed_same_feed), close 595.96 - RVOL fading 7.0191x -> 6.6914x, distribution
- **HSY** - 5.8609x now vs 1.4846x on the prior session (recomputed_same_feed), close 172.06 - RVOL fading 6.4965x -> 5.8609x, distribution
- **SA** - 7.8145x now vs 1.3391x on the prior session (recomputed_same_feed), close 22.37 - RVOL fading 9.8782x -> 7.8145x, distribution
- **SKYA** - 13.7949x now vs 1.4267x on the prior session (recomputed_same_feed), close 4.18 - RVOL fading 17.0941x -> 13.7949x, distribution
- **BBWI** - 6.4098x now vs 0.9721x on the prior session (recomputed_same_feed), close 18.23 - RVOL fading 9.9176x -> 6.4098x, distribution
- **AFL** - 6.6861x now vs 0.8666x on the prior session (recomputed_same_feed), close 124.52 - RVOL fading 10.4243x -> 6.6861x, distribution
- **HACK** - 8.1319x now vs 0.5216x on the prior session (recomputed_same_feed), close 125.71 - RVOL fading 12.0075x -> 8.1319x, distribution
- **CTKB** - 7.9265x now vs 0.5617x on the prior session (recomputed_same_feed), close 6.11 - RVOL fading 12.0039x -> 7.9265x, distribution
- **ICLR** - 6.2982x now vs 0.9498x on the prior session (recomputed_same_feed), close 195.47 - RVOL fading 11.1496x -> 6.2982x, distribution
- **STTK** - 14.0963x now vs 0.4622x on the prior session (recomputed_same_feed), close 4.45 - RVOL fading 25.4189x -> 14.0963x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 58 building against 34 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| GNR | 1.4474 | 1.0514 | 0.0112 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CGBD | 1.3238 | 0.2779 | 0.0248 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TWI | 1.4257 | 1.9258 | 0.1282 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SCOP | 1.3051 | n/a | 0.0750 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CBAN | 1.3142 | 2.4454 | 0.1326 | ACCELERATING | 0.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CP | 1.2915 | 1.0931 | 0.2934 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETSY | 1.4638 | 0.9066 | 0.5954 | ACCELERATING | 4.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRIN | 1.3771 | 1.1183 | 0.5565 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ABR | 1.3853 | 1.3889 | 0.5971 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KOS | 1.4105 | 1.5362 | 0.6338 | ACCELERATING | 3.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UNP | 1.4954 | 1.0570 | 0.7668 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ENR | 1.4378 | 3.9745 | 0.7455 | ACCELERATING | 1.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TDOC | 1.3333 | 0.8018 | 0.6590 | ACCELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADUR | 1.4470 | 1.1509 | 0.7834 | ACCELERATING | 11.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RBLX | 1.3831 | 0.9389 | 0.7221 | ACCELERATING | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PCG | 1.3036 | 1.0501 | 0.6582 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADC | 1.3569 | 0.6105 | 0.7230 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CNQ | 1.4003 | 1.7724 | 0.7672 | ACCELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PBF | 1.4815 | 1.3797 | 0.8995 | ACCELERATING | 3.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FTNT | 1.4747 | 0.4632 | 0.9122 | ACCELERATING | 8.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SFM | 1.4209 | 0.7198 | 0.8594 | ACCELERATING | 3.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MTZ | 1.2797 | 0.3642 | 0.7558 | ACCELERATING | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PURR | 1.3932 | 0.6961 | 0.9182 | ACCELERATING | 12.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DEO | 1.2760 | 1.5344 | 0.8160 | ACCELERATING | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PACB | 1.2944 | 1.0812 | 0.8554 | ACCELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HPQ | 1.3558 | 0.7197 | 0.9385 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRSP | 1.3476 | 1.1355 | 0.9394 | ACCELERATING | 7.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ESTC | 1.4470 | 4.0657 | 1.0658 | ACCELERATING | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PRAX | 1.4069 | 0.7579 | 1.0441 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HR | 1.2933 | 0.7436 | 0.9471 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KR | 1.4928 | 1.9208 | 1.1546 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRI | 1.3173 | 0.9828 | 0.9926 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMC | 1.2798 | 0.9450 | 0.9908 | ACCELERATING | 18.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRML | 1.3857 | 0.7597 | 1.1006 | ACCELERATING | 16.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WHR | 1.4398 | 1.2197 | 1.1740 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TEAM | 1.2945 | 0.6283 | 1.0454 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GEHC | 1.3209 | 0.8806 | 1.0762 | ACCELERATING | 6.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XEL | 1.3697 | 1.0526 | 1.1412 | ACCELERATING | 25.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSLV | 1.3897 | 3.6172 | 1.1627 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GGN | 1.3987 | 2.6552 | 1.1861 | ACCELERATING | 0.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ECL | 1.4019 | 1.1752 | 1.1941 | ACCELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NEXN | 1.3613 | 0.2688 | 1.1665 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAR | 1.2832 | 0.9591 | 1.0918 | ACCELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LIN | 1.3810 | 1.0438 | 1.2121 | ACCELERATING | 6.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMGN | 1.3690 | 1.2269 | 1.2290 | ACCELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IHAK | 1.3939 | 0.5921 | 1.2611 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COCO | 1.3295 | 2.4337 | 1.2006 | ACCELERATING | 4.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FMS | 1.3331 | 1.6677 | 1.2183 | ACCELERATING | 19.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AUR | 1.3349 | 1.5081 | 1.2266 | ACCELERATING | 18.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MA | 1.3734 | 1.0999 | 1.2678 | ACCELERATING | 6.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MLM | 1.2887 | 1.3912 | 1.1907 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HYMC | 1.4237 | 1.9614 | 1.3342 | ACCELERATING | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| THC | 1.3805 | 0.6930 | 1.3052 | ACCELERATING | 5.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GOOGL | 1.4592 | 0.6339 | 1.3897 | ACCELERATING | 26.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASH | 1.3906 | 0.9830 | 1.3239 | ACCELERATING | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CTAS | 1.4755 | 0.9928 | 1.4134 | ACCELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HDB | 1.3539 | 0.7470 | 1.2921 | ACCELERATING | 5.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MKL | 1.4235 | 0.6822 | 1.3630 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CCJ | 1.3571 | 1.7139 | 1.3084 | STABLE | 10.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBAI | 1.4833 | 1.0167 | 1.4542 | STABLE | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PLTR | 1.4472 | 0.5655 | 1.4196 | STABLE | 13.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARCO | 1.3139 | 0.8206 | 1.3154 | STABLE | 2.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| V | 1.2790 | 1.3619 | 1.2854 | STABLE | 3.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPWR | 1.3609 | 1.8752 | 1.3756 | STABLE | 20.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TFPM | 1.3940 | 2.1119 | 1.4096 | STABLE | 5.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NCLD | 1.3096 | 1.5452 | 1.3393 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QCOM | 1.3078 | 1.0802 | 1.3500 | STABLE | 26.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SAFE | 1.2960 | 1.2370 | 1.3455 | STABLE | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSM | 1.2913 | 1.1470 | 1.3453 | DECELERATING | 26.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STLA | 1.2927 | 1.5897 | 1.3540 | DECELERATING | 38.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BL | 1.4771 | 1.1478 | 1.5475 | DECELERATING | 14.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVIX | 1.4105 | 1.9933 | 1.4965 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WWW | 1.3645 | 0.7437 | 1.4863 | DECELERATING | 2.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMZN | 1.3100 | 0.6884 | 1.4416 | DECELERATING | 21.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PONY | 1.3495 | 4.5234 | 1.4914 | DECELERATING | 6.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IONQ | 1.3528 | 1.0282 | 1.5198 | DECELERATING | 26.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DOC | 1.4285 | 1.4013 | 1.6012 | DECELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALMS | 1.4581 | 1.7379 | 1.6377 | DECELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMP | 1.4625 | 8.5861 | 1.6492 | DECELERATING | 2.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AYI | 1.4745 | n/a | 1.6643 | DECELERATING | 20.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALM | 1.4153 | 1.2706 | 1.6067 | DECELERATING | 14.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BHP | 1.3458 | 2.0550 | 1.5604 | DECELERATING | 29.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRV | 1.3142 | 1.2459 | 1.5312 | DECELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EWW | 1.3534 | 2.1196 | 1.5807 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HLIT | 1.3356 | 0.8435 | 1.5833 | DECELERATING | 24.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DRD | 1.4580 | 2.3165 | 1.7078 | DECELERATING | 28.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HPE | 1.3131 | 0.9344 | 1.5631 | DECELERATING | 18.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RGEN | 1.4876 | 5.1720 | 1.7666 | DECELERATING | 0.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KLAC | 1.2972 | 0.5483 | 1.6016 | DECELERATING | 40.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NRXP | 1.4918 | 1.8760 | 1.8179 | DECELERATING | 22.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OLLI | 1.3028 | 0.8924 | 1.6365 | DECELERATING | 8.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLVP | 1.3259 | 2.5350 | 1.6771 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASTL | 1.3198 | 0.3269 | 1.7272 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORKA | 1.3347 | 0.3830 | 1.7503 | DECELERATING | 8.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MYRG | 1.3885 | 0.8089 | 1.8231 | DECELERATING | 39.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GH | 1.3334 | 0.3704 | 1.8006 | DECELERATING | 23.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RH | 1.4323 | 0.9966 | 1.9125 | DECELERATING | 25.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UMC | 1.4749 | 1.0514 | 1.9763 | DECELERATING | 19.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAG | 1.4636 | 1.2131 | 2.0072 | DECELERATING | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGX | 1.3484 | 0.9377 | 1.9367 | DECELERATING | 21.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RCEL | 1.2932 | 2.7183 | 2.1769 | DECELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MDGL | 1.2903 | 5.2585 | 2.8368 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **11 entered**, **100 left**, **1 stayed**.

- entered: ALAB, ARM, ENR, LUMN, RARE, RYTM, SHAZ, SLS, SNAP, VIK, YALA
- left: ADSK, ADUR, AEE, AES, AIOT, ALM, AMX, ARDT, ASC, ASST, AUR, AXGN, BBT, BEKE, BILL, BLK, BSX, CCB, CCCC, CENX, CGON, CING, CLBK, CME, CNX, COF, CRTO, CUE, DAKT, DLB, DPRO, ERO, FLO, FRVO, GANX, GILD, GL, GLBE, HD, HL, HTLD, HUBS, IAM, JMIA, JPM, KURA, LZB, MAIA, MAIN, MDB, MDGL, MDLN, MNRO, MOH, MSTR, NAVN, NEWP, NFE, NKE, NTLA, NXT, OCTV, OMF, OPEN, PAGS, PBF, PG, PHG, PNNT, PONY, POOL, POWL, POWW, PRMB, PSIG, PYPD, QLYS, QTWO, REXR, RWAY, SA, SAP, SEZL, SKT, SPCE, SVIX, SVRA, SVXY, TGB, TJX, TRMD, TROX, TSN, TU, ULCC, URGN, VIA, VYX, WCN, WELL
- stayed: BRBR

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of 12 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 304.5s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1502 of 1822 candidates
- unpriced names: 320 of 1822 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 138 published rows - measured_from_nasdaq 120, not_subtracted 18; 18 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **320 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
