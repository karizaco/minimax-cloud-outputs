# Breadth / regime — 2026-10-21

- **Generated**: 2026-10-22T11:33:57Z (cron date 2026-10-22)
- **Source**: TradingView scanner + Yahoo Finance chart API + CBOE VIX history
- **Universe**: 2928 names (close>$3, mcap>$300M, avg30 vol>100k, non-OTC)

## Breadth

The skill specifies a large-cap ($10B+) proxy for S&P 500 constituents because shibui has no index-membership table. The same proxy is used here.

| Measure | Value | n |
|---|---|---|
| % of >$10B names above 20-DMA | **65.82%** | 869 |
| % of >$10B names above 50-DMA | 48.1% | 869 |
| % of >$10B names above 200-DMA | 51.82% | — |
| % of full universe above 20-DMA | 55.19% | 2928 |
| % of full universe above 50-DMA | 38.65% | 2926 |

## Index extension from the 50-DMA (ATR units)

| Symbol | Close | 50-DMA | ATR% | Ext (ATR) | % from 50-DMA |
|---|---|---|---|---|---|
| SPY | 773.09 | 768.34 | 0.915 | **0.67** | 0.62% |
| RSP | 216.64 | 215.53 | 0.930 | **0.55** | 0.51% |
| QQQ | 725.20 | 726.75 | 1.553 | **-0.14** | -0.21% |
| QQQE | 119.37 | 120.67 | 1.331 | **-0.82** | -1.08% |
| IWM | 276.48 | 287.49 | 1.403 | **-2.84** | -3.83% |

All five last-bar dates: 2026-10-21.

## Volatility

- **VIX close (2026-10-21, CBOE official)**: **16.68** (source: cdn.cboe.com, 9,299 daily rows)

- **VIX/VXN term-structure proxy**: **0.7482** — below 1.0, i.e. no term-structure inversion.

> **The skill's VIX/VXVCLS ratio could not be computed this run.** Yahoo returns no `timestamp` array for `^VXV` and 404s on `^VIXCLS`; CBOE's `VXV_History.csv` redirects to `cdn-api.cboe.com` and returns **403 AccessDenied**. `^VXN` (NASDAQ-100 vol) is used as the substitute denominator. Per the zero-fallback policy this was not chased further — the `uncertainty` flag below is therefore a *proxy*, not the specified test.

> **Data conflict, unresolved:** Yahoo's `^VIX` quote returned 18.27 stamped 2026-10-22 11:18 UTC, which contradicts CBOE's official 2026-10-21 close of 16.68. The pre-market timestamp and the ~9.5% gap indicate a stale or mis-stamped Yahoo quote. **CBOE is treated as authoritative and 16.68 is used.** Not smoothed over.

## Regime flags

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | 50 when index < 20-DMA AND breadth < 40% |
| `uncertainty` | **false** | true when vol ratio > 1 (proxy: VIX/VXN) |
| `late_cycle` | **false** | true when any index > 6x ATR extension |

Breadth 65.82% above the 20-DMA clears the <40% threshold, so `size_cut_pct` stays 0. No index is below its 20-DMA. 

