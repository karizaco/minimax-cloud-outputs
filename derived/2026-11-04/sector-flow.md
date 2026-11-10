# Sector flow — the 2026-11-04 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-04/master.csv` and `us-stocks-in-play/2026-11-04.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 20 sector(s), factset-like vocabulary · read-only

> **Read this before the table.**
> 
> 1. **This counts the board, it does not weight the market.** A sector's share
>    is its share of the names the screen published, not of any index. A sector
>    with 40% of the board is where the screen found candidates — that is a
>    statement about the screen's output, not about market capitalisation.
> 2. **The vocabulary on this date is `factset-like`.** The boards use a FactSet-style
>    taxonomy on most dates, and GICS wherever the board carries a `gics_sector`
>    column or the sector had to be recovered from `us-eod/`. The two are never
>    blended and a delta across them is never computed.
> 3. **The ETF column is a mapping, not a fact.** Which ETF reads a sector is a
>    judgement, published in full under *The sector-to-ETF mapping* below.
> 4. **Deviations and degraded paths.**
>    - No day-over-day delta: the previous board (`daily-screens/2026-11-03/master.csv`) labels sectors with the **gics** vocabulary and this one uses **factset-like**. Two taxonomies are not comparable, so the delta column is left empty rather than mapped across.
>    - 9 sector(s) carry no tape read: Technology Services, Industrial Services, Producer Manufacturing, Commercial Services, Transportation, Process Industries. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Technology Services | 40 | 20.0% | — | — | +1.36 | — | — |
| Health Technology | 39 | 19.5% | — | — | +6.56 | +3.23 | +3.33 |
| Electronic Technology | 32 | 16.0% | — | — | -7.12 | -3.31 | -3.81 |
| Industrial Services | 15 | 7.5% | — | — | -11.65 | — | — |
| Producer Manufacturing | 10 | 5.0% | — | — | -11.89 | — | — |
| Commercial Services | 9 | 4.5% | — | — | +2.89 | — | — |
| Finance | 9 | 4.5% | — | — | +9.62 | +3.38 | +6.24 |
| Health Services | 8 | 4.0% | — | — | +10.62 | +3.23 | +7.39 |
| Transportation | 6 | 3.0% | — | — | +10.72 | — | — |
| Consumer Durables | 5 | 2.5% | — | — | +12.39 | +4.39 | +8.00 |
| Consumer Services | 5 | 2.5% | — | — | +9.83 | +4.39 | +5.44 |
| Retail Trade | 5 | 2.5% | — | — | +11.00 | +4.39 | +6.61 |
| Energy Minerals | 3 | 1.5% | — | — | -6.67 | -4.96 | — |
| Process Industries | 3 | 1.5% | — | — | +10.66 | — | — |
| Utilities | 3 | 1.5% | — | — | -8.54 | — | — |
| Communications | 2 | 1.0% | — | — | +11.62 | +3.65 | +7.97 |
| Consumer Non-Durables | 2 | 1.0% | — | — | +7.53 | +3.76 | +3.77 |
| Non-Energy Minerals | 2 | 1.0% | — | — | +13.74 | — | — |
| Distribution Services | 1 | 0.5% | — | — | +48.74 | +4.39 | +44.35 |
| Miscellaneous | 1 | 0.5% | — | — | -13.36 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Board versus tape

Sectors where the board's median name and the mapped ETF disagree by at least
2 pp. This is the column that distinguishes a sector tape from a
stock-picking one.

| Sector | Board median | Tape | Gap | Tape detail |
|---|---|---|---|---|
| Distribution Services | +48.74 | +4.39 | +44.35 | XLY +4.39% |
| Consumer Durables | +12.39 | +4.39 | +8.00 | XLY +4.39% |
| Communications | +11.62 | +3.65 | +7.97 | XLC +3.65% |
| Health Services | +10.62 | +3.23 | +7.39 | XLV +3.23% |
| Retail Trade | +11.00 | +4.39 | +6.61 | XLY +4.39% |
| Finance | +9.62 | +3.38 | +6.24 | XLF +3.38% |
| Consumer Services | +9.83 | +4.39 | +5.44 | XLY +4.39% |
| Electronic Technology | -7.12 | -3.31 | -3.81 | SMH -3.31% |
| Consumer Non-Durables | +7.53 | +3.76 | +3.77 | XLP +3.76% |
| Health Technology | +6.56 | +3.23 | +3.33 | XLV +3.23% |

A **positive gap** means the board's names outran their sector ETF: the screen
found movers the sector as a whole did not have, which is a stock-picking
read. A **negative gap** means the ETF outran the board's names, so the
sector moved without the screen's candidates leading it. Neither is good or
bad; the gap is a description of where the move lived.

## The sector-to-ETF mapping

Published in full because it is a judgement this artifact makes, not a fact it
reads. A sector mapped to two ETFs takes their median.

| Sector | ETF(s) |
|---|---|
| Commercial Services | XLI |
| Communications | XLC |
| Consumer Durables | XLY |
| Consumer Non-Durables | XLP |
| Consumer Services | XLY |
| Distribution Services | XLY |
| Electronic Technology | SMH, XLK |
| Energy Minerals | XLE |
| Finance | XLF |
| Health Services | XLV |
| Health Technology | XBI, XLV |
| Industrial Services | XLI |
| Miscellaneous | — *(no single proxy)* |
| Non-Energy Minerals | XLB |
| Process Industries | XLB |
| Producer Manufacturing | XLI |
| Retail Trade | XLY |
| Technology Services | IGV, XLK |
| Transportation | XLI |
| Utilities | XLU |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-11-04/master.csv` |
| Tape | `us-stocks-in-play/2026-11-04.md` |
| Sector source | `daily-screens/2026-11-04/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

