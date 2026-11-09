# Gap reconciliation — 2026-11-06 pre-market vs the settled close

**Source:** derived join over `earnings/2026-11-06-reactions.md` and `us-eod/2026-11-06.csv` (neither source is modified) · **Built:** 2026-11-09 · **Covers:** 198 PRE_GAP name(s) tagged at the 2026-11-06 pre-market fire · read-only

> **Read this before the table.**
> 
> 1. **These labels describe the session path, not a trade.** `held`, `faded`,
>    `reversed`, `extended` and `flat` say what the price did between the morning
>    quote and the settled close. This artifact states no direction and no size.
> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move
>    against the prior session's close; `Settled chg %` is the 16:00 ET close
>    against that same close. They are directly comparable — the subtraction a
>    reader would otherwise do across three files is done here.
> 3. **Session resolution is verified** at 99% (178 of 179 names): the morning
>    file's `Close` column matches the `2026-11-05` settled closes, so the morning gap
>    resolves into the `2026-11-06` session.
> 4. **Deviations and degraded paths.**
>    - 4 duplicate ticker key(s) on the settled side; the first row wins.
>    - 19 of 198 PRE_GAP name(s) have no settled row in the 2026-11-06 session file and are labelled `no_close` rather than dropped.
>    - The settled file publishes an `open` for 4160 of 4892 rows, so `Open gap %` is blank wherever the session file has no open.

## Outcome counts

| Outcome | Names | What the label means |
|---|---|---|
| `extended` | 78 | same sign, settled move larger than the morning gap |
| `held` | 49 | same sign, settled move kept at least 50% of the gap's magnitude |
| `faded` | 39 | same sign but under that share, or an opposite sign under 0.5pp |
| `reversed` | 12 | opposite sign, settled move at least 0.5pp |
| `flat` | 1 | settled move under 0.25pp |
| `no_close` | 19 | no settled row for this name in the session file |
| **total** | **198** | |

The counts are a distribution of session paths, not a scorecard. A high `faded`
count means opening moves were given back that day; it does not mean the morning
scan was wrong, and a `reversed` row is not a failure of the routine that found
it. What a reader should **not** conclude from this table is anything about
tradeability: the artifact knows the open and the close, and nothing about the
path between them or whether either price was reachable.

## Session resolution

