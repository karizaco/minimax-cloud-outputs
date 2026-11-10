# Sector flow — the 2026-11-03 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-03/master.csv` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 12 sector(s), gics vocabulary · read-only

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
>    - **The sector on this date is not the board's own.** `daily-screens/2026-11-03/master.csv` publishes no sector column, so each sector was recovered by joining the board's tickers to `us-eod/2026-11-03.csv (joined on ticker)` — a different source with a GICS vocabulary, where the board's own dates mostly use a FactSet-style one. 175 of 200 rows matched.
>    - The session-change column on this date is `chg_pct_2026-11-03`, chosen because it is stamped with the directory date. The column name is not stable across dates.
>    - No ETF tape found for this date in `us-stocks-in-play/`, so the board-versus-tape comparison is empty.
>    - 12 sector(s) carry no tape read: Information Technology, Health Care, Industrials, (unlabelled), Consumer Discretionary, Financials. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Information Technology | 46 | 23.0% | 21.0% | +2.00 | +2.69 | — | — |
| Health Care | 28 | 14.0% | 24.0% | -10.00 | +2.08 | — | — |
| Industrials | 28 | 14.0% | 8.5% | +5.50 | +1.85 | — | — |
| (unlabelled) | 25 | 12.5% | 11.5% | +1.00 | +2.12 | — | — |
| Consumer Discretionary | 19 | 9.5% | 12.0% | -2.50 | +0.20 | — | — |
| Financials | 19 | 9.5% | 7.5% | +2.00 | +0.33 | — | — |
| Consumer Staples | 10 | 5.0% | 1.5% | +3.50 | -1.88 | — | — |
| Communication Services | 9 | 4.5% | 4.5% | +0.00 | +2.26 | — | — |
| Energy | 9 | 4.5% | 3.0% | +1.50 | -1.23 | — | — |
| Materials | 4 | 2.0% | 5.0% | -3.00 | -1.27 | — | — |
| Real Estate | 2 | 1.0% | 1.0% | +0.00 | -0.43 | — | — |
| Utilities | 1 | 0.5% | 0.5% | +0.00 | +7.29 | — | — |

**What this table means.** `Share` is the sector's percentage of the published
board. `Median chg` is the median session change of that sector's names on the
board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is
the median change of the mapped ETFs as the in-play digest published them.

**What it does not mean.** It is not a performance attribution and not a return.
The board is a screen output, so a sector's median change describes *names that
passed a momentum screen in that sector*, which is a biased sample of the sector
by construction. A reader should not infer sector performance from it — that is
what the `Tape` column is for, and the two measure different things on purpose.

### Where the board moved, versus `2026-11-02`

Sectors whose share of the board moved at least 3 pp.

| Sector | Prev share | Share | Δ |
|---|---|---|---|
| Health Care | 24.0% | 14.0% | -10.00 |
| Industrials | 8.5% | 14.0% | +5.50 |
| Consumer Staples | 1.5% | 5.0% | +3.50 |
| Materials | 5.0% | 2.0% | -3.00 |

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
| Board | `daily-screens/2026-11-03/master.csv` |
| Tape | `— none for this date` |
| Sector source | `us-eod/2026-11-03.csv (joined on ticker)` — **joined, not the board's own column** |
| Sector column | `—` (gics vocabulary) |
| Session-change column | `chg_pct_2026-11-03` (stamped with the directory date) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

