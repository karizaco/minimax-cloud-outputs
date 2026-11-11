# Sector flow — the 2026-11-10 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-10/master.csv` and `us-stocks-in-play/2026-11-10.md` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 1356 board rows across 21 sector(s), factset-like vocabulary · read-only

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
>    - 3 sector(s) carry no tape read: Communications, (unlabelled), Miscellaneous. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Finance | 310 | 22.9% | 4.5% | +18.36 | -0.20 | +0.50 | — |
| Health Technology | 193 | 14.2% | 16.0% | -1.77 | -0.71 | +0.31 | — |
| Electronic Technology | 139 | 10.2% | 18.5% | -8.25 | -0.71 | -1.14 | — |
| Technology Services | 136 | 10.0% | 23.5% | -13.47 | -0.83 | -1.14 | — |
| Producer Manufacturing | 86 | 6.3% | 6.5% | -0.16 | -1.28 | -0.08 | — |
| Non-Energy Minerals | 64 | 4.7% | 4.0% | +0.72 | -4.84 | -0.17 | -4.67 |
| Consumer Services | 55 | 4.1% | 3.0% | +1.06 | +0.35 | +0.04 | — |
| Retail Trade | 52 | 3.8% | 5.5% | -1.67 | -0.61 | +0.04 | — |
| Industrial Services | 39 | 2.9% | 2.0% | +0.88 | -0.61 | -0.08 | — |
| Transportation | 37 | 2.7% | 1.5% | +1.23 | +0.60 | -0.08 | — |
| Utilities | 35 | 2.6% | 0.5% | +2.08 | +0.11 | -0.14 | — |
| Consumer Durables | 32 | 2.4% | — | — | -1.87 | +0.04 | — |
| Consumer Non-Durables | 31 | 2.3% | 5.0% | -2.71 | -0.09 | +0.17 | — |
| Energy Minerals | 30 | 2.2% | — | — | +0.82 | +0.46 | — |
| Commercial Services | 28 | 2.1% | 2.5% | -0.44 | +0.33 | -0.08 | — |
| Health Services | 24 | 1.8% | 2.5% | -0.73 | -0.24 | +0.31 | — |
| Process Industries | 19 | 1.4% | 1.0% | +0.40 | -0.79 | -0.17 | — |
| Communications | 17 | 1.2% | 1.0% | +0.25 | +0.54 | — | — |
| Distribution Services | 14 | 1.0% | 1.0% | +0.03 | +0.22 | +0.04 | — |
| (unlabelled) | 9 | 0.7% | 1.5% | -0.84 | — | — | — |
| Miscellaneous | 6 | 0.4% | — | — | +0.73 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-11-06`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Finance | 4.5% | 22.9% | +18.36 |
| Technology Services | 23.5% | 10.0% | -13.47 |
| Electronic Technology | 18.5% | 10.2% | -8.25 |

A share can move because a sector gained names or because another sector lost
them — the board is capped, so the shares are not independent. Read a Δ as
"more of the board looked like this today", never as an inflow.

### Board versus tape

Sectors where the board's median name and the mapped ETF disagree by at least
2 pp. This is the column that distinguishes a sector tape from a
stock-picking one.

| Sector | Board median | Tape | Gap | Tape detail |
|---|---|---|---|---|
| Non-Energy Minerals | -4.84 | -0.17 | -4.67 | XLB -0.17% |

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
| Board | `daily-screens/2026-11-10/master.csv` |
| Tape | `us-stocks-in-play/2026-11-10.md` |
| Sector source | `daily-screens/2026-11-10/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 1356 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