| Field | Value |
|---|---|
| Fire date | `2026-11-06` |
| Prior session (the `Close` column) | `2026-11-05` |
| Settled session joined to | `2026-11-06` |
| Prior-session match rate | 99% (178 of 179) |
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
| FROG | +22.96 | +27.30 | +35.33 | `extended` | sourced | US-listed |
| NET | +18.86 | — | +9.89 | `held` | sourced | US-listed |
| LASR | +16.56 | +25.70 | +29.58 | `extended` | sourced | US-listed |
| IREN | +16.03 | — | — | `no_close` | sourced | US-listed (ADR) |
| VCEL | +15.86 | +0.12 | +5.49 | `faded` | sourced | US-listed |
| ABNB | +14.32 | +12.64 | +11.67 | `held` | not_looked_up | US-listed |
| DIOD | +12.93 | +9.17 | +13.17 | `held` | not_looked_up | US-listed |
| CIFR | +11.53 | +13.15 | +17.93 | `extended` | not_looked_up | US-listed |
| FLY | +11.30 | +12.65 | +36.80 | `extended` | not_looked_up | US-listed |
| SITM | +11.28 | +14.68 | +17.44 | `extended` | not_looked_up | US-listed |
| LRCX | +10.96 | +12.85 | +8.23 | `held` | not_looked_up | US-listed |
| INOD | +10.82 | +5.26 | -4.12 | `reversed` | not_looked_up | US-listed |
| CRDO | +10.20 | +11.04 | +7.28 | `held` | not_looked_up | US-listed (ADR) |
| BE | +9.96 | +9.43 | +3.40 | `faded` | not_looked_up | US-listed |
| NBIS | +9.86 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| ICHR | +9.70 | +9.85 | +10.47 | `extended` | not_looked_up | US-listed |
| SNDK | +9.62 | +11.40 | +3.55 | `faded` | not_looked_up | US-listed |
| APLD | +9.53 | +9.31 | +9.74 | `held` | not_looked_up | US-listed |
| PENG | +9.52 | +12.09 | +12.39 | `extended` | not_looked_up | US-listed |
| MRVL | +9.46 | +8.61 | +5.73 | `held` | not_looked_up | US-listed |
| UCTT | +9.46 | +9.52 | +10.56 | `extended` | not_looked_up | US-listed |
| COHR | +9.38 | +11.79 | +13.74 | `extended` | not_looked_up | US-listed |
| MXL | +9.33 | +10.52 | +10.99 | `extended` | not_looked_up | US-listed |
| LITE | +9.28 | +8.04 | +5.67 | `held` | not_looked_up | US-listed |
| CECO | +9.24 | — | — | `no_close` | not_looked_up | US-listed |
| ONTO | +8.99 | +12.12 | +11.08 | `extended` | not_looked_up | US-listed |
| AEHR | +8.87 | +11.27 | +8.97 | `held` | not_looked_up | US-listed |
| TSEM | +8.82 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| FORM | +8.75 | +11.83 | +13.04 | `extended` | not_looked_up | US-listed |
| AXTI | +8.74 | +8.52 | +5.88 | `held` | not_looked_up | US-listed |
| TER | +8.50 | +9.87 | +2.57 | `faded` | not_looked_up | US-listed |
| ALAB | +8.41 | — | +6.26 | `held` | not_looked_up | US-listed |
| VICR | +8.32 | +9.25 | +8.72 | `extended` | not_looked_up | US-listed |
| FPS | +8.18 | +7.91 | +6.81 | `held` | not_looked_up | US-listed |
| FSLY | +8.13 | +9.62 | +3.06 | `faded` | not_looked_up | US-listed |
| SEI | +8.09 | +7.97 | +14.26 | `extended` | not_looked_up | US-listed |
| IONQ | +8.02 | +5.98 | +23.16 | `extended` | not_looked_up | US-listed |
| PLPC | +7.93 | +7.78 | +3.95 | `faded` | not_looked_up | US-listed |
| DELL | +7.92 | +9.25 | +3.76 | `faded` | not_looked_up | US-listed |
| WULF | +7.84 | +10.62 | +12.80 | `extended` | not_looked_up | US-listed |
| AMAT | +7.82 | +8.46 | +4.22 | `held` | not_looked_up | US-listed |
| CHRN | +7.78 | +10.73 | +5.81 | `held` | not_looked_up | US-listed |
| FN | +7.76 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| AMD | +7.74 | +9.79 | +11.04 | `extended` | not_looked_up | US-listed |
| ACMR | +7.73 | +9.39 | +13.48 | `extended` | not_looked_up | US-listed |
| MTSI | +7.73 | +8.77 | +10.84 | `extended` | not_looked_up | US-listed |
| SMTC | +7.60 | +11.32 | +12.75 | `extended` | not_looked_up | US-listed |
| AMKR | +7.58 | +9.54 | +7.64 | `held` | not_looked_up | US-listed |
| STX | +7.50 | +8.36 | -1.19 | `reversed` | not_looked_up | US-listed |
| COHU | +7.48 | +10.37 | +10.29 | `extended` | not_looked_up | US-listed |
| TTMI | +7.46 | +10.90 | +6.89 | `held` | not_looked_up | US-listed |
| OKLO | +7.40 | +10.52 | +22.73 | `extended` | not_looked_up | US-listed |
| WDC | +7.27 | +7.36 | -1.44 | `reversed` | not_looked_up | US-listed |
| VRT | +7.24 | +7.81 | +3.46 | `faded` | not_looked_up | US-listed |
| MU | +7.23 | +7.91 | +5.12 | `held` | not_looked_up | US-listed |
| STRL | +7.23 | +7.86 | +3.47 | `faded` | not_looked_up | US-listed |
| ALGM | +7.09 | — | +5.11 | `held` | not_looked_up | US-listed |
| CIEN | +7.01 | +9.53 | +5.30 | `held` | not_looked_up | US-listed |
| CLS | +6.98 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| RMBS | +6.92 | +9.00 | +6.96 | `held` | not_looked_up | US-listed |
| HPE | +6.91 | — | +1.54 | `faded` | not_looked_up | US-listed |
| FLEX | +6.86 | — | — | `no_close` | not_looked_up | US-listed |
| KLAC | +6.85 | +8.24 | +6.70 | `held` | not_looked_up | US-listed |
| GENB | +6.84 | +2.62 | +3.90 | `held` | not_looked_up | US-listed |
| P | +6.70 | +9.43 | +3.60 | `held` | not_looked_up | US-listed |
| CORZ | +6.68 | +6.77 | +3.34 | `faded` | not_looked_up | US-listed |
| FRVO | +6.68 | +6.03 | +15.85 | `extended` | not_looked_up | US-listed |
| EROC | +6.63 | +6.63 | +7.23 | `extended` | not_looked_up | US-listed |
| BTDR | +6.51 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| KLIC | +6.47 | — | — | `no_close` | not_looked_up | US-listed |
| DOCN | +6.44 | +10.89 | +2.55 | `faded` | not_looked_up | US-listed |
| RBRK | +6.44 | +4.54 | -0.00 | `faded` | not_looked_up | US-listed |
| FIX | +6.38 | +7.78 | +5.44 | `held` | not_looked_up | US-listed |
| CHTR | -6.25 | -8.10 | -6.19 | `held` | not_looked_up | US-listed |
| VSAT | +6.10 | +3.22 | +7.70 | `extended` | not_looked_up | US-listed |
| CLSK | +5.93 | +7.57 | +8.45 | `extended` | not_looked_up | US-listed |
| VSH | +5.90 | +5.31 | +5.75 | `held` | not_looked_up | US-listed |
| GLW | +5.87 | +5.22 | +2.59 | `faded` | not_looked_up | US-listed |
| MNST | -5.86 | -8.01 | -4.41 | `held` | not_looked_up | US-listed |
| NVTS | +5.86 | +7.12 | +9.54 | `extended` | not_looked_up | US-listed |
| IESC | +5.78 | +7.55 | +8.84 | `extended` | not_looked_up | US-listed |
| MPWR | +5.63 | +6.10 | +5.22 | `held` | not_looked_up | US-listed |
| WOLF | +5.60 | +6.48 | +16.85 | `extended` | not_looked_up | US-listed |
| AEIS | +5.57 | +7.70 | +6.11 | `extended` | not_looked_up | US-listed |
| ANET | +5.55 | +8.54 | +7.31 | `extended` | not_looked_up | US-listed |
| INFQ | +5.38 | +5.24 | +19.49 | `extended` | not_looked_up | US-listed |
| ADEA | +5.26 | +3.91 | +4.59 | `held` | not_looked_up | US-listed |
| MARA | +5.20 | +5.70 | +8.09 | `extended` | not_looked_up | US-listed |
| LBRT | +5.17 | +5.46 | +5.37 | `held` | not_looked_up | US-listed |
| POWL | +5.15 | +6.47 | +6.39 | `extended` | not_looked_up | US-listed |
| VIAV | +5.09 | +6.27 | +8.25 | `extended` | not_looked_up | US-listed |
| BELFA | +5.00 | +4.59 | +6.09 | `extended` | not_looked_up | US-listed |
| LUNR | +4.99 | +5.68 | +21.46 | `extended` | not_looked_up | US-listed |
| SNOW | +4.96 | +3.90 | +2.34 | `faded` | not_looked_up | US-listed |
| CBRS | +4.92 | +4.89 | +9.75 | `extended` | not_looked_up | US-listed |
| NVT | +4.90 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| INTC | +4.88 | +5.22 | +7.71 | `extended` | not_looked_up | US-listed |
| ENTG | +4.85 | +4.65 | +2.59 | `held` | not_looked_up | US-listed |
| IPGP | +4.79 | +5.30 | +5.29 | `extended` | not_looked_up | US-listed |
| XE | +4.78 | +6.89 | +15.89 | `extended` | not_looked_up | US-listed |
| CRWD | +4.77 | +6.21 | -0.14 | `faded` | not_looked_up | US-listed |
| SPCX | +4.69 | +6.07 | +8.62 | `extended` | not_looked_up | US-listed |
| PWR | +4.68 | +5.97 | +6.23 | `extended` | not_looked_up | US-listed |
| RKLB | +4.59 | +4.96 | +15.39 | `extended` | not_looked_up | US-listed |
| U | +4.51 | +4.78 | +5.51 | `extended` | not_looked_up | US-listed |
| AAOI | +4.50 | +4.52 | +6.91 | `extended` | not_looked_up | US-listed |
| AVGO | +4.49 | +6.72 | +0.74 | `faded` | not_looked_up | US-listed |
| ERAS | +4.47 | +1.13 | +8.59 | `extended` | not_looked_up | US-listed |
| RGTI | +4.26 | +4.67 | +19.29 | `extended` | not_looked_up | US-listed |
| AMPX | +4.24 | +4.39 | +15.96 | `extended` | not_looked_up | US-listed |
| CGNX | +4.22 | +3.58 | +0.60 | `faded` | not_looked_up | US-listed |
| GRAL | +4.09 | +2.44 | +1.94 | `faded` | not_looked_up | US-listed |
| VOYG | +4.08 | +4.62 | +17.95 | `extended` | not_looked_up | US-listed |
| PANW | +4.07 | +4.86 | -0.26 | `faded` | not_looked_up | US-listed |
| LGN | +4.05 | +4.68 | +9.84 | `extended` | not_looked_up | US-listed |
| NVDA | +4.04 | +5.23 | +2.77 | `held` | not_looked_up | US-listed |
| QBTS | +3.98 | +5.16 | +18.01 | `extended` | not_looked_up | US-listed |
| TXG | -3.98 | -0.29 | +2.10 | `reversed` | not_looked_up | US-listed |
| ETN | +3.97 | +5.66 | +4.51 | `extended` | not_looked_up | US-listed (ADR) |
| ON | +3.95 | +5.65 | +0.48 | `faded` | not_looked_up | US-listed |
| QUBT | +3.91 | +3.82 | +12.43 | `extended` | not_looked_up | US-listed |
| APH | +3.78 | +5.07 | +4.12 | `extended` | not_looked_up | US-listed |
| PRIM | +3.74 | +3.58 | +9.79 | `extended` | not_looked_up | US-listed |
| RDW | +3.71 | +5.01 | +16.40 | `extended` | not_looked_up | US-listed |
| GENI | -3.70 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| LIFE | +3.67 | +1.17 | +2.73 | `held` | not_looked_up | US-listed |
| CAI | +3.65 | +1.46 | -3.07 | `reversed` | not_looked_up | US-listed |
| VISN | +3.61 | +1.94 | +1.67 | `faded` | not_looked_up | US-listed |
| VYX | -3.45 | -1.72 | -1.17 | `faded` | not_looked_up | US-listed |
| ADP | -3.35 | -3.45 | -1.23 | `faded` | not_looked_up | US-listed |
| SPOT | -3.34 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| TXN | +3.32 | +1.87 | -0.28 | `faded` | not_looked_up | US-listed |
| SMMT | +3.24 | +4.23 | +15.08 | `extended` | not_looked_up | US-listed |
| ABSI | +3.19 | +4.69 | +8.31 | `extended` | not_looked_up | US-listed |
| VERX | -3.18 | -4.61 | -2.90 | `held` | not_looked_up | US-listed |
| DGII | +3.14 | +2.87 | +1.40 | `faded` | not_looked_up | US-listed |
| PI | +3.07 | +4.28 | +6.19 | `extended` | not_looked_up | US-listed |
| GOOGN | +3.05 | — | — | `no_close` | not_looked_up | US-listed |
| ADI | +3.04 | — | +0.71 | `faded` | not_looked_up | US-listed |
| POWI | +3.04 | +5.10 | +3.66 | `extended` | not_looked_up | US-listed |
| RVMD | +3.01 | +4.11 | +8.23 | `extended` | not_looked_up | US-listed |
| AZN | -2.99 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| OKTA | +2.99 | +3.04 | -1.44 | `reversed` | not_looked_up | US-listed |
| CEG | +2.95 | +2.63 | +4.30 | `extended` | not_looked_up | US-listed |
| CMCSA | -2.93 | -3.05 | -2.24 | `held` | not_looked_up | US-listed |
| SLS | +2.92 | +1.90 | +6.85 | `extended` | not_looked_up | US-listed |
| SEZL | -2.91 | +0.13 | -3.59 | `extended` | not_looked_up | US-listed |
| ORCL | +2.90 | — | +0.87 | `faded` | not_looked_up | US-listed |
| ARDT | -2.89 | -0.38 | +8.74 | `reversed` | not_looked_up | US-listed |
| GEV | +2.86 | +3.46 | +0.47 | `faded` | not_looked_up | US-listed |
| ADBE | -2.80 | -3.00 | -2.90 | `held` | not_looked_up | US-listed |
| RYN | -2.78 | -1.46 | -1.64 | `held` | not_looked_up | US-listed |
| QCOM | +2.77 | +3.06 | +5.53 | `extended` | not_looked_up | US-listed |
| BAM | +2.74 | — | — | `no_close` | not_looked_up | US-listed |
| CRCT | -2.70 | -2.92 | -5.08 | `extended` | not_looked_up | US-listed |
| DASH | -2.69 | -0.33 | -0.14 | `flat` | not_looked_up | US-listed |
| MDLZ | -2.68 | -2.89 | -1.20 | `faded` | not_looked_up | US-listed |
| FTNT | +2.64 | — | -3.00 | `reversed` | not_looked_up | US-listed |
| UPBD | +2.57 | -1.53 | -2.57 | `reversed` | not_looked_up | US-listed |
| ACN | -2.56 | -2.53 | -1.77 | `held` | not_looked_up | US-listed (ADR) |
| NWS | +2.52 | +0.00 | -0.03 | `faded` | not_looked_up | US-listed |
| IBKR | +2.50 | +1.99 | +4.25 | `extended` | not_looked_up | US-listed |
| TGLS | -2.50 | — | — | `no_close` | not_looked_up | US-listed |
| PEP | -2.46 | -3.08 | -0.96 | `faded` | not_looked_up | US-listed |
| BMY | -2.44 | -2.65 | -1.58 | `held` | not_looked_up | US-listed |
| CRM | -2.43 | -2.56 | -3.93 | `extended` | not_looked_up | US-listed |
| SYK | -2.43 | -3.19 | -2.77 | `extended` | not_looked_up | US-listed |
| CAT | +2.42 | +3.31 | +0.86 | `faded` | not_looked_up | US-listed |
| HD | -2.41 | -2.63 | -1.85 | `held` | not_looked_up | US-listed |
| NFLX | -2.41 | -2.65 | -3.28 | `extended` | not_looked_up | US-listed |
| ROK | +2.41 | +1.65 | -1.38 | `reversed` | not_looked_up | US-listed |
| MO | -2.40 | -3.12 | -1.89 | `held` | not_looked_up | US-listed |
| PFE | -2.39 | -2.71 | -1.64 | `held` | not_looked_up | US-listed |
| LYNX | +2.37 | +2.21 | +28.66 | `extended` | not_looked_up | US-listed |
| MOS | -2.37 | -1.48 | +0.09 | `faded` | not_looked_up | US-listed |
| WS | -2.37 | — | +2.34 | `reversed` | not_looked_up | US-listed |
| WMT | -2.36 | -3.13 | -1.72 | `held` | not_looked_up | US-listed |
| JCI | +2.31 | +2.43 | +2.67 | `extended` | not_looked_up | US-listed (ADR) |
| MRNA | +2.29 | +1.70 | +5.27 | `extended` | not_looked_up | US-listed |
| SHW | -2.24 | -2.38 | -1.42 | `held` | not_looked_up | US-listed |
| RACE | -2.21 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| CL | -2.20 | -3.44 | -2.17 | `held` | not_looked_up | US-listed |
| USB | +2.18 | -1.17 | -0.50 | `faded` | not_looked_up | US-listed |
| V | -2.17 | -1.92 | +0.03 | `faded` | not_looked_up | US-listed |
| PRDO | +2.15 | +5.80 | +1.24 | `held` | not_looked_up | US-listed |
| KKR | -2.14 | -0.83 | -1.83 | `held` | not_looked_up | US-listed |
| IBRX | +2.12 | +2.00 | +7.80 | `extended` | not_looked_up | US-listed |
| MA | -2.12 | -2.07 | -0.50 | `faded` | not_looked_up | US-listed |
| RELY | +2.11 | +2.23 | +3.60 | `extended` | not_looked_up | US-listed |
| LIN | -2.10 | -1.98 | -1.15 | `held` | not_looked_up | US-listed (ADR) |
| PM | -2.08 | -1.89 | -1.82 | `held` | not_looked_up | US-listed |
| INTU | -2.07 | -2.51 | -3.76 | `extended` | not_looked_up | US-listed |
| MCD | -2.06 | -2.88 | -0.58 | `faded` | not_looked_up | US-listed |
| SEDG | +2.06 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| TTAM | +2.05 | -1.54 | -3.55 | `reversed` | not_looked_up | US-listed (ADR) |
| AMGN | -2.04 | -2.80 | +0.03 | `faded` | not_looked_up | US-listed |
| AGI | -2.03 | — | — | `no_close` | not_looked_up | US-listed (ADR) |
| PLTR | +2.01 | +2.45 | +3.48 | `extended` | not_looked_up | US-listed |

`Open gap %` is the official 09:30 open against the prior close, taken from the
settled file's own `gap_pct` where it publishes one. It sits between the two
other columns in time, and where it differs sharply from `Pre-mkt %` the move
happened between the morning quote and the opening auction.

### Catalyst coverage

193 of 198 name(s) carry `not_looked_up`: the morning scanner's own table says
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

