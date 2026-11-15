# Sector flow — the 2026-11-11 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-11/master.csv` and `us-stocks-in-play/2026-11-11.md` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 1125 board rows across 12 sector(s), gics vocabulary · read-only

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
>    - **The sector on this date is not the board's own.** `daily-screens/2026-11-11/master.csv` publishes no sector column, so each sector was recovered by joining the board's tickers to `us-eod/2026-11-11.csv (joined on ticker)` — a different source with a GICS vocabulary, where the board's own dates mostly use a FactSet-style one. 980 of 1125 rows matched.
>    - No day-over-day delta: the previous board (`daily-screens/2026-11-10/master.csv`) labels sectors with the **factset-like** vocabulary and this one uses **gics**. Two taxonomies are not comparable, so the delta column is left empty rather than mapped across.
>    - 4 sector(s) carry no tape read: (unlabelled), Energy, Real Estate, Communication Services. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Financials | 249 | 22.1% | — | — | -0.08 | +0.56 | — |
| Health Care | 170 | 15.1% | — | — | +0.75 | +0.05 | — |
| Information Technology | 162 | 14.4% | — | — | +3.61 | +3.23 | — |
| Industrials | 159 | 14.1% | — | — | +0.89 | +1.33 | — |
| (unlabelled) | 145 | 12.9% | — | — | +0.94 | — | — |
| Consumer Discretionary | 58 | 5.2% | — | — | +0.10 | -0.06 | — |
| Energy | 47 | 4.2% | — | — | +3.43 | — | — |
| Real Estate | 36 | 3.2% | — | — | -0.45 | — | — |
| Communication Services | 35 | 3.1% | — | — | +1.46 | — | — |
| Utilities | 25 | 2.2% | — | — | +0.18 | +0.25 | — |
| Materials | 23 | 2.0% | — | — | +0.74 | +0.28 | — |
| Consumer Staples | 16 | 1.4% | — | — | +0.18 | +0.46 | — |

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
| Board | `daily-screens/2026-11-11/master.csv` |
| Tape | `us-stocks-in-play/2026-11-11.md` |
| Sector source | `us-eod/2026-11-11.csv (joined on ticker)` — **joined, not the board's own column** |
| Sector column | `—` (gics vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 1125 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

