---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-05 14:00:56 ET"
data_date: "2026-11-04"
live_date: "2026-11-05"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 909 names"
vix_quote_time: "2026-11-05 13:49:31 ET (Cboe delayed-quote CDN, ~15 min delayed)"
vix_pair: "VIX 26.57 / VIX3M 24.91 (prior close 16.61 / 18.80) — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-05/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-04 · universe 909 names · breadth 69.42% (pctile 94.3 · ABOVE_NORMAL) · divergence +29.42 pp (BROAD) · AD 658/250/1_

# Breadth & Regime Snapshot — Thursday, 05 November 2026 (intraday, cron #10)

The 14:00 ET intraday read for Thursday 05 November 2026. The **settled** breadth layer describes the **2026-11-04** session (shibui is T+1); the **live** tape and the volatility pair describe **2026-11-05 at ~14:05 ET**. Today is a violent risk-off break: the S&P 500 is down ~4%, the Nasdaq 100 down ~5.8%, and the VIX has jumped ~60% to 26.57 — its biggest one-day rise since April 2025. The breadth numbers below therefore describe the posture **before** this break, not the market as it stands now.

## TL;DR

- **Breadth (settled 2026-11-04) was strong** — 69.42% of the 909 large caps closed above their own 20-DMA, a 94.3 percentile in its own 1-year range (ABOVE_NORMAL), with **658 advancing vs 250 declining** (A/D ratio 2.63) and a 10-session net of +805 advances.
- **The divergence is the number that changes position sizing: +29.42 pp (BROAD)** — the average large cap was materially healthier than the cap-weighted index, and the spread has widened across the last four sessions (23.70 → 25.13 → 24.14 → 29.42 pp).
- **The caveat that changes how to read it:** that is yesterday's tape. The live session is in a −4% to −5.8% break with the VIX +60% at 26.57, the regime's `uncertainty` flag is already true (VIX/VIX3M 1.07 > 1), and today's tape has the equal-weight RSP falling 1.16 pp LESS than SPY — the BROAD spread is already unwinding.

## Breadth — 2026-11-04 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 909 |
| Above 20-DMA | 631 (69.42%) |
| Below 20-DMA | 278 (30.58%) |
| Above 50-DMA | 594 (65.35%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40.0%) |
| Index ETFs above their own 50-DMA | 2 of 5 (40.0%) |
| Advance/decline — settled session | 658 advancing / 250 declining / 1 unchanged (A/D ratio 2.632) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **909 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-22 | 538 | 369 | 2 | +169 | -1366 | 102.14 |
| 2026-10-23 | 271 | 636 | 2 | -365 | -1731 | 87.56 |
| 2026-10-26 | 527 | 376 | 6 | +151 | -1580 | 82.33 |
| 2026-10-27 | 465 | 441 | 3 | +24 | -1556 | 72.38 |
| 2026-10-28 | 468 | 436 | 5 | +32 | -1524 | 47.75 |
| 2026-10-29 | 675 | 234 | 0 | +441 | -1083 | 68.92 |
| 2026-10-30 | 377 | 532 | 0 | -155 | -1238 | 69.61 |
| 2026-11-02 | 598 | 311 | 0 | +287 | -951 | 62.83 |
| 2026-11-03 | 360 | 547 | 2 | -187 | -1138 | 63.43 |
| 2026-11-04 | 658 | 250 | 1 | +408 | -730 | 87.36 |

