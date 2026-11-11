# Gap reconciliation — 2026-11-09 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-09-reactions.md` and `us-eod/2026-11-09.csv` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 83 PRE_GAP name(s) tagged at the 2026-11-09 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 93% (66 of 71 names): the morning
>    file's `Close` column matches the `2026-11-06` settled closes, so the morning gap
>    resolves into the `2026-11-09` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 12 of 83 PRE_GAP name(s) have no settled row in the 2026-11-09 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4502 of 4895 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 47 | same sign, settled move larger than the morning gap |
| `held` | 11 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 4 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 9 | opposite sign, settled move at least 0.5pp |
| `no_close` | 12 | no settled row for this name in the session file |
| **total** | **83** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-09` |
| Prior session (the `Close` column) | `2026-11-06` |
| Settled session joined to | `2026-11-09` |
| Prior-session match rate | 93% (66 of 71) |
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
| CECO | +35.19 | — | — | `no_close` | sourced | US-listed |
| VIR | +15.09 | +7.94 | +11.79 | `held` | sourced | US-listed |
| IBRX | -13.72 | -16.27 | -17.66 | `extended` | sourced | US-listed |
| REF | +10.08 | +1.71 | +12.44 | `extended` | sourced | US-listed |
| IMVT | +9.66 | +8.09 | +15.13 | `extended` | sourced | US-listed |
| KGS | +8.16 | +4.77 | +7.07 | `held` | not_looked_up | US-listed |
| MNDY | -6.91 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AKAM | -6.25 | -5.25 | -3.37 | `held` | not_looked_up | US-listed |
| ASTS | +5.94 | +3.59 | +14.10 | `extended` | not_looked_up | US-listed |
| CNL | +4.85 | +3.88 | +5.83 | `extended` | not_looked_up | US-listed |
| NVDA | -4.81 | -7.29 | -4.23 | `held` | not_looked_up | US-listed |
| DB | +4.45 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AMD | +4.32 | +5.43 | +13.27 | `extended` | not_looked_up | US-listed |
| NRG | +4.20 | +5.94 | +10.36 | `extended` | not_looked_up | US-listed |
| HYMC | +4.16 | +5.17 | +13.32 | `extended` | not_looked_up | US-listed |
| MANE | +4.05 | -0.43 | +3.75 | `held` | not_looked_up | US-listed |
| PLAB | -3.98 | +2.34 | +5.70 | `reversed` | not_looked_up | US-listed |
| TH | -3.96 | -9.07 | -2.64 | `held` | not_looked_up | US-listed |
| SCCO | +3.84 | +4.61 | +5.26 | `extended` | not_looked_up | US-listed |
| FCX | +3.82 | +4.02 | +4.90 | `extended` | not_looked_up | US-listed |
| YELP | +3.80 | +0.41 | +0.62 | `faded` | not_looked_up | US-listed |
| SGI | -3.77 | -1.87 | +3.31 | `reversed` | not_looked_up | US-listed |
| KOD | +3.73 | +2.42 | +7.86 | `extended` | not_looked_up | US-listed |
| USAR | +3.71 | +2.01 | +6.50 | `extended` | not_looked_up | US-listed |
| GCT | +3.68 | +2.79 | +1.65 | `faded` | not_looked_up | US-listed |
| UEC | +3.47 | +3.83 | +10.20 | `extended` | not_looked_up | US-listed |
| AVGO | +3.45 | +3.95 | +8.78 | `extended` | not_looked_up | US-listed |
| FLO | +3.43 | -0.15 | -4.62 | `reversed` | not_looked_up | US-listed |
| IREN | -3.33 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| PPTA | +3.33 | +4.71 | +8.35 | `extended` | not_looked_up | US-listed |
| AMZN | +3.28 | +3.86 | +2.93 | `held` | not_looked_up | US-listed |
| ONDS | +3.28 | +2.49 | +11.90 | `extended` | not_looked_up | US-listed |
| BSP | +3.18 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CIFR | -3.14 | -1.30 | +4.05 | `reversed` | not_looked_up | US-listed |
| BETA | -3.10 | -3.73 | +5.20 | `reversed` | not_looked_up | US-listed |
| EROC | +3.09 | +3.23 | +15.87 | `extended` | not_looked_up | US-listed |
| AUGO | +3.06 | +4.51 | +11.78 | `extended` | not_looked_up | US-listed |
| GOOGL | +3.04 | +2.63 | +1.16 | `faded` | not_looked_up | US-listed |
| RCL | +3.01 | +2.72 | +3.03 | `held` | not_looked_up | US-listed |
| GOOG | +3.00 | +2.50 | +0.74 | `faded` | not_looked_up | US-listed |
| NVMI | +2.95 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| VICR | +2.94 | +3.61 | +11.30 | `extended` | not_looked_up | US-listed |
| IAG | +2.93 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AEM | +2.87 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| FPS | +2.82 | +5.30 | +16.20 | `extended` | not_looked_up | US-listed |
| AXON | +2.81 | +2.01 | -3.13 | `reversed` | not_looked_up | US-listed |
| SVM | +2.81 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| HUT | -2.79 | -0.61 | +8.30 | `reversed` | not_looked_up | US-listed |
| META | +2.78 | +3.41 | +5.11 | `extended` | not_looked_up | US-listed |
| NEM | +2.76 | +3.89 | +3.56 | `extended` | not_looked_up | US-listed |
| SPCX | +2.76 | +1.64 | +5.81 | `extended` | not_looked_up | US-listed |
| CENX | +2.75 | +2.51 | +9.41 | `extended` | not_looked_up | US-listed |
| ETON | +2.73 | +2.36 | +13.97 | `extended` | not_looked_up | US-listed |
| MSFT | +2.71 | +2.62 | +2.75 | `held` | not_looked_up | US-listed |
| RH | +2.70 | +1.15 | +4.35 | `extended` | not_looked_up | US-listed |
| MSDL | +2.64 | +1.39 | +2.35 | `held` | not_looked_up | US-listed |
| LRCX | +2.62 | +2.99 | +10.43 | `extended` | not_looked_up | US-listed |
| BTDR | -2.58 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AMAT | +2.55 | +3.13 | +11.36 | `extended` | not_looked_up | US-listed |
| ARDT | +2.54 | +3.12 | +3.93 | `extended` | not_looked_up | US-listed |
| CRDO | +2.53 | +2.99 | +10.29 | `extended` | not_looked_up | US-listed (ADR) |
| ATEC | +2.49 | +0.40 | -0.81 | `reversed` | not_looked_up | US-listed |
| GLP | -2.47 | — | -7.04 | `extended` | not_looked_up | US-listed |
| ANET | +2.45 | +3.40 | +9.02 | `extended` | not_looked_up | US-listed |
| CYTK | +2.42 | +1.49 | +2.70 | `extended` | not_looked_up | US-listed |
| FUN | +2.40 | -0.10 | +7.49 | `extended` | not_looked_up | US-listed |
| LUNR | +2.39 | +3.82 | +15.00 | `extended` | not_looked_up | US-listed |
| RDW | +2.36 | +1.04 | +13.12 | `extended` | not_looked_up | US-listed |
| RKLB | +2.34 | +2.34 | +10.91 | `extended` | not_looked_up | US-listed |
| ITW | +2.33 | +1.35 | +2.03 | `held` | not_looked_up | US-listed |
| VECO | +2.31 | +2.90 | +6.48 | `extended` | not_looked_up | US-listed |
| SEI | +2.30 | +2.22 | +8.40 | `extended` | not_looked_up | US-listed |
| HWM | +2.27 | +2.14 | +5.05 | `extended` | not_looked_up | US-listed |
| PENG | +2.22 | +2.68 | +9.25 | `extended` | not_looked_up | US-listed |
| GE | +2.17 | +2.66 | +3.77 | `extended` | not_looked_up | US-listed |
| NVT | +2.15 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ETN | +2.13 | +1.81 | +5.12 | `extended` | not_looked_up | US-listed (ADR) |
| APPS | +2.12 | +1.45 | +8.86 | `extended` | not_looked_up | US-listed |
| HIMS | -2.12 | -2.88 | -11.77 | `extended` | not_looked_up | US-listed |
| DKNG | -2.11 | -3.94 | +1.03 | `reversed` | not_looked_up | US-listed |
| GEV | +2.06 | +3.98 | +7.12 | `extended` | not_looked_up | US-listed |
| URGN | +2.02 | — | — | `no_close` | not_looked_up | US-listed |
| BX | +2.01 | +1.59 | +3.85 | `extended` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

78 of 83 name(s) carry `not_looked_up`: the morning scanner's own table says
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

