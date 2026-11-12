---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-12 14:00:56 ET"
data_date: "2026-11-11"
live_date: "2026-11-12"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 914 names"
vix_quote_time: "2026-11-12 13:49:31 ET (Cboe delayed-quote CDN)"
vix_pair: "VIX 18.02 / VIX3M 19.66 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-12/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-11 · universe 914 names · breadth 69.37% (pctile 94.3 · ABOVE_NORMAL) · divergence +9.37 pp (MATCHED) · AD 594/315/5_

# Breadth & Regime Snapshot — Thursday, 12 November 2026 (intraday, cron #10)

Intraday breadth & regime read — fired 2026-11-12 14:00:56 ET. The settled layer describes the **2026-11-11** session (shibui is T+1); the tape and the volatility pair are **live 2026-11-12**. Source of record for the tape: the MCP bridge (`market-recap`); for the settled breadth series: the bridge's shibui pack; for the volatility pair: the Cboe delayed-quote CDN.

## TL;DR

- **Breadth is strong, but less so than a week ago** — **69.37%** of the **914-name** large-cap universe closed above its own 20-DMA on the 2026-11-11 settled session (64.99% above the 50-DMA). The 1-year percentile is **94.3**, band **ABOVE_NORMAL**.
- **The divergence collapsed, and that is the finding** — breadth minus the index ETFs' share is **+9.37 pp**, band **MATCHED** (1-year percentile 61.5). It was **+26.96 pp (BROAD)** on the 2026-11-10 session and **+55.80 pp** on 2026-11-06, so the broad market's edge over the index has compressed in three sessions — the early-November megacap-leadership signature has faded back to agreement.
- **Read the settled layer as yesterday's posture, not today's tape** — the numbers describe **2026-11-11** (shibui is T+1), and today's live session is softer and narrower: RSP -0.57% vs SPY -0.23%, IWM -1.42%, XBI -2.58%, with the VIX +3.03% to 18.02. The settled breadth is healthy; the live tape is rotating defensively.

## Breadth — 2026-11-11 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 914 |
| Above 20-DMA | 634 (69.37%) |
| Below 20-DMA | 280 (30.63%) |
| Above 50-DMA | 594 (64.99%) |
| Index ETFs above their own 20-DMA | 3 of 5 (60.0%) |
| Index ETFs above their own 50-DMA | 2 of 5 (40.0%) |
| Advance/decline — settled session | 594 advancing / 315 declining / 5 unchanged (A/D ratio 1.886) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **914 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-29 | 675 | 239 | 0 | +436 | -893 | 70.49 |
| 2026-10-30 | 376 | 537 | 1 | -161 | -1054 | 71.65 |
| 2026-11-02 | 595 | 319 | 0 | +276 | -778 | 64.63 |
| 2026-11-03 | 367 | 545 | 2 | -178 | -956 | 65.33 |
| 2026-11-04 | 656 | 257 | 1 | +399 | -557 | 88.73 |
| 2026-11-05 | 155 | 757 | 2 | -602 | -1159 | 79.94 |
| 2026-11-06 | 393 | 515 | 6 | -122 | -1281 | 39.94 |
| 2026-11-09 | 766 | 145 | 3 | +621 | -660 | 40.77 |
| 2026-11-10 | 405 | 503 | 6 | -98 | -758 | 29.64 |
| 2026-11-11 | 594 | 315 | 5 | +279 | -479 | 29.16 |

**A/D ratio 1.886 today** (594 advancing / 315 declining). Over the last 10 sessions the net advances total **+850** and the ADL slope is **+29.16 net advances per session** (10-session A/D ratio 1.206). The ADL is cumulative from 2026-08-18, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-28 → 2026-11-11). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 69.37% | — | — |
| `breadth_pctile_1y` | 94.3 | — | ABOVE_NORMAL |
| `breadth_pct_50dma` | 64.99% | — | — |
| `breadth_pctile_1y_50dma` | 84.7 | — | ABOVE_NORMAL |
| `index_etfs_above_20dma` | 3 of 5 | 55.7 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +9.37 pp | MATCHED | 61.5 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-05 | +37.88 |
| 2026-11-06 | +55.80 |
| 2026-11-09 | +27.40 |
| 2026-11-10 | +26.96 |
| 2026-11-11 | +9.37 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 283.09 | 277.85 | 281.43 | +0.59% | 0.37 |
| QQQ | 690.38 | 698.94 | 719.04 | -3.99% | -2.57 |
| QQQE | 117.70 | 117.05 | 118.82 | -0.94% | -0.74 |
| RSP | 222.65 | 218.02 | 214.92 | +3.60% | 3.54 |
| SPY | 759.81 | 760.20 | 764.96 | -0.67% | -0.65 |

