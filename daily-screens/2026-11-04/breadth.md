---
fire_time_et: 2026-11-04 18:30:54 ET
cron: #09 stock-screener-daily-sweep-18:30
data_date: 2026-11-04 (settled regular-session close; feed is NOT T+1 for this file — every number below is the 2026-11-04 close)
data_date_t_plus_1: false
breadth_universe: "NYSE/NASDAQ/AMEX, TradingView type=stock, market_cap_basic > $10B — 1,001 names (totalCount 1001, 1001 fetched, 1001 unique). No domicile filter; type=stock includes REITs."
breadth_universe_source: "POST https://scanner.tradingview.com/america/scan (settled close columns SMA20/SMA50/SMA200/ATR)"
vix_quote_time: "2026-11-04T16:15:01 ET — VIX and VIX3M from the Cboe delayed-quote CDN (cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json and _VIX3M.json)"
vix: 16.61
vix3m: 18.80
vix_ratio: 0.8835
cross_reference: "intraday counterpart: daily-screens/2026-11-04/breadth-snapshot.md (cron #10, 14:00 ET)"
read_type: "END-OF-DAY read from the settled close — this file is authoritative for 2026-11-04 breadth; breadth-snapshot.md is the 14:00 ET intraday snapshot and is expected to differ"
---

# Breadth & regime — 2026-11-04 (end-of-day)

**One volatility pair is used everywhere in this document: VIX 16.61 / VIX3M 18.80, both stamped 2026-11-04T16:15:01 ET by the Cboe delayed-quote CDN.** No second reading is mixed in.

## Headline

Breadth was strong and the tape was broad: **71.0%** of the 1,001-name large-cap universe closed above its 20-DMA and **756 names advanced vs 243 declined**. The index complex tells a more divided story — only **2 of the 5** index ETFs (RSP, IWM) sit above their 20-DMA, so the *index* is below its 20-day mean even though the *breadth* is not. That split is the reason `size_cut_pct` stays at 0: the regime rule fires only when BOTH conditions hold (index below 20-DMA **and** breadth < 40%), and breadth came in at 71%.

| Metric | Value | Rule |
|---|---|---|
| % large caps above 20-DMA | **71.0%** (711/1,001) | size-cut needs < 40% → not triggered |
| % large caps above 50-DMA | 59.6% | — |
| % large caps above 200-DMA | 54.7% | — |
| Advance / decline (universe) | 756 / 243 / 2 | — |
| Median change (universe) | +2.22% | — |
| Index ETFs above 20-DMA | **40.0%** (2 of 5) | < 50% → index_below_20sma = true |
| VIX / VIX3M | **0.8835** | > 1.0 → uncertainty; **false** |
| Max ATR extension from 50-DMA | RSP +3.88% | > 6% → late_cycle; **false** |

## Regime payload (`_regime.json`)

```json
{
  "size_cut_pct": 0,
  "uncertainty": false,
  "late_cycle": false,
  "breadth_pct_spx": 71.0,
  "index_below_20sma": true,
  "vix": 16.61,
  "vix3m": 18.80,
  "atr_extensions": {
    "SPY":  {"extension_pct": -0.03},
    "RSP":  {"extension_pct": 3.88},
    "QQQ":  {"extension_pct": -4.37},
    "QQQE": {"extension_pct": -1.84},
    "IWM":  {"extension_pct": 0.29}
  }
}
```

## Index ETFs — settled 2026-11-04 close

| ETF | Close | Day % | 20-DMA | 50-DMA | Extension from 50-DMA | Above 20-DMA |
|---|---|---|---|---|---|---|
| SPY | 766.81 | **+1.65%** | 767.57 | 767.06 | -0.03% | no (by 0.10%) |
| RSP | 223.33 | **+1.86%** | 216.32 | 214.99 | +3.88% | yes |
| QQQ | 691.95 | +0.97% | 717.42 | 723.56 | -4.37% | no |
| QQQE | 117.38 | +1.23% | 118.60 | 119.58 | -1.84% | no |
| IWM | 284.02 | +1.51% | 277.44 | 283.19 | +0.29% | yes |

RSP (equal-weight) outperforming SPY (cap-weight) by 21bp is the cleanest statement of the session: the average stock beat the mega-cap index, and breadth confirms it. QQQ remains the laggard — 3.6% below its 20-DMA.

## Sector rotation — median relative strength of the large-cap universe

| Sector (TV taxonomy) | n | % > 20-DMA | Perf 1M | Perf 3M | Perf 6M | Median day |
|---|---|---|---|---|---|---|
| Health Technology | 73 | 90.4% | +12.6% | +15.2% | +31.2% | +3.10% |
| Health Services | 16 | 93.8% | +12.4% | +11.9% | +21.1% | +4.78% |
| Commercial Services | 23 | 82.6% | +19.5% | +8.5% | +15.6% | +2.96% |
| Technology Services | 96 | 46.3% | +2.2% | +9.4% | +22.0% | +1.97% |
| Consumer Non-Durables | 34 | 94.1% | +15.1% | +4.4% | +10.7% | +4.32% |
| Retail Trade | 32 | 87.5% | +15.5% | +7.9% | +3.8% | +5.34% |
| Consumer Durables | 19 | 100.0% | +16.4% | +4.4% | +5.7% | +5.12% |
| Consumer Services | 39 | 92.3% | +13.1% | +3.0% | +9.1% | +4.71% |
| Energy Minerals | 23 | **4.3%** | +2.7% | +8.6% | +11.6% | **-5.17%** |
| Process Industries | 23 | 73.9% | +13.0% | +1.9% | +6.4% | +3.35% |
| Electronic Technology | 87 | **31.0%** | **-11.3%** | **-10.1%** | -8.4% | -3.77% |
| Producer Manufacturing | 54 | 51.9% | -2.5% | -8.4% | -2.0% | -0.60% |

