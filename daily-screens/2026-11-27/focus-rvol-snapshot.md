---
date: 2026-11-27
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-27
focus_dir_date: 2026-11-25
screen_data_date: 2026-11-24
lag_sessions: 2
universe_source: focus_plus_wider
universe_size: 2345
wider_universe_source: focus+master+17
wider_universe_size: 2333
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
upstream: /workspace/daily-screens/2026-11-25/focus.md
names_unpriced: 514
published_rows: 108
selectivity: broad_tape
universe_median_rvol: 0.6779
universe_p90_rvol: 1.5716
universe_share_ge_1_5_pct: 10.87
universe_crossings: 133
---

# Focus RVOL snapshot - 2026-11-27 09:45 ET (cron #07)

## TL;DR
- **1831 of 2345** names scored (12 focus + 2333 wider union); **108 rows published** (the focus roster, the top 25 of the wider union, and every name in the near-miss band).
- **Required: 25 of 108 published** (83 Liquid); **74 near misses**; **12 alerts** (provable crossings).
- **The tape today: `broad_tape`.** **10.87% of the 1831 scored names cleared the 1.5x bar** (median 0.6779x, p90 1.5716x) and there were **133 crossings** across the whole scored set - the bar is a DESCRIPTION of a broad move, not a selection of it. 
- **Alerts: SUPX (ACCELERATING), SBS (ACCELERATING), AGLT (ACCELERATING), INTR (ACCELERATING), ERO (ACCELERATING), RDY (DECELERATING), KNTK (DECELERATING), GGAL (DECELERATING), STNE (DECELERATING), XP (DECELERATING), NATL (DECELERATING), EWZS (DECELERATING).** **5 are still building and 7 are already fading** between the earlier snapshot and the fire; the near-miss watch list is **42 building vs 27 fading**.
- **Every prior reading is RECOMPUTED on the same feed and the SAME TradingView denominator as today's reading**, so both sides of each crossing are one scale. The TV denominator is a rolling average and moves between fetches, so a published prior value is a cross-check, never the baseline.
- **The focus roster alone is a momentum screen on the previous session's data and structurally misses the day's movers**; the wider union is what carries them.

## Universe
- focus roster: 12 names (10 priced below; **IRON and NNNN could not be priced** - no regular-session bars in the fetched window, so they carry no RVOL reading rather than a zero)
- wider union: 2333 names from focus+master+17
- scored: 1831; unscored: 514; published rows: 108
- **the scored universe's distribution** (the context for every count below): median 0.6779x, p75 1.0258x, p90 1.5716x, p99 4.398x; 14.91% at or above 1.275x, **10.87% at or above 1.5x**, 5.73% at or above 2x, 2.29% at or above 3x - selectivity: **broad_tape**

## Focus table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CELC | 73.64 | 0.0398 | 1.3249 | 0.4627 | 0.0086 | ACCELERATING | 0.9818 | recomputed_same_feed | n/a | n/a | Liquid | NEAR MISS | 100 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ANF | 183.22 | 0.122 | 1.2272 | 0.7942 | 0.0469 | ACCELERATING | 1.0091 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 15855 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KSS | 27.31 | 0.0574 | 0.7018 | 0.8273 | 0.0367 | DECELERATING | 2.5093 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 14687 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STOK | 36.14 | 0.0408 | 0.5156 | 0.3234 | 0.0210 | ACCELERATING | 1.0081 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 952 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| COGT | 35.88 | 0.0341 | 0.3887 | 0.4644 | 0.0235 | DECELERATING | 1.0775 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 6626 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NAMS | 24.66 | 0.0124 | 0.3773 | 0.3751 | 0.0071 | STABLE | 1.3715 | recomputed_same_feed | 1.3146 | -4.15 | Liquid | WATCH | 1577 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AMTM | 25.25 | 0.0249 | 0.3478 | 0.5615 | 0.0129 | DECELERATING | 0.7790 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 2450 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DKS | 159.59 | 0.0303 | 0.3378 | 0.2658 | 0.0162 | ACCELERATING | 0.8918 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 8898 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INSM | 170.64 | 0.0709 | 0.2950 | 0.2563 | 0.0451 | STABLE | 1.5302 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 105369 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MMED | 18.89 | 0.0068 | 0.1468 | 0.0488 | 0.0012 | ACCELERATING | 0.5191 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

## Wider universe

