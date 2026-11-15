# Sector flow — the 2026-11-12 board by sector

**Source:** derived aggregation over `daily-screens/2026-11-12/master.csv` and `us-stocks-in-play/2026-11-12.md` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 1173 board rows across 21 sector(s), factset-like vocabulary · read-only

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
>    - No day-over-day delta: the previous board (`daily-screens/2026-11-11/master.csv`) labels sectors with the **gics** vocabulary and this one uses **factset-like**. Two taxonomies are not comparable, so the delta column is left empty rather than mapped across.
>    - 18 sector(s) carry no tape read: Finance, Health Technology, Producer Manufacturing, Consumer Services, Utilities, Retail Trade. Each is left blank rather than attached to a loose proxy.

## The board's sector mix

| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |
|---|---|---|---|---|---|---|---|
| Finance | 336 | 28.6% | — | — | -0.42 | — | — |
| Health Technology | 156 | 13.3% | — | — | -2.05 | — | — |
| Technology Services | 128 | 10.9% | — | — | -1.10 | -0.36 | — |
| Electronic Technology | 124 | 10.6% | — | — | -1.90 | -0.36 | — |
| Producer Manufacturing | 57 | 4.9% | — | — | -2.34 | — | — |
| Consumer Services | 38 | 3.2% | — | — | -2.29 | — | — |
| Utilities | 38 | 3.2% | — | — | +0.01 | — | — |
| Energy Minerals | 36 | 3.1% | — | — | +1.64 | +1.50 | — |
| Retail Trade | 36 | 3.1% | — | — | -1.73 | — | — |
| Industrial Services | 32 | 2.7% | — | — | -0.60 | — | — |
| Consumer Non-Durables | 28 | 2.4% | — | — | -1.31 | — | — |
| Consumer Durables | 27 | 2.3% | — | — | -2.86 | — | — |
| Non-Energy Minerals | 26 | 2.2% | — | — | -3.52 | — | — |
| Transportation | 22 | 1.9% | — | — | +0.37 | — | — |
| Commercial Services | 21 | 1.8% | — | — | -1.54 | — | — |
| Health Services | 20 | 1.7% | — | — | -1.03 | — | — |
| Communications | 12 | 1.0% | — | — | -0.20 | — | — |
| Miscellaneous | 10 | 0.8% | — | — | -1.10 | — | — |
| Distribution Services | 9 | 0.8% | — | — | +0.09 | — | — |
| Process Industries | 9 | 0.8% | — | — | -2.01 | — | — |
| (unlabelled) | 8 | 0.7% | — | — | — | — | — |

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
| Board | `daily-screens/2026-11-12/master.csv` |
| Tape | `us-stocks-in-play/2026-11-12.md` |
| Sector source | `daily-screens/2026-11-12/master.csv` |
| Sector column | `sector` (factset-like vocabulary) |
| Session-change column | `today_change` (current schema) |
| Board rows counted | 1173 |
| Share-shift threshold | 3.0 pp |
| Board-versus-tape threshold | 2.0 pp |

The column names above are not stable across dates — that is why they are
printed. `sector-flow.csv` beside this file carries the same rows.

