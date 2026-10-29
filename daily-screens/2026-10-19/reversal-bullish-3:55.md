# Reversal Bullish (Bonde) — 3:55 PM ET — 2026-10-19 (Mon)

_Source: TradingView scanner (universe) + Yahoo Finance (OHLC) — shibui MCP not available in this sandbox._
_Universe: US large/mega-cap (mcap > $5B, avg 30d vol > 1M), today's change < 0, close ≥ $15._
_Latest bar used: 2026-10-16 (Fri close) (cron fired pre-market Mon; T+1 case.)_
_Filter chain: 8 Bonde criteria from Stockbee's published playbook._

## Results — 0 candidate(s) passed all 8 Bonde criteria

**0 candidates** passed all 8 strict Bonde criteria. Market context: post-weekend scan, Fri close used. **Setup exhaustion** — Fri's broad selloff (BSP -15.6%, GRAL -13.0%, NBIS -12.2%, CRWV -11.9%, IREN -11.2%) already set fresh 5-day lows. By Mon, the prior 5-day low is the new ceiling; few names print ANOTHER new 5-day low to satisfy F1.

Filter-by-filter rejections (out of 477 in universe):

| Stage | Rejected | Reason |
|---|---|---|
| Universe gate | 0 | mcap>5B, avg-vol>1M, change<0, close≥15 |
| F1 (5-day low) | 377 | Today low NOT below prior 5-day min low (Fri already set the lows) |
| F2 (DCR ≥ 0.5) | 99 | Closed in lower half of day range |
| F3 (tail:body ≥ 3) | 1 | Bottom tail too short |
| F4 (small body) | 0 | — |
| F5 (2-day decline) | 0 | — |
| F6 (ADR ≥ 3%) | 0 | — |
| F8 (close ≥ close_20d_ago × 0.92) | 0 | — (none reached this filter) |
| **PASSED ALL 8** | **0** | |

This is consistent with Bonde's published expectation: the 3:55 PM RB scan is intentionally strict and frequently returns 0–3 names. **Do not pad with marginal setups.**

**Why so few today:** Fri's selloff (-10%+ on AI-compute / crypto-treasury names) likely already absorbed the prior 5-day-low setups. Mon pre-market session will print fresh data; re-run the scan at 15:55 ET today if today's intraday creates new 5-day-low hammers.

## Discretionary Notes

- **Day-of-week**: cron fired 04:55 ET (pre-market Mon). Bonde's RB scan is designed for the 15:30–16:00 ET same-day window. **Today's 15:55 ET fire** is the actionable event; this artifact is a planning snapshot.
- **Latest available data**: 2026-10-16 (Fri close). Oct 19 intraday not yet known.
- **Universe size**: 477 large-cap US equities (mcap > $5B, avg 30d vol > 1M, down-day, ≥ $15). Largest universe this month — broad Fri selloff concentrated in AI-compute / crypto-treasury (BSP, GRAL, NBIS, CRWV, GLXY, APLD, IREN, HUT, FROG, TWLO).
- **Source path**: PRIMARY chain shibui-finance unavailable → fallback to TradingView scanner + Yahoo Finance v8 chart (Finviz blocked by Cloudflare 403, chain terminated per zero-fallback policy).

## Last Two Weeks (cross-day summary)

- 2026-09-29 (Mon close): VSAT, STLD, EBAY (3 picks).
- 2026-09-30 (Tue close): U (1 pick, Unity).
- 2026-10-01 (Wed close): CNC (1 pick, Centene).
- 2026-10-02 (Thu close): IREN, AVTR, CNM (3 picks).
- 2026-10-05 (Mon close): NYT (1 pick, New York Times).
- 2026-10-06 (Tue close): QBTS, RGTI (2 picks, quantum-computing pair).
- 2026-10-07 (Wed close): EXPE (1 pick, Expedia — borderline DCR).
- 2026-10-08 (Thu close): NTRA, CAI, ACMR, MHK (4 picks).
- 2026-10-09 (Fri close): 12 picks — broadest day (RVTY, A, RGEN, ILMN, TEM, MAIR, PTCT, SWKS, GH, BMNR, ALGM, HBM).
- 2026-10-12 (Mon close): ALAB (1 pick, Astera Labs).
- 2026-10-15 (Thu close): 21 picks — broadest day this month (JBL, INGM, VIAV, KLAC, SNPS, AMAT, CEG, LRCX, TER + 13 more).
- 2026-10-16 (Fri close): 0 picks (this run). Setup exhaustion after broad selloff.
