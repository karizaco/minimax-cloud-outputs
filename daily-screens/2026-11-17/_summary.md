# Daily sweep summary

Generated 2026-11-17

> **shibui T+1**: the T+1 book is for **2026-11-16** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-17** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **34.16206261510129**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 37 | 37 |
| B_stockbee_ep9m | 208 | 208 |
| C_qullamaggie_rs | 73 | 73 |
| D_qullamaggie_ep | 2 | 2 |
| E_qullamaggie_5d_gainers | 1 | 1 |
| F_qullamaggie_5d_losers | 10 | 10 |
| G_peoplewish | 338 | 338 |
| H_hernandez_theme | 47 | 47 |
| K_stockbee_anticipation | 534 | 534 |

## Tier-A (appears in ≥ 3 stylists): 2

- **CGON** (stylists: 4, origins: 6, sources: A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme) [t1 2026-11-16] EXTENDED · quality: free_cash_flow_yield
- **SEZL** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish) [t1 2026-11-16] EXTENDED

## Tier-A — FRESH vs EXTENDED: 0 fresh / 2 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** CGON, SEZL

## Valuation / quality overlay: 605 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_pe, trailing_revenue_peg
- **ABCL** — free_cash_flow_yield
- **ACAD** — earnings_quality_flags
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ACRS** — free_cash_flow_yield
- **ADC** — free_cash_flow_yield
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
- **AFL** — earnings_quality_flags
- **AGL** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALM** — trailing_pe, free_cash_flow_yield
- **ALNY** — earnings_quality_flags
- **ALUB** — free_cash_flow_yield
- **ALX** — debt_to_equity, earnings_quality_flags
- **AMD** — trailing_pe, operating_pe
- **AMGN** — trailing_revenue_peg, debt_to_equity
- **AMKR** — free_cash_flow_yield
- **AMT** — debt_to_equity
- **AMZN** — free_cash_flow_yield, earnings_quality_flags
- … and 565 more (full list in `_results.json`)

## Parabolic short candidates: 1

- FRMI

## Parabolic long / mean-reversion: 10

- BBAI
- BTDR
- CTVA
- IONQ
- LEGN
- NVAX
- PLUG
- RGTI
- SMMT
- TE
