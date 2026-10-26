# Pre-Market Gapper — 2026-10-22

**`_source=mcp`** (batched TradingView extended-hours read) · sweep date 2026-10-22 · fired 21:35 ET  
**Result: 0 of 13 Focus names flagged.**

## Method (skill §6 — Sun + Bonde)
Input is the **Focus list** from the daily sweep (`daily-screens/2026-10-22/focus.md`, 13 names) — not a market-wide scan.
One extended-hours read per name. Flag rule: `gap_pct > 4` **AND** `pre_market_volume > 50,000`.

## Focus-list extended hours

| Sym | Close | Day % | PM Δ% | PM Gap% | PM Vol | Verdict |
|---|---|---|---|---|---|---|
| RCEL | 15.42 | 0.85% | 1.24% | 1.05% | 1,211 | pass |
| LIFE | 43.53 | -1.56% | -1.90% | 1.76% | 1,320 | pass |
| KOD | 85.78 | -2.21% | -0.80% | 1.46% | 26,145 | pass |
| MRNA | 202.63 | -17.57% | -2.28% | -1.40% | 187,691 | pass |
| IOVA | 14.14 | -3.28% | -1.78% | -0.82% | 41,970 | pass |
| HAS | 117.23 | 2.83% | -0.04% | -0.01% | 13,276 | pass |
| APPN | 51.15 | 4.97% | -0.35% | -1.37% | 10,327 | pass |
| TEAM | 223.16 | -1.04% | 0.27% | -0.78% | 9,081 | pass |
| MEDP | 653.96 | -1.29% | 0.08% | -0.68% | 16,149 | pass |
| TJGC | 31.89 | -2.63% | —% | —% | — | pass |
| BMBL | 5.94 | -0.17% | -0.34% | -0.34% | 40,347 | pass |
| CD | 8.21 | 7.05% | —% | —% | — | pass |
| BRZE | 45.86 | 0.39% | 0.20% | -0.09% | 5,636 | pass |

**Nothing passed.** Best PM move was **RCEL +1.24%** on 1,211 shares; heaviest PM volume was **MRNA 187,691**, under the 50k floor. A clean no-setup session, not a data gap.

### Read
- Whole Focus list sits inside ±2.3% pre-market. No catalysts, no gap-and-fade candidates.
- **MRNA -17.57% on the day** is the one real move in the group, but it is a realised session loss, not a pre-market gap — does not qualify.
- **CD +7.05%** and **APPN +4.97%** led the regular session; neither shows PM continuation.
- `TJGC` and `CD` returned null PM fields (thin / no pre-market prints) — no data, not zero.

## Timing caveat
Fired at 21:35 ET, long after the 09:30 close. These PM values are **stale end-of-session prints**, not live quotes. For actionable gapping this cron needs the 04:00–09:30 ET window; the scheduler currently fires it post-close.

## Appendix — market-wide gappers (context only, not the §6 list)
TradingView universe scan, `PM Δ% > 4 ∧ PM vol > 50k`: **30 shown of 33**. None are in today's Focus list.

| Sym | Exch | Last | PM Δ% | PM Vol | MCap |
|---|---|---|---|---|---|
| STAK | NASDAQ | 1.67 | +68.0% | 32,655,568 | 16.7M |
| SHFS | NASDAQ | 0.34 | +51.0% | 162,756,284 | 0.2M |
| BHVN | NYSE | 14.69 | +37.7% | 9,296,306 | 2218.8M |
| NCPL | NASDAQ | 2.23 | +30.6% | 1,908,914 | 17.5M |
| BKYI | NASDAQ | 2.74 | +28.6% | 10,480,262 | 5.6M |
| PFSA | NASDAQ | 1.02 | +21.3% | 11,712,730 | 0.6M |
| NANO | NASDAQ | 10.10 | +20.7% | 459,348 | 298.9M |
| SKYQ | NASDAQ | 2.10 | +19.4% | 2,539,515 | 18.4M |
| ATOM | NASDAQ | 3.08 | +18.5% | 985,725 | 120.2M |
| XLAB | NASDAQ | 4.71 | +17.6% | 9,712,155 | 303.0M |
| SAIQ | NASDAQ | 5.28 | +16.9% | 1,369,776 | 157.4M |
| AVEX | NYSE | 10.96 | +14.4% | 451,068 | 1389.4M |
| AMFN | OTC | 0.07 | +12.9% | 110,599 | 107.5M |
| SNAL | NASDAQ | 2.23 | +12.4% | 211,549 | 20.0M |
| XXII | NASDAQ | 0.22 | +10.6% | 52,705,702 | 0.2M |
| HTCO | NASDAQ | 1.17 | +10.2% | 492,318 | 10.6M |
| ARAI | NASDAQ | 0.13 | +9.9% | 534,128 | 6.6M |
| CJMB | NASDAQ | 0.52 | +9.3% | 71,087,401 | 3.0M |
| QS | NASDAQ | 4.15 | +8.3% | 896,576 | 2569.3M |
| AKAN | NASDAQ | 1.15 | +7.1% | 772,493 | 3.0M |
| CGTX | NASDAQ | 0.70 | +7.0% | 156,416 | 66.6M |
| SPOT | NYSE | 583.66 | +6.8% | 145,256 | 120165.3M |
| TENX | NASDAQ | 1.76 | +6.7% | 102,379 | 65.9M |
| BLDP | NASDAQ | 1.49 | +5.9% | 123,314 | 523.1M |
| LMT | NYSE | 589.91 | +5.5% | 80,377 | 136145.8M |
| AHT | NYSE | 2.78 | +4.9% | 240,590 | 18.0M |
| LBRT | NYSE | 15.38 | +4.9% | 57,240 | 2509.9M |
| TROO | NASDAQ | 2.32 | +4.8% | 90,069 | 283.4M |
| ZURA | NASDAQ | 3.53 | +4.6% | 157,505 | 338.3M |
| SDEV | AMEX | 1.10 | +4.5% | 13,838,717 | 56.9M |

_Market-wide movers skew heavily to sub-$20M microcaps. Size, not signal._
