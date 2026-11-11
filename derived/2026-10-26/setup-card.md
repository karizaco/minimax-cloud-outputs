# Setup card — published 2026-10-26

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 13 stalk name(s), 8 Tier-A name(s); entry session 2026-10-27 · read-only

> **Read this before the table.**
>
> 1. **This is not a routine output.** The MiniMax agent keeps writing
>    `daily-screens/`, `earnings/` and `us-eod/`. This card only joins them.
> 2. **No direction and no size.** `held`, `faded` and `reversed` describe
>    a session path. They are not an instruction.
> 3. **The tradeable moment is the next open after this card's date,**
>    not the close the screen describes. See the session clock.
> 4. **Degraded paths.**
>    - Morning-gap join for this date is unverified (prior-close match 3%). Gap paths below are provisional.

## Session clock

| Clock | Session | What the numbers on that clock describe |
|---|---|---|
| Screen | `—` | the metrics the 18:30 sweep computed (`not recorded`) |
| Observation | `2026-10-26` | the settled close on the day the card was published |
| Entry | `2026-10-27` | the next settled session. A setup cannot be entered on the observation close. |

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
were not also on Stalk. On this date Stalk has 13 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | stalk | hernandez|stockbee | 343.91 | 343.91 | -1.10 | — | — | no morning row | — | none |
| ADI | stalk, tier-a | hernandez|jeff_sun|stockbee | 407.93 | 407.93 | +4.31 | — | — | no morning row | — | none |
| CSCO | stalk, tier-a | hernandez|jeff_sun|stockbee | 110.24 | 110.24 | +3.51 | — | — | no morning row | — | none |
| HEI.A | stalk | hernandez|jeff_sun | 234.12 | 234.12 | +3.25 | — | — | no morning row | — | none |
| HII | stalk | hernandez|jeff_sun | 281.05 | 281.05 | +2.54 | — | — | no morning row | — | none |
| IHS | stalk | hernandez|jeff_sun | 8.45 | 8.45 | +0.12 | — | — | no morning row | — | none |
| KEY | stalk | jeff_sun|stockbee | 21.21 | 21.21 | +0.62 | — | — | no morning row | — | none |
| KRT | stalk | jeff_sun|stockbee | 54.35 | 54.35 | +2.55 | — | — | no morning row | — | none |
| MSFT | stalk | jeff_sun|stockbee | 532.60 | 532.60 | +1.54 | — | — | no morning row | — | none |
| NEOG | stalk | jeff_sun|peoplewish | 12.21 | 12.21 | +0.16 | — | — | no morning row | — | none |
| PLTR | stalk | jeff_sun|stockbee | 198.84 | 198.84 | +1.06 | — | — | no morning row | — | none |
| PRTH | stalk | hernandez|stockbee | 7.82 | 7.82 | +0.00 | — | — | no morning row | — | none |
| RTX | stalk | hernandez|jeff_sun | 197.48 | 197.48 | +3.39 | — | — | no morning row | — | none |
| HEI | tier-a | hernandez|jeff_sun|stockbee | 309.71 | 309.71 | +4.15 | — | — | no morning row | — | none |
| NXPI | tier-a | hernandez|jeff_sun|stockbee | 245.83 | 245.83 | +4.64 | — | — | no morning row | — | none |
| ORKA | tier-a | jeff_sun|peoplewish|stockbee | 90.33 | 90.33 | +12.70 | — | — | no morning row | — | none |
| P | tier-a | hernandez|jeff_sun|qullamaggie|stockbee | 131.33 | 131.33 | +6.49 | — | — | no morning row | — | none |
| RNG | tier-a | jeff_sun|peoplewish|qullamaggie | 86.31 | 86.31 | +3.50 | — | — | no morning row | — | none |
| TENB | tier-a | peoplewish|qullamaggie|stockbee | 48.21 | 48.21 | +8.12 | — | — | no morning row | — | none |

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

