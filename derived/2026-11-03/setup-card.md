# Setup card — published 2026-11-03

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-09 · **Covers:** 48 stalk name(s), 8 Tier-A name(s); entry session 2026-11-04 · read-only

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
| Screen | `2026-11-02` | the metrics the 18:30 sweep computed (`_results.json`) |
| Observation | `2026-11-03` | the settled close on the day the card was published |
| Entry | `2026-11-04` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 65.19 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 48 name(s) and Tier-A has 8.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| ACHR | stalk | stockbee|peoplewish | — | — | -0.96 | — | — | no morning row | — | none |
| AGNC | stalk | stockbee | — | — | -1.84 | — | — | no morning row | — | none |
| ALGM | stalk | peoplewish|jeff_sun | — | — | +4.70 | — | — | no morning row | — | none |
| APH | stalk | stockbee|jeff_sun | — | — | +5.45 | — | — | no morning row | — | none |
| BMY | stalk | stockbee | — | — | -2.08 | — | — | no morning row | — | higher-low base |
| BSX | stalk | stockbee | — | — | -1.85 | — | — | no morning row | — | none |
| COKE | stalk | stockbee|hernandez | — | — | -1.54 | — | — | no morning row | — | higher-low base |
| COMP | stalk | stockbee|jeff_sun | — | — | -1.06 | — | — | no morning row | — | none |
| COP | stalk | stockbee|hernandez | — | — | -1.66 | — | — | no morning row | — | none |
| CPNG | stalk | stockbee|jeff_sun | — | — | +3.61 | — | — | no morning row | — | none |
| CVX | stalk | stockbee|hernandez | — | — | -1.10 | — | — | no morning row | — | none |
| ECG | stalk | peoplewish|jeff_sun | — | — | +9.46 | — | — | no morning row | — | none |
| ENPH | stalk | stockbee|peoplewish | — | — | +8.92 | — | — | no morning row | — | none |
| EQX | stalk | stockbee|jeff_sun | — | — | -0.79 | — | — | no morning row | — | none |
| FICO | stalk | peoplewish|jeff_sun | — | — | +0.03 | — | — | no morning row | — | higher-low base |
| FIG | stalk | stockbee|peoplewish | — | — | -5.27 | — | — | no morning row | — | none |
| FIGS | stalk, tier-a | qullamaggie|peoplewish|hernandez | — | — | -2.21 | — | — | no morning row | — | none |
| FMC | stalk | stockbee|qullamaggie|peoplewish | — | — | -6.31 | — | — | no morning row | — | none |
| FUTU | stalk | stockbee|jeff_sun | — | — | -0.52 | — | — | no morning row | — | none |
| HTFL | stalk | qullamaggie|peoplewish|hernandez | — | — | -0.17 | — | — | no morning row | — | none |
| HWM | stalk | stockbee|jeff_sun | — | — | +4.76 | — | — | no morning row | — | none |
| INIO | stalk | peoplewish|jeff_sun | — | — | +11.58 | — | — | no morning row | — | none |
| IRON | stalk | peoplewish | — | — | +3.23 | — | — | no morning row | — | none |
| JBLU | stalk | stockbee|qullamaggie|peoplewish | — | — | +0.32 | — | — | no morning row | — | none |
| JOBY | stalk | stockbee|peoplewish | — | — | +0.83 | — | — | no morning row | — | none |
| KMI | stalk | stockbee | — | — | +0.49 | — | — | no morning row | — | none |
| KMT | stalk | stockbee|jeff_sun | — | — | -0.62 | — | — | no morning row | — | none |
| LADR | stalk | stockbee|jeff_sun | — | — | -1.83 | — | — | no morning row | — | none |
| LBTYA | stalk | stockbee|jeff_sun | — | — | +4.93 | — | — | no morning row | — | none |
| LUMN | stalk | stockbee|peoplewish | — | — | -1.66 | — | — | no morning row | — | none |
| NBBK | stalk | stockbee|jeff_sun | — | — | -1.02 | — | — | no morning row | — | none |
| NLY | stalk | stockbee | — | — | -1.41 | — | — | no morning row | — | none |
| NTSK | stalk | qullamaggie|peoplewish | — | — | -0.73 | — | — | no morning row | — | none |
| PG | stalk | stockbee | — | — | -0.92 | — | — | no morning row | — | higher-low base |
| PR | stalk | stockbee|hernandez | — | — | -2.28 | — | — | no morning row | — | none |
| PRME | stalk | qullamaggie | — | — | +2.48 | — | — | no morning row | — | none |
| QS | stalk | stockbee|peoplewish | — | — | +2.49 | — | — | no morning row | — | none |
| SDGR | stalk | qullamaggie|peoplewish | — | — | +3.78 | — | — | no morning row | — | none |
| SHLS | stalk | stockbee|jeff_sun | — | — | +11.45 | — | — | no morning row | — | gap-up ready |
| SKYD | stalk | stockbee|peoplewish | — | — | +0.12 | — | — | no morning row | — | none |
| TENB | stalk | qullamaggie|peoplewish | — | — | -0.89 | — | — | no morning row | — | none |
| TEVA | stalk | stockbee|jeff_sun | — | — | +2.97 | — | — | no morning row | — | none |
| TXN | stalk | stockbee|jeff_sun | — | — | +3.47 | — | — | no morning row | — | higher-low base |
| VSEC | stalk | stockbee|peoplewish|jeff_sun | — | — | +1.72 | — | — | no morning row | — | none |
| VZ | stalk | stockbee | — | — | +0.42 | — | — | no morning row | — | higher-low base |
| XMTR | stalk | peoplewish|jeff_sun | — | — | +16.55 | — | — | no morning row | — | none |
| XOM | stalk | stockbee | — | — | -1.23 | — | — | no morning row | — | none |
| XPEV | stalk | stockbee | — | — | +1.04 | — | — | no morning row | — | none |
| CAI | tier-a | qullamaggie|peoplewish|hernandez | — | — | +2.34 | — | — | no morning row | — | none |
| CLF | tier-a | stockbee|qullamaggie|peoplewish | — | — | -0.91 | — | — | no morning row | — | none |
| CVNA | tier-a | stockbee|qullamaggie|jeff_sun | — | — | -1.00 | — | — | no morning row | — | none |
| FTAI | tier-a | stockbee|qullamaggie|peoplewish | — | — | +1.51 | — | — | no morning row | — | none |
| KVYO | tier-a | stockbee|qullamaggie|peoplewish | — | — | -2.16 | — | — | no morning row | — | none |
| TEM | tier-a | stockbee|qullamaggie|peoplewish | — | — | -0.87 | — | — | no morning row | — | none |
| WING | tier-a | stockbee|qullamaggie|peoplewish | — | — | -0.90 | — | — | no morning row | — | none |

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

