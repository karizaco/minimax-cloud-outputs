---
date: 2026-11-04
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
fire_date: 2026-11-04
focus_dir_date: 2026-11-03
screen_data_date: 2026-11-02
lag_sessions: 1
universe_source: upstream_focus_list
universe_size: 12
elapsed_minutes: 15
session_fraction: 0.0385
source: Yahoo chart API 5m bars (session volume + close, includePrePost=false) + TradingView america scanner (average_volume_10d_calc) + bridge market-recap get_quotes (live price cross-check) + Cboe delayed-quote CDN (session-volume cross-check) + cron #08 pre-market-gapper.csv (pre-market volume)
method: rvol_tod_normalised time-of-day-normalised intraday RVOL; session volume = Yahoo 5m bars 09:30-09:45 ET (last completed bar at the fire, in-progress bar dropped); denominator = TradingView average_volume_10d_calc
metric_def: rvol_tod_normalised = (session volume 09:30-09:45 today / mean same-window volume over the prior 10 sessions) x (mean full-day volume over those prior 10 sessions / TV average_volume_10d_calc); rvol_intraday_live = cumulative session volume to the last completed bar / TV average_volume_10d_calc
bucket_rule: rvol_tod_normalised >= 1.5 -> RVOL Required, otherwise Liquid
status: ok
upstream: daily-screens/2026-11-03/focus.md
names_unpriced: 0
---

# Focus RVOL snapshot - 2026-11-04 09:45 ET (cron #07)

**Headline:** 4 of 12 focus names are running hot against their own 10-session norm for this clock window - **CVNA 2.01x**, **CLF 1.74x**, **VSEC 1.62x**, **FIGS 1.54x**. The hottest is **CVNA at 2.01x** on 1,555,831 shares in the first 15 minutes.

**Caveat that changes how this reads:** `rvol_intraday_live` is published beside every number and it is mechanically tiny (0.03-0.13x) because only 15 of 390 session minutes have elapsed - it CANNOT reach 1.5 before the lunch bell for any name. Bucket on `rvol_tod_normalised` only. The raw ratio is not a verdict.

## Universe

12 names from `daily-screens/2026-11-03/focus.md` - the most recent completed 18:30 ET sweep (Tue 2026-11-03, 12 names). `focus_dir_date` = 2026-11-03; the sweep's own `Screen data_date` = **2026-11-02** (shibui T+1), read from the focus.md header, not inferred. `lag_sessions` = **1** trading session (2026-11-03) between that screen data date and this fire - the normal weekday T+1 ingest, not a degradation.

## Table - sorted by rvol_tod_normalised desc

| symbol | close | rvol_intraday_live | rvol_tod_normalised | bucket | data timestamp |
|---|---:|---:|---:|---|---|
| CVNA | 75.225 | 0.1272 | 2.014 | RVOL Required | 2026-11-04 09:45 ET |
| CLF | 13.720 | 0.1064 | 1.738 | RVOL Required | 2026-11-04 09:45 ET |
| VSEC | 166.535 | 0.0837 | 1.622 | RVOL Required | 2026-11-04 09:45 ET |
| FIGS | 22.145 | 0.0652 | 1.544 | RVOL Required | 2026-11-04 09:45 ET |
| KVYO | 21.765 | 0.0620 | 1.317 | Liquid | 2026-11-04 09:45 ET |
| FTAI | 191.550 | 0.0843 | 1.204 | Liquid | 2026-11-04 09:45 ET |
| TEM | 80.650 | 0.1019 | 0.955 | Liquid | 2026-11-04 09:45 ET |
| WING | 170.250 | 0.0740 | 0.942 | Liquid | 2026-11-04 09:45 ET |
| CAI | 34.005 | 0.0405 | 0.804 | Liquid | 2026-11-04 09:45 ET |
| MRNA | 246.701 | 0.0987 | 0.767 | Liquid | 2026-11-04 09:45 ET |
| HTFL | 55.965 | 0.0441 | 0.712 | Liquid | 2026-11-04 09:45 ET |
| KOD | 100.390 | 0.0282 | 0.432 | Liquid | 2026-11-04 09:45 ET |

