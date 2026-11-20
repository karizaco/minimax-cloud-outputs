---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-19 14:00:46 ET"
data_date: "2026-11-18"
live_date: "2026-11-19"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 878 names"
vix_quote_time: "2026-11-19 14:00:00 ET (Yahoo chart API, 5-minute bar pinned to the fire clock)"
vix_pair: "VIX 27.56 / VIX3M 26.37 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-19/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
degraded_sources: 2
---
_contract: breadth-artifact-v1 · data_date 2026-11-18 · universe 878 names · breadth 37.24% (pctile 16.7 · BELOW_NORMAL) · divergence +37.24 pp (BROAD) · AD 381/494/3_

# Breadth & Regime Snapshot — Thursday, 19 November 2026 (intraday, cron #10)

Intraday breadth read, fired **2026-11-19 14:00:46 ET** on the live tape. The settled breadth numbers describe the **2026-11-18** close (shibui is T+1 — at a 14:00 ET fire on 2026-11-19 its newest settled session is 2026-11-18); the tape and the volatility pair are **2026-11-19 at 14:00:00 ET**. The two layers are never blended. This artifact is a **delayed replay**: the scheduled run was blocked by a platform token-plan limit for 664 minutes and resumed in place, so the live layer is reconstructed from 5-minute bars pinned to the fire clock rather than pulled live — the settled layer is unaffected.

## TL;DR

- **Breadth is still falling.** 37.24% of the 878 large caps are above their own 20-DMA (percentile 16.7, BELOW_NORMAL), down from 39.52% in the 2026-11-17 session, and 51.82% are above the 50-DMA (percentile 31.9, NORMAL). The 2026-11-18 session itself was negative — **381 advancing against 494 declining** (3 unchanged, A/D ratio 0.771) — and the 10-session ADL slope has steepened to **-72.41 net advances per session**.
- **The divergence is the story: +37.24 pp, BROAD (percentile 87.8).** All 5 index ETFs sit below their own 20-DMA (0 of 5) while 37.24% of the large-cap universe is above its own — the average large cap is materially healthier than the index, so the index is the weak leg, not the average stock. The spread has narrowed for two sessions (+51.94 → +39.52 → +37.24 pp) but it is still in the top decile of its own year. The regime carries a **50% size cut** (index below its 20-DMA and breadth under 40%) and `uncertainty: true`.
- **Read it as stress, not a washout — and read the tape as pinned.** At 14:00:00 ET on 2026-11-19 the market was down hard (SPY -1.47%, QQQ -1.61%, IWM -1.67%) with the VIX at 27.56 (+12.21%) and the term structure **inverted** (VIX 27.56 above VIX3M 26.37, ratio 1.0451) — which is what sets `uncertainty: true`. The tape and the pair are reconstructed from bars pinned to the fire clock, not live prints, and the Cboe delayed-quote CDN is blocked from this egress.

