---
date: 2026-11-10
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-10
focus_dir_date: 2026-11-09
screen_data_date: 2026-11-06
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars, interval=5m&range=1mo&includePrePost=false (session volume, the 09:45 ET price and the prior-10 same-window baseline) + TradingView america scanner average_volume_10d_calc (denominator only) + Nasdaq /historical (consolidated daily volume for the prior-10 scale factor) + Nasdaq /chart (independent 09:45 ET consolidated price print) + Cboe delayed-quote CDN (independent opening-slot volume and price cross-check) + bridge market-recap get_quotes (live price/volume corroboration) + cron #08 pre-market-gapper.csv (pre-market exclusion cross-check)
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
upstream: daily-screens/2026-11-09/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-10 09:45 ET (cron #07)

## TL;DR

- **7 of 12** focus names are in the **RVOL Required** bucket (rvol_now >= 1.5): ETON 2.74x, QNT 2.08x, RGTI 2.07x, TMDX 2.01x, FLY 1.93x, FROG 1.83x, LASR 1.81x. **Near misses: 0**.
- **Alerts: 0 - and the reason matters more than the count.** The roster turned over completely: `daily-screens/2026-11-09/focus-rvol-snapshot.csv` published an rvol_now for 12 names (WRBY, XERS, ACHC, APP, JOBY, U, MRNA, VRDN, RUN, FUN, SEZL, XNCR) and **not one of them is in today's universe**. So no crossing can be proven: the 7 Required names are **LEVELS, not crossings**, and each carries tier WATCH rather than ALERT.
- **The caveat that changes how this reads:** today's universe is the **2026-11-09 sweep** (screen data 2026-11-06, shibui T+1), because cron #09 fires at 18:30 ET and had not yet run when this artifact was written. `lag_sessions` = 1, the normal case - but 12 of 12 names are new, so **this screen ranks Monday's sweep against Tuesday's tape with no baseline behind it.**
- **Most of the Required bucket is fading, not climbing.** Of the 7 Required names, 4 are DECELERATING (QNT, FLY, FROG, LASR), 2 are ACCELERATING (RGTI, TMDX) and 1 is STABLE (ETON). ETON at 2.74x is the hottest name on the tape and is holding that pace; FROG and LASR, the two weakest of the fading set, have already given back a third of their opening burst.
- **The near-miss band is empty.** No name sits between 1.275x and 1.5x; the closest are OKLO 1.15x and CYRX 1.08x, both WATCH. There is nothing one small move away from the bar.

## Universe

12 names from `daily-screens/2026-11-09/focus.md` - the most recent completed 18:30 ET sweep (Mon 2026-11-09, 12 names). `focus_dir_date` = 2026-11-09; the sweep's own screen data date = **2026-11-06** (shibui T+1), read from the sweep's `daily-sweep.md` header, not inferred from the folder name. `lag_sessions` = **1** trading session (2026-11-09, the only session between 2026-11-06 and 2026-11-10) - the normal case, because cron #09 runs at 18:30 ET and had not yet fired when this artifact was written (the `daily-screens/2026-11-10/` directory holds only cron #08's pre-market output). All 12 names were priced (no `no_intraday_bars`).

## Table

| symbol | close | rvol_intraday_live | rvol_now | rvol_prev | rvol_at_09_38 | rvol_trend | prev_session_rvol | bucket | tier | pm_vol | pm_vol_source | data timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ETON | 65.70 | 0.2048 | 2.74 | 2.76 | 0.1602 | STABLE (-0.01) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| QNT | 42.16 | 0.1769 | 2.08 | 2.18 | 0.1454 | DECELERATING (-0.10) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RGTI | 12.47 | 0.1996 | 2.07 | 2.00 | 0.1608 | ACCELERATING (+0.07) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| TMDX | 95.72 | 0.1093 | 2.01 | 1.71 | 0.0735 | ACCELERATING (+0.29) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FLY | 24.38 | 0.1850 | 1.93 | 2.01 | 0.1665 | DECELERATING (-0.08) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| FROG | 106.24 | 0.1030 | 1.83 | 2.16 | 0.0960 | DECELERATING (-0.33) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| LASR | 44.68 | 0.0850 | 1.81 | 2.12 | 0.0767 | DECELERATING (-0.31) | n/a | RVOL Required | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| OKLO | 25.70 | 0.1114 | 1.15 | 1.19 | 0.0931 | STABLE (-0.03) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| CYRX | 19.89 | 0.0276 | 1.08 | 1.05 | 0.0217 | STABLE (+0.03) | n/a | Liquid | WATCH | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| IONQ | 34.86 | 0.1340 | 0.95 | 1.01 | 0.1170 | DECELERATING (-0.06) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| RHLD | 157.13 | 0.1300 | 0.82 | 0.76 | 0.0845 | ACCELERATING (+0.06) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |
| KRMN | 45.75 | 0.0204 | 0.52 | 0.51 | 0.0170 | STABLE (+0.01) | n/a | Liquid | - | 0 | not_subtracted | 2026-11-10 09:45 ET (last completed 5m bar, stamped 09:40; volume window 09:30-09:45 ET) |

### Counts

- Universe size: **12**
- RVOL Required (rvol_now >= 1.5): **7** (ETON, QNT, RGTI, TMDX, FLY, FROG, LASR)
- Liquid: **5**
- NEAR MISS (1.275-1.5): **0**
- Alerts: **0**
- Crossings proven: **0**
- UNADJUSTED rows (pre-market not subtracted): **0**

## Alerts

**none** - and the reason matters. `daily-screens/2026-11-09/focus-rvol-snapshot.csv` published an `rvol_now` for 12 names (WRBY, XERS, ACHC, APP, JOBY, U, MRNA, VRDN, RUN, FUN, SEZL, XNCR) and **none of them is in today's universe** - a 12-name turnover, the largest of this run's streak. Not one of today's 12 has a prior-session reading, so **no crossing can be proven for any of them**, including the 7 sitting above the 1.5x bar. Every one of those 7 is a LEVEL with no prior reading below the bar, and each carries tier **WATCH**, not ALERT. The alert tier is empty by construction, not because the tape is calm - the tape is hot.

What turns any of them into a real alert: the NEXT fire publishes an `rvol_now` >= 1.5 for that name, and this session's published reading (>= 1.5 for all seven) stands as its `prev_session_rvol`. Until then they are levels, not crossings. One line each, with the pace:

- **ETON** - rvol_now **2.74x** vs rvol_prev 2.76x (holding, -0.01); prev-session reading n/a, so the crossing test starts next session.
- **QNT** - rvol_now **2.08x** vs rvol_prev 2.18x (fading, -0.10); prev-session reading n/a, so the crossing test starts next session.
- **RGTI** - rvol_now **2.07x** vs rvol_prev 2.00x (still climbing, +0.07); prev-session reading n/a, so the crossing test starts next session.
- **TMDX** - rvol_now **2.01x** vs rvol_prev 1.71x (still climbing, +0.29); prev-session reading n/a, so the crossing test starts next session.
- **FLY** - rvol_now **1.93x** vs rvol_prev 2.01x (fading, -0.08); prev-session reading n/a, so the crossing test starts next session.
- **FROG** - rvol_now **1.83x** vs rvol_prev 2.16x (fading, -0.33); prev-session reading n/a, so the crossing test starts next session.
- **LASR** - rvol_now **1.81x** vs rvol_prev 2.12x (fading, -0.31); prev-session reading n/a, so the crossing test starts next session.

## Near misses

**none** - the 1.275x-1.5x band is empty. No name sits inside it, so there is nothing one small move away from the bar. The nearest names below the band are **OKLO 1.15x** and **CYRX 1.08x** (both WATCH, both above 1.0x), and the nearest above it is **LASR 1.81x** (DECELERATING). A name enters this band when its rvol_now prints between 1.275x and 1.5x; nothing in today's universe is there.

## Universe change

Versus the previous sweep (`daily-screens/2026-11-06/focus.md`, 12 names):

- **Entered (12):** ETON, QNT, RGTI, TMDX, FLY, FROG, LASR, OKLO, CYRX, IONQ, RHLD, KRMN
- **Left (12):** RUN, SEZL, XERS, ACHC, MRNA, APP, U, FUN, JOBY, WRBY, VRDN, XNCR
- **Carried over: 0.** Complete turnover, for the second session running - which is why the alert tier is empty and why 12 of 12 names have no prior-session baseline.

## Method

- Metric: `rvol_tod_normalised` (time-of-day-normalised). Today's window is 09:30-09:45 ET - 15 of 390 session minutes - compared with the SAME clock window on the prior 10 eligible sessions, then scaled to full-day units by the prior-10 mean consolidated daily volume / TV `average_volume_10d_calc` (the only TV field used; TV's live columns lag the session and are never used for a live field).
- Today's volume and the 09:45 ET price: Yahoo chart API, `interval=5m&range=1mo&includePrePost=false` - one call per symbol, 12/12 ok. Bars are stamped at interval start, so the last COMPLETED bar at the 09:45 fire is the one stamped 09:40 and the volume window is 09:30 + 09:35 + 09:40. The in-progress 09:45 bar and the trailing zero-volume bar were dropped.
- Prior sessions: the same Yahoo 5-minute series, `range=1mo` (22 sessions fetched), plus Nasdaq `/historical` for the consolidated daily volume that carries the scale factor. A prior session enters the baseline **only if its 09:30/09:35/09:40 bars are all present AND non-zero AND a consolidated daily print exists** - Yahoo's series has zero-volume or missing opening bars on some sessions (**RHLD 2026-11-09 has a zero-volume 09:30 bar**, so RHLD's baseline reaches back to 2026-10-19 to hold 10 clean sessions; the other 11 names run 2026-10-26/27 to 2026-11-09). An incomplete opening bar would deflate the baseline and inflate the name's rvol, so broken sessions are excluded rather than used with a zero.
- Scale factor: prior-10 mean consolidated daily volume (Nasdaq `/historical`) / TV `average_volume_10d_calc`. It lands at 1.00-1.11 for 11 of 12 names (IONQ, KRMN and OKLO are exactly 1.00 - TV's trailing-10 window coincides with their 10 completed sessions; RHLD is 0.94). The factor runs above 1.0 because TV's `average_volume_10d_calc` is a trailing-10 average that includes TODAY'S partial volume and drops the oldest completed session, so rvol_now is correspondingly higher than a completed-session basis. The same convention was used on 2026-11-09, so the two artifacts are comparable.
- Independent checks: Nasdaq `/chart` gives an independent consolidated 09:45 ET print per name, published as `nq_px_0945` with an outlier flag (a print sitting outside the range of its own 09:43-09:47 neighbouring minute prints); the bridge `market-recap` quote corroborates today's cumulative volume and price with `market_state=open` and a fresh `as_of` (09:46-09:50 ET). The bridge was read ~5 minutes AFTER the fire, so its price is NOT the fire-time close - the published `close` is the last COMPLETED bar close at the fire (the Yahoo 09:40-stamped bar), with the bridge price carried separately in `bridge_px`.
- Price agreement (strongest check of the run): the published `close` - the Yahoo 09:40-stamped bar close - equals Nasdaq's own LAST consolidated print before the bar closed (09:44 ET) **exactly on 12 of 12 names** (max difference 0.0000%, mean 0.0000%). Both feeds are independent and land on the same trade, which validates the fire-time close on every row. The Nasdaq 09:45 print is the FIRST trade AFTER the bar closed, so it is published separately as `nq_px_0945` with its own outlier flag rather than compared as the close.
- Tick outliers: the 09:45 print is flagged `nq_px_0945_outlier_tick: yes` only when it sits outside its own 09:43-09:47 neighbouring prints by at least 0.5% (1 of 12 today: TMDX); names with fewer than two neighbouring prints are flagged `n/a`. No flagged or unflagged 09:45 print ever enters the published `close` - that is the 09:40 bar close on every row.
- Cross-check snapshot: the earlier reading is the 09:30-09:35 ET slot of the same series, normalised against the prior-10 mean of that same 10-minute window (`cross_check_source: same_series_truncated`). CBOE IS reachable, but its snapshot response time is 09:48 ET - **after** the 09:45 fire - so it cannot serve as the earlier snapshot; its volume and price are published as the independent corroboration of the opening slot (`cboe_vol`, `cboe_ts`, `cboe_last_trade`, `cboe_raw_ratio`), and its last trade (09:32-09:33 ET) sits inside the 09:30 bar.
- Pre-market: excluded by construction (Yahoo `includePrePost=false`; every session's first bar is stamped 09:30 ET and the last 15:55 ET), so `pm_vol` = 0 and `pm_vol_source` = `not_subtracted`; no dependency on cron #08. Verified structurally: across the 12 symbols and 22 fetched sessions, **19,716 bars were examined and not one is stamped outside 09:30-15:55 ET**, so a pre-market print cannot be inside any bar. Cross-checked against cron #08's pre-market volumes (755 to 1,085,423 shares) and against Nasdaq `/chart`'s own pre-market prints (CYRX 08:30 20.50, 08:32 20.32, 09:23 20.32), which are absent from the Yahoo session bars.
- Trend: `ACCELERATING` / `STABLE` / `DECELERATING` with the numeric delta; |delta| <= 0.05 is STABLE. Each reading is normalised against its own prior-10 mean for its own window, so a negative delta means today's volume arrived MORE front-loaded than that name's own history.
- Tier vocabulary: `ALERT` = a proven crossing; `NEAR MISS` = 1.275-1.5x; `WATCH` = at or above 1.0x but not an alert, which includes names above the 1.5x bar with no prior-session baseline; `-` = below 1.0x; `UNADJUSTED` = pre-market not subtracted (0 rows today).

## Source health

| source | endpoint / query | status | result |
|---|---|---|---|
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/{SYM}?interval=5m&range=1mo&includePrePost=false` | ok 12/12 (429 on a bare-UA request, retried with a browser UA) | 19,716 bars, 22 sessions per symbol |
| TradingView scanner | `POST scanner.tradingview.com/america/scan`, columns + range [0,20000], filtered locally | ok | 20,000 rows returned (the request cap); all 12 universe names present; `average_volume_10d_calc` used as the denominator only |
| Nasdaq /historical | `api.nasdaq.com/api/quote/{SYM}/historical` | ok 12/12 | consolidated daily volume for the prior-10 scale factor |
| Nasdaq /chart | `api.nasdaq.com/api/quote/{SYM}/chart` | ok 12/12 | independent consolidated per-minute prints, incl. the 09:45 ET print |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | ok 12/12 | snapshot response 09:48 ET (after the fire), last trade 09:32-09:33 ET |
| bridge market-recap | `market-recap get_quotes` (12 symbols, 1 call) | ok 12/12, market_state=open | as_of 09:46-09:50 ET |
| cron #08 pre-market | `daily-screens/2026-11-10/pre-market-gapper.csv` | ok | 12/12 universe names present; used only to corroborate the pre-market exclusion |
| upstream focus list | `daily-screens/2026-11-09/focus.md` (outputs repo) | ok | 12 names |

## Degradation / caveats

- **The universe is Monday's sweep.** `daily-screens/2026-11-09/focus.md` is the newest focus list on the outputs branch; Tuesday's sweep (#09, 18:30 ET) had not fired. `focus_dir_date` 2026-11-09, screen data date 2026-11-06, `lag_sessions` 1 - the normal case, not a degradation. The roster turnover is the real limitation: 12 of 12 names have no prior-session RVOL reading, so no crossing can be proven and the alert tier is empty by construction rather than by calm tape.
- **7 names are above the 1.5x bar with nothing to compare them against.** That is the headline and the trap at the same time: the level is real and measurable, the crossing is not. Every one of them is published as WATCH, and the next fire's baseline is what turns them into alerts or dismisses them.
- **The trend column compares different window lengths.** rvol_now is a 15-minute window and rvol_prev a 10-minute slot, each normalised against its own history. The delta is directional, not a like-for-like magnitude - this is the same construction as the 2026-11-09 artifact, so the two published trend columns are comparable with each other but neither is a clean acceleration rate.
- **The daily factor runs above 1.0 for 8 of 12 names** (TV's `average_volume_10d_calc` includes today's partial volume and drops the oldest completed session), so their rvol_now is a few percent above a completed-session basis. IONQ, KRMN and OKLO sit at exactly 1.00 and are therefore on the completed-session basis, and RHLD sits below it at 0.94; the series stays comparable with the 2026-11-09 artifact because the same convention was used there.
- **RHLD's baseline is older than everyone else's** (2026-10-19 to 2026-11-06 rather than ending 2026-11-09) because its 2026-11-09 opening bar is zero-volume. Excluding that session rather than using it with a zero is what keeps RHLD's rvol honest; its 0.82x is nowhere near either threshold, so the choice does not change its tier.
- **In-progress and later bars dropped.** No bar stamped after 09:40 ET contributes any volume, and the zero-volume trailing bars were excluded. The fire snapshot is reconstructed at the 09:45 ET stamp from bars that had already closed.
- **rvol_intraday_live** is published for reference only and is mechanically tiny at 09:45 (15 of 390 session minutes). Never bucket on it.
- **Yahoo's 5-minute series undercounts the consolidated tape on full days** (its 78-bar sum runs below Nasdaq's consolidated daily volume, with the gap widest on high-volume days) - the closing auction consolidates after the last 5-minute bar. This does not affect the window ratio (today's window and the prior-10 window means come from the same feed) but it is why the scale factor uses Nasdaq's settled consolidated daily volume rather than the Yahoo bar sum.
- **No near misses and no alerts means this artifact reports a hot, unread tape.** The tier structure is empty on both sides; what it does publish is the level, the trend and the direction of each name's opening pace - and the next session's CSV is what turns any of it into a crossing test.
