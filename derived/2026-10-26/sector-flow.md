# Sector flow — the 2026-10-26 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-26/master.csv` and `us-stocks-in-play/2026-10-26.md` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 200 board rows across 18 sector(s), factset-like vocabulary · read-only

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
>    - The session-change column on this date is `change`, chosen because it is early schema. The column name is not stable across dates.
>    - 14 sector(s) carry no tape read: Health Technology, Finance, Industrial Services, Non-Energy Minerals, Producer Manufacturing, Energy Minerals. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Electronic Technology | 52 | 26.0% | 2.0% | +24.00 | +3.77 | +1.69 | +2.08 |
| Technology Services | 50 | 25.0% | 18.0% | +7.00 | +3.01 | +1.21 | — |
| Health Technology | 29 | 14.5% | 14.5% | +0.00 | +4.11 | — | — |
| Finance | 10 | 5.0% | 18.5% | -13.50 | +0.54 | — | — |
| Industrial Services | 8 | 4.0% | 4.0% | +0.00 | +4.40 | — | — |
| Non-Energy Minerals | 7 | 3.5% | — | — | +4.88 | — | — |
| Producer Manufacturing | 7 | 3.5% | 3.5% | +0.00 | +3.72 | — | — |
| Energy Minerals | 6 | 3.0% | 1.5% | +1.50 | +6.22 | — | — |
| Transportation | 6 | 3.0% | 2.5% | +0.50 | +3.19 | — | — |
| Consumer Services | 4 | 2.0% | 3.5% | -1.50 | +3.04 | — | — |
| Process Industries | 4 | 2.0% | 3.0% | -1.00 | +3.39 | — | — |
| Retail Trade | 4 | 2.0% | 6.5% | -4.50 | +4.61 | — | — |
| Commercial Services | 3 | 1.5% | 6.5% | -5.00 | +4.36 | — | — |
| Communications | 3 | 1.5% | 1.0% | +0.50 | -0.85 | -1.57 | — |
| Consumer Durables | 2 | 1.0% | 5.5% | -4.50 | +5.05 | — | — |
| Distribution Services | 2 | 1.0% | 1.0% | +0.00 | +1.99 | — | — |
| Health Services | 2 | 1.0% | 1.0% | +0.00 | +28.36 | — | — |
| Consumer Non-Durables | 1 | 0.5% | 6.0% | -5.50 | +3.12 | -0.34 | +3.46 |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-10-23`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Electronic Technology | 2.0% | 26.0% | +24.00 |
| Finance | 18.5% | 5.0% | -13.50 |
| Technology Services | 18.0% | 25.0% | +7.00 |
| Consumer Non-Durables | 6.0% | 0.5% | -5.50 |
| Commercial Services | 6.5% | 1.5% | -5.00 |
| Retail Trade | 6.5% | 2.0% | -4.50 |
| Consumer Durables | 5.5% | 1.0% | -4.50 |

A share can move because a sector gained names or because another sector lost
them — the board is capped, so the shares are not independent. Read a Δ as
"more of the board looked like this today", never as an inflow.

### Board versus tape

Sectors where the board's median name and the mapped ETF disagree by at least
2 pp. This is the column that distinguishes a sector tape from a
stock-picking one.

| Sector | Board median | Tape | Gap | Tape detail |
|---|---|---|---|---|
| Consumer Non-Durables | +3.12 | -0.34 | +3.46 | XLP -0.34% |
| Electronic Technology | +3.77 | +1.69 | +2.08 | XLK +1.69% |

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
| Process Industries | XLB |
| Producer Manufacturing | XLI |
| Retail Trade | XLY |
| Technology Services | IGV, XLK |
| Transportation | XLI |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-10-26/master.csv` |
| Tape | `us-stocks-in-play/2026-10-26.md` |
| Sector source | `daily-screens/2026-10-26/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `change` (early schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

