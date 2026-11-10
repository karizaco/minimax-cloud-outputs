# Setup card — published 2026-10-27

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-10 · **Covers:** 9 stalk name(s), 8 Tier-A name(s); entry session 2026-10-28 · read-only

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
| Observation | `2026-10-27` | the settled close on the day the card was published |
| Entry | `2026-10-28` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | — |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 9 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | stalk | jeff_sun|stockbee | 253.10 | 253.10 | +1.61 | — | — | no morning row | — | none |
| AVGO | stalk | jeff_sun|stockbee | 342.33 | 342.33 | +4.00 | — | — | no morning row | — | higher-low base |
| FSLR | stalk | jeff_sun|stockbee | 175.85 | 175.85 | +4.58 | — | — | no morning row | — | none |
| HII | stalk | hernandez|jeff_sun | 281.32 | 281.32 | +0.10 | — | — | no morning row | — | higher-low base |
| KRT | stalk | jeff_sun|stockbee | 54.47 | 54.47 | +0.22 | — | — | no morning row | — | higher-low base |
| NVDA | stalk | jeff_sun|stockbee | 217.94 | 217.94 | +0.90 | — | — | no morning row | — | higher-low base |
| PRTH | stalk | hernandez|stockbee | 7.83 | 7.83 | +0.13 | — | — | no morning row | — | higher-low base |
| SOFI | stalk | stockbee | 16.40 | 16.40 | +13.42 | — | — | no morning row | — | gap-up ready |
| UI | stalk | hernandez|jeff_sun | 599.53 | 599.53 | +2.53 | — | — | no morning row | — | higher-low base |
| CRML | tier-a | peoplewish|qullamaggie|stockbee | 8.13 | 8.13 | +27.43 | — | — | no morning row | — | gap-up ready |
| CYPH | tier-a | peoplewish|qullamaggie|stockbee | 3.13 | 3.13 | +10.78 | — | — | no morning row | — | none |
| GLXY | tier-a | jeff_sun|peoplewish|stockbee | 17.18 | 17.18 | +9.57 | — | — | no morning row | — | gap-up ready |
| HRI | tier-a | jeff_sun|peoplewish|stockbee | 156.06 | 156.06 | +22.76 | — | — | no morning row | — | gap-up ready |
| MXL | tier-a | jeff_sun|peoplewish|stockbee | 74.67 | 74.67 | +12.34 | — | — | no morning row | — | none |
| ON | tier-a | hernandez|jeff_sun|stockbee | 78.67 | 78.67 | +6.22 | — | — | no morning row | — | none |
| RDW | tier-a | jeff_sun|peoplewish|stockbee | 8.89 | 8.89 | +6.85 | — | — | no morning row | — | none |
| RKLB | tier-a | jeff_sun|peoplewish|stockbee | 58.31 | 58.31 | +8.34 | — | — | no morning row | — | none |

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

