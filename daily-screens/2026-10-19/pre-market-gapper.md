# Pre-Market Gapper — 2026-10-19

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 105 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 105 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **YMAT** | NASDAQ | 1.83 | +94.7% | 33,824,592 | +4.6% | 7.3M | Producer Manufacturing |
| 2 | **FRGT** | NASDAQ | 1.47 | +35.4% | 3,329,452 | +6.2% | 25.0M | Finance |
| 3 | **SAFX** | NASDAQ | 0.16 | +34.5% | 84,446,851 | +87.8% | 65.0M | Energy Minerals |
| 4 | **AAME** | NASDAQ | 1.45 | +33.3% | 28,316,882 | +37.1% | 29.6M | Finance |
| 5 | **MASK** | NASDAQ | 0.93 | +29.6% | 41,938,812 | -0.4% | 3.4M | Technology Services |
| 6 | **IRON** | NASDAQ | 78.93 | +29.2% | 877,084 | +10.5% | 3030.3M | Health Technology |
| 7 | **ZONE** | AMEX | 0.10 | +26.1% | 111,212 | +6.3% | 48.3M | Distribution Services |
| 8 | **RPGL** | NASDAQ | 8.05 | +21.5% | 168,756 | +16.4% | 8.4M | Technology Services |
| 9 | **XLAB** | NASDAQ | 3.06 | +19.1% | 25,943,715 | -3.4% | 103.1M | Finance |
| 10 | **FUFU** | NASDAQ | 1.19 | +16.6% | 61,492 | +8.5% | 198.3M | Technology Services |
| 11 | **UPLD** | NASDAQ | 3.32 | +16.6% | 129,395 | +14.8% | 9.8M | Technology Services |
| 12 | **CLF** | NYSE | 14.10 | +16.5% | 2,223,765 | +3.8% | 8044.6M | Non-Energy Minerals |
| 13 | **MEDS** | NASDAQ | 2.67 | +16.4% | 2,237,437 | +3.8% | 12.0M | Distribution Services |
| 14 | **AIBZ** | NASDAQ | 2.95 | +15.9% | 123,126 | +11.6% | 15.0M | Technology Services |
| 15 | **TCRT** | NASDAQ | 3.13 | +14.8% | 17,346,782 | +0.4% | 9.2M | Health Technology |
| 16 | **MNDR** | NASDAQ | 0.94 | +14.1% | 1,640,906 | +5.9% | 1.1M | Health Services |
| 17 | **DWTX** | NASDAQ | 1.21 | +11.5% | 84,043 | +0.0% | 41.1M | Health Technology |
| 18 | **EOSE** | NASDAQ | 1.81 | +11.0% | 3,305,574 | +4.3% | 659.1M | Producer Manufacturing |
| 19 | **SLXN** | NASDAQ | 0.15 | +9.8% | 2,733,262 | +0.3% | 2.2M | Health Technology |
| 20 | **PLAG** | AMEX | 0.52 | +9.6% | 9,474,592 | +0.1% | 7.4M | Consumer Non-Durables |
| 21 | **VAI** | NASDAQ | 2.67 | +9.0% | 406,995 | +12.9% | 38.9M | Finance |
| 22 | **ACTU** | NASDAQ | 0.60 | +8.9% | 127,294 | +10.8% | 14.4M | Health Technology |
| 23 | **ZNTL** | NASDAQ | 2.30 | +8.9% | 54,241 | +10.3% | 217.7M | Health Technology |
| 24 | **EQPT** | NASDAQ | 13.95 | +8.9% | 86,124 | +2.1% | 3540.6M | Technology Services |
| 25 | **RCAT** | NASDAQ | 4.68 | +8.7% | 361,165 | +3.6% | 714.7M | Technology Services |
| 26 | **TWG** | NASDAQ | 0.07 | +8.6% | 158,113,559 | +48.5% | 4.6M | Distribution Services |
| 27 | **UAMY** | NYSE | 3.10 | +8.4% | 215,273 | +4.9% | 464.0M | Non-Energy Minerals |
| 28 | **RYDE** | AMEX | 0.71 | +8.4% | 52,082 | +0.8% | 121.3M | Technology Services |
| 29 | **MRKR** | NASDAQ | 1.20 | +7.7% | 170,135 | +3.9% | 20.0M | Health Technology |
| 30 | **NRXP** | NASDAQ | 2.63 | +7.7% | 50,111 | +8.5% | 113.9M | Health Technology |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: YMAT, FRGT, SAFX, AAME, MASK.
