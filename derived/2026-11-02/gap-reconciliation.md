# Gap reconciliation — 2026-11-02 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-02-reactions.md` and `us-eod/2026-11-02.csv` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 73 PRE_GAP name(s) tagged at the 2026-11-02 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 90% (54 of 60 names): the morning
>    file's `Close` column matches the `2026-10-30` settled closes, so the morning gap
>    resolves into the `2026-11-02` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 13 of 73 PRE_GAP name(s) have no settled row in the 2026-11-02 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4733 of 4899 rows, so `Open gap %` is blank wherever the session file has no open.
>    - The 2026-11-02 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 10 | same sign, settled move larger than the morning gap |
| `held` | 3 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 6 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 38 | opposite sign, settled move at least 0.5pp |
| `flat` | 3 | settled move under 0.25pp |
| `no_close` | 13 | no settled row for this name in the session file |
| **total** | **73** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-02` |
| Prior session (the `Close` column) | `2026-10-30` |
| Settled session joined to | `2026-11-02` |
| Prior-session match rate | 90% (54 of 60) |
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
| PGEN | -30.55 | — | -25.94 | `held` | absent | — |
| RSI | -5.86 | — | -5.94 | `held` | absent | — |
| CHRN | +4.38 | — | -9.39 | `reversed` | absent | — |
| COHR | +4.35 | — | -4.93 | `reversed` | absent | — |
| INIO | +4.29 | — | — | `no_close` | absent | — |
| TEM | +3.85 | — | +8.67 | `extended` | absent | — |
| RIG | -3.79 | — | — | `no_close` | absent | — |
| WULF | +3.75 | — | -6.74 | `reversed` | absent | — |
| CRWV | +3.43 | — | -8.60 | `reversed` | absent | — |
| NTSK | +3.29 | — | -9.46 | `reversed` | absent | — |
| FORM | +3.28 | — | -0.26 | `faded` | absent | — |
| GRAL | +3.21 | — | -6.74 | `reversed` | absent | — |
| RIVN | +3.21 | — | +8.47 | `extended` | absent | — |
| RAPP | +3.19 | — | +0.32 | `faded` | absent | — |
| MAR | +3.18 | — | +4.26 | `extended` | absent | — |
| STDN | +3.09 | — | -1.09 | `reversed` | absent | — |
| AEHR | +3.08 | — | -6.23 | `reversed` | absent | — |
| AXTI | +3.03 | — | -12.46 | `reversed` | absent | — |
| POWI | +3.03 | — | +2.26 | `held` | absent | — |
| ACMR | +2.93 | — | -2.90 | `reversed` | absent | — |
| PENG | +2.91 | — | -8.53 | `reversed` | absent | — |
| CRWD | +2.90 | — | -3.44 | `reversed` | absent | — |
| AAON | +2.80 | — | +0.88 | `faded` | absent | — |
| ATEC | +2.80 | — | +3.83 | `extended` | absent | — |
| UCTT | +2.80 | — | -5.79 | `reversed` | absent | — |
| LNG | -2.79 | — | -5.65 | `extended` | absent | — |
| ALHC | +2.75 | — | -3.71 | `reversed` | absent | — |
| RMBS | +2.74 | — | -0.76 | `reversed` | absent | — |
| DOCN | +2.73 | — | +0.16 | `flat` | absent | — |
| TSEM | +2.72 | — | — | `no_close` | absent | — |
| AGIO | +2.65 | — | -1.96 | `reversed` | absent | — |
| APP | +2.63 | — | +0.15 | `flat` | absent | — |
| SITM | +2.63 | — | -6.52 | `reversed` | absent | — |
| FRVO | +2.60 | — | -0.30 | `faded` | absent | — |
| PBF | -2.55 | — | -3.74 | `extended` | absent | — |
| NBIS | +2.54 | — | — | `no_close` | absent | — |
| SECZ | +2.51 | — | -4.23 | `reversed` | absent | — |
| WOLF | +2.46 | — | -5.14 | `reversed` | absent | — |
| ABSI | +2.43 | — | -12.94 | `reversed` | absent | — |
| KLIC | +2.43 | — | — | `no_close` | absent | — |
| ICHR | +2.42 | — | -5.30 | `reversed` | absent | — |
| SU | -2.42 | — | — | `no_close` | absent | — |
| FIGR | +2.41 | — | +0.97 | `faded` | absent | — |
| AUGO | +2.39 | — | +0.03 | `flat` | absent | — |
| POWL | +2.39 | — | -1.44 | `reversed` | absent | — |
| PLPC | +2.36 | — | -4.28 | `reversed` | absent | — |
| UI | +2.34 | — | -4.21 | `reversed` | absent | — |
| PTEN | -2.33 | — | -11.41 | `extended` | absent | — |
| GDYN | -2.32 | — | +2.47 | `reversed` | absent | — |
| ARIS | +2.29 | — | — | `no_close` | absent | — |
| BUUU | -2.29 | — | — | `no_close` | absent | — |
| CRML | +2.29 | — | — | `no_close` | absent | — |
| TMUS | -2.29 | — | +2.37 | `reversed` | absent | — |
| VAL | -2.28 | — | -10.08 | `extended` | absent | — |
| CAMT | -2.26 | — | — | `no_close` | absent | — |
| AAOI | +2.24 | — | -9.49 | `reversed` | absent | — |
| VZ | -2.24 | — | +0.72 | `reversed` | absent | — |
| AEIS | +2.23 | — | -2.19 | `reversed` | absent | — |
| VICR | +2.23 | — | -8.44 | `reversed` | absent | — |
| BTDR | +2.22 | — | — | `no_close` | absent | — |
| OUST | +2.22 | — | -5.11 | `reversed` | absent | — |
| IAG | +2.20 | — | — | `no_close` | absent | — |
| TBBK | +2.14 | — | -1.24 | `reversed` | absent | — |
| TXG | +2.13 | — | -12.10 | `reversed` | absent | — |
| GLW | +2.12 | — | -0.09 | `faded` | absent | — |
| PPTA | +2.10 | — | -3.00 | `reversed` | absent | — |
| APLD | +2.09 | — | -8.95 | `reversed` | absent | — |
| LSCC | +2.09 | — | +2.66 | `extended` | absent | — |
| SBET | +2.08 | — | -3.71 | `reversed` | absent | — |
| SMTC | +2.06 | — | -3.92 | `reversed` | absent | — |
| ERO | +2.03 | — | — | `no_close` | absent | — |
| PARR | -2.03 | — | -5.35 | `extended` | absent | — |
| DDOG | +2.02 | — | -8.15 | `reversed` | absent | — |

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

