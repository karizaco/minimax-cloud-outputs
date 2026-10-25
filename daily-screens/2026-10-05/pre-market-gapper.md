# Pre-Market Gapper — 2026-10-05

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 56 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 56 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **SAIQ** | NASDAQ | 6.67 | +281.7% | 21,010,185 | +89.7% | 8.3M | Finance |
| 2 | **MI** | AMEX | 7.00 | +233.3% | 18,888,714 | +11.9% | 0.5M | Technology Services |
| 3 | **BEAT** | NASDAQ | 0.65 | +72.6% | 84,959,574 | +1.2% | 36.9M | Health Technology |
| 4 | **VEEA** | NASDAQ | 5.72 | +61.6% | 24,274,869 | +29.4% | 17.8M | Technology Services |
| 5 | **APUS** | AMEX | 4.59 | +55.0% | 15,139,056 | +0.0% | 6.9M | Health Technology |
| 6 | **PCVX** | NASDAQ | 73.82 | +54.0% | 1,322,678 | +9.9% | 10984.8M | Health Technology |
| 7 | **ALEC** | NASDAQ | 1.99 | +50.5% | 44,177,205 | +2.8% | 222.2M | Health Technology |
| 8 | **PTC** | NASDAQ | 192.26 | +35.9% | 1,834,871 | +20.4% | 20861.4M | Technology Services |
| 9 | **RETO** | NASDAQ | 1.95 | +31.6% | 8,102,639 | +23.2% | 6.8M | Non-Energy Minerals |
| 10 | **AMOD** | NASDAQ | 3.78 | +30.9% | 8,769,238 | +0.3% | 18.6M | Technology Services |
| 11 | **SDEV** | AMEX | 3.94 | +29.9% | 22,319,768 | +13.6% | 203.9M | Health Technology |
| 12 | **RXO** | NYSE | 28.65 | +24.3% | 612,156 | +1.0% | 4725.1M | Technology Services |
| 13 | **XP** | NASDAQ | 28.15 | +20.8% | 705,287 | +9.2% | 14554.0M | Finance |
| 14 | **ONEN** | NASDAQ | 2.13 | +19.8% | 1,064,050 | +1.6% | 55.4M | Finance |
| 15 | **QTEX** | NASDAQ | 1.54 | +18.6% | 43,609,296 | +7.3% | 103.3M | Health Technology |
| 16 | **INTR** | NASDAQ | 6.56 | +18.6% | 761,100 | +11.3% | 2886.4M | Finance |
| 17 | **BTTC** | NASDAQ | 0.62 | +17.0% | 15,226,239 | +17.3% | 6.7M | Technology Services |
| 18 | **VRAX** | NASDAQ | 2.40 | +16.4% | 499,003 | +1.4% | 3.2M | Finance |
| 19 | **JAGX** | NASDAQ | 4.73 | +16.1% | 719,206 | +13.4% | 9.2M | Health Technology |
| 20 | **PAGS** | NYSE | 10.95 | +14.9% | 323,891 | +10.1% | 3038.8M | Commercial Services |
| 21 | **AGMH** | NASDAQ | 0.73 | +14.3% | 523,899 | +4.0% | 3.8M | Technology Services |
| 22 | **STNE** | NASDAQ | 11.54 | +13.7% | 584,076 | +6.6% | 2806.9M | Commercial Services |
| 23 | **SXTP** | NASDAQ | 1.44 | +12.2% | 77,080 | +4.3% | 5.1M | Health Technology |
| 24 | **ACB** | NASDAQ | 4.46 | +11.7% | 203,795 | -0.8% | 289.2M | Process Industries |
| 25 | **NU** | NYSE | 15.18 | +11.7% | 5,412,956 | +7.6% | 73326.8M | Finance |
| 26 | **XRPN** | NASDAQ | 38.65 | +11.6% | 214,452 | +4.7% | 1221.0M | Finance |
| 27 | **NAUT** | NASDAQ | 1.87 | +11.5% | 2,485,732 | +13.8% | 238.0M | Health Technology |
| 28 | **ARCO** | NYSE | 8.10 | +11.1% | 68,588 | +0.3% | 1687.7M | Consumer Services |
| 29 | **CTNT** | NASDAQ | 3.13 | +11.1% | 768,376 | -0.8% | 4.2M | Industrial Services |
| 30 | **AUUD** | NASDAQ | 1.33 | +9.9% | 81,729 | +5.0% | 7.7M | Technology Services |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: SAIQ, MI, BEAT, VEEA, APUS.
