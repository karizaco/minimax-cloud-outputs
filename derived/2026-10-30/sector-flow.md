# Sector flow — the 2026-10-30 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-30/master.csv` and `us-stocks-in-play/2026-10-30.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 409 board rows across 11 sector(s), gics vocabulary · read-only

> **Read this before the table.**
> 
> 1. **This counts the board, it does not weight the market.** A sector's share
>    is its share of the names the screen published, not of any index. A sector
>    with 40% of the board is where the screen found candidates — that is a
>    statement about the screen's output, not about market capitalisation.
> 2. **The vocabulary on this date is `gics`.** The boards use a FactSet-style
>    taxonomy on most dates, and GICS wherever the board carries a `gics_sector`
>    column or the sector had to be recovered from `us-eod/`. The two are never
>    blended and a delta across them is never computed.
> 3. **The ETF column is a mapping, not a fact.** Which ETF reads a sector is a
>    judgement, published in full under *The sector-to-ETF mapping* below.
> 4. **Deviations and degraded paths.**
>    - The session-change column on this date is `chg_1030_pct`, chosen because it is stamped with the directory date. The column name is not stable across dates.
>    - 11 sector(s) carry no tape read: Information Technology, Health Care, Industrials, Energy, Financials, Consumer Discretionary. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Information Technology | 113 | 27.6% | 26.1% | +1.53 | -6.37 | — | — |
| Health Care | 71 | 17.4% | 17.5% | -0.18 | -1.32 | — | — |
| Industrials | 56 | 13.7% | 12.7% | +0.97 | -2.84 | — | — |
| Energy | 54 | 13.2% | 11.6% | +1.58 | +1.75 | — | — |
| Financials | 50 | 12.2% | 10.5% | +1.69 | -1.90 | — | — |
| Consumer Discretionary | 32 | 7.8% | 8.1% | -0.29 | +0.03 | — | — |
| Communication Services | 13 | 3.2% | 3.1% | +0.11 | +0.05 | — | — |
| Materials | 11 | 2.7% | 7.9% | -5.20 | -4.88 | — | — |
| Consumer Staples | 3 | 0.7% | 0.4% | +0.29 | +3.54 | — | — |
| Real Estate | 3 | 0.7% | 0.7% | +0.07 | +0.92 | — | — |
| Utilities | 3 | 0.7% | 1.3% | -0.59 | -1.83 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-10-29`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Materials | 7.9% | 2.7% | -5.20 |

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
| Communication Services | XLC |
| Consumer Discretionary | XLY |
| Consumer Staples | XLP |
| Financials | XLF |
| Health Care | XLV |
| Industrials | XLI |
| Information Technology | XLK |
| Materials | XLB |
| Real Estate | XLRE |
| Utilities | XLU |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-10-30/master.csv` |
| Tape | `us-stocks-in-play/2026-10-30.md` |
| Sector source | `daily-screens/2026-10-30/master.csv` |
| Sector column | `gics_sector` (gics vocabulary) |
| Session-change column | `chg_1030_pct` (stamped with the directory date) |
| Board rows counted | 409 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

