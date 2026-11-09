# Gap reconciliation — 2026-11-04 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-04-reactions.md` and `us-eod/2026-11-04.csv` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 171 PRE_GAP name(s) tagged at the 2026-11-04 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 95% (140 of 147 names): the morning
>    file's `Close` column matches the `2026-11-03` settled closes, so the morning gap
>    resolves into the `2026-11-04` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 24 of 171 PRE_GAP name(s) have no settled row in the 2026-11-04 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4342 of 4895 rows, so `Open gap %` is blank wherever the session file has no open.
>    - The 2026-11-04 session file carries no `gap_pct` column (only the newest one does), so the `Open gap %` column is empty for this date.
>    - This reactions file predates the `Catalyst` column, so catalyst coverage cannot be reported for it.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 95 | same sign, settled move larger than the morning gap |
| `held` | 22 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 10 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 20 | opposite sign, settled move at least 0.5pp |
| `no_close` | 24 | no settled row for this name in the session file |
| **total** | **171** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-04` |
| Prior session (the `Close` column) | `2026-11-03` |
| Settled session joined to | `2026-11-04` |
| Prior-session match rate | 95% (140 of 147) |
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
| DUOL | +19.51 | — | +25.99 | `extended` | absent | — |
| CBLL | -15.53 | — | -3.11 | `faded` | absent | — |
| CIFR | -15.52 | — | -19.95 | `extended` | absent | — |
| SEDG | -14.39 | — | — | `no_close` | absent | — |
| NVTS | +12.73 | — | +9.00 | `held` | absent | — |
| KD | +11.67 | — | +30.06 | `extended` | absent | — |
| DJT | -11.03 | — | -24.54 | `extended` | absent | — |
| FIX | -11.01 | — | -15.22 | `extended` | absent | — |
| HUT | -10.90 | — | -23.23 | `extended` | absent | — |
| LIME | -9.54 | — | -27.83 | `extended` | absent | — |
| OSCR | +9.53 | — | +8.58 | `held` | absent | — |
| CLSK | -9.13 | — | -16.56 | `extended` | absent | — |
| VSH | +8.30 | — | -5.00 | `reversed` | absent | — |
| AUGO | +8.25 | — | +12.92 | `extended` | absent | — |
| GLXY | -7.84 | — | -16.99 | `extended` | absent | — |
| SPCX | -7.39 | — | -3.81 | `held` | absent | — |
| ECG | -7.30 | — | -29.29 | `extended` | absent | — |
| VRT | -7.09 | — | -12.88 | `extended` | absent | — |
| CRWV | -6.96 | — | -9.90 | `extended` | absent | — |
| STRL | -6.96 | — | -21.46 | `extended` | absent | — |
| BTDR | -6.94 | — | — | `no_close` | absent | — |
| CGAU | +6.86 | — | — | `no_close` | absent | — |
| RAL | +6.72 | — | +0.36 | `faded` | absent | — |
| CORZ | -6.60 | — | -10.39 | `extended` | absent | — |
| IREN | -6.46 | — | — | `no_close` | absent | — |
| GEV | -6.45 | — | -9.30 | `extended` | absent | — |
| CGEM | -6.35 | — | -20.70 | `extended` | absent | — |
| SEI | -6.30 | — | -16.92 | `extended` | absent | — |
| SHLS | +6.26 | — | +8.15 | `extended` | absent | — |
| AEM | +6.24 | — | — | `no_close` | absent | — |
| NXT | +6.23 | — | +11.12 | `extended` | absent | — |
| APLD | -6.18 | — | -6.74 | `extended` | absent | — |
| ELE | +6.16 | — | — | `no_close` | absent | — |
| KGC | +6.13 | — | — | `no_close` | absent | — |
| FLNC | +5.87 | — | +10.18 | `extended` | absent | — |
| HCA | +5.86 | — | +10.39 | `extended` | absent | — |
| TSLA | -5.77 | — | -3.34 | `held` | absent | — |
| FPS | -5.75 | — | -17.34 | `extended` | absent | — |
| LDOS | -5.73 | — | +0.75 | `reversed` | absent | — |
| SMG | +5.66 | — | +8.75 | `extended` | absent | — |
| NEM | +5.64 | — | +9.94 | `extended` | absent | — |
| MARA | -5.59 | — | -4.05 | `held` | absent | — |
| ANET | +5.35 | — | +5.05 | `held` | absent | — |
| PWR | -5.18 | — | -11.67 | `extended` | absent | — |
| INIO | -4.97 | — | — | `no_close` | absent | — |
| RUN | +4.94 | — | +1.27 | `faded` | absent | — |
| WULF | -4.87 | — | -6.62 | `extended` | absent | — |
| TLN | -4.84 | — | -8.54 | `extended` | absent | — |
| CRDO | -4.83 | — | -9.55 | `extended` | absent | — |
| PLTR | -4.79 | — | -2.11 | `faded` | absent | — |
| LZ | +4.78 | — | +3.14 | `held` | absent | — |
| ETN | -4.77 | — | -9.99 | `extended` | absent | — |
| SEZL | +4.72 | — | +11.65 | `extended` | absent | — |
| POWL | -4.71 | — | -12.39 | `extended` | absent | — |
| ZG | +4.66 | — | +9.89 | `extended` | absent | — |
| UBS | +4.65 | — | — | `no_close` | absent | — |
| NVT | -4.53 | — | — | `no_close` | absent | — |
| DELL | -4.51 | — | -9.06 | `extended` | absent | — |
| SNOW | -4.50 | — | -1.50 | `faded` | absent | — |
| ORCL | -4.46 | — | -1.92 | `faded` | absent | — |
| CEG | -4.39 | — | -6.71 | `extended` | absent | — |
| NBIS | -4.37 | — | — | `no_close` | absent | — |
| SNDX | +4.32 | — | -26.87 | `reversed` | absent | — |
| NYT | +4.29 | — | -0.94 | `reversed` | absent | — |
| NET | -4.25 | — | -2.49 | `held` | absent | — |
| XPEL | -4.07 | — | -0.85 | `faded` | absent | — |
| DHI | +3.97 | — | +8.13 | `extended` | absent | — |
| ERO | +3.94 | — | — | `no_close` | absent | — |
| LEN | +3.86 | — | +7.07 | `extended` | absent | — |
| LKQ | +3.84 | — | +8.72 | `extended` | absent | — |
| AGX | -3.80 | — | -16.54 | `extended` | absent | — |
| INBX | -3.76 | — | +7.01 | `reversed` | absent | — |
| PHM | +3.64 | — | +7.20 | `extended` | absent | — |
| OC | -3.62 | — | +8.51 | `reversed` | absent | — |
| FCX | +3.61 | — | +1.38 | `faded` | absent | — |
| SCCO | +3.60 | — | +1.97 | `held` | absent | — |
| AMZN | +3.56 | — | +6.12 | `extended` | absent | — |
| ULCC | +3.55 | — | +9.58 | `extended` | absent | — |
| VERX | -3.47 | — | +4.33 | `reversed` | absent | — |
| CLS | -3.44 | — | — | `no_close` | absent | — |
| AMGN | +3.41 | — | +3.73 | `extended` | absent | — |
| BMRN | +3.41 | — | +2.64 | `held` | absent | — |
| MMM | +3.36 | — | +9.57 | `extended` | absent | — |
| LMT | -3.34 | — | -6.95 | `extended` | absent | — |
| FLEX | -3.33 | — | — | `no_close` | absent | — |
| AMRZ | +3.31 | — | +5.15 | `extended` | absent | — |
| LBTYA | +3.29 | — | — | `no_close` | absent | — |
| SRAD | +3.27 | — | — | `no_close` | absent | — |
| CCEP | +3.23 | — | — | `no_close` | absent | — |
| ISRG | +3.23 | — | +9.38 | `extended` | absent | — |
| SHW | +3.19 | — | +6.64 | `extended` | absent | — |
| RTX | -3.10 | — | -2.63 | `held` | absent | — |
| PFGC | +3.00 | — | +13.63 | `extended` | absent | — |
| WDC | -2.97 | — | -6.77 | `extended` | absent | — |
| CVS | -2.91 | — | -12.54 | `extended` | absent | — |
| TH | -2.90 | — | -22.08 | `extended` | absent | — |
| RH | +2.89 | — | +8.14 | `extended` | absent | — |
| WCC | -2.88 | — | -9.88 | `extended` | absent | — |
| RCUS | +2.86 | — | +2.04 | `held` | absent | — |
| SOLS | +2.85 | — | -6.54 | `reversed` | absent | — |
| T | +2.85 | — | +2.15 | `held` | absent | — |
| AEHR | -2.83 | — | -6.56 | `extended` | absent | — |
| LEN.B | +2.81 | — | +6.22 | `extended` | absent | — |
| HD | +2.80 | — | +6.54 | `extended` | absent | — |
| EROC | -2.79 | — | -11.44 | `extended` | absent | — |
| BE | -2.76 | — | -6.38 | `extended` | absent | — |
| MRNA | +2.75 | — | +13.11 | `extended` | absent | — |
| RRX | -2.74 | — | -3.62 | `extended` | absent | — |
| ALK | +2.73 | — | +8.75 | `extended` | absent | — |
| INTC | -2.73 | — | -3.77 | `extended` | absent | — |
| Z | +2.68 | — | +9.43 | `extended` | absent | — |
| TMUS | +2.65 | — | +3.08 | `extended` | absent | — |
| GILD | +2.63 | — | +4.19 | `extended` | absent | — |
| MRVL | -2.62 | — | -7.08 | `extended` | absent | — |
| ALHC | +2.58 | — | +10.15 | `extended` | absent | — |
| FRVO | +2.58 | — | -4.51 | `reversed` | absent | — |
| AXTI | -2.57 | — | -7.38 | `extended` | absent | — |
| VZ | +2.56 | — | +2.06 | `held` | absent | — |
| BFLY | +2.53 | — | +5.78 | `extended` | absent | — |
| IP | +2.51 | — | +1.52 | `held` | absent | — |
| BUUU | -2.44 | — | — | `no_close` | absent | — |
| NEE | +2.44 | — | +4.87 | `extended` | absent | — |
| ABNB | +2.42 | — | +5.64 | `extended` | absent | — |
| STDN | +2.42 | — | -1.89 | `reversed` | absent | — |
| TRV | +2.42 | — | +3.51 | `extended` | absent | — |
| WGS | +2.42 | — | +1.02 | `faded` | absent | — |
| CAT | -2.41 | — | -5.26 | `extended` | absent | — |
| SMMT | +2.41 | — | +2.34 | `held` | absent | — |
| STX | -2.40 | — | -8.13 | `extended` | absent | — |
| SYK | +2.40 | — | +9.41 | `extended` | absent | — |
| DRTS | +2.36 | — | — | `no_close` | absent | — |
| AMRC | +2.33 | — | -4.58 | `reversed` | absent | — |
| GD | -2.33 | — | -2.57 | `held` | absent | — |
| UNH | -2.33 | — | +1.20 | `reversed` | absent | — |
| FN | -2.29 | — | — | `no_close` | absent | — |
| FTRE | +2.29 | — | -0.57 | `reversed` | absent | — |
| ADP | +2.28 | — | +2.54 | `extended` | absent | — |
| MSFT | +2.28 | — | +6.68 | `extended` | absent | — |
| TWST | +2.28 | — | +1.63 | `held` | absent | — |
| MCD | +2.27 | — | +6.58 | `extended` | absent | — |
| INTU | +2.26 | — | +3.46 | `extended` | absent | — |
| MYRG | -2.26 | — | -9.50 | `extended` | absent | — |
| WLK | +2.23 | — | -0.81 | `reversed` | absent | — |
| MPC | -2.22 | — | -8.13 | `extended` | absent | — |
| PAGS | +2.22 | — | — | `no_close` | absent | — |
| ENPH | +2.20 | — | +3.71 | `extended` | absent | — |
| IT | +2.19 | — | +1.40 | `held` | absent | — |
| JNJ | +2.19 | — | +3.81 | `extended` | absent | — |
| MAR | +2.19 | — | +2.04 | `held` | absent | — |
| WMT | +2.19 | — | +3.45 | `extended` | absent | — |
| MOS | -2.17 | — | +17.35 | `reversed` | absent | — |
| BX | +2.16 | — | +6.25 | `extended` | absent | — |
| CRM | +2.16 | — | +2.23 | `held` | absent | — |
| EMR | -2.16 | — | +2.35 | `reversed` | absent | — |
| LOW | +2.16 | — | +7.54 | `extended` | absent | — |
| RVTY | +2.15 | — | -2.50 | `reversed` | absent | — |
| CRCL | -2.14 | — | +1.26 | `reversed` | absent | — |
| REGN | +2.12 | — | -4.39 | `reversed` | absent | — |
| TJX | +2.11 | — | +5.18 | `extended` | absent | — |
| ABT | +2.10 | — | +5.61 | `extended` | absent | — |
| GLW | -2.10 | — | -5.83 | `extended` | absent | — |
| LLY | +2.10 | — | +0.59 | `faded` | absent | — |
| WRBY | +2.10 | — | -3.05 | `reversed` | absent | — |
| AXP | +2.09 | — | +2.21 | `held` | absent | — |
| IBTA | +2.07 | — | +3.79 | `extended` | absent | — |
| CNQ | -2.04 | — | — | `no_close` | absent | — |
| DIS | +2.03 | — | +4.18 | `extended` | absent | — |
| AZN | +2.02 | — | — | `no_close` | absent | — |
| PLPC | -2.02 | — | -8.45 | `extended` | absent | — |
| BAX | +2.00 | — | +3.92 | `extended` | absent | — |
| MGA | +2.00 | — | — | `no_close` | absent | — |

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

