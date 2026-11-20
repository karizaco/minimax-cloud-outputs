# Daily sweep summary

Generated 2026-11-20

> **shibui T+1**: the T+1 book is for **2026-11-19** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-20** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **14.943609022556393**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 41 | 41 |
| B_stockbee_ep9m | 224 | 224 |
| C_qullamaggie_rs | 45 | 45 |
| D_qullamaggie_ep | 0 | 0 |
| E_qullamaggie_5d_gainers | 4 | 4 |
| F_qullamaggie_5d_losers | 18 | 18 |
| G_peoplewish | 368 | 368 |
| H_hernandez_theme | 32 | 32 |
| K_stockbee_anticipation | 506 | 506 |

## Tier-A (appears in ≥ 3 stylists): 4

- **INSM** (stylists: 4, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) [t1 2026-11-19] EXTENDED · quality: free_cash_flow_yield
- **NTSK** (stylists: 3, origins: 4, sources: A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish) [t1 2026-11-19] EXTENDED · quality: free_cash_flow_yield, debt_to_equity
- **OKTA** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish) [t1 2026-11-19] EXTENDED · quality: trailing_pe, operating_pe, trailing_revenue_peg
- **VRDN** (stylists: 4, origins: 4, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) [t1 2026-11-19] · quality: free_cash_flow_yield

## Tier-A — FRESH vs EXTENDED: 1 fresh / 3 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** VRDN

**Extended:** INSM, NTSK, OKTA

## Valuation / quality overlay: 598 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_revenue_peg
- **ACAA** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACEL** — debt_to_equity
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ADMA** — trailing_revenue_peg, earnings_quality_flags
- **ADP** — trailing_revenue_peg
- **ADPT** — free_cash_flow_yield, debt_to_equity
- **ADT** — debt_to_equity
- **AEAQ** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **AEE** — free_cash_flow_yield, debt_to_equity
- **AEHR** — free_cash_flow_yield
- **AEIS** — earnings_quality_flags
- **AEP** — free_cash_flow_yield, debt_to_equity
- **AES** — free_cash_flow_yield, debt_to_equity
- **AESI** — free_cash_flow_yield
- **AFL** — earnings_quality_flags
- **AFRM** — debt_to_equity, earnings_quality_flags
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AHR** — trailing_pe, operating_pe, trailing_revenue_peg, free_cash_flow_yield
- **AHRT** — debt_to_equity
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALC** — trailing_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALLY** — debt_to_equity
- **ALM** — operating_pe, free_cash_flow_yield, earnings_quality_flags
- **ALNY** — earnings_quality_flags
- **ALRM** — trailing_revenue_peg
- **ALRS** — trailing_revenue_peg
- … and 558 more (full list in `_results.json`)

## Parabolic short candidates: 4

- BRBR
- MOD
- SLS
- TU

## Parabolic long / mean-reversion: 18

- AAOI
- ACHR
- ASST
- ASTS
- BETA
- BTDR
- FCEL
- GDS
- HTFL
- IONQ
