# Pre-Market Gapper — 2026-09-29

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 47 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 47 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **BKYI** | NASDAQ | 3.12 | +100.0% | 58,021,320 | +25.0% | 4.5M | Technology Services |
| 2 | **SSTI** | NASDAQ | 8.21 | +51.5% | 1,417,525 | +2.0% | 108.1M | Technology Services |
| 3 | **SLND** | AMEX | 0.69 | +50.6% | 114,593,177 | +0.0% | 37.6M | Industrial Services |
| 4 | **SANG** | NASDAQ | 4.93 | +39.3% | 967,023 | +36.5% | 164.1M | Electronic Technology |
| 5 | **SLXN** | NASDAQ | 0.32 | +28.6% | 141,314,804 | +71.9% | 3.5M | Health Technology |
| 6 | **MSGY** | NASDAQ | 4.44 | +28.1% | 12,470,496 | +6.4% | 9.4M | Industrial Services |
| 7 | **NCPL** | NASDAQ | 1.22 | +23.2% | 1,340,642 | +5.6% | 9.6M | Commercial Services |
| 8 | **SMMT** | NASDAQ | 16.39 | +22.0% | 2,018,107 | +26.4% | 13075.1M | Health Technology |
| 9 | **MITQ** | AMEX | 0.59 | +19.6% | 224,729 | -3.8% | 5.9M | Consumer Durables |
| 10 | **JELD** | NYSE | 1.99 | +16.9% | 228,713 | +4.5% | 172.7M | Non-Energy Minerals |
| 11 | **IOVA** | NASDAQ | 14.45 | +16.5% | 2,468,914 | +0.1% | 6545.4M | Health Technology |
| 12 | **XRPN** | NASDAQ | 12.90 | +14.2% | 196,483 | +7.0% | 407.5M | Finance |
| 13 | **QMLS** | NASDAQ | 6.53 | +14.0% | 438,328 | -1.3% | 218.5M | Technology Services |
| 14 | **AVAT** | NASDAQ | 1.90 | +13.8% | 346,562 | +3.0% | 83.1M | Finance |
| 15 | **CCL** | NYSE | 25.11 | +10.2% | 4,112,984 | +0.2% | 34391.9M | Consumer Services |
| 16 | **NVTS** | NASDAQ | 11.73 | +9.1% | 2,836,671 | +12.5% | 3062.6M | Electronic Technology |
| 17 | **FFAI** | NASDAQ | 1.30 | +8.5% | 7,499,808 | +22.0% | 8.0M | Consumer Durables |
| 18 | **NAUT** | NASDAQ | 1.36 | +8.1% | 3,031,125 | +2.7% | 173.7M | Health Technology |
| 19 | **FCEL** | NASDAQ | 16.90 | +7.7% | 356,454 | +0.2% | 1351.2M | Electronic Technology |
| 20 | **KMX** | NYSE | 59.23 | +7.5% | 633,443 | +0.8% | 8405.4M | Retail Trade |
| 21 | **ZONE** | AMEX | 0.13 | +7.5% | 677,773 | +4.0% | 28.9M | Distribution Services |
| 22 | **BLMN** | NASDAQ | 8.06 | +7.3% | 72,024 | +2.0% | 690.1M | Consumer Services |
| 23 | **DUO** | NASDAQ | 0.64 | +7.3% | 274,755 | +10.7% | 24.6M | Technology Services |
| 24 | **AIXC** | NASDAQ | 1.01 | +7.2% | 82,019 | +5.4% | 21.3M | Technology Services |
| 25 | **DEFT** | NASDAQ | 0.49 | +7.2% | 76,065 | +1.7% | 190.2M | Finance |
| 26 | **CAPS** | NASDAQ | 0.16 | +7.2% | 54,115,491 | -2.4% | 3.4M | Distribution Services |
| 27 | **RCL** | NYSE | 260.67 | +7.0% | 67,544 | +0.1% | 69716.7M | Consumer Services |
| 28 | **UEC** | AMEX | 9.29 | +7.0% | 472,354 | +0.8% | 4597.4M | Non-Energy Minerals |
| 29 | **BNC** | NASDAQ | 5.87 | +6.9% | 201,433 | +1.1% | 241.7M | Producer Manufacturing |
| 30 | **PN** | NASDAQ | 2.84 | +6.9% | 629,219 | +0.8% | 41.9M | Utilities |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: BKYI, SSTI, SLND, SANG, SLXN.