### Counts

- Focus tickers: **12**
- RVOL Required (rvol_tod_normalised >= 1.5): **4** - CVNA 2.01x, CLF 1.74x, VSEC 1.62x, FIGS 1.54x
- Liquid: **8** - KVYO 1.32x, FTAI 1.20x, TEM 0.95x, WING 0.94x, CAI 0.80x, MRNA 0.77x, HTFL 0.71x, KOD 0.43x
- Crossings (prior reading < 1.5, today >= 1.5): **4** - CVNA, CLF, VSEC, FIGS

## Alerts

**4 names crossed the 1.5 bar this session:**

- **CVNA** - 2.01x vs 0.66x on the prior session (1,555,831 shares in 09:30-09:45 vs a 791,791-share mean for that same window), close 75.23
- **CLF** - 1.74x vs 1.07x on the prior session (2,202,847 shares in 09:30-09:45 vs a 1,334,296-share mean for that same window), close 13.72
- **VSEC** - 1.62x vs 0.23x on the prior session (37,964 shares in 09:30-09:45 vs a 20,906-share mean for that same window), close 166.53
- **FIGS** - 1.54x vs 1.02x on the prior session (217,319 shares in 09:30-09:45 vs a 140,200-share mean for that same window), close 22.14

**Baseline provenance - read this before trusting the crossing list.** The routine's designated baseline is `daily-screens/<previous session>/focus-rvol-snapshot.csv`. **That file does not exist for 2026-11-03** - the 2026-11-03 run published only a `.md`, and its `RVOL` column is the SUPERSEDED pace-adjusted metric with a 3x bucket bar, which is a different quantity from `rvol_tod_normalised` and cannot be compared to it. The prior readings used above were therefore **recomputed from the same Yahoo 5-minute series with the identical formula**, on the 2026-11-03 session, using its own trailing-10 baseline and the same TradingView denominator. Both sides of every crossing comparison are the same metric computed the same way on the same source - this is a real prior reading, not a fabricated one, but it is a recomputation and not a value read from a published artifact. This run writes `focus-rvol-snapshot.csv` so the next fire has a native prior reading to compare against.

## Universe change

Versus the previous sweep (`daily-screens/2026-11-02/focus.md`, 12 names). The roster turns over almost completely between sweeps - only 4 of 12 names carry over - so this screen is a different set of names from the last one, not a re-rank of the same set.

- Entered (8): CLF, CVNA, FIGS, FTAI, KVYO, TEM, VSEC, WING
- Left (8): ABCL, CDNA, CVI, LQDA, MTZ, NOW, PURR, QLYS
- Retained (4): CAI, HTFL, KOD, MRNA

## Method

1. **Session volume** - Yahoo chart API, one call per symbol, `interval=5m&range=1mo&includePrePost=false`. The `includePrePost=false` flag matters: it returns regular-session bars only (78 bars per session, first stamped 09:30), so no pre-market print leaks into the numerator. Session volume for the fire window = the sum of the three bars stamped 09:30, 09:35 and 09:40 ET. The bar stamped 09:45 is IN PROGRESS at the 09:45 fire and its volume is not yet settled, so it was DROPPED; the window ends at the last COMPLETED bar (09:40, covering 09:40-09:45).
2. **The denominator** - TradingView america scanner, one full-universe pull (20,000 rows, `range:[0,20000]`, `sort` by name, filter locally), column `average_volume_10d_calc`. TradingView supplies the denominator only; its LIVE columns lag the session and were not used for any live field.
3. **rvol_tod_normalised** - today's 09:30-09:45 volume divided by the mean 09:30-09:45 volume over the prior 10 sessions (same clock window each day, summed from the same Yahoo series), multiplied by the mean full-day volume over those same 10 sessions divided by TV's `average_volume_10d_calc`. The last factor puts the number in the same units as cron #09's completed-session relative volume, so the two are directly comparable. 1.0 = a normal morning for that name; 1.5 = 50% hotter than its own 10-session norm at this hour.
4. **Why not time-scaled** - dividing by elapsed TIME assumes volume accrues evenly across the session. It does not: the first 15 minutes of a session carry a median ~8% of the day's volume against 3.8% for time-even accrual, so a time-scaled projection over-states the session by roughly 2x. `rvol_intraday_live` is published alongside as the raw ratio, but the bucket uses the time-of-day-normalised form.
5. **Crossings** - a name crosses when its prior-session `rvol_tod_normalised` was < 1.5 and today's is >= 1.5 (see Baseline provenance above for exactly what the prior reading is).

