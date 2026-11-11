# Daily sweep summary

Generated 2026-11-11

> **shibui T+1**: the T+1 book is for **2026-11-10** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-11** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **False**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **63.73**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 60 | 60 |
| B_stockbee_ep9m | 204 | 204 |
| C_qullamaggie_rs | 79 | 79 |
| D_qullamaggie_ep | 2 | 2 |
| E_qullamaggie_5d_gainers | 16 | 16 |
| F_qullamaggie_5d_losers | 10 | 10 |
| G_peoplewish | 361 | 361 |
| H_hernandez_theme | 153 | 153 |
| K_stockbee_anticipation | 309 | 309 |
| jeff_sun_canslim | 69 | 69 |

> **Cap signature:** A_stockbee_4pct land(s) exactly on a known cap (30 / 50 / 60 / 200). When `rows_passing` agrees, that is the true count; when it does not, the branch was truncated and the run must fail.

## Tier-A (appears in ≥ 3 stylists): 4

- **AAON** (stylists: 4, origins: 4, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim) [t1 2026-11-10] EXTENDED · quality: free_cash_flow_yield
- **LQDA** (stylists: 5, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, TV_volume_breakout) [fresh+t1 2026-11-11] EXTENDED
- **QNT** (stylists: 3, origins: 3, sources: A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish) [t1 2026-11-10] EXTENDED · quality: free_cash_flow_yield
- **ZETA** (stylists: 3, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-11] EXTENDED · quality: trailing_pe, operating_pe, trailing_revenue_peg

## Tier-A — FRESH vs EXTENDED: 0 fresh / 4 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** AAON, LQDA, QNT, ZETA

## Valuation / quality overlay: 647 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AAMI** — earnings_quality_flags
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_pe, trailing_revenue_peg
- **ABCL** — free_cash_flow_yield
- **ACAD** — earnings_quality_flags
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ADC** — free_cash_flow_yield
- **ADMA** — trailing_revenue_peg, earnings_quality_flags
- **ADPT** — free_cash_flow_yield, debt_to_equity
- **ADT** — debt_to_equity
- **AEAQ** — free_cash_flow_yield
- **AEE** — free_cash_flow_yield, debt_to_equity
- **AEHR** — free_cash_flow_yield
- **AEIS** — earnings_quality_flags
- **AEP** — free_cash_flow_yield, debt_to_equity
- **AER** — debt_to_equity
- **AES** — free_cash_flow_yield, debt_to_equity
- **AFRM** — operating_pe, debt_to_equity, earnings_quality_flags
- **AGL** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AI** — free_cash_flow_yield
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **ALAB** — trailing_pe, operating_pe
- **ALC** — trailing_pe, trailing_revenue_peg
- **ALEC** — free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALH** — trailing_revenue_peg, debt_to_equity
- **ALHC** — trailing_pe
- **ALK** — free_cash_flow_yield, debt_to_equity
- **ALKS** — operating_pe
- **ALM** — trailing_pe, free_cash_flow_yield
- **ALMR** — free_cash_flow_yield
- **ALSN** — debt_to_equity
- **ALUB** — free_cash_flow_yield
- … and 607 more (full list in `_results.json`)

## Parabolic short candidates: 16

- ACHC
- APP
- AUGO
- FLY
- FUN
- JBLU
- KD
- MGNI
- OUST
- QNT

## Parabolic long / mean-reversion: 10

- AXON
- CAI
- CLMT
- DOX
- FIS
- HIMS
- IONS
- IRTC
- NRIX
- TE
