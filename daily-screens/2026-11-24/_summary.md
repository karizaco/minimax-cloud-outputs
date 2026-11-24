# Daily sweep summary

Generated 2026-11-24

> **shibui T+1**: the T+1 book is for **2026-11-23** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-24** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **50**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **34.93975903614458**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 281 | 281 |
| B_stockbee_ep9m | 237 | 237 |
| C_qullamaggie_rs | 47 | 47 |
| D_qullamaggie_ep | 177 | 177 |
| E_qullamaggie_5d_gainers | 3 | 3 |
| F_qullamaggie_5d_losers | 1 | 1 |
| G_peoplewish | 403 | 403 |
| H_hernandez_theme | 58 | 58 |
| K_stockbee_anticipation | 461 | 461 |

## Tier-A (appears in ≥ 3 stylists): 8

- **ALAB** (stylists: 3, origins: 3, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) [t1 2026-11-23] EXTENDED · quality: trailing_pe, operating_pe
- **CRWV** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-24] EXTENDED · quality: free_cash_flow_yield, debt_to_equity
- **DELL** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-24] EXTENDED
- **KYMR** (stylists: 5, origins: 7, sources: A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme, TV_volume_breakout) [fresh+t1 2026-11-24] EXTENDED · quality: free_cash_flow_yield
- **LITE** (stylists: 3, origins: 3, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) [t1 2026-11-23] EXTENDED · quality: operating_pe
- **NVDA** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-24] EXTENDED · quality: earnings_quality_flags
- **SITM** (stylists: 3, origins: 3, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) [t1 2026-11-23] EXTENDED · quality: trailing_pe, operating_pe, earnings_quality_flags
- **SMTC** (stylists: 3, origins: 3, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) [t1 2026-11-23] EXTENDED · quality: trailing_pe, operating_pe

## Tier-A — FRESH vs EXTENDED: 0 fresh / 8 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** ALAB, CRWV, DELL, KYMR, LITE, NVDA, SITM, SMTC

## Valuation / quality overlay: 721 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **AAUC** — free_cash_flow_yield
- **ABBV** — trailing_revenue_peg
- **ABSI** — free_cash_flow_yield
- **ABVX** — free_cash_flow_yield
- **ACAA** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACEL** — debt_to_equity
- **ACHR** — free_cash_flow_yield
- **ACI** — debt_to_equity
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
- **AHRT** — debt_to_equity
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **ALAB** — trailing_pe, operating_pe
- **ALC** — trailing_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALH** — trailing_revenue_peg, debt_to_equity
- **ALK** — free_cash_flow_yield, debt_to_equity
- … and 681 more (full list in `_results.json`)

## Parabolic short candidates: 3

- BRBR
- MPT
- SLS

## Parabolic long / mean-reversion: 1

- SNEX
