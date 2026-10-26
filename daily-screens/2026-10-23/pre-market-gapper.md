# Pre-Market Gapper — 2026-10-23

**`_source=tv_fallback`** (TradingView public scanner, tier 2) · sweep date 2026-10-23 · fired 21:31 ET  
**Result: 0 of 5 Focus names flagged.**

## Method (skill §6 — Sun + Bonde)
Input is the **Focus list** from the daily sweep (`daily-screens/2026-10-23/focus.md`, 5 names). One extended-hours read per name. Flag rule: `gap_pct > 4` **AND** `pre_market_volume > 50,000`.

## Focus-list extended hours

| Sym | Close | Day % | PM Δ% | PM Gap% | PM Vol | Verdict |
|---|---|---|---|---|---|---|
| XLAB | 3.35 | -28.87% | -5.52% | 0.85% | 1,325,766 | pass |
| MRNA | 200.10 | -1.25% | -3.18% | -1.00% | 523,503 | pass |
| KOD | 87.63 | 2.16% | -0.33% | -0.15% | 215 | pass |
| TJGC | 31.89 | -2.63% | —% | —% | — | pass |
| CD | 8.76 | 6.76% | 3.60% | 0.55% | 444 | pass |

**Nothing passed.** Best PM move in the list was **CD +3.60%** on 444 shares — below the +4% gate. Two names cleared the 50k volume floor on the downside (XLAB 1,325,766 and MRNA 523,503) but both are **down**, not up, so neither qualifies as a gapper. Clean no-setup session, not a data gap.

### Read
- No Focus name gaps up. The entire list is flat-to-down pre-market; there is no gap-up setup to trade here.
- **XLAB -5.52% on 1,325,766 PM shares** is the only real pre-market event in the group — but it is a **gap DOWN**, the mirror image of what this cron hunts. It follows a -28.87% session loss. Worth a trader's attention; out of scope for a gapper.
- `TJGC` returned null PM fields (no pre-market prints) — no data, not zero.
- `CD` +6.76% on the day and `KOD` +2.16% are regular-session moves; neither carries into pre-market.

## Lag / timing
- **Data lag:** the sweep behind this Focus list closed **2026-10-22** (`data_date`); the cron date is 2026-10-23. Shibui-style T+1 applies to the sweep, not to the extended-hours read below, which is live-sourced.
- **Fire time:** 21:31 ET, long after the 09:30 close, so these are stale end-of-session prints rather than live quotes. The 08:30 ET schedule this cron was migrated from would have landed in the actionable pre-market window.

## Appendix — market-wide gappers (context only, not the §6 list)
TradingView universe scan, `PM Δ% > 4 ∧ PM vol > 50k`: **24 shown of 24**. None are in today's Focus list.

| Sym | Exch | Last | PM Δ% | PM Vol | MCap |
|---|---|---|---|---|---|
| XXII | NASDAQ | 0.20 | +50.7% | 144,066,320 | 0.1M |
| LUCD | NASDAQ | 0.41 | +32.1% | 40,947,442 | 83.5M |
| YMAT | NASDAQ | 2.05 | +31.8% | 13,974,767 | 8.2M |
| SAIQ | NASDAQ | 6.12 | +27.7% | 1,476,159 | 182.5M |
| GPUS | AMEX | 0.17 | +20.0% | 106,258,822 | 32.4M |
| BKYI | NASDAQ | 3.39 | +19.0% | 4,921,235 | 6.9M |
| CCI | NYSE | 85.97 | +17.2% | 417,575 | 36576.4M |
| GETYQ | OTC | 0.03 | +15.5% | 500,000 | 11.8M |
| RNG | NYSE | 83.39 | +14.6% | 52,311 | 6963.6M |
| FMST | NASDAQ | 0.52 | +12.9% | 1,938,356 | 9.0M |
| AMT | NYSE | 188.97 | +11.3% | 210,169 | 88052.5M |
| STAK | NASDAQ | 1.74 | +9.6% | 5,171,513 | 17.4M |
| SAGT | NASDAQ | 0.64 | +8.4% | 82,627 | 15.9M |
| CJMB | NASDAQ | 0.57 | +8.1% | 17,670,433 | 3.3M |
| BNC | NASDAQ | 5.34 | +7.1% | 70,222 | 219.9M |
| COSM | NASDAQ | 0.26 | +6.7% | 126,246 | 26.3M |
| RITM | NYSE | 9.39 | +4.8% | 285,098 | 5243.4M |
| EONR | AMEX | 0.45 | +4.7% | 71,423 | 24.9M |
| RBNE | NASDAQ | 0.19 | +4.6% | 27,939,422 | 0.3M |
| BHVN | NYSE | 13.88 | +4.5% | 65,062 | 2096.5M |
| AKAN | NASDAQ | 1.01 | +4.3% | 86,247 | 2.7M |
| LDI | NYSE | 0.61 | +4.2% | 50,578 | 207.6M |
| OLOX | NASDAQ | 0.92 | +4.2% | 186,677 | 1.5M |
| RDN | NYSE | 35.75 | +4.0% | 53,992 | 4729.8M |

_Market-wide movers skew to small caps. Size, not signal._
