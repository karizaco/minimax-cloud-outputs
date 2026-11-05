---
date: 2026-11-05
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-05
focus_dir_date: 2026-11-04
screen_data_date: 2026-11-03
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: TradingView america scanner (average_volume_10d_calc, denominator only) + polygon/Massive 5-minute aggregates via the Pipeworx gateway (prior-session window and full-day volumes) + StockTwits chart_data 1D/1W/1M (today's 5-minute bars, 30-minute and daily history) + Nasdaq /chart (independent consolidated daily volume) + Cboe delayed-quote CDN + bridge market-recap get_quotes (price/volume cross-checks)
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Session volume = StockTwits 5-minute bars stamped 09:30/09:35/09:40 ET (the in-progress bar and every bar after the fire were dropped); prior-session same-window mean = polygon 5-minute bars over the prior 10 sessions; because the two feeds cover different fractions of consolidated tape, the window ratio is bridged by f_win = mean over the prior sessions of (StockTwits 30-minute 09:30-10:00 bar / polygon 09:30-10:00 sum), then scaled by (prior-10 mean consolidated daily volume / TV average_volume_10d_calc). The bridge is constructed so that a name printing exactly its own prior-session opening window reads exactly 1.00x. rvol_intraday_live = consolidated-equivalent cumulative session volume / TV average_volume_10d_calc (reference only - never bucket on it). rvol_prev is the same metric at the 09:40 ET cross-check snapshot; the Cboe delayed snapshot was NOT usable for it (it had already advanced to 10:19-10:21 ET, later than the fire), so the cross-check truncates the same 5-minute series at the 09:35 bar. Pre-market prints are excluded by construction (both intraday feeds are regular-session only), so pm_vol = 0 and pm_vol_source = not_subtracted. Trend epsilon: |delta| <= 0.05 = STABLE.
metric_def: rvol_tod_normalised = (today's 09:30-09:45 ET window volume / (f_win x prior-10 mean same-window volume)) x (prior-10 mean full-day volume / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the last completed bar / TV average_volume_10d_calc
bucket_rule: rvol_tod_normalised >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's published reading.
pm_source_status: not_subtracted
cross_check_source: same_series_truncated
status: ok
upstream: daily-screens/2026-11-04/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-05 09:45 ET (cron #07)

## TL;DR

- 7 of 12 focus names are in the **RVOL Required** bucket (rvol_now >= 1.5): FN 2.33x, EVER 2.32x, APLD 1.88x, AEHR 1.80x, CIFR 1.80x, AEIS 1.58x, ECG 1.51x.
- 2 near miss(es) (1.275-1.5x): CLSK 1.48x, FISV 1.30x.
- **Alerts: none** - the 2026-11-04 snapshot published no rvol_now for any of today's 12 names (the roster turned over completely), so no crossing can be claimed. The names above the bar carry tier WATCH, not ALERT.
- **Caveat that changes how this reads:** the contract's primary intraday path (Yahoo chart API) was rate-limited from this egress all session, so today's window volume comes from the StockTwits intraday feed and the prior-session baseline from polygon 5-minute bars. The two feeds cover different fractions of consolidated tape (55-82% vs 79-89%), so every ratio is bridged by a same-window factor measured on the prior sessions; names within ~0.15x of the 1.5 bar can flip bucket on the bridge choice (CLSK 1.48x/1.53x, ECG 1.51x/1.86x, BETA 1.20x/1.39x).
- This artifact is a **late reconstruction**: the fire was 09:45 ET and the run executed ~3.5 hours later, so the snapshot window (09:30-09:45 ET) was rebuilt from intraday bars.

## Universe

12 names from `daily-screens/2026-11-04/focus.md` - the most recent completed 18:30 ET sweep (Tue 2026-11-04, 12 names). `focus_dir_date` = 2026-11-04; the sweep's own screen data date = **2026-11-03** (shibui T+1), read from the focus.md header, not inferred from the folder name. `lag_sessions` = **1** trading session - the normal weekday T+1 ingest, not a degradation.

## Table

Sorted by rvol_now desc, then by trend (accelerating first).

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---|---|
| FN | 314.55 | 0.1925 | **2.3288** | 2.1574 | 0.1396 | ACCELERATING (+0.171) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| EVER | 30.81 | 0.1676 | **2.3184** | 2.6976 | 0.1571 | DECELERATING (-0.379) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| APLD | 15.10 | 0.2066 | **1.8758** | 1.8069 | 0.1471 | ACCELERATING (+0.069) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| AEHR | 53.85 | 0.2541 | **1.7970** | 1.8555 | 0.2054 | DECELERATING (-0.058) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| CIFR | 5.99 | 0.1731 | **1.7954** | 1.6597 | 0.1123 | ACCELERATING (+0.136) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| AEIS | 198.50 | 0.0965 | **1.5809** | 1.7413 | 0.0854 | DECELERATING (-0.160) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| ECG | 75.01 | 0.0701 | **1.5056** | 1.7137 | 0.0548 | DECELERATING (-0.208) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| CLSK | 6.36 | 0.1336 | **1.4819** | 1.4352 | 0.0969 | STABLE (+0.047) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-05 09:45 ET |
| FISV | 62.45 | 0.0918 | **1.2999** | 1.3135 | 0.0726 | STABLE (-0.014) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-05 09:45 ET |
| BETA | 24.39 | 0.0957 | **1.2011** | 1.4318 | 0.0809 | DECELERATING (-0.231) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| CORZ | 11.88 | 0.0926 | **1.0916** | 1.0233 | 0.0635 | ACCELERATING (+0.068) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-05 09:45 ET |
| FRVO | 8.22 | 0.0508 | **0.6479** | 0.6728 | 0.0409 | STABLE (-0.025) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-05 09:45 ET |

### Counts

- Focus tickers: **12**
- RVOL Required (rvol_now >= 1.5): **7** - FN 2.33x, EVER 2.32x, APLD 1.88x, AEHR 1.80x, CIFR 1.80x, AEIS 1.58x, ECG 1.51x
- Liquid: **5** - CLSK 1.48x, FISV 1.30x, BETA 1.20x, CORZ 1.09x, FRVO 0.65x
- NEAR MISS (1.275 <= rvol_now < 1.5): **2** - CLSK 1.48x, FISV 1.30x
- Alerts (crossings): **0**
- Crossings (prior reading < 1.5 and rvol_now >= 1.5): **0** - no prior reading available for any of today's names
- UNADJUSTED rows: **0**
- Names with a prior-session baseline: **0 / 12**

## Alerts

**none (no prior reading available).** The alert rule needs the previous session's published rvol_now for the SAME ticker. `daily-screens/2026-11-04/focus-rvol-snapshot.csv` exists and carries 12 tickers - but they are the previous SWEEP's roster (CVNA, CLF, VSEC, FIGS, KVYO, FTAI, TEM, WING, CAI, MRNA, HTFL, KOD) and share **zero** names with today's universe, so `prev_session_rvol` is `n/a` on every row and no crossing can be claimed. Claiming one without a prior reading would be fabrication, not a signal.

The names that are **at or above the 1.5 bar without an alert** (tier WATCH) are: FN 2.33x (ACCELERATING), EVER 2.32x (DECELERATING), APLD 1.88x (ACCELERATING), AEHR 1.80x (DECELERATING), CIFR 1.80x (ACCELERATING), AEIS 1.58x (DECELERATING), ECG 1.51x (DECELERATING).

Reads: FN ACCELERATING 2.16x -> 2.33x; EVER DECELERATING 2.70x -> 2.32x; APLD ACCELERATING 1.81x -> 1.88x; AEHR DECELERATING 1.86x -> 1.80x; CIFR ACCELERATING 1.66x -> 1.80x; AEIS DECELERATING 1.74x -> 1.58x; ECG DECELERATING 1.71x -> 1.51x

## Near misses

| symbol | rvol_now | rvol_prev | trend | what turns it into an alert |
|---|---:|---:|---|---|
| CLSK | 1.482 | 1.435 | STABLE (+0.047) | rvol_now reaching 1.5 while prev_session_rvol stays below 1.5 |
| FISV | 1.300 | 1.313 | STABLE (-0.014) | rvol_now reaching 1.5 while prev_session_rvol stays below 1.5 |

## Universe change

Versus the previous sweep (`daily-screens/2026-11-03/focus.md`, 12 names):

- Entered (12): AEHR, AEIS, APLD, BETA, CIFR, CLSK, CORZ, ECG, EVER, FISV, FN, FRVO
- Left (12): WING, KVYO, CVNA, FTAI, FIGS, TEM, CLF, CAI, HTFL, KOD, MRNA, VSEC
- Overlap: **0** - the roster turned over completely, which is why the previous session's baseline covers none of today's names.

## Method

- Metric: `rvol_tod_normalised` (time-of-day-normalised). Today's window is 09:30-09:45 ET - 15 of 390 session minutes - and is compared with the SAME clock window on the prior 10 sessions, then scaled to full-day units.
- Today's volume: StockTwits `chart_data` period 1D, 5-minute bars, regular session only. Bars stamped 09:30, 09:35 and 09:40 are the last COMPLETED bars at the fire; the in-progress bar and everything after it were dropped.
- Prior sessions: polygon/Massive 5-minute aggregates, 2026-10-20 to 2026-11-04 (12 sessions available; the most recent 10 are used), regular-session 09:30-16:00 sums for full-day volume and the same-window sums for the baseline.
- Cross-feed bridge: the StockTwits intraday feed covers 55-82% of consolidated tape volume and polygon's minute bars cover 79-89% (both measured against the consolidated daily). The ratio `f_win` (mean over the prior sessions of StockTwits' 09:30-10:00 bar divided by polygon's 09:30-10:00 sum) is applied so the window comparison is like-for-like; per name it ranges 0.76-0.97 with a per-name spread of 0.002-0.055.
- Scale factor: prior-10 mean consolidated daily volume (StockTwits 1M, verified identical to Nasdaq consolidated volume on 12/12 names) divided by TV `average_volume_10d_calc` (the only TV field used - TV's live columns lag the session and are never used for a live field).
- Cross-check snapshot: the same 5-minute series truncated at the 09:35 bar (`cross_check_source: same_series_truncated`). The Cboe delayed-quote CDN was reachable but its snapshot had already advanced to 10:19-10:21 ET, i.e. LATER than the fire, so it could not serve as the earlier reading.
- Pre-market: excluded by construction (both intraday feeds are regular-session only), so `pm_vol` = 0 and `pm_vol_source` = not_subtracted; no dependency on cron #08.
- Trend: `ACCELERATING` / `STABLE` / `DECELERATING` with the numeric delta; |delta| <= 0.05 is STABLE.
- Tier vocabulary: `ALERT` = a proven crossing; `NEAR MISS` = 1.275-1.5x; `WATCH` = at or above its own norm but not an alert - which includes names at or above the 1.5 bar that have no prior-session baseline, since no crossing can be proven for them; `-` = below 1.0x; `UNADJUSTED` = pre-market not subtracted (0 rows today).

## Source health

| source | url / query | status |
|---|---|---|
| Yahoo chart API (contract's primary intraday path) | query1/query2 /v8/finance/chart, interval=5m | failed: 429 rate-limited from this egress all session (incl. the crumb handshake) - replaced by the two feeds below |
| polygon / Massive aggregates (Pipeworx gateway) | polygon-io `aggregates`, 5m, 2026-10-20..2026-11-05 | ok 12/12 symbols (free tier, 5 req/min shared key) |
| StockTwits chart_data 1D (today, 5m bars) | stocktwits `chart_data` period 1D | ok 12/12 symbols, 78 bars each |
| StockTwits chart_data 1W / 1M (history) | periods 1W, 1M | ok 12/12 |
| TradingView america scanner | POST scanner.tradingview.com/america/scan, `average_volume_10d_calc` | ok 19,950 rows, 12/12 matched |
| Nasdaq /chart (independent consolidated daily) | api.nasdaq.com/api/quote/{SYM}/chart | ok 12/12 - matches the StockTwits daily series to 0.00% on 11-04 |
| Cboe delayed-quote CDN | cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json | ok 12/12 but snapshot 10:19-10:21 ET (later than the fire) - cross-check only |
| bridge market-recap get_quotes | Pipeworx gateway, batched 12 symbols | ok 12/12, market_state open |
| MCP availability probe | probe_mcp.py | catalog_ok total=135 finance_tools=0, bridge packs tradier/fmp/market-recap |

## Degradation / caveats

- **Yahoo was unavailable.** The contract's primary intraday source returned HTTP 429 from this egress for every request including the cookie+crumb handshake, so today's window volume comes from StockTwits and the prior-session baseline from polygon. The metric is therefore bridged across feeds (see Method).
- **Bridge sensitivity.** Using the session-wide coverage ratio instead of the same-window factor moves individual names by up to ~0.35x: FN 2.33x->2.62x; EVER 2.32x->2.66x; AEHR 1.80x->1.97x; AEIS 1.58x->1.78x; ECG 1.51x->1.86x; BETA 1.20x->1.39x. Names within ~0.15x of a bar (CLSK 1.48x, ECG 1.51x, BETA 1.20x) can move bucket; the ones well inside a band cannot.
- **No alert baseline.** The previous session's snapshot shares no ticker with today's universe (roster turnover is complete), so `prev_session_rvol` is `n/a` everywhere and the alert tier is empty. The 1.5x names are reported as WATCH, not ALERT.
- **Late reconstruction.** The fire was 09:45 ET; this run executed ~3.5 hours later because the data path had to be re-planned around the Yahoo block. The snapshot window itself (09:30-09:45 ET) is reconstructed exactly from intraday bars, but the cross-check could not use the live CBOE tape.
- **In-progress bars dropped.** Every 5-minute bar stamped after 09:40 ET was excluded from the session total, including the feed's zero-volume trailing bars.
- `rvol_intraday_live` is published for reference only and is mechanically tiny at 09:45 (15 of 390 session minutes). Never bucket on it.
