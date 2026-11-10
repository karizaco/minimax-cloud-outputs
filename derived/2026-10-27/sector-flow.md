# Sector flow — the 2026-10-27 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-27/master.csv` and `us-stocks-in-play/2026-10-27.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 17 sector(s), factset-like vocabulary · read-only

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
>    - 16 sector(s) carry no tape read: Electronic Technology, Technology Services, Health Technology, Finance, Non-Energy Minerals, Producer Manufacturing. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Electronic Technology | 64 | 32.0% | 26.0% | +6.00 | +5.62 | — | — |
| Technology Services | 44 | 22.0% | 25.0% | -3.00 | +5.63 | — | — |
| Health Technology | 29 | 14.5% | 14.5% | +0.00 | +5.81 | — | — |
| Finance | 13 | 6.5% | 5.0% | +1.50 | +4.24 | — | — |
| Non-Energy Minerals | 13 | 6.5% | 3.5% | +3.00 | +7.76 | — | — |
| Producer Manufacturing | 13 | 6.5% | 3.5% | +3.00 | +7.18 | — | — |
| Industrial Services | 4 | 2.0% | 4.0% | -2.00 | +4.13 | — | — |
| Consumer Services | 3 | 1.5% | 2.0% | -0.50 | +4.35 | — | — |
| Process Industries | 3 | 1.5% | 2.0% | -0.50 | +0.22 | — | — |
| Retail Trade | 3 | 1.5% | 2.0% | -0.50 | +1.61 | — | — |
| Commercial Services | 2 | 1.0% | 1.5% | -0.50 | +0.83 | — | — |
| Communications | 2 | 1.0% | 1.5% | -0.50 | +6.12 | — | — |
| Consumer Non-Durables | 2 | 1.0% | 0.5% | +0.50 | -0.60 | — | — |
| Energy Minerals | 2 | 1.0% | 3.0% | -2.00 | -2.41 | -2.03 | — |
| Consumer Durables | 1 | 0.5% | 1.0% | -0.50 | +3.67 | — | — |
| Distribution Services | 1 | 0.5% | 1.0% | -0.50 | +1.53 | — | — |
| Transportation | 1 | 0.5% | 3.0% | -2.50 | +1.87 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-10-26`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Electronic Technology | 26.0% | 32.0% | +6.00 |
| Technology Services | 25.0% | 22.0% | -3.00 |
| Non-Energy Minerals | 3.5% | 6.5% | +3.00 |
| Producer Manufacturing | 3.5% | 6.5% | +3.00 |

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
| Board | `daily-screens/2026-10-27/master.csv` |
| Tape | `us-stocks-in-play/2026-10-27.md` |
| Sector source | `daily-screens/2026-10-27/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `change` (early schema) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

