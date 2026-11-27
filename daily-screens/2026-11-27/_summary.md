# Daily sweep summary

Generated 2026-11-27

> **shibui T+1**: the T+1 book is for **2026-11-25** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-27** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **False**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **50.64220183486239**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 150 | 150 |
| B_stockbee_ep9m | 213 | 213 |
| C_qullamaggie_rs | 51 | 51 |
| D_qullamaggie_ep | 0 | 0 |
| E_qullamaggie_5d_gainers | 5 | 5 |
| F_qullamaggie_5d_losers | 3 | 3 |
| G_peoplewish | 437 | 437 |
| H_hernandez_theme | 67 | 67 |
| K_stockbee_anticipation | 493 | 493 |

## Tier-A (appears in ≥ 3 stylists): 4

- **CAR** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish) [t1 2026-11-25] EXTENDED
- **CHTR** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish) [t1 2026-11-25] EXTENDED · quality: debt_to_equity
- **INIO** (stylists: 3, origins: 3, sources: A_stockbee_4pct, G_peoplewish, jeff_sun_canslim) [t1 2026-11-25] EXTENDED · quality: debt_to_equity
- **SHLS** (stylists: 3, origins: 3, sources: A_stockbee_4pct, G_peoplewish, jeff_sun_canslim) [t1 2026-11-25] EXTENDED · quality: free_cash_flow_yield, earnings_quality_flags

## Tier-A — FRESH vs EXTENDED: 0 fresh / 4 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** CAR, CHTR, INIO, SHLS

## Valuation / quality overlay: 671 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **AACO** — free_cash_flow_yield
- **AADX** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **AAUC** — free_cash_flow_yield
- **ABBV** — trailing_pe, trailing_revenue_peg
- **ABVX** — free_cash_flow_yield
- **ACAA** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACDC** — free_cash_flow_yield, debt_to_equity
- **ACEL** — debt_to_equity
- **ACHR** — free_cash_flow_yield
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ADAM** — debt_to_equity
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
- **AFL** — earnings_quality_flags
- **AFRM** — debt_to_equity, earnings_quality_flags
- **AGLT** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AGRO** — debt_to_equity
- **AHR** — trailing_pe, operating_pe, trailing_revenue_peg, free_cash_flow_yield
- **AHRT** — debt_to_equity
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALLY** — debt_to_equity
- … and 631 more (full list in `_results.json`)

## Parabolic short candidates: 5

- CELC
- COGT
- INSM
- KYMR
- VRDN

## Parabolic long / mean-reversion: 3

- AMBA
- SLS
- SNEX
