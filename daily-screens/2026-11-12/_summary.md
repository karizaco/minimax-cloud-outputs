# Daily sweep summary

Generated 2026-11-13

> **shibui T+1**: the T+1 book is for **2026-11-11** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-12** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **False**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **53.03**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 199 | 199 |
| B_stockbee_ep9m | 195 | 195 |
| C_qullamaggie_rs | 81 | 81 |
| D_qullamaggie_ep | 5 | 5 |
| E_qullamaggie_5d_gainers | 13 | 13 |
| F_qullamaggie_5d_losers | 6 | 6 |
| G_peoplewish | 351 | 351 |
| H_hernandez_theme | 62 | 62 |
| K_stockbee_anticipation | 402 | 402 |
| jeff_sun_canslim | 154 | 154 |

## Tier-A (appears in ≥ 3 stylists): 6

- **AXGN** (stylists: 5, origins: 5, sources: A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, jeff_sun_canslim) [t1 2026-11-11] EXTENDED
- **AZTA** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme) [t1 2026-11-11] EXTENDED
- **CAPR** (stylists: 3, origins: 4, sources: A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, H_hernandez_theme) [t1 2026-11-11] EXTENDED · quality: free_cash_flow_yield
- **CRWV** (stylists: 3, origins: 6, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish) [fresh+t1 2026-11-12] EXTENDED · quality: free_cash_flow_yield, debt_to_equity
- **NBIS** (stylists: 3, origins: 5, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-12] EXTENDED · quality: trailing_pe, free_cash_flow_yield
- **SHAZ** (stylists: 3, origins: 3, sources: A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) [t1 2026-11-11] EXTENDED · quality: free_cash_flow_yield

## Tier-A — FRESH vs EXTENDED: 0 fresh / 6 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** (none)

**Extended:** AXGN, AZTA, CAPR, CRWV, NBIS, SHAZ

## Valuation / quality overlay: 646 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABBV** — trailing_pe, trailing_revenue_peg
- **ABCL** — free_cash_flow_yield
- **ABUS** — earnings_quality_flags
- **ACAD** — earnings_quality_flags
- **ACHR** — free_cash_flow_yield
- **ACI** — debt_to_equity
- **ACMR** — free_cash_flow_yield, earnings_quality_flags
- **ACRS** — free_cash_flow_yield
- **ADC** — free_cash_flow_yield
- **ADI** — operating_pe
- **ADMA** — trailing_revenue_peg, earnings_quality_flags
- **ADPT** — free_cash_flow_yield, debt_to_equity
- **ADT** — debt_to_equity
- **AEAQ** — free_cash_flow_yield
- **AEE** — free_cash_flow_yield, debt_to_equity
- **AEHR** — free_cash_flow_yield
- **AEIS** — earnings_quality_flags
- **AEP** — free_cash_flow_yield, debt_to_equity
- **AES** — free_cash_flow_yield, debt_to_equity
- **AFL** — earnings_quality_flags
- **AFRM** — operating_pe, debt_to_equity, earnings_quality_flags
- **AGBK** — free_cash_flow_yield, debt_to_equity
- **AGL** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AI** — free_cash_flow_yield
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALLY** — debt_to_equity
- **ALM** — trailing_pe, free_cash_flow_yield
- **ALMR** — free_cash_flow_yield
- … and 606 more (full list in `_results.json`)

## Parabolic short candidates: 13

- AAON
- APP
- CRWV
- EWTX
- FLY
- FROG
- FRVO
- FUN
- KRMN
- MGNI

## Parabolic long / mean-reversion: 6

- AXON
- CAI
- IBRX
- IONS
- IRTC
- OPEN
