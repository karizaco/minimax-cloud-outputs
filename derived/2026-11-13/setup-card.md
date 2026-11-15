# Setup card — published 2026-11-13

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-15 · **Covers:** 0 stalk name(s), 5 Tier-A name(s); entry session not yet settled · read-only

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
| Screen | `2026-11-12` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-13` | the settled close on the day the card was published |
| Entry | `not yet settled` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 52.82 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 0 name(s) and Tier-A has 5.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | tier-a | peoplewish|qullamaggie|stockbee | 585.30 | 534.06 | -8.75 | -2.78 | extended | not_looked_up | — | none |
| CHA | tier-a | hernandez|jeff_sun|stockbee | 13.51 | 14.37 | +6.37 | — | — | no morning row | — | none |
| DPC | tier-a | peoplewish|qullamaggie|stockbee | 34.33 | 34.26 | -0.20 | — | — | no morning row | — | none |
| IRTC | tier-a | peoplewish|qullamaggie|stockbee | 93.56 | 91.91 | -1.76 | — | — | no morning row | — | none |
| LUNR | tier-a | peoplewish|qullamaggie|stockbee | 13.03 | 13.00 | -0.23 | — | — | no morning row | — | none |

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
| CSCO | -3.62 | -6.24 | extended | no |
| AMD | -2.78 | -8.75 | extended | yes |
| AEHR | -2.52 | -6.65 | extended | no |
| MSTR | -2.41 | -2.45 | held | no |
| VOYG | -2.30 | -2.73 | extended | no |
| AVGO | -2.27 | -4.78 | extended | no |
| GLXY | -2.04 | -5.27 | extended | no |

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

