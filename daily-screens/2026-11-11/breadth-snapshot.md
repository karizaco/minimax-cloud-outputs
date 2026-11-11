---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-11 14:00:54 ET"
data_date: "2026-11-10"
live_date: "2026-11-11"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 905 names"
vix_quote_time: "2026-11-11 13:47:31 ET (Cboe delayed-quote CDN, _VIX.json / _VIX3M.json)"
vix_pair: "VIX 17.34 / VIX3M 19.34 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-11/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-10 · universe 905 names · breadth 67.40% (pctile 88.9 · ABOVE_NORMAL) · divergence +27.40 pp (BROAD) · AD 402/497/6_

# Breadth & Regime Snapshot — Wednesday, 11 November 2026 (intraday, cron #10)

Intraday breadth snapshot fired 2026-11-11 14:00:54 ET with the US cash session open. The breadth layer is the **2026-11-10 settled session** (shibui is T+1, so the newest closed session it carries is the prior one); the tape and the volatility pair are **live on 2026-11-11**. Source of record: shibui over the MCP-over-HTTP bridge for the settled layer, `market-recap` get_quotes for the live tape, the Cboe delayed-quote CDN for the volatility pair. Cross-reference: the end-of-day counterpart for this same session is cron #09's `daily-screens/2026-11-11/breadth.md` (18:30 ET).

## TL;DR

- **Breadth level is healthy but yesterday's session was soft.** 67.40% of the 905 large caps closed 2026-11-10 above their own 20-DMA — the 88.9th percentile of its own trailing year (ABOVE_NORMAL), and 63.31% above the 50-DMA (77.9th pctile, NORMAL). The session itself was negative underneath that level: **402 advancing / 497 declining / 6 unchanged (A/D ratio 0.81)**.
- **The one metric that changes position sizing: `breadth_divergence` = +27.40 pp, band BROAD.** The average large cap is materially healthier than the index — only **2 of the 5 index ETFs** sat above their own 20-DMA on 2026-11-10. The index is the weak leg, not the megacaps' strength. The spread has narrowed hard from its +56.13 pp extreme on 2026-11-06 but has held +27 pp for two sessions.
- **Caveat that changes how to read it: today's live tape is the opposite shape — cap-weighted and tech-led.** At 14:03 ET SPY is +1.61% while RSP (equal weight) is only +0.80%, with XLK +4.24% and SMH +6.31%. If that settles, it *narrows* the BROAD gap recorded above rather than extending it, so the settled divergence is a 2026-11-10 reading, not a live posture.

## Breadth — 2026-11-10 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 905 |
| Above 20-DMA | 610 (67.40%) |
| Below 20-DMA | 295 (32.60%) |
| Above 50-DMA | 573 (63.31%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 402 advancing / 497 declining / 6 unchanged (A/D ratio 0.809) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **905 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-28 | 467 | 433 | 5 | +34 | -1476 | 47.56 |
| 2026-10-29 | 672 | 233 | 0 | +439 | -1037 | 68.96 |
| 2026-10-30 | 375 | 529 | 1 | -154 | -1191 | 70.28 |
| 2026-11-02 | 593 | 312 | 0 | +281 | -910 | 63.58 |
| 2026-11-03 | 359 | 544 | 2 | -185 | -1095 | 64.28 |
| 2026-11-04 | 653 | 251 | 1 | +402 | -693 | 87.85 |
| 2026-11-05 | 155 | 748 | 2 | -593 | -1286 | 80.23 |
| 2026-11-06 | 385 | 514 | 6 | -129 | -1415 | 40.7 |
| 2026-11-09 | 759 | 143 | 3 | +616 | -799 | 41.76 |
| 2026-11-10 | 402 | 497 | 6 | -95 | -894 | 30.65 |

**A/D ratio 0.809 today** (402 advancing / 497 declining). Over the last 10 sessions the net advances total **+616** and the ADL slope is **+30.65 net advances per session** (10-session A/D ratio 1.147). The ADL is cumulative from 2026-08-17, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-27 → 2026-11-10). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 67.40% | — | — |
| `breadth_pctile_1y` | 88.9 | — | ABOVE_NORMAL |
| `breadth_pct_50dma` | 63.31% | — | — |
| `breadth_pctile_1y_50dma` | 77.9 | — | NORMAL |
| `index_etfs_above_20dma` | 2 of 5 | 43.1 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +27.40 pp | BROAD | 78.6 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-04 | +29.17 |
| 2026-11-05 | +38.56 |
| 2026-11-06 | +56.13 |
| 2026-11-09 | +27.73 |
| 2026-11-10 | +27.40 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 280.58 | 277.27 | 281.58 | -0.35% | -0.22 |
| QQQ | 674.76 | 700.86 | 719.39 | -6.20% | -4.01 |
| QQQE | 115.12 | 117.09 | 118.87 | -3.15% | -2.49 |
| RSP | 220.88 | 217.49 | 214.82 | +2.82% | 2.78 |
| SPY | 749.92 | 760.69 | 765.00 | -1.97% | -1.9 |

