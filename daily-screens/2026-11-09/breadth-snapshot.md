---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-09 14:00:54 ET"
data_date: "2026-11-06"
live_date: "2026-11-09"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 895 names"
vix_quote_time: "2026-11-09 13:46:31 ET (Cboe delayed-quote CDN, regular-hours live print)"
vix_pair: "VIX 20.14 / VIX3M 21.14 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-06/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-06 · universe 895 names · breadth 56.42% (pctile 51.2 · NORMAL) · divergence +56.42 pp (BROAD) · AD 378/511/6_

# Breadth & Regime Snapshot — Monday, 09 November 2026 (intraday, cron #10)

**Monday, 9 November 2026 — the 14:00 ET fire, taken on a live (session-open) tape.** The settled breadth layer below describes **Friday 6 November 2026**, shibui's newest ingested session; the live tape and the volatility pair are **today**. The two layers are never blended into one number. Source of record for the settled layer: shibui-finance over the MCP-over-HTTP bridge. Source of record for the live tape: the `market-recap` bridge for the ETFs (14:03 ET) and the Cboe delayed-quote CDN for the indices and the volatility pair (13:46 ET).

## TL;DR

- **Breadth was middling, not healthy.** 56.42% of the 895 large caps closed Friday above their own 20-DMA — a percentile of 51.2 in its own trailing year, a `NORMAL` reading.
- **The divergence is the story: +56.42 pp (`BROAD`), at a 1-year percentile of 100.0.** The average large cap was far healthier than the index — 0 of 5 index ETFs sat above their own 20-DMA (a percentile of 15.0), so on Friday the megacaps were the WEAK leg, not the strong one.
- **Caveat that changes how you read it:** the settled layer is Friday's close, and today's tape is a violent broad rally that has not entered those numbers yet — RSP +2.53% ahead of SPY +2.39%, IWM +3.22%, VIX collapsing from 25.64 to 20.14. The extreme divergence percentile comes from the INDEX leg being weak, not from the broad leg being strong.