The top 25 of the wider union by `rvol_now`.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VERA | 34.03 | 0.728 | 25.0486 | 35.1687 | 0.5574 | DECELERATING | 1.6379 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 62251 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BBD | 2.83 | 0.829 | 16.6222 | 26.1891 | 0.6497 | DECELERATING | 2.0990 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 21446392 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| INTR | 4.63 | 0.932 | 14.6144 | 14.3773 | 0.5307 | ACCELERATING | 0.7277 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 1936970 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FRT | 114.32 | 0.326 | 14.4810 | 26.2244 | 0.3152 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AFYA | 11.78 | 0.972 | 13.5271 | 36.1450 | 0.8297 | DECELERATING | n/a | unavailable | n/a | n/a | RVOL Required | WATCH | 59068 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EWZS | 12.14 | 1.59 | 12.4072 | 40.0264 | 0.9391 | DECELERATING | 0.1934 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XP | 16.71 | 0.731 | 11.1614 | 15.7226 | 0.5135 | DECELERATING | 1.0881 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 2182998 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SNDK | 78.93 | 0.214 | 9.3676 | 10.4596 | 0.1577 | DECELERATING | 8.3804 | recomputed_same_feed | 8.5548 | 2.08 | RVOL Required | WATCH | 10398041 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SBS | 5.45 | 0.602 | 8.6960 | 7.2744 | 0.2782 | ACCELERATING | 1.4379 | recomputed_same_feed | 1.4886 | 4.12 | RVOL Required | ALERT | 533383 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NATL | 49.04 | 0.362 | 8.1784 | 16.6930 | 0.2811 | DECELERATING | 0.3590 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ECHO | 87.78 | 0.422 | 7.7575 | 17.0973 | 0.4093 | DECELERATING | 1.5073 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 1509214 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GGAL | 28.39 | 0.326 | 6.9481 | 7.6804 | 0.2016 | DECELERATING | 1.2183 | recomputed_same_feed | 1.3223 | 8.53 | RVOL Required | ALERT | 72552 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OBX | 14.45 | 0.245 | 6.7857 | 11.9472 | 0.2339 | DECELERATING | 2.6729 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 100 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| STNE | 8.14 | 0.32 | 6.0652 | 7.9404 | 0.2271 | DECELERATING | 0.4832 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 508974 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| SUPX | 2.44 | 0.219 | 4.9943 | 2.7581 | 0.0630 | ACCELERATING | 1.4815 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 6361 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LZM | 3.70 | 0.269 | 4.9849 | 7.4691 | 0.2450 | DECELERATING | 3.6055 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KNTK | 58.76 | 0.2 | 4.9241 | 5.5821 | 0.1248 | DECELERATING | 0.2589 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 15012 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DFTX | 33.69 | 0.216 | 4.4911 | 6.9199 | 0.1423 | DECELERATING | 2.8450 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 7335 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IQMX | 7.26 | 0.328 | 4.3980 | 5.6574 | 0.2436 | DECELERATING | 2.1250 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 35945 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PBR | 16.90 | 0.364 | 4.3436 | 4.6964 | 0.2397 | DECELERATING | 1.8559 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 2538628 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RDY | 15.07 | 0.118 | 4.1832 | 4.5656 | 0.0737 | DECELERATING | 0.4290 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 3946 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| XNTK | 291.73 | 0.239 | 4.1649 | 5.4054 | 0.1616 | DECELERATING | 2.1862 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ERO | 20.88 | 0.285 | 4.1210 | 3.9266 | 0.1668 | ACCELERATING | 1.2963 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 168953 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AGLT | 6.70 | 0.474 | 4.0935 | 3.0010 | 0.2084 | ACCELERATING | 0.6160 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 121839 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TGTX | 64.66 | 0.269 | 4.0159 | 2.9977 | 0.0773 | ACCELERATING | 2.8614 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 9320 | measured_from_nasdaq | 2026-11-27 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts
- universe size: 2345
- focus roster size: 12
- wider universe size: 2333
- scored: 1831; unpriced: 514; published rows: 108
- Required count: 25 (of 108 published)
- Liquid count: 83
- NEAR MISS count: 74 (42 building, 27 fading)
- alert count: 12 (5 building, 7 fading)
- crossings: 12 published; **133 across all 1831 scored names**
- universe distribution: median 0.6779x, p90 1.5716x; 10.87% of the scored universe at or above 1.5x (selectivity: broad_tape)

## Alerts

A name is listed only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides on the same feed and the same denominator. Ordered by the trend delta (the earlier cross-check snapshot -> the fire), so the names still BUILDING come first.

