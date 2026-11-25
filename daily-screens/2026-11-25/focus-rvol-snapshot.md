---
date: 2026-11-25
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-25
focus_dir_date: 2026-11-24
screen_data_date: 2026-11-23
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 2094
wider_universe_source: focus+master+17
wider_universe_size: 2082
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
upstream: /workspace/daily-screens/2026-11-24/focus.md
names_unpriced: 396
published_rows: 180
selectivity: broad_tape
universe_median_rvol: 0.9465
universe_p90_rvol: 1.8789
universe_share_ge_1_5_pct: 20.08
universe_crossings: 238
---

# Focus RVOL snapshot - 2026-11-25 09:45 ET (cron #07)

## TL;DR
- **1698 of 2094** names scored (12 focus + 2082 wider union); **180 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 28 of 180 published** (152 Liquid); **145 near misses**; **19 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **20.08% of the 1698 scored names cleared the 1.5x bar** (median 0.9465x, p90 1.8789x) and there were **238 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: AWI (ACCELERATING), PAGP (ACCELERATING), GSAT (ACCELERATING), CNH (ACCELERATING), ADEA (ACCELERATING), NTNX (ACCELERATING), ETON (ACCELERATING), AMBA (ACCELERATING), BG (ACCELERATING), WCC (ACCELERATING), WDAY (ACCELERATING), HPQ (ACCELERATING), BTDR (STABLE), ALAB (STABLE), ECG (DECELERATING), FA (DECELERATING), URBN (DECELERATING), PYPD (DECELERATING), STEP (DECELERATING).** **12 are still building and 5 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **79 building vs 45 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names
- wider union: 2082 names from focus+master+17
- scored: 1698; unscored: 396; published rows: 180
- **the scored universe's distribution** (the context for every count below): median 0.9465x, p75 1.3401x, p90 1.8789x, p99 3.9164x; 28.62% at or above 1.275x, **20.08% at or above 1.5x**, 8.54% at or above 2x, 2.77% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 275.43 | 0.588 | 4.3568 | 5.1573 | 0.4169 | DECELERATING | 1.8455 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 2944470 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SMTC | 78.97 | 0.207 | 2.4685 | 1.4392 | 0.0705 | ACCELERATING | 3.9014 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 57209 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ALAB | 169.77 | 0.184 | 1.6773 | 1.6744 | 0.1227 | STABLE | 1.1262 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 281721 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| APLD | 10.89 | 0.192 | 1.3752 | 1.4278 | 0.1220 | DECELERATING | 0.8683 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 941136 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SITM | 341.75 | 0.104 | 1.2813 | 1.4250 | 0.0688 | DECELERATING | 2.0773 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 8281 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MXL | 37.40 | 0.135 | 1.1318 | 1.1084 | 0.0935 | STABLE | 0.8442 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 59524 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KYMR | 165.12 | 0.142 | 0.9740 | 0.3319 | 0.0332 | ACCELERATING | 3.5841 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 4853 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LITE | 435.55 | 0.151 | 0.9063 | 0.8783 | 0.0945 | STABLE | 0.9441 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 183789 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AXTI | 28.38 | 0.176 | 0.8793 | 1.0141 | 0.1288 | DECELERATING | 0.9251 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 725820 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CRWV | 37.56 | 0.167 | 0.8608 | 0.8370 | 0.1100 | STABLE | 0.7240 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 4419173 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NBIS | 77.15 | 0.191 | 0.8608 | 0.8100 | 0.1262 | ACCELERATING | 0.5844 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 2946506 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NVDA | 141.65 | 0.132 | 0.6751 | 0.7119 | 0.0966 | STABLE | 0.7722 | recomputed_same_feed | 0.7786 | 0.91 | Liquid | WATCH | 20302935 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMBA | 34.36 | 1.74 | 33.1633 | 32.5247 | 1.1588 | ACCELERATING | 0.7025 | recomputed_same_feed | 1.2831 | 82.66 | RVOL Required | ALERT | 1514749 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| URBN | 77.02 | 0.566 | 17.9925 | 20.1364 | 0.3491 | DECELERATING | 1.3645 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 110249 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NTNX | 43.04 | 0.452 | 16.1379 | 14.8401 | 0.2384 | ACCELERATING | 1.3115 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 72329 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AWI | 177.30 | 0.305 | 13.1098 | 2.8119 | 0.0304 | ACCELERATING | 0.6856 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CTRI | 20.94 | 0.289 | 11.4353 | 9.0601 | 0.1068 | ACCELERATING | 4.1053 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1063 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DE | 619.83 | 0.381 | 9.1388 | 11.2486 | 0.2717 | DECELERATING | 3.1446 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 157774 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HPQ | 30.31 | 0.378 | 8.5712 | 8.5020 | 0.1678 | ACCELERATING | 1.2352 | recomputed_same_feed | 1.3118 | 15.25 | RVOL Required | ALERT | 508419 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNDK | 69.45 | 0.195 | 8.5548 | 9.0015 | 0.1357 | DECELERATING | 7.0034 | recomputed_same_feed | 6.7880 | -3.08 | RVOL Required | WATCH | 9123003 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PYPD | 4.37 | 0.647 | 7.3215 | 9.5577 | 0.4502 | DECELERATING | 0.6024 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 174767 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WDAY | 174.64 | 0.223 | 6.6871 | 6.5509 | 0.1352 | ACCELERATING | 0.8951 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 77694 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PAGP | 25.37 | 0.163 | 6.1887 | 3.4212 | 0.0448 | ACCELERATING | 1.3260 | recomputed_same_feed | 1.2920 | -2.57 | RVOL Required | ALERT | 1096 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RNA | 7.45 | 0.249 | 5.7321 | 7.7542 | 0.2260 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 2436 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CNH | 11.37 | 0.174 | 5.4740 | 3.1766 | 0.0387 | ACCELERATING | 1.2288 | recomputed_same_feed | 1.2905 | 9.27 | RVOL Required | ALERT | 24355 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STEP | 44.29 | 0.134 | 5.4597 | 9.3514 | 0.1289 | DECELERATING | 0.8208 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 103818 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ENTX | 3.22 | 0.579 | 5.0256 | 35.4077 | 0.5090 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 410 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BTDR | 2.74 | 0.371 | 4.9552 | 4.9519 | 0.2243 | STABLE | 1.0558 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 787326 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GSAT | 85.64 | 0.211 | 3.9164 | 1.6054 | 0.0400 | ACCELERATING | 1.2974 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 3524 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ETON | 60.90 | 0.221 | 3.9161 | 2.8618 | 0.1092 | ACCELERATING | 0.9721 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 5386 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BDC | 96.21 | 0.109 | 3.8652 | 2.3468 | 0.0432 | ACCELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 453 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WCC | 276.76 | 0.129 | 3.6726 | 3.2143 | 0.0700 | ACCELERATING | 1.1888 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 9546 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IBIO | 1.11 | 0.191 | 3.6482 | 6.1190 | 0.1713 | DECELERATING | 2.3115 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 62988 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ADEA | 12.79 | 0.138 | 3.6383 | 2.0577 | 0.0593 | ACCELERATING | 0.8882 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 7678 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BG | 87.71 | 0.0838 | 3.6183 | 3.1334 | 0.0414 | ACCELERATING | 0.8044 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2250 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ECG | 73.49 | 0.163 | 3.5930 | 4.6297 | 0.1396 | DECELERATING | 1.1057 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 60946 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FA | 20.89 | 0.266 | 3.5668 | 5.1910 | 0.2639 | DECELERATING | 0.4605 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 590434 | measured_from_nasdaq | 2026-11-25 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 2094
- focus roster size: 12
- wider universe size: 2082
- scored: 1698; unpriced: 396; published rows: 180
- Required count: 28 (of 180 published)
- Liquid count: 152
- NEAR MISS count: 145 (79 building, 45 fading)
- alert count: 19 (12 building, 5 fading)
- crossings: 19 published; **238 across all 1698 scored names**
- universe distribution: median 0.9465x, p90 1.8789x; 20.08% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **AWI** - 13.1098x now vs 0.6856x on the prior session (recomputed_same_feed), close 177.30 - RVOL building 2.8119x -> 13.1098x, accumulation
- **PAGP** - 6.1887x now vs 1.3260x on the prior session (recomputed_same_feed), close 25.37 - RVOL building 3.4212x -> 6.1887x, accumulation
- **GSAT** - 3.9164x now vs 1.2974x on the prior session (recomputed_same_feed), close 85.64 - RVOL building 1.6054x -> 3.9164x, accumulation
- **CNH** - 5.4740x now vs 1.2288x on the prior session (recomputed_same_feed), close 11.37 - RVOL building 3.1766x -> 5.4740x, accumulation
- **ADEA** - 3.6383x now vs 0.8882x on the prior session (recomputed_same_feed), close 12.79 - RVOL building 2.0577x -> 3.6383x, accumulation
- **NTNX** - 16.1379x now vs 1.3115x on the prior session (recomputed_same_feed), close 43.04 - RVOL building 14.8401x -> 16.1379x, accumulation
- **ETON** - 3.9161x now vs 0.9721x on the prior session (recomputed_same_feed), close 60.90 - RVOL building 2.8618x -> 3.9161x, accumulation
- **AMBA** - 33.1633x now vs 0.7025x on the prior session (recomputed_same_feed), close 34.36 - RVOL building 32.5247x -> 33.1633x, accumulation
- **BG** - 3.6183x now vs 0.8044x on the prior session (recomputed_same_feed), close 87.71 - RVOL building 3.1334x -> 3.6183x, accumulation
- **WCC** - 3.6726x now vs 1.1888x on the prior session (recomputed_same_feed), close 276.76 - RVOL building 3.2143x -> 3.6726x, accumulation
- **WDAY** - 6.6871x now vs 0.8951x on the prior session (recomputed_same_feed), close 174.64 - RVOL building 6.5509x -> 6.6871x, accumulation
- **HPQ** - 8.5712x now vs 1.2352x on the prior session (recomputed_same_feed), close 30.31 - RVOL building 8.5020x -> 8.5712x, accumulation
- **BTDR** - 4.9552x now vs 1.0558x on the prior session (recomputed_same_feed), close 2.74 - RVOL flat 4.9519x -> 4.9552x
- **ALAB** - 1.6773x now vs 1.1262x on the prior session (recomputed_same_feed), close 169.77 - RVOL flat 1.6744x -> 1.6773x
- **ECG** - 3.5930x now vs 1.1057x on the prior session (recomputed_same_feed), close 73.49 - RVOL fading 4.6297x -> 3.5930x, distribution
- **FA** - 3.5668x now vs 0.4605x on the prior session (recomputed_same_feed), close 20.89 - RVOL fading 5.1910x -> 3.5668x, distribution
- **URBN** - 17.9925x now vs 1.3645x on the prior session (recomputed_same_feed), close 77.02 - RVOL fading 20.1364x -> 17.9925x, distribution
- **PYPD** - 7.3215x now vs 0.6024x on the prior session (recomputed_same_feed), close 4.37 - RVOL fading 9.5577x -> 7.3215x, distribution
- **STEP** - 5.4597x now vs 0.8208x on the prior session (recomputed_same_feed), close 44.29 - RVOL fading 9.3514x -> 5.4597x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - on 2026-11-12 that split was 79 building against 45 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| CMCO | 1.4215 | n/a | 0.0699 | ACCELERATING | 3.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BITQ | 1.4605 | 1.9148 | 0.1135 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MTRX | 1.3762 | n/a | 0.1404 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LIND | 1.3024 | n/a | 0.1011 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VLTO | 1.2800 | 1.0966 | 0.1533 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| REYN | 1.3627 | 1.1036 | 0.3711 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CAVA | 1.3619 | 0.8856 | 0.3742 | ACCELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FLTW | 1.4843 | 0.7509 | 0.5080 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EMA | 1.4562 | 1.4231 | 0.6159 | ACCELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COUR | 1.4136 | 0.9574 | 0.5883 | ACCELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PALL | 1.3325 | 1.9801 | 0.5802 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APLE | 1.3250 | 0.5853 | 0.6474 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VSXY | 1.3218 | 0.7083 | 0.6742 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CTAS | 1.2760 | 1.3892 | 0.6342 | ACCELERATING | 0.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NTST | 1.3771 | n/a | 0.7526 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EXK | 1.4495 | 0.6724 | 0.8295 | ACCELERATING | 7.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BXSL | 1.4088 | n/a | 0.8318 | ACCELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FIVE | 1.3677 | 1.5092 | 0.7935 | ACCELERATING | 0.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PTON | 1.2977 | 1.3543 | 0.7260 | ACCELERATING | 2.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVTR | 1.3114 | 2.5670 | 0.7707 | ACCELERATING | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SHOE | 1.3531 | 31.7656 | 0.8379 | ACCELERATING | 1.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LQDA | 1.2933 | 0.6883 | 0.7933 | ACCELERATING | 5.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KOD | 1.2975 | 2.9465 | 0.7980 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VIAV | 1.3098 | 0.4181 | 0.8108 | ACCELERATING | 10.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SMHX | 1.3401 | 0.5742 | 0.8419 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WLTH | 1.3658 | 0.4238 | 0.8780 | ACCELERATING | 3.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XERS | 1.2883 | 0.6896 | 0.8604 | ACCELERATING | 4.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DUOL | 1.3786 | 0.3284 | 0.9523 | ACCELERATING | 4.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GKOS | 1.4009 | 1.2390 | 0.9885 | ACCELERATING | 5.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MLI | 1.4996 | 1.1991 | 1.1107 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NI | 1.3523 | 0.6025 | 0.9783 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BOOT | 1.4455 | 0.8391 | 1.0798 | ACCELERATING | 6.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NBIX | 1.3559 | n/a | 0.9918 | ACCELERATING | 10.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UEC | 1.4536 | 0.6198 | 1.0967 | ACCELERATING | 11.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FFBC | 1.3039 | 0.4711 | 0.9558 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAR | 1.3511 | 1.2214 | 1.0031 | ACCELERATING | 2.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SION | 1.3246 | 1.8298 | 0.9798 | ACCELERATING | 8.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COR | 1.3307 | 0.6614 | 1.0308 | ACCELERATING | 3.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IAM | 1.3911 | 0.5631 | 1.0914 | ACCELERATING | 20.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORCL | 1.3460 | 0.6535 | 1.0484 | ACCELERATING | 22.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLZE | 1.3083 | 0.6430 | 1.0232 | ACCELERATING | 4.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DDOG | 1.3732 | 0.5775 | 1.1003 | ACCELERATING | 16.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ADBE | 1.2911 | 1.2663 | 1.0306 | ACCELERATING | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GGAL | 1.3223 | 2.3200 | 1.0672 | ACCELERATING | 9.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FCEL | 1.2977 | 1.3295 | 1.0457 | ACCELERATING | 17.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SOUN | 1.3711 | 1.0400 | 1.1251 | ACCELERATING | 16.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MFG | 1.3046 | 2.5066 | 1.0782 | ACCELERATING | 1.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ETN | 1.3492 | 0.6874 | 1.1414 | ACCELERATING | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HBAN | 1.3088 | 1.0633 | 1.1013 | ACCELERATING | 0.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LU | 1.4017 | n/a | 1.1963 | ACCELERATING | 16.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MSTY | 1.2838 | 0.6919 | 1.0840 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AMZN | 1.4386 | 0.6839 | 1.2482 | ACCELERATING | 21.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BILI | 1.4655 | 5.6982 | 1.2878 | ACCELERATING | 13.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AU | 1.4208 | 0.9210 | 1.2482 | ACCELERATING | 26.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PL | 1.3332 | 0.9476 | 1.1674 | ACCELERATING | 14.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SERV | 1.3622 | 0.9526 | 1.2038 | ACCELERATING | 11.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MRVI | 1.3339 | 1.0943 | 1.1812 | ACCELERATING | 9.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVTS | 1.3727 | 1.0332 | 1.2206 | ACCELERATING | 19.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GILD | 1.2868 | 1.5800 | 1.1369 | ACCELERATING | 4.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RIOT | 1.4897 | 0.5956 | 1.3432 | ACCELERATING | 21.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| C | 1.2845 | 0.6643 | 1.1425 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HDB | 1.3184 | 0.5632 | 1.1805 | ACCELERATING | 4.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALT | 1.3425 | 0.9103 | 1.2048 | ACCELERATING | 18.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NNE | 1.4890 | 1.1287 | 1.3554 | ACCELERATING | 23.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ORCS | 1.2796 | 4.2860 | 1.1468 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UAMY | 1.3486 | 0.9615 | 1.2190 | ACCELERATING | 19.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COIN | 1.3106 | 0.6761 | 1.1829 | ACCELERATING | 24.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DFDV | 1.4140 | 0.7893 | 1.2959 | ACCELERATING | 16.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DOC | 1.3702 | 0.9205 | 1.2558 | ACCELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RKLB | 1.3523 | 0.8109 | 1.2414 | ACCELERATING | 25.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRLV | 1.3159 | 0.6073 | 1.2119 | ACCELERATING | 7.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VFC | 1.3684 | 1.0781 | 1.2645 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GOOG | 1.3962 | 0.7622 | 1.3053 | ACCELERATING | 26.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DOCU | 1.4017 | 0.6427 | 1.3174 | ACCELERATING | 8.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BMRN | 1.4280 | 3.5156 | 1.3495 | ACCELERATING | 1.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLDP | 1.3299 | 1.9086 | 1.2689 | ACCELERATING | 16.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLVR | 1.3118 | 1.1259 | 1.2525 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NVII | 1.3691 | 0.9988 | 1.3135 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MDLZ | 1.3092 | 0.8250 | 1.2550 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EVR | 1.3044 | 1.8235 | 1.2640 | STABLE | 20.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SBS | 1.4886 | 4.2514 | 1.4502 | STABLE | 11.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAIR | 1.3182 | n/a | 1.2930 | STABLE | 3.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DHI | 1.4132 | 1.0803 | 1.3913 | STABLE | 4.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GOOGL | 1.4008 | 0.8858 | 1.3789 | STABLE | 24.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALDX | 1.2925 | 8.6707 | 1.2713 | STABLE | 19.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CMBT | 1.2863 | 2.1690 | 1.2734 | STABLE | 18.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RELY | 1.4021 | 1.0300 | 1.3892 | STABLE | 8.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RDW | 1.2946 | 0.8822 | 1.2873 | STABLE | 20.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RUN | 1.4351 | 1.5158 | 1.4281 | STABLE | 12.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OSCR | 1.3376 | 0.4290 | 1.3334 | STABLE | 7.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| U | 1.2793 | 1.0814 | 1.2786 | STABLE | 11.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LMND | 1.4872 | 0.6622 | 1.4900 | STABLE | 7.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EBS | 1.2838 | 1.2678 | 1.2873 | STABLE | 3.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| INSW | 1.3369 | 0.7591 | 1.3494 | STABLE | 26.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HPE | 1.4211 | 4.2127 | 1.4528 | STABLE | 14.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GTLB | 1.4641 | 1.1665 | 1.4986 | STABLE | 22.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SEDG | 1.4406 | 1.5899 | 1.4775 | STABLE | 11.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MCHP | 1.3919 | 1.2757 | 1.4320 | STABLE | 17.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KN | 1.4504 | 0.9270 | 1.4941 | STABLE | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OUST | 1.3629 | 1.0586 | 1.4096 | STABLE | 17.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APLD | 1.3752 | 0.8683 | 1.4278 | DECELERATING | 15.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| COMP | 1.3800 | 0.7651 | 1.4413 | DECELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MT | 1.4356 | 1.9928 | 1.4987 | DECELERATING | 24.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PRCH | 1.4674 | 0.8046 | 1.5317 | DECELERATING | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASST | 1.3274 | 0.7864 | 1.3989 | DECELERATING | 29.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CBRE | 1.3968 | 1.0633 | 1.4736 | DECELERATING | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AAPL | 1.4859 | 0.8459 | 1.5694 | DECELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JANX | 1.4216 | 0.5927 | 1.5089 | DECELERATING | 2.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GBDC | 1.4101 | 1.1026 | 1.5184 | DECELERATING | 4.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BELFB | 1.3708 | 1.2948 | 1.5030 | DECELERATING | 38.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MORT | 1.3232 | 0.9616 | 1.4613 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CDE | 1.4792 | 0.9006 | 1.6225 | DECELERATING | 4.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SITM | 1.2813 | 2.0773 | 1.4250 | DECELERATING | 12.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BEAM | 1.2780 | 0.9458 | 1.4239 | DECELERATING | 4.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ET | 1.3786 | 0.8794 | 1.5390 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RXRX | 1.2790 | 0.6939 | 1.4416 | DECELERATING | 14.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PNNT | 1.4770 | 3.9938 | 1.6518 | DECELERATING | 7.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UMC | 1.4070 | 1.5290 | 1.5859 | DECELERATING | 22.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TECK | 1.4355 | 2.5764 | 1.6186 | DECELERATING | 6.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ITUB | 1.4150 | 1.5186 | 1.6022 | DECELERATING | 10.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STRL | 1.3044 | 0.7651 | 1.4946 | DECELERATING | 25.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MKSI | 1.3828 | 1.1008 | 1.5815 | DECELERATING | 16.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BIIB | 1.4544 | 1.9378 | 1.6637 | DECELERATING | 2.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KRMN | 1.3038 | 1.0764 | 1.5275 | DECELERATING | 7.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VISN | 1.3026 | 0.6622 | 1.5387 | DECELERATING | 23.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AIPO | 1.4370 | 1.7750 | 1.6870 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TLRY | 1.2870 | 1.0450 | 1.5466 | DECELERATING | 22.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LEN | 1.3688 | 1.3429 | 1.6290 | DECELERATING | 12.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CDNA | 1.4751 | 0.7556 | 1.7425 | DECELERATING | 16.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CHTR | 1.3003 | 2.1006 | 1.5679 | DECELERATING | 2.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MAS | 1.3814 | 0.6499 | 1.6566 | DECELERATING | 0.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CCJ | 1.3541 | 0.8546 | 1.6330 | DECELERATING | 11.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MARA | 1.2976 | 1.0479 | 1.5928 | DECELERATING | 14.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AM | 1.3053 | 0.5089 | 1.6200 | DECELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| YUMC | 1.2924 | 1.0542 | 1.6279 | DECELERATING | 5.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FFIN | 1.3013 | 1.5772 | 1.6529 | DECELERATING | 0.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EEFT | 1.2777 | 0.8497 | 1.6365 | DECELERATING | 20.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BMY | 1.3041 | 1.4608 | 1.7305 | DECELERATING | 26.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ZYME | 1.3093 | 1.0331 | 1.8492 | DECELERATING | 37.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NTRA | 1.4620 | 0.8461 | 2.0183 | DECELERATING | 7.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SIGA | 1.4248 | 1.9502 | 2.0058 | DECELERATING | 2.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSCO | 1.2998 | 1.0685 | 1.9303 | DECELERATING | 6.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NAMS | 1.3146 | 0.7008 | 2.0004 | DECELERATING | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BL | 1.3632 | 0.6551 | 2.0836 | DECELERATING | 41.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CTOS | 1.3749 | n/a | 2.4110 | DECELERATING | 3.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **11 entered**, **182 left**, **1 stayed**.