## Live tape — 2026-11-11

| Symbol | Last | Chg % | Session range | Volume | As of (ET) |
|---|---|---|---|---|---|
| SPY | 761.97 | **+1.61%** | 754.91 – 762.51 | 18,353,794 | 14:03:40 |
| QQQ | 694.42 | **+2.91%** | 683.60 – 695.57 | 28,705,913 | 14:03:39 |
| QQQE | 117.95 | +2.46% | 116.37 – 118.08 | 115,439 | 14:01:25 |
| RSP | 222.64 | **+0.80%** | 220.92 – 222.71 | 4,128,553 | 14:03:21 |
| IWM | 283.37 | +0.99% | 281.49 – 283.72 | 10,015,283 | 14:03:41 |
| DIA | 524.52 | +0.53% | 520.07 – 524.63 | 1,709,103 | 14:03:36 |
| XLK | 176.07 | **+4.24%** | 172.51 – 176.49 | 9,253,370 | 14:03:38 |
| SMH | 514.13 | **+6.31%** | — | 10,518,340 | 14:03:37 |
| XLE | 63.11 | +1.45% | 62.35 – 63.26 | 15,697,375 | 14:03:14 |
| XLI | 171.29 | +1.52% | — | 3,918,385 | 14:03:38 |
| XLF | 58.55 | +0.44% | 58.02 – 58.55 | 10,629,197 | 14:03:31 |
| XBI | 156.32 | +0.81% | — | 3,555,195 | 14:03:36 |
| XLV | 188.26 | −0.33% | 186.85 – 188.27 | 5,347,741 | 14:03:30 |
| XLY | 121.14 | +0.07% | — | 4,003,781 | 14:03:34 |
| XLP | 90.86 | −0.19% | — | 10,209,317 | 14:03:37 |
| XLU | 43.74 | +0.02% | — | 8,285,135 | 14:03:37 |
| XLB | 52.98 | +0.25% | — | 3,309,662 | 14:03:37 |
| HYG | 77.37 | +0.24% | — | 8,604,731 | 14:03:39 |
| TLT | 80.85 | −0.04% | — | 16,697,597 | 14:03:28 |
| GLD | 365.41 | −1.07% | — | 3,767,528 | 14:03:41 |

Source: `market-recap` `get_quotes` over the MCP-over-HTTP bridge, 22/22 symbols found, retrieved 2026-11-11T19:03:42Z (14:03:42 ET), all `market_state: open`. **The live tape and the settled breadth are two different instants and are never blended**: the numbers above are 2026-11-11 intraday, the breadth table above them is the 2026-11-10 close.

**Leadership read on the live tape:** the move is concentrated. QQQ +2.91% versus RSP +0.80% is a 2.1 pp cap-weight gap, and semis (SMH +6.31%) and tech (XLK +4.24%) account for most of it, while the defensive and rate-sensitive corners did nothing (XLU +0.02%, XLP −0.19%, XLV −0.33%, XLY +0.07%). Gold fell 1.07% and bonds were flat, so this is an equity-risk-on tape funded out of gold, not a flight to safety.

## Volatility — single pair, live

| Instrument | Last | Prev close | Chg % | Quote time (ET) |
|---|---|---|---|---|
| VIX | **17.34** | 19.46 | −10.89% | 2026-11-11 13:47:31 |
| VIX3M | **19.34** | 20.64 | −6.30% | 2026-11-11 13:47:31 |

**One pair, used everywhere in this document: VIX 17.34 / VIX3M 19.34**, from the Cboe delayed-quote CDN (`_VIX.json` / `_VIX3M.json`), quoted at 13:47:31 ET on 2026-11-11 — a regular-hours live print, not a settled close. The pair was pulled twice and both pulls returned the identical values (`vix_stable: true`).

The **term structure is inverted**: VIX3M 19.34 sits **2.00 points above** VIX 17.34 (ratio 0.897), so `uncertainty` is **false** under the contract's rule (VIX/VIX3M > 1.0) and the front-matter flag is `false`. Forward vol above spot is the market pricing a calmer, better-supplied tape ahead than the current session is delivering — consistent with the -10.9% drop in VIX on the day.