**A/D ratio 2.632 today** (658 advancing / 250 declining). Over the last 10 sessions the net advances total **+805** and the ADL slope is **+87.36 net advances per session** (10-session A/D ratio 1.195). The ADL is cumulative from 2026-08-11, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-21 → 2026-11-04). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 69.42% | — | — |
| `breadth_pctile_1y` | 94.3 | — | ABOVE_NORMAL |
| `breadth_pct_50dma` | 65.35% | — | — |
| `breadth_pctile_1y_50dma` | 88.5 | — | ABOVE_NORMAL |
| `index_etfs_above_20dma` | 2 of 5 | 41.6 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +29.42 pp | BROAD | 83.2 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-10-29 | +29.20 |
| 2026-10-30 | +23.70 |
| 2026-11-02 | +25.13 |
| 2026-11-03 | +24.14 |
| 2026-11-04 | +29.42 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 284.02 | 277.44 | 283.19 | +0.29% | 0.18 |
| QQQ | 691.95 | 717.42 | 723.56 | -4.37% | -2.87 |
| QQQE | 117.38 | 118.60 | 119.58 | -1.84% | -1.47 |
| RSP | 223.33 | 216.32 | 214.99 | +3.88% | 3.84 |
| SPY | 766.81 | 767.57 | 767.06 | -0.03% | -0.03 |

## Live tape — 2026-11-05

Live tape, 2026-11-05 ~14:05 ET. Index levels are from the Cboe delayed-quote CDN
(quote stamp 13:47–13:48 ET, ~15 min delayed); the ETF and sector tape is from the
`market-recap` bridge (14:04:52 ET) and is the fresher print.

| Index | Last | Change | Prior close |
|---|---|---|---|
| S&P 500 (SPX) | 7,383.02 | **-3.97%** | 7,688.62 |
| Nasdaq 100 (NDX) | 26,783.22 | **-5.82%** | 28,437.20 |
| Russell 2000 (RUT) | 2,731.04 | **-4.41%** | 2,856.95 |
| Dow Jones (DJX x100) | 51,727 | **-3.05%** | 53,356 |

| ETF (bridge, 14:04:52 ET) | Last | Change | Prior close | Volume |
|---|---|---|---|---|
| SPY | 734.58 | -4.20% | 766.81 | 68,461,193 |
| QQQ | 650.84 | **-5.94%** | 691.95 | 88,095,825 |
| RSP | 216.53 | -3.04% | 223.33 | 17,579,749 |
| IWM | 270.92 | -4.61% | 284.02 | 34,060,504 |
| QQQE | 111.88 | -4.69% | 117.38 | 266,869 |

**Sector rotation (bridge, 14:04 ET) — every sector is down; the damage is concentrated in
AI and semiconductors.**

| Sector ETF | Change | | Sector ETF | Change |
|---|---|---|---|---|
| XLK (tech) | **-7.35%** | | XLF (financials) | -2.85% |
| XLY (cons. disc.) | -4.54% | | XLV (health care) | -2.08% |
| XLI (industrials) | -4.21% | | XLE (energy) | -1.44% |
| XLB (materials) | -3.38% | | XLU (utilities) | -1.12% |
| | | | XLC (comm. svcs) | -1.08% |
| | | | XLP (staples) | -0.66% |

**The equal-weight index is outperforming the cap-weighted one by 1.16 pp** (RSP -3.04% vs
SPY -4.20%) — the exact opposite of the settled session's BROAD divergence. The megacap leg
is the weak one today, and the BROAD spread that stood at +29.42 pp yesterday is
unwinding from that end. The session is a post-midterm unwind of the crowded AI trade
(chips and data-centre names led down; press reports the VIX's largest one-day jump since
April 2025), and there is **no FOMC meeting today** — the last was 27–28 October, the next
is 8–9 December.

## Volatility — single pair, live

| Metric | Value | Change | Prior close |
|---|---|---|---|
| VIX | **26.57** | +59.96% | 16.61 |
| VIX3M | 24.91 | +32.50% | 18.80 |
| VIX / VIX3M | 1.067 | — | 0.884 |

One pair, one source: **Cboe delayed-quote CDN** (`_VIX.json` / `_VIX3M.json`), quote stamp
**2026-11-05 13:49:31 ET**, session mode *regular hours — live print*. The pair was
pulled twice and the two pulls agreed exactly (`vix_stable: true`), so the number is stable on
this feed. The ratio at **1.067** is above 1.0, which is what sets the
regime's `uncertainty` flag to true — the front end of the curve is now priced for more
near-term volatility than the three-month view.

