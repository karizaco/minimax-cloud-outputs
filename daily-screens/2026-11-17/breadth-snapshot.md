---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-17 14:01:01 ET"
data_date: "2026-11-16"
live_date: "2026-11-17"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 890 names"
vix_quote_time: "2026-11-17 13:48:31 ET (Cboe delayed-quote CDN — ~13 min behind the 14:04 ET tape)"
vix_pair: "VIX 25.96 / VIX3M 25.05 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-17/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-16 · universe 890 names · breadth 51.01% (pctile 34.9 · NORMAL) · divergence +51.01 pp (BROAD) · AD 232/653/5_

# Breadth & Regime Snapshot — Tuesday, 17 November 2026 (intraday, cron #10)

Intraday breadth & regime read — fired **2026-11-17 14:01 ET**. The settled layer describes the **2026-11-16** session (shibui is T+1, so at a 14:00 ET fire on 2026-11-17 its newest settled session is 2026-11-16); the tape and the volatility pair are **live 2026-11-17**. Sources of record — settled layer: the `shibui` MCP server over the HTTPS bridge; live tape: the `market-recap` bridge (`get_quotes`, Yahoo-sourced), pulled 2026-11-17 14:04:17 ET; volatility pair: the Cboe delayed-quote CDN, quote stamp 2026-11-17 13:48:31 ET.

## TL;DR

- **What breadth did:** **51.01%** of the **890-name** large-cap universe closed above its own 20-DMA on the **2026-11-16** settled session (59.21% above the 50-DMA), at the **34.9** percentile of its own trailing year (**NORMAL**) — down from 61.96% on the prior settled session. Participation was negative: **232 advancing / 653 declining / 5 unchanged** (ratio **0.355**, net **-421**), with the 10-session ADL slope at **+0.12** net advances per session.
- **The one divergence that changes position sizing: +51.01 pp, band BROAD, 1-year percentile 99.2** — **0 of 5** index ETFs sit above their own 20-DMA, so the cap-weighted index is the weak leg while the average large cap is not. After dipping to +9.44 pp on 2026-11-11 the spread has widened three sessions running (+22.47 → +42.25 → +51.01 pp) and now sits at the 99.2th percentile of its own year.
- **The caveat that changes how to read it:** the settled layer is 2026-11-16, and today's live tape is a broad risk-off session — SPY -1.26%, SPX -1.24%, Dow -1.62%, every sector red, and the VIX **+13.31%** to **25.96** with the front month **inverted above VIX3M** (1.036), which holds `uncertainty` at **true**. Expect the 2026-11-17 settled breadth to fall further; read today's numbers as a posture, not a tape.

