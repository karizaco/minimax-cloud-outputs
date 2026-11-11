# Setup card — published 2026-10-28

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 13 stalk name(s), 8 Tier-A name(s); entry session 2026-10-29 · read-only

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
| Observation | `2026-10-28` | the settled close on the day the card was published |
| Entry | `2026-10-29` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 65.86 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 13 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AKAM | stalk | peoplewish | — | — | -1.50 | — | — | no morning row | MACD cross-up | none |
| AMKR | stalk | peoplewish | — | — | +5.68 | — | — | no morning row | gap-up ready | none |
| AMPX | stalk | peoplewish | — | — | +3.27 | — | — | no morning row | MACD cross-up | none |
| CHRN | stalk | stockbee | — | — | -2.69 | — | — | no morning row | MACD cross-up | none |
| CLS | stalk | peoplewish | — | — | +8.50 | — | — | no morning row | gap-up ready | none |
| FIGS | stalk | peoplewish|qullamaggie | — | — | +0.90 | — | — | no morning row | higher-low base | higher-low base |
| FLY | stalk | peoplewish | — | — | -0.23 | — | — | no morning row | MACD cross-up | none |
| NVDA | stalk | jeff_sun|stockbee | — | — | -1.17 | — | — | no morning row | higher-low base | none |
| ONDS | stalk | peoplewish|stockbee | — | — | +3.16 | — | — | no morning row | MACD cross-up | none |
| RUN | stalk | peoplewish | — | — | -1.46 | — | — | no morning row | higher-low base | none |
| TWLO | stalk | peoplewish | — | — | -0.34 | — | — | no morning row | higher-low base | none |
| ULCC | stalk | jeff_sun|stockbee | — | — | +11.57 | — | — | no morning row | MACD cross-up | none |
| WDC | stalk | jeff_sun|peoplewish | — | — | +4.08 | — | — | no morning row | MACD cross-up | none |
| DXC | tier-a | hernandez|peoplewish|qullamaggie | — | — | +1.58 | — | — | no morning row | — | none |
| IOVA | tier-a | hernandez|peoplewish|qullamaggie | — | — | +1.58 | — | — | no morning row | — | none |
| KNSA | tier-a | jeff_sun|qullamaggie|stockbee | — | — | +6.70 | — | — | no morning row | gap-up ready', 'MACD cross-up | none |
| NTSK | tier-a | hernandez|peoplewish|qullamaggie | — | — | +1.41 | — | — | no morning row | — | none |
| PRME | tier-a | hernandez|jeff_sun|stockbee | — | — | +23.22 | — | — | no morning row | — | none |
| QLYS | tier-a | hernandez|peoplewish|qullamaggie | — | — | -1.92 | — | — | no morning row | — | none |
| SOFI | tier-a | jeff_sun|qullamaggie|stockbee | — | — | +4.51 | — | — | no morning row | gap-up ready | none |
| TENB | tier-a | hernandez|peoplewish|qullamaggie | — | — | +0.14 | — | — | no morning row | — | none |

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