- **SUPX** - 4.9943x now vs 1.4815x on the prior session (recomputed_same_feed), close 2.44 - RVOL building 2.7581x -> 4.9943x, accumulation
- **SBS** - 8.6960x now vs 1.4379x on the prior session (recomputed_same_feed), close 5.45 - RVOL building 7.2744x -> 8.6960x, accumulation
- **AGLT** - 4.0935x now vs 0.6160x on the prior session (recomputed_same_feed), close 6.70 - RVOL building 3.0010x -> 4.0935x, accumulation
- **INTR** - 14.6144x now vs 0.7277x on the prior session (recomputed_same_feed), close 4.63 - RVOL building 14.3773x -> 14.6144x, accumulation
- **ERO** - 4.1210x now vs 1.2963x on the prior session (recomputed_same_feed), close 20.88 - RVOL building 3.9266x -> 4.1210x, accumulation
- **RDY** - 4.1832x now vs 0.4290x on the prior session (recomputed_same_feed), close 15.07 - RVOL fading 4.5656x -> 4.1832x, distribution
- **KNTK** - 4.9241x now vs 0.2589x on the prior session (recomputed_same_feed), close 58.76 - RVOL fading 5.5821x -> 4.9241x, distribution
- **GGAL** - 6.9481x now vs 1.2183x on the prior session (recomputed_same_feed), close 28.39 - RVOL fading 7.6804x -> 6.9481x, distribution
- **STNE** - 6.0652x now vs 0.4832x on the prior session (recomputed_same_feed), close 8.14 - RVOL fading 7.9404x -> 6.0652x, distribution
- **XP** - 11.1614x now vs 1.0881x on the prior session (recomputed_same_feed), close 16.71 - RVOL fading 15.7226x -> 11.1614x, distribution
- **NATL** - 8.1784x now vs 0.3590x on the prior session (recomputed_same_feed), close 49.04 - RVOL fading 16.6930x -> 8.1784x, distribution
- **EWZS** - 12.4072x now vs 0.1934x on the prior session (recomputed_same_feed), close 12.14 - RVOL fading 40.0264x -> 12.4072x, distribution

