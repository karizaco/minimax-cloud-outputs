# Daily sweep summary

Generated 2026-11-25

> **shibui T+1**: the T+1 book is for **2026-11-24** (shibui's newest ingested session).
> **Fresh book**: the cron-day settled bar is **2026-11-25** — the primary book. Every row in `_results.json` carries `data_as_of` and `source`.

## Regime

- size_cut_pct: **0**
- uncertainty: **True**
- late_cycle: **False**
- breadth % S&P > 20-DMA: **41.06813996316759**

## Screen coverage (rows_passing = names that passed the branch filter)

| Branch | rows_passing | rows_kept |
|---|---|---|
| A_stockbee_4pct | 207 | 207 |
| B_stockbee_ep9m | 200 | 200 |
| C_qullamaggie_rs | 60 | 60 |
| D_qullamaggie_ep | 4 | 4 |
| E_qullamaggie_5d_gainers | 4 | 4 |
| F_qullamaggie_5d_losers | 4 | 4 |
| G_peoplewish | 415 | 415 |
| H_hernandez_theme | 64 | 64 |
| K_stockbee_anticipation | 496 | 496 |

> **Cap signature:** B_stockbee_ep9m, C_qullamaggie_rs land(s) exactly on a known cap (30 / 50 / 60 / 200). When `rows_passing` agrees, that is the true count; when it does not, the branch was truncated and the run must fail.

## Tier-A (appears in ≥ 3 stylists): 7

- **ANF** (stylists: 3, origins: 4, sources: A_stockbee_4pct, A_tv_breakout_4pct, D_qullamaggie_ep, G_peoplewish) [fresh+t1 2026-11-25] EXTENDED
- **COGT** (stylists: 3, origins: 4, sources: A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-25] EXTENDED · quality: free_cash_flow_yield
- **INSM** (stylists: 4, origins: 8, sources: A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme) [fresh+t1 2026-11-25] EXTENDED · quality: free_cash_flow_yield
- **IRON** (stylists: 3, origins: 3, sources: A_stockbee_4pct, G_peoplewish, H_hernandez_theme) [t1 2026-11-24] · quality: free_cash_flow_yield
- **KSS** (stylists: 3, origins: 6, sources: A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout) [fresh+t1 2026-11-25] EXTENDED · quality: debt_to_equity
- **NAMS** (stylists: 3, origins: 3, sources: A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme) [t1 2026-11-24] EXTENDED · quality: free_cash_flow_yield
- **STOK** (stylists: 4, origins: 5, sources: A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, H_hernandez_theme, TV_volume_breakout) [fresh+t1 2026-11-25] EXTENDED · quality: free_cash_flow_yield

## Tier-A — FRESH vs EXTENDED: 1 fresh / 6 extended

`extended` is a LABEL (ATR% > 5, RSI > 75, > 15% above its 20-DMA, or 3+ consecutive up sessions) with its reasons published. Nothing is dropped from the book.

**Fresh (not extended):** IRON

**Extended:** ANF, COGT, INSM, KSS, NAMS, STOK

## Valuation / quality overlay: 729 candidates carry a flag

A NULL is a flag, never a pass: no reported earnings is itself a risk marker. See `daily-sweep.md` for the per-name reasons.

- **A** — trailing_revenue_peg
- **AACO** — free_cash_flow_yield
- **AAOI** — free_cash_flow_yield
- **AAON** — free_cash_flow_yield
- **AAPL** — trailing_revenue_peg
- **AAT** — trailing_pe, debt_to_equity
- **ABSI** — free_cash_flow_yield
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
- **AGIO** — free_cash_flow_yield
- **AGNC** — debt_to_equity, earnings_quality_flags
- **AHR** — trailing_pe, operating_pe, trailing_revenue_peg, free_cash_flow_yield
- **AHRT** — debt_to_equity
- **AKAM** — trailing_revenue_peg, debt_to_equity
- **AKR** — trailing_pe, operating_pe
- **ALAB** — trailing_pe, operating_pe
- **ALF** — trailing_pe, free_cash_flow_yield, earnings_quality_flags
- **ALGM** — trailing_pe, operating_pe, trailing_revenue_peg
- **ALGT** — debt_to_equity
- **ALKS** — operating_pe
- **ALLY** — debt_to_equity
- **ALM** — operating_pe, free_cash_flow_yield, earnings_quality_flags
- **ALMR** — free_cash_flow_yield
- … and 689 more (full list in `_results.json`)

## Parabolic short candidates: 4

- BRBR
- INSM
- KYMR
- ZS

## Parabolic long / mean-reversion: 4

- BTDR
- SHAZ
- SLS
- SNEX
