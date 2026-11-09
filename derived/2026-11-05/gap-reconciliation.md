# Gap reconciliation — 2026-11-05 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-05-reactions.md` and `us-eod/2026-11-05.csv` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 164 PRE_GAP name(s) tagged at the 2026-11-05 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 95% (133 of 140 names): the morning
>    file's `Close` column matches the `2026-11-04` settled closes, so the morning gap
>    resolves into the `2026-11-05` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 24 of 164 PRE_GAP name(s) have no settled row in the 2026-11-05 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4516 of 4896 rows, so `Open gap %` is blank wherever the session file has no open.
>    - The 2026-11-05 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 96 | same sign, settled move larger than the morning gap |
| `held` | 5 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 10 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 29 | opposite sign, settled move at least 0.5pp |
| `no_close` | 24 | no settled row for this name in the session file |
| **total** | **164** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-05` |
| Prior session (the `Close` column) | `2026-11-04` |
| Settled session joined to | `2026-11-05` |
| Prior-session match rate | 95% (133 of 140) |
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
| SEZL | +29.49 | — | +13.40 | `faded` | sourced | US-listed |
| APP | +21.47 | — | +31.04 | `extended` | sourced | US-listed |
| LYNX | +20.98 | — | +20.77 | `held` | sourced | US-listed |
| TRIP | -20.69 | — | -27.65 | `extended` | sourced | US-listed |
| FOUR | -15.19 | — | -4.51 | `faded` | sourced | US-listed |
| ALNT | +13.35 | — | -5.13 | `reversed` | not_looked_up | US-listed |
| ZG | -11.95 | — | -9.40 | `held` | not_looked_up | US-listed |
| LMAT | -10.41 | — | -5.04 | `faded` | not_looked_up | US-listed |
| QCOM | -10.39 | — | -9.49 | `held` | not_looked_up | US-listed |
| MELI | -8.67 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| Z | -8.55 | — | -10.65 | `extended` | not_looked_up | US-listed |
| ENOV | +8.52 | — | +17.20 | `extended` | not_looked_up | US-listed |
| PH | +7.67 | — | -1.97 | `reversed` | not_looked_up | US-listed |
| VCEL | +7.50 | — | +13.85 | `extended` | not_looked_up | US-listed |
| ARHS | -7.30 | — | -1.60 | `faded` | not_looked_up | US-listed |
| EXPE | -7.25 | — | -13.74 | `extended` | not_looked_up | US-listed |
| MXL | -7.25 | — | -22.06 | `extended` | not_looked_up | US-listed |
| NVAX | +7.04 | — | -8.17 | `reversed` | not_looked_up | US-listed |
| BUUU | -7.00 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| RGC | +6.57 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| SNDK | -6.32 | — | -22.26 | `extended` | not_looked_up | US-listed |
| AEHR | -6.31 | — | -19.20 | `extended` | not_looked_up | US-listed |
| LIME | +6.31 | — | -0.27 | `faded` | not_looked_up | US-listed |
| OUST | -6.05 | — | -9.00 | `extended` | not_looked_up | US-listed |
| AXTI | -5.97 | — | -22.76 | `extended` | not_looked_up | US-listed |
| SMTC | -5.79 | — | -17.50 | `extended` | not_looked_up | US-listed |
| ACCV | -5.73 | — | -15.00 | `extended` | not_looked_up | US-listed |
| VICR | -5.70 | — | -15.07 | `extended` | not_looked_up | US-listed |
| BE | -5.64 | — | -16.41 | `extended` | not_looked_up | US-listed |
| FORM | -5.62 | — | -15.81 | `extended` | not_looked_up | US-listed |
| PLPC | -5.58 | — | -11.63 | `extended` | not_looked_up | US-listed |
| EROC | -5.52 | — | -16.37 | `extended` | not_looked_up | US-listed |
| DELL | -5.33 | — | -14.96 | `extended` | not_looked_up | US-listed |
| CIEN | -5.21 | — | -15.22 | `extended` | not_looked_up | US-listed |
| ICHR | -5.07 | — | -16.85 | `extended` | not_looked_up | US-listed |
| LRCX | -4.90 | — | -16.36 | `extended` | not_looked_up | US-listed |
| PENG | -4.86 | — | -23.02 | `extended` | not_looked_up | US-listed |
| STX | -4.86 | — | -16.25 | `extended` | not_looked_up | US-listed |
| UCTT | -4.86 | — | -15.53 | `extended` | not_looked_up | US-listed |
| NVTS | -4.82 | — | -15.76 | `extended` | not_looked_up | US-listed |
| STRL | -4.82 | — | -13.86 | `extended` | not_looked_up | US-listed |
| OGC | +4.77 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| WDC | -4.77 | — | -17.35 | `extended` | not_looked_up | US-listed |
| LITE | -4.72 | — | -18.68 | `extended` | not_looked_up | US-listed |
| AMAT | -4.71 | — | -13.58 | `extended` | not_looked_up | US-listed |
| IREN | -4.69 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| FLEX | -4.62 | — | — | `no_close` | not_looked_up | US-listed |
| TTMI | -4.61 | — | -15.21 | `extended` | not_looked_up | US-listed |
| AMD | -4.56 | — | -17.26 | `extended` | not_looked_up | US-listed |
| MU | -4.55 | — | -17.46 | `extended` | not_looked_up | US-listed |
| FIX | -4.51 | — | -11.58 | `extended` | not_looked_up | US-listed |
| COHU | -4.50 | — | -20.65 | `extended` | not_looked_up | US-listed |
| CRDO | -4.48 | — | -17.71 | `extended` | not_looked_up | US-listed (ADR) |
| MRVL | -4.41 | — | -16.43 | `extended` | not_looked_up | US-listed |
| AAOI | -4.40 | — | -20.89 | `extended` | not_looked_up | US-listed |
| LGN | -4.28 | — | -20.92 | `extended` | not_looked_up | US-listed |
| ALGM | -4.26 | — | -14.24 | `extended` | not_looked_up | US-listed |
| KGS | +4.22 | — | -5.65 | `reversed` | not_looked_up | US-listed |
| FPS | -4.19 | — | -18.85 | `extended` | not_looked_up | US-listed |
| CIFR | -4.14 | — | -14.62 | `extended` | not_looked_up | US-listed |
| NVT | -4.12 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ULCC | +4.09 | — | +0.42 | `faded` | not_looked_up | US-listed |
| TPL | +4.07 | — | -5.38 | `reversed` | not_looked_up | US-listed |
| DXPE | -4.02 | — | -16.11 | `extended` | not_looked_up | US-listed |
| TER | -3.98 | — | -15.24 | `extended` | not_looked_up | US-listed |
| NET | -3.92 | — | -8.28 | `extended` | not_looked_up | US-listed |
| BELFB | -3.87 | — | -9.88 | `extended` | not_looked_up | US-listed |
| NBIS | -3.87 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| KLAC | -3.84 | — | -13.33 | `extended` | not_looked_up | US-listed |
| VRT | -3.81 | — | -14.02 | `extended` | not_looked_up | US-listed |
| CRWV | -3.80 | — | -9.83 | `extended` | not_looked_up | US-listed |
| APLD | -3.78 | — | -14.69 | `extended` | not_looked_up | US-listed |
| AMBQ | -3.71 | — | -15.21 | `extended` | not_looked_up | US-listed |
| GEV | -3.64 | — | -7.48 | `extended` | not_looked_up | US-listed |
| ANET | -3.63 | — | -10.82 | `extended` | not_looked_up | US-listed |
| MOH | +3.60 | — | -4.32 | `reversed` | not_looked_up | US-listed |
| CLS | -3.56 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| HUT | -3.56 | — | -6.11 | `extended` | not_looked_up | US-listed |
| ONTO | -3.55 | — | -15.60 | `extended` | not_looked_up | US-listed |
| GLW | -3.51 | — | -12.92 | `extended` | not_looked_up | US-listed |
| DOCN | -3.50 | — | -15.85 | `extended` | not_looked_up | US-listed |
| ONDS | -3.42 | — | -14.23 | `extended` | not_looked_up | US-listed |
| OSCR | -3.38 | — | -5.71 | `extended` | not_looked_up | US-listed |
| TSEM | -3.34 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ESLT | -3.33 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| POWL | -3.33 | — | -12.61 | `extended` | not_looked_up | US-listed |
| INIO | -3.32 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| SANM | -3.32 | — | -9.42 | `extended` | not_looked_up | US-listed |
| HCA | +3.22 | — | -0.63 | `reversed` | not_looked_up | US-listed |
| MOD | -3.19 | — | -7.28 | `extended` | not_looked_up | US-listed |
| UBER | +3.18 | — | -1.56 | `reversed` | not_looked_up | US-listed |
| ADI | -3.13 | — | -11.13 | `extended` | not_looked_up | US-listed |
| GLXY | -3.13 | — | -7.09 | `extended` | not_looked_up | US-listed |
| GPGI | -3.13 | — | +6.57 | `reversed` | not_looked_up | US-listed |
| CLMT | +3.10 | — | -0.57 | `reversed` | not_looked_up | US-listed |
| LMND | +3.05 | — | -9.63 | `reversed` | not_looked_up | US-listed |
| CI | +3.03 | — | -1.29 | `reversed` | not_looked_up | US-listed |
| CSCO | -3.00 | — | -7.62 | `extended` | not_looked_up | US-listed |
| LASR | -3.00 | — | -11.06 | `extended` | not_looked_up | US-listed |
| AGX | -2.98 | — | -10.13 | `extended` | not_looked_up | US-listed |
| BELFA | -2.98 | — | -11.15 | `extended` | not_looked_up | US-listed |
| NN | -2.97 | — | -8.33 | `extended` | not_looked_up | US-listed |
| SKE | +2.96 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CNQ | +2.94 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CRWD | -2.91 | — | -9.88 | `extended` | not_looked_up | US-listed |
| TRMB | +2.91 | — | -1.12 | `reversed` | not_looked_up | US-listed |
| WULF | -2.91 | — | -13.85 | `extended` | not_looked_up | US-listed |
| AADX | -2.88 | — | -8.64 | `extended` | not_looked_up | US-listed |
| SNOW | -2.88 | — | -7.25 | `extended` | not_looked_up | US-listed |
| DASH | -2.85 | — | -9.40 | `extended` | not_looked_up | US-listed |
| CDE | -2.84 | — | +0.34 | `faded` | not_looked_up | US-listed |
| ATEC | -2.78 | — | -5.80 | `extended` | not_looked_up | US-listed |
| BTG | +2.74 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CAMT | -2.73 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| NEWP | +2.71 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| IESC | -2.70 | — | -13.89 | `extended` | not_looked_up | US-listed |
| PLTR | -2.70 | — | -9.73 | `extended` | not_looked_up | US-listed |
| INTC | -2.68 | — | -10.33 | `extended` | not_looked_up | US-listed |
| MTRN | +2.66 | — | -5.23 | `reversed` | not_looked_up | US-listed |
| TXN | -2.64 | — | -10.70 | `extended` | not_looked_up | US-listed |
| AVGO | -2.56 | — | -10.43 | `extended` | not_looked_up | US-listed |
| FTAI | -2.55 | — | -9.54 | `extended` | not_looked_up | US-listed |
| APH | -2.54 | — | -9.37 | `extended` | not_looked_up | US-listed |
| RVLV | +2.54 | — | -4.71 | `reversed` | not_looked_up | US-listed |
| TREX | +2.54 | — | -2.00 | `reversed` | not_looked_up | US-listed |
| SPCX | -2.51 | — | -9.05 | `extended` | not_looked_up | US-listed |
| PPLI | +2.50 | — | -2.33 | `reversed` | not_looked_up | US-listed |
| TRUP | +2.45 | — | +3.10 | `extended` | not_looked_up | US-listed |
| SVM | +2.43 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| BWLP | +2.39 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| DOX | +2.38 | — | +0.39 | `faded` | not_looked_up | US-listed |
| DG | +2.37 | — | -2.57 | `reversed` | not_looked_up | US-listed |
| CQP | +2.33 | — | +0.97 | `faded` | not_looked_up | US-listed |
| CEG | -2.31 | — | -2.47 | `held` | not_looked_up | US-listed |
| TSLA | -2.30 | — | -10.77 | `extended` | not_looked_up | US-listed |
| ETN | -2.29 | — | -7.38 | `extended` | not_looked_up | US-listed (ADR) |
| BAC | +2.27 | — | -3.58 | `reversed` | not_looked_up | US-listed |
| COF | +2.27 | — | -1.18 | `reversed` | not_looked_up | US-listed |
| EXK | +2.27 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| HL | +2.27 | — | -3.34 | `reversed` | not_looked_up | US-listed |
| AMZN | +2.26 | — | -2.19 | `reversed` | not_looked_up | US-listed |
| INNV | +2.25 | — | -7.15 | `reversed` | not_looked_up | US-listed |
| COST | +2.20 | — | +1.83 | `held` | not_looked_up | US-listed |
| RIG | +2.20 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| SSMR | +2.20 | — | -3.54 | `reversed` | not_looked_up | US-listed |
| AVAV | -2.19 | — | -9.85 | `extended` | not_looked_up | US-listed |
| ENTG | -2.18 | — | -12.68 | `extended` | not_looked_up | US-listed |
| FTNT | -2.16 | — | -5.32 | `extended` | not_looked_up | US-listed |
| VET | +2.14 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ASST | -2.13 | — | -10.17 | `extended` | not_looked_up | US-listed |
| SNPS | -2.12 | — | -4.89 | `extended` | not_looked_up | US-listed |
| VST | -2.11 | — | -6.15 | `extended` | not_looked_up | US-listed |
| ANDE | +2.10 | — | -0.34 | `faded` | not_looked_up | US-listed |
| NXT | +2.09 | — | -6.67 | `reversed` | not_looked_up | US-listed |
| SM | +2.09 | — | -4.60 | `reversed` | not_looked_up | US-listed |
| RIOT | -2.08 | — | -3.97 | `extended` | not_looked_up | US-listed |
| WMB | +2.08 | — | -5.32 | `reversed` | not_looked_up | US-listed |
| MMYT | +2.07 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| BWXT | -2.06 | — | -5.38 | `extended` | not_looked_up | US-listed |
| CNC | +2.06 | — | -2.42 | `reversed` | not_looked_up | US-listed |
| PL | -2.06 | — | -10.12 | `extended` | not_looked_up | US-listed |
| EQX | +2.04 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| DDOG | -2.03 | — | -7.48 | `extended` | not_looked_up | US-listed |
| HAWK | +2.02 | — | -4.56 | `reversed` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

159 of 164 name(s) carry `not_looked_up`: the morning scanner's own table says
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