## Source health

| source | query / URL | status | result |
|---|---|---|---|
| Yahoo chart API | `query2.finance.yahoo.com/v8/finance/chart/{SYM}?interval=5m&range=1mo&includePrePost=false` | 200 | ok - 12/12 symbols, ~1,725 bars each, ~23 sessions |
| Yahoo chart API (fallback host) | `query1.finance.yahoo.com/...` | - | not needed - query2 answered on the first attempt |
| TradingView scanner | `POST scanner.tradingview.com/america/scan`, `range:[0,20000]`, `sort` by name | 200 | ok - 20,000 rows returned, totalCount 20,010; filtered locally (a `name in [...]` filter returns HTTP 400 on this endpoint) |
| Bridge `market-recap get_quotes` | `mcp_bridge.py market-recap get_quotes` (12 symbols, 1 call) | 200 | ok - 12/12 found, `market_state: open` on 12/12 |
| Bridge price vs Yahoo price (matched timestamps) | 12 pairs | - | ok - max divergence 0.28%, 12/12 inside the 0.6% tolerance |
| Cboe delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | 200 | ok - 12/12; session-only volume vs Yahoo cumulative at the SAME timestamp: median -3.6%, worst -13.8% (TEM), 2/12 outside 10% |
| cron #08 pre-market-gapper.csv | `daily-screens/2026-11-04/pre-market-gapper.csv` | - | ok - 12/12 tickers present; used only to subtract pre-market from the bridge's gross volume |

**Source selection and the one deviation.** Prices and session volume come from the Yahoo chart series, one source per field. The bridge `market-recap` is the cross-check for price, not the publisher: its live quote is a moving tape and the pull for this run landed ~40 minutes after the fire, so publishing it as `close` would pair a 10:25 ET price with a 09:45 ET volume and make the row incoherent. The published `close` is therefore the 09:40-stamped bar's close - the price at the 09:45 window boundary, the same instant as the published volume. At matched timestamps the two sources agreed within 0.28% on 12/12 names, so the choice costs nothing in accuracy.

**Pre-market is excluded twice over.** The Yahoo bars carry `includePrePost=false` (no pre-market bars at all) and the bridge's gross cumulative volume, which DOES include pre-market, was reduced by cron #08's published pre-market volume before being used as a cross-check. The bridge's remaining gap versus Yahoo's regular-session bars is the pre-market print plus a different consolidation basis.

## Degradation

None material. Two caveats carried forward:

1. **The upstream focus list carries a 1-session screen-data lag** (`Screen data_date: 2026-11-02` vs the sweep's 2026-11-03 prices). This is the documented shibui T+1 behaviour and stays inside the `lag_sessions <= 1` threshold, so status is `ok`. It does mean the roster was selected on 2026-11-02 metrics.
2. **The previous session's baseline CSV is missing** (see Baseline provenance). The crossing list is sound but it rests on a recomputed prior reading rather than a published artifact value. This run writes the CSV so 2026-11-05 has a native baseline.

---

Generated by cron #07 at 2026-11-04 09:45 ET (scheduled_at_ms 1793803515169). Fire date resolved from the scheduled instant, not the wall clock. 12 tickers priced, 0 unpriced, 0 source errors.
