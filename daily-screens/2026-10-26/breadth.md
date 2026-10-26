# Breadth & regime — 2026-10-26

- **Session:** 2026-10-26 US/Eastern close (no lag)
- **Sources:** TradingView public scanner (S&P 500 membership from the Wikipedia constituent list, 502 tickers) + Yahoo Finance daily bars

## Breadth

| Metric | Value |
|---|---|
| S&P 500 members evaluated | 502 |
| Above 20-DMA | 358 |
| Below 20-DMA | 143 |
| No data | 1 |
| **% above 20-DMA** | **71.46%** |
| Cross-check vs Yahoo-computed SMA20 | 40/40 agree |

## Index ATR extension (late-cycle test)

| Symbol | Close | ATR% | Median ATR% (252d) | Extension | Last bar |
|---|---|---|---|---|---|
| SPY | 765.37 | 0.947% | 1.014% | 0.93× | 2026-10-26 |
| RSP | 217.29 | 0.952% | 1.012% | 0.94× | 2026-10-26 |
| QQQ | 712.20 | 1.735% | 1.615% | 1.07× | 2026-10-26 |
| QQQE | 118.06 | 1.405% | 1.284% | 1.09× | 2026-10-26 |
| IWM | 276.99 | 1.309% | 1.597% | 0.82× | 2026-10-26 |

**Max extension 1.09× — late_cycle = False** (threshold is 6×).

## Volatility

| Leg | Value | Note |
|---|---|---|
| VIX | 18.39 (-5.45% vs prior close) | last bar 2026-10-26 |
| VXV | no_close_bars | Yahoo returns 0 bars for `^VXV` and `^VXVCLS`; the VIX/VXV ratio needs both legs, so `uncertainty` is left null rather than inferred. |

## Sector ETF relative strength (Hernandez theme → group)

| Rank | ETF | Sector | Perf 1M | Perf 3M | Perf 6M | Composite | > 20-DMA |
|---|---|---|---|---|---|---|---|
| 1 | XLE | Energy | 12.47% | 19.23% | 19.49% | 51.19 | yes |
| 2 | XLV | Healthcare | 5.50% | 8.01% | 26.02% | 39.52 | yes |
| 3 | XLK | Electronic Technology | -4.71% | 8.83% | 17.31% | 21.42 | no |
| 4 | XLP | Consumer Defensive | 8.05% | 1.02% | 6.28% | 15.35 | yes |
| 5 | XLF | Financial | 2.55% | -1.94% | 7.46% | 8.07 | yes |
| 6 | XLY | Consumer Cyclical | 3.24% | 2.33% | -1.68% | 3.89 | yes |
| 7 | XLB | Basic Materials | 3.21% | -1.19% | -0.21% | 1.81 | yes |
| 8 | XLU | Utilities | 7.97% | -7.22% | -7.64% | -6.89 | yes |
| 9 | XLRE | Real Estate | 2.44% | -7.30% | -2.17% | -7.03 | yes |
| 10 | XLI | Industrial | -1.52% | -8.58% | -2.51% | -12.60 | no |
| 11 | XLC | Communication Services | -8.47% | -4.14% | -10.12% | -22.73 | no |

Composite = Perf.1M + Perf.3M + Perf.6M (equal weight). The top 3 ETFs define the themes used by `hernandez_theme_group`.

## Regime payload

```json
{
  "cron_date": "2026-10-26",
  "data_date": "2026-10-23",
  "generated": "2026-10-26T18:08Z",
  "size_cut_pct": 0,
  "uncertainty": false,
  "uncertainty_note": "VIX/VIX3M ratio 0.950 (^VIX3M used as the long-end proxy; ^VXV returns 0 bars on Yahoo)",
  "late_cycle": false,
  "late_cycle_note": "code rule: any index ETF >6% above its 50-DMA (max 0.55%); max ATR%/median multiple = 1.09x",
  "vix": 19.45,
  "vix_bar_date": "2026-10-23",
  "vix3m": 20.48,
  "vix_ratio": 0.95,
  "breadth_pct_above_sma20_spx": 69.7,
  "breadth_denominator_note": "actual S&P 500 constituents (502 of 503, BRK.B, BF.B, VYLR missing) \u2014 prior runs used a mcap > $10B proxy because no constituents table was available",
  "indices_below_sma20": [
    "SPY",
    "QQQ",
    "QQQE",
    "IWM"
  ],
  "index_detail": {
    "SPY": {
      "close": 759.97,
      "sma20": 770.15,
      "sma50": 767.81,
      "ext_from_50_pct": -1.02,
      "atr_pct": 0.94,
      "atr_x_median": 0.91,
      "bars": 499
    },
    "RSP": {
      "close": 216.54,
      "sma20": 212.66,
      "sma50": 215.35,
      "ext_from_50_pct": 0.55,
      "atr_pct": 0.96,
      "atr_x_median": 0.95,
      "bars": 499
    },
    "QQQ": {
      "close": 704.4,
      "sma20": 735.24,
      "sma50": 725.81,
      "ext_from_50_pct": -2.95,
      "atr_pct": 1.71,
      "atr_x_median": 1.06,
      "bars": 499
    },
    "QQQE": {
      "close": 117.17,
      "sma20": 119.98,
      "sma50": 120.41,
      "ext_from_50_pct": -2.69,
      "atr_pct": 1.4,
      "atr_x_median": 1.09,
      "bars": 499
    },
    "IWM": {
      "close": 275.75,
      "sma20": 277.19,
      "sma50": 286.41,
      "ext_from_50_pct": -3.72,
      "atr_pct": 1.34,
      "atr_x_median": 0.82,
      "bars": 499
    }
  },
  "live_session_overlay": {
    "as_of": "2026-10-26 14:08 ET",
    "spx_pct_above_sma20_intraday": 72.1,
    "vix": 18.48,
    "vix3m": 19.97,
    "vix_ratio_intraday": 0.925,
    "indices": {
      "SPY": {
        "live": 765.83,
        "chg_pct": 0.77,
        "above_sma20_now": false
      },
      "RSP": {
        "live": 217.17,
        "chg_pct": 0.29,
        "above_sma20_now": true
      },
      "QQQ": {
        "live": 713.99,
        "chg_pct": 1.36,
        "above_sma20_now": false
      },
      "QQQE": {
        "live": 118.35,
        "chg_pct": 1.0,
        "above_sma20_now": false
      },
      "IWM": {
        "live": 277.55,
        "chg_pct": 0.65,
        "above_sma20_now": true
      }
    }
  }
}
```

Interpretation: breadth is healthy, so `size_cut_pct` is 0 even though SPY, QQQ, QQQE and IWM closed below their 20-DMA — the size-cut rule requires BOTH an index below its 20-DMA AND breadth under 40%. No index is near the 6× ATR-extension threshold, so `late_cycle` is false. The uncertainty flag is uncomputable this session because the VXV leg is missing.
