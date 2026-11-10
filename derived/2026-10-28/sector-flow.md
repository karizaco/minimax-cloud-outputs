# Sector flow — the 2026-10-28 board by sector

**Source:** derived aggregation over `daily-screens/2026-10-28/master.csv` and `us-stocks-in-play/2026-10-28.md` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 200 board rows across 11 sector(s), gics vocabulary · read-only

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
>    - **The sector on this date is not the board's own.** `daily-screens/2026-10-28/master.csv` publishes no sector column, so each sector was recovered by joining the board's tickers to `us-eod/2026-10-28.csv (joined on ticker)` — a different source with a GICS vocabulary, where the board's own dates mostly use a FactSet-style one. 182 of 200 rows matched.
>    - The session-change column on this date is `chg_pct_1028`, chosen because it is stamped with the directory date. The column name is not stable across dates.
>    - No day-over-day delta: the previous board (`daily-screens/2026-10-27/master.csv`) labels sectors with the **factset-like** vocabulary and this one uses **gics**. Two taxonomies are not comparable, so the delta column is left empty rather than mapped across.
>    - 11 sector(s) carry no tape read: Information Technology, Health Care, Industrials, (unlabelled), Financials, Energy. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Information Technology | 65 | 32.5% | — | — | +0.53 | — | — |
| Health Care | 47 | 23.5% | — | — | +6.70 | — | — |
| Industrials | 26 | 13.0% | — | — | +3.32 | — | — |
| (unlabelled) | 18 | 9.0% | — | — | +6.03 | — | — |
| Financials | 12 | 6.0% | — | — | +4.51 | — | — |
| Energy | 11 | 5.5% | — | — | — | — | — |
| Consumer Discretionary | 9 | 4.5% | — | — | -0.83 | — | — |
| Communication Services | 4 | 2.0% | — | — | — | — | — |
| Materials | 4 | 2.0% | — | — | +0.77 | — | — |
| Utilities | 3 | 1.5% | — | — | — | — | — |
| Consumer Staples | 1 | 0.5% | — | — | — | — | — |

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
| Utilities | XLU |

## Method and caveats

| Field | Value |
|---|---|
| Board | `daily-screens/2026-10-28/master.csv` |
| Tape | `us-stocks-in-play/2026-10-28.md` |
| Sector source | `us-eod/2026-10-28.csv (joined on ticker)` — **joined, not the board's own column** |
| Sector column | `—` (gics vocabulary) |
| Session-change column | `chg_pct_1028` (stamped with the directory date) |
| Board rows counted | 200 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