- entered: ALAB, APLD, AXTI, CRWV, DELL, KYMR, LITE, MXL, NBIS, SITM, SMTC
- left: ABUS, ACMR, AGIO, AIG, ALKS, AMBA, ANF, AOA, AOD, ARTY, ARWR, ASHR, AVA, AVBH, AVR, BAM, BAX, BBD, BBIO, BELFB, BILI, BKNG, BMA, BST, BTX, BURL, CBLL, CGBL, CLDX, CMP, CMPS, CMRC, CNH, COGT, CRWD, CTA, DAPP, DBO, DFAE, DKNG, DTCR, DY, EGP, EH, ELMT, EMBC, ERIC, ESTA, ETHA, ETW, ETY, EWW, EXLS, FCEL, FICO, FIDU, FLNC, FTI, FUBO, FWDI, GDRX, GEMI, GNRC, GPIX, GPN, HBM, HIMX, HPQ, HTFL, HYLN, IBKR, ICUI, IFF, IMRX, INFY, INSM, INTC, INTR, INTU, INVH, IOT, IREN, IRON, IWF, JEPQ, JKS, KMB, KNX, KR, KVYO, KWEB, LBRX, LEU, LTBR, MAA, MCHP, MDT, MDY, MEDP, MLTX, MMYT, MSGK, MU, NCLD, NKE, NOK, NSLR, NTLA, NVAX, NWPX, OEF, ON, OUNZ, PAGP, PB, PBF, PENG, PHAT, PINS, PLAB, PLMR, PRAX, PRTA, PSEC, PSI, PTCT, PTEN, PTON, QNDX, QTOP, RCKT, RDVY, RDY, REXC, RMBS, ROCQ, ROP, RPD, RXST, SCHG, SIRI, SJM, SLDP, SMH, SNDK, SPMD, SPRX, SPTM, SPYM, SRPT, STE, STOK, SVCO, SVOL, SWIM, TARS, TEM, TEX, TGLS, TMO, TNGX, TPL, TRFK, UPB, UPS, VFF, VLRS, VMC, VOD, VOO, VOX, VOYG, VTWO, WCLD, WGMI, WH, XMMO, XPEV, XRAY, XSD, XYL, ZS
- stayed: NVDA

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of 12 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 366.8s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1698 of 2094 candidates
- unpriced names: 396 of 2094 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 180 published rows - measured_from_nasdaq 162, not_subtracted 18; 18 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **396 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
