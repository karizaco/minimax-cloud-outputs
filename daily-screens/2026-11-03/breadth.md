---
fire_time_et: 2026-11-03 18:30 ET
data_date: 2026-11-02 (shibui breadth feed; T+1 — shibui has not ingested the 2026-11-03 session)
breadth_universe: NYSE/NASDAQ/AMEX, market_cap > $10B, close > $3, 902 names
vix_quote_time: 2026-11-03T16:15:01 ET (CBOE delayed-quote CDN, settled cash close; VIX3M 2026-11-03T16:15:01 ET)
cross_reference: intraday counterpart: daily-screens/2026-11-03/breadth-snapshot.md (cron #10, 14:00 ET)
volatility_pair: VIX 20.83 / VIX3M 21.27 (ratio 0.9793) — single pair, used everywhere in this file
---

# Breadth & regime — end-of-day read

**Cron #09 stock_screener_daily_sweep_18_30** · fire 2026-11-03 18:30 ET · generated 2026-11-03 19:43:47 ET

## Self-description

| Field | Value |
|---|---|
| Fire time (ET) | 2026-11-03 18:30 ET |
| Breadth data date | 2026-11-02 — shibui feed is **T+1**; the 2026-11-03 session is not yet ingested |
| Breadth universe | NYSE/NASDAQ/AMEX, market cap > $10B, close > $3 — **902 names** |
| % above 20-DMA | **65.19%** |
| % above 50-DMA | 61.09% |
| Index ETFs above their own 20-DMA | 2% of 5 (SPY, RSP, QQQ, QQQE, IWM) |
| VIX / VIX3M | 20.83 / 21.27 = 0.9793 (-1.51% / -1.53%) |
| VIX quote time / feed | 2026-11-03T16:15:01 ET · CBOE delayed-quote CDN (settled close) |
| Cross-reference | intraday counterpart: daily-screens/2026-11-03/breadth-snapshot.md (cron #10, 14:00 ET) |

> The breadth percentages describe the **2026-11-02** session (shibui's latest ingested bar). The volatility pair is the **2026-11-03** settled close — one pair only, quoted consistently throughout this artifact. The two are one session apart by construction, not by accident.

## Regime flags (skill contract)

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | 0 | 50 only when the indices sit below their 20-DMA **and** large-cap breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 (front-end stress vs the long end) |
| `late_cycle` | false | any index ETF more than 6% above its 50-DMA |

Size-cut is **not** triggered: the index ETFs are in a weak posture (only 2% of the 5 sit above their 20-DMA on 2026-11-02) but large-cap breadth is 65.19%, well above the 40% gate. The volatility ratio of 0.9793 is below 1.0, so the uncertainty band is not formally triggered either.

## Index extension (shibui, 2026-11-02)

| Symbol | Close | SMA20 | SMA50 | ATR% | ATR% 252d median | % vs SMA50 | ATR ext. multiple |
|---|---|---|---|---|---|---|---|
| SPY | 752.1 | 769.33 | 767.22 | 1.07 | 1.079 | -1.97 | 0.991 |
| RSP | 219.98 | 215.34 | 215.02 | 0.949 | 1.041 | 2.31 | 0.911 |
| QQQ | 681.09 | 724.43 | 724.35 | 1.934 | 1.593 | -5.97 | 1.214 |
| QQQE | 115.89 | 119.18 | 119.8 | 1.432 | 1.284 | -3.26 | 1.115 |
| IWM | 279.14 | 277.2 | 283.86 | 1.381 | 1.689 | -1.66 | 0.817 |

No index ETF is more than 6% above its 50-DMA, so `late_cycle` is false. The ATR-extension multiples (current ATR% ÷ 252-session median ATR%) run 0.82x–1.21x — no stretched index.

## Session close for reference (2026-11-03, CBOE delayed-quote CDN)

| Symbol | Close | Change | | Symbol | Close | Change |
|---|---|---|---|---|---|---|
| SPY 754.35 +0.30%  | | | QQQE 115.95 +0.05%  | |
| QQQ 685.28 +0.62%  | | | DIA 517.06 -0.44%  | |
| RSP 219.26 -0.33%  | | | SMH 518.52 +2.01%  | |
| IWM 279.79 +0.23%  | | | _SPX 7,568.92 +0.36%  | |

VIX 20.83 (-1.51%) · VIX3M 21.27 (-1.53%) · ratio 0.9793 · quote time 2026-11-03T16:15:01 ET.

## Sector rotation — top themes by equal-weight 1M+6M relative strength (shibui, 2026-11-02)

| Theme ETF | Close | 1M % | 6M % | rel 1M | rel 6M | composite |
|---|---|---|---|---|---|---|
| XLV | 184.6 | 13.78 | 27.17 | 14.52 | 22.81 | 18.66 |
| XLE | 67.25 | 14.39 | 14.27 | 15.13 | 9.91 | 12.52 |
| XLP | 90.83 | 7.04 | 7.91 | 7.77 | 3.55 | 5.66 |
| XLF | 57.56 | 0.31 | 10.86 | 1.05 | 6.5 | 3.77 |
| XLB | 53.67 | 5.21 | 4.52 | 5.95 | 0.15 | 3.05 |
| XLK | 174.22 | -2.15 | 7.63 | -1.41 | 3.27 | 0.93 |
| XLY | 118.16 | -0.04 | -0.4 | 0.69 | -4.76 | -2.03 |
| XLRE | 43.64 | -3.41 | -1.53 | -2.67 | -5.9 | -4.29 |
| XLU | 43.67 | -1.56 | -6.19 | -0.82 | -10.55 | -5.69 |
| XLI | 169.71 | -7.34 | -1.88 | -6.61 | -6.24 | -6.43 |
| XLC | 100.26 | -9.95 | -14.1 | -9.22 | -18.47 | -13.84 |

## Source health

| Source | Query / URL | Status |
|---|---|---|
| shibui (MCP-over-HTTP bridge) | breadth + ATR SQL, data_date 2026-11-02, 902-name large-cap universe | ok |
| shibui (MCP-over-HTTP bridge) | 868-candidate indicator + skip-flag pass, data_date 2026-11-02 | ok |
| shibui (MCP-over-HTTP bridge) | sweep SQL — stockbee / qullamaggie / peoplewish / CANSLIM rebuild | ok |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` — 868/868 candidate closes for 2026-11-03 | ok |
| CBOE delayed-quote CDN | `quotes/{sym}.json` (SPX, NDX, RUT, DJX, VIX, VIX3M, 6 index ETFs, 11 sector ETFs) | ok |
| connector catalog probe | `probe_mcp.py` | catalog_ok total=135 finance_tools=0 |

## Method

- Breadth = share of the large-cap universe trading above its own 20-DMA on the shibui session (NYSE/NASDAQ/AMEX, market cap > $10B, close > $3).
- Index extension uses shibui's `technical_indicators` (sma_20, sma_50, atr_14) joined to `stock_quotes` on (symbol, date).
- The skill's own `compute_regime()` is used verbatim so the flags here and in `_regime.json` cannot drift apart.
- The skill's shipped breadth SQL computes `atr_252d_avg` inside a CTE already filtered to one date, so its partition holds a single row; the true ATR multiple is recomputed here over a real 252-session window.
