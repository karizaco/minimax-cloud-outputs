---
date: 2026-11-13
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-13
focus_dir_date: 2026-11-12
screen_data_date: 2026-11-11
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1970
wider_universe_source: focus+master+17
wider_universe_size: 1958
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
upstream: /workspace/daily-screens/2026-11-12/focus.md
names_unpriced: 444
published_rows: 99
selectivity: broad_tape
universe_median_rvol: 0.5489
universe_p90_rvol: 1.4786
universe_share_ge_1_5_pct: 9.9
universe_crossings: 85
---

# Focus RVOL snapshot - 2026-11-13 09:45 ET (cron #07)

## TL;DR
- **1526 of 1970** names scored (12 focus + 1958 wider union); **99 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 25 of 99 published** (74 Liquid); **63 near misses**; **15 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **9.9% of the 1526 scored names cleared the 1.5x bar** (median 0.5489x, p90 1.4786x) and there were **85 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: APMD (ACCELERATING), GHRS (ACCELERATING), YSS (DECELERATING), CBRS (DECELERATING), MOD (DECELERATING), SPCE (DECELERATING), DGXX (DECELERATING), FLO (DECELERATING), CVLT (DECELERATING), BNY (DECELERATING), VIR (DECELERATING), NMAX (DECELERATING), XLAB (DECELERATING), STIM (DECELERATING), RZLT (DECELERATING).** **2 are still building and 13 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **31 building vs 27 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 1958 names from focus+master+17
- scored: 1526; unscored: 444; published rows: 99
- **the scored universe's distribution** (the context for every count below): median 0.5489x, p75 0.9207x, p90 1.4786x, p99 6.3299x; 14.02% at or above 1.275x, **9.9% at or above 1.5x**, 6.03% at or above 2x, 3.54% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NBIS | 114.45 | 0.305 | 1.4447 | 0.9263 | 0.1421 | ACCELERATING | 5.2166 | recomputed_same_feed | 5.6991 | 9.88 | Liquid | NEAR MISS | 1895852 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LGN | 36.00 | 0.0401 | 1.1222 | 1.3031 | 0.0255 | DECELERATING | 2.6282 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 5791 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CAPR | 9.77 | 0.0817 | 1.0052 | 0.7830 | 0.0382 | ACCELERATING | 2.4155 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 52410 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNDK | 888.22 | 0.163 | 0.9480 | 0.7609 | 0.0899 | ACCELERATING | 1.6480 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 777963 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FPS | 21.53 | 0.0804 | 0.8908 | 0.8034 | 0.0419 | ACCELERATING | 3.6998 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 114792 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CRWV | 52.57 | 0.148 | 0.8462 | 0.7049 | 0.0840 | ACCELERATING | 2.9947 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 3032333 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AAOI | 50.60 | 0.108 | 0.6933 | 0.6718 | 0.0734 | STABLE | 1.0054 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 716301 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AXTI | 41.77 | 0.111 | 0.6565 | 0.6073 | 0.0690 | STABLE | 1.5876 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 497802 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SHAZ | 23.40 | 0.0757 | 0.5777 | 0.2973 | 0.0276 | ACCELERATING | 1.2060 | recomputed_same_feed | 1.2905 | 7.06 | Liquid | WATCH | 27666 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GLXY | 14.54 | 0.0456 | 0.5339 | 0.6495 | 0.0316 | DECELERATING | 1.1684 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 44666 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AZTA | 44.22 | 0.0278 | 0.5066 | 0.3850 | 0.0113 | ACCELERATING | 1.9216 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 739 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AXGN | 55.64 | 0.0124 | 0.3155 | 0.0441 | 0.0010 | ACCELERATING | 4.7168 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 644 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RZLT | 4.15 | 1.17 | 40.3011 | 65.8013 | 0.8274 | DECELERATING | 0.8608 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 614924 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CADL | 6.03 | 1.35 | 32.3395 | 43.0392 | 0.9454 | DECELERATING | 1.5602 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 474787 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LFTO | 23.24 | 1.48 | 27.2693 | 34.0310 | 0.8090 | DECELERATING | 4.5432 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 251251 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XLAB | 2.39 | 0.544 | 21.0724 | 26.1764 | 0.4621 | DECELERATING | 0.0977 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2819361 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| APMD | 16.66 | 0.766 | 18.9398 | 0.1381 | 0.0018 | ACCELERATING | 0.3938 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NMAX | 9.14 | 1.15 | 18.4710 | 22.9152 | 0.8476 | DECELERATING | 0.5938 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 92830 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STIM | 1.29 | 2.22 | 18.2606 | 29.1259 | 1.9883 | DECELERATING | 1.0274 | recomputed_same_feed | 1.4666 | 42.75 | RVOL Required | ALERT | 7798477 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KDP | 36.70 | 0.733 | 12.3745 | 15.2118 | 0.4660 | DECELERATING | 2.8577 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 5774849 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| YSS | 5.35 | 0.486 | 11.2229 | 11.8854 | 0.3129 | DECELERATING | 1.1858 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 67373 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DGXX | 2.33 | 0.793 | 9.2932 | 10.5917 | 0.5237 | DECELERATING | 1.1908 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 970445 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| VIR | 10.16 | 1.27 | 9.2664 | 13.1040 | 0.8853 | DECELERATING | 0.4815 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1313676 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SPCE | 2.26 | 0.783 | 9.1221 | 10.3619 | 0.5212 | DECELERATING | 1.0062 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1167094 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CDNL | 6.64 | 0.956 | 8.3848 | 7.8814 | 0.4921 | ACCELERATING | 26.9460 | recomputed_same_feed | 66.5516 | 146.93 | RVOL Required | WATCH | 207691 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CBRS | 105.22 | 0.839 | 7.0685 | 8.0317 | 0.5591 | DECELERATING | 1.2563 | recomputed_same_feed | 1.3998 | 11.51 | RVOL Required | ALERT | 2363940 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PRE | 16.93 | 0.407 | 6.4052 | 2.9421 | 0.1103 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 318 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ADIG | 9.66 | 0.139 | 6.3299 | 5.0607 | 0.0499 | ACCELERATING | 4.0478 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 419 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MOD | 140.73 | 0.586 | 5.8379 | 7.0628 | 0.4255 | DECELERATING | 0.1226 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 644286 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HTFL | 52.74 | 0.274 | 5.6739 | 2.7897 | 0.0511 | ACCELERATING | 3.2613 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 4635 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BNY | 153.13 | 0.231 | 5.5990 | 8.9208 | 0.2197 | DECELERATING | 0.4668 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 175 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NEOV | 2.89 | 0.434 | 5.4578 | 6.0982 | 0.2790 | DECELERATING | 2.9263 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 129708 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CVLT | 153.98 | 0.224 | 5.3448 | 6.9228 | 0.1726 | DECELERATING | 0.6908 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 27538 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FLO | 5.94 | 0.261 | 4.8729 | 6.2226 | 0.1588 | DECELERATING | 0.5720 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 174445 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EZPW | 26.93 | 0.157 | 4.7476 | 6.5118 | 0.1329 | DECELERATING | 3.4300 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 6801 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GHRS | 18.36 | 0.121 | 4.6455 | 3.1401 | 0.0402 | ACCELERATING | 1.3378 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 708 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INBX | 84.01 | 0.206 | 4.5715 | 6.3279 | 0.1319 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 13021 | measured_from_nasdaq | 2026-11-13 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 1970
- focus roster size: 12
- wider universe size: 1958
- scored: 1526; unpriced: 444; published rows: 99
- Required count: 25 (of 99 published)
- Liquid count: 74
- NEAR MISS count: 63 (31 building, 27 fading)
- alert count: 15 (2 building, 13 fading)
- crossings: 15 published; **85 across all 1526 scored names**
- universe distribution: median 0.5489x, p90 1.4786x; 9.9% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **APMD** - 18.9398x now vs 0.3938x on the prior session (recomputed_same_feed), close 16.66 - RVOL building 0.1381x -> 18.9398x, accumulation
- **GHRS** - 4.6455x now vs 1.3378x on the prior session (recomputed_same_feed), close 18.36 - RVOL building 3.1401x -> 4.6455x, accumulation
- **YSS** - 11.2229x now vs 1.1858x on the prior session (recomputed_same_feed), close 5.35 - RVOL fading 11.8854x -> 11.2229x, distribution
- **CBRS** - 7.0685x now vs 1.2563x on the prior session (recomputed_same_feed), close 105.22 - RVOL fading 8.0317x -> 7.0685x, distribution
- **MOD** - 5.8379x now vs 0.1226x on the prior session (recomputed_same_feed), close 140.73 - RVOL fading 7.0628x -> 5.8379x, distribution
- **SPCE** - 9.1221x now vs 1.0062x on the prior session (recomputed_same_feed), close 2.26 - RVOL fading 10.3619x -> 9.1221x, distribution
- **DGXX** - 9.2932x now vs 1.1908x on the prior session (recomputed_same_feed), close 2.33 - RVOL fading 10.5917x -> 9.2932x, distribution
- **FLO** - 4.8729x now vs 0.5720x on the prior session (recomputed_same_feed), close 5.94 - RVOL fading 6.2226x -> 4.8729x, distribution
- **CVLT** - 5.3448x now vs 0.6908x on the prior session (recomputed_same_feed), close 153.98 - RVOL fading 6.9228x -> 5.3448x, distribution
- **BNY** - 5.5990x now vs 0.4668x on the prior session (recomputed_same_feed), close 153.13 - RVOL fading 8.9208x -> 5.5990x, distribution
- **VIR** - 9.2664x now vs 0.4815x on the prior session (recomputed_same_feed), close 10.16 - RVOL fading 13.1040x -> 9.2664x, distribution
- **NMAX** - 18.4710x now vs 0.5938x on the prior session (recomputed_same_feed), close 9.14 - RVOL fading 22.9152x -> 18.4710x, distribution
- **XLAB** - 21.0724x now vs 0.0977x on the prior session (recomputed_same_feed), close 2.39 - RVOL fading 26.1764x -> 21.0724x, distribution
- **STIM** - 18.2606x now vs 1.0274x on the prior session (recomputed_same_feed), close 1.29 - RVOL fading 29.1259x -> 18.2606x, distribution
- **RZLT** - 40.3011x now vs 0.8608x on the prior session (recomputed_same_feed), close 4.15 - RVOL fading 65.8013x -> 40.3011x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 31 building against 27 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| BJRI | 1.2960 | n/a | 0.0501 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OGE | 1.2873 | n/a | 0.0492 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DGII | 1.4339 | 7.9630 | 0.2793 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LAZR | 1.3152 | 1.7466 | 0.3066 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZBIO | 1.3129 | n/a | 0.4028 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RPRX | 1.3249 | 0.6395 | 0.5654 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PBLS | 1.3909 | 0.8356 | 0.6452 | ACCELERATING | 8.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MLYS | 1.3506 | 0.4811 | 0.7241 | ACCELERATING | 2.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STUB | 1.2757 | 0.7493 | 0.7241 | ACCELERATING | 2.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NBIS | 1.4447 | 5.2166 | 0.9263 | ACCELERATING | 17.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CSWC | 1.3092 | 0.5760 | 0.7960 | ACCELERATING | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SGMT | 1.3885 | 2.2475 | 0.9373 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AREC | 1.3622 | 1.3440 | 0.9376 | ACCELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XNCR | 1.4232 | 1.0066 | 1.0224 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CXW | 1.3901 | 0.3283 | 0.9903 | ACCELERATING | 5.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETHB | 1.3615 | 1.3418 | 1.0030 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STDN | 1.4233 | 1.6781 | 1.0765 | ACCELERATING | 12.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GSOL | 1.3552 | 1.0392 | 1.0276 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZETA | 1.4313 | 1.0877 | 1.1180 | ACCELERATING | 4.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NIQ | 1.3524 | 4.5638 | 1.0716 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RVMD | 1.4786 | 1.0769 | 1.2347 | ACCELERATING | 1.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CGEM | 1.3082 | 2.5541 | 1.0897 | ACCELERATING | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XE | 1.3899 | 2.5149 | 1.2003 | ACCELERATING | 9.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| S | 1.3257 | 1.6869 | 1.1589 | ACCELERATING | 3.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SMMT | 1.3503 | 1.1525 | 1.1898 | ACCELERATING | 11.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NKTR | 1.4240 | 1.3840 | 1.2856 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IONQ | 1.2828 | 0.8483 | 1.1640 | ACCELERATING | 22.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JBS | 1.4476 | 2.9984 | 1.3445 | ACCELERATING | 7.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BSOL | 1.3191 | 0.9260 | 1.2370 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVDA | 1.3142 | 5.3762 | 1.2473 | ACCELERATING | 25.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HOOD | 1.3499 | 0.9794 | 1.2954 | ACCELERATING | 20.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MBGL | 1.4445 | 7.9148 | 1.4040 | STABLE | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MSTW | 1.3413 | n/a | 1.3094 | STABLE | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BZ | 1.4251 | 10.4150 | 1.3942 | STABLE | 9.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIDU | 1.4498 | 1.6151 | 1.4340 | STABLE | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NLY | 1.4385 | 1.3338 | 1.4462 | STABLE | 5.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLDX | 1.3813 | 0.3985 | 1.4465 | DECELERATING | 11.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STRO | 1.3529 | 0.6254 | 1.4282 | DECELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MFA | 1.2930 | 0.8802 | 1.3726 | DECELERATING | 3.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KLAR | 1.2915 | 1.5459 | 1.3752 | DECELERATING | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| USAS | 1.4269 | 1.0772 | 1.5112 | DECELERATING | 22.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CTVA | 1.3403 | 5.4640 | 1.4643 | DECELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PANL | 1.3639 | 3.6280 | 1.4910 | DECELERATING | 6.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APLD | 1.4994 | 1.4032 | 1.6452 | DECELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COIN | 1.3538 | 0.9195 | 1.5106 | DECELERATING | 29.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVR | 1.4264 | 0.1747 | 1.6167 | DECELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PURR | 1.4443 | 0.7486 | 1.6437 | DECELERATING | 38.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIVR | 1.3261 | 1.0813 | 1.5400 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVAX | 1.2938 | 1.1966 | 1.5186 | DECELERATING | 17.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CHA | 1.4202 | 7.2862 | 1.6746 | DECELERATING | 16.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LCID | 1.4379 | 0.9903 | 1.7437 | DECELERATING | 5.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INIO | 1.3795 | 1.0099 | 1.6866 | DECELERATING | 5.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TGEN | 1.4120 | 2.2700 | 1.7382 | DECELERATING | 11.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMQ | 1.3738 | 1.9225 | 1.7055 | DECELERATING | 9.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RCEL | 1.4525 | 0.5784 | 1.8331 | DECELERATING | 2.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UAMY | 1.3997 | 1.0942 | 1.8045 | DECELERATING | 18.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAE | 1.2922 | 6.2554 | 1.6986 | DECELERATING | 4.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LOW | 1.4482 | 2.1424 | 1.8559 | DECELERATING | 6.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SSMR | 1.4591 | 0.9369 | 1.8989 | DECELERATING | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BCS | 1.4818 | 0.5380 | 1.9503 | DECELERATING | 40.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NB | 1.4296 | 1.3000 | 2.0727 | DECELERATING | 6.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BTC | 1.4626 | 2.0979 | 2.3242 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NAMS | 1.3632 | 0.5323 | 3.0281 | DECELERATING | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **10 entered**, **91 left**, **2 stayed**.

