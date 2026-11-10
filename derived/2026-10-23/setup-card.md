# Setup card — published 2026-10-23

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-10 · **Covers:** 39 stalk name(s), 1 Tier-A name(s); entry session 2026-10-26 · read-only

> **Read this before the table.**
>
> 1. **This is not a routine output.** The MiniMax agent keeps writing
>    `daily-screens/`, `earnings/` and `us-eod/`. This card only joins them.
> 2. **No direction and no size.** `held`, `faded` and `reversed` describe
>    a session path. They are not an instruction.
> 3. **The tradeable moment is the next open after this card's date,**
>    not the close the screen describes. See the session clock.
> 4. **Degraded paths.**
>    - No reactions artifact for this fire (`earnings/<date>-reactions.md`), so no catalyst status and no morning-gap path.

## Session clock

| Clock | Session | What the numbers on that clock describe |
|---|---|---|
| Screen | `—` | the metrics the 18:30 sweep computed (`not recorded`) |
| Observation | `2026-10-23` | the settled close on the day the card was published |
| Entry | `2026-10-26` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | — |
| `uncertainty` | None |
| `late_cycle` | False |
| breadth % (screen input) | — |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 39 name(s) and Tier-A has 1.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAL | stalk | stockbee | 12.60 | 12.60 | +2.98 | — | — | no morning row | — | none |
| ADT | stalk | jeff_sun | 6.99 | 6.99 | +2.79 | — | — | no morning row | — | none |
| AMLX | stalk | qullamaggie | 28.57 | 28.57 | -1.58 | — | — | no morning row | — | none |
| BALY | stalk | peoplewish | 13.76 | 13.76 | -0.22 | — | — | no morning row | — | none |
| BIP | stalk | jeff_sun | 37.29 | 37.29 | +2.53 | — | — | no morning row | — | none |
| CCS | stalk | stockbee | 58.34 | 58.34 | +7.48 | — | — | no morning row | — | none |
| CLBK | stalk | jeff_sun | 10.86 | 10.86 | +2.16 | — | — | no morning row | — | none |
| CMPR | stalk | jeff_sun | 82.27 | 82.27 | +1.36 | — | — | no morning row | — | none |
| COF/PJ | stalk | jeff_sun | 16.09 | 16.09 | +0.44 | — | — | no morning row | — | none |
| COF/PL | stalk | jeff_sun | 14.77 | 14.77 | +0.96 | — | — | no morning row | — | none |
| CPB | stalk | stockbee | 21.26 | 21.26 | +8.69 | — | — | no morning row | — | none |
| CWBC | stalk | jeff_sun | 26.29 | 26.29 | +2.78 | — | — | no morning row | — | none |
| ECO | stalk | qullamaggie | 90.05 | 90.05 | -1.29 | — | — | no morning row | — | none |
| EPAC | stalk | jeff_sun | 35.63 | 35.63 | +0.48 | — | — | no morning row | — | none |
| EXE | stalk | jeff_sun | 92.96 | 92.96 | +0.14 | — | — | no morning row | — | none |
| FBYD | stalk | peoplewish | 8.28 | 8.28 | +0.85 | — | — | no morning row | — | none |
| FIS | stalk | jeff_sun | 38.29 | 38.29 | +5.13 | — | — | no morning row | — | none |
| FIVN | stalk | qullamaggie | 35.10 | 35.10 | -0.54 | — | — | no morning row | — | none |
| FLO | stalk | stockbee | 6.42 | 6.42 | +10.50 | — | — | no morning row | — | none |
| FRPT | stalk | jeff_sun | 67.00 | 67.00 | +7.06 | — | — | no morning row | — | none |
| GPI | stalk | stockbee | 242.79 | 242.79 | +7.98 | — | — | no morning row | — | none |
| INDV | stalk | jeff_sun | 35.33 | 35.33 | +1.55 | — | — | no morning row | — | none |
| INVA | stalk | jeff_sun | 21.06 | 21.06 | +0.72 | — | — | no morning row | — | none |
| JNJ | stalk | jeff_sun | 267.61 | 267.61 | +3.81 | — | — | no morning row | — | none |
| KRG | stalk | jeff_sun | 24.77 | 24.77 | +2.44 | — | — | no morning row | — | none |
| KRNY | stalk | jeff_sun | 9.27 | 9.27 | +2.32 | — | — | no morning row | — | none |
| LAD | stalk | stockbee | 291.07 | 291.07 | +8.15 | — | — | no morning row | — | none |
| LULU | stalk | stockbee | 104.06 | 104.06 | +7.80 | — | — | no morning row | — | none |
| MG | stalk | stockbee | 21.42 | 21.42 | +0.52 | — | — | no morning row | — | none |
| MHK | stalk | stockbee | 128.70 | 128.70 | +9.03 | — | — | no morning row | — | none |
| MRP | stalk | jeff_sun | 23.97 | 23.97 | +3.81 | — | — | no morning row | — | none |
| PCG | stalk | stockbee | 12.98 | 12.98 | -1.29 | — | — | no morning row | — | none |
| RAMP | stalk | jeff_sun | 38.24 | 38.24 | +0.10 | — | — | no morning row | — | none |
| SHC | stalk | jeff_sun | 18.13 | 18.13 | +2.03 | — | — | no morning row | — | none |
| SXT | stalk | jeff_sun | 130.94 | 130.94 | -0.95 | — | — | no morning row | — | none |
| TFIN | stalk | jeff_sun | 62.21 | 62.21 | +0.35 | — | — | no morning row | — | none |
| TSLX | stalk | jeff_sun | 17.38 | 17.38 | +2.30 | — | — | no morning row | — | none |
| UPBD | stalk | stockbee | 17.37 | 17.37 | +7.42 | — | — | no morning row | — | none |
| WHR | stalk | stockbee | 28.80 | 28.80 | +8.56 | — | — | no morning row | — | none |
| XLAB | tier-a | peoplewish|qullamaggie|stockbee | 4.71 | 4.71 | +73.16 | — | — | no morning row | — | none |

**What the tag columns mean.** `Tags published` is copied from the screen CSV
when that file has a `setup_tags` column — only some dates do. `Tags recomputed`
is calculated here from `us-eod/` bars. `none` there does not mean the routine
found no tag. Compression needs 50 sessions and MACD is not in `us-eod/` at all,
so those two are never recomputed. The blocked list is in `setup-card.csv`.

## Unchecked gaps that held

Morning `PRE_GAP` names the scanner marked as not looked up, whose gap
then held or extended into the observation close. Sorted by the size of
the morning gap. **Not checked is not the same as no catalyst.**

None on this date, or no verified morning file to read.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

