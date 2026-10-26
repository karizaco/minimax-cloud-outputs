<!-- cron #10 stock-screener-breadth-snapshot | cron_date=2026-10-26 | data_date=2026-10-23 | _source=yahoo_chart_api_fallback | generated=2026-10-26T18:20Z -->
# Breadth & regime — 2026-10-23 close (cron date 2026-10-26)

**69.7% of the S&P 500 closed above its 20-DMA** on the 2026-10-23 settle, and 72.1% are above it on the in-progress 2026-10-26 session. No regime flag fires: `size_cut_pct` = 0, `uncertainty` = false, `late_cycle` = false. The one thing worth flagging is a divergence, not a level — stock-level breadth is healthy while four of the five index ETFs closed *below* their 20-DMA, because mega-cap tech is dragging the cap-weighted indices down while the median constituent is fine.

**Degraded path — read this before trusting the numbers.** Every Tier-1 MCP for this skill (`shibui-finance`, `tradingview-advanced`, `financekit`) is **not registered in this cloud sandbox**, so the skill's breadth SQL was re-implemented on the Yahoo public chart API. Three consequences: (1) the breadth denominator is the **real S&P 500 constituent list (502 of 503 names)**, not the `mcap > $10B` proxy earlier runs used — so this 69.7% is **not directly comparable** to the 65.3% printed in the 2026-10-23 run; (2) `^VXV` returns zero bars on Yahoo, so `^VIX3M` is used as the long-end proxy exactly as `screen.py:compute_regime()` prescribes, which makes the `uncertainty` flag computable for the first time; (3) sector rotation is computed from sector-ETF price performance rather than the `financekit` call.

## Breadth

| Measure | 2026-10-23 close | 2026-10-26 (in progress) |
| --- | --- | --- |
| S&P 500 above 20-DMA | 69.7% (350 / 502) | 72.1% (362 / 502) |
| S&P 500 above 50-DMA | 58.0% | 59.0% |
| Index ETFs below their 20-DMA | 4 of 5 (SPY, QQQ, QQQE, IWM) | 3 of 5 (SPY, QQQ, QQQE) |
| Names below their own 20-DMA | 152 of 502 | 140 of 502 |

Breadth at 69.7% is not a stressed tape. The index/breadth divergence is the signal: 69.7% of names hold their 20-DMA, yet SPY closed 1.02% below its 50-DMA and QQQ 2.95% below, because the cap-weighted indices are being dragged by a mega-cap tech complex that is in the middle of a drawdown (see sector table). Breadth above 50-DMA at 58.0% confirms the average stock is intact — this is concentration risk in the index, not distribution risk across the market.

## Index detail

| Index | Close (10/23) | 20-DMA | 50-DMA | Ext from 50 | ATR% | ATR× median | Live 10/26 | Live vs 20-DMA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.97 | 770.15 | 767.81 | -1.02% | 0.94 | 0.91 | 765.83 (+0.77%) | -0.56% |
| RSP | 216.54 | 212.66 | 215.35 | +0.55% | 0.96 | 0.95 | 217.17 (+0.29%) | +2.12% |
| QQQ | 704.40 | 735.24 | 725.81 | -2.95% | 1.71 | 1.06 | 713.99 (+1.36%) | -2.89% |
| QQQE | 117.17 | 119.98 | 120.41 | -2.69% | 1.40 | 1.09 | 118.35 (+1.00%) | -1.36% |
| IWM | 275.75 | 277.19 | 286.41 | -3.72% | 1.34 | 0.82 | 277.55 (+0.65%) | +0.13% |

Only RSP sits above both its 20-DMA and 50-DMA, which is the equal-weight tell: the average stock is trending, the cap-weighted index is not. IWM remains the weakest structure (-3.72% from its 50-DMA, ATR×median 0.82 — the most compressed volatility in the group) and is the one that just turned back above its 20-DMA intraday on a +0.65% move. QQQ's ATR×median of 1.06 is the most elevated of the five, so the tech bounce is happening on the highest-volatility leg of the group.

The Monday session so far is a broad risk-on move (all five indices green), but it is not yet a breadth *regime* change: SPY is still 0.56% below its 20-DMA and QQQ 2.89% below, so the 3-of-5-below count improves only because IWM crossed back over.

## Volatility

| Measure | 2026-10-23 close | 2026-10-26 live |
| --- | --- | --- |
| ^VIX | 19.45 | 18.48 |
| ^VIX3M | 20.48 | 19.97 |
| VIX / VIX3M | 0.950 | 0.925 |

The front end is trading *below* the 3-month term, so there is no front-end stress signal: `uncertainty` = false. The ratio has been drifting down through the session (0.950 → 0.925) as the bid comes back, which is consistent with the equity rally rather than a vol-bid melt-up. Note the long end (VIX3M) is the higher of the two legs — the market is pricing a somewhat elevated multi-month horizon, which is a different concern from immediate stress.

## Sector rotation

