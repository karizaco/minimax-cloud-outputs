# Sector flow — the 2026-11-13 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-13/master.csv` and `us-stocks-in-play/2026-11-13.md` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 1188 board rows across 21 sector(s), factset-like vocabulary · read-only

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
>    - 19 sector(s) carry no tape read: Finance, Health Technology, Producer Manufacturing, Consumer Services, Utilities, Consumer Non-Durables. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Finance | 354 | 29.8% | 28.6% | +1.16 | +0.19 | — | — |
| Health Technology | 147 | 12.4% | 13.3% | -0.93 | +0.14 | — | — |
| Technology Services | 115 | 9.7% | 10.9% | -1.23 | -0.42 | -2.01 | — |
| Electronic Technology | 107 | 9.0% | 10.6% | -1.56 | -3.61 | -2.01 | — |
| Producer Manufacturing | 48 | 4.0% | 4.9% | -0.82 | -0.48 | — | — |
| Consumer Services | 43 | 3.6% | 3.2% | +0.38 | +0.36 | — | — |
| Utilities | 40 | 3.4% | 3.2% | +0.13 | +0.54 | — | — |
| Consumer Non-Durables | 39 | 3.3% | 2.4% | +0.89 | +1.47 | — | — |
| Retail Trade | 38 | 3.2% | 3.1% | +0.13 | +0.67 | — | — |
| Industrial Services | 37 | 3.1% | 2.7% | +0.38 | -0.19 | — | — |
| Commercial Services | 35 | 3.0% | 1.8% | +1.16 | +0.96 | — | — |
| Energy Minerals | 31 | 2.6% | 3.1% | -0.46 | +0.77 | — | — |
| Non-Energy Minerals | 31 | 2.6% | 2.2% | +0.39 | -1.35 | — | — |
| Consumer Durables | 25 | 2.1% | 2.3% | -0.20 | +0.04 | — | — |
| Transportation | 24 | 2.0% | 1.9% | +0.14 | +0.65 | — | — |
| Health Services | 22 | 1.9% | 1.7% | +0.14 | -0.01 | — | — |
| Communications | 15 | 1.3% | 1.0% | +0.24 | +0.06 | — | — |
| Miscellaneous | 11 | 0.9% | 0.8% | +0.08 | +0.00 | — | — |
| Process Industries | 11 | 0.9% | 0.8% | +0.16 | +0.90 | — | — |
| Distribution Services | 9 | 0.8% | 0.8% | -0.01 | +0.91 | — | — |
| (unlabelled) | 6 | 0.5% | 0.7% | -0.17 | — | — | — |

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
| Board | `daily-screens/2026-11-13/master.csv` |
| Tape | `us-stocks-in-play/2026-11-13.md` |
| Sector source | `daily-screens/2026-11-13/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 1188 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

