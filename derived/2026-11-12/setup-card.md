# Setup card — published 2026-11-12

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-15 · **Covers:** 0 stalk name(s), 4 Tier-A name(s); entry session 2026-11-13 · read-only

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
| Screen | `2026-11-11` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-12` | the settled close on the day the card was published |
| Entry | `2026-11-13` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 53.07 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 0 name(s) and Tier-A has 4.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AXGN | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 58.63 | 55.40 | -5.51 | — | — | no morning row | — | none |
| CRWV | tier-a | peoplewish|qullamaggie|stockbee | 60.77 | 56.60 | -6.86 | -9.45 | held | not_looked_up | — | none |
| NBIS | tier-a | peoplewish|qullamaggie|stockbee | 154.69 | 128.64 | -16.84 | -9.11 | no_close | not_looked_up | — | none |
| SHAZ | tier-a | peoplewish|qullamaggie|stockbee | 26.42 | 24.29 | -8.06 | — | — | no morning row | — | within 2% of sma20 |

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
| CRWV | -9.45 | -6.86 | held | yes |
| YETI | -8.62 | -10.38 | extended | no |
| TWST | -8.23 | -6.85 | held | no |
| NVDA | -7.56 | -4.32 | held | no |
| SNDK | -6.00 | -4.11 | held | no |
| FPS | -5.98 | -9.77 | extended | no |
| AXTI | -5.98 | -7.30 | extended | no |
| AAOI | -5.96 | -5.39 | held | no |
| SMCI | -5.75 | -11.30 | extended | no |
| EQPT | -5.62 | -3.50 | held | no |
| ASST | -5.60 | -4.09 | held | no |
| PURR | -5.42 | -3.77 | held | no |
| BMNR | -5.15 | -4.05 | held | no |
| APLD | -5.08 | -5.36 | extended | no |
| GLXY | -4.82 | -4.95 | held | no |
| WULF | -4.42 | -2.40 | held | no |
| LITE | -4.24 | -3.61 | held | no |
| MANE | -4.20 | -13.55 | extended | no |
| WOLF | -4.19 | -3.94 | held | no |
| AEHR | -4.03 | -7.21 | extended | no |
| SECZ | -3.97 | -7.34 | extended | no |
| HIMS | -3.89 | -5.19 | extended | no |
| ACMR | -3.84 | -4.86 | extended | no |
| AMBQ | -3.83 | -3.47 | held | no |
| TTMI | -3.81 | -3.08 | held | no |

27 further unchecked held-or-extended gap(s) are in the CSV.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