| Sector | ETF | Perf 1M | Perf 3M | Perf 6M | Composite | Members above 20-DMA | Ext from 50-DMA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Energy | XLE | +10.75% | +18.80% | +21.91% | +17.15 | 85.7% | +7.76% |
| Health Care | XLV | +5.54% | +9.72% | +24.34% | +13.20 | 93.3% | +4.77% |
| Consumer Staples | XLP | +8.03% | +3.40% | +6.04% | +5.82 | 90.9% | +4.60% |
| Information Technology | XLK | -5.90% | +5.12% | +14.36% | +4.53 | 38.7% | -3.38% |
| Financials | XLF | +2.51% | -1.72% | +8.71% | +3.17 | 76.3% | -0.31% |
| Materials | XLB | +3.28% | -0.16% | -1.17% | +0.65 | 79.2% | +0.58% |
| Consumer Discretionary | XLY | +2.52% | +2.04% | -4.71% | -0.05 | 63.8% | -0.30% |
| Utilities | XLU | +8.13% | -6.83% | -7.84% | -2.18 | 87.1% | +1.65% |
| Real Estate | XLRE | +2.21% | -6.97% | -2.87% | -2.55 | 80.0% | -0.71% |
| Industrials | XLI | -2.49% | -10.14% | -4.55% | -5.73 | 60.2% | -4.42% |
| Communication Services | XLC | -7.44% | -2.00% | -8.68% | -6.04 | 40.9% | -5.46% |

Rotation is defensive-to-commodity, not growth: Energy and Health Care occupy the top two composite slots, and the two sectors with the worst member breadth are exactly the two that have dragged the indices (Technology 38.7% of members above their 20-DMA, Communication Services 40.9%). Industrials is the structural laggard on 3-month performance (-10.14%) with 60.2% breadth. The Monday rally being tech-led (+1.36% in QQQ) is a bounce inside a downtrend for that complex, not a leadership rotation — Communication Services and Technology are still the two worst 1-month performers on the board.

## Regime flags

| Flag | Value | Rule |
| --- | --- | --- |
| `size_cut_pct` | **0** | 50 when a majority of index ETFs are < 20-DMA **and** breadth < 40%. 4 of 5 indices are below, but breadth is 69.7%, so the second condition fails. |
| `uncertainty` | **false** | VIX / VIX3M > 1. Ratio is 0.950 (0.925 intraday). |
| `late_cycle` | **false** | Any index ETF > 6% above its 50-DMA. Max is +0.55% (RSP); max ATR% vs 252-day median is 1.09×. |

No position-sizing action is implied by this snapshot. The `size_cut_pct` rule is intentionally two-legged, and the breadth leg vetoes it: a broad market sitting on its 20-DMAs is a different animal from four index ETFs punching below theirs with internals deteriorating, which is not what the tape shows.

## Method & caveats

- **Data source.** Yahoo Finance public chart API (`query2.finance.yahoo.com/v8/finance/chart`, range 1y–2y, 1d interval, browser UA). 521 of 521 requests succeeded on the first attempt; zero rate-limit events, zero retries. The skill's Tier-1 MCPs (`mcp__shibui-finance__stock_data_query`, `mcp__tradingview-advanced__yahoo_price`, `mcp__financekit__sector_rotation`) are absent from this sandbox's tool registry, and `mcode-tools connector tools` returns only media-generation and email connectors — so this is a documented fallback, not a choice.
- **Pipeline validation.** The implementation was checked against the prior published run (`daily-screens/2026-10-23/breadth.md`, data date 2026-10-22) and reproduces its close, 20-DMA, 50-DMA, 50-DMA extension and ATR% **exactly** for all five ETFs. It also revealed the pipeline's ATR convention: ATR(14) is the *simple mean of True Range*, not Wilder smoothing — the earlier `_breadth_raw.json` values reproduce only under the simple-mean definition. The `ATR× median` column drifts ~0.01–0.03 versus the prior run (median-window definition), which is immaterial to the 6× `late_cycle` threshold.
- **Data lag.** Primary figures are on the **2026-10-23** settle (the most recent completed bar). The 2026-10-26 session was still open at the time of the run (~14:2x ET); its values appear only in the explicitly labeled live columns. The `live` breadth column uses today's partial close against 20-DMAs computed through 2026-10-23.
- **Constituent coverage.** 502 of 503 S&P 500 constituents produced usable history. `VYLR` returned insufficient history and is excluded from every denominator. Sector membership uses the GICS sector from the Wikipedia constituent table, which can lag an index reclassification by a few days.
- **Definition notes.** `Perf.1M / 3M / 6M` are computed on **trading sessions** (22 / 64 / 127 bars), not calendar months, so they differ slightly from a vendor's calendar-month return. Composite = equal-weight mean of the three, matching the skill's equal-weight RS convention.
- **Not computed.** `^VXV` and `^VXVCLS` return zero bars on Yahoo, so the VIX/VXV ratio is unavailable; `^VIX3M` is used as the long-end proxy per `screen.py:compute_regime()`. The `mcap > $10B` breadth proxy from the skill's SQL was not reproduced — no market-cap source is available in this sandbox — so the headline uses actual S&P 500 membership instead.

## Files

- `breadth-snapshot.md` — this report.
- `breadth-snapshot.json` — full computed payload: per-index detail, sector rotation, live-session overlay, regime.
- `breadth-snapshot.csv` — per-constituent rows (close, 20/50-DMA, breadth flags, 1M/3M performance, ATR%), `_source=yahoo_chart_api_fallback`.
- `_regime.json` — the regime contract payload consumed by the 18:30 ET daily sweep and the 07:37 ET pre-market brief. The sweep's copy is authoritative; this one will be overwritten on the same date.
