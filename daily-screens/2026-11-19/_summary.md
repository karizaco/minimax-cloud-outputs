# Daily sweep summary

Generated 2026-11-19

> **shibui T+1**: the T+1 book is for **2026-11-18** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-19** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **21.200750469043154**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 145 | 145 |
| B_stockbee_ep9m | 198 | 198 |
| C_qullamaggie_rs | 54 | 54 |
| D_qullamaggie_ep | 0 | 0 |
| E_qullamaggie_5d_gainers | 3 | 3 |
| F_qullamaggie_5d_losers | 20 | 20 |
| G_peoplewish | 352 | 352 |
| H_hernandez_theme | 45 | 45 |
| K_stockbee_anticipation | 452 | 452 |

## Tier-A (appears in ≥ 3 stylists): 5

- **BRBR** (stylists: 3, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout) [fresh+t1 2026-11-19] EXTENDED
- **NTSK** (stylists: 4, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-19] EXTENDED · quality: free_cash_flow_yield, debt_to_equity
- **NUAI** (stylists: 3, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout) [fresh+t1 2026-11-19] EXTENDED · quality: free_cash_flow_yield
- **OKTA** (stylists: 3, origins: 4, sources: A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-19] EXTENDED · quality: trailing_pe, operating_pe, trailing_revenue_peg
- **PANW** (stylists: 3, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-19] EXTENDED · quality: trailing_pe, operating_pe, trailing_revenue_peg

## Tier-A — FRESH vs EXTENDED: 0 fresh / 5 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** BRBR, NTSK, NUAI, OKTA, PANW

## Valuation / quality overlay: 618 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAP** — debt_to_equity
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_revenue_peg
- **ABSI** — free_cash_flow_yield
- **ACAA** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACCV** — debt_to_equity
- **ACEL** — debt_to_equity
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ADC** — free_cash_flow_yield
- **ADMA** — trailing_revenue_peg, earnings_quality_flags
- **ADP** — trailing_revenue_peg
- **ADPT** — free_cash_flow_yield, debt_to_equity
- **ADT** — debt_to_equity
- **ADV** — debt_to_equity
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
- **AGYS** — trailing_pe, operating_pe, trailing_revenue_peg
- **AHR** — trailing_pe, operating_pe, trailing_revenue_peg, free_cash_flow_yield
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALM** — operating_pe, free_cash_flow_yield, earnings_quality_flags
- … and 578 more (full list in `_results.json`)

## Parabolic short candidates: 3

- FRMI
- MOD
- SLS

## Parabolic long / mean-reversion: 20

- AAOI
- ACHR
- ASST
- ASTS
- BETA
- BTDR
- CTVA
- FCEL
- GDS
- IONQ
