# Sector flow — the 2026-11-05 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-05/master.csv` and `us-stocks-in-play/2026-11-05.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 19 sector(s), factset-like vocabulary · read-only

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
>    - 5 sector(s) carry no tape read: Producer Manufacturing, (unlabelled), Industrial Services, Commercial Services, Transportation. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Technology Services | 39 | 19.5% | 20.0% | -0.50 | -6.93 | -6.21 | — |
| Health Technology | 37 | 18.5% | 19.5% | -1.00 | -5.78 | -4.62 | — |
| Electronic Technology | 28 | 14.0% | 16.0% | -2.00 | -12.50 | -9.62 | -2.88 |
| Finance | 17 | 8.5% | 4.5% | +4.00 | -7.84 | -2.85 | -4.99 |
| Consumer Non-Durables | 12 | 6.0% | 1.0% | +5.00 | -2.80 | -0.75 | -2.05 |
| Producer Manufacturing | 10 | 5.0% | 5.0% | +0.00 | -9.54 | — | — |
| (unlabelled) | 9 | 4.5% | — | — | -10.69 | — | — |
| Non-Energy Minerals | 9 | 4.5% | 1.0% | +3.50 | -3.34 | -2.91 | — |
| Health Services | 6 | 3.0% | 4.0% | -1.00 | -2.04 | -2.50 | — |
| Industrial Services | 6 | 3.0% | 7.5% | -4.50 | -12.17 | — | — |
| Retail Trade | 5 | 2.5% | 2.5% | +0.00 | -4.63 | -3.83 | — |
| Consumer Durables | 4 | 2.0% | 2.5% | -0.50 | -2.61 | -3.83 | — |
| Consumer Services | 4 | 2.0% | 2.5% | -0.50 | -3.19 | -3.83 | — |
| Commercial Services | 3 | 1.5% | 4.5% | -3.00 | +0.00 | — | — |
| Transportation | 3 | 1.5% | 3.0% | -1.50 | -1.97 | — | — |
| Communications | 2 | 1.0% | 1.0% | +0.00 | -13.09 | -0.59 | -12.50 |
| Distribution Services | 2 | 1.0% | 0.5% | +0.50 | -1.95 | -3.83 | — |
| Energy Minerals | 2 | 1.0% | 1.5% | -0.50 | -6.62 | -2.90 | -3.72 |
| Utilities | 2 | 1.0% | 1.5% | -0.50 | -9.31 | -0.71 | -8.60 |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-11-04`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Consumer Non-Durables | 1.0% | 6.0% | +5.00 |
| Industrial Services | 7.5% | 3.0% | -4.50 |
| Finance | 4.5% | 8.5% | +4.00 |
| Non-Energy Minerals | 1.0% | 4.5% | +3.50 |
| Commercial Services | 4.5% | 1.5% | -3.00 |

A share can move because a sector gained names or because another sector lost
them — the board is capped, so the shares are not independent. Read a Δ as
"more of the board looked like this today", never as an inflow.

### Board versus tape

Sectors where the board's median name and the mapped ETF disagree by at least
2 pp. This is the column that distinguishes a sector tape from a
stock-picking one.

| Sector | Board median | Tape | Gap | Tape detail |
|---|---|---|---|---|
| Communications | -13.09 | -0.59 | -12.50 | XLC -0.59% |
| Utilities | -9.31 | -0.71 | -8.60 | XLU -0.71% |
| Finance | -7.84 | -2.85 | -4.99 | XLF -2.85% |
| Energy Minerals | -6.62 | -2.90 | -3.72 | XLE -2.90% |
| Electronic Technology | -12.50 | -9.62 | -2.88 | SMH -11.21%, XLK -8.04% |
| Consumer Non-Durables | -2.80 | -0.75 | -2.05 | XLP -0.75% |

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
| Non-Energy Minerals | XLB |
| Producer Manufacturing | XLI |
| Retail Trade | XLY |
| Technology Services | IGV, XLK |
| Transportation | XLI |
| Utilities | XLU |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-11-05/master.csv` |
| Tape | `us-stocks-in-play/2026-11-05.md` |
| Sector source | `daily-screens/2026-11-05/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

