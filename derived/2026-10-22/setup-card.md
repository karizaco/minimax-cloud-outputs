# Setup card — published 2026-10-22

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-09 · **Covers:** 54 stalk name(s), 2 Tier-A name(s); entry session 2026-10-23 · read-only

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
| Observation | `2026-10-22` | the settled close on the day the card was published |
| Entry | `2026-10-23` | the next settled session. A setup cannot be entered on the observation close. |

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
were not also on Stalk. On this date Stalk has 54 name(s) and Tier-A has 2.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | stalk | — | 343.99 | 343.99 | — | — | — | no morning row | — | none |
| ABCL | stalk | — | 12.24 | 12.24 | — | — | — | no morning row | — | none |
| AIT | stalk | — | 338.89 | 338.89 | — | — | — | no morning row | — | none |
| ALMR | stalk | — | 31.45 | 31.45 | — | — | — | no morning row | — | none |
| AMBA | stalk | — | 66.00 | 66.00 | — | — | — | no morning row | — | none |
| AME | stalk | — | 250.28 | 250.28 | — | — | — | no morning row | — | none |
| ARX | stalk | — | 19.75 | 19.75 | — | — | — | no morning row | — | none |
| BMNR | stalk | — | 23.96 | 23.96 | — | — | — | no morning row | — | none |
| BRKR | stalk | — | 59.10 | 59.10 | — | — | — | no morning row | — | none |
| BWIN | stalk | — | 31.92 | 31.92 | — | — | — | no morning row | — | none |
| CEG | stalk | — | 270.74 | 270.74 | — | — | — | no morning row | — | none |
| CELH | stalk | — | 28.31 | 28.31 | — | — | — | no morning row | — | none |
| CLMT | stalk | — | 52.59 | 52.59 | — | — | — | no morning row | — | none |
| CWEN | stalk | — | 31.61 | 31.61 | — | — | — | no morning row | — | none |
| DDOG | stalk | — | 273.09 | 273.09 | — | — | — | no morning row | — | none |
| ECHO | stalk | — | 92.64 | 92.64 | — | — | — | no morning row | — | none |
| FROG | stalk | — | 96.30 | 96.30 | — | — | — | no morning row | — | none |
| FRPT | stalk | — | 62.58 | 62.58 | — | — | — | no morning row | — | none |
| FWDI | stalk | — | 7.55 | 7.55 | — | — | — | no morning row | — | none |
| GNRC | stalk | — | 203.14 | 203.14 | — | — | — | no morning row | — | none |
| GRAL | stalk | — | 132.60 | 132.60 | — | — | — | no morning row | — | none |
| GSAT | stalk | — | 83.42 | 83.42 | — | — | — | no morning row | — | none |
| HQ | stalk | — | 15.12 | 15.12 | — | — | — | no morning row | — | none |
| IHS | stalk | — | 8.43 | 8.43 | — | — | — | no morning row | — | none |
| INOD | stalk | — | 60.56 | 60.56 | — | — | — | no morning row | — | none |
| KOD | stalk | — | 87.72 | 87.72 | — | — | — | no morning row | — | none |
| KRSA | stalk | — | 32.54 | 32.54 | — | — | — | no morning row | — | none |
| LIME | stalk | — | 27.65 | 27.65 | — | — | — | no morning row | — | none |
| LOCO | stalk | — | 15.06 | 15.06 | — | — | — | no morning row | — | none |
| MDB | stalk | — | 390.75 | 390.75 | — | — | — | no morning row | — | none |
| MSFT | stalk | — | 532.95 | 532.95 | — | — | — | no morning row | — | none |
| MSTR | stalk | — | 153.48 | 153.48 | — | — | — | no morning row | — | none |
| NDSN | stalk | — | 331.54 | 331.54 | — | — | — | no morning row | — | none |
| NTNX | stalk | — | 70.11 | 70.11 | — | — | — | no morning row | — | none |
| OFG | stalk | — | 50.50 | 50.50 | — | — | — | no morning row | — | none |
| OKTA | stalk | — | 208.64 | 208.64 | — | — | — | no morning row | — | none |
| OZK | stalk | — | 48.09 | 48.09 | — | — | — | no morning row | — | none |
| PCVX | stalk | — | 63.23 | 63.23 | — | — | — | no morning row | — | none |
| PNFP | stalk | — | 98.21 | 98.21 | — | — | — | no morning row | — | none |
| PTLO | stalk | — | 4.32 | 4.32 | — | — | — | no morning row | — | none |
| RNW | stalk | — | 6.87 | 6.87 | — | — | — | no morning row | — | none |
| ROIV | stalk | — | 36.80 | 36.80 | — | — | — | no morning row | — | none |
| SBAC | stalk | — | 173.41 | 173.41 | — | — | — | no morning row | — | none |
| SBET | stalk | — | 8.35 | 8.35 | — | — | — | no morning row | — | none |
| STDN | stalk | — | 12.73 | 12.73 | — | — | — | no morning row | — | none |
| STNG | stalk | — | 83.02 | 83.02 | — | — | — | no morning row | — | none |
| STRC | stalk | — | 99.20 | 99.20 | — | — | — | no morning row | — | none |
| SYM | stalk | — | 41.73 | 41.73 | — | — | — | no morning row | — | none |
| TNK | stalk | — | 95.99 | 95.99 | — | — | — | no morning row | — | none |
| TRNS | stalk | — | 86.31 | 86.31 | — | — | — | no morning row | — | none |
| TWST | stalk | — | 149.13 | 149.13 | — | — | — | no morning row | — | none |
| TXNM | stalk | — | 58.49 | 58.49 | — | — | — | no morning row | — | none |
| WFRD | stalk | — | 85.49 | 85.49 | — | — | — | no morning row | — | none |
| XXI | stalk | — | 5.89 | 5.89 | — | — | — | no morning row | — | none |
| LIFE | tier-a | — | 44.22 | 44.22 | — | — | — | no morning row | — | none |
| RCEL | tier-a | — | 15.29 | 15.29 | — | — | — | no morning row | — | none |

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

