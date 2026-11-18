# Daily sweep summary

Generated 2026-11-18

> **shibui T+1**: the T+1 book is for **2026-11-17** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-18** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **32.00740055504163**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 41 | 41 |
| B_stockbee_ep9m | 199 | 199 |
| C_qullamaggie_rs | 58 | 58 |
| D_qullamaggie_ep | 1 | 1 |
| E_qullamaggie_5d_gainers | 3 | 3 |
| F_qullamaggie_5d_losers | 11 | 11 |
| G_peoplewish | 345 | 345 |
| H_hernandez_theme | 66 | 66 |
| K_stockbee_anticipation | 483 | 483 |

## Tier-A (appears in ≥ 3 stylists): 4

- **ALAB** (stylists: 3, origins: 3, sources: A_stockbee_4pct, G_peoplewish, jeff_sun_canslim) [t1 2026-11-17] EXTENDED · quality: trailing_pe, operating_pe
- **BRBR** (stylists: 3, origins: 5, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, TV_volume_breakout) [fresh+t1 2026-11-18] EXTENDED
- **RYTM** (stylists: 4, origins: 4, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) [t1 2026-11-17] EXTENDED · quality: free_cash_flow_yield
- **SLS** (stylists: 4, origins: 8, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme) [fresh+t1 2026-11-18] EXTENDED · quality: free_cash_flow_yield

## Tier-A — FRESH vs EXTENDED: 0 fresh / 4 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** ALAB, BRBR, RYTM, SLS

## Valuation / quality overlay: 582 candidates carry a flag

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
- **AFRM** — debt_to_equity, earnings_quality_flags
- **AGL** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AGYS** — trailing_pe, operating_pe, trailing_revenue_peg
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALM** — operating_pe, free_cash_flow_yield, earnings_quality_flags
- **ALNY** — earnings_quality_flags
- **ALRS** — trailing_revenue_peg
- **ALUB** — free_cash_flow_yield
- **ALX** — debt_to_equity, earnings_quality_flags
- **AMD** — trailing_pe, operating_pe
- **AMKR** — free_cash_flow_yield
- **AMPX** — free_cash_flow_yield
- … and 542 more (full list in `_results.json`)

## Parabolic short candidates: 3

- FRMI
- MOD
- SLS

## Parabolic long / mean-reversion: 11

- ACHR
- AMPX
- BETA
- BTDR
- CTVA
- IONQ
- JOBY
- QS
- RGTI
- SMMT
