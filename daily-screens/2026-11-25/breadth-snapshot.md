---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-25 14:00:01 ET"
data_date: "2026-11-24"
live_date: "2026-11-25"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 875 names"
vix_quote_time: "2026-11-25 13:46:31 ET (Yahoo chart API ^VIX/^VIX3M, 5-minute bar pinned to the 14:00:01 ET fire clock)"
vix_pair: "VIX 27.92 / VIX3M 26.15 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-25/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
degraded_sources: 1
---
_contract: breadth-artifact-v1 · data_date 2026-11-24 · universe 875 names · breadth 36.34% (pctile 17.9 · BELOW_NORMAL) · divergence +36.34 pp (BROAD) · AD 572/299/4_

# Breadth & Regime Snapshot — Wednesday, 25 November 2026 (intraday, cron #10)

**Intraday breadth read — 2026-11-25, snapshot at 14:00:01 ET.** The breadth, advance/decline and index-positioning layers describe the *settled* 2026-11-24 session (shibui is T+1). The tape and the volatility pair are *live* 2026-11-25 at 14:01:50 ET. The two layers are never blended. Source of record for prices: the MCP-over-HTTP bridge's `market-recap`; for the settled breadth series: shibui over the same bridge. Not a replay — the fire was dispatched on schedule (`stall_min: 0`).

## TL;DR

- **Breadth is repairing off the washout, but the trend structure is still broken and the index has not repaired at all.** On the settled 2026-11-24 session only **36.34%** of the 875 large caps are above their own 20-DMA — the **17.9th percentile** of the past year (BELOW_NORMAL), up from the 2026-11-20 washout low of 16.82% — while **0 of 5** index ETFs are above theirs. The settled advance/decline tally was **572 advancing / 299 declining / 4 unchanged** (ratio 1.913, net **+273**), but the ten-session net is still **-1410** and the ADL slope is **-250.88 net advances per session** — participation is healing far more slowly than the tape.
- **The divergence is the number that changes position sizing: +36.34 pp, BROAD (87.4th percentile) — the widest of the five-session window.** The spread has widened three sessions running (+16.82 → +29.03 → +36.34 pp) because the index's own trend damage outran the average stock's: with 0 of 5 index ETFs above their 20-DMA, the **index is the weak leg**, not the market. Today's live tape repeats the same shape — RSP **+0.93%** against SPY -0.37% (+1.30 pp), IWM +0.56% against QQQ -1.05%.
- **Read the tape as a washout and a bounce, not a regime change — and it is the last full session before Thanksgiving.** SPY printed a low of 695.45 (**-3.25%**) with the Nasdaq opening near -4%, then the afternoon bought almost all of it back to -0.37%. The driver was the 8:30 ET **October PCE** (headline 3.8% y/y, core 3.3% vs 3.2% expected) plus new tariff proposals, and the chips never came back (NVDA -4.76%, MU -6.38%). Volatility says the same: VIX **27.92** (+5.92%) against VIX3M 26.15 = **1.0677**, so `uncertainty` is ON. Regime stays defensive: size cut **ON** (50), index below its 20-DMA, not late cycle.

## Breadth — 2026-11-24 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 875 |
| Above 20-DMA | 318 (36.34%) |
| Below 20-DMA | 557 (63.66%) |
| Above 50-DMA | 442 (50.51%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 0 of 5 (0.0%) |
| Advance/decline — settled session | 572 advancing / 299 declining / 4 unchanged (A/D ratio 1.913) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **875 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-11 | 567 | 303 | 4 | +264 | 83 | 27.04 |
| 2026-11-12 | 217 | 654 | 3 | -437 | -354 | 19.46 |
| 2026-11-13 | 525 | 341 | 8 | +184 | -170 | 13.79 |
| 2026-11-16 | 234 | 635 | 5 | -401 | -571 | 0.56 |
| 2026-11-17 | 162 | 710 | 1 | -548 | -1119 | -49.98 |
| 2026-11-18 | 378 | 492 | 3 | -114 | -1233 | -71.84 |
| 2026-11-19 | 76 | 794 | 3 | -718 | -1951 | -155.81 |
| 2026-11-20 | 175 | 695 | 4 | -520 | -2471 | -260.47 |
| 2026-11-23 | 739 | 132 | 4 | +607 | -1864 | -271.19 |
| 2026-11-24 | 572 | 299 | 4 | +273 | -1591 | -250.88 |

**A/D ratio 1.913 today** (572 advancing / 299 declining). Over the last 10 sessions the net advances total **-1410** and the ADL slope is **-250.88 net advances per session** (10-session A/D ratio 0.721). The ADL is cumulative from 2026-08-31, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-11-10 → 2026-11-24). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 36.34% | — | — |
| `breadth_pctile_1y` | 17.9 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 50.51% | — | — |
| `breadth_pctile_1y_50dma` | 28.6 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 16.8 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +36.34 pp | BROAD | 87.4 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-18 | +37.11 |
| 2026-11-19 | +23.57 |
| 2026-11-20 | +16.82 |
| 2026-11-23 | +29.03 |
| 2026-11-24 | +36.34 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 267.14 | 275.01 | 277.46 | -3.72% | -2.26 |
| QQQ | 638.10 | 671.31 | 708.47 | -9.93% | -6.16 |
| QQQE | 109.58 | 114.09 | 117.51 | -6.75% | -5.15 |
| RSP | 213.96 | 217.68 | 214.75 | -0.37% | -0.36 |
| SPY | 718.78 | 743.11 | 758.64 | -5.25% | -4.91 |

