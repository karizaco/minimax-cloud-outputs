---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-10 14:00:53 ET"
data_date: "2026-11-09"
live_date: "2026-11-10"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 911 names"
vix_quote_time: "2026-11-10T13:50:31 (Cboe delayed-quote CDN; regular hours — live print)"
vix_pair: "VIX 20.42 / VIX3M 21.31 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-10/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-09 · universe 911 names · breadth 67.84% (pctile 90.8 · ABOVE_NORMAL) · divergence +27.84 pp (BROAD) · AD 765/143/3_

# Breadth & Regime Snapshot — Tuesday, 10 November 2026 (intraday, cron #10)

Intraday breadth read, fired 2026-11-10 14:00:53 ET on 2026-11-10. The breadth numbers below describe the *settled* 2026-11-09 session (shibui is T+1); the live tape and the volatility pair are *live* 2026-11-10. Universe: NYSE/NASDAQ/AMEX, market cap > $10B — **911 names**. Source of record for prices and movers: the market-recap MCP-over-HTTP bridge; breadth and advance/decline: shibui over the same bridge.

## TL;DR

- **Breadth 67.84%** of the 911-name large-cap universe above its own 20-DMA on the 2026-11-09 settled session (261 sessions of history) — 1-year percentile **90.8**, band **ABOVE_NORMAL**; 64.43% above the 50-DMA.
- **Divergence +27.84 pp (BROAD)** — the average large cap is materially healthier than the index — participation is broader than the headline index and the index's own posture is the weak leg; the spread's own 1-year percentile is 79.3, and the settled A/D tally was **765 advancing / 143 declining / 3 unchanged** (ratio 5.35).
- **Caveat:** the breadth numbers are the *settled* 2026-11-09 session (shibui settles T+1), while the live tape and the volatility pair in this document are *live* on 2026-11-10 — the two layers are never blended; this fire's own end-of-day counterpart is `daily-screens/2026-11-10/breadth.md` (cron #09, 18:30 ET).

## Breadth — 2026-11-09 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 911 |
| Above 20-DMA | 618 (67.84%) |
| Below 20-DMA | 293 (32.16%) |
| Above 50-DMA | 587 (64.43%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40.0%) |
| Index ETFs above their own 50-DMA | 2 of 5 (40.0%) |
| Advance/decline — settled session | 765 advancing / 143 declining / 3 unchanged (A/D ratio 5.35) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **911 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-27 | 470 | 438 | 3 | +32 | -1862 | 73.49 |
| 2026-10-28 | 473 | 433 | 5 | +40 | -1822 | 49.68 |
| 2026-10-29 | 674 | 236 | 1 | +438 | -1384 | 71.23 |
| 2026-10-30 | 374 | 537 | 0 | -163 | -1547 | 71.63 |
| 2026-11-02 | 595 | 316 | 0 | +279 | -1268 | 64.0 |
| 2026-11-03 | 362 | 547 | 2 | -185 | -1453 | 63.95 |
| 2026-11-04 | 657 | 253 | 1 | +404 | -1049 | 87.38 |
| 2026-11-05 | 154 | 755 | 2 | -601 | -1650 | 79.09 |
| 2026-11-06 | 389 | 516 | 6 | -127 | -1777 | 39.24 |
| 2026-11-09 | 765 | 143 | 3 | +622 | -1155 | 40.35 |

**A/D ratio 5.35 today** (765 advancing / 143 declining). Over the last 10 sessions the net advances total **+739** and the ADL slope is **+40.35 net advances per session** (10-session A/D ratio 1.177). The ADL is cumulative from 2026-08-14, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (261 sessions, 2025-10-27 → 2026-11-09). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 67.84% | — | — |
| `breadth_pctile_1y` | 90.8 | — | ABOVE_NORMAL |
| `breadth_pct_50dma` | 64.43% | — | — |
| `breadth_pctile_1y_50dma` | 82.4 | — | ABOVE_NORMAL |
| `index_etfs_above_20dma` | 2 of 5 | 42.9 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +27.84 pp | BROAD | 79.3 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-03 | +24.00 |
| 2026-11-04 | +29.15 |
| 2026-11-05 | +38.29 |
| 2026-11-06 | +56.20 |
| 2026-11-09 | +27.84 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 282.51 | 277.07 | 281.84 | +0.24% | 0.15 |
| QQQ | 679.35 | 704.30 | 720.23 | -5.68% | -3.68 |
| QQQE | 115.54 | 117.36 | 119.00 | -2.91% | -2.3 |
| RSP | 220.95 | 217.11 | 214.79 | +2.87% | 2.83 |
| SPY | 752.69 | 762.09 | 765.35 | -1.65% | -1.6 |

## Live tape — 2026-11-10

Live tape, intraday — the 2026-11-10 session is still open. These are LIVE prices, not settled closes, and they are never blended with the settled breadth numbers above.

