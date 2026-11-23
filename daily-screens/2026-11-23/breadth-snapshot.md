---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-23 14:00:05 ET"
data_date: "2026-11-20"
live_date: "2026-11-23"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 860 names"
vix_quote_time: "2026-11-23 13:45:00 ET (Yahoo chart API ^VIX/^VIX3M, 5-minute bar pinned to the 14:00:05 ET fire clock)"
vix_pair: "VIX 27.09 / VIX3M 25.47 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-23/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
degraded_sources: 1
---
_contract: breadth-artifact-v1 · data_date 2026-11-20 · universe 860 names · breadth 16.74% (pctile 1.2 · BELOW_NORMAL) · divergence +16.74 pp (BROAD) · AD 174/682/4_

# Breadth & Regime Snapshot — Monday, 23 November 2026 (intraday, cron #10)

Intraday breadth read, fired **2026-11-23 14:00:05 ET** on the live tape. The settled breadth numbers describe the **2026-11-20** close (shibui is T+1 — at a 14:00 ET fire on 2026-11-23 its newest ingested session is 2026-11-20, Friday's rout); the tape and the volatility pair are **2026-11-23 at 14:00–14:03 ET**. The two layers are never blended. This is NOT a replay: the fire was dispatched on schedule (`stall_min: 1`), so the live layer is a live pull, not a reconstruction from pinned bars. Source of record for the tape: the MCP-over-HTTP bridge's `market-recap` (`get_quotes` / `market_snapshot`).

## TL;DR

- **Breadth has broken down, and the settled read is as bad as it has been in a year.** Only **16.74%** of the 860 large caps are above their own 20-DMA (1-year percentile **1.2**, BELOW_NORMAL), with 38.72% above the 50-DMA (percentile 16.5). The settled session (2026-11-20) was the rout itself: **174 advancing against 682 declining** (4 unchanged, A/D ratio **0.255**) and a 10-session ADL slope of **-255.21 net advances per session** — the steepest reading in the published 30-session window.
- **The divergence is the number that changes sizing: +16.74 pp, BROAD (percentile 64.6)** — all 5 index ETFs sit below their own 20-DMA (0 of 5) while 16.74% of the large-cap universe is above its own, so on the settled session the average large cap was healthier than the index. The spread has narrowed for four straight sessions (+51.46 → +39.23 → +36.90 → +23.26 → +16.74 pp) as the index's own damage outran the average stock's.
- **Read today's tape as a narrow, event-driven relief rally — not a breadth repair.** SPY +4.75% and QQQ +6.92% at 14:01 ET, but RSP is only **+2.53%** (2.22 pp behind SPY) and the whole move is Nvidia (NVDA **+31.31%**) after Jensen Huang was reinstated as CEO, with SMH +14.42%. The settled breadth still carries a **50% size cut**, `uncertainty: true` (VIX 27.09 above VIX3M 25.47, ratio 1.064) and 0 of 5 index ETFs above their 20-DMA — none of which today's tape has repaired.

## Breadth — 2026-11-20 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 860 |
| Above 20-DMA | 144 (16.74%) |
| Below 20-DMA | 716 (83.26%) |
| Above 50-DMA | 333 (38.72%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 0 of 5 (0.0%) |
| Advance/decline — settled session | 174 advancing / 682 declining / 4 unchanged (A/D ratio 0.255) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **860 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-09 | 716 | 140 | 3 | +576 | -560 | 41.43 |
| 2026-11-10 | 389 | 464 | 6 | -75 | -635 | 29.59 |
| 2026-11-11 | 559 | 296 | 4 | +263 | -372 | 27.1 |
| 2026-11-12 | 216 | 640 | 3 | -424 | -796 | 19.92 |
| 2026-11-13 | 520 | 331 | 8 | +189 | -607 | 14.89 |
| 2026-11-16 | 227 | 627 | 5 | -400 | -1007 | 2.09 |
| 2026-11-17 | 161 | 697 | 1 | -536 | -1543 | -47.38 |
| 2026-11-18 | 369 | 487 | 3 | -118 | -1661 | -69.04 |
| 2026-11-19 | 73 | 783 | 3 | -710 | -2371 | -151.99 |
| 2026-11-20 | 174 | 682 | 4 | -508 | -2879 | -255.21 |

**A/D ratio 0.255 today** (174 advancing / 682 declining). Over the last 10 sessions the net advances total **-1743** and the ADL slope is **-255.21 net advances per session** (10-session A/D ratio 0.661). The ADL is cumulative from 2026-08-27, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (260 sessions, 2025-11-10 → 2026-11-20). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 16.74% | — | — |
| `breadth_pctile_1y` | 1.2 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 38.72% | — | — |
| `breadth_pctile_1y_50dma` | 16.5 | — | BELOW_NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 16.2 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +16.74 pp | BROAD | 64.6 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-16 | +51.46 |
| 2026-11-17 | +39.23 |
| 2026-11-18 | +36.90 |
| 2026-11-19 | +23.26 |
| 2026-11-20 | +16.74 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 256.61 | 276.23 | 278.26 | -7.78% | -4.75 |
| QQQ | 608.45 | 678.53 | 710.96 | -14.42% | -9.03 |
| QQQE | 105.41 | 114.95 | 117.80 | -10.52% | -8.09 |
| RSP | 207.44 | 218.08 | 214.80 | -3.43% | -3.34 |
| SPY | 689.81 | 747.81 | 760.18 | -9.26% | -8.72 |

## Live tape — 2026-11-23

Live quotes via the bridge's `market-recap` (Yahoo-sourced, cross-checked against a second quote source: 5/5, 16/16 and 5/5 agreement on the three pulls). Prices stamped 14:01–14:03 ET, one to three minutes after the fire clock.

| Instrument | Last | Chg % | Note |
|---|---|---|---|
| SPY | 722.55 | **+4.75%** | S&P 500 ETF |
| QQQ | 650.56 | **+6.92%** | Nasdaq-100 ETF |
| QQQE | 110.19 | +4.53% | Nasdaq-100 equal-weight |
| RSP | 212.70 | +2.53% | S&P 500 equal-weight — **2.22 pp behind SPY** |
| IWM | 265.03 | +3.28% | Russell 2000 |
| ^GSPC | 7,243.50 | +4.82% | S&P 500 index |
| NVDA | 164.83 | **+31.31%** | Huang reinstated as CEO — the driver of the day |
| MU | 707.81 | +19.06% | memory |
| TSM | 366.39 | +14.96% | foundry |
| AMD | 453.12 | +6.77% | |
| AVGO | 311.34 | +2.28% | |

Sector rotation (same pull):

| ETF | Chg % | | ETF | Chg % |
|---|---|---|---|---|
| SMH | **+14.42%** | | XLF | +2.13% |
| XLK | +8.72% | | XLV | +1.19% |
| XBI | +4.64% | | XLU | +1.18% |
| XLY | +4.31% | | XLRE | +0.84% |
| XLI | +3.84% | | XLP | -0.01% |
| XLC | +3.46% | | XLE | -0.47% |
| XLB | +2.85% | | | |

Cross-asset and overnight (bridge `market_snapshot`):

| Instrument | Level | Chg |
|---|---|---|
| ES=F S&P 500 future | 7,248 | +4.51% |
| US 10-year yield | 4.94% | +2.8 bp |
| DXY dollar index | 104.44 | +0.61% |
| WTI crude | 80.73 | -3.21% |
| Gold | 3,652.80 | +3.91% |
| Bitcoin | 61,477.75 | +0.52% |
| Nikkei 225 | 56,436.65 | **-5.06%** |
| Hang Seng | 22,383.74 | -0.12% |
| Shanghai Composite | 3,538.95 | +0.15% |
| FTSE 100 | 10,480.82 | +1.30% |
| DAX | 25,337.27 | +2.15% |

**The tape in one line:** a violent, concentrated relief rally in the AI complex after Friday's rout (Nasdaq Composite -5.3% and NVDA -14% on 2026-11-20, per Reuters and CBS), not a broad risk-on session — the equal-weight index gained roughly half of what SPY gained, two sectors were flat-to-red, and the Nikkei fell 5.06% in the same session. The corporate action behind it (Nvidia reinstating Jensen Huang as CEO) is reported by Reuters and CNN.

## Volatility — single pair, live

**One pair, used everywhere in this document.**

| Instrument | Level | vs prior settle |
|---|---|---|
| VIX | **27.09** | -24.52% (prior 35.89) |
| VIX3M | **25.47** | -22.84% (prior 33.01) |
| VIX / VIX3M | **1.0636** | front month **above** the 3-month — inverted |

Quote time **2026-11-23 13:45:00 ET**, source **Yahoo chart API** (`^VIX` and `^VIX3M` read from the **same** 5-minute bar stamped 13:45 ET, pinned to the 14:00:05 ET fire clock).

Reading: the volatility complex has collapsed along with the selloff — the front month is down 24.5% in one session — but the term structure is **still inverted** at 1.064, which is what sets `uncertainty: true`. A calm front month inside an inverted structure is a bounce, not a regime change. The Cboe delayed-quote CDN (the primary feed) answered HTTP 403 from this egress, so this is the Yahoo fallback rather than the venue's own print.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **RSP +2.53% vs SPY +4.75% (2.22 pp)** — the rebound is cap-weighted, the mirror image of the settled BROAD divergence. The equal-weight S&P is not confirming the index.
- **SMH +14.42% vs XLP -0.01% and XLE -0.47%** — roughly a 15 pp spread inside one session. A "market is up" reading hides that only the AI/semis complex moved; defensives and energy did not participate at all.
- **NVDA +31.31% on a single corporate-action headline** (Jensen Huang reinstated as CEO) — a name moving more than 30% on news is a source of index-level volatility, so today's index prints are not a clean read on market sentiment.
- **VIX 27.09 after a 35.89 settle (-24.52%)** — the volatility collapse is as violent as the selloff it follows, and with the pair still inverted at 1.064 the tape is not pricing calm.
- **Nikkei 225 -5.06% against a US +4.8%** — the session is a US/AI-specific relief rally; Asia did not confirm it, so the bounce is not yet a global risk-on signal.

## Method, source health & caveats

**Settled layer (2026-11-20)** — shibui over the MCP-over-HTTP bridge (`shibui.stock_data_query`): **ok**. shibui is T+1, so at the 14:00 ET fire its newest ingested session is **2026-11-20**; the 2026-11-23 close is not in the feed and no settled number in this artifact is from the fire session. Series: 260 sessions, 2025-11-10 → 2026-11-20, so the percentile windows are a full year of the same series.

**Universe** — NYSE/NASDAQ/AMEX, market cap > $10B taken from the latest `valuation` row: **860 names**. The universe is deliberately **not frozen** — the count has moved 909 → 866 → 860 across recent fires as valuation rows refresh. The advance/decline tally uses the **same** indicator-joined population as the breadth percentage, so advancing + declining + unchanged equals the published universe count (174 + 682 + 4 = 860).

**Live layer (2026-11-23)** — bridge `market-recap` (`get_quotes`, `market_snapshot`): **ok**, 5/5 agreement on the index pull, 16/16 on the sector pull and 5/5 on the single-name pull against the second quote source. Quotes stamped 14:01–14:03 ET.

**Volatility** — the Cboe delayed-quote CDN answered **HTTP 403** (Cloudflare "Attention Required") from this egress for every User-Agent. That is the **one degraded source of this run** (`degraded_sources: 1`); the pair falls back to Yahoo's chart API with both symbols read from the same 5-minute bar, pinned to the fire clock. The pair is published as one reading with its quote time, and it is never mixed with a settled close.

**MCP probe** — `catalog_ok total=135 finance_tools=0`: no finance MCP is registered on this runtime, so the bridge is the data path (the absent `mcp__*` tools are not an error).

**No live advance/decline tally is published.** Every advancing/declining figure in this artifact is the settled 2026-11-20 count; the live tape is published without an A/D number rather than with an unmeasured one.

**`atr_extensions`** carries all five index ETFs (SPY, RSP, QQQ, QQQE, IWM) on the `ticker` key the SQL emits, so `late_cycle` is computable rather than vacuously false. No probe returned empty.

**Layers kept separate** — the breadth percentages, the A/D tally and the percentile context describe the 2026-11-20 settled session; the tape, the cross-asset table and the volatility pair describe 2026-11-23 intraday. The 14:00 ET read and the 18:30 ET end-of-day read (`daily-screens/2026-11-23/breadth.md`, cron #09) are expected to differ.

**News context** — the day's driver (Nvidia reinstating Jensen Huang as CEO and president) and Friday's rout are sourced from Reuters, CNN and CBS reports carried by web search on 2026-11-23; they are context for the tape, not inputs to any breadth number. Every price, level and count in this artifact comes from the two layers described above.
