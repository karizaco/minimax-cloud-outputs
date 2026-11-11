# Setup card — published 2026-10-29

**Source:** derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md` and `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-11 · **Covers:** 50 stalk name(s), 4 Tier-A name(s); entry session 2026-10-30 · read-only

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
| Observation | `2026-10-29` | the settled close on the day the card was published |
| Entry | `2026-10-30` | the next settled session. A setup cannot be entered on the observation close. |

A figure in the table below is stamped with the clock it belongs to.
Do not read an observation-session change as an entry.

## Regime the sweep recorded

| Flag | Value |
|---|---|
| `size_cut_pct` | 0 |
| `uncertainty` | False |
| `late_cycle` | False |
| breadth % (screen input) | 63.77 |

Copied from the sweep's own regime file. A true `uncertainty` flag is a
header on this card because the skill treats it as a condition on every
name below, not as a footnote.

## Published setups

Stalk first — that is the skill's setup tier — then Tier-A names that
were not also on Stalk. On this date Stalk has 50 name(s) and Tier-A has 4.

| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |
|---|---|---|---|---|---|---|---|---|---|---|
| AAL | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | compression, higher-low base | none |
| AAPL | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | compression, higher-low base | higher-low base |
| AI | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| ALM | stalk | peoplewish | — | — | — | — | — | no morning row | MACD cross-up | none |
| AMBA | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| AMN | stalk | qullamaggie | — | — | — | — | — | no morning row | compression | none |
| AMZN | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | higher-low base | none |
| ATLC | stalk | jeff_sun | — | — | — | — | — | no morning row | higher-low base | none |
| AVGO | stalk | jeff_sun | — | — | — | -2.49 | held | absent | compression, MACD cross-up | none |
| BP | stalk | jeff_sun | — | — | — | — | — | no morning row | compression, higher-low base | none |
| BRAI | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | gap-up ready | none |
| BROS | stalk | jeff_sun | — | — | — | — | — | no morning row | compression | none |
| BSP | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| CCC | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | compression, higher-low base | higher-low base |
| CORZ | stalk | peoplewish | — | — | — | -3.67 | held | absent | compression | none |
| CVE | stalk | jeff_sun | — | — | — | — | — | no morning row | higher-low base | none |
| ECVT | stalk | jeff_sun | — | — | — | — | — | no morning row | compression, MACD cross-up, higher-low base | higher-low base |
| EE | stalk | jeff_sun | — | — | — | — | — | no morning row | higher-low base | none |
| ELF | stalk | jeff_sun | — | — | — | — | — | no morning row | compression, higher-low base | higher-low base |
| F | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | higher-low base | none |
| FIGS | stalk, tier-a | jeff_sun|peoplewish|qullamaggie | — | — | — | — | — | no morning row | compression, higher-low base | none |
| FIS | stalk | jeff_sun | — | — | — | — | — | no morning row | compression | none |
| GLOB | stalk | qullamaggie | — | — | — | — | — | no morning row | compression | none |
| GLXY | stalk | peoplewish | — | — | — | -4.61 | extended | absent | compression, MACD cross-up | none |
| GOOGL | stalk | jeff_sun|stockbee | — | — | — | -11.30 | extended | absent | higher-low base | none |
| HIMS | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| HPK | stalk | jeff_sun | — | — | — | — | — | no morning row | compression | none |
| KSS | stalk | qullamaggie | — | — | — | — | — | no morning row | compression | none |
| KVYO | stalk | peoplewish|qullamaggie | — | — | — | — | — | no morning row | compression, higher-low base | none |
| LIFE | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| MAN | stalk | peoplewish | — | — | — | — | — | no morning row | MACD cross-up, higher-low base | none |
| MU | stalk | jeff_sun | — | — | — | -2.58 | extended | absent | compression | none |
| NESR | stalk | jeff_sun|peoplewish | — | — | — | — | — | no morning row | compression | none |
| NKTR | stalk | peoplewish | — | — | — | — | — | no morning row | higher-low base | higher-low base |
| NVDA | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | higher-low base | none |
| OBA | stalk | stockbee | — | — | — | — | — | no morning row | higher-low base | none |
| OKLO | stalk | peoplewish | — | — | — | — | — | no morning row | higher-low base | none |
| PCG | stalk | jeff_sun|stockbee | — | — | — | — | — | no morning row | compression, higher-low base | higher-low base |
| QBTS | stalk | peoplewish | — | — | — | — | — | no morning row | MACD cross-up | none |
| RBLX | stalk | qullamaggie | — | — | — | — | — | no morning row | compression | none |
| SEZL | stalk | jeff_sun|peoplewish | — | — | — | — | — | no morning row | compression | none |
| SPHR | stalk | peoplewish | — | — | — | — | — | no morning row | compression, higher-low base | higher-low base |
| TWLO | stalk | peoplewish | — | — | — | — | — | no morning row | higher-low base | none |
| UEC | stalk | peoplewish | — | — | — | -2.03 | held | absent | MACD cross-up | none |
| UPST | stalk | jeff_sun | — | — | — | — | — | no morning row | compression, higher-low base | none |
| VSTM | stalk | qullamaggie | — | — | — | — | — | no morning row | compression | none |
| WGS | stalk | peoplewish | — | — | — | — | — | no morning row | MACD cross-up | none |
| WIX | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| XMTR | stalk | peoplewish | — | — | — | — | — | no morning row | compression | none |
| ZETA | stalk | qullamaggie | — | — | — | — | — | no morning row | compression, higher-low base | none |
| GMAB | tier-a | peoplewish|qullamaggie | — | — | — | — | — | no morning row | — | none |
| PRME | tier-a | qullamaggie | — | — | — | — | — | no morning row | — | none |
| SDGR | tier-a | peoplewish|qullamaggie | — | — | — | -4.44 | held | absent | MACD cross-up | none |

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

