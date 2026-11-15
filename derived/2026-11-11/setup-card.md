# Setup card — published 2026-11-11

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-15 · **Covers:** 0 stalk name(s), 4 Tier-A name(s); entry session 2026-11-12 · read-only

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
| Screen | `2026-11-10` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-11` | the settled close on the day the card was published |
| Entry | `2026-11-12` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 63.73 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 0 name(s) and Tier-A has 4.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAON | tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | 75.01 | 76.33 | +1.76 | +2.12 | held | not_looked_up | — | none |
| LQDA | tier-a | hernandez|jeff_sun|peoplewish|qullamaggie|stockbee | 55.21 | 55.21 | +7.41 | — | — | no morning row | — | none |
| QNT | tier-a | peoplewish|qullamaggie|stockbee | 43.00 | 40.57 | -5.65 | +2.33 | reversed | not_looked_up | — | none |
| ZETA | tier-a | jeff_sun|peoplewish|stockbee | 37.74 | 37.74 | +7.61 | — | — | no morning row | — | none |

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
| MRVL | +8.93 | +9.33 | extended | no |
| STX | +8.83 | +9.99 | extended | no |
| FPS | +8.01 | +14.34 | extended | no |
| EROC | +8.01 | +12.20 | extended | no |
| WDC | +8.00 | +8.33 | extended | no |
| SNDK | +7.88 | +13.69 | extended | no |
| FUN | +7.78 | +9.05 | extended | no |
| BE | +7.32 | +13.00 | extended | no |
| CORZ | +7.31 | +10.97 | extended | no |
| DELL | +7.30 | +11.75 | extended | no |
| TTMI | +7.16 | +8.96 | extended | no |
| AAOI | +6.73 | +15.60 | extended | no |
| GLW | +6.66 | +7.40 | extended | no |
| MU | +6.49 | +11.89 | extended | no |
| CLSK | +6.24 | +5.17 | held | no |
| KLAC | +6.15 | +5.23 | held | no |
| INTC | +5.98 | +7.47 | extended | no |
| LRCX | +5.76 | +6.07 | extended | no |
| ONDS | +5.57 | +2.87 | held | no |
| AMAT | +5.49 | +6.07 | extended | no |
| AMD | +5.48 | +7.32 | extended | no |
| ORCL | +5.15 | +8.81 | extended | no |
| INOD | +5.04 | +8.90 | extended | no |
| TDW | +4.93 | +6.66 | extended | no |
| ANET | +4.89 | +6.32 | extended | no |

40 further unchecked held-or-extended gap(s) are in the CSV.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

