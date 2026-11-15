# Gap reconciliation — 2026-11-12 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-12-reactions.md` and `us-eod/2026-11-12.csv` (neither source is modified) · **Built:** 2026-11-15 · **Covers:** 115 PRE_GAP name(s) tagged at the 2026-11-12 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 96% (95 of 99 names): the morning
>    file's `Close` column matches the `2026-11-11` settled closes, so the morning gap
>    resolves into the `2026-11-12` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 16 of 115 PRE_GAP name(s) have no settled row in the 2026-11-12 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 3751 of 4893 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 27 | same sign, settled move larger than the morning gap |
| `held` | 27 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 33 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 11 | opposite sign, settled move at least 0.5pp |
| `flat` | 1 | settled move under 0.25pp |
| `no_close` | 16 | no settled row for this name in the session file |
| **total** | **115** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-12` |
| Prior session (the `Close` column) | `2026-11-11` |
| Settled session joined to | `2026-11-12` |
| Prior-session match rate | 96% (95 of 99) |
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
| EYE | -16.09 | +0.11 | +2.65 | `reversed` | sourced | US-listed |
| DPC | +13.64 | — | — | `no_close` | sourced | US-listed (ADR) |
| AVEX | +11.29 | +12.53 | +13.44 | `extended` | sourced | US-listed |
| TTEK | +10.77 | +10.34 | +4.84 | `faded` | sourced | US-listed |
| EROC | -9.98 | -13.93 | -5.61 | `held` | sourced | US-listed |
| CRWV | -9.45 | -16.26 | -6.86 | `held` | not_looked_up | US-listed |
| NBIS | -9.11 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| YETI | -8.62 | -6.97 | -10.38 | `extended` | not_looked_up | US-listed |
| TWST | -8.23 | -18.77 | -6.85 | `held` | not_looked_up | US-listed |
| NVDA | -7.56 | -13.07 | -4.32 | `held` | not_looked_up | US-listed |
| SNDK | -6.00 | -9.16 | -4.11 | `held` | not_looked_up | US-listed |
| AXTI | -5.98 | -9.30 | -7.30 | `extended` | not_looked_up | US-listed |
| FPS | -5.98 | -13.48 | -9.77 | `extended` | not_looked_up | US-listed |
| AAOI | -5.96 | -8.36 | -5.39 | `held` | not_looked_up | US-listed |
| SMCI | -5.75 | -10.65 | -11.30 | `extended` | not_looked_up | US-listed |
| EQPT | -5.62 | -1.94 | -3.50 | `held` | not_looked_up | US-listed |
| ASST | -5.60 | -7.84 | -4.09 | `held` | not_looked_up | US-listed |
| CIFR | -5.54 | -7.88 | +0.56 | `reversed` | not_looked_up | US-listed |
| IREN | -5.52 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| PURR | -5.42 | -7.65 | -3.77 | `held` | not_looked_up | US-listed |
| BMNR | -5.15 | -7.54 | -4.05 | `held` | not_looked_up | US-listed |
| APLD | -5.08 | -7.15 | -5.36 | `extended` | not_looked_up | US-listed |
| HUT | -5.03 | -5.47 | +1.51 | `reversed` | not_looked_up | US-listed |
| COHR | -4.92 | -8.78 | -1.02 | `faded` | not_looked_up | US-listed |
| GLXY | -4.82 | -7.26 | -4.95 | `held` | not_looked_up | US-listed |
| MXL | -4.81 | -7.39 | -1.65 | `faded` | not_looked_up | US-listed |
| CORZ | -4.80 | -5.22 | -1.30 | `faded` | not_looked_up | US-listed |
| PENG | -4.77 | -5.64 | +1.73 | `reversed` | not_looked_up | US-listed |
| CLSK | -4.63 | — | -1.01 | `faded` | not_looked_up | US-listed |
| LGN | +4.48 | -1.91 | -2.21 | `reversed` | not_looked_up | US-listed |
| CRDO | -4.46 | -6.44 | -1.13 | `faded` | not_looked_up | US-listed (ADR) |
| WULF | -4.42 | -4.94 | -2.40 | `held` | not_looked_up | US-listed |
| MU | -4.31 | -5.18 | -1.59 | `faded` | not_looked_up | US-listed |
| LITE | -4.24 | -8.49 | -3.61 | `held` | not_looked_up | US-listed |
| MANE | -4.20 | — | -13.55 | `extended` | not_looked_up | US-listed |
| WOLF | -4.19 | -6.94 | -3.94 | `held` | not_looked_up | US-listed |
| ALAB | -4.17 | -6.67 | -1.34 | `faded` | not_looked_up | US-listed |
| BTDR | -4.13 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| STX | -4.06 | -3.93 | -1.20 | `faded` | not_looked_up | US-listed |
| WDC | -4.04 | -4.05 | -0.67 | `faded` | not_looked_up | US-listed |
| AEHR | -4.03 | -6.61 | -7.21 | `extended` | not_looked_up | US-listed |
| SECZ | -3.97 | -7.34 | -7.34 | `extended` | not_looked_up | US-listed |
| DELL | -3.93 | — | -0.64 | `faded` | not_looked_up | US-listed |
| HIMS | -3.89 | -6.01 | -5.19 | `extended` | not_looked_up | US-listed |
| ACMR | -3.84 | -5.19 | -4.86 | `extended` | not_looked_up | US-listed |
| AMBQ | -3.83 | — | -3.47 | `held` | not_looked_up | US-listed |
| CIEN | -3.83 | -4.93 | -0.61 | `faded` | not_looked_up | US-listed |
| TTMI | -3.81 | -6.56 | -3.08 | `held` | not_looked_up | US-listed |
| BE | -3.78 | -6.49 | -3.58 | `held` | not_looked_up | US-listed |
| NVTS | -3.67 | -6.36 | -5.07 | `extended` | not_looked_up | US-listed |
| MRVL | -3.64 | -6.69 | -2.55 | `held` | not_looked_up | US-listed |
| TH | +3.56 | +0.68 | +1.52 | `faded` | not_looked_up | US-listed |
| VIAV | -3.54 | -4.67 | -1.39 | `faded` | not_looked_up | US-listed |
| SMCIP | -3.41 | — | — | `no_close` | not_looked_up | US-listed |
| SEI | -3.33 | -5.02 | -0.40 | `faded` | not_looked_up | US-listed |
| COHU | -3.32 | -4.87 | -2.13 | `held` | not_looked_up | US-listed |
| SITM | -3.21 | -4.44 | -0.42 | `faded` | not_looked_up | US-listed |
| ECO | -3.19 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ENTG | -3.19 | -4.93 | -0.65 | `faded` | not_looked_up | US-listed |
| ORCL | -3.18 | -3.97 | -1.01 | `faded` | not_looked_up | US-listed |
| FUN | +3.15 | -1.08 | +1.08 | `faded` | not_looked_up | US-listed |
| RMBS | -3.09 | -4.32 | -0.46 | `faded` | not_looked_up | US-listed |
| INOD | -3.07 | -4.74 | -4.92 | `extended` | not_looked_up | US-listed |
| DOCN | -3.04 | -5.78 | +3.31 | `reversed` | not_looked_up | US-listed |
| HPE | -3.04 | -5.25 | -0.12 | `flat` | not_looked_up | US-listed |
| GLW | -3.01 | -5.73 | -0.66 | `faded` | not_looked_up | US-listed |
| MKSI | -3.01 | -4.91 | -1.99 | `held` | not_looked_up | US-listed |
| ONTO | -2.98 | -6.14 | -2.46 | `held` | not_looked_up | US-listed |
| QNT | -2.97 | -4.46 | -7.67 | `extended` | not_looked_up | US-listed |
| INTC | -2.96 | -4.48 | -2.03 | `held` | not_looked_up | US-listed |
| TER | -2.93 | -5.00 | -0.75 | `faded` | not_looked_up | US-listed |
| ASTS | -2.91 | -5.22 | -5.79 | `extended` | not_looked_up | US-listed |
| VSH | -2.88 | -4.33 | -4.57 | `extended` | not_looked_up | US-listed |
| CLS | -2.85 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| P | -2.85 | -3.29 | +3.48 | `reversed` | not_looked_up | US-listed |
| ALGM | -2.83 | -4.24 | -1.25 | `faded` | not_looked_up | US-listed |
| AMKR | -2.81 | -4.51 | -2.57 | `held` | not_looked_up | US-listed |
| BLSH | -2.80 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| KLAC | -2.80 | -3.23 | -2.30 | `held` | not_looked_up | US-listed |
| ZETA | -2.78 | -3.31 | -1.27 | `faded` | not_looked_up | US-listed |
| LRCX | -2.77 | -3.39 | -0.89 | `faded` | not_looked_up | US-listed |
| FRVO | -2.70 | -4.71 | -9.97 | `extended` | not_looked_up | US-listed |
| NET | -2.70 | -2.73 | +1.18 | `reversed` | not_looked_up | US-listed |
| UCTT | -2.70 | -6.23 | -3.08 | `extended` | not_looked_up | US-listed |
| FORM | -2.69 | -5.63 | -3.61 | `extended` | not_looked_up | US-listed |
| MPWR | -2.68 | -3.04 | -2.16 | `held` | not_looked_up | US-listed |
| FLY | -2.67 | -1.62 | -4.88 | `extended` | not_looked_up | US-listed |
| VRT | -2.67 | -4.31 | +1.55 | `reversed` | not_looked_up | US-listed |
| INIO | -2.65 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| FIX | -2.64 | -1.98 | -2.93 | `extended` | not_looked_up | US-listed |
| PARR | +2.56 | +0.32 | +1.12 | `faded` | not_looked_up | US-listed |
| PBF | +2.54 | +0.06 | +1.79 | `held` | not_looked_up | US-listed |
| RKLB | -2.53 | -3.52 | -3.14 | `extended` | not_looked_up | US-listed |
| FN | -2.51 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AEM | -2.49 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AMAT | -2.48 | -4.00 | -3.57 | `extended` | not_looked_up | US-listed |
| EGO | -2.45 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ICHR | -2.43 | -6.49 | -1.01 | `faded` | not_looked_up | US-listed |
| LLY | +2.42 | +0.63 | -0.56 | `reversed` | not_looked_up | US-listed |
| STRL | -2.33 | -3.49 | -0.76 | `faded` | not_looked_up | US-listed |
| FSLY | -2.32 | -3.94 | -0.41 | `faded` | not_looked_up | US-listed |
| PDFS | -2.32 | -3.21 | -2.75 | `extended` | not_looked_up | US-listed |
| PLPC | -2.32 | — | -2.39 | `held` | not_looked_up | US-listed |
| GFS | -2.31 | — | -0.54 | `faded` | not_looked_up | US-listed |
| TSEM | -2.28 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| GNRC | -2.22 | — | -0.67 | `faded` | not_looked_up | US-listed |
| NEWP | -2.22 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| TRAX | -2.22 | -3.15 | -3.62 | `extended` | not_looked_up | US-listed |
| CBRS | -2.21 | -4.22 | -3.31 | `extended` | not_looked_up | US-listed |
| ON | -2.21 | -2.98 | +0.15 | `faded` | not_looked_up | US-listed |
| POWI | -2.13 | -2.13 | -0.92 | `faded` | not_looked_up | US-listed |
| FROG | -2.11 | -2.28 | +1.00 | `reversed` | not_looked_up | US-listed |
| NEM | -2.08 | -2.95 | -4.89 | `extended` | not_looked_up | US-listed |
| NVMI | -2.08 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| EQX | -2.04 | — | — | `no_close` | not_looked_up | US-listed (ADR) |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

110 of 115 name(s) carry `not_looked_up`: the morning scanner's own table says
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

