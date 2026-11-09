# Setup card — published 2026-11-05

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-09 · **Covers:** 8 stalk name(s), 6 Tier-A name(s); entry session 2026-11-06 · read-only

> **Read this before the table.**
>
> 1. **This is not a routine output.** The MiniMax agent keeps writing
>    `daily-screens/`, `earnings/` and `us-eod/`. This card only joins them.
> 2. **No direction and no size.** `held`, `faded` and `reversed` describe
>    a session path. They are not an instruction.
> 3. **The tradeable moment is the next open after this card's date,**
>    not the close the screen describes. See the session clock.

## Session clock

| Clock | Session | What the numbers on that clock describe |
|---|---|---|
| Screen | `2026-11-04` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-05` | the settled close on the day the card was published |
| Entry | `2026-11-06` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | True |
| `late_cycle` | False |
| breadth % (screen input) | 58.31 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 8 name(s) and Tier-A has 6.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AFRM | stalk | jeff_sun|peoplewish|stockbee | 75.59 | 69.66 | -7.84 | — | — | no morning row | — | none |
| AG | stalk | jeff_sun|stockbee | 15.39 | 14.89 | -3.25 | — | — | no morning row | — | none |
| ANET | stalk | jeff_sun|stockbee | 178.48 | 159.16 | -10.82 | -3.63 | extended | not_looked_up | — | none |
| B | stalk | jeff_sun|stockbee | 40.13 | 40.34 | +0.52 | — | — | no morning row | — | none |
| BFC | stalk | jeff_sun|stockbee | 149.60 | 147.45 | -1.44 | — | — | no morning row | — | none |
| HL | stalk | jeff_sun|stockbee | 14.95 | 14.45 | -3.34 | +2.27 | reversed | not_looked_up | — | none |
| LSCC | stalk | jeff_sun|peoplewish | 107.25 | 98.03 | -8.60 | — | — | no morning row | — | none |
| TE | stalk | peoplewish|qullamaggie | 2.73 | 2.28 | -16.48 | — | — | no morning row | — | none |
| DUOL | tier-a | peoplewish|qullamaggie|stockbee | 161.27 | 157.02 | -2.64 | — | — | no morning row | — | none |
| KD | tier-a | peoplewish|qullamaggie|stockbee | 16.84 | 16.18 | -3.92 | — | — | no morning row | — | none |
| LIVN | tier-a | hernandez|qullamaggie|stockbee | 91.14 | 91.14 | -3.24 | — | — | no morning row | — | none |
| OUST | tier-a | peoplewish|qullamaggie|stockbee | 33.54 | 30.52 | -9.00 | -6.05 | extended | not_looked_up | — | none |
| VRDN | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 28.55 | 28.55 | -1.74 | — | — | no morning row | — | none |
| XNCR | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 34.05 | 34.05 | -2.80 | — | — | no morning row | — | none |

**What the tag columns mean.** `Tags published` is copied from the screen CSV
when that file has a `setup_tags` column — only some dates do. `Tags recomputed`
is calculated here from `us-eod/` bars. `none` there does not mean the routine
found no tag. Compression needs 50 sessions and MACD is not in `us-eod/` at all,
so those two are never recomputed. The blocked list is in `setup-card.csv`.

## Unchecked gaps that held

Morning `PRE_GAP` names the scanner marked as not looked up, whose gap
then held or extended into the observation close. Sorted by the size of
the morning gap. **Not checked is not the same as no catalyst.**

| Ticker | Morning gap | Observation chg | Path | Also on Stalk or Tier-A |
|---|---|---|---|---|
| ZG | -11.95 | -9.40 | held | no |
| QCOM | -10.39 | -9.49 | held | no |
| Z | -8.55 | -10.65 | extended | no |
| ENOV | +8.52 | +17.20 | extended | no |
| VCEL | +7.50 | +13.85 | extended | no |
| MXL | -7.25 | -22.06 | extended | no |
| EXPE | -7.25 | -13.74 | extended | no |
| SNDK | -6.32 | -22.26 | extended | no |
| AEHR | -6.31 | -19.20 | extended | no |
| OUST | -6.05 | -9.00 | extended | yes |
| AXTI | -5.97 | -22.76 | extended | no |
| SMTC | -5.79 | -17.50 | extended | no |
| ACCV | -5.73 | -15.00 | extended | no |
| VICR | -5.70 | -15.07 | extended | no |
| BE | -5.64 | -16.41 | extended | no |
| FORM | -5.62 | -15.81 | extended | no |
| PLPC | -5.58 | -11.63 | extended | no |
| EROC | -5.52 | -16.37 | extended | no |
| DELL | -5.33 | -14.96 | extended | no |
| CIEN | -5.21 | -15.22 | extended | no |
| ICHR | -5.07 | -16.85 | extended | no |
| LRCX | -4.90 | -16.36 | extended | no |
| PENG | -4.86 | -23.02 | extended | no |
| UCTT | -4.86 | -15.53 | extended | no |
| STX | -4.86 | -16.25 | extended | no |

73 further unchecked held-or-extended gap(s) are in the CSV.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