## Live tape — 2026-11-25

Live quotes via the bridge's `market-recap` (`get_quotes`), Yahoo-sourced and cross-checked inside the same call against a second quote source — **17/17 `agrees`**, max difference 0.04%. Snapshot **2026-11-25 14:01:50 ET**, one minute after the fire clock; `market_state: open` — a live mid-session print, not a settled close.

| Instrument | Role | Last | Chg % | Day range (low – high) | Volume |
|---|---|---|---|---|---|
| SPY | S&P 500 | 716.11 | -0.37% | 695.45 – 718.18 | 49,060,534 |
| QQQ | Nasdaq-100 | 631.40 | -1.05% | 607.76 – 633.33 | 60,964,821 |
| RSP | S&P 500 equal-weight | 215.96 | +0.93% | 210.54 – 216.59 | 9,880,808 |
| QQQE | Nasdaq-100 equal-weight | 109.74 | +0.15% | 105.89 – 110.06 | 119,599 |
| IWM | Russell 2000 | 268.64 | +0.56% | 260.84 – 269.44 | 21,772,945 |
| | | | | | |
| SMH | VanEck Semiconductor | 417.55 | -2.16% | 393.88 – 418.94 | 10,450,395 |
| XLK | Technology | 154.89 | -1.40% | 148.39 – 155.35 | 14,891,098 |
| XLC | Communication services | 105.26 | +0.78% | 101.41 – 105.67 | 3,723,726 |
| XLY | Consumer discretionary | 117.81 | +0.08% | 113.85 – 118.16 | 5,435,676 |
| XLP | Consumer staples | 92.52 | +0.70% | 91.86 – 92.86 | 16,701,938 |
| XLE | Energy | 61.09 | +1.07% | 59.63 – 61.28 | 17,097,784 |
| XLF | Financials | 56.54 | +0.77% | 55.34 – 56.70 | 24,635,679 |
| XLV | Health care | 184.69 | -0.02% | 181.71 – 185.26 | 11,816,495 |
| XLI | Industrials | 162.90 | +0.80% | 157.41 – 163.36 | 9,315,131 |
| XLB | Materials | 51.27 | +2.20% | 49.48 – 51.44 | 10,034,423 |
| XLRE | Real estate | 44.06 | +1.38% | 43.23 – 44.16 | 5,212,684 |
| XLU | Utilities | 43.65 | +0.56% | 43.28 – 43.76 | 13,349,133 |
| | | | | | |
| ^GSPC | S&P 500 index | 7,178.70 | -0.31% | — | — |
| ^IXIC | Nasdaq Composite | 23,516.40 | -0.91% | — | — |
| ^DJI | Dow Jones Industrial Average | 50,275.35 | +0.51% | — | — |
| ^RUT | Russell 2000 index | 2,705.33 | +0.76% | — | — |
| | | | | | |
| NVDA | Nvidia | 147.98 | -4.76% | — | — |
| MU | Micron | 589.88 | -6.38% | — | — |
| AMD | Advanced Micro Devices | 401.67 | -2.81% | — | — |
| TSM | TSMC ADR | 339.32 | -2.83% | — | — |
| AVGO | Broadcom | 295.56 | -1.83% | — | — |
| XBI | SPDR S&P Biotech | 156.49 | -0.21% | — | — |

**The tape in one line: a violent AI-led washout that the afternoon bought back.** The open was a capitulation tape — the Nasdaq opened near -4%, and SPY printed a low of 695.45 (**-3.25%**), QQQ 607.76 (**-4.75%**) and SMH 393.88 (**-7.70%**). By the 14:01 ET pull SPY was -0.37%, QQQ -1.05% and SMH -2.16% — 2.9 pp, 3.7 pp and 5.5 pp of recovery from the lows, while the Dow closed positive (**+0.51%**) and the Russell 2000 (**+0.76%**) outperformed. The chips never came back: NVDA -4.76%, MU -6.38%, AMD -2.81%, TSM -2.83%.