This is the same pair that drives the `uncertainty` flag in `_regime-intraday.json`; no other
volatility reading appears anywhere in this document.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **SPY — the two live feeds disagree, because the tape is still moving.** The Cboe delayed
  print is 735.93 @ 13:47:00 ET; the `market-recap` bridge is 734.58 @ 14:04:52 ET — 0.19%
  apart. The bridge is the fresher print; the Cboe index levels carry a ~15-minute lag.
- **VIX — the published print lags the session.** 26.57 is the 13:49:31 ET delayed quote;
  press reports an intraday high of 28.09 later in the session. The published pair is the
  delayed print, **not** the session high, and it is used everywhere unchanged.
- **SPY — its 20-DMA membership is marginal.** On the settled session SPY closed 766.81 against
  its own 20-DMA of 767.57 — **0.10% below** — so the index-ETF count (2 of 5 above their
  20-DMA) turns on a rounding-level move in SPY. Treat that count as a 2-of-5 with the
  third slot inside noise.
- **QQQ — the index's weak leg was already in place.** QQQ closed 4.37% **below** its own
  50-DMA on the settled session (691.95 vs 723.56) while the broad universe sat 69.42% above
  its 20-DMA. Today's −5.94% extends a weakness that the breadth table does not show.

## Method, source health & caveats

- **Settled layer (2026-11-04) — shibui via the MCP-over-HTTP bridge.** Three paged SQL
  queries (the large-cap breadth series, the index-ETF series, the advance/decline series),
  262 sessions from 2025-10-21 to 2026-11-04, every query answered. The advance/decline tally
  uses the **same** indicator-joined population as the breadth percentage, so
  advancing + declining + unchanged (658 + 250 + 1 = 909) equals the published universe count.
- **Live layer (2026-11-05) — Cboe delayed-quote CDN + the `market-recap` bridge.** The Cboe
  CDN carries the VIX/VIX3M pair (pulled twice, stable) and the index levels (13:47–13:48 ET);
  the bridge carries the ETF and sector tape (14:04:52 ET). The Cboe feed runs ~15 minutes
  behind the bridge feed, which is stated wherever the two are compared.
- **Universe — not frozen.** NYSE/NASDAQ/AMEX with market cap > $10B taken from the **latest**
  `valuation` row. Today's count is **909 names**, unchanged across the trailing 30 sessions;
  it moved earlier in November (904 → 902 → 905 → 909) as those rows refreshed, so the count is
  republished every run. The universe itself was **not** changed — that would break the series.
- **Settled vs live are never blended.** The breadth numbers, the ADL and the index positioning
  describe the 2026-11-04 close; the tape and the volatility pair describe 2026-11-05 at
  ~14:05 ET. They are two fields, two sections, two labels.
- **Percentile windows.** `breadth_pctile_1y` is an expanding rank against every session from
  the start of the 262-session window to that row; the divergence history is the last 5 dated
  sessions. The ADL is a **level** cumulative from 2026-08-11 (the first session of the A/D
  series, ~60 sessions back) and the 10-session slope is its **rate**.
- **`atr_extensions` note.** The "ATR multiple" column in the index-positioning table is
  (close − 50-DMA) ÷ ATR(14), **not** a true 252-day median comparison: the breadth SQL
  computes its ATR average inside a single-date CTE, so that window holds exactly one row and
  the average collapses to the current ATR. The regime payload's `atr_extensions` is therefore
  a distance from the 50-DMA in percent, and `late_cycle` is computed on that.
- **Event context.** No FOMC meeting today — the last was 27–28 October 2026 and the next is
  8–9 December. The session is a post-midterm unwind of the AI trade, and the volatility
  print is a live intraday one, not a settled close.
- **Degraded probes: none.** `probe_mcp.py` → `catalog_ok total=135 finance_tools=0` — no
  finance MCP is registered on this runtime, so the MCP-over-HTTP bridge is the finance path
  and it answered every call.
