# Pre-Market Gapper — 2026-09-30

_Source: TradingView public scanner (`https://scanner.tradingview.com/america/scan`). Filter: premarket_change > 4% AND premarket_volume > 50,000. Cloud cron #8 (no `focus.md` available on fresh session — running standalone market-wide scan). 30 of 50 qualifying names shown._

## Criteria applied (Sun + Bonde style)
- Pre-market change > **+4%** (gap-up threshold)
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- No price/mcap floor applied in this scan (sweep-level universe)

## Flagged names (30 shown, top of 50 matching)

| # | Symbol | Exch | Last | PM Δ% | PM Vol | PM Gap% | MCap | Sector |
|---|---|---|---|---|---|---|---|---|
| 1 | **NIVF** | NASDAQ | 0.17 | +132.1% | 349,793,980 | +23.9% | 0.2M | Finance |
| 2 | **CNTB** | NASDAQ | 1.10 | +89.6% | 90,180,008 | +0.8% | 69.3M | Health Technology |
| 3 | **VBIO** | NASDAQ | 2.80 | +41.7% | 26,826,536 | +0.0% | 2.5M | Health Technology |
| 4 | **NCI** | NASDAQ | 1.26 | +40.5% | 7,356,704 | +87.3% | 3.0M | Retail Trade |
| 5 | **BBLR** | OTC | 0.00 | +33.3% | 100,000 | +33.3% | 0.2M | Technology Services |
| 6 | **FFR** | NASDAQ | 1.31 | +30.7% | 10,369,436 | +7.9% | 27.7M | Technology Services |
| 7 | **TGE** | NYSE | 1.55 | +26.5% | 22,199,837 | +8.4% | 75.1M | Finance |
| 8 | **AEON** | AMEX | 0.30 | +25.1% | 12,329,349 | -2.4% | 15.0M | Health Technology |
| 9 | **WETO** | NASDAQ | 1.01 | +23.6% | 4,731,835 | +27.3% | 1.1M | Transportation |
| 10 | **RETO** | NASDAQ | 0.11 | +21.5% | 288,530,259 | +6.5% | 5.8M | Non-Energy Minerals |
| 11 | **BIYA** | NASDAQ | 1.96 | +20.0% | 2,219,629 | +18.1% | 12.3M | Commercial Services |
| 12 | **SGMT** | NASDAQ | 9.88 | +16.8% | 357,421 | +1.0% | 608.5M | Health Technology |
| 13 | **CAPR** | NASDAQ | 9.47 | +16.7% | 4,546,140 | +16.3% | 550.6M | Health Technology |
| 14 | **FRGT** | NASDAQ | 0.28 | +15.9% | 46,717,983 | +2.1% | 0.2M | Finance |
| 15 | **NCPL** | NASDAQ | 1.24 | +15.6% | 1,552,594 | +3.3% | 9.7M | Commercial Services |
| 16 | **XERI** | OTC | 0.01 | +14.1% | 60,000 | +15.2% | 10.8M | Electronic Technology |
| 17 | **FNGR** | NASDAQ | 0.18 | +13.7% | 74,767,206 | +31.9% | 13.5M | Technology Services |
| 18 | **BTTC** | NASDAQ | 0.52 | +12.6% | 16,217,548 | +12.0% | 5.6M | Technology Services |
| 19 | **PWCM** | NASDAQ | 1.13 | +11.5% | 55,062 | +5.4% | 2.7M | Commercial Services |
| 20 | **MSGY** | NASDAQ | 5.66 | +11.0% | 279,151 | +12.6% | 12.0M | Industrial Services |
| 21 | **GNS** | AMEX | 0.16 | +9.6% | 1,615,303 | +3.0% | 30.5M | Technology Services |
| 22 | **GCDT** | AMEX | 0.52 | +9.4% | 4,931,219 | -5.7% | 7.0M | Industrial Services |
| 23 | **ORBS** | NASDAQ | 1.17 | +8.9% | 1,183,489 | +0.0% | 502.8M | Finance |
| 24 | **CYPH** | NASDAQ | 3.33 | +8.4% | 892,873 | -0.3% | 358.9M | Finance |
| 25 | **TOVX** | AMEX | 0.23 | +8.1% | 135,237 | +3.0% | 10.3M | Health Technology |
| 26 | **BTCT** | NASDAQ | 1.13 | +7.7% | 199,868 | +0.9% | 19.2M | Technology Services |
| 27 | **NAUT** | NASDAQ | 1.42 | +7.7% | 3,189,030 | +7.7% | 180.7M | Health Technology |
| 28 | **NAMM** | NASDAQ | 0.96 | +7.5% | 440,240 | +2.5% | 53.5M | Non-Energy Minerals |
| 29 | **HPE** | NYSE | 63.89 | +7.3% | 1,016,215 | +0.0% | 84811.7M | Electronic Technology |
| 30 | **ONMD** | NASDAQ | 5.79 | +7.3% | 190,348 | +0.9% | 34.3M | Finance |

## Notes
- `_source=tv_fallback` — TradingView public scanner used (no MCP shibui/financekit/yahoo available in cloud env, no focus.md from prior step).
- `pm_gap` and `pm_change` are reported by TV as separate fields; both shown for transparency.
- Extreme movers (>50% PM change) likely reflect illiquid names — flag manually before any execution.
- Top names by gap magnitude: NIVF, CNTB, VBIO, NCI, BBLR.
