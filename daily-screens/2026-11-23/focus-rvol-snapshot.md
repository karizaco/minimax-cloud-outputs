---
date: 2026-11-23
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-23
focus_dir_date: 2026-11-20
screen_data_date: 2026-11-19
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 2198
wider_universe_source: focus+master+17
wider_universe_size: 2186
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
upstream: /workspace/daily-screens/2026-11-20/focus.md
names_unpriced: 414
published_rows: 239
selectivity: broad_tape
universe_median_rvol: 1.2586
universe_p90_rvol: 2.5281
universe_share_ge_1_5_pct: 37.67
universe_crossings: 314
---

# Focus RVOL snapshot - 2026-11-23 09:45 ET (cron #07)

## TL;DR
- **1784 of 2198** names scored (12 focus + 2186 wider union); **239 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 32 of 239 published** (207 Liquid); **203 near misses**; **14 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **37.67% of the 1784 scored names cleared the 1.5x bar** (median 1.2586x, p90 2.5281x) and there were **314 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: BHC (ACCELERATING), CBLL (ACCELERATING), RVI (ACCELERATING), AEHR (ACCELERATING), IVR (ACCELERATING), NUAI (ACCELERATING), UPB (DECELERATING), PANW (DECELERATING), HPE (DECELERATING), NTSK (DECELERATING), BST (DECELERATING), SCCO (DECELERATING), OBIO (DECELERATING), ZS (DECELERATING).** **6 are still building and 8 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **89 building vs 83 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 2186 names from focus+master+17
- scored: 1784; unscored: 414; published rows: 239
- **the scored universe's distribution** (the context for every count below): median 1.2586x, p75 1.8109x, p90 2.5281x, p99 5.2062x; 49.05% at or above 1.275x, **37.67% at or above 1.5x**, 20.24% at or above 2x, 6.11% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMBA | 55.80 | 0.217 | 3.2178 | 2.9917 | 0.1402 | ACCELERATING | 1.9801 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 51734 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NTSK | 25.27 | 0.173 | 3.0694 | 4.1899 | 0.1144 | DECELERATING | 1.4586 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 107741 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PURR | 8.85 | 0.278 | 2.4805 | 2.0302 | 0.1438 | ACCELERATING | 2.3990 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1002444 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PANW | 354.84 | 0.192 | 1.8742 | 2.2461 | 0.1454 | DECELERATING | 1.3947 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 678177 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OKTA | 204.57 | 0.124 | 1.7956 | 1.7277 | 0.0624 | ACCELERATING | 1.5900 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 46628 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IVR | 5.45 | 0.0951 | 1.5935 | 1.1156 | 0.0426 | ACCELERATING | 1.0878 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 18549 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NUAI | 4.32 | 0.174 | 1.5346 | 1.3348 | 0.0896 | ACCELERATING | 1.2330 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 770018 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| P | 102.54 | 0.0977 | 1.4373 | 1.3878 | 0.0555 | STABLE | 1.5324 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 69615 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VRDN | 31.14 | 0.0279 | 0.7972 | 0.4520 | 0.0079 | ACCELERATING | 2.7243 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 1378 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INSM | 145.14 | 0.0415 | 0.7086 | 0.5003 | 0.0225 | ACCELERATING | 1.4998 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 11400 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DPC | 33.63 | 0.0174 | 0.5576 | 0.1024 | 0.0018 | ACCELERATING | 0.4422 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TU | 10.82 | 0.0406 | 0.3931 | 0.2839 | 0.0182 | ACCELERATING | 0.7602 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 16330 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KYMR | 144.02 | 2.11 | 64.4519 | 78.0610 | 1.5636 | DECELERATING | 1.7029 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1063471 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ZS | 230.66 | 1.79 | 24.4035 | 31.4153 | 1.2182 | DECELERATING | 1.0671 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1661651 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNDK | 93.46 | 0.301 | 13.1681 | 14.9510 | 0.2254 | DECELERATING | 6.3909 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 16508059 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CAPR | 1.94 | 1.35 | 11.2371 | 13.2887 | 1.0133 | DECELERATING | 2.9661 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 5441853 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SYM | 36.80 | 0.599 | 11.0402 | 13.6226 | 0.4589 | DECELERATING | 1.7722 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 52592 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BHC | 8.24 | 0.304 | 10.3728 | 0.7956 | 0.0104 | ACCELERATING | 0.6880 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 4523 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| UPB | 1.87 | 0.159 | 8.9850 | 9.1886 | 0.0998 | DECELERATING | 0.8237 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 509 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CRWD | 209.81 | 0.908 | 8.5764 | 10.0471 | 0.6476 | DECELERATING | 1.6516 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 3472218 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EMPD | 1.93 | 1.94 | 8.0325 | 8.9983 | 1.9201 | DECELERATING | 41.9566 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1002484 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SMHX | 45.79 | 0.719 | 7.1413 | 9.0037 | 0.6090 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BSP | 46.37 | 0.572 | 6.5850 | 5.3321 | 0.2545 | ACCELERATING | 5.7180 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 142255 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ABVX | 75.42 | 0.186 | 6.4079 | 8.7059 | 0.1280 | DECELERATING | 1.5813 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 130215 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OBIO | 6.92 | 0.498 | 5.9513 | 8.7681 | 0.4933 | DECELERATING | 0.8522 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 340600 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NATL | 47.87 | 0.242 | 5.7297 | 0.6273 | 0.0221 | ACCELERATING | 2.1113 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AEHR | 47.80 | 0.848 | 5.6590 | 2.7859 | 0.2744 | ACCELERATING | 1.4892 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 358255 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SUPX | 3.65 | 0.158 | 5.4433 | 3.5167 | 0.0666 | ACCELERATING | 3.7395 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 12134 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OABI | 4.82 | 0.197 | 5.3340 | 4.2545 | 0.1038 | ACCELERATING | 3.1824 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 20986 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EWT | 90.27 | 0.621 | 5.2364 | 5.4757 | 0.3491 | DECELERATING | 1.6716 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FAST | 51.29 | 0.21 | 5.2062 | 2.7604 | 0.0722 | ACCELERATING | 4.4396 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 81772 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SCCO | 141.90 | 0.391 | 5.1342 | 7.7428 | 0.3222 | DECELERATING | 1.1529 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 195601 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RVI | 18.75 | 0.574 | 5.1302 | 1.8480 | 0.1281 | ACCELERATING | 1.4690 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 13932 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HPE | 45.90 | 0.383 | 5.0842 | 6.1124 | 0.2699 | DECELERATING | 1.4041 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1546416 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CBLL | 28.62 | 0.265 | 5.0129 | 1.6564 | 0.0459 | ACCELERATING | 1.4623 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2734 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CXT | 52.21 | 0.131 | 5.0112 | 4.8310 | 0.0727 | ACCELERATING | 3.7324 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1266 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BST | 41.78 | 0.366 | 4.9920 | 6.2465 | 0.2487 | DECELERATING | 0.9965 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 15960 | measured_from_nasdaq | 2026-11-23 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 2198
- focus roster size: 12
- wider universe size: 2186
- scored: 1784; unpriced: 414; published rows: 239
- Required count: 32 (of 239 published)
- Liquid count: 207
- NEAR MISS count: 203 (89 building, 83 fading)
- alert count: 14 (6 building, 8 fading)
- crossings: 14 published; **314 across all 1784 scored names**
- universe distribution: median 1.2586x, p90 2.5281x; 37.67% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **BHC** - 10.3728x now vs 0.6880x on the prior session (recomputed_same_feed), close 8.24 - RVOL building 0.7956x -> 10.3728x, accumulation
- **CBLL** - 5.0129x now vs 1.4623x on the prior session (recomputed_same_feed), close 28.62 - RVOL building 1.6564x -> 5.0129x, accumulation
- **RVI** - 5.1302x now vs 1.4690x on the prior session (recomputed_same_feed), close 18.75 - RVOL building 1.8480x -> 5.1302x, accumulation
- **AEHR** - 5.6590x now vs 1.4892x on the prior session (recomputed_same_feed), close 47.80 - RVOL building 2.7859x -> 5.6590x, accumulation
- **IVR** - 1.5935x now vs 1.0878x on the prior session (recomputed_same_feed), close 5.45 - RVOL building 1.1156x -> 1.5935x, accumulation
- **NUAI** - 1.5346x now vs 1.2330x on the prior session (recomputed_same_feed), close 4.32 - RVOL building 1.3348x -> 1.5346x, accumulation
- **UPB** - 8.9850x now vs 0.8237x on the prior session (recomputed_same_feed), close 1.87 - RVOL fading 9.1886x -> 8.9850x, distribution
- **PANW** - 1.8742x now vs 1.3947x on the prior session (recomputed_same_feed), close 354.84 - RVOL fading 2.2461x -> 1.8742x, distribution
- **HPE** - 5.0842x now vs 1.4041x on the prior session (recomputed_same_feed), close 45.90 - RVOL fading 6.1124x -> 5.0842x, distribution
- **NTSK** - 3.0694x now vs 1.4586x on the prior session (recomputed_same_feed), close 25.27 - RVOL fading 4.1899x -> 3.0694x, distribution
- **BST** - 4.9920x now vs 0.9965x on the prior session (recomputed_same_feed), close 41.78 - RVOL fading 6.2465x -> 4.9920x, distribution
- **SCCO** - 5.1342x now vs 1.1529x on the prior session (recomputed_same_feed), close 141.90 - RVOL fading 7.7428x -> 5.1342x, distribution
- **OBIO** - 5.9513x now vs 0.8522x on the prior session (recomputed_same_feed), close 6.92 - RVOL fading 8.7681x -> 5.9513x, distribution
- **ZS** - 24.4035x now vs 1.0671x on the prior session (recomputed_same_feed), close 230.66 - RVOL fading 31.4153x -> 24.4035x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 89 building against 83 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| HRI | 1.3724 | 3.5571 | 0.0466 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HR | 1.4991 | 0.6236 | 0.4370 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FTS | 1.4870 | 1.2776 | 0.5266 | ACCELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IDCC | 1.3463 | 2.3864 | 0.5070 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BJ | 1.4290 | 13.9585 | 0.5928 | ACCELERATING | 0.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRNS | 1.4380 | 3.2916 | 0.6128 | ACCELERATING | 4.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDY | 1.3307 | 1.2330 | 0.5119 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FPI | 1.3195 | 1.8459 | 0.5326 | ACCELERATING | 4.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KNSL | 1.4240 | 3.5448 | 0.6858 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UPBD | 1.3652 | 1.0618 | 0.6761 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TS | 1.4471 | 0.4541 | 0.7781 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INVH | 1.3890 | 1.5207 | 0.7643 | ACCELERATING | 0.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MATW | 1.3996 | 2.4112 | 0.8248 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| S | 1.4510 | 0.9091 | 0.8792 | ACCELERATING | 8.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BRX | 1.3322 | 1.4461 | 0.7995 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GSL | 1.3525 | 0.9219 | 0.8494 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRBG | 1.3358 | 0.8609 | 0.8455 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HOS | 1.3776 | 1.1293 | 0.9108 | ACCELERATING | 7.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AWK | 1.3401 | 1.8678 | 0.8746 | ACCELERATING | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MRNA | 1.2959 | 0.9069 | 0.8421 | ACCELERATING | 13.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LASR | 1.3913 | 1.2111 | 0.9618 | ACCELERATING | 10.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FLO | 1.4427 | 0.7196 | 1.0515 | ACCELERATING | 5.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CVS | 1.4228 | 1.2883 | 1.0359 | ACCELERATING | 19.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGI | 1.4347 | 1.1023 | 1.0498 | ACCELERATING | 17.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRU | 1.2901 | 0.8128 | 0.9114 | ACCELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTFC | 1.4562 | n/a | 1.1013 | ACCELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BSM | 1.3947 | 5.5569 | 1.0433 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SAIL | 1.4983 | 1.1604 | 1.1477 | ACCELERATING | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMCO | 1.4740 | 3.1209 | 1.1257 | ACCELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SNN | 1.3001 | 0.3640 | 0.9642 | ACCELERATING | 7.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TOYO | 1.3078 | 1.1265 | 0.9754 | ACCELERATING | 21.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GAP | 1.4571 | 9.4364 | 1.1303 | ACCELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GFI | 1.4872 | 2.2298 | 1.1623 | ACCELERATING | 19.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COCO | 1.3719 | 2.1831 | 1.0536 | ACCELERATING | 2.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GRAB | 1.4850 | 2.4563 | 1.1669 | ACCELERATING | 17.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMX | 1.3214 | 1.6877 | 1.0077 | ACCELERATING | 3.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVA | 1.3601 | 1.7527 | 1.0482 | ACCELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMC | 1.4044 | 1.4063 | 1.0938 | ACCELERATING | 10.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SHW | 1.2871 | 2.1494 | 0.9819 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NKTR | 1.3637 | 3.6816 | 1.0756 | ACCELERATING | 9.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| B | 1.3632 | 1.4690 | 1.0752 | ACCELERATING | 25.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CECO | 1.3499 | 0.4262 | 1.0731 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AOD | 1.3725 | 1.0638 | 1.1000 | ACCELERATING | 6.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HBNC | 1.4987 | 2.3595 | 1.2279 | ACCELERATING | 2.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| L | 1.3218 | 3.9729 | 1.0549 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FSLY | 1.3896 | 1.4798 | 1.1324 | ACCELERATING | 14.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COHU | 1.3943 | 0.9624 | 1.1382 | ACCELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TIGR | 1.4615 | 3.0466 | 1.2078 | ACCELERATING | 25.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NN | 1.3214 | 1.5482 | 1.0769 | ACCELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMQ | 1.2816 | 1.5410 | 1.0520 | ACCELERATING | 7.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CHAT | 1.2802 | 1.0558 | 1.0508 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GNRC | 1.4863 | 1.7524 | 1.2579 | ACCELERATING | 9.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INDI | 1.4588 | 1.1915 | 1.2314 | ACCELERATING | 16.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRV | 1.4082 | 1.7743 | 1.1858 | ACCELERATING | 4.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NAMS | 1.3362 | 0.6013 | 1.1218 | ACCELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZWS | 1.3049 | 5.7508 | 1.0960 | ACCELERATING | 4.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HBAN | 1.3376 | 1.5679 | 1.1306 | ACCELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GLUE | 1.4092 | 1.9871 | 1.2092 | ACCELERATING | 3.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OTIS | 1.4140 | 1.2836 | 1.2141 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SEZL | 1.4102 | 2.7216 | 1.2103 | ACCELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETN | 1.2922 | 1.6081 | 1.1058 | ACCELERATING | 9.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MA | 1.4413 | 2.3728 | 1.2569 | ACCELERATING | 5.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MFG | 1.4851 | 1.1668 | 1.3114 | ACCELERATING | 1.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UPWK | 1.2909 | 3.5807 | 1.1193 | ACCELERATING | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SBSW | 1.4970 | 3.9171 | 1.3406 | ACCELERATING | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NAVN | 1.3487 | 1.7614 | 1.1963 | ACCELERATING | 4.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NEXT | 1.4360 | 2.5581 | 1.2895 | ACCELERATING | 13.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAG | 1.2768 | 1.5743 | 1.1324 | ACCELERATING | 4.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ONDS | 1.3011 | 1.2065 | 1.1612 | ACCELERATING | 28.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PYPL | 1.3754 | 4.0900 | 1.2399 | ACCELERATING | 11.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NXPI | 1.3437 | 5.0904 | 1.2108 | ACCELERATING | 10.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FIS | 1.3432 | 1.4561 | 1.2151 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVMI | 1.4122 | 0.9090 | 1.2952 | ACCELERATING | 25.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CNP | 1.3013 | 1.3025 | 1.1941 | ACCELERATING | 4.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MXL | 1.4380 | 1.1272 | 1.3314 | ACCELERATING | 21.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLDP | 1.4841 | 0.7728 | 1.3796 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TKR | 1.4455 | 1.0479 | 1.3550 | ACCELERATING | 11.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GBCI | 1.3673 | 3.5022 | 1.2774 | ACCELERATING | 17.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WDAY | 1.3441 | 1.7871 | 1.2571 | ACCELERATING | 9.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INO | 1.3821 | 0.6077 | 1.2970 | ACCELERATING | 29.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SOUN | 1.3229 | 1.2866 | 1.2380 | ACCELERATING | 26.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FTK | 1.4912 | 0.8845 | 1.4065 | ACCELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVPT | 1.4124 | 2.3209 | 1.3354 | ACCELERATING | 16.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RYAM | 1.3421 | 2.6728 | 1.2661 | ACCELERATING | 9.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SNEX | 1.3209 | 2.6799 | 1.2450 | ACCELERATING | 6.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SWKS | 1.3984 | 1.1350 | 1.3265 | ACCELERATING | 4.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UBS | 1.4895 | 1.2765 | 1.4195 | ACCELERATING | 9.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JKS | 1.4570 | 0.8912 | 1.3896 | ACCELERATING | 25.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VZ | 1.4758 | 1.8567 | 1.4130 | ACCELERATING | 9.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| P | 1.4373 | 1.5324 | 1.3878 | STABLE | 16.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NXG | 1.4387 | 1.7967 | 1.3965 | STABLE | 6.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WMT | 1.3630 | 1.6807 | 1.3221 | STABLE | 12.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PCG | 1.3113 | 2.1532 | 1.2707 | STABLE | 10.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMPX | 1.2813 | 1.0054 | 1.2409 | STABLE | 20.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UL | 1.4700 | 1.6775 | 1.4319 | STABLE | 16.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GGN | 1.3052 | 1.6631 | 1.2732 | STABLE | 10.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KKR | 1.4930 | 5.4792 | 1.4624 | STABLE | 40.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TENX | 1.3320 | 10.1513 | 1.3028 | STABLE | 20.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PDD | 1.3096 | 3.5272 | 1.2811 | STABLE | 11.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QUBT | 1.3554 | 1.8044 | 1.3269 | STABLE | 23.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MEC | 1.3250 | 0.7380 | 1.2986 | STABLE | 4.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GILD | 1.4896 | 2.3412 | 1.4639 | STABLE | 10.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GM | 1.2939 | 1.6285 | 1.2687 | STABLE | 9.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NCLH | 1.3182 | 0.7125 | 1.3075 | STABLE | 11.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MKC | 1.3714 | 2.4814 | 1.3657 | STABLE | 2.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BIDU | 1.2871 | 3.0117 | 1.2857 | STABLE | 28.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SCHW | 1.3260 | 1.6966 | 1.3251 | STABLE | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CINF | 1.3062 | 3.1522 | 1.3053 | STABLE | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MET | 1.3997 | 1.6990 | 1.4015 | STABLE | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FDMT | 1.3449 | 2.0538 | 1.3471 | STABLE | 3.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SBUX | 1.4889 | 1.9504 | 1.4974 | STABLE | 11.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TDY | 1.2950 | 1.5943 | 1.3126 | STABLE | 2.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLK | 1.4298 | 2.0406 | 1.4488 | STABLE | 9.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGLT | 1.4501 | 0.7297 | 1.4698 | STABLE | 22.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RVII | 1.4331 | 2.8455 | 1.4534 | STABLE | 24.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RIG | 1.3339 | 1.4527 | 1.3714 | STABLE | 16.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JD | 1.3436 | 1.0497 | 1.3842 | STABLE | 18.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NRGV | 1.3619 | 0.8302 | 1.4047 | STABLE | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMDX | 1.3544 | 2.3483 | 1.3996 | STABLE | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FNV | 1.3262 | 1.4881 | 1.3720 | STABLE | 16.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ROP | 1.3573 | 2.3958 | 1.4120 | DECELERATING | 8.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EXG | 1.4041 | 2.2210 | 1.4611 | DECELERATING | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DFTX | 1.3917 | 3.0307 | 1.4492 | DECELERATING | 14.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XP | 1.4144 | 0.9804 | 1.4760 | DECELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BKSY | 1.3968 | 1.9029 | 1.4689 | DECELERATING | 17.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AESI | 1.3031 | 0.3864 | 1.3775 | DECELERATING | 4.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZCSH | 1.3219 | 1.4041 | 1.3973 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WMB | 1.3083 | 1.5143 | 1.3966 | DECELERATING | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVBH | 1.3149 | 1.5262 | 1.4077 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EQX | 1.4611 | 1.0604 | 1.5539 | DECELERATING | 12.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMD | 1.4297 | 1.3457 | 1.5229 | DECELERATING | 28.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SPCX | 1.4728 | 1.4814 | 1.5722 | DECELERATING | 27.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDDT | 1.4617 | 1.5856 | 1.5731 | DECELERATING | 21.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VST | 1.4267 | 1.4284 | 1.5387 | DECELERATING | 21.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TXG | 1.3162 | 0.9090 | 1.4342 | DECELERATING | 9.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| T | 1.4099 | 1.8256 | 1.5288 | DECELERATING | 12.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CIEN | 1.3008 | 0.8375 | 1.4211 | DECELERATING | 17.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VCX | 1.4454 | 5.1999 | 1.5671 | DECELERATING | 25.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CRK | 1.4434 | 1.1635 | 1.5696 | DECELERATING | 17.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TLRY | 1.3452 | 1.3485 | 1.4732 | DECELERATING | 18.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APP | 1.4278 | 1.2160 | 1.5584 | DECELERATING | 21.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSUS | 1.4359 | 3.1139 | 1.5689 | DECELERATING | 3.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NTAP | 1.4267 | 2.1112 | 1.5673 | DECELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KHC | 1.3015 | 2.1030 | 1.4476 | DECELERATING | 26.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PIPR | 1.3028 | 3.7772 | 1.4491 | DECELERATING | 14.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BKKT | 1.3656 | 0.8287 | 1.5142 | DECELERATING | 31.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BETR | 1.4760 | 1.2036 | 1.6400 | DECELERATING | 0.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KD | 1.3701 | 0.5601 | 1.5421 | DECELERATING | 28.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PRLB | 1.3178 | n/a | 1.4902 | DECELERATING | 22.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ABCL | 1.3651 | 1.7127 | 1.5504 | DECELERATING | 25.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RLI | 1.4363 | 1.4467 | 1.6296 | DECELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AEM | 1.4269 | 1.7110 | 1.6233 | DECELERATING | 14.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JKHY | 1.3540 | 2.1832 | 1.5569 | DECELERATING | 16.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WTW | 1.3025 | 1.6347 | 1.5107 | DECELERATING | 13.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALM | 1.4274 | 1.9825 | 1.6380 | DECELERATING | 12.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CELH | 1.3137 | 1.0302 | 1.5244 | DECELERATING | 14.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BELFB | 1.3473 | n/a | 1.5605 | DECELERATING | 39.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BEN | 1.3093 | n/a | 1.5265 | DECELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| USAR | 1.4999 | 0.8802 | 1.7181 | DECELERATING | 27.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CSX | 1.3043 | 4.9936 | 1.5226 | DECELERATING | 7.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLM | 1.4091 | 2.1773 | 1.6307 | DECELERATING | 28.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TW | 1.4244 | 3.4035 | 1.6471 | DECELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BB | 1.4486 | 1.3484 | 1.6749 | DECELERATING | 27.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AAL | 1.3554 | 0.7406 | 1.6023 | DECELERATING | 23.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CGAU | 1.4889 | 3.0588 | 1.7404 | DECELERATING | 14.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FSLR | 1.4020 | 0.8439 | 1.6564 | DECELERATING | 13.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IRTC | 1.3736 | 0.7905 | 1.6333 | DECELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HLIT | 1.4737 | 2.2404 | 1.7373 | DECELERATING | 11.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ITW | 1.3345 | 2.0622 | 1.6018 | DECELERATING | 12.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ESLT | 1.4536 | n/a | 1.7426 | DECELERATING | 22.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OSK | 1.2859 | 1.4987 | 1.5835 | DECELERATING | 20.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ACHR | 1.4942 | 1.2013 | 1.7936 | DECELERATING | 21.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HOMB | 1.3064 | 3.1472 | 1.6134 | DECELERATING | 12.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSMR | 1.4073 | 1.3060 | 1.7147 | DECELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JBLU | 1.4846 | 0.5459 | 1.7929 | DECELERATING | 15.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASB | 1.4382 | 2.9463 | 1.7474 | DECELERATING | 15.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIRI | 1.3038 | 0.9725 | 1.6192 | DECELERATING | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NWCL | 1.3355 | 0.5685 | 1.6700 | DECELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NI | 1.4728 | 1.4971 | 1.8218 | DECELERATING | 27.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STX | 1.2790 | 1.3153 | 1.6479 | DECELERATING | 21.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BWXT | 1.3228 | 1.1507 | 1.6933 | DECELERATING | 15.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EMR | 1.3302 | 2.5837 | 1.7047 | DECELERATING | 2.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| QNT | 1.4694 | 0.8890 | 1.8545 | DECELERATING | 25.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RYTM | 1.3121 | 4.6768 | 1.7218 | DECELERATING | 9.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SFM | 1.3646 | 1.9280 | 1.7918 | DECELERATING | 28.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BCAX | 1.3968 | 1.4086 | 1.8429 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EVGO | 1.3593 | 1.6084 | 1.8110 | DECELERATING | 32.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CPNG | 1.4634 | 2.0311 | 1.9346 | DECELERATING | 6.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SVM | 1.3184 | 1.1946 | 1.8059 | DECELERATING | 20.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RSI | 1.3112 | 1.6670 | 1.8091 | DECELERATING | 28.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WGMI | 1.3716 | 1.6520 | 1.8743 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PSI | 1.2832 | 1.4668 | 1.7871 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KVYO | 1.3471 | 0.6904 | 1.9168 | DECELERATING | 34.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NEXA | 1.4254 | 0.8160 | 1.9960 | DECELERATING | 8.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WWD | 1.4540 | 0.5958 | 2.2508 | DECELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSP | 1.4763 | n/a | 2.3203 | DECELERATING | 11.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WAT | 1.4684 | 2.3953 | 2.3224 | DECELERATING | 2.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DISK | 1.3963 | 1.1184 | 2.2676 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSB | 1.4194 | n/a | 2.2999 | DECELERATING | 16.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAGN | 1.4883 | 2.5963 | 2.3700 | DECELERATING | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSYS | 1.3165 | 0.6366 | 2.2492 | DECELERATING | 29.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRLV | 1.4892 | 1.5740 | 2.5202 | DECELERATING | 20.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GAU | 1.3143 | 1.5102 | 2.6832 | DECELERATING | 7.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **12 entered**, **0 left**, **0 stayed**.

- entered: AMBA, DPC, INSM, IVR, NTSK, NUAI, OKTA, P, PANW, PURR, TU, VRDN
- left: none
- stayed: none

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 0 of 12 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 333.5s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1784 of 2198 candidates
- unpriced names: 414 of 2198 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 239 published rows - measured_from_nasdaq 224, not_subtracted 15; 15 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **414 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
