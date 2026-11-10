# Setup card — published 2026-11-02

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-10 · **Covers:** 59 stalk name(s), 11 Tier-A name(s); entry session 2026-11-03 · read-only

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
| Observation | `2026-11-02` | the settled close on the day the card was published |
| Entry | `2026-11-03` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 63.89 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 59 name(s) and Tier-A has 11.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAL | stalk | stockbee | — | — | +3.81 | — | — | no morning row | — | none |
| AAPL | stalk | stockbee | — | — | -1.83 | — | — | no morning row | — | none |
| ABCL | stalk, tier-a | hernandez|peoplewish|qullamaggie | — | — | -9.37 | — | — | no morning row | — | none |
| ADPT | stalk | peoplewish | — | — | -5.93 | — | — | no morning row | — | none |
| AI | stalk | peoplewish | — | — | -2.53 | — | — | no morning row | — | none |
| AMN | stalk | qullamaggie | — | — | -2.84 | — | — | no morning row | — | none |
| ARQT | stalk | qullamaggie | — | — | -2.53 | — | — | no morning row | — | none |
| BAC | stalk | stockbee | — | — | -0.88 | — | — | no morning row | — | none |
| BLLN | stalk | peoplewish | — | — | -2.57 | — | — | no morning row | — | none |
| BSP | stalk | peoplewish | — | — | -0.31 | — | — | no morning row | — | none |
| CAI | stalk, tier-a | hernandez|peoplewish|qullamaggie | — | — | -6.50 | — | — | no morning row | — | none |
| CRL | stalk | qullamaggie | — | — | -5.81 | — | — | no morning row | — | none |
| CSGP | stalk | stockbee | — | — | +5.47 | — | — | no morning row | — | none |
| CVI | stalk, tier-a | hernandez|jeff_sun|qullamaggie | — | — | -4.20 | — | — | no morning row | — | none |
| CVLG | stalk | stockbee | — | — | +8.25 | — | — | no morning row | — | none |
| CZR | stalk | jeff_sun|stockbee | — | — | -0.34 | — | — | no morning row | — | higher-low base |
| EQPT | stalk | peoplewish | — | — | -6.64 | — | — | no morning row | — | none |
| F | stalk | jeff_sun|stockbee | — | — | +2.86 | — | — | no morning row | — | none |
| FIVN | stalk | peoplewish | — | — | -1.57 | — | — | no morning row | — | none |
| GH | stalk | peoplewish | — | — | -4.51 | — | — | no morning row | — | none |
| GRAL | stalk | peoplewish|qullamaggie | — | — | -6.74 | +3.21 | reversed | absent | — | none |
| GTLB | stalk | qullamaggie | — | — | -3.66 | — | — | no morning row | — | none |
| HTFL | stalk, tier-a | hernandez|peoplewish|qullamaggie | — | — | -7.72 | — | — | no morning row | — | none |
| IDT | stalk | jeff_sun|stockbee | — | — | +0.30 | — | — | no morning row | — | none |
| IRON | stalk | peoplewish|qullamaggie | — | — | -2.75 | — | — | no morning row | — | none |
| KSS | stalk | peoplewish|qullamaggie | — | — | -0.66 | — | — | no morning row | — | higher-low base |
| KVUE | stalk | stockbee | — | — | — | — | — | no morning row | — | none |
| KVYO | stalk | peoplewish | — | — | +8.24 | — | — | no morning row | — | none |
| LIFE | stalk | peoplewish | — | — | -1.77 | — | — | no morning row | — | none |
| LU | stalk | stockbee | — | — | +0.97 | — | — | no morning row | — | none |
| MANE | stalk | peoplewish | — | — | -7.27 | — | — | no morning row | — | none |
| MPC | stalk | hernandez|jeff_sun | — | — | -3.22 | — | — | no morning row | — | none |
| MSFT | stalk | stockbee | — | — | -2.83 | — | — | no morning row | — | none |
| NESR | stalk | peoplewish | — | — | -1.60 | — | — | no morning row | — | none |
| NRIX | stalk | peoplewish | — | — | -4.10 | — | — | no morning row | — | none |
| NTRA | stalk | qullamaggie | — | — | -8.54 | — | — | no morning row | — | none |
| NTSK | stalk | peoplewish|qullamaggie | — | — | -9.47 | +3.29 | reversed | absent | — | none |
| PGEN | stalk | stockbee | — | — | -25.94 | -30.55 | held | absent | — | none |
| PSX | stalk | hernandez|jeff_sun | — | — | -2.75 | — | — | no morning row | — | none |
| QLYS | stalk, tier-a | jeff_sun|peoplewish|qullamaggie | — | — | -7.37 | — | — | no morning row | — | none |
| QXO | stalk | peoplewish | — | — | +5.80 | — | — | no morning row | — | none |
| RBRK | stalk | peoplewish|qullamaggie | — | — | -7.64 | — | — | no morning row | — | none |
| RGEN | stalk | peoplewish | — | — | -2.26 | — | — | no morning row | — | none |
| RNG | stalk | peoplewish | — | — | -4.52 | — | — | no morning row | — | none |
| RPD | stalk | qullamaggie | — | — | -10.30 | — | — | no morning row | — | none |
| RXRX | stalk | peoplewish | — | — | -4.96 | — | — | no morning row | — | none |
| SAIL | stalk | peoplewish | — | — | -8.88 | — | — | no morning row | — | none |
| SDGR | stalk | peoplewish|qullamaggie | — | — | -3.50 | — | — | no morning row | — | none |
| SPHR | stalk | peoplewish | — | — | -3.80 | — | — | no morning row | — | none |
| SYRE | stalk | peoplewish | — | — | -1.09 | — | — | no morning row | — | none |
| TEM | stalk | peoplewish|qullamaggie | — | — | +8.67 | +3.85 | extended | absent | — | none |
| THRM | stalk | peoplewish | — | — | +1.39 | — | — | no morning row | — | none |
| TMUS | stalk | stockbee | — | — | +2.37 | -2.29 | reversed | absent | — | none |
| TTAN | stalk | qullamaggie|stockbee | — | — | -1.60 | — | — | no morning row | — | none |
| TWST | stalk | peoplewish|qullamaggie | — | — | -15.54 | — | — | no morning row | — | none |
| VCYT | stalk | peoplewish | — | — | -2.02 | — | — | no morning row | — | none |
| VSTM | stalk | qullamaggie | — | — | -1.64 | — | — | no morning row | — | none |
| WIX | stalk | peoplewish | — | — | -2.75 | — | — | no morning row | — | none |
| ZURA | stalk | stockbee | — | — | -2.48 | — | — | no morning row | — | none |
| CDNA | tier-a | peoplewish|qullamaggie|stockbee | — | — | -1.75 | — | — | no morning row | — | none |
| KOD | tier-a | hernandez|peoplewish|qullamaggie | — | — | -1.57 | — | — | no morning row | — | none |
| MRNA | tier-a | hernandez|peoplewish|qullamaggie | — | — | -0.40 | — | — | no morning row | — | none |
| MTZ | tier-a | jeff_sun|peoplewish|stockbee | — | — | +4.14 | — | — | no morning row | — | none |
| NOW | tier-a | jeff_sun|qullamaggie|stockbee | — | — | +0.85 | — | — | no morning row | — | none |
| PURR | tier-a | peoplewish|qullamaggie|stockbee | — | — | -11.81 | — | — | no morning row | — | none |

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

