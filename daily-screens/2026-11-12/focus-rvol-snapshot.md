---
date: 2026-11-12
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-12
focus_dir_date: 2026-11-11
screen_data_date: 2026-11-10
lag_sessions: 1
universe_source: focus_plus_wider
universe_size: 1636
wider_universe_source: focus+master+17
wider_universe_size: 1624
wider_shown: 25
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars (interval=5m&range=1mo, regular session only) for the session volume, the 09:45 close and the prior-10 same-window baseline; Yahoo chart API 1d bars (range=3mo) for the prior-10 full-day volume; TradingView america scanner average_volume_10d_calc for the denominator (ONE pull, used for BOTH sides of every crossing); Cboe delayed-quote CDN for the independent earlier snapshot; cron #08 pre-market-gapper.csv cross-check
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean full-day volume divided by TV average_volume_10d_calc. The earlier reading is the same metric over the earlier snapshot's own clock window, against the prior-10 mean of that SAME window, on the same denominator.
metric_def: rvol_tod_normalised = (cumulative volume 09:30 -> the fire's bar, today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 sessions) x (mean full-day volume across those prior 10 sessions / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the fire bar / TV average_volume_10d_calc (reference only, never bucketed); rvol_prev = the same formula over the earlier cross-check snapshot's window against the prior-10 mean of that same window; rvol_at_09_38 = the raw cumulative ratio at that earlier snapshot
bucket_rule: rvol_now >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's reading of the same metric.
pm_source_status: not_subtracted
cross_check_source: cboe_delayed
status: ok
upstream: daily-screens/2026-11-11/focus.md
names_unpriced: 332
---

# Focus RVOL snapshot - 2026-11-12 09:45 ET (cron #07)

## TL;DR
- **25 of 93** published names sit at or above the **1.5x** bar (RVOL Required); **68** are below it. **18** of them are proven **crossings** (`prev_session_rvol` below 1.5x, `rvol_now` at or above it) and 56 are **near misses** (1.275x-1.5x).
- **Alerts (focus roster first):** HP 19.74x (ACCELERATING), NVDA 11.91x (ACCELERATING), FRMI 10.37x (ACCELERATING), LUNR 7.56x (DECELERATING), FIGR 8.53x (DECELERATING), BBOT 7.30x (DECELERATING), TWST 7.19x (DECELERATING), ENVX 7.98x (DECELERATING), CTVA 6.24x (DECELERATING), YETI 17.75x (DECELERATING), AVEX 10.96x (DECELERATING), EROC 5.44x (DECELERATING), TTEK 10.14x (DECELERATING), PLX 5.57x (DECELERATING), DGII 9.60x (DECELERATING), HWC 19.89x (DECELERATING), CCC 16.87x (DECELERATING), CDNL 66.55x (DECELERATING).
- **The focus roster itself is quiet.** Its best name is TNGX at **1.19x**, and the roster's **0 of 12** names clear the bar. The roster is a momentum screen built on the PREVIOUS session's data, so it structurally cannot hold a name whose move has not happened yet — the movers are in the wider union below.
- **Trend split on the names above the bar: 4 ACCELERATING, 21 DECELERATING** (the earlier cross-check snapshot -> the fire) — CDNL is the biggest fade (96.61x -> 66.55x), HP the biggest build (0.73x -> 19.74x).
- **The caveat that changes how this reads: the prior reading is RECOMPUTED, not taken from the previous session's published file.** The roster turns over almost completely between sweeps (1 of 12 names shared with the previous sweep), so a published prior would be `n/a` on nearly every row — which is what silently disarmed this routine's alert tier for five straight sessions. Every prior reading here is the same metric recomputed on the same feed and the same TradingView denominator, so both sides of every crossing are one scale.

## Universe
- **Focus roster: 12 names** from `daily-screens/2026-11-11/focus.md` - the 2026-11-11 18:30 ET sweep, the newest one on disk at the 09:45 fire (cron #09 runs after the open, so today's own sweep cannot exist yet).
- **Three dates, kept separate.** `fire_date` = **2026-11-12** (this fire's scheduled instant). `focus_dir_date` = **2026-11-11** (the folder the focus list was found in). `screen_data_date` = **2026-11-10**, read from the sweep's own header line `Screen data_date: 2026-11-10 (shibui T+1)` in `focus.md` - NOT inferred from the folder name.
- **`lag_sessions` = 1** trading session (2026-11-11, the only session between 2026-11-10 and 2026-11-12). The one-session lag is NORMAL: cron #09 fires on weekdays only, so a morning fire always reads the previous evening's sweep. The degradation would be a lag INSIDE `screen_data_date`, not this one.
- **Wider universe: 1624 names** unioned from what was already on disk for the previous session (2026-11-11): the focus roster's `focus.csv` (12), the sweep's `master.csv` (1,125) and cron #17's mover boards (1,381) - `focus+master+17`. The market was NOT re-scanned to build it.
- **Scored: 1304 of 1636** names carried a usable session window and a prior-10 baseline. **332 were unpriced** (`no_session_bars` - no regular-session bars in the fetched window). **93 names are published below**: the 12 focus-roster names, the top 25 of the wider union by `rvol_now`, and every name in the near-miss band.

## Focus table

The focus roster in full. Every number for a name is in that name's row.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TNGX | 24.6100 | 0.0439 | 1.1896 | 3.6501 | 0.0465 | DECELERATING | 2.1189 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ZETA | 37.2100 | 0.1050 | 1.0802 | 1.9505 | 0.0993 | DECELERATING | 2.6767 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MARA | 7.3600 | 0.1093 | 1.0311 | 1.5036 | 0.0887 | DECELERATING | 1.2335 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| QNT | 38.9900 | 0.0668 | 0.7695 | 1.1240 | 0.0585 | DECELERATING | 1.0445 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BW | 4.7250 | 0.0640 | 0.6977 | 1.1211 | 0.0655 | DECELERATING | 3.8371 | recomputed_same_feed | 4.0758 | 13.01 | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PEPG | 5.0900 | 0.2971 | 0.6815 | 0.5500 | 0.1926 | ACCELERATING | 0.5915 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LUMN | 4.3700 | 0.0271 | 0.4995 | 1.0926 | 0.0287 | DECELERATING | 0.7675 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AAON | 76.3925 | 0.0292 | 0.4961 | 0.8994 | 0.0294 | DECELERATING | 1.0473 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CHTR | 134.4850 | 0.0349 | 0.4722 | 0.8166 | 0.0396 | DECELERATING | 0.7823 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LQDA | 54.8100 | 0.0477 | 0.4567 | 1.2207 | 0.0541 | DECELERATING | 1.3876 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HROW | 29.1450 | 0.0372 | 0.3589 | 0.4310 | 0.0261 | DECELERATING | 0.8762 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| GDYN | 13.6620 | 0.0111 | 0.1693 | 0.4222 | 0.0152 | DECELERATING | 1.0671 | recomputed_same_feed | n/a | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |


## Wider universe

The top 25 of the wider union by `rvol_now`. This is where the day's movers live - the focus roster is a momentum screen on the previous session's data and cannot hold a name whose move has not happened yet. A focus-roster name is not repeated here.

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | prev_session_rvol_source | prev_session_rvol_published | denominator_drift_pct | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CDNL | 6.1725 | 2.5251 | 66.5516 | 96.6118 | 2.3791 | DECELERATING | 0.5310 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HWC | 64.7650 | 0.5471 | 19.8884 | 40.7767 | 0.6720 | DECELERATING | 0.6283 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| HP | 36.1900 | 0.4152 | 19.7425 | 0.7347 | 0.0082 | ACCELERATING | 0.8051 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| YETI | 39.7700 | 0.4515 | 17.7511 | 23.2477 | 0.3822 | DECELERATING | 1.2046 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CCC | 7.7050 | 0.5992 | 16.8698 | 39.4831 | 0.6243 | DECELERATING | 0.5479 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FAC | 3.9900 | 1.2179 | 15.8516 | 29.9954 | 1.2261 | DECELERATING | 3.8839 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NVDA | 159.9300 | 1.8638 | 11.9062 | 6.3465 | 0.6848 | ACCELERATING | 1.4809 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| AVEX | 14.6600 | 0.6169 | 10.9572 | 18.4804 | 0.5705 | DECELERATING | 1.0431 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MANE | 135.2188 | 0.7237 | 10.4065 | 29.9290 | 0.8930 | DECELERATING | 3.0340 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FRMI | 2.0750 | 0.8249 | 10.3748 | 8.7254 | 0.3953 | ACCELERATING | 1.3496 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TTEK | 39.9039 | 0.2760 | 10.1446 | 19.8999 | 0.2915 | DECELERATING | 0.8476 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DGII | 53.4800 | 0.2525 | 9.5971 | 21.8717 | 0.3174 | DECELERATING | 0.9565 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FIGR | 25.2300 | 0.4030 | 8.5325 | 10.6258 | 0.3005 | DECELERATING | 0.6558 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| ENVX | 1.9900 | 0.5885 | 7.9774 | 12.5087 | 0.4744 | DECELERATING | 0.7869 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LUNR | 13.7709 | 0.7745 | 7.5648 | 8.3977 | 0.5310 | DECELERATING | 1.2670 | recomputed_same_feed | 1.4150 | 11.67 | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| BBOT | 2.1200 | 0.3271 | 7.3023 | 10.5124 | 0.3402 | DECELERATING | 0.6769 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TWST | 102.7750 | 0.5220 | 7.1934 | 10.7166 | 0.4017 | DECELERATING | 1.3349 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CAE | 28.7500 | 0.3112 | 6.9113 | 19.7727 | 0.4188 | DECELERATING | 1.7354 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CTVA | 9.6550 | 0.2803 | 6.2398 | 11.4624 | 0.3045 | DECELERATING | 0.4677 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| DPC | 34.0700 | 0.1336 | 5.7258 | 10.5606 | 0.1296 | DECELERATING | 2.0041 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| NBIS | 128.8050 | 0.9562 | 5.6991 | 3.4700 | 0.3876 | ACCELERATING | 2.1267 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PLX | 3.0500 | 0.4166 | 5.5712 | 17.2942 | 0.4970 | DECELERATING | 1.4235 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| EROC | 7.9312 | 0.2731 | 5.4368 | 14.6252 | 0.3643 | DECELERATING | 0.7492 | recomputed_same_feed | n/a | n/a | RVOL Required | ALERT | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CANG | 1.5600 | 0.6719 | 5.3563 | 6.8984 | 0.6456 | DECELERATING | 6.1979 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FATE | 1.4400 | 0.2280 | 5.2743 | 11.2182 | 0.2675 | DECELERATING | 3.6336 | recomputed_same_feed | n/a | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-12 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |


### Counts
- universe size: **1636** candidates (focus 12 + wider 1624)
- scored: **1304**; unpriced: **332**; published rows: **93**
- Required count (`rvol_now` >= 1.5x): **25** published (194 of the 1304 scored names in the wider universe clear the bar; the published rows are the top of that set)
- Liquid count: **68**
- NEAR MISS count (1.275x <= `rvol_now` < 1.5x): **56** published (56 across the 1304 scored names)
- alert count: **18**
- crossings (prior < 1.5x <= now): **18** published (focus roster 0, wider union 18) - 133 across all 1304 scored names
- UNADJUSTED rows (session volume not pre-market-adjusted): **0**

## Alerts
A name is listed here only if the crossing is PROVEN: `prev_session_rvol` below 1.5x and `rvol_now` at or above it, both sides computed on the same feed and the same denominator. Ordered by trend delta, descending.

- **HP** — 19.74x now; the previous session read 0.81x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 36.1900 — RVOL building 0.73x -> 19.74x between the earlier snapshot and the fire — accumulation, the morning pace is running above its own norm.
- **NVDA** — 11.91x now; the previous session read 1.48x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 159.9300 — RVOL building 6.35x -> 11.91x between the earlier snapshot and the fire — accumulation, the morning pace is running above its own norm.
- **FRMI** — 10.37x now; the previous session read 1.35x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 2.0750 — RVOL building 8.73x -> 10.37x between the earlier snapshot and the fire — accumulation, the morning pace is running above its own norm.
- **LUNR** — 7.56x now; the previous session read 1.27x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 13.7709 — RVOL fading 8.40x -> 7.56x between the earlier snapshot and the fire — distribution, not accumulation.
- **FIGR** — 8.53x now; the previous session read 0.66x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 25.2300 — RVOL fading 10.63x -> 8.53x between the earlier snapshot and the fire — distribution, not accumulation.
- **BBOT** — 7.30x now; the previous session read 0.68x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 2.1200 — RVOL fading 10.51x -> 7.30x between the earlier snapshot and the fire — distribution, not accumulation.
- **TWST** — 7.19x now; the previous session read 1.33x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 102.7750 — RVOL fading 10.72x -> 7.19x between the earlier snapshot and the fire — distribution, not accumulation.
- **ENVX** — 7.98x now; the previous session read 0.79x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 1.9900 — RVOL fading 12.51x -> 7.98x between the earlier snapshot and the fire — distribution, not accumulation.
- **CTVA** — 6.24x now; the previous session read 0.47x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 9.6550 — RVOL fading 11.46x -> 6.24x between the earlier snapshot and the fire — distribution, not accumulation.
- **YETI** — 17.75x now; the previous session read 1.20x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 39.7700 — RVOL fading 23.25x -> 17.75x between the earlier snapshot and the fire — distribution, not accumulation.
- **AVEX** — 10.96x now; the previous session read 1.04x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 14.6600 — RVOL fading 18.48x -> 10.96x between the earlier snapshot and the fire — distribution, not accumulation.
- **EROC** — 5.44x now; the previous session read 0.75x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 7.9312 — RVOL fading 14.63x -> 5.44x between the earlier snapshot and the fire — distribution, not accumulation.
- **TTEK** — 10.14x now; the previous session read 0.85x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 39.9039 — RVOL fading 19.90x -> 10.14x between the earlier snapshot and the fire — distribution, not accumulation.
- **PLX** — 5.57x now; the previous session read 1.42x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 3.0500 — RVOL fading 17.29x -> 5.57x between the earlier snapshot and the fire — distribution, not accumulation.
- **DGII** — 9.60x now; the previous session read 0.96x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 53.4800 — RVOL fading 21.87x -> 9.60x between the earlier snapshot and the fire — distribution, not accumulation.
- **HWC** — 19.89x now; the previous session read 0.63x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 64.7650 — RVOL fading 40.78x -> 19.89x between the earlier snapshot and the fire — distribution, not accumulation.
- **CCC** — 16.87x now; the previous session read 0.55x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 7.7050 — RVOL fading 39.48x -> 16.87x between the earlier snapshot and the fire — distribution, not accumulation.
- **CDNL** — 66.55x now; the previous session read 0.53x (recomputed_same_feed), so it crossed UP through the 1.5x bar; close 6.1725 — RVOL fading 96.61x -> 66.55x between the earlier snapshot and the fire — distribution, not accumulation.

## Near misses
Names between 1.275x and 1.5x - the tradable edge. Each would become an ALERT if `rvol_now` reaches 1.5x while `prev_session_rvol` stays below 1.5x. Ordered by `rvol_now`, descending; the CSV carries every one of them.

| symbol | rvol_now | prev_session_rvol | rvol_prev | rvol_trend | what would turn it into an alert |
|---|---|---|---|---|---|
| GGG | 1.4991 | 4.6202 | 3.4900 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RXT | 1.4962 | 2.4132 | 3.1663 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STLA | 1.4923 | 1.0103 | 0.9743 | ACCELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LEGN | 1.4858 | 1.2583 | 3.9835 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| AGNT | 1.4820 | 1.7660 | 3.8800 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| PG | 1.4811 | 0.6194 | 2.5289 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ILMN | 1.4783 | 0.5604 | 3.0940 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CLYM | 1.4701 | 1.5257 | 2.6269 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| STIM | 1.4666 | 8.8082 | 3.0111 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WDC | 1.4520 | 1.1597 | 1.1970 | ACCELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TV | 1.4513 | n/a | 5.4304 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GROY | 1.4478 | 0.6198 | 1.9144 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KEYS | 1.4466 | 1.4474 | 1.9430 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SLDB | 1.4447 | 1.9477 | 4.0373 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| KLIC | 1.4426 | 0.8164 | 2.9655 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| RS | 1.4356 | 0.4524 | 2.0283 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| VRA | 1.4324 | 0.5455 | 2.2259 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| WGO | 1.4251 | n/a | 1.0330 | ACCELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ALH | 1.4209 | 2.5207 | 3.1722 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SO | 1.4109 | 0.2950 | 3.5727 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BV | 1.4101 | 5.4476 | 2.6831 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ANGX | 1.4100 | 5.1713 | 4.0058 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ABCL | 1.4094 | 1.1081 | 2.5617 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| GPCR | 1.4033 | 0.6586 | 2.5580 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| XPRO | 1.4006 | 0.4138 | 2.2322 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| CBRS | 1.3998 | 0.8263 | 2.2310 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| LION | 1.3947 | 0.7411 | 3.1273 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| IREN | 1.3938 | 1.3248 | 1.4217 | STABLE | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| TSM | 1.3932 | 1.3915 | 1.8821 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ERAS | 1.3931 | 4.9335 | 3.4422 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NUAI | 1.3924 | 0.9267 | 2.3324 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| DC | 1.3887 | 0.5506 | 2.7767 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| BULL | 1.3886 | 1.6969 | 1.3284 | ACCELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| SKHY | 1.3785 | 0.8637 | 0.8325 | ACCELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| NLY | 1.3784 | 0.8444 | 3.0051 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| APLD | 1.3776 | 0.9794 | 2.1745 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ABTC | 1.3749 | 1.2306 | 2.4051 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| OLMA | 1.3685 | 0.6404 | 3.6245 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| REPL | 1.3653 | 0.6968 | 3.2878 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |
| ASST | 1.3616 | 0.9769 | 1.7383 | DECELERATING | rvol_now reaching 1.5x with prev_session_rvol below 1.5x |

(16 further near misses are in the CSV.)

## Universe change
The focus roster against the previous sweep (`daily-screens/2026-11-10/focus.csv`): **11 entered**, **11 left**, **1 stayed**.

- entered: AAON, CHTR, GDYN, HROW, LQDA, LUMN, MARA, PEPG, QNT, TNGX, ZETA
- left: FRVO, IAM, IMVT, LUNR, MPWR, PL, PRAX, QXO, TLS, TTD, WRBY
- stayed: BW

This turnover is why the prior reading is recomputed rather than read from the previous session's published CSV: only 1 of today's 12 roster names were in yesterday's file, so a published baseline would be `n/a` on almost every row and the alert tier would be silently dead again.

## Method
- **The metric.** `rvol_tod_normalised` = (cumulative volume 09:30 -> the fire's bar today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 eligible sessions) x (mean full-day volume across those prior 10 sessions / TV `average_volume_10d_calc`). 1.0 is that name's own normal morning; 1.5 is 50% hotter than its own norm at the same hour.
- **The raw ratio is published but never bucketed.** `rvol_intraday_live` is the cumulative session volume divided by the 10-day average daily volume. At 09:45 only 15 of 390 session minutes have elapsed, so it is mechanically ~1/26 of the meaningful value and cannot reach 3 before the lunch bell for any name.
- **Why not time-scaled.** Dividing by elapsed TIME assumes volume accrues evenly across the session. It does not: the first 15 minutes carry a median 8.2% of the day's volume against 3.8% for time-even accrual, so a time-scaled projection over-states the session by roughly 2x. The time-of-day-normalised metric had less than half the error.
- **The earlier cross-check snapshot.** The Cboe delayed-quote CDN's own `last_trade_time` defines the earlier window; its cumulative regular-session volume is the numerator, against the prior-10 mean of the SAME clock window on the same Yahoo series. `rvol_at_09_38` publishes the RAW ratio at that snapshot so the normalisation can be checked rather than trusted. 93 of 93 published rows carry a live Cboe corroboration.
- **The prior-session reading.** Recomputed on the same feed with the identical formula - the previous session's own clock window, its own prior-10 baseline, and the SAME TradingView denominator as today's reading. The published value is carried alongside as `prev_session_rvol_published` with `denominator_drift_pct` as a CROSS-CHECK, never as the baseline: `average_volume_10d_calc` is a rolling average and moves between fetches as each session prints into the window, so a published value is on that day's scale and a tiny move can flip a verdict near the bar.
- **The daily-volume source.** Yahoo `interval=1d` bars. Measured over 240 symbol-sessions across 40 names, Yahoo-1d / Nasdaq-consolidated is median 1.0000, mean 0.9997, max deviation 0.32%, with zero comparisons outside +/-1% - and the Nasdaq call is 16x slower per symbol and returns empty for some symbols.
- **Pre-market.** The Yahoo chart call uses regular-session bars (`includePrePost` off), so session volume EXCLUDES pre-market prints by construction: `pm_vol_source: not_subtracted`, `pm_vol: 0`. No subtraction was needed, so no dependency on cron #08's file was required.
- **Every published `rvol_now` was recomputed from the same Yahoo series and asserted against the scoring engine's own value before anything was written. Rows that failed the assertion were dropped, not published.

## Source health
- **TradingView scanner (denominator):** one pull, no truncation and no coverage problem reported - one denominator set used for BOTH sides of every crossing.
- **Yahoo chart API (session volume, close, baselines):** healthy; every published row was verified against the engine's independent value.
- **Cboe delayed-quote CDN (earlier snapshot):** reachable and live - 93 of 93 published rows carry its own timestamp and volume.
- **Upstream focus list:** `daily-screens/2026-11-11/focus.md`, 12 names, `lag_sessions` 1.
- **Unpriced names:** 332 of 1636 candidates had no regular-session bars in the fetched window (`no_session_bars`); they are reported as unpriced, never as a zero.

## Degradation / caveats
- **332 candidates could not be priced** - no regular-session bars in the fetched window. They are excluded from every count rather than published as a zero or a daily proxy.
- **The universe is a CANDIDATE SET, not the market.** It is unioned from the previous session's published files (focus roster, sweep master, cron #17 boards). A name that was in none of them cannot appear here, so this screen can still miss a mover that was off every board yesterday.
- **`rvol_tod_normalised` is a morning metric.** It says how hot a name is against its OWN norm at 09:45. It is not a full-day relative volume and it is not comparable with cron #09's completed-session `rvol_<date>` (call that `rvol_session_eod` when you compare them).
- **`rvol_intraday_live` is reference only.** It is mechanically tiny at 09:45 and is never used for bucketing.
- **The `rvol_trend` column is the earlier-snapshot delta** (`rvol_now` - `rvol_prev`), per the artifact contract. The session-over-session delta is kept separately as `rvol_vs_prev_session` in the CSV so nothing is lost.
