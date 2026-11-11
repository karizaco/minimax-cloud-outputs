# Setup card — published 2026-10-30

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 48 stalk name(s), 10 Tier-A name(s); entry session 2026-11-02 · read-only

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
| Observation | `2026-10-30` | the settled close on the day the card was published |
| Entry | `2026-11-02` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 58.00 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 48 name(s) and Tier-A has 10.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAL | stalk | stockbee | — | — | -1.41 | — | — | no morning row | — | none |
| AAPL | stalk | stockbee | — | — | -1.23 | — | — | no morning row | — | none |
| ABCL | stalk | peoplewish|qullamaggie | — | — | -6.19 | — | — | no morning row | — | none |
| AI | stalk | peoplewish | — | — | -2.63 | — | — | no morning row | — | none |
| AMG | stalk | jeff_sun | — | — | -4.37 | — | — | no morning row | — | none |
| ARX | stalk | jeff_sun | — | — | +0.00 | — | — | no morning row | — | none |
| ARXS | stalk | peoplewish | — | — | -7.48 | — | — | no morning row | — | none |
| ASTH | stalk | jeff_sun | — | — | -0.25 | — | — | no morning row | — | none |
| ATLC | stalk | jeff_sun | — | — | -4.78 | — | — | no morning row | — | none |
| AUB | stalk | jeff_sun | — | — | -1.16 | — | — | no morning row | — | none |
| BFC | stalk | jeff_sun | — | — | -1.06 | — | — | no morning row | — | higher-low base |
| CNH | stalk | stockbee | — | — | +4.16 | — | — | no morning row | — | none |
| CRSP | stalk | peoplewish | — | — | -5.23 | — | — | no morning row | — | none |
| CVE | stalk | jeff_sun | — | — | +1.87 | — | — | no morning row | — | none |
| DMLP | stalk | jeff_sun | — | — | -2.10 | — | — | no morning row | — | none |
| DNA | stalk | qullamaggie | — | — | -12.01 | — | — | no morning row | — | none |
| ELF | stalk | jeff_sun | — | — | -1.12 | — | — | no morning row | — | none |
| ENTG | stalk | peoplewish | — | — | -3.51 | — | — | no morning row | — | none |
| EQBK | stalk | jeff_sun | — | — | -0.88 | — | — | no morning row | — | none |
| EXPD | stalk | jeff_sun | — | — | +0.23 | — | — | no morning row | — | higher-low base |
| F | stalk | stockbee | — | — | -0.89 | — | — | no morning row | — | higher-low base |
| FVRR | stalk | stockbee | — | — | -7.29 | — | — | no morning row | — | none |
| GCT | stalk | jeff_sun | — | — | -3.70 | — | — | no morning row | — | none |
| GTLB | stalk | qullamaggie | — | — | -4.52 | — | — | no morning row | — | none |
| HBT | stalk | jeff_sun | — | — | -0.76 | — | — | no morning row | — | higher-low base |
| HRMY | stalk | jeff_sun | — | — | +0.44 | — | — | no morning row | — | none |
| HUM | stalk | jeff_sun | — | — | -0.73 | — | — | no morning row | — | none |
| JPM | stalk | jeff_sun | — | — | -1.90 | — | — | no morning row | — | higher-low base |
| LB | stalk | jeff_sun | — | — | +0.92 | — | — | no morning row | — | none |
| LUMN | stalk | peoplewish | — | — | +1.88 | — | — | no morning row | — | none |
| MSFT | stalk | stockbee | — | — | -1.55 | — | — | no morning row | — | none |
| MUSA | stalk | jeff_sun | — | — | -0.94 | — | — | no morning row | — | none |
| NBBK | stalk | jeff_sun | — | — | -1.91 | — | — | no morning row | — | none |
| NESR | stalk | peoplewish | — | — | -0.56 | — | — | no morning row | — | none |
| NP | stalk | jeff_sun | — | — | +1.28 | — | — | no morning row | — | none |
| NTRS | stalk | jeff_sun | — | — | -2.17 | — | — | no morning row | — | higher-low base |
| OBA | stalk | stockbee | — | — | -0.10 | — | — | no morning row | — | none |
| QXO | stalk | peoplewish | — | — | -2.99 | — | — | no morning row | — | none |
| RBRK | stalk | peoplewish|qullamaggie | — | — | -7.09 | — | — | no morning row | — | none |
| RGEN | stalk | peoplewish | — | — | -6.20 | — | — | no morning row | — | none |
| RNG | stalk | peoplewish|qullamaggie | — | — | -2.72 | — | — | no morning row | — | none |
| RNST | stalk | jeff_sun | — | — | -0.82 | — | — | no morning row | — | none |
| RUN | stalk | peoplewish | — | — | -1.45 | — | — | no morning row | — | none |
| RXRX | stalk | peoplewish | — | — | -4.95 | — | — | no morning row | — | none |
| SKYD | stalk | peoplewish | — | — | +0.63 | — | — | no morning row | — | none |
| SPHR | stalk | peoplewish | — | — | -3.50 | — | — | no morning row | — | none |
| TWST | stalk | peoplewish|qullamaggie | — | — | -11.92 | — | — | no morning row | — | none |
| WIX | stalk | peoplewish | — | — | -1.27 | — | — | no morning row | — | none |
| CDNA | tier-a | jeff_sun|peoplewish|qullamaggie | — | — | +22.22 | — | — | no morning row | — | gap-up ready |
| FIGS | tier-a | jeff_sun|peoplewish|qullamaggie | — | — | -1.16 | — | — | no morning row | — | none |
| FTAI | tier-a | peoplewish|qullamaggie|stockbee | — | — | -4.46 | — | — | no morning row | — | none |
| GRAL | tier-a | hernandez|peoplewish|qullamaggie | — | — | -9.75 | — | — | no morning row | — | none |
| HTFL | tier-a | hernandez|peoplewish|qullamaggie | — | — | -2.45 | — | — | no morning row | — | none |
| IOVA | tier-a | hernandez|qullamaggie|stockbee | — | — | -11.30 | — | — | no morning row | — | none |
| KOD | tier-a | hernandez|peoplewish|qullamaggie | — | — | -1.22 | — | — | no morning row | — | none |
| MRNA | tier-a | hernandez|peoplewish|qullamaggie | — | — | -0.47 | — | — | no morning row | — | none |
| P | tier-a | jeff_sun|peoplewish|qullamaggie | — | — | -7.45 | — | — | no morning row | — | none |
| PURR | tier-a | peoplewish|qullamaggie|stockbee | — | — | -10.41 | — | — | no morning row | — | none |

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