## Near misses

Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. **Ordered by the trend delta, so the names that are BUILDING come first** - today's split is 42 building against 27 fading, and the fading ones were a watch list in name only.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | pm_share_pct | what would turn it into an alert |
|---|---|---|---|---|---|---|
| HURN | 1.3407 | 0.6828 | 0.0198 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BCAX | 1.4668 | 0.8248 | 0.3222 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TMDX | 1.4473 | 0.7505 | 0.4097 | ACCELERATING | 3.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FMTM | 1.3180 | 0.6660 | 0.2916 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AVBH | 1.2991 | 1.5396 | 0.2916 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GLUE | 1.4841 | 0.6858 | 0.5439 | ACCELERATING | 1.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SWX | 1.2763 | n/a | 0.4025 | ACCELERATING | 1.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CELC | 1.3249 | 0.9818 | 0.4627 | ACCELERATING | 0.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WLDN | 1.2849 | 0.9772 | 0.4510 | ACCELERATING | 6.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TFX | 1.4385 | 3.2197 | 0.6587 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GNTX | 1.3119 | 1.5703 | 0.5434 | ACCELERATING | 1.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FDTX | 1.4274 | 1.5529 | 0.6948 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JAKK | 1.3272 | 1.6096 | 0.6053 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CGGR | 1.4575 | 1.0296 | 0.7412 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KRMN | 1.3492 | 1.2774 | 0.6686 | ACCELERATING | 7.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FULT | 1.4252 | 0.9773 | 0.8108 | ACCELERATING | 5.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DE | 1.2820 | 9.0856 | 0.7111 | ACCELERATING | 1.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BLBD | 1.3696 | 3.8651 | 0.8013 | ACCELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| FOUR | 1.4252 | 0.7610 | 0.8647 | ACCELERATING | 3.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HPQ | 1.4611 | 7.4001 | 0.9300 | ACCELERATING | 5.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VYX | 1.3739 | 0.8371 | 0.9131 | ACCELERATING | 0.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IP | 1.2976 | 1.1904 | 0.8716 | ACCELERATING | 5.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IPGP | 1.3629 | 1.4713 | 0.9596 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| USDE | 1.3106 | 0.5132 | 0.9105 | ACCELERATING | 20.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SNEX | 1.4321 | 2.5443 | 1.0332 | ACCELERATING | 6.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PAR | 1.3864 | 0.8376 | 1.0277 | ACCELERATING | 2.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PLUG | 1.3660 | 1.3328 | 1.0081 | ACCELERATING | 12.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SN | 1.4528 | 2.3936 | 1.1084 | ACCELERATING | 5.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NEXT | 1.4164 | 0.9836 | 1.0798 | ACCELERATING | 8.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AIRJ | 1.3413 | 0.8326 | 1.0161 | ACCELERATING | 15.6 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALKS | 1.4465 | 0.8854 | 1.1689 | ACCELERATING | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BZ | 1.4806 | 2.0356 | 1.2465 | ACCELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| EMBC | 1.4589 | 2.7941 | 1.2328 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMB | 1.3079 | 1.3181 | 1.1206 | ACCELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GDXY | 1.4542 | 1.4123 | 1.2740 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GOLD | 1.3027 | 1.5751 | 1.1500 | ACCELERATING | 9.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RES | 1.3394 | 0.9265 | 1.2007 | ACCELERATING | 7.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RELY | 1.4568 | 1.3369 | 1.3395 | ACCELERATING | 8.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| HRI | 1.2995 | 2.3293 | 1.2042 | ACCELERATING | 13.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MUX | 1.3827 | 0.8469 | 1.2895 | ACCELERATING | 14.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OGG | 1.2961 | 1.1376 | 1.2087 | ACCELERATING | 11.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GDX | 1.3954 | 0.9579 | 1.3189 | ACCELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VPG | 1.4500 | 2.9368 | 1.4397 | STABLE | 10.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IBN | 1.4656 | 0.7047 | 1.4654 | STABLE | 1.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RBLX | 1.3248 | 0.9750 | 1.3351 | STABLE | 7.0 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASTS | 1.3835 | 1.0087 | 1.4076 | STABLE | 24.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PAAS | 1.3733 | 1.6830 | 1.4169 | STABLE | 18.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WPM | 1.4792 | 1.1968 | 1.5427 | DECELERATING | 14.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SHMD | 1.3145 | 3.7187 | 1.3998 | DECELERATING | 39.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLV | 1.4559 | 1.3682 | 1.5816 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VNET | 1.3019 | 0.6609 | 1.4325 | DECELERATING | 13.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GSK | 1.2827 | 1.5015 | 1.5032 | DECELERATING | 32.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| JD | 1.3071 | 1.2237 | 1.5364 | DECELERATING | 17.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MFG | 1.3208 | 1.2776 | 1.6157 | DECELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APP | 1.3917 | 0.8821 | 1.6917 | DECELERATING | 12.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| UEC | 1.3762 | 1.4469 | 1.7028 | DECELERATING | 25.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NDSN | 1.3440 | 1.1862 | 1.6836 | DECELERATING | 29.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| METC | 1.4942 | 1.4485 | 1.8428 | DECELERATING | 8.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GDYN | 1.4071 | 0.6435 | 1.7857 | DECELERATING | 11.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VNDA | 1.3507 | 2.7824 | 1.7502 | DECELERATING | 2.4 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BG | 1.4627 | 3.5222 | 1.8795 | DECELERATING | 26.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AEE | 1.2975 | n/a | 1.7461 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RBRK | 1.4664 | 1.1417 | 1.9657 | DECELERATING | 6.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LAES | 1.4696 | 1.1044 | 1.9890 | DECELERATING | 35.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WRD | 1.3083 | 1.1474 | 1.8865 | DECELERATING | 27.8 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OVV | 1.4301 | 0.6608 | 2.0437 | DECELERATING | 0.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSAT | 1.4219 | 0.9752 | 2.0588 | DECELERATING | 14.3 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GLXY | 1.2965 | 0.8346 | 1.9456 | DECELERATING | 26.1 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LEGN | 1.3709 | 1.0556 | 2.0751 | DECELERATING | 7.7 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TRLV | 1.2751 | 1.3211 | 2.0270 | DECELERATING | 1.5 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KRG | 1.2950 | n/a | 2.1286 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| MOMO | 1.4282 | 2.6364 | 2.6935 | DECELERATING | 3.9 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KMX | 1.3589 | 1.5156 | 2.7732 | DECELERATING | 43.2 | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SETM | 1.3657 | 2.6086 | 4.2991 | DECELERATING | n/a | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

## Universe change

The focus roster against the previous session's published roster: **9 entered**, **179 left**, **1 stayed**.

