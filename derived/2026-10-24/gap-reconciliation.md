# Gap reconciliation — 2026-10-24 pre-market vs the settled close

**Source:** derived join over `earnings/2026-10-24-reactions.md` and `no settled file` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 52 PRE_GAP name(s) tagged at the 2026-10-24 pre-market fire · read-only

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
>    - No settled EOD file for 2026-10-24 (`us-eod/<date>.csv`) - the fire landed on a day with no settled US session, so no name can be given a settled close and every row is `no_close`.
>    - **Session base unverified.** The morning file's `Close` column matches no settled session's closes above 50% (best: 2026-10-23 at 4%, 2 of 54 names compared). The labels in this artifact rest on an unverified base and should not be read as firm.
>    - No settled file, so no open-gap column.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `no_close` | 52 | no settled row for this name in the session file |
| **total** | **52** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-10-24` |
| Prior session (the `Close` column) | `2026-10-23` |
| Settled session joined to | `—` |
| Prior-session match rate | 4% (2 of 54) |
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
| LKQ | -19.94 | — | — | `no_close` | absent | — |
| CCI | +17.20 | — | — | `no_close` | absent | — |
| RNG | +14.58 | — | — | `no_close` | absent | — |
| RHI | +12.74 | — | — | `no_close` | absent | — |
| AMT | +11.25 | — | — | `no_close` | absent | — |
| SBAC | +10.76 | — | — | `no_close` | absent | — |
| GNTX | -8.46 | — | — | `no_close` | absent | — |
| TNGX | -8.20 | — | — | `no_close` | absent | — |
| CRDO | -7.23 | — | — | `no_close` | absent | — |
| KNSL | -7.07 | — | — | `no_close` | absent | — |
| BE | -6.78 | — | — | `no_close` | absent | — |
| FLG | -6.64 | — | — | `no_close` | absent | — |
| SIGI | +5.73 | — | — | `no_close` | absent | — |
| DECK | -5.55 | — | — | `no_close` | absent | — |
| TMUS | -5.55 | — | — | `no_close` | absent | — |
| FIX | -5.42 | — | — | `no_close` | absent | — |
| SLM | -5.24 | — | — | `no_close` | absent | — |
| CHRD | -5.02 | — | — | `no_close` | absent | — |
| RITM | +4.78 | — | — | `no_close` | absent | — |
| KN | +4.52 | — | — | `no_close` | absent | — |
| BHVN | +4.49 | — | — | `no_close` | absent | — |
| ORIC | -4.48 | — | — | `no_close` | absent | — |
| T | -4.44 | — | — | `no_close` | absent | — |
| RDN | +4.03 | — | — | `no_close` | absent | — |
| FCNCA | +3.83 | — | — | `no_close` | absent | — |
| VZ | -3.76 | — | — | `no_close` | absent | — |
| ALV | -3.57 | — | — | `no_close` | absent | — |
| GE | -3.24 | — | — | `no_close` | absent | — |
| SEZL | -3.24 | — | — | `no_close` | absent | — |
| MRNA | -3.18 | — | — | `no_close` | absent | — |
| AXP | -3.12 | — | — | `no_close` | absent | — |
| PCVX | -3.04 | — | — | `no_close` | absent | — |
| NEM | -3.02 | — | — | `no_close` | absent | — |
| ACN | -2.93 | — | — | `no_close` | absent | — |
| SAM | -2.92 | — | — | `no_close` | absent | — |
| CECO | -2.81 | — | — | `no_close` | absent | — |
| ONON | -2.79 | — | — | `no_close` | absent | — |
| MTG | +2.74 | — | — | `no_close` | absent | — |
| HWM | -2.67 | — | — | `no_close` | absent | — |
| INTR | +2.52 | — | — | `no_close` | absent | — |
| CCL | -2.51 | — | — | `no_close` | absent | — |
| AAL | -2.46 | — | — | `no_close` | absent | — |
| NN | +2.39 | — | — | `no_close` | absent | — |
| WDC | -2.30 | — | — | `no_close` | absent | — |
| CNXC | -2.28 | — | — | `no_close` | absent | — |
| BIRK | -2.23 | — | — | `no_close` | absent | — |
| MLTX | -2.19 | — | — | `no_close` | absent | — |
| SPCX | +2.18 | — | — | `no_close` | absent | — |
| FLO | -2.10 | — | — | `no_close` | absent | — |
| VC | -2.06 | — | — | `no_close` | absent | — |
| STX | -2.05 | — | — | `no_close` | absent | — |
| RCL | -2.04 | — | — | `no_close` | absent | — |

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

