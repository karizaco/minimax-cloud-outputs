# Gap reconciliation — 2026-10-26 pre-market vs the settled close

**Source:** derived join over `earnings/2026-10-26-reactions.md` and `us-eod/2026-10-26.csv` (neither source is modified) · **Built:** 2026-11-11 · **Covers:** 33 PRE_GAP name(s) tagged at the 2026-10-26 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **This date's base is UNVERIFIED — treat every label as provisional.**
>    See *Session resolution* below for the match rate that failed.
> 4. **Deviations and degraded paths.**
>    - **Session base unverified.** The morning file's `Close` column matches no settled session's closes above 50% (best: 2026-10-23 at 3%, 1 of 33 names compared). The labels in this artifact rest on an unverified base and should not be read as firm.
>    - The 2026-10-26 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 11 | same sign, settled move larger than the morning gap |
| `held` | 7 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 4 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 9 | opposite sign, settled move at least 0.5pp |
| `flat` | 2 | settled move under 0.25pp |
| **total** | **33** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-10-26` |
| Prior session (the `Close` column) | `2026-10-23` |
| Settled session joined to | `2026-10-26` |
| Prior-session match rate | 3% (1 of 33) |
| Verified | **no** |

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
| XP | -47.65 | — | -47.68 | `held` | absent | — |
| INTR | -37.13 | — | -35.33 | `held` | absent | — |
| AGBK | -21.50 | — | -38.19 | `extended` | absent | — |
| MELI | -14.49 | — | -8.14 | `held` | absent | — |
| RRC | +10.83 | — | +17.25 | `extended` | absent | — |
| MRNA | -8.05 | — | -1.31 | `faded` | absent | — |
| ADPT | -6.00 | — | +2.55 | `reversed` | absent | — |
| CLS | +3.87 | — | -3.35 | `reversed` | absent | — |
| PBLS | +3.72 | — | +3.25 | `held` | absent | — |
| MRVI | -3.55 | — | +2.39 | `reversed` | absent | — |
| SDRL | -3.17 | — | -1.50 | `faded` | absent | — |
| SMTC | +3.03 | — | +4.48 | `extended` | absent | — |
| RGC | +2.83 | — | -12.65 | `reversed` | absent | — |
| FORM | +2.53 | — | +3.29 | `extended` | absent | — |
| APA | -2.49 | — | -0.21 | `flat` | absent | — |
| MU | +2.49 | — | +3.45 | `extended` | absent | — |
| WGS | +2.49 | — | +9.03 | `extended` | absent | — |
| MGM | +2.46 | — | +1.64 | `held` | absent | — |
| TDW | -2.41 | — | -1.91 | `held` | absent | — |
| AVBP | +2.38 | — | -28.07 | `reversed` | absent | — |
| TSLA | +2.38 | — | +5.71 | `extended` | absent | — |
| VG | -2.36 | — | -1.04 | `faded` | absent | — |
| SNDK | +2.33 | — | +1.99 | `held` | absent | — |
| BTDR | -2.30 | — | +3.74 | `reversed` | absent | — |
| NN | -2.28 | — | +14.29 | `reversed` | absent | — |
| ATEN | -2.27 | — | +2.28 | `reversed` | absent | — |
| KLAC | +2.24 | — | +2.97 | `extended` | absent | — |
| ORIC | -2.20 | — | -31.47 | `extended` | absent | — |
| PSX | -2.18 | — | +1.84 | `reversed` | absent | — |
| BE | +2.15 | — | +6.26 | `extended` | absent | — |
| COHU | +2.15 | — | +2.44 | `extended` | absent | — |
| DVN | -2.14 | — | +0.38 | `faded` | absent | — |
| SM | -2.08 | — | -0.16 | `flat` | absent | — |

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

