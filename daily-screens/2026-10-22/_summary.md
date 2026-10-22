# _summary — cron #9 daily sweep

- **Cron date**: 2026-10-22 (Thursday) · **Data session**: **2026-10-21** — last completed close
- **Fired at**: 07:32 ET (see `daily-sweep.md` → *Schedule deviation*)
- **Generated**: 2026-10-22T11:33:57Z

## 1. Regime state

- Breadth: **65.82%** of >$10B names above the 20-DMA (869 names); 48.1% above the 50-DMA.
- VIX **16.68** (CBOE, 2026-10-21) · VIX/VXN proxy **0.7482** (no inversion).
- `size_cut_pct` **0** · `uncertainty` **false** · `late_cycle` **false**.
- Read: constructive short-term tape (broad above the 20-DMA, VIX in the mid-teens) but the 50-DMA line is the divider — IWM sits -3.83% below its 50-DMA while SPY is 0.62% above. Small caps are the weak leg.

## 2. Tier-A names (convergence >= 4 screens)

| Sym | Close | Chg | 1M | 3M | Flags |
|---|---|---|---|---|---|
| **RCEL** | 15.29 | 10.80% | 38.50% | 219.87% | bonde_4pct, kse, kullamagi_momentum, qm |
| **LIFE** | 44.22 | 7.67% | 21.68% | 135.46% | bonde_4pct, kullamagi_momentum, pw, qm |

Full merged counts — **Master 200** · **Stalk 54** · **Focus 13** · **Tier-A 2**.

## 3. Parabolic short / long candidates

- **Short**: 1 name(s) — BRZE. Thin: the 5-day >=+20% plus >=1.30x the 20-DMA plus 1.5x RVOL conjunction is demanding in a quiet tape.
- **Long / reversal**: 10 names — GEMI, QVCG, BRUN, BLZE, FRVO, FUN, ITG, AVEX, QMCO, FMC.

## 4. Reversal-bullish (15:55 ET Bonde)

**Not run.** The skill gates this scan to weekdays 15:30–16:00 ET. This fire landed at 07:32 ET, outside the window. No names are reported rather than a loose substitute being presented as the real scan.

## Verification

- **15/15** picks independently re-derived from Yahoo Finance matched the TradingView scanner's daily change to within 0.35pp (observed max delta: 0.00pp).
- Session date confirmed three ways: CBOE VIX history ends 2026-10-21; Yahoo daily bars end 2026-10-21; scanner `close` equals Yahoo's 2026-10-21 close at 0.00% on AAPL/NVDA/TSLA.

