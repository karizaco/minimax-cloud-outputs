# Sector flow — the 2026-10-22 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-22/master.csv` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 200 board rows across 19 sector(s), factset-like vocabulary · read-only

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
>    - The session-change column on this date is `change_pct`, chosen because it is early schema. The column name is not stable across dates.
>    - No previous board found, so there is no day-over-day delta.
>    - No ETF tape found for this date in `us-stocks-in-play/`, so the board-versus-tape comparison is empty.
>    - 19 sector(s) carry no tape read: Technology Services, Health Technology, Finance, Electronic Technology, Commercial Services, Transportation. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Technology Services | 44 | 22.0% | — | — | — | — | — |
| Health Technology | 36 | 18.0% | — | — | — | — | — |
| Finance | 20 | 10.0% | — | — | — | — | — |
| Electronic Technology | 18 | 9.0% | — | — | — | — | — |
| Commercial Services | 12 | 6.0% | — | — | — | — | — |
| Transportation | 12 | 6.0% | — | — | — | — | — |
| Consumer Services | 8 | 4.0% | — | — | — | — | — |
| Producer Manufacturing | 8 | 4.0% | — | — | — | — | — |
| Consumer Non-Durables | 7 | 3.5% | — | — | — | — | — |
| Industrial Services | 6 | 3.0% | — | — | — | — | — |
| Retail Trade | 6 | 3.0% | — | — | — | — | — |
| Distribution Services | 4 | 2.0% | — | — | — | — | — |
| Process Industries | 4 | 2.0% | — | — | — | — | — |
| Utilities | 4 | 2.0% | — | — | — | — | — |
| Communications | 3 | 1.5% | — | — | — | — | — |
| Consumer Durables | 3 | 1.5% | — | — | — | — | — |
| Energy Minerals | 2 | 1.0% | — | — | — | — | — |
| Health Services | 2 | 1.0% | — | — | — | — | — |
| Non-Energy Minerals | 1 | 0.5% | — | — | — | — | — |

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

No sector's board median and mapped ETF disagree by 2 pp or more on this
date, or no tape was available to compare against.

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
| Board | `daily-screens/2026-10-22/master.csv` |
| Tape | `— none for this date` |
| Sector source | `daily-screens/2026-10-22/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `change_pct` (early schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