| Index / ETF | Last | Change | Previous close |
|---|---|---|---|
| SPY | 748.16 | -0.60% | 752.69 |
| QQQ | 671.64 | -1.13% | 679.35 |
| IWM | 280.02 | -0.88% | 282.51 |
| RSP | 220.54 | -0.19% | 220.95 |
| QQQE | 114.54 | -0.87% | 115.54 |

| Sector / theme ETF | Last | Change | Previous close |
|---|---|---|---|
| XLK | 168.13 | -1.61% | 170.88 |
| XLF | 58.34 | +0.60% | 57.99 |
| XLE | 62.25 | +0.50% | 61.94 |
| XLV | 188.34 | +0.01% | 188.33 |
| XLY | 120.69 | -0.26% | 121.01 |
| XLP | 91.19 | +0.33% | 90.89 |
| XLU | 43.70 | -0.19% | 43.79 |
| XLI | 168.16 | -0.43% | 168.89 |
| XLB | 52.77 | -0.31% | 52.94 |
| SMH | 480.63 | -1.39% | 487.41 |
| XBI | 154.68 | -1.42% | 156.90 |

Source: market-recap `get_quotes` over the MCP-over-HTTP bridge, retrieved 2026-11-10T19:05:05.813Z (all 16 symbols found, market_state=open).

## Volatility — single pair, live

| Instrument | Last | Previous close | Change |
|---|---|---|---|
| VIX | 20.42 | 19.92 | 2.51% |
| VIX3M | 21.31 | 20.85 | 2.2062% |

**One pair, used everywhere in this document:** VIX 20.42 / VIX3M 21.31 (ratio 0.958), quoted 2026-11-10T13:50:31 ET from the Cboe delayed-quote CDN (`_VIX.json` / `_VIX3M.json`).

Quote mode: regular hours — live print. The pair was pulled twice and `vix_stable: true` — a disagreement between the two pulls would be published here rather than hidden behind one number.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **Universe drift:** the large-cap count is **911 names** this session (the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh — 904 → 902 → 905 → 909 → 911 across five November sessions). A change in the count moves the breadth percentage slightly, so the level is only comparable within a stable count.
- **Volatility pair:** one VIX/VIX3M pair is used in the front matter, the volatility section and the regime payload; no second volatility reading appears anywhere in this document.
- **Regime flag plumbing:** `atr_extensions` is populated with 5 index ETFs (IWM +0.24%, QQQ -5.68%, QQQE -2.91%, RSP +2.87%, SPY -1.65%), so `late_cycle` is a computed value and not a flag that could never fire.

## Method, source health & caveats

| Source | Endpoint / query | Status |
|---|---|---|
| MCP availability probe | `_shared/probe_mcp.py` | `catalog_ok total=135 finance_tools=0 · bridge bridge_ok packs=tradier,fmp,market-recap` |
| shibui (breadth, A/D, index ETFs, ATR extensions) | `shibui stock_data_query` over the MCP-over-HTTP bridge | ok — 6 calls, every paged series asserted `rows_kept == rows_passing` |
| Live tape | `market-recap get_quotes` over the bridge, 16 symbols | ok — 16/16 found, market_state=open, retrieved 2026-11-10T19:05:05.813Z |
| Volatility pair | Cboe delayed-quote CDN `_VIX.json` / `_VIX3M.json` | ok — pulled twice, `vix_stable: true` |

- **Settled vs live.** Breadth, the advance/decline tally, the percentile and the divergence describe the *settled* 2026-11-09 session. The tape and the volatility pair are *live* 2026-11-10. They are published in separate sections and separate front-matter fields (`data_date` vs `live_date`) and are never combined.
- **Universe.** NYSE/NASDAQ/AMEX, market cap > $10B — **911 names** on the data date, computed on the indicator-joined large-cap set, which is the same population the advance/decline tally uses (advancing + declining + unchanged = 911). The universe is not frozen; the count is published every run.
- **Percentile windows.** `breadth_pctile_1y` is the inclusive rank of the level in its own trailing distribution (261 sessions, 2025-10-27 → 2026-11-09); the CSV's percentile columns are expanding.
- **Advance/decline.** The tally is a `LAG()` self-join over `stock_quotes` on the same universe, so it is a real tally and not an estimate. The ADL is a level cumulative from 2026-08-14; the published slope is +40.35 net advances per session over 2026-10-27 → 2026-11-09.
- **`atr_extensions`.** Populated with 5 rows (IWM, QQQ, QQQE, RSP, SPY); the index identifier is read from `ticker`, which is what the breadth SQL emits.
- **Regime flags.** `size_cut_pct` 0 (size cut requires the index below its 20-DMA **and** breadth < 40%), `uncertainty` false (VIX/VIX3M > 1.0), `late_cycle` false (any index ETF > 6% above its own 50-DMA).
- **Endpoint of day.** The end-of-day counterpart — the settled-close read of 2026-11-10 — is cron #09's `daily-screens/2026-11-10/breadth.md` at 18:30 ET, and it will quote different VIX quote times and a different universe count. This file is the intraday read and is authoritative for the 14:00 ET fire.

degraded_sources: 0