**But the average stock was the strong leg all day.** RSP **+0.93%** against SPY -0.37% — **+1.30 pp** of equal-weight outperformance — and RSP's own low was only -1.60%. Materials led (**+2.20%**), then real estate (+1.38%), energy (+1.07%), industrials (+0.80%), staples (+0.70%) and financials (+0.77%); tech (-1.40%) and semiconductors (-2.16%) were the losers. That is the live mirror of the settled divergence below — the index is the weak leg, not the market.

**Cross-asset and overnight** (bridge `market_snapshot`, same pull):

| Instrument | Level | Chg |
|---|---|---|
| S&P 500 future | 7,199.75 | -0.25% |
| US 10-year yield | 4.84 | -1.35% |
| US Dollar Index (DXY) | 103.62 | -0.18% |
| WTI crude | 83.78 | +2.11% |
| Gold | 3,569.60 | -0.60% |
| Bitcoin | 59,664.60 | -0.14% |
| Nikkei 225 | 57,011.62 | -2.78% |
| Hang Seng | 21,966.01 | -1.87% |
| Shanghai Composite | 3,476.47 | -1.77% |
| DAX | 24,702.13 | -1.26% |
| FTSE 100 | 10,426.94 | -0.38% |

Asia did not confirm the American recovery: the Nikkei fell -2.78% and the Hang Seng -1.87% on the semiconductor sell-off, and the 10-year yield FELL to 4.838% — the hot inflation print did not push yields up, which is why the tape could recover. WTI was the outlier, +2.11%.

## Volatility — single pair, live

**One pair, one source, one moment.** VIX **27.92** / VIX3M **26.15**, quoted **2026-11-25 13:46:31 ET**, both symbols read from the **same** 5-minute bar of the same session.

| | Value | Prior close | Change |
|---|---|---|---|
| **VIX** | **27.92** | 26.36 | +5.92% |
| **VIX3M** | **26.15** | 25.31 | +3.32% |
| **VIX / VIX3M** | **1.0677** | — | front month **above** the 3-month — inverted |