- entered: AAOI, AXGN, AXTI, AZTA, CAPR, CRWV, FPS, GLXY, LGN, SNDK
- left: AAON, ABCL, ABTC, AGNT, ALH, ANGX, APLD, ASPI, ASST, AVEX, BBOT, BEAM, BULL, BV, BW, CAE, CANG, CBRS, CCC, CDNL, CHTR, CLYM, CRML, CTVA, CWST, DC, DGII, DPC, EIKN, ELE, ENVX, ERAS, EROC, FAC, FATE, FIGR, FRMI, GDYN, GGG, GPCR, GRAL, GROY, HP, HROW, HWC, ICLR, ILMN, IREN, KEYS, KLIC, LEGN, LION, LQDA, LUMN, LUNR, MANE, MARA, MTRN, MTSI, NLY, NUAI, NVDA, ODD, OLMA, OMER, PEPG, PG, PLX, QNT, REPL, RGTI, RS, RXT, SKHY, SLDB, SO, STIM, STLA, TNGX, TSM, TTEK, TV, TWST, UBER, VRA, WAT, WDC, WGO, XPRO, YETI, ZETA
- stayed: NBIS, SHAZ

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 2 of 12 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 359.6s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1526 of 1970 candidates
- unpriced names: 444 of 1970 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero

## Degradation / caveats
- **444 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
