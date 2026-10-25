# Pre-Market Gapper — 2026-10-02

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 57 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 57 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **AMOD** | NASDAQ | 3.49 | +197.4% | 78,074,895 | +79.5% | 5.8M | Technology Services |
| 2 | **NIVF** | NASDAQ | 0.13 | +60.6% | 190,944,935 | +32.6% | 0.3M | Finance |
| 3 | **SDEV** | AMEX | 7.48 | +36.8% | 20,141,200 | +23.2% | 189.4M | Health Technology |
| 4 | **SGRX** | NASDAQ | 1.26 | +27.7% | 7,059,015 | +25.2% | 1.0M | Consumer Non-Durables |
| 5 | **XRPN** | NASDAQ | 39.42 | +23.5% | 163,932 | +13.8% | 1245.3M | Finance |
| 6 | **SCNX** | NASDAQ | 0.16 | +18.9% | 111,013,010 | -2.1% | 6.5M | Commercial Services |
| 7 | **QTEX** | NASDAQ | 1.10 | +18.0% | 20,952,081 | +11.5% | 73.8M | Health Technology |
| 8 | **SYNA** | NASDAQ | 121.10 | +14.7% | 409,120 | +14.2% | 4806.8M | Electronic Technology |
| 9 | **SCKT** | NASDAQ | 0.71 | +12.0% | 17,014,438 | +8.0% | 5.9M | Electronic Technology |
| 10 | **CYCU** | NASDAQ | 3.82 | +11.5% | 3,058,165 | +5.2% | 12.3M | Technology Services |
| 11 | **TNON** | NASDAQ | 3.70 | +11.4% | 3,109,521 | +0.0% | 3.8M | Health Services |
| 12 | **TNMG** | NASDAQ | 4.76 | +10.8% | 5,711,935 | -2.9% | 3.6M | Technology Services |
| 13 | **CYPH** | NASDAQ | 3.03 | +10.6% | 1,215,876 | +4.8% | 326.5M | Finance |
| 14 | **ORBS** | NASDAQ | 1.16 | +9.7% | 1,534,392 | +3.5% | 498.5M | Finance |
| 15 | **SMTOF** | OTC | 16.57 | +9.6% | 76,390 | +9.6% | 52389.5M | Producer Manufacturing |
| 16 | **GOW** | NASDAQ | 3.87 | +8.7% | 3,193,795 | +4.0% | 17.2M | Finance |
| 17 | **FWDI** | NASDAQ | 8.16 | +8.4% | 229,828 | +3.2% | 622.5M | Finance |
| 18 | **VERI** | NASDAQ | 0.75 | +8.1% | 368,624 | +4.8% | 75.3M | Commercial Services |
| 19 | **BTCT** | NASDAQ | 1.15 | +7.4% | 553,894 | +8.3% | 19.5M | Technology Services |
| 20 | **NAMM** | NASDAQ | 1.26 | +6.9% | 628,135 | +1.5% | 70.4M | Non-Energy Minerals |
| 21 | **SOC** | NYSE | 3.51 | +6.4% | 122,542 | +0.3% | 673.5M | Energy Minerals |
| 22 | **ZONE** | AMEX | 0.13 | +6.1% | 430,151 | -0.2% | 67.0M | Distribution Services |
| 23 | **BTDR** | NASDAQ | 11.02 | +6.0% | 358,424 | +1.8% | 2995.0M | Technology Services |
| 24 | **FPS** | NYSE | 40.35 | +6.0% | 205,439 | +1.3% | 12283.7M | Producer Manufacturing |
| 25 | **DFDV** | NASDAQ | 5.25 | +5.9% | 80,472 | +3.7% | 171.3M | Finance |
| 26 | **ON** | NASDAQ | 84.89 | +5.8% | 604,904 | +5.7% | 33048.7M | Electronic Technology |
| 27 | **COSM** | NASDAQ | 0.38 | +5.5% | 82,251 | +3.4% | 38.2M | Health Technology |
| 28 | **RKT** | NYSE | 11.70 | +5.3% | 1,314,124 | +0.5% | 33130.2M | Finance |
| 29 | **CMPX** | NASDAQ | 0.86 | +5.1% | 51,702 | +1.7% | 154.3M | Health Technology |
| 30 | **AZTR** | AMEX | 0.13 | +5.1% | 134,446 | +3.0% | 8.0M | Health Technology |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: AMOD, NIVF, SDEV, SGRX, XRPN.