**The ratio is above 1.0, so `uncertainty` is ON.** The front month is 1.77 points above the second month — the near-term-event-risk structure — after the front month rose +5.92% on the day. The pair is the latest 5-minute bar the Yahoo feed carried at the fire clock, so it is the **live print** for this session, not a reconstruction from a later bar. The Cboe delayed-quote CDN (the venue's own feed, the primary source for this routine) answered **HTTP 403** from this egress, so this pair is the Yahoo chart-API fallback and the `source` string in the regime sidecar names it.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **The published tape is a mid-session print 1 minute after the fire clock, and the session had already reversed 2.9 pp off its low.** SPY's low was -3.25% and the published print is -0.37%; QQQ's low was -4.75% against a published -1.05%, and SMH's low was -7.70% against -2.16%. Do not read the closing-hour numbers as the session's character — this was a washout and a bounce, and the bounce is still in progress.
- **QQQE is too thin to read as the equal-weight Nasdaq.** Its volume was 119,599 shares against QQQ's 60,964,821 — a factor of 510. Its +0.15% is not the same signal as QQQ's; the equal-weight read in this document is RSP and IWM.
- **The `BROAD` band is mechanically floored by the index leg.** With **0 of 5** index ETFs above their own 20-DMA, the index side of the spread is zero, so a +36.34 pp reading is what "36.34% of large caps above their 20-DMA against 0% of the index ETFs" produces. It measures how far the trend structure lags the index, not a disagreement between two sources.
- **No live advance/decline figure is published.** Every advancing/declining number in this artifact is the **settled 2026-11-24** count (572 / 299 / 4). The intraday participation for 2026-11-25 is not computed here; the tape section reports index, sector and single-name prints only.
- **The universe moved again: 875 names**, against 870 on the 2026-11-23 settled session. The filter is unchanged (NYSE/NASDAQ/AMEX, market cap > $10B); the count moves because the market-cap floor is applied to the latest `valuation` row. The drift is disclosed, not smoothed away.
- **The volatility pair is one feed's fallback, not the venue's print.** The Cboe delayed-quote CDN answered HTTP 403 (Cloudflare) for every User-Agent from this egress — the one degraded source of this run. The pair comes from Yahoo's chart API with both symbols read from the same 5-minute bar, and it is used everywhere in this document.
- **IWM is quoted twice in this run** — 268.64 (+0.56%) in the 17-instrument pull and 268.715 (+0.59%) in the index pull, seconds apart. The published number is the 17-instrument pull; the gap is a timestamp difference, not a data conflict.

## Method, source health & caveats

### Method

- **Two layers, never blended.** The breadth, advance/decline, percentile and index-positioning layers describe the **settled 2026-11-24** session from shibui (T+1 — the newest ingested session at the 14:00:01 ET fire on 2026-11-25). The tape and the volatility pair are **live 2026-11-25**. The front matter carries both dates (`data_date` / `live_date`) and no number in this artifact mixes the two.
- **The universe is the contract's, not a new one:** NYSE/NASDAQ/AMEX, market cap > $10B taken from the latest `valuation` row, **875 names**. It is not frozen — the count moves as valuation rows refresh (870 on the 2026-11-23 session, 875 on 2026-11-24). The advance/decline tally uses the **same** indicator-joined population as the breadth percentage, so 572 + 299 + 4 = 875, the published universe count.
- **Percentile windows.** The level percentiles are ranks against the trailing 262-session distribution of the same series (2025-11-10 → 2026-11-24); the ADL window is 60 sessions and the ADL is cumulative from **2026-08-31** (a level), with the published slope (**-250.88 net advances per session**) as the rate over 10 sessions.
- **`atr_extensions` is non-empty** — all five index ETFs are carried, read from the `ticker` key the SQL actually emits, so `late_cycle` is computable rather than vacuously false. Every one of the five is *below* its own 50-DMA (SPY -5.25%, QQQ -9.93%, RSP -0.37%), so `late_cycle` is genuinely false today.
- **One number per field, one source per field.** Prices and the tape come from the bridge's `market-recap` (cross-checked inside the call against a second quote source); the breadth, A/D and index-ETF rows come from shibui; the volatility pair comes from Yahoo's chart API. Where two feeds could serve the same field, one was chosen and named here.

### Source health

| Source | What it served | Status |
|---|---|---|
| shibui `stock_data_query` over the MCP-over-HTTP bridge | the settled breadth series, the A/D tally, the index-ETF positioning (newest ingested session **2026-11-24**, T+1 — one session behind the cron day) | **ok** (lag disclosed, not blended) |
| bridge `market-recap` `get_quotes` | the live tape — 17 instruments (17/17 `agrees` against a second quote source) and the index/single-name pull (11/11 `agrees`) | **ok** |
| bridge `market-recap` `market_snapshot` | the cross-asset block (futures, yields, FX, Asia, Europe) | **ok** |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the volatility pair, both symbols from the same 5-minute bar stamped 2026-11-25 13:46:31 ET | **ok** — *fallback* |
| Cboe delayed-quote CDN | the primary volatility source | **failed: HTTP 403 (Cloudflare)** — the Yahoo fallback served the pair |
| web search (Reuters, CNBC, Barron's, Investopedia, YCharts, StockTitan) | the day's catalysts only — the October PCE print, the new tariff proposals, the chip rout and the afternoon recovery | **ok** — no published number comes from it |

**Degraded sources: 1** — the Cboe delayed-quote CDN (HTTP 403). The volatility pair was published from the Yahoo fallback instead, and the `source` string in `_regime-intraday.json` names it.

### MCP availability probe

`catalog_ok total=138 finance_tools=0` — no finance MCP is registered on this runtime, so the MCP-over-HTTP bridge is the data path. The absent `mcp__*` tools are **not** an error and are not counted in the degraded-source tally.

### What happened on the tape (context, not a published number)

- **8:30 ET — October PCE:** headline **3.8% y/y** (in line, the hottest since 2023), core **3.3%** (a tick hotter than the 3.2% expected, the hottest core since November 2023), with Q3 GDP revised up to **4.3%** annualised. December rate-hike odds went to ~98%.
- **New tariff proposals** — a Section 301 review of semiconductors and electronics plus 20% tariff headlines on Nvidia and Intel — landed alongside it. The proposals are not expected to take effect before January; they hit sentiment, not earnings.
- **The AI complex broke again**, third session running: NVDA fell as much as 9% intraday and settled -4.76%, MU -6.38%, AMD -2.81%, TSM -2.83%, AVGO -1.83%. The Nasdaq Composite is on pace for its worst November since 2008.
- **The afternoon bought it back** — the Dow turned positive, the Russell outperformed, and the 10-year yield FELL even on the hot inflation print, which is what allowed the bounce.
- **Holiday-week context:** markets are closed Thursday 26 November (Thanksgiving) and close early on Friday 27 November, so this is the last full session before the break — liquidity thins into it.
