# Sector flow — the 2026-10-23 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-23/master.csv` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 200 board rows across 19 sector(s), factset-like vocabulary · read-only

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
>    - No ETF tape found for this date in `us-stocks-in-play/`, so the board-versus-tape comparison is empty.
>    - 19 sector(s) carry no tape read: Finance, Technology Services, Health Technology, Commercial Services, Retail Trade, Consumer Non-Durables. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Finance | 37 | 18.5% | 10.0% | +8.50 | +3.25 | — | — |
| Technology Services | 36 | 18.0% | 22.0% | -4.00 | +4.50 | — | — |
| Health Technology | 29 | 14.5% | 18.0% | -3.50 | +1.70 | — | — |
| Commercial Services | 13 | 6.5% | 6.0% | +0.50 | +2.61 | — | — |
| Retail Trade | 13 | 6.5% | 3.0% | +3.50 | +7.53 | — | — |
| Consumer Non-Durables | 12 | 6.0% | 3.5% | +2.50 | +7.10 | — | — |
| Consumer Durables | 11 | 5.5% | 1.5% | +4.00 | +8.56 | — | — |
| Industrial Services | 8 | 4.0% | 3.0% | +1.00 | +0.76 | — | — |
| Consumer Services | 7 | 3.5% | 4.0% | -0.50 | +2.05 | — | — |
| Producer Manufacturing | 7 | 3.5% | 4.0% | -0.50 | +4.27 | — | — |
| Process Industries | 6 | 3.0% | 2.0% | +1.00 | +8.45 | — | — |
| Transportation | 5 | 2.5% | 6.0% | -3.50 | +2.98 | — | — |
| Electronic Technology | 4 | 2.0% | 9.0% | -7.00 | +3.45 | — | — |
| Energy Minerals | 3 | 1.5% | 1.0% | +0.50 | +0.14 | — | — |
| Communications | 2 | 1.0% | 1.5% | -0.50 | +3.97 | — | — |
| Distribution Services | 2 | 1.0% | 2.0% | -1.00 | +6.37 | — | — |
| Health Services | 2 | 1.0% | 1.0% | +0.00 | +2.40 | — | — |
| Utilities | 2 | 1.0% | 2.0% | -1.00 | +0.62 | — | — |
| Miscellaneous | 1 | 0.5% | — | — | +2.30 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-10-22`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Finance | 10.0% | 18.5% | +8.50 |
| Electronic Technology | 9.0% | 2.0% | -7.00 |
| Technology Services | 22.0% | 18.0% | -4.00 |
| Consumer Durables | 1.5% | 5.5% | +4.00 |
| Health Technology | 18.0% | 14.5% | -3.50 |
| Retail Trade | 3.0% | 6.5% | +3.50 |
| Transportation | 6.0% | 2.5% | -3.50 |

A share can move because a sector gained names or because another sector lost
them — the board is capped, so the shares are not independent. Read a Δ as
"more of the board looked like this today", never as an inflow.

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
| Miscellaneous | — *(no single proxy)* |
| Process Industries | XLB |
| Producer Manufacturing | XLI |
| Retail Trade | XLY |
| Technology Services | IGV, XLK |
| Transportation | XLI |
| Utilities | XLU |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-10-23/master.csv` |
| Tape | `— none for this date` |
| Sector source | `daily-screens/2026-10-23/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `change_pct` (early schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

