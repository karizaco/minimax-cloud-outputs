---
date: 2026-11-16
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-16
focus_dir_date: 2026-11-13
screen_data_date: 2026-11-12
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1604
wider_universe_source: focus+master+17
wider_universe_size: 1592
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
upstream: /workspace/daily-screens/2026-11-13/focus.md
names_unpriced: 285
published_rows: 100
selectivity: broad_tape
universe_median_rvol: 0.7118
universe_p90_rvol: 1.7407
universe_share_ge_1_5_pct: 14.33
universe_crossings: 133
---

# Focus RVOL snapshot - 2026-11-16 09:45 ET (cron #07)

## TL;DR
- **1319 of 1604** names scored (12 focus + 1592 wider union); **100 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 26 of 100 published** (74 Liquid); **66 near misses**; **17 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **14.33% of the 1319 scored names cleared the 1.5x bar** (median 0.7118x, p90 1.7407x) and there were **133 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: MPT (ACCELERATING), PUBM (ACCELERATING), PSNY (ACCELERATING), OKE (ACCELERATING), CDZI (ACCELERATING), URGN (STABLE), HODL (DECELERATING), LMND (DECELERATING), WWW (DECELERATING), NRR (DECELERATING), BLOX (DECELERATING), BHYP (DECELERATING), HLF (DECELERATING), CGON (DECELERATING), CCOI (DECELERATING), TJX (DECELERATING), SMMT (DECELERATING).** **5 are still building and 11 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **22 building vs 37 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 1592 names from focus+master+17
- scored: 1319; unscored: 285; published rows: 100
- **the scored universe's distribution** (the context for every count below): median 0.7118x, p75 1.1082x, p90 1.7407x, p99 4.9886x; 19.33% at or above 1.275x, **14.33% at or above 1.5x**, 7.43% at or above 2x, 3.41% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LMND | 44.35 | 0.139 | 1.6069 | 1.8959 | 0.0996 | DECELERATING | 0.4744 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 5791 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CHA | 13.94 | 0.157 | 1.0512 | 0.8261 | 0.0792 | ACCELERATING | 1.2429 | recomputed_same_feed | 1.4202 | 14.27 | Liquid | WATCH | 31812 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AMD | 525.56 | 0.141 | 0.8539 | 0.8676 | 0.0897 | STABLE | 0.7244 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 2049226 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FIGR | 25.44 | 0.0577 | 0.6714 | 0.6825 | 0.0404 | STABLE | 1.6768 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 56531 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HUBS | 216.67 | 0.0511 | 0.6325 | 0.6210 | 0.0293 | STABLE | 0.5279 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 14284 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LUNR | 12.29 | 0.0819 | 0.5591 | 0.5830 | 0.0570 | STABLE | 0.9286 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 208510 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ANET | 190.93 | 0.0638 | 0.5488 | 0.5658 | 0.0396 | STABLE | 1.1046 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 91866 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DPC | 33.49 | 0.00343 | 0.1140 | 0.0468 | 0.0007 | ACCELERATING | 0.5021 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IRTC | 92.63 | 0.00656 | 0.0876 | 0.1022 | 0.0039 | STABLE | 0.2248 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CGON | 82.44 | 1.08 | 43.5018 | 45.1204 | 0.6892 | DECELERATING | 0.9029 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 564577 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RMIX | 5.02 | 0.393 | 13.3245 | 11.0641 | 0.1751 | ACCELERATING | 2.5175 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 19668 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SMMT | 12.96 | 0.868 | 13.2234 | 21.8938 | 0.6383 | DECELERATING | 1.1345 | recomputed_same_feed | 1.3503 | 19.07 | RVOL Required | ALERT | 1935264 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PSNY | 2.97 | 0.514 | 11.9622 | 10.5941 | 0.2764 | ACCELERATING | 0.2811 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 23531 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PUBM | 20.90 | 0.317 | 7.9148 | 6.4627 | 0.1568 | ACCELERATING | 0.6271 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 881 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CDZI | 3.06 | 0.187 | 6.1089 | 5.9409 | 0.0722 | ACCELERATING | 1.0980 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 6912 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KLC | 1.30 | 0.678 | 5.7962 | 3.0893 | 0.1006 | ACCELERATING | 23.6672 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 12358 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TJX | 132.81 | 0.271 | 5.7249 | 10.0817 | 0.2462 | DECELERATING | 1.0548 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1481961 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OKE | 88.73 | 0.181 | 5.4587 | 4.4587 | 0.0770 | ACCELERATING | 0.6426 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 30091 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MSBT | 18.70 | 0.639 | 5.4317 | 5.0211 | 0.4392 | ACCELERATING | 3.1125 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ATAT | 39.26 | 0.366 | 5.3884 | 8.8929 | 0.2602 | DECELERATING | 1.7327 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 19095 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BHYP | 37.98 | 1.2 | 5.2401 | 6.5484 | 1.1514 | DECELERATING | 0.6667 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DLB | 61.66 | 0.144 | 5.0185 | 2.9846 | 0.0696 | ACCELERATING | 8.4803 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 2994 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SPCE | 1.63 | 0.513 | 4.9886 | 4.7633 | 0.2947 | ACCELERATING | 5.7750 | recomputed_same_feed | 9.1221 | 65.16 | RVOL Required | WATCH | 305802 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WWW | 25.20 | 0.162 | 4.7792 | 5.1074 | 0.1126 | DECELERATING | 1.4020 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 788 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HLF | 15.96 | 0.18 | 4.5813 | 5.9430 | 0.1348 | DECELERATING | 0.1956 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 4178 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| URGN | 25.55 | 0.207 | 4.4539 | 4.4286 | 0.1037 | STABLE | 0.9426 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 30583 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NRR | 16.88 | 0.692 | 4.3074 | 5.1436 | 0.6243 | DECELERATING | 0.9678 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CCOI | 3.87 | 0.139 | 4.2615 | 6.4170 | 0.1214 | DECELERATING | 0.9782 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 47805 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BLOX | 8.73 | 0.497 | 4.1652 | 5.4350 | 0.3118 | DECELERATING | 0.6518 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HPP | 9.79 | 0.0839 | 3.9088 | 3.7481 | 0.0526 | ACCELERATING | 3.4878 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 997 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MPT | 1.66 | 0.176 | 3.8482 | 1.5825 | 0.0380 | ACCELERATING | 0.5666 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 142853 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HODL | 18.44 | 0.398 | 3.8400 | 4.0182 | 0.1877 | DECELERATING | 1.3263 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INBX | 83.37 | 0.202 | 3.7938 | 1.6398 | 0.0482 | ACCELERATING | 4.4405 | recomputed_same_feed | 4.5715 | 2.95 | RVOL Required | WATCH | 6585 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SBC | 6.84 | 0.485 | 3.7772 | 4.4028 | 0.3429 | DECELERATING | 6.0057 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 35073 | measured_from_nasdaq | 2026-11-16 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 1604
- focus roster size: 12
- wider universe size: 1592
- scored: 1319; unpriced: 285; published rows: 100
- Required count: 26 (of 100 published)
- Liquid count: 74
- NEAR MISS count: 66 (22 building, 37 fading)
- alert count: 17 (5 building, 11 fading)
- crossings: 17 published; **133 across all 1319 scored names**
- universe distribution: median 0.7118x, p90 1.7407x; 14.33% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **MPT** - 3.8482x now vs 0.5666x on the prior session (recomputed_same_feed), close 1.66 - RVOL building 1.5825x -> 3.8482x, accumulation
- **PUBM** - 7.9148x now vs 0.6271x on the prior session (recomputed_same_feed), close 20.90 - RVOL building 6.4627x -> 7.9148x, accumulation
- **PSNY** - 11.9622x now vs 0.2811x on the prior session (recomputed_same_feed), close 2.97 - RVOL building 10.5941x -> 11.9622x, accumulation
- **OKE** - 5.4587x now vs 0.6426x on the prior session (recomputed_same_feed), close 88.73 - RVOL building 4.4587x -> 5.4587x, accumulation
- **CDZI** - 6.1089x now vs 1.0980x on the prior session (recomputed_same_feed), close 3.06 - RVOL building 5.9409x -> 6.1089x, accumulation
- **URGN** - 4.4539x now vs 0.9426x on the prior session (recomputed_same_feed), close 25.55 - RVOL flat 4.4286x -> 4.4539x
- **HODL** - 3.8400x now vs 1.3263x on the prior session (recomputed_same_feed), close 18.44 - RVOL fading 4.0182x -> 3.8400x, distribution
- **LMND** - 1.6069x now vs 0.4744x on the prior session (recomputed_same_feed), close 44.35 - RVOL fading 1.8959x -> 1.6069x, distribution
- **WWW** - 4.7792x now vs 1.4020x on the prior session (recomputed_same_feed), close 25.20 - RVOL fading 5.1074x -> 4.7792x, distribution
- **NRR** - 4.3074x now vs 0.9678x on the prior session (recomputed_same_feed), close 16.88 - RVOL fading 5.1436x -> 4.3074x, distribution
- **BLOX** - 4.1652x now vs 0.6518x on the prior session (recomputed_same_feed), close 8.73 - RVOL fading 5.4350x -> 4.1652x, distribution
- **BHYP** - 5.2401x now vs 0.6667x on the prior session (recomputed_same_feed), close 37.98 - RVOL fading 6.5484x -> 5.2401x, distribution
- **HLF** - 4.5813x now vs 0.1956x on the prior session (recomputed_same_feed), close 15.96 - RVOL fading 5.9430x -> 4.5813x, distribution
- **CGON** - 43.5018x now vs 0.9029x on the prior session (recomputed_same_feed), close 82.44 - RVOL fading 45.1204x -> 43.5018x, distribution
- **CCOI** - 4.2615x now vs 0.9782x on the prior session (recomputed_same_feed), close 3.87 - RVOL fading 6.4170x -> 4.2615x, distribution
- **TJX** - 5.7249x now vs 1.0548x on the prior session (recomputed_same_feed), close 132.81 - RVOL fading 10.0817x -> 5.7249x, distribution
- **SMMT** - 13.2234x now vs 1.1345x on the prior session (recomputed_same_feed), close 12.96 - RVOL fading 21.8938x -> 13.2234x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 22 building against 37 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| MGNX | 1.4523 | 0.9541 | 0.1515 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MWH | 1.3945 | 0.3419 | 0.2701 | ACCELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VSXY | 1.2931 | 0.4163 | 0.3992 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OGN | 1.4085 | 0.3418 | 0.5653 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DX | 1.3419 | 1.8435 | 0.7324 | ACCELERATING | 7.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GEV | 1.2988 | 0.4066 | 0.7329 | ACCELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ENGN | 1.3510 | 3.2339 | 0.9250 | ACCELERATING | 26.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VIAV | 1.3446 | 0.2687 | 0.9514 | ACCELERATING | 6.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ONTO | 1.4119 | 0.3414 | 1.1128 | ACCELERATING | 14.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OVV | 1.4716 | 0.5149 | 1.1763 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALEC | 1.4643 | 1.9568 | 1.1955 | ACCELERATING | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QNT | 1.3431 | 0.8760 | 1.1089 | ACCELERATING | 9.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NUAI | 1.3417 | 2.6977 | 1.1494 | ACCELERATING | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MRAM | 1.3431 | 0.3884 | 1.1511 | ACCELERATING | 9.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BRUN | 1.4567 | 0.8646 | 1.2879 | ACCELERATING | 15.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SOXX | 1.4438 | 0.9226 | 1.3017 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FMC | 1.4426 | 0.7248 | 1.3140 | ACCELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SGML | 1.4288 | 3.5263 | 1.3263 | ACCELERATING | 9.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETHE | 1.4803 | 1.1562 | 1.3946 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TNXP | 1.3595 | 1.3449 | 1.2867 | ACCELERATING | 11.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UPS | 1.3499 | 0.5530 | 1.2828 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PAAS | 1.4867 | 0.4579 | 1.4205 | ACCELERATING | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SYM | 1.4275 | 0.9647 | 1.3782 | STABLE | 15.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STLN | 1.2866 | 0.3847 | 1.2774 | STABLE | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| S | 1.3727 | 1.3425 | 1.3846 | STABLE | 3.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRCL | 1.3729 | 1.0252 | 1.3865 | STABLE | 31.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COHU | 1.2971 | 0.7941 | 1.3246 | STABLE | 7.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PATH | 1.3904 | 0.6126 | 1.4250 | STABLE | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PANL | 1.4649 | 1.2036 | 1.5096 | STABLE | 3.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ACHR | 1.4834 | 0.7519 | 1.5452 | DECELERATING | 21.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BKKT | 1.2961 | 0.5909 | 1.3592 | DECELERATING | 22.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMI | 1.4301 | 0.8297 | 1.4939 | DECELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HOOD | 1.3935 | 1.3305 | 1.4680 | DECELERATING | 24.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VELO | 1.2991 | 0.5694 | 1.3908 | DECELERATING | 21.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SKHY | 1.4154 | 0.7774 | 1.5324 | DECELERATING | 37.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSQL | 1.3370 | 1.7178 | 1.4909 | DECELERATING | 20.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PEP | 1.3979 | 0.4133 | 1.5567 | DECELERATING | 28.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SBUX | 1.3130 | 0.5781 | 1.4891 | DECELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LFMD | 1.3987 | 2.9627 | 1.5785 | DECELERATING | 5.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALNT | 1.3224 | n/a | 1.5120 | DECELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CL | 1.4445 | 0.5416 | 1.6421 | DECELERATING | 3.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALM | 1.3273 | 1.1391 | 1.5345 | DECELERATING | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KNSA | 1.3594 | 1.2127 | 1.5679 | DECELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LUMN | 1.3870 | 0.4856 | 1.6032 | DECELERATING | 10.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLS | 1.4869 | 2.5142 | 1.7043 | DECELERATING | 17.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HYMC | 1.4754 | 0.5006 | 1.6976 | DECELERATING | 14.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVM | 1.4605 | 0.3890 | 1.7035 | DECELERATING | 12.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LAES | 1.3324 | 0.5219 | 1.5926 | DECELERATING | 20.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MPWR | 1.3521 | 0.2857 | 1.6243 | DECELERATING | 18.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LEVI | 1.3682 | 0.8663 | 1.6535 | DECELERATING | 0.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BITO | 1.4958 | 1.1440 | 1.7828 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRSR | 1.4662 | 0.6355 | 1.7899 | DECELERATING | 33.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KODK | 1.3011 | 0.1617 | 1.6275 | DECELERATING | 24.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JNJ | 1.3420 | 0.9244 | 1.6714 | DECELERATING | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| YMM | 1.3194 | 0.4218 | 1.6640 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPRX | 1.2779 | 0.2930 | 1.6322 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ARKB | 1.3285 | 1.0691 | 1.6867 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMPG | 1.2900 | 8.8489 | 1.6544 | DECELERATING | 26.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STGW | 1.3984 | 0.1206 | 1.8296 | DECELERATING | 8.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HL | 1.2844 | 0.5867 | 1.7249 | DECELERATING | 16.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTW | 1.3301 | 0.3622 | 1.7746 | DECELERATING | 38.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| Q | 1.3254 | 0.5865 | 1.7778 | DECELERATING | 20.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SOXQ | 1.4000 | 0.3809 | 1.9175 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BCSF | 1.3906 | 0.3331 | 1.9174 | DECELERATING | 5.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DFTX | 1.3989 | 0.9839 | 1.9994 | DECELERATING | 6.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMBQ | 1.3215 | 0.6881 | 2.1505 | DECELERATING | 30.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **8 entered**, **98 left**, **1 stayed**.