## Live tape — 2026-11-12

**Live tape — 2026-11-12, 2026-11-12 14:04:55 ET.** Indices from the Cboe delayed-quote CDN (stamped 2026-11-12 13:49:36 ET); ETFs from the `market-recap` bridge (2026-11-12 14:04:55 ET — Yahoo-sourced, market_state `open`).

| Index | Level | Change |
|---|---|---|
| S&P 500 (SPX) | 7,614.51 | -0.06% |
| Nasdaq 100 (NDX) | 28,332.48 | -0.15% |
| Russell 2000 (RUT) | 2,815.45 | -1.08% |
| Dow (DJX) | 525.23 | +0.07% |

| ETF | Last | Change |
|---|---|
| SPY | 758.10 | -0.23% |
| QQQ | 687.94 | -0.35% |
| DIA | 523.95 | -0.09% |
| RSP | 221.37 | -0.57% |
| QQQE | 116.77 | -0.79% |
| IWM | 279.06 | -1.42% |

**Sector rotation (11 SPDR sectors + three thematic ETFs), best to worst:**

| ETF | Change |
|---|---|
| XLE (Energy) | +2.03% |
| XLU (Utilities) | +0.58% |
| XLP (Staples) | -0.17% |
| XLV (Health Care) | -0.24% |
| XLRE (Real Estate) | -0.27% |
| XLC (Comm. Services) | -0.31% |
| XLF (Financials) | -0.38% |
| XLY (Cons. Disc.) | -0.53% |
| XLK (Technology) | -0.57% |
| XLI (Industrials) | -0.62% |
| XLB (Materials) | -0.96% |
| SMH (Semis) | -1.42% |
| ARKK (Innovation) | -2.44% |
| XBI (Biotech) | -2.58% |

XLE is the only green sector, leading by 1.45 pp over XLU; XBI is the clear laggard at -2.58%. The tape is rotating defensively — energy and utilities bid, growth and cyclicals sold.

**Live participation proxy — NOT an advance/decline tally.** No live A/D feed exists on any reachable source, so this is a cap-weight proxy only, and it is a DIFFERENT population from the settled tally above:

| Spread | Value |
|---|---|
| RSP - SPY | -0.34 pp |
| QQQE - QQQ | -0.44 pp |
| IWM - SPY | -1.19 pp |

Equal weight lags cap weight on both measures, so the live tape is narrow at the top of the market while small caps lag outright.

## Volatility — single pair, live

**One pair, used everywhere in this document: VIX 18.02 / VIX3M 19.66.**

| Metric | Value |
|---|---|
| VIX | 18.02 (prev close 17.49, +3.03%) |
| VIX3M | 19.66 (prev close 19.24, +2.18%) |
| VIX/VIX3M ratio | **0.92** |
| Quote time | 2026-11-12 13:49:31 ET |
| Source | Cboe delayed-quote CDN (`_VIX.json` / `_VIX3M.json`) |
| Stability | `vix_stable: true` — two pulls inside the run returned identical values |

