# Gap reconciliation — 2026-11-10 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-10-reactions.md` and `us-eod/2026-11-10.csv` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 69 PRE_GAP name(s) tagged at the 2026-11-10 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 100% (64 of 64 names): the morning
>    file's `Close` column matches the `2026-11-09` settled closes, so the morning gap
>    resolves into the `2026-11-10` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 5 of 69 PRE_GAP name(s) have no settled row in the 2026-11-10 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4786 of 4893 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 28 | same sign, settled move larger than the morning gap |
| `held` | 16 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 11 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 6 | opposite sign, settled move at least 0.5pp |
| `flat` | 3 | settled move under 0.25pp |
| `no_close` | 5 | no settled row for this name in the session file |
| **total** | **69** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-10` |
| Prior session (the `Close` column) | `2026-11-09` |
| Settled session joined to | `2026-11-10` |
| Prior-session match rate | 100% (64 of 64) |
| Verified | yes |

The reactions file's `Ref close` / `Ref asof` columns are the base of its `Chg %`
column — the prior session's own change — and are **not** the base of the
pre-market column. Using them to pick the session dates the join two sessions
early and turns held gaps into false reversals; that error was found and fixed
before this artifact was first published.

## Every PRE_GAP name

Sorted by the magnitude of the morning gap. Every row the scanner tagged
`PRE_GAP` is here, including the ones it did not look up a catalyst for.

| Ticker | Pre-mkt % | Open gap % | Settled chg % | Outcome | Catalyst | US access |
|---|---|---|---|---|---|---|
| APPS | -23.89 | -27.65 | -35.84 | `extended` | sourced | US-listed |
| AAON | +15.52 | +13.95 | +19.31 | `extended` | sourced | US-listed |
| SANM | +13.95 | +10.29 | +3.90 | `faded` | sourced | US-listed |
| RKLB | -7.78 | -6.58 | +6.54 | `reversed` | sourced | US-listed |
| SRRK | -6.83 | +0.93 | -6.89 | `held` | sourced | US-listed |
| LIF | -6.66 | -6.15 | -6.75 | `held` | not_looked_up | US-listed |
| CLMT | -6.54 | -3.99 | -3.19 | `faded` | not_looked_up | US-listed |
| GEV | -6.19 | -8.90 | -3.89 | `held` | not_looked_up | US-listed |
| TTD | -5.44 | -2.21 | +3.28 | `reversed` | not_looked_up | US-listed |
| QUBT | -4.81 | -4.81 | -8.16 | `extended` | not_looked_up | US-listed |
| ATEN | -4.14 | -0.48 | +2.70 | `reversed` | not_looked_up | US-listed |
| OUST | -3.98 | -1.48 | -0.91 | `faded` | not_looked_up | US-listed |
| CAT | -3.79 | -4.86 | -2.39 | `held` | not_looked_up | US-listed |
| AXTI | -3.78 | -4.41 | -8.39 | `extended` | not_looked_up | US-listed |
| SEI | -3.69 | -3.79 | -1.18 | `faded` | not_looked_up | US-listed |
| FLY | -3.62 | -3.29 | -2.51 | `held` | not_looked_up | US-listed |
| HYMC | -3.62 | -4.51 | -11.28 | `extended` | not_looked_up | US-listed |
| IONQ | -3.62 | -2.60 | -0.99 | `faded` | not_looked_up | US-listed |
| TTWO | +3.47 | +5.26 | +8.31 | `extended` | not_looked_up | US-listed |
| LEU | -3.45 | -4.35 | -6.33 | `extended` | not_looked_up | US-listed |
| COHR | -3.43 | -4.57 | -4.68 | `extended` | not_looked_up | US-listed |
| VRT | -3.41 | -5.99 | -3.13 | `held` | not_looked_up | US-listed |
| WIX | -3.23 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| RDW | -3.07 | -2.09 | -0.25 | `flat` | not_looked_up | US-listed |
| LITE | -3.06 | -3.56 | -1.78 | `held` | not_looked_up | US-listed |
| BE | -3.00 | -4.59 | -4.37 | `extended` | not_looked_up | US-listed |
| CIEN | -2.99 | -2.15 | +1.04 | `reversed` | not_looked_up | US-listed |
| RGTI | -2.93 | -3.08 | -6.39 | `extended` | not_looked_up | US-listed |
| VICR | -2.89 | -3.06 | -1.11 | `faded` | not_looked_up | US-listed |
| PPTA | -2.88 | -5.15 | -8.65 | `extended` | not_looked_up | US-listed |
| SMTC | -2.88 | -1.72 | -2.50 | `held` | not_looked_up | US-listed |
| AEHR | -2.86 | -2.17 | -0.40 | `faded` | not_looked_up | US-listed |
| ASTS | -2.82 | -7.29 | -8.67 | `extended` | not_looked_up | US-listed |
| LUNR | -2.74 | -4.24 | -1.91 | `held` | not_looked_up | US-listed |
| BTDR | -2.72 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| MXL | -2.72 | -3.42 | -3.72 | `extended` | not_looked_up | US-listed |
| FPS | -2.70 | -4.56 | -4.96 | `extended` | not_looked_up | US-listed |
| AEM | -2.69 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| SG | -2.62 | +1.87 | -0.90 | `faded` | not_looked_up | US-listed |
| OKLO | -2.57 | -4.25 | -6.52 | `extended` | not_looked_up | US-listed |
| ONTO | +2.56 | +3.35 | +1.81 | `held` | not_looked_up | US-listed |
| EROC | -2.55 | -4.24 | -4.61 | `extended` | not_looked_up | US-listed |
| ONDS | -2.51 | -2.28 | -6.70 | `extended` | not_looked_up | US-listed |
| INTC | -2.48 | -2.36 | -2.09 | `held` | not_looked_up | US-listed |
| ECG | -2.40 | -0.63 | +1.54 | `reversed` | not_looked_up | US-listed |
| MOD | -2.39 | -3.01 | -2.95 | `extended` | not_looked_up | US-listed |
| INFQ | -2.38 | -2.69 | -3.21 | `extended` | not_looked_up | US-listed |
| WOLF | -2.37 | -1.23 | +0.42 | `faded` | not_looked_up | US-listed |
| FN | -2.36 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AVAV | -2.33 | -3.31 | -2.76 | `extended` | not_looked_up | US-listed |
| FLR | -2.33 | -0.72 | +0.22 | `faded` | not_looked_up | US-listed |
| ETN | -2.31 | -3.26 | -1.41 | `held` | not_looked_up | US-listed (ADR) |
| MRVL | -2.31 | -2.98 | -0.14 | `flat` | not_looked_up | US-listed |
| AUGO | -2.30 | -4.44 | -6.53 | `extended` | not_looked_up | US-listed |
| GLW | -2.26 | -1.98 | -3.25 | `extended` | not_looked_up | US-listed |
| PENG | -2.21 | -2.63 | -2.32 | `held` | not_looked_up | US-listed |
| NEM | -2.19 | -3.83 | -4.18 | `extended` | not_looked_up | US-listed |
| CLSK | -2.17 | -4.46 | -4.92 | `extended` | not_looked_up | US-listed |
| PWR | -2.17 | -1.32 | -1.41 | `held` | not_looked_up | US-listed |
| TEM | -2.17 | -2.45 | -4.62 | `extended` | not_looked_up | US-listed |
| MKSI | -2.16 | -1.94 | +0.88 | `reversed` | not_looked_up | US-listed |
| SVM | -2.16 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| SKYD | -2.11 | -3.33 | -7.59 | `extended` | not_looked_up | US-listed |
| TTMI | -2.11 | -1.22 | -4.12 | `extended` | not_looked_up | US-listed |
| TER | -2.08 | -2.07 | -0.24 | `flat` | not_looked_up | US-listed |
| NVTS | -2.07 | -2.71 | -2.09 | `held` | not_looked_up | US-listed |
| PL | -2.06 | -3.06 | -0.70 | `faded` | not_looked_up | US-listed |
| CEG | -2.02 | -2.10 | -3.02 | `extended` | not_looked_up | US-listed |
| MPWR | -2.01 | -2.02 | -2.19 | `held` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

64 of 69 name(s) carry `not_looked_up`: the morning scanner's own table says
"no catalyst lookup (outside the per-run budget)" for them. **The absence of a
catalyst for those names is a budget decision, not a finding** — and a reader of
the sweep has no way to tell those two apart. This column makes the difference
visible instead of leaving an empty cell that reads as "nothing happened".

## Method and caveats

| Rule | Value |
|---|---|
| Morning gap counts as a gap at | 1.0 pp |
| `held` keeps at least | 50% of the gap's magnitude |
| `extended` requires | settled move ≥ gap + 0.25 pp |
| `reversed` requires | opposite sign and settled move ≥ 0.5 pp |
| `flat` is | settled move < 0.25 pp |

These constants live at the top of `scripts/build_gap_reconciliation.py`. Change
them there and the labels change here — this table is never adjusted by hand.

The join is a copy: every value in it comes from one of the two sources in the
provenance line. Nothing is interpolated, no missing price is filled in, and a
name with no settled row is labelled rather than dropped. `gap-reconciliation.csv`
beside this file carries the same rows with the prior close, the move-vs-average
figure and the catalyst text in full.

