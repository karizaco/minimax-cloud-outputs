# Pre-Market Gapper — 2026-10-01

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 36 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 36 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **NXL** | NASDAQ | 7.55 | +104.9% | 14,092,562 | +16.8% | 6.3M | Health Technology |
| 2 | **RZAI** | NASDAQ | 26.31 | +47.6% | 87,028 | +128.0% | 1464.0M | Technology Services |
| 3 | **SDEV** | AMEX | 3.66 | +38.6% | 25,520,837 | +10.0% | 189.4M | Health Technology |
| 4 | **VEEA** | NASDAQ | 3.47 | +36.9% | 24,840,842 | +0.8% | 10.8M | Technology Services |
| 5 | **GIPR** | NASDAQ | 0.45 | +31.4% | 72,011,772 | +13.1% | 1.4M | Finance |
| 6 | **HXHX** | NASDAQ | 0.40 | +27.9% | 4,006,571 | +2.5% | 5.9M | Transportation |
| 7 | **MEDS** | NASDAQ | 4.06 | +22.7% | 18,666,771 | +3.8% | 12.9M | Distribution Services |
| 8 | **BTTC** | NASDAQ | 0.63 | +18.3% | 17,635,930 | -5.1% | 6.8M | Technology Services |
| 9 | **ACN** | NYSE | 212.30 | +17.3% | 2,270,103 | +0.3% | 129915.3M | Technology Services |
| 10 | **FLNA** | NASDAQ | 0.96 | +15.1% | 599,422 | +6.2% | 46.6M | Health Technology |
| 11 | **EFXT** | NYSE | 25.44 | +13.0% | 76,209 | +0.2% | 3106.3M | Producer Manufacturing |
| 12 | **QSI** | NASDAQ | 1.43 | +12.2% | 1,595,285 | +10.3% | 313.0M | Technology Services |
| 13 | **SCKT** | NASDAQ | 0.54 | +11.6% | 77,597,252 | +0.0% | 4.5M | Electronic Technology |
| 14 | **EJH** | NASDAQ | 1.79 | +10.6% | 1,105,546 | -1.4% | 5.7M | Consumer Services |
| 15 | **LPA** | AMEX | 2.91 | +10.5% | 198,160 | +9.1% | 92.2M | Finance |
| 16 | **INSG** | NASDAQ | 4.37 | +9.8% | 72,936 | +14.8% | 71.8M | Electronic Technology |
| 17 | **GLOB** | NYSE | 36.98 | +9.6% | 65,997 | +0.9% | 1596.8M | Technology Services |
| 18 | **AISP** | NASDAQ | 2.22 | +9.1% | 479,358 | +1.1% | 76.5M | Technology Services |
| 19 | **QNME** | NASDAQ | 0.54 | +8.9% | 4,021,630 | -1.5% | 18.5M | Transportation |
| 20 | **SDOT** | NASDAQ | 11.76 | +8.3% | 145,837 | +4.7% | 17.1M | Consumer Services |
| 21 | **CTSH** | NASDAQ | 60.88 | +7.9% | 187,323 | -1.5% | 27423.0M | Technology Services |
| 22 | **WVE** | NASDAQ | 3.88 | +7.6% | 111,678 | +0.3% | 764.5M | Health Technology |
| 23 | **SNPS** | NASDAQ | 490.54 | +7.3% | 95,456 | +1.9% | 94005.4M | Technology Services |
| 24 | **PMAX** | NASDAQ | 0.94 | +7.3% | 5,561,769 | +0.0% | 1.8M | Communications |
| 25 | **FICO** | NYSE | 661.75 | +7.2% | 126,612 | -0.3% | 14292.2M | Commercial Services |
| 26 | **ABAT** | NASDAQ | 2.28 | +6.8% | 10,654,865 | +0.9% | 325.1M | Non-Energy Minerals |
| 27 | **AIB** | AMEX | 1.52 | +6.7% | 555,490 | +8.3% | 115.5M | Technology Services |
| 28 | **VUZI** | NASDAQ | 2.88 | +6.5% | 102,669 | +2.6% | 243.5M | Electronic Technology |
| 29 | **QNC** | AMEX | 1.74 | +6.1% | 107,144 | +7.4% | 381.7M | Electronic Technology |
| 30 | **WETO** | NASDAQ | 1.12 | +5.9% | 794,643 | +14.8% | 1.2M | Transportation |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: NXL, RZAI, SDEV, VEEA, GIPR.
