# Gap reconciliation — 2026-10-29 pre-market vs the settled close

**Source:** derived join over `earnings/2026-10-29-reactions.md` and `us-eod/2026-10-29.csv` (neither source is modified) · **Built:** 2026-11-10 · **Covers:** 124 PRE_GAP name(s) tagged at the 2026-10-29 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 90% (95 of 105 names): the morning
>    file's `Close` column matches the `2026-10-28` settled closes, so the morning gap
>    resolves into the `2026-10-29` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 19 of 124 PRE_GAP name(s) have no settled row in the 2026-10-29 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4258 of 4899 rows, so `Open gap %` is blank wherever the session file has no open.
>    - The 2026-10-29 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 38 | same sign, settled move larger than the morning gap |
| `held` | 33 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 19 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 15 | opposite sign, settled move at least 0.5pp |
| `no_close` | 19 | no settled row for this name in the session file |
| **total** | **124** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-10-29` |
| Prior session (the `Close` column) | `2026-10-28` |
| Settled session joined to | `2026-10-29` |
| Prior-session match rate | 90% (95 of 105) |
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
| FTNT | -26.04 | — | -20.09 | `held` | absent | — |
| SFM | -23.06 | — | -22.58 | `held` | absent | — |
| PRCH | +20.61 | — | +28.16 | `extended` | absent | — |
| NOW | -19.81 | — | -26.97 | `extended` | absent | — |
| TDOC | +14.10 | — | +26.82 | `extended` | absent | — |
| MRVL | -11.38 | — | -13.24 | `extended` | absent | — |
| GOOGL | -11.30 | — | -12.64 | `extended` | absent | — |
| GOOG | -11.06 | — | -12.29 | `extended` | absent | — |
| COHU | +9.69 | — | +0.49 | `faded` | absent | — |
| CAT | -9.34 | — | -9.27 | `held` | absent | — |
| BHC | +8.09 | — | — | `no_close` | absent | — |
| NVCR | +7.54 | — | — | `no_close` | absent | — |
| INIO | -7.36 | — | — | `no_close` | absent | — |
| FTRE | -7.34 | — | -10.61 | `extended` | absent | — |
| GOOGN | -7.23 | — | — | `no_close` | absent | — |
| GOOGM | -7.21 | — | — | `no_close` | absent | — |
| AXTI | -7.19 | — | -5.44 | `held` | absent | — |
| CRWD | -6.94 | — | -2.07 | `faded` | absent | — |
| PANW | -6.84 | — | -3.53 | `held` | absent | — |
| NBIS | -6.70 | — | — | `no_close` | absent | — |
| CRWV | -6.54 | — | -4.99 | `held` | absent | — |
| TYL | -6.27 | — | +3.54 | `reversed` | absent | — |
| CRM | -6.24 | — | -4.61 | `held` | absent | — |
| FTAI | +6.05 | — | +17.27 | `extended` | absent | — |
| LITE | +5.80 | — | +0.61 | `faded` | absent | — |
| TT | -5.68 | — | -3.89 | `held` | absent | — |
| PWR | +5.62 | — | +4.66 | `held` | absent | — |
| ENTG | +5.45 | — | +0.43 | `faded` | absent | — |
| MYRG | +5.39 | — | +1.10 | `faded` | absent | — |
| STRL | -5.35 | — | -3.91 | `held` | absent | — |
| IREN | -4.93 | — | — | `no_close` | absent | — |
| CIFR | -4.74 | — | -8.68 | `extended` | absent | — |
| NET | -4.62 | — | -2.67 | `held` | absent | — |
| GLXY | -4.61 | — | -5.03 | `extended` | absent | — |
| LLY | +4.46 | — | +6.57 | `extended` | absent | — |
| SDGR | -4.44 | — | -2.85 | `held` | absent | — |
| MOD | -4.42 | — | -3.30 | `held` | absent | — |
| RIOT | -4.36 | — | -4.91 | `extended` | absent | — |
| WOLF | -4.28 | — | -6.38 | `extended` | absent | — |
| HONA | -4.25 | — | -9.60 | `extended` | absent | — |
| WULF | -4.25 | — | -4.99 | `extended` | absent | — |
| APLD | -4.22 | — | -4.81 | `extended` | absent | — |
| BE | -4.20 | — | -2.52 | `held` | absent | — |
| OWL | +4.03 | — | +7.55 | `extended` | absent | — |
| INTU | -4.02 | — | +0.91 | `reversed` | absent | — |
| CRDO | -3.93 | — | -4.84 | `extended` | absent | — |
| RCL | +3.90 | — | +4.06 | `held` | absent | — |
| SNOW | -3.84 | — | -3.05 | `held` | absent | — |
| MARA | -3.83 | — | -2.52 | `held` | absent | — |
| ICHR | -3.78 | — | -1.51 | `faded` | absent | — |
| CORZ | -3.67 | — | -3.80 | `held` | absent | — |
| AMGN | +3.58 | — | +1.97 | `held` | absent | — |
| SEI | -3.58 | — | +0.17 | `faded` | absent | — |
| ADBE | -3.50 | — | -0.66 | `faded` | absent | — |
| ACN | -3.46 | — | +1.59 | `reversed` | absent | — |
| CSTL | +3.46 | — | +4.99 | `extended` | absent | — |
| INOD | -3.42 | — | -3.11 | `held` | absent | — |
| AESI | +3.39 | — | -1.96 | `reversed` | absent | — |
| KLAC | +3.34 | — | +5.45 | `extended` | absent | — |
| VRTX | +3.34 | — | +1.95 | `held` | absent | — |
| BTU | +3.29 | — | -1.29 | `reversed` | absent | — |
| CLS | -3.27 | — | — | `no_close` | absent | — |
| CLSK | -3.27 | — | -4.43 | `extended` | absent | — |
| FLEX | -3.25 | — | — | `no_close` | absent | — |
| ALAB | -3.23 | — | -2.28 | `held` | absent | — |
| GEV | -3.18 | — | +1.16 | `reversed` | absent | — |
| FPS | -3.14 | — | -3.21 | `held` | absent | — |
| INTC | -3.12 | — | -3.62 | `extended` | absent | — |
| DDOG | -3.09 | — | -4.51 | `extended` | absent | — |
| TTMI | -3.07 | — | -3.48 | `extended` | absent | — |
| CMPR | -3.06 | — | — | `no_close` | absent | — |
| VRT | -3.04 | — | +1.24 | `reversed` | absent | — |
| PGY | -3.03 | — | +1.66 | `reversed` | absent | — |
| VIAV | -2.99 | — | -3.31 | `extended` | absent | — |
| TMUS | +2.98 | — | -0.53 | `reversed` | absent | — |
| GILD | +2.94 | — | +4.03 | `extended` | absent | — |
| STX | -2.93 | — | +0.36 | `faded` | absent | — |
| BTDR | -2.90 | — | — | `no_close` | absent | — |
| DB | +2.89 | — | — | `no_close` | absent | — |
| WDC | -2.89 | — | -0.25 | `faded` | absent | — |
| KYMR | -2.87 | — | +0.07 | `faded` | absent | — |
| UCTT | -2.85 | — | -2.11 | `held` | absent | — |
| GLW | -2.82 | — | -1.82 | `held` | absent | — |
| POWL | -2.80 | — | +0.28 | `faded` | absent | — |
| TER | -2.80 | — | -5.43 | `extended` | absent | — |
| TEX | -2.75 | — | +5.96 | `reversed` | absent | — |
| TEM | -2.74 | — | +1.61 | `reversed` | absent | — |
| BEAM | -2.71 | — | +0.21 | `faded` | absent | — |
| FN | -2.67 | — | — | `no_close` | absent | — |
| FRVO | +2.64 | — | +7.92 | `extended` | absent | — |
| MU | -2.58 | — | -4.98 | `extended` | absent | — |
| SAIA | +2.58 | — | +5.68 | `extended` | absent | — |
| ADP | +2.57 | — | +0.25 | `faded` | absent | — |
| IBM | -2.54 | — | +1.97 | `reversed` | absent | — |
| AAOI | -2.53 | — | -3.69 | `extended` | absent | — |
| ON | -2.53 | — | -0.52 | `faded` | absent | — |
| AVGO | -2.49 | — | -1.94 | `held` | absent | — |
| SNDK | -2.49 | — | -5.32 | `extended` | absent | — |
| SHAZ | -2.44 | — | -8.08 | `extended` | absent | — |
| BFLY | +2.43 | — | -3.84 | `reversed` | absent | — |
| AMKR | -2.42 | — | -2.37 | `held` | absent | — |
| GFL | +2.41 | — | — | `no_close` | absent | — |
| MRK | +2.40 | — | +3.85 | `extended` | absent | — |
| AER | +2.36 | — | — | `no_close` | absent | — |
| DELL | -2.31 | — | -3.74 | `extended` | absent | — |
| NTLA | -2.26 | — | -0.68 | `faded` | absent | — |
| AZN | +2.25 | — | — | `no_close` | absent | — |
| BKNG | +2.25 | — | +1.68 | `held` | absent | — |
| MO | +2.25 | — | +5.08 | `extended` | absent | — |
| APPN | -2.23 | — | -2.87 | `extended` | absent | — |
| TTE | +2.22 | — | — | `no_close` | absent | — |
| SBUX | +2.21 | — | +2.24 | `held` | absent | — |
| HPE | -2.20 | — | -2.42 | `held` | absent | — |
| BMY | +2.18 | — | +1.38 | `held` | absent | — |
| ONTO | -2.18 | — | -0.75 | `faded` | absent | — |
| NN | -2.14 | — | -3.59 | `extended` | absent | — |
| AMD | -2.13 | — | -2.08 | `held` | absent | — |
| UBS | +2.12 | — | — | `no_close` | absent | — |
| CBRS | -2.11 | — | +2.31 | `reversed` | absent | — |
| NEO | -2.11 | — | -0.33 | `faded` | absent | — |
| SNPS | -2.11 | — | +1.72 | `reversed` | absent | — |
| CRML | -2.05 | — | — | `no_close` | absent | — |
| MS | +2.04 | — | -0.07 | `faded` | absent | — |
| UEC | -2.03 | — | -2.22 | `held` | absent | — |

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

