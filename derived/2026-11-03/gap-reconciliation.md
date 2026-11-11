# Gap reconciliation — 2026-11-03 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-03-reactions.md` and `us-eod/2026-11-03.csv` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 6 PRE_GAP name(s) tagged at the 2026-11-03 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 100% (5 of 5 names): the morning
>    file's `Close` column matches the `2026-11-02` settled closes, so the morning gap
>    resolves into the `2026-11-03` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 1 of 6 PRE_GAP name(s) have no settled row in the 2026-11-03 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4566 of 4896 rows, so `Open gap %` is blank wherever the session file has no open.
>    - The 2026-11-03 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 1 | same sign, settled move larger than the morning gap |
| `held` | 1 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 3 | same sign but under that share, or an opposite sign under 0.5pp |
| `no_close` | 1 | no settled row for this name in the session file |
| **total** | **6** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-03` |
| Prior session (the `Close` column) | `2026-11-02` |
| Settled session joined to | `2026-11-03` |
| Prior-session match rate | 100% (5 of 5) |
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
| HLMN | -4.65 | — | -0.48 | `faded` | absent | — |
| UPWK | +4.64 | — | +2.16 | `faded` | absent | — |
| ECO | +3.52 | — | — | `no_close` | absent | — |
| PGR | -3.47 | — | -2.03 | `held` | absent | — |
| AESI | -2.43 | — | -0.97 | `faded` | absent | — |
| ULCC | -2.42 | — | -12.92 | `extended` | absent | — |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

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