Health care and consumer led; **semis and energy were sold**. Electronic Technology is the weakest sector on every horizon (1M -11.3%) with only 31% of names above their 20-DMA, and Energy Minerals has 4.3% above its 20-DMA with a -5.17% median day.

## Sector ETF read-through (same 2026-11-04 close)

| ETF | Day % | 1M | 3M | 6M |
|---|---|---|---|---|
| XLV (health) | +3.06% | +14.3% | +14.2% | +31.2% |
| XLP (staples) | +3.36% | +14.2% | +6.5% | +8.8% |
| XLF (financials) | +3.51% | +10.7% | +1.4% | +14.6% |
| XLY (cons. disc.) | +4.26% | +11.4% | +3.1% | +1.7% |
| XLRE (real estate) | +3.32% | +10.7% | -0.9% | +1.3% |
| XLC (comm.) | +3.47% | -4.8% | -5.6% | -10.3% |
| **XLE (energy)** | **-4.74%** | +1.2% | +8.8% | +13.7% |
| **SMH (semis)** | **-2.75%** | **-20.1%** | -10.8% | -8.6% |
| XLK (tech) | -0.01% | -11.9% | -3.7% | +2.9% |
| XLI (industrials) | -1.09% | -0.1% | -9.2% | -3.2% |
| GDX (miners) | **+9.01%** | -3.7% | +2.6% | -9.2% |
| TAN (solar) | +5.65% | +4.8% | -9.9% | -24.8% |
| JETS (airlines) | +6.70% | +4.4% | -11.2% | +6.5% |
| IBB (biotech) | +2.63% | +7.7% | +14.2% | +30.4% |
| XBI (biotech) | +2.67% | +2.3% | +3.3% | +18.8% |
| RSP | +1.86% | +6.4% | +1.4% | +9.2% |
| SPY | +1.65% | -0.4% | -0.4% | +4.3% |
| IWM | +1.51% | +0.7% | -5.2% | -0.0% |
| QQQ | +0.97% | -7.7% | -2.7% | -1.1% |

GDX +9.0% and TAN +5.7% against XLE -4.7% is a genuine split inside energy: the move is in metals and in a recovering solar complex, not in the integrated/energy sector.

## Cross-check against the T+1 shibui feed (2026-11-03 session)

The stylist screens in this directory run on shibui, whose newest settled session on the cron day is **2026-11-03**. Its own breadth read for that session:

| | shibui 2026-11-03 | TradingView 2026-11-04 |
|---|---|---|
| Large-cap population | 905 names | 1,001 names |
| % above 20-DMA | 63.98% | 71.0% |
| Index ETFs above 20-DMA | 40% (2 of 5) | 40% (2 of 5) |
| SPY ATR extension | -1.65% | -0.03% |
| QQQ ATR extension | -5.34% | -4.37% |
| RSP ATR extension | +2.00% | +3.88% |

The two feeds agree on the shape — the index is below its 20-DMA while breadth is not, and QQQ is the weakest major index — but the populations differ (905 vs 1,001 names) because the market-cap source differs (shibui `valuation` vs TradingView `market_cap_basic`). **Do not treat the two breadth percentages as the same series.**

## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` (large-cap universe, indices, volume breakout, sector ETFs, movers) | ok — totalCount 1001, fetched 1001, 1001 unique | close, SMA20/50/200, ATR, Perf 1M/3M/6M, sector, market cap |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json`, `_VIX3M.json` (+5 index ETFs) | ok — `last_trade_time` 2026-11-04T16:15:01 / 15:59:59 | VIX, VIX3M, index closes (independent of TV) |
| shibui via MCP bridge | `stock_data_query` — breadth SQL | ok — 7 rows | T+1 cross-check (2026-11-03) |
| Nasdaq `/info` | `api.nasdaq.com/api/quote/{SYM}/info` | ok — 15/15 names | official 4 PM close cross-check (see below) |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | no finance MCP registered; the bridge is the finance path |
| Finviz | — | not attempted | known Cloudflare 403 from this egress |
| Yahoo JSON | — | not used | — |

**Close-source verification.** On 15 Focus/Tier-A names, TradingView's `close` was compared against Nasdaq's official 4:00 PM close (`secondaryData`): **15 of 15 matched** (e.g. MRNA 258.38, ECG 79.71, LSCC 107.25, FTAI 179.58, GPK 11.75). Nasdaq's `primaryData` on the same pulls was the *after-hours* print stamped 18:36 ET, not the official close — `primaryData` must not be used for a settled close.

## Caveats

- The breadth universe is a **market-cap proxy**, not an index membership list: shibui has no S&P-500 table and TradingView's `market_cap_basic` does not equal the index's float-adjusted cap. 1,001 names at $10B+ is the population stated above, not "the market".
- `type=stock` includes REITs and foreign-domiciled US listings; no domicile filter was applied (filtering on domicile drops ADR/Canadian listings that are genuine constituents of the traded universe).
- Sector labels are **TradingView's taxonomy** (Health Technology, Commercial Services, …), not GICS.
- ATR extension here is `(close − SMA50) / SMA50`, the same formula the skill's breadth SQL uses; the skill's "6×" late-cycle test is applied to that percentage, not to an ATR multiple.
