# Reversal Bullish (Bonde) — 3:55 PM ET — 2026-10-21 (Wed)

**Data date:** 2026-10-20 (Tue close) · **Cron fire:** 04:55 ET pre-market (T+1 lag) · **Source:** `_source=yahoo_fallback`

> **Degraded run — read first.** The TradingView scanner endpoint (PRIMARY universe source) was unreachable this run (2 attempts, HTTP 000 / TLS EOF). Per the zero-fallback policy the chain stopped immediately. The universe is therefore **yesterday's (Mon 2026-10-20) 493-name large-cap list**, re-gated locally on fresh Yahoo bars: `change < 0` and `avg 30d volume > 1M`. Market-cap and liquidity gates are inherited from Monday, and **any large-cap that dropped today but was not already in Monday's universe is not in scope**. Treat results as a subset of the true scan, not the full list. `mcap` column omitted — not available from the Yahoo fallback path.

## Results — 2 candidates passed all 8 Bonde criteria

| # | Symbol | Close | Chg% | DCR | Body% | Tail:Body | ADR% | 20d Trend | 2d Drop | 5d Low | Body Low Stop | Signal Age |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | $694.25 | -1.59% | 0.85 | 0.05 | 18.1 | 3.14 | -5.75% | -2.13% | $693.86 | $694.25 | **Day 3** (also flagged 10-20, 10-21) |
| 2 | **FRO** | $50.32 | -0.79% | 0.56 | 0.04 | 15.1 | 3.80 | +5.01% | -4.13% | $49.53 | $50.24 | **Day 1** (fresh) |

### Notes per name

- **META** ($694.25, Meta Platforms) — DCR 0.85, ADR 3.14%, 20d trend -5.75%, tail:body 18.1 (near-doji hammer on a fresh 5-day low). **This is Day 3 of the signal** — it was flagged on both the 10-20 and 10-21 runs, and the close has ground lower each session ($705.44 → $694.25). Bonde's rule is *"exit on stop if it does not work on 3rd day"*. The DCR improved (0.77 → 0.85) but the structure is degrading, not resolving. **Treat as Day 3 — pass unless already in from the 10-20 entry.**
- **FRO** ($50.32, FrontRow) — DCR 0.56 (borderline), ADR 3.80%, 20d trend +5.01% (clean uptrend), tail:body 15.1. **Day 1, freshest setup.** Passes on a clean trend but DCR is barely over Bonde's 0.5 floor, so discretionary scrutiny is warranted. If taking anything today, this is the only genuine Day 1 candidate.

**Bonde's output discipline:** "Select 1 to 3 ideas" — do not pad. Given one name is Day 3 and the other is borderline, the honest read is **at most one entry (FRO, Day 1)**, and Bonde's stop rule may already have been triggered on META depending on the 10-20 entry fill. Body-low stop for both is the `close` (doji body — no lower wick to reference beyond it).

## Near Misses — 1 stock failed only F8 (long-term trend)

| # | Symbol | Close | DCR | Body% | Tail:Body | ADR% | 20d Trend |
|---|---|---|---|---|---|---|---|
| 1 | VRT | $203.56 | 0.51 | 0.10 | 4.3 | 3.63 | -19.69% |

**VRT** (Vertiv, $203.56, -19.69% from 20d ago) — had the reversal candle but is in a hard downtrend. Bonde's common-rejections table marks exactly this profile as *do not trade*.

## Filter-chain diagnostic (seed 493 → 90 down-day/liquid → 2 passed)

| Stage | Rejected | Reason |
|---|---|---|
| Universe re-gate (change >= 0) | 403 | Not a down day on Tue close |
| Universe re-gate (avg 30d vol < 1M) | 1 | Illiquid |
| F1 (5-day low) | 59 | Today low NOT below prior 5-day min low |
| F2 (DCR >= 0.5) | 18 | Closed in lower half of day range |
| F3 (tail:body >= 3) | 6 | Bottom tail too short |
| F4 (small body) | 2 | Body > 40% of day range |
| F5 (2-day decline) | 0 | — |
| F6 (ADR >= 3%) | 1 | Slow mover |
| F8 (close >= close_20d_ago x 0.92) | 1 | Long-term downtrend |
| **PASSED ALL 8** | **2** | |

90/493 down-day names is a mild tape — well below last week's selloff volume, consistent with the post-Oct-16 exhaustion pattern seen on 10-19 and 10-20.

## Market context — largest down-day movers in universe (Tue close)

`GM -6.84% · FPS -4.09% · HWM -3.82% · GE -3.67% · ELAN -3.36% · FTAI -3.30% · FLR -2.98% · ARXS -2.94% · NE -2.86% · ET -2.78%`

Defensives (GM, HWM, GE, ELAN) led the downside — risk-off tone, no high-beta capitulation. Consistent with a low count of genuine Bonde hammers.

## Discretionary Notes

- **Window**: cron fired 04:55 ET pre-market, outside Bonde's 15:30–16:00 ET scan window by design (scheduler granularity). This artifact is a **planning snapshot off Monday's data basis** — re-verify META/FRO at the 15:55 ET fire today before any entry. Note the universe is stale, so that run should also confirm the TradingView scanner has recovered.
- **T+1 lag**: latest bar is 2026-10-20 (Tue close); cron date is 2026-10-21.
- **Data health**: shibui-finance MCP, tradingview-advanced MCP and yahoo-finance MCP were all absent from this sandbox, as on prior runs. Yahoo v8 chart HTTP worked normally (493/493 symbols fetched). Finviz remains behind a Cloudflare challenge.

## Recent runs

| Run date | Data date | Picks |
|---|---|---|
| 2026-10-09 | Fri 10-09 | 12 — RVTY, A, RGEN, ILMN, TEM, MAIR, PTCT, SWKS, GH, BMNR, ALGM, HBM |
| 2026-10-12 | Fri 10-09 | 1 — ALAB |
| 2026-10-15 | Wed 10-14 | 21 — broadest this month, semicap/optical heavy |
| 2026-10-16 | Thu 10-15 | 21 — JBL, INGM, VIAV, KLAC, SNPS, AMAT, CEG, LRCX, TER + 13 |
| 2026-10-19 | Fri 10-16 | 0 — setup exhaustion after broad selloff |
| 2026-10-20 | Mon 10-19 | 1 — META |
| 2026-10-21 | Tue 10-20 | 2 — META (Day 3), FRO (Day 1) — *degraded universe* |