- entered: AMD, ANET, DPC, FIGR, HUBS, IRTC, LMND, LUNR
- left: AAOI, ADIG, APLD, APMD, AREC, AVR, AXGN, AXTI, AZTA, BCS, BJRI, BNY, BSOL, BTC, BZ, CADL, CAE, CAPR, CBRS, CDNL, CGEM, CLDX, COIN, CRWV, CSWC, CTVA, CVLT, CXW, DGII, DGXX, ETHB, EZPW, FLO, FPS, GHRS, GLXY, GSOL, HOOD, HTFL, INBX, INIO, IONQ, JBS, KDP, KLAR, LAZR, LCID, LFTO, LGN, LOW, MBGL, MFA, MLYS, MOD, MSTW, NAMS, NB, NBIS, NEOV, NIQ, NKTR, NLY, NMAX, NVAX, NVDA, OGE, PANL, PBLS, PRE, PURR, RCEL, RPRX, RVMD, RZLT, S, SGMT, SHAZ, SIDU, SIVR, SMMT, SNDK, SPCE, SSMR, STDN, STIM, STRO, STUB, TGEN, TMQ, UAMY, USAS, VIR, XE, XLAB, XNCR, YSS, ZBIO, ZETA
- stayed: CHA

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of 9 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 300.0s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1319 of 1604 candidates
- unpriced names: 285 of 1604 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero

## Degradation / caveats
- **285 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
