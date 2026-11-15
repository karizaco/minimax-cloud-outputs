# Gap reconciliation — 2026-11-11 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-11-reactions.md` and `us-eod/2026-11-11.csv` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 120 PRE_GAP name(s) tagged at the 2026-11-11 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 100% (101 of 101 names): the morning
>    file's `Close` column matches the `2026-11-10` settled closes, so the morning gap
>    resolves into the `2026-11-11` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 19 of 120 PRE_GAP name(s) have no settled row in the 2026-11-11 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 3782 of 4891 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 43 | same sign, settled move larger than the morning gap |
| `held` | 25 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 14 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 15 | opposite sign, settled move at least 0.5pp |
| `flat` | 4 | settled move under 0.25pp |
| `no_close` | 19 | no settled row for this name in the session file |
| **total** | **120** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-11` |
| Prior session (the `Close` column) | `2026-11-10` |
| Settled session joined to | `2026-11-11` |
| Prior-session match rate | 100% (101 of 101) |
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
| NBIS | +13.11 | — | — | `no_close` | sourced | US-listed (ADR) |
| ATRO | -11.82 | -8.29 | -2.69 | `faded` | sourced | US-listed |
| COHR | +9.66 | +9.78 | +9.27 | `held` | sourced | US-listed |
| NN | +9.64 | +8.48 | +0.60 | `faded` | sourced | US-listed |
| CIFR | +9.49 | +9.34 | +8.88 | `held` | sourced | US-listed |
| AXTI | +9.47 | +9.29 | +19.49 | `extended` | sourced | US-listed |
| MRVL | +8.93 | +8.10 | +9.33 | `extended` | not_looked_up | US-listed |
| STX | +8.83 | +7.99 | +9.99 | `extended` | not_looked_up | US-listed |
| EROC | +8.01 | +6.73 | +12.20 | `extended` | not_looked_up | US-listed |
| FPS | +8.01 | +7.36 | +14.34 | `extended` | not_looked_up | US-listed |
| WDC | +8.00 | +6.60 | +8.33 | `extended` | not_looked_up | US-listed |
| SNDK | +7.88 | +7.93 | +13.69 | `extended` | not_looked_up | US-listed |
| FUN | +7.78 | +9.05 | +9.05 | `extended` | not_looked_up | US-listed |
| BE | +7.32 | — | +13.00 | `extended` | not_looked_up | US-listed |
| CORZ | +7.31 | +5.86 | +10.97 | `extended` | not_looked_up | US-listed |
| DELL | +7.30 | +7.78 | +11.75 | `extended` | not_looked_up | US-listed |
| TTMI | +7.16 | +7.16 | +8.96 | `extended` | not_looked_up | US-listed |
| OKLO | +6.98 | +4.74 | +3.11 | `faded` | not_looked_up | US-listed |
| IREN | +6.96 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AAOI | +6.73 | +6.75 | +15.60 | `extended` | not_looked_up | US-listed |
| GLW | +6.66 | +6.60 | +7.40 | `extended` | not_looked_up | US-listed |
| MU | +6.49 | +7.20 | +11.89 | `extended` | not_looked_up | US-listed |
| CLSK | +6.24 | +6.47 | +5.17 | `held` | not_looked_up | US-listed |
| FN | +6.23 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| KLAC | +6.15 | +5.16 | +5.23 | `held` | not_looked_up | US-listed |
| INTC | +5.98 | +6.28 | +7.47 | `extended` | not_looked_up | US-listed |
| SMR | +5.84 | +5.75 | +0.19 | `flat` | not_looked_up | US-listed |
| ABSI | +5.82 | — | +1.50 | `faded` | not_looked_up | US-listed |
| SANM | +5.78 | +5.21 | +2.51 | `faded` | not_looked_up | US-listed |
| LRCX | +5.76 | +5.93 | +6.07 | `extended` | not_looked_up | US-listed |
| INIO | +5.74 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ONDS | +5.57 | +4.94 | +2.87 | `held` | not_looked_up | US-listed |
| GEV | +5.52 | — | +1.43 | `faded` | not_looked_up | US-listed |
| AMAT | +5.49 | +5.40 | +6.07 | `extended` | not_looked_up | US-listed |
| AMD | +5.48 | +5.42 | +7.32 | `extended` | not_looked_up | US-listed |
| ORCL | +5.15 | +5.34 | +8.81 | `extended` | not_looked_up | US-listed |
| INOD | +5.04 | +4.94 | +8.90 | `extended` | not_looked_up | US-listed |
| TDW | +4.93 | +3.27 | +6.66 | `extended` | not_looked_up | US-listed |
| ANET | +4.89 | +5.30 | +6.32 | `extended` | not_looked_up | US-listed |
| MTZ | +4.79 | +5.92 | +4.59 | `held` | not_looked_up | US-listed |
| RGC | +4.78 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| UEC | +4.74 | +2.79 | +0.91 | `faded` | not_looked_up | US-listed |
| PWR | +4.57 | +5.42 | +4.27 | `held` | not_looked_up | US-listed |
| ACCV | +4.49 | +3.75 | +11.52 | `extended` | not_looked_up | US-listed |
| LEU | +4.47 | +3.09 | +2.00 | `faded` | not_looked_up | US-listed |
| USAR | +4.29 | +4.54 | +4.36 | `held` | not_looked_up | US-listed |
| AVGO | +4.10 | +5.48 | +3.98 | `held` | not_looked_up | US-listed |
| MARA | +4.09 | +4.59 | +4.36 | `extended` | not_looked_up | US-listed |
| AMRC | +3.98 | +1.01 | -4.02 | `reversed` | not_looked_up | US-listed |
| UUUU | +3.86 | +2.08 | +2.82 | `held` | not_looked_up | US-listed |
| IE | +3.79 | +2.22 | -2.48 | `reversed` | not_looked_up | US-listed |
| APH | +3.78 | — | -0.81 | `reversed` | not_looked_up | US-listed |
| CAI | +3.76 | +4.75 | +0.25 | `flat` | not_looked_up | US-listed |
| ETN | +3.75 | +2.79 | +1.78 | `faded` | not_looked_up | US-listed (ADR) |
| ELE | -3.67 | — | — | `no_close` | not_looked_up | US-listed |
| NVDA | +3.57 | +2.25 | +2.84 | `held` | not_looked_up | US-listed |
| NTSK | +3.54 | +3.59 | +4.34 | `extended` | not_looked_up | US-listed |
| QLYS | +3.36 | +3.83 | +4.34 | `extended` | not_looked_up | US-listed |
| QBTS | +3.35 | +4.39 | +1.62 | `faded` | not_looked_up | US-listed |
| FIGR | +3.34 | +2.87 | +3.64 | `extended` | not_looked_up | US-listed |
| BAND | +3.33 | +3.95 | +10.33 | `extended` | not_looked_up | US-listed |
| QCOM | +3.33 | +2.65 | +1.79 | `held` | not_looked_up | US-listed |
| SNOW | +3.22 | +3.92 | +1.86 | `held` | not_looked_up | US-listed |
| SHLS | +3.19 | +0.98 | +8.24 | `extended` | not_looked_up | US-listed |
| CAT | +3.10 | +2.75 | +2.94 | `held` | not_looked_up | US-listed |
| TENB | +3.10 | +3.58 | +2.31 | `held` | not_looked_up | US-listed |
| TXN | +3.09 | +3.39 | +3.10 | `held` | not_looked_up | US-listed |
| EQPT | +3.07 | +3.25 | +18.18 | `extended` | not_looked_up | US-listed |
| FTAI | +3.06 | +2.18 | +1.65 | `held` | not_looked_up | US-listed |
| TEM | +3.05 | +3.24 | -1.38 | `reversed` | not_looked_up | US-listed |
| QUBT | +3.04 | — | -2.06 | `reversed` | not_looked_up | US-listed |
| CRWD | +3.03 | +4.25 | +1.46 | `faded` | not_looked_up | US-listed |
| SECZ | +3.01 | +2.46 | +6.16 | `extended` | not_looked_up | US-listed |
| ASTS | +3.00 | +3.59 | +8.70 | `extended` | not_looked_up | US-listed |
| MRCY | +2.97 | +3.40 | +5.68 | `extended` | not_looked_up | US-listed |
| RGTI | +2.96 | +6.34 | -8.56 | `reversed` | not_looked_up | US-listed |
| PS | +2.94 | — | +0.43 | `faded` | not_looked_up | US-listed |
| LIME | +2.91 | +1.66 | +7.42 | `extended` | not_looked_up | US-listed |
| NEWP | +2.86 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| NTLA | +2.86 | +1.16 | +2.15 | `held` | not_looked_up | US-listed |
| MBLY | +2.84 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CRSP | +2.77 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ADI | +2.72 | +3.28 | +4.02 | `extended` | not_looked_up | US-listed |
| ALM | +2.70 | — | — | `no_close` | not_looked_up | US-listed |
| NET | +2.68 | +3.37 | +2.98 | `extended` | not_looked_up | US-listed |
| NXE | +2.64 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| VOYG | +2.62 | +1.69 | +1.90 | `held` | not_looked_up | US-listed |
| AYA | +2.61 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ALB | +2.60 | +0.60 | +1.07 | `faded` | not_looked_up | US-listed |
| ETOR | +2.58 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| IEP | +2.56 | +1.38 | -1.48 | `reversed` | not_looked_up | US-listed |
| HYMC | +2.54 | +0.42 | -0.90 | `reversed` | not_looked_up | US-listed |
| ROAD | +2.49 | +2.42 | +2.93 | `extended` | not_looked_up | US-listed |
| SEDG | +2.47 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ENPH | +2.46 | +1.70 | +2.39 | `held` | not_looked_up | US-listed |
| WPM | +2.45 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| XP | +2.40 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| FROG | +2.37 | +4.73 | +5.70 | `extended` | not_looked_up | US-listed |
| PLTR | +2.36 | +2.67 | +2.13 | `held` | not_looked_up | US-listed |
| SVM | +2.36 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| PANW | +2.34 | +3.49 | +2.48 | `held` | not_looked_up | US-listed |
| QNT | +2.33 | +2.33 | -5.65 | `reversed` | not_looked_up | US-listed |
| NXT | +2.32 | +0.58 | +0.78 | `faded` | not_looked_up | US-listed |
| SA | +2.30 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| PGY | +2.27 | +1.28 | +0.17 | `flat` | not_looked_up | US-listed |
| PBF | +2.26 | +2.94 | +5.81 | `extended` | not_looked_up | US-listed |
| JOBY | +2.20 | +1.52 | -0.93 | `reversed` | not_looked_up | US-listed |
| IBKR | +2.17 | — | +6.32 | `extended` | not_looked_up | US-listed |
| CRK | +2.15 | +2.98 | +4.92 | `extended` | not_looked_up | US-listed |
| FCX | +2.14 | +2.14 | +3.02 | `extended` | not_looked_up | US-listed |
| AAON | +2.12 | +1.75 | +1.76 | `held` | not_looked_up | US-listed |
| AUGO | +2.08 | +1.25 | +0.11 | `flat` | not_looked_up | US-listed |
| XXI | +2.07 | +0.75 | -1.13 | `reversed` | not_looked_up | US-listed |
| IAG | +2.05 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| INGM | +2.04 | +1.57 | +2.04 | `held` | not_looked_up | US-listed |
| REPL | +2.04 | +0.00 | -6.44 | `reversed` | not_looked_up | US-listed |
| CDE | +2.03 | +0.65 | -1.64 | `reversed` | not_looked_up | US-listed |
| HL | +2.03 | +0.70 | -1.12 | `reversed` | not_looked_up | US-listed |
| REGN | -2.03 | -1.21 | +4.73 | `reversed` | not_looked_up | US-listed |
| SRPT | +2.01 | +0.06 | +1.58 | `held` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

114 of 120 name(s) carry `not_looked_up`: the morning scanner's own table says
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

