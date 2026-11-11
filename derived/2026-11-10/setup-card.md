# Setup card — published 2026-11-10

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 0 stalk name(s), 4 Tier-A name(s); entry session not yet settled · read-only

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
| Screen | `2026-11-09` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-10` | the settled close on the day the card was published |
| Entry | `not yet settled` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 62.03 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 0 name(s) and Tier-A has 4.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| FRVO | tier-a | peoplewish|qullamaggie|stockbee | 11.38 | 11.38 | +0.00 | — | — | no morning row | — | none |
| PRAX | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 332.97 | 337.59 | +1.39 | — | — | no morning row | — | none |
| QXO | tier-a | peoplewish|qullamaggie|stockbee | 13.78 | 13.73 | -0.36 | — | — | no morning row | — | none |
| WRBY | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 30.21 | 29.90 | -1.03 | — | — | no morning row | — | none |

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
| LIF | -6.66 | -6.75 | held | no |
| GEV | -6.19 | -3.89 | held | no |
| QUBT | -4.81 | -8.16 | extended | no |
| CAT | -3.79 | -2.39 | held | no |
| AXTI | -3.78 | -8.39 | extended | no |
| HYMC | -3.62 | -11.28 | extended | no |
| FLY | -3.62 | -2.51 | held | no |
| TTWO | +3.47 | +8.31 | extended | no |
| LEU | -3.45 | -6.33 | extended | no |
| COHR | -3.43 | -4.68 | extended | no |
| VRT | -3.41 | -3.13 | held | no |
| LITE | -3.06 | -1.78 | held | no |
| BE | -3.00 | -4.37 | extended | no |
| RGTI | -2.93 | -6.39 | extended | no |
| PPTA | -2.88 | -8.65 | extended | no |
| SMTC | -2.88 | -2.50 | held | no |
| ASTS | -2.82 | -8.67 | extended | no |
| LUNR | -2.74 | -1.91 | held | no |
| MXL | -2.72 | -3.72 | extended | no |
| FPS | -2.70 | -4.96 | extended | no |
| OKLO | -2.57 | -6.52 | extended | no |
| ONTO | +2.56 | +1.81 | held | no |
| EROC | -2.55 | -4.61 | extended | no |
| ONDS | -2.51 | -6.70 | extended | no |
| INTC | -2.48 | -2.09 | held | no |

16 further unchecked held-or-extended gap(s) are in the CSV.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

