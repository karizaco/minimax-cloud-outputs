# Pre-Market Gapper — 2026-10-08

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 26 of 26 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (26 shown, top of 26 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **FLYE** | NASDAQ | 2.32 | +149.6% | 60,368,871 | +13.4% | 3.8M | Consumer Durables |
| 2 | **PCRX** | NASDAQ | 36.39 | +44.1% | 6,046,124 | +0.4% | 1450.6M | Health Technology |
| 3 | **MRNO** | NASDAQ | 0.26 | +43.0% | 45,373,685 | +69.4% | 20.7M | Consumer Services |
| 4 | **OLB** | NASDAQ | 0.55 | +31.7% | 83,838,230 | +31.4% | 13.2M | Technology Services |
| 5 | **IPW** | NASDAQ | 0.92 | +25.5% | 18,229,509 | +66.3% | 1.2M | Retail Trade |
| 6 | **HELE** | NASDAQ | 26.55 | +22.5% | 148,210 | -0.1% | 618.4M | Consumer Durables |
| 7 | **HYPR** | NASDAQ | 0.94 | +15.7% | 4,295,492 | +4.8% | 99.7M | Health Technology |
| 8 | **PROF** | NASDAQ | 6.91 | +15.3% | 549,332 | +20.8% | 252.4M | Health Technology |
| 9 | **SOAR** | AMEX | 0.31 | +13.9% | 41,822,693 | +3.2% | 16.5M | Transportation |
| 10 | **HAE** | NYSE | 119.47 | +13.1% | 89,450 | -0.2% | 5435.5M | Health Technology |
| 11 | **WOLF** | NYSE | 31.02 | +11.6% | 1,300,836 | +17.1% | 1641.9M | Electronic Technology |
| 12 | **RCKT** | NASDAQ | 2.63 | +9.3% | 94,309 | +2.6% | 288.7M | Health Technology |
| 13 | **MEDS** | NASDAQ | 3.40 | +6.9% | 5,394,271 | +2.1% | 10.8M | Distribution Services |
| 14 | **RNA** | NASDAQ | 8.26 | +6.9% | 78,009 | +7.8% | 141.3M | Health Technology |
| 15 | **FNGR** | NASDAQ | 0.20 | +6.8% | 20,465,574 | +5.0% | 15.2M | Technology Services |
| 16 | **GLND** | NASDAQ | 2.60 | +6.3% | 133,009 | -2.6% | 113.9M | Finance |
| 17 | **ENLV** | NASDAQ | 0.28 | +6.1% | 6,750,176 | +26.9% | 4.8M | Health Technology |
| 18 | **NCPL** | NASDAQ | 1.31 | +5.7% | 221,560 | -4.4% | 10.3M | Commercial Services |
| 19 | **CYAB** | NASDAQ | 0.17 | +5.3% | 703,827 | +0.4% | 3.0M | Technology Services |
| 20 | **SKYQ** | NASDAQ | 2.52 | +5.3% | 108,083 | +1.6% | 22.3M | Energy Minerals |
| 21 | **FRGT** | NASDAQ | 0.26 | +5.1% | 1,818,686 | +22.2% | 0.2M | Finance |
| 22 | **SRFM** | NYSE | 0.93 | +4.9% | 340,209 | +2.4% | 123.5M | Transportation |
| 23 | **KAPA** | AMEX | 0.96 | +4.5% | 156,404 | +1.4% | 3.2M | Health Technology |
| 24 | **RYDE** | AMEX | 0.67 | +4.2% | 52,387 | -3.0% | 111.9M | Technology Services |
| 25 | **AISP** | NASDAQ | 2.29 | +4.2% | 108,371 | -1.4% | 78.9M | Technology Services |
| 26 | **QS** | NASDAQ | 4.58 | +4.2% | 952,999 | -1.1% | 2835.5M | Producer Manufacturing |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: FLYE, PCRX, MRNO, OLB, IPW.