- entered: AMTM, ANF, CELC, COGT, DKS, INSM, KSS, MMED, STOK
- left: AAPL, ADBE, ADEA, AIPO, ALAB, ALDX, ALT, AM, AMBA, AMZN, APLD, APLE, ASST, AU, AVTR, AWI, AXTI, BDC, BEAM, BELFB, BG, BIIB, BILI, BITQ, BL, BLDP, BLZE, BMRN, BMY, BOOT, BTDR, BXSL, C, CAVA, CBRE, CCJ, CDE, CDNA, CHTR, CMBT, CMCO, CNH, COIN, COMP, COR, COUR, CRWV, CTAS, CTOS, CTRI, DDOG, DE, DELL, DFDV, DHI, DOC, DOCU, DUOL, EBS, ECG, EEFT, EMA, ENTX, ET, ETN, ETON, EVR, EXK, FA, FCEL, FFBC, FFIN, FIVE, FLTW, GBDC, GGAL, GILD, GKOS, GOOG, GOOGL, GSAT, GTLB, HBAN, HDB, HPE, HPQ, IAM, IBIO, INSW, ITUB, JANX, KN, KOD, KRMN, KYMR, LEN, LIND, LITE, LMND, LQDA, LU, MAIR, MAR, MARA, MAS, MCHP, MDLZ, MFG, MKSI, MLI, MORT, MRVI, MSTY, MT, MTRX, MXL, NBIS, NBIX, NI, NNE, NTNX, NTRA, NTST, NVDA, NVII, NVTS, ORCL, ORCS, OSCR, OUST, PAGP, PALL, PL, PNNT, PRCH, PTON, PYPD, RDW, RELY, REYN, RIOT, RKLB, RNA, RUN, RXRX, SBS, SEDG, SERV, SHOE, SIGA, SION, SITM, SLVR, SMHX, SMTC, SNDK, SOUN, STEP, STRL, TECK, TLRY, TRLV, TSCO, U, UAMY, UEC, UMC, URBN, VFC, VIAV, VISN, VLTO, VSXY, WCC, WDAY, WLTH, XERS, YUMC, ZYME
- stayed: NAMS

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of 10 roster names were in that file, so a published baseline would be `n/a` on nearly every row and the alert tier would be silently dead again.

## Method
- scored by `tools/focus_rvol_score.py` in 451.2s
- window volume: Yahoo 5m bars, 09:30/09:35/09:40 stamps, the last COMPLETED bar
- prior-10 same-window baseline: the same Yahoo series
- prior-10 full-day volume: Yahoo 1d bars (median ratio 1.0000 vs Nasdaq consolidated, max deviation 0.32%)
- denominator: TV `average_volume_10d_calc`, ONE pull used for BOTH sides of every crossing
- the previous session's reading is recomputed on that same denominator; the published value is carried as a cross-check with its drift
- **one vintage per artifact**: the whole run is one process, so every published number comes from the same bytes. The pre-market pass fetches the same window again with includePrePost=true, and the session volume in THAT response is compared with the bulk pass's - a drift over 2% publishes the share as `n/a` rather than mixing vintages
- pre-market: `pm_vol` is MEASURED for the published rows (the bars before 09:30 on the includePrePost response) and is not subtracted from the session volume - the session bars exclude pre-market by construction

## Source health
- TradingView scanner (the denominator): one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing
- Yahoo chart API (session volume, close, baselines): healthy; the engine scored 1831 of 2345 candidates
- unpriced names: 514 of 2345 candidates had no usable session window (`no_session_bars`); they are reported as unpriced, never as a zero
- pre-market share: 108 published rows - measured_from_nasdaq 88, not_subtracted 20; 20 row(s) carried NO measurable pre-market volume (Yahoo's pre-open bars carry volume 0 and Nasdaq's pre-session counter had no row for them), so their `pm_vol_source` reads `not_subtracted` and their `pm_share_pct` is `n/a` rather than a wrong number

## Degradation / caveats
- **514 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (the focus roster, the sweep's master list and cron #17's mover boards). A name that was in none of them cannot appear here.
- **The wider table shows the TOP 25, not every name above the bar.** On a broad tape the counts above give the full picture; the table is the screen, the counts are the context.
- **`rvol_tod_normalised` is a MORNING metric** - how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod`).
- **`rvol_intraday_live` is reference only** - mechanically tiny at 09:45, never used for bucketing.
- **`rvol_trend` is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`); the session-over-session delta is carried as `rvol_vs_prev_session`.
- **The TV denominator is a rolling average** and moves ~2% every 15 minutes, so a name sitting within ~2% of the bar can flip on the denominator alone.
- **The pre-market share is measured only on the fire's OWN day.** Nasdaq's pre-session counter is the source (Yahoo's extended-hours bars carry volume 0 - measured 2026-11-13, on the live session and on history), and a REPLAY cannot measure it at all: the endpoint serves TODAY's pre-market, which is a different session. On a replay the rows read `pm_vol_source: not_subtracted` and the share is `n/a` rather than a wrong number.
- **`lag_sessions` is a WEEKDAY count** between the sweep's own `Screen data_date:` and this fire - a venue holiday inside the gap would add one, so it is an upper bound.
