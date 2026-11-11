---
date: 2026-11-11
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-11
focus_dir_date: 2026-11-10
screen_data_date: 2026-11-09
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars, interval=5m&range=1mo&includePrePost=false (session volume, the 09:45 ET close and the prior-10 same-window baseline) + TradingView america scanner average_volume_10d_calc (denominator only) + Nasdaq /historical (consolidated daily volume for the prior-10 scale factor) + Nasdaq /chart (independent 09:44 ET consolidated price print) + Cboe delayed-quote CDN (independent opening-slot volume and price cross-check) + bridge market-recap get_quotes (live price/volume corroboration) + cron #08 pre-market-gapper.csv (pre-market exclusion cross-check)
method: rvol_tod_normalised, time-of-day-normalised intraday RVOL. Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean consolidated daily volume divided by TV average_volume_10d_calc. The earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 10-minute window; the Cboe delayed snapshot corroborates that slot.
metric_def: rvol_tod_normalised = (cumulative volume 09:30 -> the fire's bar, today) / (mean cumulative volume over 09:30 -> the SAME clock window across the prior 10 sessions) x (mean full-day volume across those prior 10 sessions / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the fire bar / TV average_volume_10d_calc (reference only, never bucketed); rvol_prev = the same formula over the 09:30-09:35 ET slot against the prior-10 mean of that slot; rvol_at_09_38 = the raw cumulative ratio at that earlier snapshot
bucket_rule: rvol_tod_normalised >= 1.5 -> RVOL Required, otherwise Liquid
rvol_required_bucket: 1.5
rvol_alert_threshold: 1.5
near_miss_floor: 1.275
alert_rule: An alert fires for a name whose rvol_now is at or above RVOL_ALERT_THRESHOLD (1.5) AND whose prev_session_rvol is below RVOL_ALERT_THRESHOLD (1.5) - that is, the name crossed UP through the alert bar since the previous session's published reading.
pm_source_status: not_subtracted
cross_check_source: same_series_truncated
status: ok
upstream: daily-screens/2026-11-10/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-11 09:45 ET (cron #07)

## TL;DR

- **1 of 12** focus names is in the **RVOL Required** bucket (rvol_now >= 1.5): **BW 4.08x**, and it is the only name on the tape above the bar. **Near misses: 2** - LUNR 1.42x and FRVO 1.33x. **Alerts: 0.**
- **The caveat that changes how this reads: the Required name is a LEVEL, not a crossing, and the alert tier is empty by construction rather than by a calm tape.** The roster turned over completely again - the previous session's published snapshot (`daily-screens/2026-11-10/focus-rvol-snapshot.csv`) carries an rvol_now for 12 names (ETON, QNT, RGTI, TMDX, FLY, FROG, LASR, OKLO, CYRX, IONQ, RHLD, KRMN) and **not one of them is in today's universe**. So `prev_session_rvol` is `n/a` on every row and no crossing can be proven. BW is published as WATCH, not ALERT.
- **BW is fading inside the Required bucket, not building.** It printed 4.42x on the 09:30-09:35 ET slot and is down to 4.08x at the fire - a **-0.34x** delta, the largest fade on the tape, on a name already +8.18% versus the prior close (4.87 vs 4.50). The opening burst is already being handed back.
- **LUNR crossed the OTHER way.** At the 09:30-09:35 ET slot it read 1.52x - **above the 1.5x alert bar** - and it is now 1.42x, back below it. That is a downward crossing, not an upward one, so it is a near miss and not an alert; it is the name to watch for a re-break upward.
- **The fastest climber is not near the bar.** PRAX is the day's biggest riser at **+0.28x** (0.86x -> 1.14x), with QXO +0.24x and MPWR +0.21x behind it - all three still below 1.0x. **Trend split: 5 ACCELERATING** (IAM, PRAX, TTD, QXO, MPWR), **4 DECELERATING** (BW, LUNR, FRVO, PL), **3 STABLE** (WRBY, TLS, IMVT).

## Universe

12 names from `daily-screens/2026-11-10/focus.md` - the 2026-11-10 18:30 ET sweep, which **has already fired** (unlike the 2026-11-10 run, whose day's sweep had not yet run at 09:45). `focus_dir_date` = 2026-11-10; the sweep's own header `Screen data_date:` = **2026-11-09** (shibui T+1), read from `focus.md`, not inferred from the folder name. `lag_sessions` = **1** trading session (2026-11-10, the only session between 2026-11-09 and 2026-11-11; the same counting convention as the 2026-11-10 artifact) - the normal case, because cron #09 fires at 18:30 ET and today's sweep cannot exist yet. All 12 names were priced (no `no_intraday_bars`).

## Table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BW | 4.87 | 0.3019 | 4.08 | 4.42 | 0.2707 | DECELERATING (-0.34) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LUNR | 12.11 | 0.1419 | 1.42 | 1.52 | 0.1218 | DECELERATING (-0.11) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FRVO | 11.98 | 0.0831 | 1.33 | 1.40 | 0.0648 | DECELERATING (-0.07) | n/a | Liquid | NEAR MISS | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IAM | 14.09 | 0.1149 | 1.17 | 1.10 | 0.0883 | ACCELERATING (+0.06) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PRAX | 340.53 | 0.0355 | 1.14 | 0.86 | 0.0225 | ACCELERATING (+0.28) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TTD | 15.95 | 0.0968 | 0.94 | 0.89 | 0.0798 | ACCELERATING (+0.05) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| PL | 14.46 | 0.0699 | 0.94 | 0.99 | 0.0588 | DECELERATING (-0.05) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| QXO | 13.84 | 0.0588 | 0.90 | 0.65 | 0.0328 | ACCELERATING (+0.24) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| MPWR | 1403.61 | 0.0586 | 0.89 | 0.67 | 0.0360 | ACCELERATING (+0.21) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| WRBY | 30.75 | 0.0385 | 0.72 | 0.71 | 0.0316 | STABLE (+0.02) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TLS | 7.80 | 0.0970 | 0.59 | 0.64 | 0.0941 | STABLE (-0.05) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IMVT | 36.36 | 0.0124 | 0.23 | 0.24 | 0.0102 | STABLE (-0.01) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-11 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts

- Universe size: **12**
- RVOL Required (rvol_now >= 1.5): **1** - BW 4.08x
- Liquid: **11**
- NEAR MISS (1.275 <= rvol_now < 1.5): **2** - LUNR 1.42x, FRVO 1.33x
- Alert count: **0** - crossings: **0**
- UNADJUSTED rows (pre-market not subtracted): **0**
- Names unpriced: **0**

## Alerts

**none - no prior reading available.**

The alert rule requires a name whose `rvol_now` is at or above `RVOL_ALERT_THRESHOLD` (1.5) **and** whose `prev_session_rvol` is below 1.5, i.e. a proven upward crossing since the previous session's published reading. `daily-screens/2026-11-10/focus-rvol-snapshot.csv` published an `rvol_now` for ETON, QNT, RGTI, TMDX, FLY, FROG, LASR, OKLO, CYRX, IONQ, RHLD and KRMN - **zero of those 12 names is in today's universe**, so the baseline does not cover a single row and `prev_session_rvol` is `n/a` everywhere. BW is above the bar but carries no prior reading, so it is published as **WATCH**: a measurable level, not a proven crossing. It is the name the next fire's baseline will convert into an alert or dismiss.

## Near misses

| symbol | rvol_now | rvol_prev | prev_session_rvol | trend | what would turn it into an alert |
|---|---|---|---|---|---|
| LUNR | 1.42x | 1.52x | n/a | DECELERATING (-0.11) | rvol_now back to >= 1.5 while prev_session_rvol stays below 1.5. It already read 1.52x on the 09:30-09:35 ET slot, so it has been above the bar and fallen back through it - the re-break is the trade, not the level. |
| FRVO | 1.33x | 1.40x | n/a | DECELERATING (-0.07) | rvol_now reaching 1.5 with prev_session_rvol still below 1.5. It is 0.17x short of the bar and fading, so it needs volume to accelerate, not merely persist. |

## Universe change

Compared with the previous sweep (`daily-screens/2026-11-09/focus.md`, 12 names).

- **Entered (12):** BW, FRVO, IAM, IMVT, LUNR, MPWR, PL, PRAX, QXO, TLS, TTD, WRBY
- **Left (12):** CYRX, ETON, FLY, FROG, IONQ, KRMN, LASR, OKLO, QNT, RGTI, RHLD, TMDX

**100% turnover again** - the 2026-11-10 sweep shares exactly ZERO names with the 2026-11-09 sweep. The roster is rebuilt from scratch on most nights, which is exactly why a missing baseline is a structural condition of this routine rather than an occasional failure: the next fire's CSV is the only baseline that survives the turnover.

## Method

- Metric: `rvol_tod_normalised` (time-of-day-normalised). Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean consolidated daily volume / TV `average_volume_10d_calc` (the only TV field used; TV's live columns lag the session and are never used for a live field).
- Today's volume and the 09:45 ET close: Yahoo chart API, `interval=5m&range=1mo&includePrePost=false` - one call per symbol, 12/12 ok. Bars are stamped at interval start, so the last COMPLETED bar at the 09:45 fire is the one stamped 09:40 and the volume window is 09:30 + 09:35 + 09:40. The in-progress 09:45 bar and the trailing zero-volume bar were dropped.
- Prior sessions: the same Yahoo 5-minute series (`range=1mo`, 21-22 sessions fetched) plus Nasdaq `/historical` for the consolidated daily volume that carries the scale factor. A prior session enters the baseline **only if its 09:30/09:35/09:40 bars are all present AND non-zero AND a consolidated daily print exists**. Ten names run 2026-10-28 -> 2026-11-10 with no exclusions; **IAM and WRBY each skip one session and reach back to 2026-10-27** (a zero-volume or missing opening bar). An incomplete opening bar would deflate the baseline and inflate the name's rvol, so broken sessions are excluded rather than used with a zero.
- Scale factor: prior-10 mean consolidated daily volume (Nasdaq `/historical`) / TV `average_volume_10d_calc`. It lands at 1.03-1.22 for 12 of 12 names (IAM is the outlier at 1.22). The factor runs above 1.0 because TV's `average_volume_10d_calc` is a trailing-10 average that includes TODAY'S partial volume and drops the oldest completed session, so rvol_now is correspondingly higher than a completed-session basis. The same convention was used on 2026-11-10, so the two artifacts are comparable.
- Independent checks: Nasdaq `/chart` gives an independent consolidated per-minute print, and the published `close` - the Yahoo 09:40-stamped bar close - equals Nasdaq's own LAST consolidated print before the bar closed (09:44 ET) **exactly on 12 of 12 names** (max difference 0.0000%). Both feeds are independent and land on the same trade, which validates the fire-time close on every row. The Nasdaq 09:45 print is the FIRST trade AFTER the bar closed, so it is published separately as `nq_px_0945` with its own outlier flag (0 of 12 flagged today) rather than compared as the close.
- The bridge `market-recap` quote corroborates today's cumulative volume and price with `market_state=open` and a fresh `as_of` (09:50-09:51 ET). The bridge was read ~6 minutes AFTER the fire, so its price is NOT the fire-time close - the published `close` is the last COMPLETED bar close at the fire (the Yahoo 09:40-stamped bar), with the bridge price carried separately in `bridge_px`.
- Cross-check snapshot: the earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 10-minute window (`cross_check_source: same_series_truncated`). CBOE IS reachable, but its snapshot response is 09:48:45 ET - **after** the 09:45 fire - so it cannot serve as the earlier snapshot; its volume and price are published as the independent corroboration of the opening slot (`cboe_vol`, `cboe_ts`, `cboe_last_trade`, `cboe_raw_ratio`).
- Pre-market: excluded by construction (Yahoo `includePrePost=false`; every session's first bar is stamped 09:30 ET and the last 15:55 ET), so `pm_vol` = 0 and `pm_vol_source` = `not_subtracted`; no dependency on cron #08. Verified structurally: across the 12 symbols and the fetched sessions, **20,428 bars were examined and not one is stamped outside 09:30-15:55 ET**, so a pre-market print cannot be inside any bar. Cross-checked against cron #08's pre-market volumes for the same 12 names (157,925 shares for BW, 153,000 for TTD, 625 for PRAX), none of which appears in the Yahoo session bars.
- Trend: `ACCELERATING` / `STABLE` / `DECELERATING` with the numeric delta; |delta| <= 0.05 is STABLE. Each reading is normalised against its own prior-10 mean for its own window, so a negative delta means today's volume arrived MORE front-loaded than that name's own history.
- Tier vocabulary: `ALERT` = a proven crossing; `NEAR MISS` = 1.275-1.5x; `WATCH` = at or above 1.0x but not an alert, which includes names above the 1.5x bar with no prior-session baseline; `-` = below 1.0x; `UNADJUSTED` = pre-market not subtracted (0 rows today).

## Source health

| source | endpoint / query | status | result |
|---|---|---|---|
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/{SYM}?interval=5m&range=1mo&includePrePost=false` | ok 12/12 | 20,428 bars, 21-22 sessions per symbol; 0 bars outside 09:30-15:55 ET |
| TradingView scanner | `POST scanner.tradingview.com/america/scan`, columns + `range [0,10000]` and `[10000,20155]`, `sort {"sortBy":"name","sortOrder":"asc"}` | ok | 20,155 rows returned = `totalCount` 20,155, **zero overlap between the two pages**; all 12 universe names present; `average_volume_10d_calc` used as the denominator only |
| Nasdaq /historical | `api.nasdaq.com/api/quote/{SYM}/historical` | ok 12/12 | consolidated daily volume for the prior-10 scale factor |
| Nasdaq /chart | `api.nasdaq.com/api/quote/{SYM}/chart` | ok 12/12 | independent consolidated per-minute prints, incl. the 09:44 ET print; fire close agrees on 12/12 |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | ok 12/12 | snapshot response 09:48:45 ET (after the fire), last trade 09:33-09:34 ET |
| bridge market-recap | `market-recap get_quotes` (12 symbols, 1 call) | ok 12/12, market_state=open | as_of 09:50-09:51 ET |
| cron #08 pre-market | `daily-screens/2026-11-11/pre-market-gapper.csv` | ok | 12/12 universe names present; used only to corroborate the pre-market exclusion |
| upstream focus list | `daily-screens/2026-11-10/focus.md` (outputs repo) | ok | 12 names |
| MCP catalog probe | `probe_mcp.py` | ok | `catalog_ok total=135 finance_tools=0` - no financial MCP registered; bridge packs tradier, fmp, market-recap |

## Degradation / caveats

- **No alert can be proven for the third fire running.** The roster turns over completely between sweeps (12 of 12 new names again), and the previous session's published CSV does not cover a single one of today's names. The alert tier is empty by construction, not because the tape was quiet - BW at 4.08x is the loudest print in this artifact and still cannot be called a crossing.
- **BW is the only Required name and it is decelerating.** 4.42x on the 09:30-09:35 ET slot down to 4.08x at the fire, on a name +8.18% versus the prior close after a +4.49% pre-market gap (cron #08 FLAGGED). The level is real; the direction is not accumulation.
- **LUNR is the mirror image**: it read 1.52x on the earlier slot - above the 1.5x bar - and is now 1.42x. A name that crossed the bar DOWNWARD is a near miss, not an alert, and it is published as such.
- **The trend column compares different window lengths.** rvol_now is a 15-minute window and rvol_prev a 10-minute slot, each normalised against its own history. The delta is directional, not a like-for-like magnitude - this is the same construction as the 2026-11-09 and 2026-11-10 artifacts, so the three published trend columns are comparable with each other but none is a clean acceleration rate.
- **The daily factor runs above 1.0 for 12 of 12 names** (TV's `average_volume_10d_calc` includes today's partial volume and drops the oldest completed session), so every rvol_now is a few percent above a completed-session basis. The series stays comparable with the 2026-11-10 artifact because the same convention was used there.
- **IAM's factor is the outlier at 1.22**, the widest of the set; its baseline reaches back to 2026-10-27 because one session was excluded for a broken opening bar. IAM is nowhere near either threshold, so the choice does not change its tier.
- **In-progress and later bars dropped.** No bar stamped after 09:40 ET contributes any volume, and the zero-volume trailing bars were excluded. The fire snapshot is reconstructed at the 09:45 ET stamp from bars that had already closed, so this artifact is the 09:45 tape even though the data was pulled minutes later.
- **rvol_intraday_live** is published for reference only and is mechanically tiny at 09:45 (15 of 390 session minutes). Never bucket on it. TV's `relative_volume_10d_calc` is carried as `tv_rvol_proxy_daily` for the same reason - it is a live-column proxy, not intraday RVOL.
- **Yahoo's 5-minute series undercounts the consolidated tape on full days** (its bar sum runs below Nasdaq's consolidated daily volume, because the closing auction consolidates after the last 5-minute bar). This does not affect the window ratio - today's window and the prior-10 window means come from the same feed - but it is why the scale factor uses Nasdaq's settled consolidated daily volume rather than the Yahoo bar sum.
- **One Required name, two near misses and no alerts means this artifact reports a thin, mostly quiet tape with one very loud name in it.** The tier structure is empty on the alert side; what it does publish is the level, the trend and the direction of each name's opening pace - and the next session's CSV is what turns any of it into a crossing test.
