---
date: 2026-11-18
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-18
focus_dir_date: 2026-11-17
screen_data_date: 2026-11-16
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1734
wider_universe_source: focus+master+17
wider_universe_size: 1722
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
upstream: /workspace/daily-screens/2026-11-17/focus.md
names_unpriced: 347
published_rows: 101
selectivity: broad_tape
universe_median_rvol: 0.7091
universe_p90_rvol: 1.7916
universe_share_ge_1_5_pct: 13.99
universe_crossings: 123
---

# Focus RVOL snapshot - 2026-11-18 09:45 ET (cron #07)

## TL;DR
- **1387 of 1734** names scored (12 focus + 1722 wider union); **101 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 27 of 101 published** (74 Liquid); **65 near misses**; **19 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **13.99% of the 1387 scored names cleared the 1.5x bar** (median 0.7091x, p90 1.7916x) and there were **123 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: JMIA (ACCELERATING), WELL (ACCELERATING), MDGL (ACCELERATING), BILL (ACCELERATING), OMF (ACCELERATING), TJX (ACCELERATING), BRBR (ACCELERATING), ERO (DECELERATING), LZB (DECELERATING), TGB (DECELERATING), GANX (DECELERATING), PSIG (DECELERATING), CRTO (DECELERATING), ARDT (DECELERATING), PRMB (DECELERATING), GLBE (DECELERATING), MDLN (DECELERATING), CUE (DECELERATING), AES (DECELERATING).** **7 are still building and 12 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **40 building vs 20 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 1722 names from focus+master+17
- scored: 1387; unscored: 347; published rows: 101
- **the scored universe's distribution** (the context for every count below): median 0.7091x, p75 1.0825x, p90 1.7916x, p99 7.7017x; 18.67% at or above 1.275x, **13.99% at or above 1.5x**, 8.07% at or above 2x, 3.6% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BILL | 65.23 | 0.116 | 4.8303 | 3.1479 | 0.0433 | ACCELERATING | 0.5899 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 15441 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| POWL | 150.84 | 0.14 | 2.3494 | 3.1702 | 0.1097 | DECELERATING | 3.2319 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 46111 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TSN | 64.03 | 0.0509 | 1.0502 | 0.8097 | 0.0215 | ACCELERATING | 0.8185 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 3577 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ULCC | 8.11 | 0.0385 | 0.7252 | 0.5720 | 0.0191 | ACCELERATING | 0.6082 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1427 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| URGN | 29.04 | 0.0292 | 0.5860 | 0.5048 | 0.0127 | ACCELERATING | 0.6620 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 4216 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| QLYS | 180.90 | 0.0246 | 0.4983 | 0.2947 | 0.0091 | ACCELERATING | 0.6376 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1395 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TU | 9.33 | 0.0362 | 0.3754 | 0.4456 | 0.0255 | DECELERATING | 1.3264 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 8358 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SEZL | 156.14 | 0.0374 | 0.3431 | 0.2060 | 0.0136 | ACCELERATING | 0.4650 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1759 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MOH | 216.69 | 0.0133 | 0.2433 | 0.1128 | 0.0031 | ACCELERATING | 1.5568 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HUBS | 213.07 | 0.0161 | 0.2039 | 0.1639 | 0.0077 | STABLE | 0.5702 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1793 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CGON | 79.27 | 0.018 | 0.1977 | 0.0405 | 0.0022 | ACCELERATING | 1.0124 | recomputed_same_feed | 0.9604 | -5.14 | Liquid | WATCH | 0 | not_subtracted | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CUE | 3.34 | 5.62 | 127.2108 | 196.7374 | 3.9155 | DECELERATING | 0.5667 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1483721 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AES | 15.01 | 4.76 | 88.1861 | 195.3250 | 4.3092 | DECELERATING | 0.2150 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 43607366 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PRMB | 22.60 | 1.26 | 42.6247 | 54.8732 | 0.8197 | DECELERATING | 0.4014 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2214409 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MDLN | 38.67 | 1.64 | 42.1814 | 56.6191 | 1.0136 | DECELERATING | 0.8226 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 5355859 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GLBE | 36.70 | 1.16 | 35.2866 | 48.2046 | 0.9131 | DECELERATING | 1.2028 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 327821 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ARDT | 14.25 | 1.31 | 28.7722 | 39.1382 | 0.8522 | DECELERATING | 0.4145 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 344760 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| JMIA | 3.51 | 1.51 | 27.9928 | 17.0587 | 0.6040 | ACCELERATING | 0.6195 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 758751 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BRBR | 13.52 | 0.418 | 19.8105 | 19.6732 | 0.2100 | ACCELERATING | 1.3102 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 330138 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CCB | 37.56 | 0.485 | 15.4907 | 21.5756 | 0.2753 | DECELERATING | 2.8252 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OMF | 58.67 | 0.261 | 11.1597 | 10.3932 | 0.1475 | ACCELERATING | 0.2953 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 770 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MAIA | 1.37 | 0.761 | 10.7630 | 11.9859 | 0.3351 | DECELERATING | 7.1567 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 47932 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DLB | 57.94 | 0.307 | 9.3805 | 7.4288 | 0.1278 | ACCELERATING | 3.4781 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 57931 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CRTO | 18.87 | 0.257 | 8.7918 | 13.1852 | 0.1504 | DECELERATING | 0.9320 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 60321 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LZB | 31.10 | 0.179 | 7.7205 | 7.9306 | 0.1112 | DECELERATING | 1.2829 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1669 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MNRO | 10.63 | 0.259 | 7.7017 | 1.5272 | 0.0187 | ACCELERATING | 1.8458 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 480 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WELL | 246.46 | 0.212 | 6.9312 | 0.7585 | 0.0127 | ACCELERATING | 1.0933 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 641 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TJX | 140.51 | 0.387 | 6.1725 | 5.6608 | 0.2329 | ACCELERATING | 1.1284 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 538994 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TROX | 1.53 | 0.344 | 5.9803 | 5.3665 | 0.1665 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 12819 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GANX | 1.19 | 0.405 | 5.9668 | 8.3737 | 0.3156 | DECELERATING | 0.6200 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 71787 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ERO | 24.11 | 0.298 | 5.6491 | 5.7179 | 0.1646 | DECELERATING | 0.9060 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 103168 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PONY | 4.19 | 0.708 | 5.5347 | 7.2119 | 0.4802 | DECELERATING | 4.3448 | recomputed_same_feed | 3.7959 | -12.63 | RVOL Required | WATCH | 866901 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TGB | 5.59 | 0.26 | 5.4679 | 6.2566 | 0.1646 | DECELERATING | 0.9454 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 115536 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SVRA | 4.74 | 0.226 | 5.2630 | 4.6209 | 0.1309 | ACCELERATING | 4.1177 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 222451 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MDGL | 420.05 | 0.195 | 5.0538 | 0.7611 | 0.0150 | ACCELERATING | 0.1949 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2863 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PSIG | 3.52 | 0.295 | 4.9537 | 7.6616 | 0.2062 | DECELERATING | 1.3993 | recomputed_same_feed | 1.3522 | -3.37 | RVOL Required | ALERT | 156325 | measured_from_nasdaq | 2026-11-18 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 1734
- focus roster size: 12
- wider universe size: 1722
- scored: 1387; unpriced: 347; published rows: 101
- Required count: 27 (of 101 published)
- Liquid count: 74
- NEAR MISS count: 65 (40 building, 20 fading)
- alert count: 19 (7 building, 12 fading)
- crossings: 19 published; **123 across all 1387 scored names**
- universe distribution: median 0.7091x, p90 1.7916x; 13.99% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **JMIA** - 27.9928x now vs 0.6195x on the prior session (recomputed_same_feed), close 3.51 - RVOL building 17.0587x -> 27.9928x, accumulation
- **WELL** - 6.9312x now vs 1.0933x on the prior session (recomputed_same_feed), close 246.46 - RVOL building 0.7585x -> 6.9312x, accumulation
- **MDGL** - 5.0538x now vs 0.1949x on the prior session (recomputed_same_feed), close 420.05 - RVOL building 0.7611x -> 5.0538x, accumulation
- **BILL** - 4.8303x now vs 0.5899x on the prior session (recomputed_same_feed), close 65.23 - RVOL building 3.1479x -> 4.8303x, accumulation
- **OMF** - 11.1597x now vs 0.2953x on the prior session (recomputed_same_feed), close 58.67 - RVOL building 10.3932x -> 11.1597x, accumulation
- **TJX** - 6.1725x now vs 1.1284x on the prior session (recomputed_same_feed), close 140.51 - RVOL building 5.6608x -> 6.1725x, accumulation
- **BRBR** - 19.8105x now vs 1.3102x on the prior session (recomputed_same_feed), close 13.52 - RVOL building 19.6732x -> 19.8105x, accumulation
- **ERO** - 5.6491x now vs 0.9060x on the prior session (recomputed_same_feed), close 24.11 - RVOL fading 5.7179x -> 5.6491x, distribution
- **LZB** - 7.7205x now vs 1.2829x on the prior session (recomputed_same_feed), close 31.10 - RVOL fading 7.9306x -> 7.7205x, distribution
- **TGB** - 5.4679x now vs 0.9454x on the prior session (recomputed_same_feed), close 5.59 - RVOL fading 6.2566x -> 5.4679x, distribution
- **GANX** - 5.9668x now vs 0.6200x on the prior session (recomputed_same_feed), close 1.19 - RVOL fading 8.3737x -> 5.9668x, distribution
- **PSIG** - 4.9537x now vs 1.3993x on the prior session (recomputed_same_feed), close 3.52 - RVOL fading 7.6616x -> 4.9537x, distribution
- **CRTO** - 8.7918x now vs 0.9320x on the prior session (recomputed_same_feed), close 18.87 - RVOL fading 13.1852x -> 8.7918x, distribution
- **ARDT** - 28.7722x now vs 0.4145x on the prior session (recomputed_same_feed), close 14.25 - RVOL fading 39.1382x -> 28.7722x, distribution
- **PRMB** - 42.6247x now vs 0.4014x on the prior session (recomputed_same_feed), close 22.60 - RVOL fading 54.8732x -> 42.6247x, distribution
- **GLBE** - 35.2866x now vs 1.2028x on the prior session (recomputed_same_feed), close 36.70 - RVOL fading 48.2046x -> 35.2866x, distribution
- **MDLN** - 42.1814x now vs 0.8226x on the prior session (recomputed_same_feed), close 38.67 - RVOL fading 56.6191x -> 42.1814x, distribution
- **CUE** - 127.2108x now vs 0.5667x on the prior session (recomputed_same_feed), close 3.34 - RVOL fading 196.7374x -> 127.2108x, distribution
- **AES** - 88.1861x now vs 0.2150x on the prior session (recomputed_same_feed), close 15.01 - RVOL fading 195.3250x -> 88.1861x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 40 building against 20 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| AXGN | 1.3337 | 0.9874 | 0.0474 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| REXR | 1.4843 | 0.6468 | 0.3565 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RWAY | 1.3928 | 1.3754 | 0.2973 | ACCELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NEWP | 1.4360 | 1.3841 | 0.3999 | ACCELERATING | 2.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADUR | 1.3251 | n/a | 0.4168 | ACCELERATING | 8.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CCCC | 1.3161 | 0.6094 | 0.4443 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PHG | 1.2960 | 0.7937 | 0.4473 | ACCELERATING | 2.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PAGS | 1.3337 | 1.4839 | 0.5104 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SKT | 1.3206 | 0.6665 | 0.5280 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NFE | 1.3355 | 1.5177 | 0.6467 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NAVN | 1.4763 | 0.7242 | 0.7955 | ACCELERATING | 3.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASST | 1.4069 | 0.5806 | 0.7601 | ACCELERATING | 19.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PNNT | 1.3687 | 0.9180 | 0.7372 | ACCELERATING | 15.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JPM | 1.4840 | 1.3985 | 0.8799 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASC | 1.4806 | 0.8517 | 0.8857 | ACCELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HTLD | 1.4441 | 1.0317 | 0.8617 | ACCELERATING | 2.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLK | 1.3019 | 0.5835 | 0.8271 | ACCELERATING | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVIX | 1.4670 | 0.5644 | 1.0637 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DAKT | 1.4522 | 3.8610 | 1.0778 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLBK | 1.3890 | 1.8543 | 1.0162 | ACCELERATING | 0.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SA | 1.4308 | 1.5208 | 1.0649 | ACCELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VYX | 1.3411 | 0.3660 | 0.9904 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAIN | 1.4191 | 1.1854 | 1.0716 | ACCELERATING | 4.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| POOL | 1.3884 | 1.0718 | 1.0638 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BEKE | 1.4202 | 0.6268 | 1.0997 | ACCELERATING | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HD | 1.3911 | 2.2919 | 1.0728 | ACCELERATING | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CING | 1.3263 | 21.6306 | 1.0157 | ACCELERATING | 15.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVXY | 1.4214 | 0.8205 | 1.1487 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPCE | 1.2917 | 2.6902 | 1.0190 | ACCELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KURA | 1.4556 | 2.8267 | 1.2112 | ACCELERATING | 8.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VIA | 1.3502 | 0.3458 | 1.1503 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BSX | 1.4929 | 0.5448 | 1.3027 | ACCELERATING | 21.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GL | 1.4644 | n/a | 1.3318 | ACCELERATING | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MSTR | 1.4920 | 0.5857 | 1.3611 | ACCELERATING | 23.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OPEN | 1.2784 | 0.9597 | 1.1499 | ACCELERATING | 14.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OCTV | 1.3141 | 1.3389 | 1.2007 | ACCELERATING | 12.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SAP | 1.4531 | 0.8608 | 1.3510 | ACCELERATING | 15.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CME | 1.3614 | 0.6518 | 1.2748 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HL | 1.3482 | 1.0781 | 1.2967 | ACCELERATING | 12.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AIOT | 1.2790 | 1.3175 | 1.2286 | ACCELERATING | 0.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GILD | 1.4283 | 1.1147 | 1.3895 | STABLE | 3.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRMD | 1.4419 | 1.3423 | 1.4086 | STABLE | 16.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FLO | 1.2758 | 1.5099 | 1.2427 | STABLE | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NTLA | 1.3439 | 1.1395 | 1.3440 | STABLE | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADSK | 1.2831 | 0.5822 | 1.3118 | STABLE | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| POWW | 1.3630 | 0.7434 | 1.4445 | DECELERATING | 4.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NKE | 1.4674 | 3.7110 | 1.5526 | DECELERATING | 13.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CNX | 1.3697 | 0.8589 | 1.4665 | DECELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WCN | 1.3538 | 0.7383 | 1.4506 | DECELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALM | 1.2933 | 1.3210 | 1.4807 | DECELERATING | 15.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DPRO | 1.4388 | 1.2879 | 1.6312 | DECELERATING | 22.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CENX | 1.3356 | 0.9175 | 1.5556 | DECELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PBF | 1.3413 | 0.6756 | 1.6564 | DECELERATING | 2.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PYPD | 1.4162 | 1.1152 | 1.7390 | DECELERATING | 14.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IAM | 1.4506 | 0.2590 | 1.7948 | DECELERATING | 19.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FRVO | 1.3837 | 0.3892 | 1.7573 | DECELERATING | 7.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NXT | 1.4447 | 1.2156 | 1.8356 | DECELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BBT | 1.3849 | 1.0856 | 1.7889 | DECELERATING | 9.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AEE | 1.4504 | 0.4916 | 1.8692 | DECELERATING | 25.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MDB | 1.4143 | 1.4364 | 1.8431 | DECELERATING | 38.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QTWO | 1.3093 | 0.6425 | 1.8068 | DECELERATING | 25.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PG | 1.2883 | 0.8313 | 1.8760 | DECELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AUR | 1.3994 | 0.5950 | 2.0418 | DECELERATING | 34.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COF | 1.3681 | 0.4140 | 2.2610 | DECELERATING | 0.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMX | 1.4509 | 0.6440 | 2.8646 | DECELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **10 entered**, **107 left**, **1 stayed**.

