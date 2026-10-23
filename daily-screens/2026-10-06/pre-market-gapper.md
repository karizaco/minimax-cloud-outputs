# Pre-Market Gapper — 2026-10-06

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 42 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 42 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **FRGT** | NASDAQ | 0.32 | +168.0% | 137,366,161 | +34.7% | 0.2M | Finance |
| 2 | **IPDN** | NASDAQ | 4.61 | +102.6% | 30,688,218 | -0.7% | 3.1M | Commercial Services |
| 3 | **OLOX** | NASDAQ | 1.25 | +64.8% | 34,210,099 | +115.9% | 2.1M | Producer Manufacturing |
| 4 | **JAGX** | NASDAQ | 5.62 | +38.5% | 8,862,331 | +22.6% | 10.9M | Health Technology |
| 5 | **OPCH** | NASDAQ | 31.00 | +32.8% | 11,613,988 | +21.2% | 4643.3M | Health Services |
| 6 | **APOG** | NASDAQ | 40.00 | +18.9% | 83,591 | -4.6% | 834.7M | Producer Manufacturing |
| 7 | **AXG** | NASDAQ | 0.11 | +16.0% | 126,730,276 | +8.0% | 21.6M | Finance |
| 8 | **AIFA** | NASDAQ | 7.67 | +13.9% | 82,041 | +0.4% | 49.2M | Consumer Services |
| 9 | **PRME** | NASDAQ | 3.50 | +12.5% | 399,167 | +1.2% | 634.8M | Health Technology |
| 10 | **CIRC** | NASDAQ | 0.50 | +12.2% | 2,052,126 | +11.4% | 56.7M | Health Technology |
| 11 | **QTEX** | NASDAQ | 1.59 | +11.0% | 26,489,404 | +19.5% | 106.6M | Health Technology |
| 12 | **AIIO** | NASDAQ | 1.13 | +9.0% | 20,873,278 | +0.9% | 134.5M | Consumer Durables |
| 13 | **BRUN** | NASDAQ | 15.17 | +8.9% | 510,254 | +0.1% | 1271.9M | Technology Services |
| 14 | **CEG** | NASDAQ | 300.40 | +8.5% | 579,090 | +3.4% | 106433.9M | Utilities |
| 15 | **OSTX** | AMEX | 1.49 | +8.1% | 2,250,103 | +2.5% | 69.7M | Health Technology |
| 16 | **SRFM** | NYSE | 1.01 | +7.8% | 984,826 | +2.2% | 124.9M | Transportation |
| 17 | **WHLR** | NASDAQ | 0.91 | +7.3% | 7,203,817 | +42.2% | 0.5M | Finance |
| 18 | **RUBI** | NASDAQ | 0.65 | +7.2% | 24,101,401 | +17.1% | 0.8M | Transportation |
| 19 | **BIAF** | NASDAQ | 6.06 | +7.0% | 51,351 | -4.7% | 7.1M | Health Technology |
| 20 | **BRN** | AMEX | 0.96 | +6.7% | 7,831,145 | +12.0% | 13.8M | Energy Minerals |
| 21 | **PENN** | NASDAQ | 15.91 | +6.3% | 69,200 | +1.3% | 2133.0M | Consumer Services |
| 22 | **XHLD** | NASDAQ | 0.62 | +6.3% | 4,213,415 | +1.9% | 7.5M | Commercial Services |
| 23 | **XNDU** | NASDAQ | 5.06 | +6.2% | 1,379,375 | +1.6% | 1549.8M | Electronic Technology |
| 24 | **VERI** | NASDAQ | 0.75 | +6.1% | 223,381 | +3.5% | 75.0M | Commercial Services |
| 25 | **CLF** | NYSE | 12.25 | +5.9% | 261,961 | +0.5% | 6989.1M | Non-Energy Minerals |
| 26 | **LW** | NYSE | 47.91 | +5.9% | 390,998 | +0.6% | 6586.7M | Consumer Non-Durables |
| 27 | **PSQL** | NASDAQ | 6.84 | +5.8% | 60,797 | +0.2% | 1452.1M | Electronic Technology |
| 28 | **CTVA** | NYSE | 13.91 | +5.7% | 656,032 | +2.5% | 9282.1M | Process Industries |
| 29 | **PL** | NYSE | 18.57 | +5.4% | 417,413 | +0.9% | 6756.7M | Technology Services |
| 30 | **RZLV** | NASDAQ | 2.15 | +5.4% | 1,917,854 | +0.9% | 896.3M | Technology Services |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: FRGT, IPDN, OLOX, JAGX, OPCH.
