# Daily sweep summary

Generated 2026-11-23

> **shibui T+1**: the T+1 book is for **2026-11-20** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-23** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **31.49532710280374**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 20 | 20 |
| B_stockbee_ep9m | 282 | 282 |
| C_qullamaggie_rs | 29 | 29 |
| D_qullamaggie_ep | 0 | 0 |
| E_qullamaggie_5d_gainers | 3 | 3 |
| F_qullamaggie_5d_losers | 47 | 47 |
| G_peoplewish | 387 | 387 |
| H_hernandez_theme | 44 | 44 |
| K_stockbee_anticipation | 446 | 446 |

## Tier-A (appears in ≥ 3 stylists): 4

- **INTC** (stylists: 3, origins: 5, sources: A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish) [fresh+t1 2026-11-23] EXTENDED · quality: operating_pe
- **IREN** (stylists: 3, origins: 6, sources: A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish) [fresh+t1 2026-11-23] EXTENDED · quality: free_cash_flow_yield, debt_to_equity
- **NVDA** (stylists: 4, origins: 7, sources: A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, TV_volume_breakout, jeff_sun_canslim) [fresh+t1 2026-11-23] EXTENDED · quality: earnings_quality_flags
- **SNDK** (stylists: 3, origins: 5, sources: B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish) [fresh+t1 2026-11-23] EXTENDED

## Tier-A — FRESH vs EXTENDED: 0 fresh / 4 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** INTC, IREN, NVDA, SNDK

## Valuation / quality overlay: 598 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_revenue_peg
- **ABVX** — free_cash_flow_yield
- **ACAA** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACEL** — debt_to_equity
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
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AHR** — trailing_pe, operating_pe, trailing_revenue_peg, free_cash_flow_yield
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALC** — trailing_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALKS** — operating_pe
- **ALLY** — debt_to_equity
- **ALM** — operating_pe, free_cash_flow_yield, earnings_quality_flags
- **ALNY** — earnings_quality_flags
- **ALRM** — trailing_revenue_peg
- … and 558 more (full list in `_results.json`)

## Parabolic short candidates: 3

- BRBR
- SLS
- TU

## Parabolic long / mean-reversion: 47

- AAOI
- ACHR
- AEHR
- APLD
- ASST
- ASTS
- ASX
- AVAV
- AXTI
- BE
