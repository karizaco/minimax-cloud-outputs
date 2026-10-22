# peoplewish — ADR + velocity

- **Sweep date (cron)**: 2026-10-22  ·  **Data session**: 2026-10-21 (last completed close)
- **Matched**: 66 names in the prefiltered universe  ·  **listed**: 15
- **Source**: TradingView public scanner, `_source=mcp` · universe 2928 rows
- **Generated**: 2026-10-22T11:33:57Z

## Filter as implemented

> Average daily range >=4% (monthly Volatility.M), 1-month velocity >=+20%, 30-day average volume >=500k so a $50k account can size in.

| Sym | Close | Chg | 1M | 3M | 6M | Mcap | Vol/30d | RVOL | ADR% | Sector |
|---|---|---|---|---|---|---|---|---|---|---|
| **XRPN** | 15.75 | +6.06% | +49.29% | +50.43% | +52.32% | 0.37B | 0.56× | 0.49 | 26.37% | Finance |
| **TJGC** | 31.89 | -2.63% | +193.65% | +608.67% | +681.62% | 0.32B | 0.07× | 1.18 | 11.83% | Electronic Technology |
| **DNA** | 10.01 | +1.52% | +24.35% | +29.83% | +28.66% | 0.67B | 0.58× | 0.57 | 12.52% | Health Services |
| **KOD** | 87.72 | -5.65% | +165.50% | +114.26% | +91.15% | 5.51B | 0.32× | 0.66 | 8.29% | Health Technology |
| **GRAL** | 132.60 | +6.36% | +41.46% | +89.73% | +160.05% | 5.92B | 0.44× | 0.70 | 7.60% | Health Technology |
| **VSTM** | 9.21 | -1.39% | +22.15% | +56.90% | +47.12% | 1.12B | 0.72× | 0.38 | 8.04% | Health Technology |
| **MRNA** | 245.81 | +1.54% | +52.63% | +329.74% | +360.49% | 98.14B | 0.94× | 0.81 | 7.19% | Health Technology |
| **MANE** | 136.66 | +7.51% | +27.20% | +26.26% | +98.06% | 5.71B | 0.78× | 0.62 | 6.65% | Health Technology |
| **LIFE** | 44.22 | +7.67% | +21.68% | +135.46% | +170.62% | 2.87B | 1.52× | 2.08 | 5.85% | Technology Services |
| **TNGX** | 26.98 | +6.85% | +23.20% | -2.07% | +3.73% | 4.55B | 1.54× | 1.44 | 6.12% | Health Technology |
| **QDEL** | 14.08 | -0.91% | +30.61% | -15.69% | +25.38% | 0.97B | 1.60× | 1.37 | 6.75% | Health Technology |
| **MAZE** | 32.58 | +0.40% | +44.67% | +15.53% | +26.03% | 1.81B | 1.12× | 1.10 | 5.51% | Health Technology |
| **IOVA** | 14.62 | -1.62% | +40.17% | +190.66% | +318.91% | 6.62B | 0.66× | 0.92 | 6.13% | Health Technology |
| **PICS** | 13.77 | -2.62% | +44.79% | +11.95% | +5.92% | 1.78B | 0.54× | 0.44 | 5.77% | Commercial Services |
| **CDNA** | 70.74 | +2.23% | +31.44% | +84.03% | +250.20% | 3.66B | 1.15× | 1.25 | 5.58% | Health Technology |


## Notes

ADR floor is the skill's account-relative rule at the default $50,000 account size (`ACCOUNT_SIZE_USD` is unset in this sandbox, so the skill's 50000 fallback applies).
