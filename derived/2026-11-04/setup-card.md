# Setup card — published 2026-11-04

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 17 stalk name(s), 8 Tier-A name(s); entry session 2026-11-05 · read-only

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
| Screen | `—` | the metrics the 18:30 sweep computed (`not recorded`) |
| Observation | `2026-11-04` | the settled close on the day the card was published |
| Entry | `2026-11-05` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | — |
| `uncertainty` | None |
| `late_cycle` | None |
| breadth % (screen input) | — |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 17 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | stalk | jeff_sun|stockbee | 349.51 | 349.51 | +5.31 | — | — | no morning row | — | none |
| ALHC | stalk | peoplewish | 7.39 | 8.14 | +10.15 | +2.58 | extended | absent | — | none |
| BB | stalk | jeff_sun|peoplewish | 8.19 | 8.76 | +6.96 | — | — | no morning row | — | none |
| BSP | stalk | jeff_sun|peoplewish | 46.58 | 46.58 | +6.47 | — | — | no morning row | — | none |
| CAI | stalk | peoplewish|qullamaggie | 32.85 | 33.22 | +1.13 | — | — | no morning row | — | none |
| FN | stalk | peoplewish|stockbee | 363.33 | 341.64 | -5.97 | -2.29 | no_close | absent | — | none |
| GRAL | stalk | peoplewish|qullamaggie | 139.44 | 143.66 | +3.03 | — | — | no morning row | — | none |
| HL | stalk | stockbee | 13.21 | 14.95 | +13.17 | — | — | no morning row | — | gap-up ready |
| HTFL | stalk | peoplewish|qullamaggie | 54.40 | 56.57 | +3.99 | — | — | no morning row | — | none |
| LSCC | stalk, tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | 105.92 | 107.25 | +1.26 | — | — | no morning row | — | none |
| MARA | stalk | peoplewish|stockbee | 7.16 | 6.87 | -4.05 | -5.59 | held | absent | — | none |
| ODTX | stalk | stockbee | 21.57 | 19.50 | -9.60 | — | — | no morning row | — | none |
| OPEN | stalk | peoplewish | 1.74 | 1.98 | +13.79 | — | — | no morning row | — | gap-up ready |
| SNAP | stalk | jeff_sun|peoplewish|stockbee | 5.92 | 5.92 | +5.90 | — | — | no morning row | — | none |
| TMO | stalk | hernandez|stockbee | 698.34 | 706.16 | +1.12 | — | — | no morning row | — | higher-low base |
| VSAT | stalk | peoplewish | 75.24 | 66.79 | -11.23 | — | — | no morning row | — | none |
| VSTM | stalk | peoplewish|qullamaggie | 9.77 | 9.85 | +0.82 | — | — | no morning row | — | none |
| CDNA | tier-a | jeff_sun|peoplewish|qullamaggie | 88.47 | 85.86 | -2.95 | — | — | no morning row | — | none |
| FISV | tier-a | hernandez|jeff_sun|stockbee | 62.05 | 62.05 | +6.25 | — | — | no morning row | — | none |
| FTAI | tier-a | jeff_sun|peoplewish|qullamaggie | 200.74 | 179.58 | -10.54 | — | — | no morning row | — | none |
| GKOS | tier-a | hernandez|peoplewish|qullamaggie | 233.04 | 246.70 | +5.86 | — | — | no morning row | — | none |
| GPK | tier-a | jeff_sun|qullamaggie|stockbee | 11.75 | 11.75 | +3.89 | — | — | no morning row | — | none |
| KVYO | tier-a | jeff_sun|peoplewish|qullamaggie | 21.36 | 21.36 | +0.14 | — | — | no morning row | — | none |
| MRNA | tier-a | hernandez|peoplewish|qullamaggie | 228.44 | 258.38 | +13.11 | +2.75 | extended | absent | — | none |

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