The ratio is **below 1.0**, so the term structure is in contango and the `uncertainty` regime flag stays false. The VIX is +3.03% on the session while the index is flat-to-lower: the market is paying up for protection into an intraday fade, which is not a vol shock. This is a **mid-session delayed print**, NOT a settled close, and it is never blended with the settled breadth layer above.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | false | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **`VIX` clock skew** — the volatility pair is stamped **2026-11-12 13:49:31 ET** (Cboe delayed feed) while the ETF tape is **2026-11-12 14:04:55 ET** (bridge). The two live layers are about 15 minutes apart, so the volatility read does not describe the tape's final hour. Treat them as two instants, not one.
- **`VIX` print is stable across the run** — an independent pre-run pull and the published pair both read 18.02, and the engine's two in-run pulls agreed (`vix_stable: true`).
- **`RSP`/`QQQE` proxy contradicts the settled tally's direction** — the 2026-11-11 settle had broad participation (594 advancing vs 315 declining), but today's live tape has equal weight *behind* cap weight (RSP -0.57% vs SPY -0.23%). Different sessions, different populations: the settled breadth is not a preview of today's tape.
- **`XBI` -2.58% against `XLV` -0.24%** — a 2.34 pp dislocation inside one GICS sector. It is a real print, not a data error, but the healthcare leg of today's tape is a biotech-specific event and does not describe health care broadly.
- **Universe refresh** — the market-cap floor is applied to the latest `valuation` row, so membership refreshes between runs. Today's universe is **914 names** against **905** in the 2026-11-11 published artifact, and the trailing series is recomputed on today's membership — which is why today's recomputed 2026-11-10 divergence (+26.96 pp) differs from the +27.40 pp published then. The series is comparable in level, not to the third decimal.

## Method, source health & caveats

**Sources tried, and their status.**

| Source | Use | Status |
|---|---|---|
| MCP bridge, `market-recap` `get_quotes` | live ETF tape (SPY/QQQ/IWM/RSP/DIA/QQQE) + 11 sector ETFs + SMH/XBI/ARKK | ok — 6/6 ETFs and 14/14 sectors found, 2026-11-12 14:04:55 ET, Yahoo-sourced, market_state `open` |
| MCP bridge, `shibui` `stock_data_query` | settled breadth series, A/D tally, index-ETF positioning | ok — 262 sessions, 2025-10-28 → 2026-11-11 |
| Cboe delayed-quote CDN | VIX/VIX3M pair, SPX/NDX/RUT/DJX | ok — but stamped 2026-11-12 13:49:31 ET (delayed feed) |
| MCP catalog probe (`probe_mcp.py`) | registration check | ok — `catalog_ok total=135 finance_tools=0`, `bridge_ok packs=tradier,fmp,market-recap` |
| TradingView scanner (`tv_scan.py`) | — | not used this run: the settled layer is shibui's, the live layer is the bridge's |

**Universe and its drift.** `NYSE/NASDAQ/AMEX, market cap > $10B, 914 names`, market cap taken from the latest `valuation` row. The universe is deliberately **not frozen** — it was 905 names in the 2026-11-11 artifact and 914 today, and the trailing series is recomputed on today's membership, so published history shifts by fractions of a point between runs.

**Settled vs live split.** The breadth numbers, the A/D tally, the ADL and the index-ETF positioning describe the **2026-11-11 settled session** (shibui is T+1; at the 14:00 ET fire the newest settled session is D-1). The tape, the sector rotation and the volatility pair are **live 2026-11-12**. Two fields, two labels, never blended.

**Percentile windows.** `breadth_pctile_1y` and `divergence_pctile_1y` are expanding percentiles against the trailing window (262 sessions, 2025-10-28 → 2026-11-11) — 100 x (sessions at or below the value) / (sessions in the window), so they are 0..100 by construction. The ADL slope needs a full 10-session window and is published as net advances per session; the ADL is a level, cumulative from 2026-08-18.

**`atr_extensions` note.** The five index-ETF rows are present and the map is **non-empty** (IWM +0.59%, QQQ -3.99%, QQQE -0.94%, RSP +3.60%, SPY -0.67%, each measured from its own 50-DMA) — no `probe_failed` — so `late_cycle = false` is a computed value, not a quiet default: no index ETF is more than 6% above its own 50-DMA.

**What could not be verified.** No live advance/decline tally exists on any reachable feed — the RSP/QQQE spreads are published explicitly as a cap-weight proxy, in its own labelled table, and are not an A/D count. The volatility pair is a mid-session delayed print, not a settle. Nothing in this artifact was reconstructed from a prior session's published artifact.
