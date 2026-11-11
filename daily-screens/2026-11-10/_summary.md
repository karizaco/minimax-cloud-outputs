# Daily sweep summary

Generated 2026-11-11

> **shibui T+1**: the T+1 book is for **2026-11-09** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-10** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **False**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **62.02872531418312**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 468 | 468 |
| B_stockbee_ep9m | 225 | 225 |
| C_qullamaggie_rs | 83 | 83 |
| D_qullamaggie_ep | 1 | 1 |
| E_qullamaggie_5d_gainers | 22 | 22 |
| F_qullamaggie_5d_losers | 8 | 8 |
| G_peoplewish | 356 | 356 |
| H_hernandez_theme | 159 | 159 |
| K_stockbee_anticipation | 285 | 285 |

## Tier-A (appears in ≥ 3 stylists): 4

- **FRVO** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish) [fresh+t1 2026-11-10] EXTENDED · quality: free_cash_flow_yield
- **PRAX** (stylists: 4, origins: 4, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) [t1 2026-11-09] EXTENDED · quality: free_cash_flow_yield
- **QXO** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish) [fresh+t1 2026-11-10] EXTENDED
- **WRBY** (stylists: 4, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme) [t1 2026-11-09] EXTENDED · quality: trailing_pe, operating_pe, trailing_revenue_peg, earnings_quality_flags

## Tier-A — FRESH vs EXTENDED: 0 fresh / 4 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** FRVO, PRAX, QXO, WRBY

## Valuation / quality overlay: 684 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AAMI** — earnings_quality_flags
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield, earnings_quality_flags
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_pe, trailing_revenue_peg
- **ABCL** — free_cash_flow_yield
- **ACAD** — earnings_quality_flags
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ADC** — free_cash_flow_yield
- **ADPT** — free_cash_flow_yield, debt_to_equity
- **ADT** — debt_to_equity
- **ADTN** — operating_pe, free_cash_flow_yield, debt_to_equity
- **AEAQ** — free_cash_flow_yield
- **AEHR** — free_cash_flow_yield
- **AEIS** — earnings_quality_flags
- **AEP** — free_cash_flow_yield, debt_to_equity
- **AES** — free_cash_flow_yield, debt_to_equity
- **AFRM** — operating_pe, debt_to_equity, earnings_quality_flags
- **AGBK** — free_cash_flow_yield, debt_to_equity
- **AGIO** — free_cash_flow_yield
- **AGL** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AI** — free_cash_flow_yield
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **ALAB** — trailing_pe, operating_pe
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALH** — trailing_revenue_peg, debt_to_equity
- **ALK** — free_cash_flow_yield, debt_to_equity
- **ALLT** — operating_pe, earnings_quality_flags
- **ALLY** — debt_to_equity
- **ALM** — trailing_pe, free_cash_flow_yield
- **ALMR** — free_cash_flow_yield
- **ALMS** — free_cash_flow_yield
- **ALNT** — trailing_pe, trailing_revenue_peg
- **ALOY** — free_cash_flow_yield
- **ALUB** — free_cash_flow_yield
- … and 644 more (full list in `_results.json`)

## Parabolic short candidates: 22

- ACHC
- APP
- ARRY
- AUGO
- EWTX
- FLY
- FROG
- FRVO
- FUN
- IONQ

## Parabolic long / mean-reversion: 8

- AXON
- CVI
- DOX
- FIS
- IRTC
- NRIX
- SNDX
- VCYT