Cross-check: the bridge's own `^VIX` quote read 17.35 at 13:48:31 ET, one cent from the CDN print — the two independent paths agree, so the pair is not a single-source artefact.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **`QQQE` — live print on 115,439 shares.** That is roughly 1/160th of SPY's volume and ~1/250th of QQQ's, so its +2.46% live move is a thin-book print. QQQE is one of the **five ETFs in the divergence denominator**, so its settled 20-DMA state carries a fifth of the index-ETF share — treat the QQQE leg as the least reliable of the five.
- **`^VXN` — stale quote in the bridge's index path.** `^VXN` came back stamped `2026-11-10T21:00:00Z` (yesterday's close), not the live session, while `^VIX` came back live at 18:48:31Z. The Nasdaq-100 volatility index is therefore **not used** in this artifact; the volatility section quotes the Cboe pair only.
- **`SPY` — the two layers sit on different instants.** In the settled layer SPY closed 2026-11-10 **1.97% below its own 50-DMA**; in the live tape SPY is +1.61% above its prior close at 14:03 ET. Read together they say the index is recovering toward its 50-DMA, but they are two different sessions and one different hour — do not collapse them into a trend.
- **`XLK` / `SMH` — the tape is one-sector concentrated.** XLK +4.24% and SMH +6.31% are the two largest moves in the tape and the only ones above +5%; a single-sector impulse like this can lift the cap-weighted index while the equal-weight basket barely moves (RSP +0.80%). The BROAD divergence recorded for 2026-11-10 is the opposite condition and is the reason the two layers are labelled separately.

## Method, source health & caveats

| Source | Query / URL | Status | Result |
|---|---|---|---|
| shibui (MCP-over-HTTP bridge, `stock_data_query`) | `shibui.stock_quotes` + `shibui.technical_indicators` + `shibui.valuation`, schema-qualified, paged with `rows_passing` asserted on every page | ok | settled layer — 262 sessions 2025-10-27 → 2026-11-10 |
| Cboe delayed-quote CDN | `https://cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` and `_VIX3M.json`, pulled twice | ok | VIX 17.34 / VIX3M 19.34 @ 13:47:31 ET, `vix_stable: true` |
| `market-recap` `get_quotes` (MCP-over-HTTP bridge) | 22 symbols (index ETFs, sector ETFs, HYG/TLT/GLD, ^VIX/^VXN) | ok | 22/22 found, retrieved 14:03:42 ET, all `market_state: open` |
| MCP catalog probe (`probe_mcp.py`) | connector catalog | ok | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier, fmp, market-recap` |
| Yahoo JSON / Nasdaq API / TradingView scanner | — | not attempted | the bridge carried every field this artifact publishes; no fallback was needed |

**The settled-vs-live split.** The breadth percentage, the advance/decline tally, the ADL, the percentiles and the divergence are all computed from the **2026-11-10 settled close** — shibui is T+1, so on this fire day its newest closed session is the prior one, and `data_date` says so explicitly. The live tape and the volatility pair are **2026-11-11 intraday**. Nothing in the settled layer is re-stated from the live tape.

**The universe is not frozen.** `NYSE/NASDAQ/AMEX · market cap > $10B · market_cap from the latest valuation row` = **905 names** today. The cap floor is applied to the latest `valuation` row, so the count drifts as those rows refresh (904 → 902 → 905 → 909 across four November sessions); today's count is unchanged from the 905 published for 2026-11-03. The advance/decline tally uses the **same** population as the breadth percentage (the indicator-joined large-cap set), so 402 + 497 + 6 = 905 exactly.

**Percentile windows.** `breadth_pctile_1y` is the rank of today's level in the trailing 262-session (≈1 year) distribution of the same series; the 50-DMA split and the index-ETF count carry their own percentiles. The divergence percentile uses the same window. The CSV's percentile columns are expanding — each row against every session from the start of the window to that row.

**`atr_extensions` is populated, not empty.** The five index-ETF rows are present and the map is non-empty (SPY −1.97%, QQQ −6.20%, QQQE −3.15%, RSP +2.82%, IWM −0.35% from their own 50-DMAs), so `late_cycle` is a computed flag and not a silently-empty `any()` over an empty map. `index_below_20sma` is **true** (2 of 5 index ETFs above their own 20-DMA) and `size_cut_pct` is **0** because the size-cut rule needs the index below its 20-DMA *and* breadth below 40%, and breadth is 67.40%.

**What could not be verified.** There is no second volatility source for VIX3M (the Cboe CDN is the only path that serves it), so the term structure rests on one feed — the `^VIX` cross-check covers the front leg only. The bridge's `^VXN` print was stale and was discarded. The live tape carries no advance/decline tally: this artifact's A/D is the settled 2026-11-10 tally, and no live A/D figure is claimed. The volume figures in the live tape are intraday cumulative and are not final — the closing auction consolidates later.
