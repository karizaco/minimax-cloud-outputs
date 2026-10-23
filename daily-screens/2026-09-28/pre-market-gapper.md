# Pre-Market Gapper — 2026-09-28

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 33 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 33 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **SOAR** | AMEX | 0.32 | +118.1% | 285,020,477 | +0.9% | 17.1M | Transportation |
| 2 | **KOD** | NASDAQ | 89.92 | +90.6% | 3,072,639 | +9.7% | 2033.2M | Health Technology |
| 3 | **CLRO** | NASDAQ | 5.10 | +68.1% | 9,876,346 | +50.7% | 13.6M | Consumer Durables |
| 4 | **GYGY** | NASDAQ | 0.87 | +63.6% | 54,411,335 | +96.0% | 12.6M | Technology Services |
| 5 | **MIMI** | NASDAQ | 0.90 | +34.9% | 12,945,701 | +25.8% | 13.3M | Commercial Services |
| 6 | **ARAY** | NASDAQ | 0.30 | +34.6% | 172,039,996 | +32.5% | 35.8M | Health Technology |
| 7 | **MEDS** | NASDAQ | 3.81 | +25.4% | 10,123,160 | +0.0% | 12.1M | Distribution Services |
| 8 | **WBUY** | NASDAQ | 0.90 | +25.0% | 25,878,732 | +2.1% | 4.9M | Retail Trade |
| 9 | **LABT** | NASDAQ | 1.15 | +23.4% | 22,397,474 | +0.6% | 2.7M | Health Technology |
| 10 | **DLXY** | NASDAQ | 2.44 | +20.4% | 71,950 | +8.4% | 40.9M | Distribution Services |
| 11 | **MX** | NYSE | 3.79 | +16.7% | 710,558 | +10.6% | 138.4M | Electronic Technology |
| 12 | **AMPX** | NYSE | 9.60 | +14.9% | 1,794,236 | -0.7% | 1402.4M | Producer Manufacturing |
| 13 | **ONCO** | NASDAQ | 1.11 | +14.7% | 10,589,692 | +7.8% | 4.9M | Health Technology |
| 14 | **SDEV** | AMEX | 1.57 | +14.4% | 5,871,250 | +19.5% | 79.5M | Health Technology |
| 15 | **NYXH** | NASDAQ | 1.59 | +11.0% | 50,721 | +1.4% | 161.9M | Health Technology |
| 16 | **FFAI** | NASDAQ | 1.41 | +10.7% | 728,889 | +9.3% | 8.6M | Consumer Durables |
| 17 | **MGLD** | AMEX | 1.97 | +9.4% | 493,332 | +3.6% | 84.1M | Miscellaneous |
| 18 | **PMAX** | NASDAQ | 1.26 | +9.3% | 11,969,420 | +0.0% | 2.5M | Communications |
| 19 | **CRMT** | NASDAQ | 1.03 | +8.6% | 79,282 | +1.9% | 8.6M | Retail Trade |
| 20 | **LOBO** | NASDAQ | 0.58 | +8.3% | 298,323 | +1.8% | 8.4M | Consumer Durables |
| 21 | **ROC** | NASDAQ | 4.22 | +7.7% | 55,519 | -1.0% | 80.5M | Technology Services |
| 22 | **BUR** | NYSE | 3.93 | +7.1% | 110,548 | +7.7% | 863.0M | Finance |
| 23 | **TONX** | NASDAQ | 3.98 | +7.1% | 100,920 | +0.7% | 219.2M | Technology Services |
| 24 | **SHMD** | NASDAQ | 4.38 | +6.4% | 457,043 | +14.4% | 291.3M | Electronic Technology |
| 25 | **SG** | NYSE | 8.24 | +5.8% | 55,496 | -0.5% | 980.9M | Consumer Services |
| 26 | **TRSG** | NASDAQ | 1.22 | +5.7% | 690,394 | +10.7% | 20.0M | Producer Manufacturing |
| 27 | **COSM** | NASDAQ | 0.37 | +5.2% | 399,131 | -1.3% | 37.3M | Health Technology |
| 28 | **MAIA** | AMEX | 1.18 | +5.0% | 56,745 | +1.7% | 71.8M | Health Technology |
| 29 | **MSGY** | NASDAQ | 3.13 | +4.8% | 1,762,245 | -25.6% | 17.1M | Industrial Services |
| 30 | **TOVX** | AMEX | 0.22 | +4.8% | 74,097 | +4.6% | 9.9M | Health Technology |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: SOAR, KOD, CLRO, GYGY, MIMI.