## Breadth — 2026-11-06 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 895 |
| Above 20-DMA | 505 (56.42%) |
| Below 20-DMA | 390 (43.58%) |
| Above 50-DMA | 501 (55.98%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 378 advancing / 511 declining / 6 unchanged (A/D ratio 0.74) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **895 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-26 | 516 | 375 | 4 | +141 | -1786 | 81.59 |
| 2026-10-27 | 457 | 435 | 3 | +22 | -1764 | 71.08 |
| 2026-10-28 | 461 | 429 | 5 | +32 | -1732 | 46.39 |
| 2026-10-29 | 665 | 230 | 0 | +435 | -1297 | 66.81 |
| 2026-10-30 | 375 | 520 | 0 | -145 | -1442 | 68.1 |
| 2026-11-02 | 587 | 308 | 0 | +279 | -1163 | 61.64 |
| 2026-11-03 | 352 | 541 | 2 | -189 | -1352 | 62.16 |
| 2026-11-04 | 649 | 245 | 1 | +404 | -948 | 85.69 |
| 2026-11-05 | 154 | 739 | 2 | -585 | -1533 | 78.99 |
| 2026-11-06 | 378 | 511 | 6 | -133 | -1666 | 40.79 |

**A/D ratio 0.74 today** (378 advancing / 511 declining). Over the last 10 sessions the net advances total **+261** and the ADL slope is **+40.79 net advances per session** (10-session A/D ratio 1.06). The ADL is cumulative from 2026-08-13, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (260 sessions, 2025-10-27 → 2026-11-06). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 56.42% | — | — |
| `breadth_pctile_1y` | 51.2 | — | NORMAL |
| `breadth_pct_50dma` | 55.98% | — | — |
| `breadth_pctile_1y_50dma` | 50.0 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 15.0 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +56.42 pp | BROAD | 100.0 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-02 | +25.36 |
| 2026-11-03 | +24.25 |
| 2026-11-04 | +29.39 |
| 2026-11-05 | +38.66 |
| 2026-11-06 | +56.42 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 273.67 | 276.84 | 282.11 | -2.99% | -1.86 |
| QQQ | 656.10 | 707.64 | 720.97 | -9.00% | -5.86 |
| QQQE | 112.01 | 117.63 | 119.14 | -5.98% | -4.75 |
| RSP | 216.05 | 216.72 | 214.78 | +0.59% | 0.58 |
| SPY | 735.29 | 763.36 | 765.68 | -3.97% | -3.84 |

## Live tape — 2026-11-09

| Instrument | Last | Chg % | Quote time (ET) | Source |
|---|---:|---:|---|---|
| SPY | 752.90 | +2.39% | 14:03 | `market-recap` bridge |
| RSP | 221.51 | +2.53% | 14:03 | `market-recap` bridge |
| QQQ | 677.86 | +3.32% | 14:03 | `market-recap` bridge |
| QQQE | 115.65 | +3.25% | 14:03 | `market-recap` bridge |
| IWM | 282.48 | +3.22% | 14:03 | `market-recap` bridge |
| S&P 500 (SPX) | 7,552.69 | +2.38% | 13:46 | Cboe delayed-quote CDN |
| Nasdaq 100 (NDX) | 27,868.18 | +3.25% | 13:46 | Cboe delayed-quote CDN |
| Russell 2000 (RUT) | 2,838.06 | +3.05% | 13:46 | Cboe delayed-quote CDN |
| Dow (DJX) | 524.12 | +2.20% | 13:46 | Cboe delayed-quote CDN |

Equal weight (RSP +2.53%) is ahead of the cap-weighted SPY (+2.39%) and the small-caps are up +3.22% — this is a broad rally, not a megacap-led one, which is the direct counterpart to Friday's divergence. The Cboe delayed-quote CDN's own ETF prints, taken at 13:45 ET, agree with the bridge on every name to within 0.11%.

## Volatility — single pair, live

| Measure | Last | Prior close | Chg % | Quote time (ET) |
|---|---:|---:|---:|---|
| VIX | 20.14 | 25.64 | -21.45% | 13:46:31 |
| VIX3M | 21.14 | 24.60 | -14.07% | 13:46:31 |

VIX/VIX3M = **0.953** — below 1.0, so the `uncertainty` regime flag is **false**. The prior close is derived as `close - price_change` and cross-checked against the CDN's own `prev_day_close` field; both agree on both legs. This is ONE pair, quoted from the Cboe delayed-quote CDN during regular hours (the live print, not a settle), and it is the only volatility reading used anywhere in this document.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **The volatility print is live, not a settle.** The metrics engine pulled the pair twice inside the same trade stamp (13:46:31 ET) and the two agreed — `vix_stable: true`. An independent re-pull at 13:47:31 ET printed marginally lower, so the print is drifting intraday; the published pair is the 13:46:31 quote and the regime implication (VIX below VIX3M, `uncertainty` false) is unchanged either way.
- **QQQ is the most stretched index leg.** Its settled close sits **-9.00%** below its own 50-DMA — a 5.86 ATR extension below — against SPY -3.97%, IWM -2.99%, QQQE -5.98% and RSP +0.59%. The 0-of-5 index-ETF reading above the 20-DMA is driven by this leg.
- **The extreme divergence percentile belongs to the INDEX leg, not the broad leg.** The broad market's 56.42% is only a percentile of 51.2 in its own year, while the index-ETF share above the 20-DMA sits at a percentile of 15.0. Read `100.0` as 'the index is unusually weak', not 'the average stock is unusually strong'.

## Method, source health & caveats

| Source | Endpoint / query | Status |
|---|---|---|
| shibui-finance (settled layer) | MCP-over-HTTP bridge, `shibui.stock_data_query` — breadth series, index-ETF series, advance/decline series, ETF ATR extension | ok |
| Cboe delayed-quote CDN (volatility + indices) | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json`, `_VIX3M.json`, `_SPX.json`, `_NDX.json`, `_RUT.json`, `_DJX.json` | ok (HTTP 200 × 6) |
| `market-recap` bridge (ETF tape) | `get_quotes` on SPY, QQQ, IWM, RSP, QQQE | ok |
| Cboe delayed-quote CDN (ETF corroboration) | `quotes/SPY.json`, `QQQ.json`, `IWM.json`, `RSP.json`, `QQQE.json` | ok (HTTP 200 × 5) |
| MCP availability probe | `catalog_ok total=135 finance_tools=0` — no finance MCP registered on this runtime; bridge packs tradier, fmp, market-recap | ok (informational) |

**Two layers, two dates.** The settled breadth layer is Friday **2026-11-06** (shibui's newest ingested session at or before the fire date — shibui is T+1). The live tape and the volatility pair are **2026-11-09**, mid-session. The two are reported in separate sections and never merged into one number.

**Universe.** NYSE/NASDAQ/AMEX, market cap > $10B, **895 names**, taken from the latest `valuation` row. The universe is not frozen — it has moved across recent sessions (895 through the last 15 published sessions; earlier November prints ran 902–909). The advance/decline tally uses the SAME indicator-joined population as the breadth percentage, so advancing + declining + unchanged = 378 + 511 + 6 = 895.

**Percentile windows.** 260 sessions, 2025-10-27 → 2026-11-06. Each percentile is expanding — every session from the start of the window up to that row.

**ATR extensions.** Non-empty — all five index ETFs (SPY, RSP, QQQ, QQQE, IWM) carry a `ticker`-keyed extension, so `late_cycle` was actually computed rather than defaulted to false by the empty-map trap.

**Regime.** `size_cut_pct: 0` because the size cut needs the index below its 20-DMA **and** breadth below 40%; breadth is 56.42%, so the index-below-20-DMA condition on its own does not trigger it. `index_below_20sma: true` (0 of 5 index ETFs above their own 20-DMA) and `uncertainty: false` (VIX/VIX3M 0.953) are independent of the size cut.

**Degraded sources.** None. `degraded_sources: 0`.
