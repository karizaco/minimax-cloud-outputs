# Sector flow — the 2026-11-06 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-06/master.csv` and `us-stocks-in-play/2026-11-06.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 18 sector(s), factset-like vocabulary · read-only

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
>    - 5 sector(s) carry no tape read: Producer Manufacturing, Commercial Services, Industrial Services, (unlabelled), Transportation. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Technology Services | 47 | 23.5% | 19.5% | +4.00 | +3.46 | +0.66 | +2.80 |
| Electronic Technology | 37 | 18.5% | 14.0% | +4.50 | +6.26 | +2.54 | +3.72 |
| Health Technology | 32 | 16.0% | 18.5% | -2.50 | +2.79 | +1.25 | — |
| Producer Manufacturing | 13 | 6.5% | 5.0% | +1.50 | +6.97 | — | — |
| Retail Trade | 11 | 5.5% | 2.5% | +3.00 | -1.63 | -0.05 | — |
| Consumer Non-Durables | 10 | 5.0% | 6.0% | -1.00 | +0.17 | -1.28 | — |
| Finance | 9 | 4.5% | 8.5% | -4.00 | +1.62 | -0.59 | +2.21 |
| Non-Energy Minerals | 8 | 4.0% | 4.5% | -0.50 | +1.79 | -0.73 | +2.52 |
| Consumer Services | 6 | 3.0% | 2.0% | +1.00 | +2.96 | -0.05 | +3.01 |
| Commercial Services | 5 | 2.5% | 1.5% | +1.00 | +0.22 | — | — |
| Health Services | 5 | 2.5% | 3.0% | -0.50 | +6.35 | -0.06 | +6.41 |
| Industrial Services | 4 | 2.0% | 3.0% | -1.00 | +5.14 | — | — |
| (unlabelled) | 3 | 1.5% | 4.5% | -3.00 | — | — | — |
| Transportation | 3 | 1.5% | 1.5% | +0.00 | -0.14 | — | — |
| Communications | 2 | 1.0% | 1.0% | +0.00 | +3.65 | +0.43 | +3.22 |
| Distribution Services | 2 | 1.0% | 1.0% | +0.00 | -4.03 | -0.05 | -3.98 |
| Process Industries | 2 | 1.0% | — | — | -5.14 | -0.73 | -4.41 |
| Utilities | 1 | 0.5% | 1.0% | -0.50 | +15.85 | -0.39 | +16.24 |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-11-05`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Electronic Technology | 14.0% | 18.5% | +4.50 |
| Technology Services | 19.5% | 23.5% | +4.00 |
| Finance | 8.5% | 4.5% | -4.00 |
| Retail Trade | 2.5% | 5.5% | +3.00 |
| (unlabelled) | 4.5% | 1.5% | -3.00 |

A share can move because a sector gained names or because another sector lost
them — the board is capped, so the shares are not independent. Read a Δ as
"more of the board looked like this today", never as an inflow.

### Board versus tape

Sectors where the board's median name and the mapped ETF disagree by at least
2 pp. This is the column that distinguishes a sector tape from a
stock-picking one.

| Sector | Board median | Tape | Gap | Tape detail |
|---|---|---|---|---|
| Utilities | +15.85 | -0.39 | +16.24 | XLU -0.39% |
| Health Services | +6.35 | -0.06 | +6.41 | XLV -0.06% |
| Process Industries | -5.14 | -0.73 | -4.41 | XLB -0.73% |
| Distribution Services | -4.03 | -0.05 | -3.98 | XLY -0.05% |
| Electronic Technology | +6.26 | +2.54 | +3.72 | SMH +3.62%, XLK +1.45% |
| Communications | +3.65 | +0.43 | +3.22 | XLC +0.43% |
| Consumer Services | +2.96 | -0.05 | +3.01 | XLY -0.05% |
| Technology Services | +3.46 | +0.66 | +2.80 | IGV -0.13%, XLK +1.45% |
| Non-Energy Minerals | +1.79 | -0.73 | +2.52 | XLB -0.73% |
| Finance | +1.62 | -0.59 | +2.21 | XLF -0.59% |

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
| Consumer Non-Durables | XLP |
| Consumer Services | XLY |
| Distribution Services | XLY |
| Electronic Technology | SMH, XLK |
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
| Board | `daily-screens/2026-11-06/master.csv` |
| Tape | `us-stocks-in-play/2026-11-06.md` |
| Sector source | `daily-screens/2026-11-06/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