## Breadth — 2026-11-18 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 878 |
| Above 20-DMA | 327 (37.24%) |
| Below 20-DMA | 551 (62.76%) |
| Above 50-DMA | 455 (51.82%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 381 advancing / 494 declining / 3 unchanged (A/D ratio 0.771) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **878 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-05 | 151 | 725 | 2 | -574 | -1257 | 81.02 |
| 2026-11-06 | 369 | 504 | 5 | -135 | -1392 | 41.87 |
| 2026-11-09 | 734 | 141 | 3 | +593 | -799 | 41.78 |
| 2026-11-10 | 397 | 475 | 6 | -78 | -877 | 29.94 |
| 2026-11-11 | 571 | 303 | 4 | +268 | -609 | 27.99 |
| 2026-11-12 | 217 | 658 | 3 | -441 | -1050 | 20.75 |
| 2026-11-13 | 528 | 342 | 8 | +186 | -864 | 14.96 |
| 2026-11-16 | 232 | 641 | 5 | -409 | -1273 | 1.28 |
| 2026-11-17 | 162 | 715 | 1 | -553 | -1826 | -49.96 |
| 2026-11-18 | 381 | 494 | 3 | -113 | -1939 | -72.41 |

**A/D ratio 0.771 today** (381 advancing / 494 declining). Over the last 10 sessions the net advances total **-1256** and the ADL slope is **-72.41 net advances per session** (10-session A/D ratio 0.749). The ADL is cumulative from 2026-08-25, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (263 sessions, 2025-11-03 → 2026-11-18). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 37.24% | — | — |
| `breadth_pctile_1y` | 16.7 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 51.82% | — | — |
| `breadth_pctile_1y_50dma` | 31.9 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 16.0 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +37.24 pp | BROAD | 87.8 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-12 | +23.33 |
| 2026-11-13 | +43.10 |
| 2026-11-16 | +51.94 |
| 2026-11-17 | +39.52 |
| 2026-11-18 | +37.24 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 270.12 | 277.80 | 279.38 | -3.31% | -2.03 |
| QQQ | 659.51 | 686.30 | 714.36 | -7.68% | -4.86 |
| QQQE | 112.01 | 115.92 | 118.22 | -5.25% | -4.07 |
| RSP | 215.43 | 218.87 | 214.98 | +0.21% | 0.21 |
| SPY | 730.20 | 753.72 | 762.51 | -4.24% | -4.02 |

## Live tape — 2026-11-19

Index levels and the ETF tape are pinned to **2026-11-19 14:00:00 ET** — the fire's own clock. This run is a delayed replay, so the live print no longer exists on any feed: every number below is reconstructed from Yahoo's chart API 5-minute bars at that stamp (the Cboe delayed-quote CDN answers HTTP 403 from this egress, and the bridge's `market-recap` would now serve the next session's pre-market quotes, not this session's tape).

| Index | Last | Change | Bar stamp |
|---|---|---|---|
| S&P 500 | 7,212.31 | -1.50% | 14:00:00 ET |
| Nasdaq 100 | 26,662.78 | -1.65% | 14:00:00 ET |
| Russell 2000 | 2,670.90 | -1.61% | 14:00:00 ET |
| Dow Jones | 493.28 | -1.72% | 14:00:00 ET |

| Index ETF | Last | Change | Prior close | Bar stamp |
|---|---|---|---|---|
| SPY | 719.560 | -1.47% | 730.330 | 14:00:00 ET |
| QQQ | 648.862 | -1.61% | 659.510 | 14:00:00 ET |
| IWM | 265.630 | -1.67% | 270.140 | 14:00:00 ET |
| RSP | 212.560 | -1.36% | 215.480 | 14:00:00 ET |
| DIA | 493.170 | -1.70% | 501.700 | 14:00:00 ET |

**Sector rotation (live, 14:00:00 ET)** — every sector is down; the defensives held up best and consumer discretionary fell hardest:

| Sector ETF | Sector | Last | Change |
|---|---|---|---|
| XLE | Energy | 60.985 | -0.52% |
| XLU | Utilities | 43.105 | -1.00% |
| XLRE | Real estate | 43.095 | -1.23% |
| XLP | Consumer staples | 90.050 | -1.25% |
| XLK | Technology | 161.680 | -1.29% |
| XLF | Financials | 55.700 | -1.29% |
| XLB | Materials | 49.670 | -1.52% |
| XLI | Industrials | 162.120 | -1.55% |
| XLC | Communication | 103.660 | -1.84% |
| XLV | Health care | 177.790 | -1.86% |
| XLY | Consumer discretionary | 116.430 | -2.32% |

Semiconductors (SMH) 451.67 (-1.68%) — the mega-cap leg is being sold with the index, not leading it.

## Volatility — single pair, live

**27.56 / 26.37** — VIX 27.56, VIX3M 26.37, one pair, quoted at 14:00:00 ET on 2026-11-19 from Yahoo's chart API (^VIX / ^VIX3M), both symbols read from the SAME 5-minute bar.

- Session mode: replay — reconstructed from the pinned 5-minute bar at the fire clock (the live print is no longer available).
- Prior close: VIX 24.56 (+12.21%), VIX3M 24.24 (+8.79%) — volatility is spiking, and the front end is moving more than the 3-month.
- VIX/VIX3M = 1.0451 — the VIX is ABOVE the 3-month, an inverted term structure, which is what sets `uncertainty: true`. This is a real inversion, not a rounding-scale difference.
- The Cboe delayed-quote CDN answered HTTP 403 (Cloudflare) from this egress, so the pair came from the pinned fallback; both symbols carry the same bar stamp, so the pair is internally consistent.

This is the ONLY volatility pair in this document. It is the print that existed at the fire, not a settled close, and the settled sections above never carry a VIX number.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **RSP is the only one of the five index ETFs above its own 50-DMA** (+0.21%), while SPY (-4.24%), QQQ (-7.68%), QQQE (-5.25%) and IWM (-3.31%) sit below theirs. The BROAD divergence is a 20-DMA reading; on the 50-DMA horizon the equal-weight index is the healthy one — the two horizons disagree, and neither is wrong.
- **QQQ's -7.68% distance from its 50-DMA is the deepest of the five** (ATR multiple -4.86x, against -2.03x for IWM) — the mega-cap complex is the leg that broke, and it is also the leg that fell hardest on the tape (-1.61%).
- **The same session reads differently across runs.** The 2026-11-17 breadth reads 39.52% in today's CSV against 39.11% in the 2026-11-18 artifact, and the universe count is 878 today (877 at the last fire, 890 at the 2026-11-17 fire) — the market-cap floor is applied to the LATEST `valuation` row, so the population and the advance/decline denominator move between runs. The published 878 is today's population, not a frozen one.
- **Two sources disagree on the 2026-11-18 close.** shibui's settled close for SPY is 730.20 while Yahoo's 2026-11-18 session bar closes at 730.330 (IWM 270.12 vs 270.140, RSP 215.43 vs 215.480; QQQ agrees exactly at 659.51). The gap is at most 0.02% and moves no 20-DMA or 50-DMA reading, but the two feeds are not interchangeable — flagged rather than reconciled.
- **`uncertainty` fires on a genuine inversion this time.** VIX 27.56 against VIX3M 26.37 is a 4.51% gap — the 2026-11-18 fire flagged `uncertainty` on a 0.04% rounding-scale difference, so this one is a different signal entirely and should not be read as a continuation of it.

## Method, source health & caveats

**Settled layer (data_date 2026-11-18).** All breadth, advance/decline, percentile and divergence numbers come from shibui through the MCP-over-HTTP bridge. shibui is T+1: at a 14:00 ET fire on 2026-11-19 its newest settled session is 2026-11-18, so the settled layer is one session behind the live tape by construction.

- **Universe** — NYSE/NASDAQ/AMEX, market cap > $10B (floor applied to the latest `valuation` row), **878 names** today. The universe is NOT frozen and the count moves as valuation rows refresh; it is published every run.
- **Advance/decline** — a real tally from `stock_quotes` with a `LAG()` self-join over the same indicator-joined population the breadth percentage uses, so advancing + declining + unchanged ties to the published universe count (381 + 494 + 3 = 878).
- **ADL** — cumulative net advances from **2026-08-25** (a level), with the 10-session OLS slope as the rate. The slope needs a full 10-session window and is published blank otherwise.
- **Percentiles** — against the trailing 1-year distribution of the same series: 263 sessions, 2025-11-03 → 2026-11-18. Bands: ABOVE_NORMAL ≥ 80, BELOW_NORMAL ≤ 20, NORMAL in between.
- **Divergence** — large-cap breadth % above the 20-DMA minus the index ETFs' share above their own 20-DMA, in percentage points. BROAD ≥ +15 pp, NARROW ≤ -15 pp.
- **Index positioning** — the five index ETFs' own 20-DMA / 50-DMA from shibui, measured on the 2026-11-18 settled close. `atr_extensions` is non-empty (5 symbols), so `late_cycle` was computed, not defaulted.

**Live layer (2026-11-19, 14:00:00 ET).** Yahoo's chart API 5-minute bars, pinned to the fire day and the fire clock: the index proxies, the five index ETFs, the eleven sector ETFs, SMH, and the ^VIX / ^VIX3M pair (both symbols from the same bar). The pair was taken from the same pinned series, so the artifact's Volatility section and the regime payload's `uncertainty` flag are the same pair.

**Source health.**

| Source | Use | Status |
|---|---|---|
| shibui via MCP bridge (`stock_data_query`) | settled breadth, A/D, index positioning | ok |
| Yahoo chart API (5-minute bars, pinned) | live tape, sector rotation, volatility pair | ok |
| Cboe delayed-quote CDN (`_VIX/_VIX3M`) | volatility pair | **blocked** — HTTP 403 (Cloudflare) from this egress; the pinned Yahoo fallback served the pair |
| bridge `market-recap` `get_quotes` | live ETF tape | not used — on a delayed replay it would serve the next session's quotes, not this session's tape |
| MCP availability probe | catalog check | ok — the finance MCPs are reached over the bridge; this is not a degradation |

**Degraded sources: 2.** (1) The Cboe delayed-quote CDN is HTTP 403 from this egress, so the volatility pair and the tape came from the pinned Yahoo fallback rather than the primary source. (2) The scheduled fire was blocked by a platform token-plan limit for 664 minutes before its first tool call (`42212: Token Plan usage limit reached ... (2056)`), and this artifact is the resumed replay of that fire.

**Caveats.** The trailing series is recomputed each run against the LATEST valuation snapshot, so a historical breadth percentage can shift slightly between runs. The live tape is a reconstruction from pinned 5-minute bars, not a live print — the numbers are what the tape showed at the fire, but they carry no quote-stamp jitter and no bid/ask information. No source number in this artifact is a cap-weight stand-in for a real advance/decline tally.