- entered: BILL, HUBS, MOH, POWL, QLYS, SEZL, TSN, TU, ULCC, URGN
- left: AAOI, ABX, ACRS, ADAM, ADIG, AEIS, AGNC, ALM, ALNY, AMH, AS, AVBH, BBIO, BBWI, BFLY, BITO, BMI, BXDC, BYD, CANG, CAPR, CBRS, CDE, CMC, CNOB, CPNG, CPRI, CROX, CVBF, DBO, DCOM, DUOT, EAF, ED, ELE, EQPT, FFIN, FHN, FLO, FOUR, FPS, FR, FSCO, FSOL, FWDI, GFF, GLAS, GLND, GLSI, GOOD, H, HODL, HXL, HYMC, IBCP, INFQ, INOD, KLAR, KVYO, LH, LTBR, MBX, MOD, MPLT, NRIM, NSIT, OI, OILK, OLMA, OMER, PATH, PICK, PICS, PKX, PONY, PRAX, PSEC, PSIG, PSIX, PSNY, RCAT, RCI, RNA, ROST, RYDE, SA, SENS, SFBS, SIGI, SILJ, SSB, SSTK, STCE, STLA, TD, TNDM, U, UNH, URNJ, VKTX, VPG, WNTR, WTFC, WTW, WWD, WWW, XP
- stayed: CGON

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of 11 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 283.3s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1387 of 1734 candidates
- unpriced names: 347 of 1734 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 101 published rows - measured_from_nasdaq 93, not_subtracted 8; 8 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number
- REPAIR (this fire): the CSV's `tier` column said `WATCH` on two names that this artifact's own near-miss table publishes — **GL (1.4644x)** and **ADUR (1.3251x)** — because both have an unavailable prior reading (`prev_session_rvol_source: unavailable`). The near-miss band is a LEVEL rule and does not depend on the prior reading; the prior reading only decides a CROSSING. Both rows are tiered `NEAR MISS`, which makes the CSV (65 NEAR MISS rows) agree with the `### Counts` block and the near-miss table. **No number changed** — the tier label and the front-matter `pm_source_status` (was hardcoded `measured_from_series`, which named a source that produced ZERO rows here) are the only edits. The engine fix is in `karizaco/maxhermes-migration` (`tools/focus_rvol_score.py`, commit `73ebb24`) so the next fire derives both values instead of asserting them.

## Degradation / caveats
- **347 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