## Breadth — 2026-11-16 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 890 |
| Above 20-DMA | 454 (51.01%) |
| Below 20-DMA | 436 (48.99%) |
| Above 50-DMA | 527 (59.21%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 232 advancing / 653 declining / 5 unchanged (A/D ratio 0.355) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **890 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-03 | 349 | 539 | 2 | -190 | -1078 | 62.37 |
| 2026-11-04 | 642 | 247 | 1 | +395 | -683 | 85.24 |
| 2026-11-05 | 153 | 735 | 2 | -582 | -1265 | 78.2 |
| 2026-11-06 | 375 | 509 | 6 | -134 | -1399 | 39.61 |
| 2026-11-09 | 744 | 143 | 3 | +601 | -798 | 40.45 |
| 2026-11-10 | 397 | 487 | 6 | -90 | -888 | 28.9 |
| 2026-11-11 | 579 | 306 | 5 | +273 | -615 | 27.27 |
| 2026-11-12 | 220 | 667 | 3 | -447 | -1062 | 20.0 |
| 2026-11-13 | 536 | 346 | 8 | +190 | -872 | 14.11 |
| 2026-11-16 | 232 | 653 | 5 | -421 | -1293 | 0.12 |

**A/D ratio 0.355 today** (232 advancing / 653 declining). Over the last 10 sessions the net advances total **-405** and the ADL slope is **+0.12 net advances per session** (10-session A/D ratio 0.913). The ADL is cumulative from 2026-08-21, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (261 sessions, 2025-11-03 → 2026-11-16). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 51.01% | — | — |
| `breadth_pctile_1y` | 34.9 | — | NORMAL |
| `breadth_pct_50dma` | 59.21% | — | — |
| `breadth_pctile_1y_50dma` | 58.2 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 15.3 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +51.01 pp | BROAD | 99.2 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-10 | +27.19 |
| 2026-11-11 | +9.44 |
| 2026-11-12 | +22.47 |
| 2026-11-13 | +42.25 |
| 2026-11-16 | +51.01 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 272.94 | 278.46 | 280.30 | -2.63% | -1.62 |
| QQQ | 661.75 | 692.62 | 716.72 | -7.67% | -4.89 |
| QQQE | 113.42 | 116.62 | 118.51 | -4.29% | -3.35 |
| RSP | 218.93 | 218.93 | 214.98 | +1.84% | 1.8 |
| SPY | 739.95 | 757.69 | 763.82 | -3.13% | -2.98 |

## Live tape — 2026-11-17

Live tape, 2026-11-17 14:04 ET — source of record: the `market-recap` bridge (`get_quotes`, Yahoo-sourced), pulled 2026-11-17T19:04:17.972Z. These are LIVE prints; they are not the settled layer above.

| Index | Level | Change |
|---|---|---|
| S&P 500 | 7,324.94 | -1.24% |
| Nasdaq Composite | 24,230.26 | -1.14% |
| Russell 2000 | 2,712.90 | -1.10% |
| Dow Jones | 50,770.99 | -1.62% |

| Index ETF | Price | Change | Volume (partial session) |
|---|---|---|---|
| SPY | 730.66 | -1.26% | 39,688,065 |
| RSP (equal weight) | 216.32 | -1.19% | 8,493,159 |
| QQQ | 653.78 | -1.20% | 35,352,724 |
| QQQE (equal weight) | 112.04 | -1.22% | 156,295 |
| IWM | 269.39 | -1.30% | 17,087,482 |
| DIA | 507.36 | -1.61% | 2,682,173 |

| Sector SPDR | Change |
|---|---|
| Technology (XLK) | -1.77% |
| Financials (XLF) | -1.70% |
| Health care (XLV) | -1.43% |
| Utilities (XLU) | -1.10% |
| Real estate (XLRE) | -0.99% |
| Cons. discr. (XLY) | -0.90% |
| Cons. staples (XLP) | -0.82% |
| Industrials (XLI) | -0.70% |
| Materials (XLB) | -0.55% |
| Energy (XLE) | -0.45% |
| Semis (SMH) | -1.58% |
| Biotech (XBI) | -0.74% |

Cap-weight versus equal-weight is a wash on the tape: **RSP -1.19%** versus **SPY -1.26%** (+0.07 pp), but **QQQE -1.22%** versus **QQQ -1.20%** (-0.02 pp). Every sector is red; the defensive end leads (XLE -0.45%, XLB -0.55%) and the highest-beta corners lag (XLK -1.77%, SMH -1.58%).

## Volatility — single pair, live

**One pair, used everywhere in this document: VIX 25.96 / VIX3M 25.05** — source: Cboe delayed-quote CDN (_VIX.json / _VIX3M.json), quote stamp **2026-11-17 13:48:31 ET** (regular hours — live print). The pair was pulled twice and agreed to the cent (`vix_stable: true`).

| Metric | Value | Prior settle | Change |
|---|---|---|---|
| VIX | 25.96 | 22.91 | +13.31% |
| VIX3M | 25.05 | 23.02 | +8.82% |
| VIX / VIX3M | 1.036 | 22.91 / 23.02 = 0.995 | inverted — front month above the 3-month |

The term structure is **inverted** (ratio 1.036 > 1.0), so the `uncertainty` regime flag is **true** — and it is a TERM-STRUCTURE test (front month above 3-month), not a level test: the front month is 25.96, far from any absolute panic threshold, but the curve is paying up for near-term risk. The independent bridge quote for `^VIX` (25.98, stamped 2026-11-17 13:49:16 ET) agrees with the Cboe print to within 0.02 — two different vendors, one reading.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **QQQE — thin line.** 156,295 shares and an `as_of` of 2026-11-17 14:01:02 ET (3 minutes behind the rest of the tape). Its -1.22% is a low-conviction print, and it is one of the five index-ETF legs inside the divergence — treat the ETF leg as 4 reliable reads plus one thin one.
- **^RUT — stale index print.** The small-cap index reads 2,712.90 (-1.10%) with a **NULL** volume and an `as_of` of 2026-11-17 13:49:15 ET — about 15 minutes behind the other index rows, which are stamped 14:04 ET.
- **SPY — partial-session volume.** 39,688,065 shares at 14:04 ET is a **snapshot**, not a settled volume; it is published as a tape number only and must not be compared with a full-session average.
- **VIX pair stamp — 13 minutes behind the fire.** The Cboe pair is stamped 2026-11-17 13:48:31 ET against a 14:04 ET tape, so the volatility reading is a mid-session print rather than the 14:00 ET instant. Both vendors' readings agree, so nothing is distorted — but it is a stamp, not a settle.

## Method, source health & caveats

**Sources.** Settled layer: the `shibui` MCP server over the HTTPS bridge (`261` sessions, 2025-11-03 → 2026-11-16, 380-day window), 6 SQL calls, each paged with a `rows_kept == rows_passing` assertion. Live tape: the `market-recap` bridge (`get_quotes`), 23 symbols requested, 23 found. Volatility pair: the Cboe delayed-quote CDN. MCP catalog probe: `catalog_ok total=135 finance_tools=0` — no financial MCP is registered on this runtime, so every market number here comes from the bridge or the CDN.

**Settled vs live — never blended.** The breadth numbers describe the **2026-11-16** settled session (shibui is T+1: at a 14:00 ET fire on 2026-11-17 its newest settled session is 2026-11-16). The tape and the volatility pair are **live 2026-11-17**. The two layers are in separate sections and separate front-matter fields (`data_date` / `live_date`).

**Universe.** NYSE/NASDAQ/AMEX, market cap > $10B, applied to the LATEST `valuation` row — the universe is NOT frozen. Today's count is **890 names**; the previous fire (2026-11-16) published **899**. The $10B floor is unchanged and the venue list is unchanged; only the refreshed valuation rows moved the count.

**Percentile windows.** The percentiles are expanding over the same trailing window (261 sessions from 2025-11-03), so `breadth_pctile_1y` is the rank of today's level inside its own history — a level without it is a number without a context. `breadth_pctile_1y_50dma` and `divergence_pctile_1y` use the same window.

**`atr_extensions` note.** The skill's breadth SQL emits `extension_pct` from a window function over a date-filtered CTE, where the 252-day ATR average collapses to the 14-day ATR. The published `extension_pct` is therefore the distance from the 50-DMA, which is what the "Index positioning" table labels it. The extension map is populated for all five index ETFs (IWM, QQQ, QQQE, RSP, SPY), so `late_cycle` is a live flag, not a flag that could never fire.

**Regime flags.** `uncertainty` is a TERM-STRUCTURE test (VIX > VIX3M), not a level test; `size_cut_pct` triggers only when the index is below its 20-DMA **and** breadth < 40% (breadth is 51.01%, so it does not trigger); `late_cycle` fires when any index ETF is more than 6% above its own 50-DMA (the furthest above is RSP at +1.84%, the furthest below QQQ at -7.67%, so the trigger does not fire).

**Session-to-session context.** The settled breadth fell from **61.96%** (the 2026-11-13 session, published in the 2026-11-16 artifact) to **51.01%**, and the divergence widened from +41.96 pp to **+51.01 pp**. The settled layer is getting weaker, not healthier — the spread is widening because the index leg is deteriorating, not because the broad market is improving.

**Not verified.** The 2026-11-17 session is not settled yet, so this artifact cannot say what today's breadth closes at; the live tape is the only 2026-11-17 evidence here. The per-symbol volume figures are partial-session snapshots.
