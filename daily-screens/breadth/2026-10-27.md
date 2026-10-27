# Breadth & regime — 2026-10-27

- **Session:** 2026-10-27 US/Eastern close (no lag)
- **Sources:** TradingView public scanner (S&P 500 membership from the Wikipedia constituent list, 502 tickers) + Yahoo Finance daily bars

## Breadth

| Metric | Value |
|---|---|
| S&P 500 members evaluated | 502 |
| Above 20-DMA | 366 |
| Below 20-DMA | 135 |
| No data | 1 |
| **% above 20-DMA** | **73.05%** |
| Cross-check vs Yahoo-computed SMA20 | 40/40 agree |

## Index ATR extension (late-cycle test)

| Symbol | Close | ATR% | Median ATR% (252d) | Extension | Last bar |
|---|---|---|---|---|---|
| SPY | 769.66 | 0.946% | 1.029% | 0.92× | 2026-10-27 |
| RSP | 217.52 | 0.918% | 1.012% | 0.91× | 2026-10-27 |
| QQQ | 721.25 | 1.740% | 1.628% | 1.07× | 2026-10-27 |
| QQQE | 119.31 | 1.379% | 1.304% | 1.06× | 2026-10-27 |
| IWM | 280.18 | 1.272% | 1.597% | 0.80× | 2026-10-27 |

**Max extension 1.07× — late_cycle = False** (threshold is 6×).

## Volatility

| Leg | Value | Note |
|---|---|---|
| VIX | 17.52 (-4.73% vs prior close) | last bar 2026-10-27 |
| VXV | no_close_bars | Yahoo returns 0 bars for `^VXV` and `^VXVCLS`; the VIX/VXV ratio needs both legs, so `uncertainty` is left null rather than inferred. |

## Sector ETF relative strength (Hernandez theme → group)

| Rank | ETF | Sector | Perf 1M | Perf 3M | Perf 6M | Composite | > 20-DMA |
|---|---|---|---|---|---|---|---|
| 1 | XLE | Energy | 10.16% | 15.45% | 17.20% | 42.81 | yes |
| 2 | XLV | Healthcare | 5.44% | 7.20% | 24.71% | 37.34 | yes |
| 3 | XLK | Electronic Technology | -3.09% | 10.74% | 18.69% | 26.34 | no |
| 4 | XLP | Consumer Defensive | 7.05% | 0.94% | 4.63% | 12.62 | yes |
| 5 | XLF | Financial | 2.30% | -2.46% | 8.48% | 8.32 | yes |
| 6 | XLY | Consumer Cyclical | 4.32% | 3.13% | -2.57% | 4.87 | yes |
| 7 | XLB | Basic Materials | 4.02% | -1.07% | 1.69% | 4.64 | yes |
| 8 | XLU | Utilities | 8.73% | -6.36% | -6.54% | -4.17 | yes |
| 9 | XLRE | Real Estate | 1.58% | -7.83% | -2.53% | -8.78 | yes |
| 10 | XLI | Industrial | -0.95% | -7.23% | -2.08% | -10.26 | no |
| 11 | XLC | Communication Services | -8.71% | -5.42% | -9.93% | -24.05 | no |

Composite = Perf.1M + Perf.3M + Perf.6M (equal weight). The top 3 ETFs define the themes used by `hernandez_theme_group`.

## Regime payload

```json
{
  "size_cut_pct": 0,
  "uncertainty": null,
  "late_cycle": false
}
```

Interpretation: breadth is healthy, so `size_cut_pct` is 0 even though SPY, QQQ, QQQE and IWM closed below their 20-DMA — the size-cut rule requires BOTH an index below its 20-DMA AND breadth under 40%. No index is near the 6× ATR-extension threshold, so `late_cycle` is false. The uncertainty flag is uncomputable this session because the VXV leg is missing.
