# Setup card — published 2026-11-06

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-09 · **Covers:** 2 stalk name(s), 8 Tier-A name(s); entry session not yet settled · read-only

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
| Screen | `2026-11-05` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-06` | the settled close on the day the card was published |
| Entry | `not yet settled` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | True |
| `late_cycle` | False |
| breadth % (screen input) | 57.26 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 2 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| EWTX | stalk | peoplewish|qullamaggie | 38.87 | 45.04 | +15.87 | — | — | no morning row | — | none |
| ROKU | stalk | jeff_sun|stockbee | 160.52 | 160.52 | +0.09 | — | — | no morning row | — | higher-low base |
| ACHC | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 37.00 | 37.00 | +6.35 | — | — | no morning row | — | none |
| APP | tier-a | jeff_sun|qullamaggie|stockbee | 356.10 | 391.22 | +9.86 | — | — | no morning row | — | none |
| FUN | tier-a | peoplewish|qullamaggie|stockbee | 9.24 | 10.00 | +8.23 | — | — | no morning row | — | none |
| MRNA | tier-a | hernandez|peoplewish|qullamaggie|stockbee | 254.19 | 254.19 | +5.27 | +2.29 | extended | not_looked_up | — | none |
| RUN | tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | 9.87 | 9.98 | +1.11 | — | — | no morning row | — | none |
| SEZL | tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | 155.00 | 149.43 | -3.59 | -2.91 | extended | not_looked_up | — | none |
| U | tier-a | peoplewish|qullamaggie|stockbee | 48.80 | 51.49 | +5.51 | +4.51 | extended | not_looked_up | — | gap-up ready |
| XERS | tier-a | hernandez|jeff_sun|qullamaggie|stockbee | 15.20 | 15.20 | +16.21 | — | — | no morning row | — | gap-up ready |

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
| ABNB | +14.32 | +11.67 | held | no |
| DIOD | +12.93 | +13.17 | held | no |
| CIFR | +11.53 | +17.93 | extended | no |
| FLY | +11.30 | +36.80 | extended | no |
| SITM | +11.28 | +17.44 | extended | no |
| LRCX | +10.96 | +8.23 | held | no |
| CRDO | +10.20 | +7.28 | held | no |
| ICHR | +9.70 | +10.47 | extended | no |
| APLD | +9.53 | +9.74 | held | no |
| PENG | +9.52 | +12.39 | extended | no |
| MRVL | +9.46 | +5.73 | held | no |
| UCTT | +9.46 | +10.56 | extended | no |
| COHR | +9.38 | +13.74 | extended | no |
| MXL | +9.33 | +10.99 | extended | no |
| LITE | +9.28 | +5.67 | held | no |
| ONTO | +8.99 | +11.08 | extended | no |
| AEHR | +8.87 | +8.97 | held | no |
| FORM | +8.75 | +13.04 | extended | no |
| AXTI | +8.74 | +5.88 | held | no |
| ALAB | +8.41 | +6.26 | held | no |
| VICR | +8.32 | +8.72 | extended | no |
| FPS | +8.18 | +6.81 | held | no |
| SEI | +8.09 | +14.26 | extended | no |
| IONQ | +8.02 | +23.16 | extended | no |
| WULF | +7.84 | +12.80 | extended | no |

99 further unchecked held-or-extended gap(s) are in the CSV.

A name in this table and not on the published board is a coverage hole,
not a setup the screen rejected. The scanner's budget stopped at the lookup.

