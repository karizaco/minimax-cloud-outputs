# Daily sweep summary

Generated 2026-11-16

> **shibui T+1**: the T+1 book is for **2026-11-13** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-16** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **False**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **43.926940639269404**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 71 | 71 |
| B_stockbee_ep9m | 170 | 170 |
| C_qullamaggie_rs | 64 | 64 |
| D_qullamaggie_ep | 2 | 2 |
| E_qullamaggie_5d_gainers | 6 | 6 |
| F_qullamaggie_5d_losers | 4 | 4 |
| G_peoplewish | 334 | 334 |
| H_hernandez_theme | 57 | 57 |
| K_stockbee_anticipation | 534 | 534 |

## Tier-A (appears in ≥ 3 stylists): 3

- **CBRS** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-16] EXTENDED · quality: free_cash_flow_yield
- **CGON** (stylists: 5, origins: 7, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, H_hernandez_theme, TV_volume_breakout) [fresh+t1 2026-11-16] EXTENDED · quality: free_cash_flow_yield
- **MOD** (stylists: 3, origins: 4, sources: A_stockbee_4pct, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish) [t1 2026-11-13] EXTENDED · quality: trailing_pe, free_cash_flow_yield

## Tier-A — FRESH vs EXTENDED: 0 fresh / 3 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** CBRS, CGON, MOD

## Valuation / quality overlay: 598 candidates carry a flag

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
- **ACCV** — debt_to_equity
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
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
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALLY** — debt_to_equity
- **ALM** — trailing_pe, free_cash_flow_yield
- **ALNY** — earnings_quality_flags
- **ALUB** — free_cash_flow_yield
- **AMD** — trailing_pe, operating_pe
- **AMGN** — trailing_revenue_peg, debt_to_equity
- **AMKR** — free_cash_flow_yield
- **AMT** — debt_to_equity
- **AMZN** — free_cash_flow_yield, earnings_quality_flags
- **APLD** — free_cash_flow_yield, debt_to_equity
- … and 558 more (full list in `_results.json`)

## Parabolic short candidates: 6

- AAON
- FRMI
- FRVO
- LGN
- LQDA
- MOD

## Parabolic long / mean-reversion: 4

- BZ
- IBRX
- IONS
- LEGN
