# Gap reconciliation — 2026-11-13 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-13-reactions.md` and `us-eod/2026-11-13.csv` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 25 PRE_GAP name(s) tagged at the 2026-11-13 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 95% (18 of 19 names): the morning
>    file's `Close` column matches the `2026-11-12` settled closes, so the morning gap
>    resolves into the `2026-11-13` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 6 of 25 PRE_GAP name(s) have no settled row in the 2026-11-13 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 3640 of 4890 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 7 | same sign, settled move larger than the morning gap |
| `held` | 1 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 4 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 7 | opposite sign, settled move at least 0.5pp |
| `no_close` | 6 | no settled row for this name in the session file |
| **total** | **25** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-13` |
| Prior session (the `Close` column) | `2026-11-12` |
| Settled session joined to | `2026-11-13` |
| Prior-session match rate | 95% (18 of 19) |
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
| VIR | -16.67 | -13.70 | -17.82 | `extended` | sourced | US-listed |
| SLS | +8.66 | +7.86 | -2.12 | `reversed` | sourced | US-listed |
| HOS | +6.35 | +1.37 | +1.80 | `faded` | sourced | US-listed |
| GENB | +4.53 | +0.56 | -3.98 | `reversed` | sourced | US-listed |
| TRV | +3.68 | +0.82 | -0.05 | `faded` | sourced | US-listed |
| CSCO | -3.62 | -1.67 | -6.24 | `extended` | not_looked_up | US-listed |
| ALM | +3.33 | — | — | `no_close` | not_looked_up | US-listed |
| PANW | +3.13 | +2.82 | -0.15 | `faded` | not_looked_up | US-listed |
| AGBK | +3.01 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CRML | +3.01 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AMD | -2.78 | -3.18 | -8.75 | `extended` | not_looked_up | US-listed |
| WGS | -2.64 | -1.68 | +0.96 | `reversed` | not_looked_up | US-listed |
| ABSI | +2.57 | +2.46 | -7.50 | `reversed` | not_looked_up | US-listed |
| AEHR | -2.52 | — | -6.65 | `extended` | not_looked_up | US-listed |
| NBIS | -2.44 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CRWD | +2.43 | +2.44 | -1.44 | `reversed` | not_looked_up | US-listed |
| MSTR | -2.41 | -2.10 | -2.45 | `held` | not_looked_up | US-listed |
| SECZ | +2.38 | +1.79 | -3.69 | `reversed` | not_looked_up | US-listed |
| PLBL | -2.34 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| VOYG | -2.30 | -0.94 | -2.73 | `extended` | not_looked_up | US-listed |
| S | +2.29 | +1.93 | -0.18 | `faded` | not_looked_up | US-listed |
| AVGO | -2.27 | -2.17 | -4.78 | `extended` | not_looked_up | US-listed |
| FIGR | +2.26 | +1.36 | -1.75 | `reversed` | not_looked_up | US-listed |
| IREN | -2.05 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| GLXY | -2.04 | -1.65 | -5.27 | `extended` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

20 of 25 name(s) carry `not_looked_up`: the morning scanner's own table says
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

