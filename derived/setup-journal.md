# Setup journal — next session versus the published close

**Source:** derived join of `daily-screens/<date>/{stalk,tier-a}.csv` to the next `us-eod/<date>.csv` (no routine artifact is modified) · **Built:** 2026-11-10 · **Covers:** 432 published setup-row(s) across 2026-10-22 → 2026-11-06; 432 scored, 0 waiting on a session that has not settled · read-only

> **Read this before the table.**
>
> 1. **This scores a published list. It does not recommend a name.**
>    `held` means the entry session's close kept at least half the open
>    gap's magnitude, in the same direction. It is a path, not a result
>    to copy.
> 2. **The base is the observation close** — the settled close on the day
>    the sweep was published. The entry open and the entry close are both
>    measured against that close, so the two numbers share one clock.
> 3. **A stylist count is not a sample.** Most combinations appear once.
>    The summary below does not rank them. A median over two names is a
>    description, not evidence that the combination works.
> 4. **The combinations are canonical.** A row's stylist list is resolved to the
>    five buckets the skill names — `hernandez`, `jeff_sun`, `peoplewish`,
>    `qullamaggie`, `stockbee` — and sorted, so the group IS the combination
>    rather than the spelling the screen happened to use. The screen publishes
>    these in at least 30 different spellings across the archive (`sun_canslim`,
>    `jeff_sun_canslim`, `Jeff Sun`, `bonde_4pct`, `ADR + velocity`, and the
>    pipe order varies too). Grouped on the raw string, the same combination
>    appears as several rows with medians that contradict each other. The raw
>    label is kept in `setup-journal.csv` as `stylists_raw`, so the mapping can
>    be audited row by row.

## By stylist combination

| Stylists | Scored | Next close up | Next close down | Median next change |
|---|---|---|---|---|
| jeff_sun | 60 | 20 | 34 | -0.49 |
| peoplewish | 60 | 16 | 36 | -1.03 |
| (no stylist column on that date) | 56 | 15 | 33 | -0.66 |
| stockbee | 37 | 18 | 16 | +0.18 |
| jeff_sun|stockbee | 26 | 11 | 11 | -0.08 |
| qullamaggie | 22 | 10 | 11 | -0.49 |
| peoplewish|qullamaggie | 21 | 11 | 10 | +0.66 |
| peoplewish|qullamaggie|stockbee | 19 | 12 | 5 | +2.17 |
| hernandez|peoplewish|qullamaggie | 18 | 8 | 9 | -0.29 |
| jeff_sun|peoplewish|stockbee | 10 | 8 | 2 | +1.02 |
| peoplewish|stockbee | 9 | 6 | 3 | +3.65 |
| hernandez|jeff_sun | 8 | 4 | 4 | -0.10 |
| hernandez|stockbee | 8 | 2 | 5 | -2.35 |
| jeff_sun|peoplewish|qullamaggie | 8 | 1 | 6 | -2.16 |
| hernandez|jeff_sun|stockbee | 7 | 4 | 2 | +1.11 |
| jeff_sun|peoplewish | 7 | 3 | 3 | -0.25 |
| jeff_sun|qullamaggie|stockbee | 6 | 5 | 1 | +2.83 |
| hernandez|peoplewish|qullamaggie|stockbee | 4 | 3 | 0 | +4.67 |
| jeff_sun|peoplewish|qullamaggie|stockbee | 3 | 1 | 2 | -2.40 |
| hernandez|jeff_sun|qullamaggie|stockbee | 2 | 2 | 0 | +4.63 |

Combinations that appear once are omitted from this table and kept in the
row file. Up and down use a 0.25 pp band around zero so a flat close is
neither.

## Every scored setup

| Published | Entry session | Ticker | Boards | Stylists | Entry open gap | Entry close chg | Path |
|---|---|---|---|---|---|---|---|
| 2026-10-22 | 2026-10-23 | AAPL | stalk | — | +1.17 | +1.33 | held |
| 2026-10-22 | 2026-10-23 | ABCL | stalk | — | -4.22 | -6.32 | held |
| 2026-10-22 | 2026-10-23 | AIT | stalk | — | -1.83 | -2.14 | held |
| 2026-10-22 | 2026-10-23 | ALMR | stalk | — | -2.15 | -5.23 | held |
| 2026-10-22 | 2026-10-23 | AMBA | stalk | — | -1.65 | +0.08 | faded |
| 2026-10-22 | 2026-10-23 | AME | stalk | — | -1.30 | -0.77 | held |
| 2026-10-22 | 2026-10-23 | ARX | stalk | — | -0.15 | -0.03 | flat |
| 2026-10-22 | 2026-10-23 | BMNR | stalk | — | -2.12 | +0.17 | faded |
| 2026-10-22 | 2026-10-23 | BRKR | stalk | — | -3.51 | -3.89 | held |
| 2026-10-22 | 2026-10-23 | BWIN | stalk | — | -0.14 | -0.19 | flat |
| 2026-10-22 | 2026-10-23 | CEG | stalk | — | -2.74 | -3.51 | held |
| 2026-10-22 | 2026-10-23 | CELH | stalk | — | -1.14 | +0.77 | reversed |
| 2026-10-22 | 2026-10-23 | CLMT | stalk | — | -6.09 | -6.60 | held |
| 2026-10-22 | 2026-10-23 | CWEN | stalk | — | -0.32 | +0.22 | faded |
| 2026-10-22 | 2026-10-23 | DDOG | stalk | — | -2.88 | -2.35 | held |
| 2026-10-22 | 2026-10-23 | ECHO | stalk | — | -4.75 | -3.02 | held |
| 2026-10-22 | 2026-10-23 | FROG | stalk | — | -1.45 | -1.32 | held |
| 2026-10-22 | 2026-10-23 | FRPT | stalk | — | +4.31 | +1.76 | faded |
| 2026-10-22 | 2026-10-23 | FWDI | stalk | — | -1.97 | -1.05 | held |
| 2026-10-22 | 2026-10-23 | GNRC | stalk | — | -2.33 | -2.54 | held |
| 2026-10-22 | 2026-10-23 | GRAL | stalk | — | -1.07 | -0.53 | faded |
| 2026-10-22 | 2026-10-23 | GSAT | stalk | — | -0.84 | -0.75 | held |
| 2026-10-22 | 2026-10-23 | HQ | stalk | — | -3.38 | -2.97 | held |
| 2026-10-22 | 2026-10-23 | IHS | stalk | — | +0.12 | +0.18 | flat |
| 2026-10-22 | 2026-10-23 | INOD | stalk | — | -0.60 | +1.07 | reversed |
| 2026-10-22 | 2026-10-23 | KOD | stalk | — | -3.16 | -3.92 | held |
| 2026-10-22 | 2026-10-23 | KRSA | stalk | — | +3.86 | +1.10 | faded |
| 2026-10-22 | 2026-10-23 | LIFE | tier-a | — | +0.30 | +1.77 | held |
| 2026-10-22 | 2026-10-23 | LIME | stalk | — | +1.36 | -0.57 | reversed |
| 2026-10-22 | 2026-10-23 | LOCO | stalk | — | -1.58 | -2.90 | held |
| 2026-10-22 | 2026-10-23 | MDB | stalk | — | -2.95 | -2.42 | held |
| 2026-10-22 | 2026-10-23 | MSFT | stalk | — | -1.55 | -1.24 | held |
| 2026-10-22 | 2026-10-23 | MSTR | stalk | — | -1.40 | +1.51 | reversed |
| 2026-10-22 | 2026-10-23 | NDSN | stalk | — | -0.55 | -0.50 | held |
| 2026-10-22 | 2026-10-23 | NTNX | stalk | — | -0.71 | -1.02 | held |
| 2026-10-22 | 2026-10-23 | OFG | stalk | — | -1.79 | -1.83 | held |
| 2026-10-22 | 2026-10-23 | OKTA | stalk | — | -3.31 | -2.28 | held |
| 2026-10-22 | 2026-10-23 | OZK | stalk | — | +1.02 | +1.18 | held |
| 2026-10-22 | 2026-10-23 | PCVX | stalk | — | -2.17 | -2.97 | held |
| 2026-10-22 | 2026-10-23 | PNFP | stalk | — | +1.80 | +1.13 | held |
| 2026-10-22 | 2026-10-23 | PTLO | stalk | — | +1.14 | -0.57 | reversed |
| 2026-10-22 | 2026-10-23 | RCEL | tier-a | — | -0.39 | -4.76 | held |
| 2026-10-22 | 2026-10-23 | RNW | stalk | — | +0.07 | +0.00 | flat |
| 2026-10-22 | 2026-10-23 | ROIV | stalk | — | -2.63 | -3.34 | held |
| 2026-10-22 | 2026-10-23 | SBAC | stalk | — | +11.84 | +8.56 | held |
| 2026-10-22 | 2026-10-23 | SBET | stalk | — | -0.95 | +0.37 | reversed |
| 2026-10-22 | 2026-10-23 | STDN | stalk | — | +0.25 | +1.03 | held |
| 2026-10-22 | 2026-10-23 | STNG | stalk | — | +1.00 | +2.13 | held |
| 2026-10-22 | 2026-10-23 | STRC | stalk | — | -0.03 | +0.19 | faded |
| 2026-10-22 | 2026-10-23 | SYM | stalk | — | -0.85 | -1.33 | held |
| 2026-10-22 | 2026-10-23 | TNK | stalk | — | +1.78 | +3.36 | held |
| 2026-10-22 | 2026-10-23 | TRNS | stalk | — | -2.97 | -2.98 | held |
| 2026-10-22 | 2026-10-23 | TWST | stalk | — | -6.79 | -4.51 | held |
| 2026-10-22 | 2026-10-23 | TXNM | stalk | — | -0.72 | -0.53 | held |
| 2026-10-22 | 2026-10-23 | WFRD | stalk | — | -1.67 | +1.17 | reversed |
| 2026-10-22 | 2026-10-23 | XXI | stalk | — | -3.15 | -0.88 | faded |
| 2026-10-23 | 2026-10-26 | AAL | stalk | stockbee | +0.79 | +1.79 | held |
| 2026-10-23 | 2026-10-26 | ADT | stalk | jeff_sun | +0.29 | -0.36 | reversed |
| 2026-10-23 | 2026-10-26 | AMLX | stalk | qullamaggie | -3.02 | -4.43 | held |
| 2026-10-23 | 2026-10-26 | BALY | stalk | peoplewish | +1.48 | -0.15 | faded |
| 2026-10-23 | 2026-10-26 | BIP | stalk | jeff_sun | -0.68 | -0.89 | held |
| 2026-10-23 | 2026-10-26 | CCS | stalk | stockbee | +1.12 | +0.41 | faded |
| 2026-10-23 | 2026-10-26 | CLBK | stalk | jeff_sun | -0.05 | +0.46 | reversed |
| 2026-10-23 | 2026-10-26 | CMPR | stalk | jeff_sun | -0.04 | +1.16 | reversed |
| 2026-10-23 | 2026-10-26 | COF/PJ | stalk | jeff_sun | +0.06 | -0.59 | reversed |
| 2026-10-23 | 2026-10-26 | COF/PL | stalk | jeff_sun | -0.34 | -1.62 | held |
| 2026-10-23 | 2026-10-26 | CPB | stalk | stockbee | -0.72 | -1.65 | held |
| 2026-10-23 | 2026-10-26 | CWBC | stalk | jeff_sun | -1.88 | -1.73 | held |
| 2026-10-23 | 2026-10-26 | ECO | stalk | qullamaggie | +3.59 | +3.57 | held |
| 2026-10-23 | 2026-10-26 | EPAC | stalk | jeff_sun | +2.16 | +0.74 | faded |
| 2026-10-23 | 2026-10-26 | EXE | stalk | jeff_sun | -1.85 | +0.19 | faded |
| 2026-10-23 | 2026-10-26 | FBYD | stalk | peoplewish | +0.63 | -1.58 | reversed |
| 2026-10-23 | 2026-10-26 | FIS | stalk | jeff_sun | -0.90 | -2.34 | held |
| 2026-10-23 | 2026-10-26 | FIVN | stalk | qullamaggie | +3.72 | +5.18 | held |
| 2026-10-23 | 2026-10-26 | FLO | stalk | stockbee | -1.77 | -0.97 | held |
| 2026-10-23 | 2026-10-26 | FRPT | stalk | jeff_sun | -1.91 | -1.69 | held |
| 2026-10-23 | 2026-10-26 | GPI | stalk | stockbee | +2.44 | +2.73 | held |
| 2026-10-23 | 2026-10-26 | INDV | stalk | jeff_sun | -1.05 | -0.88 | held |
| 2026-10-23 | 2026-10-26 | INVA | stalk | jeff_sun | -0.29 | +0.72 | reversed |
| 2026-10-23 | 2026-10-26 | JNJ | stalk | jeff_sun | +1.24 | +1.09 | held |
| 2026-10-23 | 2026-10-26 | KRG | stalk | jeff_sun | -0.04 | +0.02 | faded |
| 2026-10-23 | 2026-10-26 | KRNY | stalk | jeff_sun | -0.05 | -0.11 | flat |
| 2026-10-23 | 2026-10-26 | LAD | stalk | stockbee | +4.25 | +1.27 | faded |
| 2026-10-23 | 2026-10-26 | LULU | stalk | stockbee | -0.26 | +2.41 | reversed |
| 2026-10-23 | 2026-10-26 | MG | stalk | stockbee | +1.25 | +0.07 | flat |
| 2026-10-23 | 2026-10-26 | MHK | stalk | stockbee | +0.66 | -0.69 | reversed |
| 2026-10-23 | 2026-10-26 | MRP | stalk | jeff_sun | +0.67 | +0.04 | flat |
| 2026-10-23 | 2026-10-26 | PCG | stalk | stockbee | -0.04 | +1.27 | reversed |
| 2026-10-23 | 2026-10-26 | RAMP | stalk | jeff_sun | +0.05 | -0.07 | faded |
| 2026-10-23 | 2026-10-26 | SHC | stalk | jeff_sun | +0.92 | +2.31 | held |
| 2026-10-23 | 2026-10-26 | SXT | stalk | jeff_sun | +2.30 | +1.13 | faded |
| 2026-10-23 | 2026-10-26 | TFIN | stalk | jeff_sun | +0.28 | +0.22 | flat |
| 2026-10-23 | 2026-10-26 | TSLX | stalk | jeff_sun | +0.23 | -0.88 | reversed |
| 2026-10-23 | 2026-10-26 | UPBD | stalk | stockbee | +1.59 | -0.29 | reversed |
| 2026-10-23 | 2026-10-26 | WHR | stalk | stockbee | -0.94 | -6.08 | held |
| 2026-10-23 | 2026-10-26 | XLAB | tier-a | peoplewish|qullamaggie|stockbee | -12.58 | -17.46 | held |
| 2026-10-26 | 2026-10-27 | AAPL | stalk | hernandez|stockbee | -0.44 | +0.69 | reversed |
| 2026-10-26 | 2026-10-27 | ADI | stalk, tier-a | hernandez|jeff_sun|stockbee | +0.56 | +3.75 | held |
| 2026-10-26 | 2026-10-27 | CSCO | stalk, tier-a | hernandez|jeff_sun|stockbee | +0.72 | +1.17 | held |
| 2026-10-26 | 2026-10-27 | HEI | tier-a | hernandez|jeff_sun|stockbee | +0.47 | +0.08 | flat |
| 2026-10-26 | 2026-10-27 | HEI.A | stalk | hernandez|jeff_sun | +0.43 | +0.43 | held |
| 2026-10-26 | 2026-10-27 | HII | stalk | hernandez|jeff_sun | +0.35 | +0.46 | held |
| 2026-10-26 | 2026-10-27 | IHS | stalk | hernandez|jeff_sun | +0.41 | +0.53 | held |
| 2026-10-26 | 2026-10-27 | KEY | stalk | jeff_sun|stockbee | +0.73 | -0.12 | faded |
| 2026-10-26 | 2026-10-27 | KRT | stalk | jeff_sun|stockbee | -0.02 | -0.04 | flat |
| 2026-10-26 | 2026-10-27 | MSFT | stalk | jeff_sun|stockbee | +0.00 | -0.20 | flat |
| 2026-10-26 | 2026-10-27 | NEOG | stalk | jeff_sun|peoplewish | +0.49 | +2.21 | held |
| 2026-10-26 | 2026-10-27 | NXPI | tier-a | hernandez|jeff_sun|stockbee | -0.04 | +2.42 | reversed |
| 2026-10-26 | 2026-10-27 | ORKA | tier-a | jeff_sun|peoplewish|stockbee | -1.13 | +6.41 | reversed |
| 2026-10-26 | 2026-10-27 | P | tier-a | hernandez|jeff_sun|qullamaggie|stockbee | +0.61 | +4.92 | held |
| 2026-10-26 | 2026-10-27 | PLTR | stalk | jeff_sun|stockbee | -0.66 | -0.36 | held |
| 2026-10-26 | 2026-10-27 | PRTH | stalk | hernandez|stockbee | +0.00 | +0.00 | flat |
| 2026-10-26 | 2026-10-27 | RNG | tier-a | jeff_sun|peoplewish|qullamaggie | -1.85 | -1.22 | held |
| 2026-10-26 | 2026-10-27 | RTX | stalk | hernandez|jeff_sun | +0.35 | -1.02 | reversed |
| 2026-10-26 | 2026-10-27 | TENB | tier-a | peoplewish|qullamaggie|stockbee | +0.61 | +1.57 | held |
| 2026-10-27 | 2026-10-28 | AMZN | stalk | jeff_sun|stockbee | -0.08 | +0.59 | reversed |
| 2026-10-27 | 2026-10-28 | AVGO | stalk | jeff_sun|stockbee | — | +2.78 | up |
| 2026-10-27 | 2026-10-28 | CRML | tier-a | peoplewish|qullamaggie|stockbee | — | — | no_bar |
| 2026-10-27 | 2026-10-28 | CYPH | tier-a | peoplewish|qullamaggie|stockbee | — | +3.35 | up |
| 2026-10-27 | 2026-10-28 | FSLR | stalk | jeff_sun|stockbee | — | +0.28 | up |
| 2026-10-27 | 2026-10-28 | GLXY | tier-a | jeff_sun|peoplewish|stockbee | — | +11.12 | up |
| 2026-10-27 | 2026-10-28 | HII | stalk | hernandez|jeff_sun | — | -0.71 | down |
| 2026-10-27 | 2026-10-28 | HRI | tier-a | jeff_sun|peoplewish|stockbee | — | +6.47 | up |
| 2026-10-27 | 2026-10-28 | KRT | stalk | jeff_sun|stockbee | — | -1.96 | down |
| 2026-10-27 | 2026-10-28 | MXL | tier-a | jeff_sun|peoplewish|stockbee | — | +0.63 | up |
| 2026-10-27 | 2026-10-28 | NVDA | stalk | jeff_sun|stockbee | — | -1.15 | down |
| 2026-10-27 | 2026-10-28 | ON | tier-a | hernandez|jeff_sun|stockbee | — | -3.86 | down |
| 2026-10-27 | 2026-10-28 | PRTH | stalk | hernandez|stockbee | — | +0.26 | up |
| 2026-10-27 | 2026-10-28 | RDW | tier-a | jeff_sun|peoplewish|stockbee | — | +1.41 | up |
| 2026-10-27 | 2026-10-28 | RKLB | tier-a | jeff_sun|peoplewish|stockbee | — | +0.50 | up |
| 2026-10-27 | 2026-10-28 | SOFI | stalk | stockbee | — | +4.51 | up |
| 2026-10-27 | 2026-10-28 | UI | stalk | hernandez|jeff_sun | — | +0.52 | up |
| 2026-10-28 | 2026-10-29 | AKAM | stalk | peoplewish | -2.44 | +1.30 | reversed |
| 2026-10-28 | 2026-10-29 | AMKR | stalk | peoplewish | -1.87 | -2.37 | held |
| 2026-10-28 | 2026-10-29 | AMPX | stalk | peoplewish | -1.64 | -0.38 | faded |
| 2026-10-28 | 2026-10-29 | CHRN | stalk | stockbee | -2.94 | -8.23 | held |
| 2026-10-28 | 2026-10-29 | CLS | stalk | peoplewish | — | — | no_bar |
| 2026-10-28 | 2026-10-29 | DXC | tier-a | hernandez|peoplewish|qullamaggie | -3.23 | -5.47 | held |
| 2026-10-28 | 2026-10-29 | FIGS | stalk | peoplewish|qullamaggie | — | +4.31 | up |
| 2026-10-28 | 2026-10-29 | FLY | stalk | peoplewish | -1.26 | +0.10 | faded |
| 2026-10-28 | 2026-10-29 | IOVA | tier-a | hernandez|peoplewish|qullamaggie | -27.75 | -35.45 | held |
| 2026-10-28 | 2026-10-29 | KNSA | tier-a | jeff_sun|qullamaggie|stockbee | -0.19 | +2.50 | reversed |
| 2026-10-28 | 2026-10-29 | NTSK | tier-a | hernandez|peoplewish|qullamaggie | -5.73 | -1.24 | faded |
| 2026-10-28 | 2026-10-29 | NVDA | stalk | jeff_sun|stockbee | -0.46 | -0.79 | held |
| 2026-10-28 | 2026-10-29 | ONDS | stalk | peoplewish|stockbee | -1.75 | +0.29 | reversed |
| 2026-10-28 | 2026-10-29 | PRME | tier-a | hernandez|jeff_sun|stockbee | -1.31 | -2.24 | held |
| 2026-10-28 | 2026-10-29 | QLYS | tier-a | hernandez|peoplewish|qullamaggie | -4.70 | +3.04 | reversed |
| 2026-10-28 | 2026-10-29 | RUN | stalk | peoplewish | -0.40 | +2.29 | reversed |
| 2026-10-28 | 2026-10-29 | SOFI | tier-a | jeff_sun|qullamaggie|stockbee | -1.28 | +2.74 | reversed |
| 2026-10-28 | 2026-10-29 | TENB | tier-a | hernandez|peoplewish|qullamaggie | -6.14 | +6.28 | reversed |
| 2026-10-28 | 2026-10-29 | TWLO | stalk | peoplewish | -4.18 | -4.69 | held |
| 2026-10-28 | 2026-10-29 | ULCC | stalk | jeff_sun|stockbee | +2.27 | +5.02 | held |
| 2026-10-28 | 2026-10-29 | WDC | stalk | jeff_sun|peoplewish | -1.59 | -0.25 | faded |
| 2026-10-29 | 2026-10-30 | AAL | stalk | jeff_sun | -1.10 | -1.41 | held |
| 2026-10-29 | 2026-10-30 | AAPL | stalk | jeff_sun | -0.63 | -1.23 | held |
| 2026-10-29 | 2026-10-30 | AI | stalk | peoplewish | -1.81 | -2.39 | held |
| 2026-10-29 | 2026-10-30 | ALM | stalk | peoplewish | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | AMBA | stalk | peoplewish | -4.99 | -2.26 | faded |
| 2026-10-29 | 2026-10-30 | AMN | stalk | qullamaggie | +0.17 | +0.58 | up |
| 2026-10-29 | 2026-10-30 | AMZN | stalk | jeff_sun | -4.63 | -1.44 | faded |
| 2026-10-29 | 2026-10-30 | ATLC | stalk | jeff_sun | -1.50 | -4.78 | held |
| 2026-10-29 | 2026-10-30 | AVGO | stalk | jeff_sun | -4.14 | -5.48 | held |
| 2026-10-29 | 2026-10-30 | BP | stalk | jeff_sun | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | BRAI | stalk | jeff_sun | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | BROS | stalk | jeff_sun | +0.02 | -2.59 | reversed |
| 2026-10-29 | 2026-10-30 | BSP | stalk | peoplewish | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | CCC | stalk | jeff_sun | +0.00 | -0.39 | down |
| 2026-10-29 | 2026-10-30 | CORZ | stalk | peoplewish | -6.03 | -8.18 | held |
| 2026-10-29 | 2026-10-30 | CVE | stalk | jeff_sun | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | ECVT | stalk | jeff_sun | -0.39 | -1.17 | held |
| 2026-10-29 | 2026-10-30 | EE | stalk | jeff_sun | — | +0.91 | up |
| 2026-10-29 | 2026-10-30 | ELF | stalk | jeff_sun | +0.18 | -1.15 | reversed |
| 2026-10-29 | 2026-10-30 | F | stalk | jeff_sun | -0.41 | -0.89 | held |
| 2026-10-29 | 2026-10-30 | FIGS | stalk, tier-a | qullamaggie | -0.51 | -1.11 | held |
| 2026-10-29 | 2026-10-30 | FIS | stalk | jeff_sun | +0.91 | +3.41 | held |
| 2026-10-29 | 2026-10-30 | GLOB | stalk | qullamaggie | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | GLXY | stalk | peoplewish | -6.62 | -11.75 | held |
| 2026-10-29 | 2026-10-30 | GMAB | tier-a | qullamaggie | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | GOOGL | stalk | jeff_sun | -0.95 | -1.41 | held |
| 2026-10-29 | 2026-10-30 | HIMS | stalk | peoplewish | -4.01 | -6.80 | held |
| 2026-10-29 | 2026-10-30 | HPK | stalk | jeff_sun | +0.96 | -2.49 | reversed |
| 2026-10-29 | 2026-10-30 | KSS | stalk | qullamaggie | -0.73 | -0.86 | held |
| 2026-10-29 | 2026-10-30 | KVYO | stalk | qullamaggie | +0.29 | -1.52 | reversed |
| 2026-10-29 | 2026-10-30 | LIFE | stalk | peoplewish | -1.99 | -0.53 | faded |
| 2026-10-29 | 2026-10-30 | MAN | stalk | peoplewish | — | +1.92 | up |
| 2026-10-29 | 2026-10-30 | MU | stalk | jeff_sun | -5.38 | -5.31 | held |
| 2026-10-29 | 2026-10-30 | NESR | stalk | peoplewish | -3.41 | -0.56 | faded |
| 2026-10-29 | 2026-10-30 | NKTR | stalk | peoplewish | -0.66 | -0.79 | held |
| 2026-10-29 | 2026-10-30 | NVDA | stalk | jeff_sun | -2.25 | -4.26 | held |
| 2026-10-29 | 2026-10-30 | OBA | stalk | stockbee | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | OKLO | stalk | peoplewish | -6.09 | -5.79 | held |
| 2026-10-29 | 2026-10-30 | PCG | stalk | jeff_sun | +0.91 | -0.30 | reversed |
| 2026-10-29 | 2026-10-30 | PRME | tier-a | qullamaggie | -4.01 | -9.92 | held |
| 2026-10-29 | 2026-10-30 | QBTS | stalk | peoplewish | -5.62 | -7.87 | held |
| 2026-10-29 | 2026-10-30 | RBLX | stalk | qullamaggie | -12.94 | -18.18 | held |
| 2026-10-29 | 2026-10-30 | SDGR | tier-a | qullamaggie | -3.47 | -9.50 | held |
| 2026-10-29 | 2026-10-30 | SEZL | stalk | peoplewish | -1.49 | +0.67 | reversed |
| 2026-10-29 | 2026-10-30 | SPHR | stalk | peoplewish | -0.80 | -3.71 | held |
| 2026-10-29 | 2026-10-30 | TWLO | stalk | peoplewish | -22.83 | -15.10 | held |
| 2026-10-29 | 2026-10-30 | UEC | stalk | peoplewish | -5.58 | -5.46 | held |
| 2026-10-29 | 2026-10-30 | UPST | stalk | jeff_sun | -2.74 | -7.33 | held |
| 2026-10-29 | 2026-10-30 | VSTM | stalk | qullamaggie | -0.31 | +0.93 | reversed |
| 2026-10-29 | 2026-10-30 | WGS | stalk | peoplewish | -2.39 | -2.76 | held |
| 2026-10-29 | 2026-10-30 | WIX | stalk | peoplewish | — | — | no_bar |
| 2026-10-29 | 2026-10-30 | XMTR | stalk | peoplewish | -3.73 | -7.09 | held |
| 2026-10-29 | 2026-10-30 | ZETA | stalk | qullamaggie | -2.20 | -4.82 | held |
| 2026-10-30 | 2026-11-02 | AAL | stalk | stockbee | +3.89 | +3.81 | held |
| 2026-10-30 | 2026-11-02 | AAPL | stalk | stockbee | -0.55 | -1.83 | held |
| 2026-10-30 | 2026-11-02 | ABCL | stalk | peoplewish|qullamaggie | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | AI | stalk | peoplewish | -0.51 | -2.53 | held |
| 2026-10-30 | 2026-11-02 | AMG | stalk | jeff_sun | +2.20 | -2.88 | reversed |
| 2026-10-30 | 2026-11-02 | ARX | stalk | jeff_sun | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | ARXS | stalk | peoplewish | -0.16 | -0.24 | flat |
| 2026-10-30 | 2026-11-02 | ASTH | stalk | jeff_sun | +0.96 | +0.96 | held |
| 2026-10-30 | 2026-11-02 | ATLC | stalk | jeff_sun | +0.76 | -0.35 | reversed |
| 2026-10-30 | 2026-11-02 | AUB | stalk | jeff_sun | +0.99 | +2.83 | held |
| 2026-10-30 | 2026-11-02 | BFC | stalk | jeff_sun | +0.34 | +1.28 | held |
| 2026-10-30 | 2026-11-02 | CDNA | tier-a | jeff_sun|peoplewish|qullamaggie | +0.07 | -1.75 | reversed |
| 2026-10-30 | 2026-11-02 | CNH | stalk | stockbee | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | CRSP | stalk | peoplewish | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | CVE | stalk | jeff_sun | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | DMLP | stalk | jeff_sun | -3.99 | -4.83 | held |
| 2026-10-30 | 2026-11-02 | DNA | stalk | qullamaggie | +1.07 | -12.29 | reversed |
| 2026-10-30 | 2026-11-02 | ELF | stalk | jeff_sun | +2.42 | -0.90 | reversed |
| 2026-10-30 | 2026-11-02 | ENTG | stalk | peoplewish | +1.23 | -1.81 | reversed |
| 2026-10-30 | 2026-11-02 | EQBK | stalk | jeff_sun | +0.59 | +2.48 | held |
| 2026-10-30 | 2026-11-02 | EXPD | stalk | jeff_sun | +1.11 | +0.91 | held |
| 2026-10-30 | 2026-11-02 | F | stalk | stockbee | +1.47 | +3.11 | held |
| 2026-10-30 | 2026-11-02 | FIGS | tier-a | jeff_sun|peoplewish|qullamaggie | +2.02 | -0.09 | faded |
| 2026-10-30 | 2026-11-02 | FTAI | tier-a | peoplewish|qullamaggie|stockbee | +1.98 | +5.61 | held |
| 2026-10-30 | 2026-11-02 | FVRR | stalk | stockbee | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | GCT | stalk | jeff_sun | +1.64 | -1.58 | reversed |
| 2026-10-30 | 2026-11-02 | GRAL | tier-a | hernandez|peoplewish|qullamaggie | +3.56 | -6.69 | reversed |
| 2026-10-30 | 2026-11-02 | GTLB | stalk | qullamaggie | +0.07 | -3.66 | reversed |
| 2026-10-30 | 2026-11-02 | HBT | stalk | jeff_sun | +1.26 | +2.71 | held |
| 2026-10-30 | 2026-11-02 | HRMY | stalk | jeff_sun | +0.03 | -2.19 | reversed |
| 2026-10-30 | 2026-11-02 | HTFL | tier-a | hernandez|peoplewish|qullamaggie | +0.15 | -7.72 | reversed |
| 2026-10-30 | 2026-11-02 | HUM | stalk | jeff_sun | +1.47 | -0.99 | reversed |
| 2026-10-30 | 2026-11-02 | IOVA | tier-a | hernandez|qullamaggie|stockbee | +0.59 | -5.42 | reversed |
| 2026-10-30 | 2026-11-02 | JPM | stalk | jeff_sun | +1.13 | +1.04 | held |
| 2026-10-30 | 2026-11-02 | KOD | tier-a | hernandez|peoplewish|qullamaggie | +0.13 | -1.57 | reversed |
| 2026-10-30 | 2026-11-02 | LB | stalk | jeff_sun | +0.05 | -4.88 | reversed |
| 2026-10-30 | 2026-11-02 | LUMN | stalk | peoplewish | +0.82 | -1.02 | reversed |
| 2026-10-30 | 2026-11-02 | MRNA | tier-a | hernandez|peoplewish|qullamaggie | +1.13 | -0.41 | reversed |
| 2026-10-30 | 2026-11-02 | MSFT | stalk | stockbee | +0.40 | -2.84 | reversed |
| 2026-10-30 | 2026-11-02 | MUSA | stalk | jeff_sun | -1.12 | -4.11 | held |
| 2026-10-30 | 2026-11-02 | NBBK | stalk | jeff_sun | +0.59 | +1.76 | held |
| 2026-10-30 | 2026-11-02 | NESR | stalk | peoplewish | +0.47 | -1.60 | reversed |
| 2026-10-30 | 2026-11-02 | NP | stalk | jeff_sun | -1.06 | +0.65 | reversed |
| 2026-10-30 | 2026-11-02 | NTRS | stalk | jeff_sun | +1.42 | +0.89 | held |
| 2026-10-30 | 2026-11-02 | OBA | stalk | stockbee | — | — | no_bar |
| 2026-10-30 | 2026-11-02 | P | tier-a | jeff_sun|peoplewish|qullamaggie | +1.73 | -10.39 | reversed |
| 2026-10-30 | 2026-11-02 | PURR | tier-a | peoplewish|qullamaggie|stockbee | -1.91 | -11.81 | held |
| 2026-10-30 | 2026-11-02 | QXO | stalk | peoplewish | +3.08 | +5.80 | held |
| 2026-10-30 | 2026-11-02 | RBRK | stalk | peoplewish|qullamaggie | -0.24 | -7.57 | down |
| 2026-10-30 | 2026-11-02 | RGEN | stalk | peoplewish | +0.68 | -2.26 | reversed |
| 2026-10-30 | 2026-11-02 | RNG | stalk | peoplewish|qullamaggie | -0.81 | -4.50 | held |
| 2026-10-30 | 2026-11-02 | RNST | stalk | jeff_sun | +1.08 | +1.55 | held |
| 2026-10-30 | 2026-11-02 | RUN | stalk | peoplewish | +4.41 | +10.29 | held |
| 2026-10-30 | 2026-11-02 | RXRX | stalk | peoplewish | +1.99 | -4.96 | reversed |
| 2026-10-30 | 2026-11-02 | SKYD | stalk | peoplewish | +1.51 | +1.77 | held |
| 2026-10-30 | 2026-11-02 | SPHR | stalk | peoplewish | +2.75 | -3.58 | reversed |
| 2026-10-30 | 2026-11-02 | TWST | stalk | peoplewish|qullamaggie | +0.26 | -15.58 | reversed |
| 2026-10-30 | 2026-11-02 | WIX | stalk | peoplewish | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | AAL | stalk | stockbee | +0.31 | -1.99 | reversed |
| 2026-11-02 | 2026-11-03 | AAPL | stalk | stockbee | -3.78 | -1.89 | held |
| 2026-11-02 | 2026-11-03 | ABCL | stalk, tier-a | hernandez|peoplewish|qullamaggie | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | ADPT | stalk | peoplewish | +1.60 | +2.95 | held |
| 2026-11-02 | 2026-11-03 | AI | stalk | peoplewish | -1.13 | -0.09 | flat |
| 2026-11-02 | 2026-11-03 | AMN | stalk | qullamaggie | -0.31 | -1.01 | held |
| 2026-11-02 | 2026-11-03 | ARQT | stalk | qullamaggie | +0.19 | +2.37 | up |
| 2026-11-02 | 2026-11-03 | BAC | stalk | stockbee | -0.40 | +0.18 | faded |
| 2026-11-02 | 2026-11-03 | BLLN | stalk | peoplewish | +0.18 | +0.09 | flat |
| 2026-11-02 | 2026-11-03 | BSP | stalk | peoplewish | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | CAI | stalk, tier-a | hernandez|peoplewish|qullamaggie | +0.53 | +2.34 | held |
| 2026-11-02 | 2026-11-03 | CDNA | tier-a | peoplewish|qullamaggie|stockbee | -0.29 | +3.02 | reversed |
| 2026-11-02 | 2026-11-03 | CRL | stalk | qullamaggie | +0.41 | +3.90 | held |
| 2026-11-02 | 2026-11-03 | CSGP | stalk | stockbee | -1.51 | -1.57 | held |
| 2026-11-02 | 2026-11-03 | CVI | stalk, tier-a | hernandez|jeff_sun|qullamaggie | -8.69 | -13.11 | held |
| 2026-11-02 | 2026-11-03 | CVLG | stalk | stockbee | -0.87 | +0.00 | flat |
| 2026-11-02 | 2026-11-03 | CZR | stalk | jeff_sun|stockbee | -0.07 | +0.24 | faded |
| 2026-11-02 | 2026-11-03 | EQPT | stalk | peoplewish | +0.44 | -0.81 | reversed |
| 2026-11-02 | 2026-11-03 | F | stalk | jeff_sun|stockbee | +0.16 | -2.38 | reversed |
| 2026-11-02 | 2026-11-03 | FIVN | stalk | peoplewish | -3.08 | +0.00 | flat |
| 2026-11-02 | 2026-11-03 | GH | stalk | peoplewish | +1.35 | +2.52 | held |
| 2026-11-02 | 2026-11-03 | GRAL | stalk | peoplewish|qullamaggie | +2.39 | +4.19 | held |
| 2026-11-02 | 2026-11-03 | GTLB | stalk | qullamaggie | -2.00 | +0.50 | reversed |
| 2026-11-02 | 2026-11-03 | HTFL | stalk, tier-a | hernandez|peoplewish|qullamaggie | -0.46 | -0.17 | flat |
| 2026-11-02 | 2026-11-03 | IDT | stalk | jeff_sun|stockbee | -0.05 | -1.24 | down |
| 2026-11-02 | 2026-11-03 | IRON | stalk | peoplewish|qullamaggie | +1.00 | +3.23 | held |
| 2026-11-02 | 2026-11-03 | KOD | tier-a | hernandez|peoplewish|qullamaggie | +1.17 | +1.30 | held |
| 2026-11-02 | 2026-11-03 | KSS | stalk | peoplewish|qullamaggie | -1.33 | -2.15 | held |
| 2026-11-02 | 2026-11-03 | KVUE | stalk | stockbee | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | KVYO | stalk | peoplewish | -3.17 | -2.11 | held |
| 2026-11-02 | 2026-11-03 | LIFE | stalk | peoplewish | +17.27 | -4.08 | reversed |
| 2026-11-02 | 2026-11-03 | LU | stalk | stockbee | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | MANE | stalk | peoplewish | — | +2.86 | up |
| 2026-11-02 | 2026-11-03 | MPC | stalk | hernandez|jeff_sun | -0.09 | -0.63 | down |
| 2026-11-02 | 2026-11-03 | MRNA | tier-a | hernandez|peoplewish|qullamaggie | +0.54 | +3.44 | held |
| 2026-11-02 | 2026-11-03 | MSFT | stalk | stockbee | +0.28 | +2.74 | held |
| 2026-11-02 | 2026-11-03 | MTZ | tier-a | jeff_sun|peoplewish|stockbee | +1.81 | +2.22 | held |
| 2026-11-02 | 2026-11-03 | NESR | stalk | peoplewish | +1.72 | -1.34 | reversed |
| 2026-11-02 | 2026-11-03 | NOW | tier-a | jeff_sun|qullamaggie|stockbee | -0.66 | +2.92 | reversed |
| 2026-11-02 | 2026-11-03 | NRIX | stalk | peoplewish | +0.08 | +0.47 | up |
| 2026-11-02 | 2026-11-03 | NTRA | stalk | qullamaggie | +1.82 | +2.56 | held |
| 2026-11-02 | 2026-11-03 | NTSK | stalk | peoplewish|qullamaggie | -0.09 | -0.73 | down |
| 2026-11-02 | 2026-11-03 | PGEN | stalk | stockbee | +3.31 | +2.14 | held |
| 2026-11-02 | 2026-11-03 | PSX | stalk | hernandez|jeff_sun | -0.44 | -1.02 | held |
| 2026-11-02 | 2026-11-03 | PURR | tier-a | peoplewish|qullamaggie|stockbee | +2.78 | +4.63 | held |
| 2026-11-02 | 2026-11-03 | QLYS | stalk, tier-a | jeff_sun|peoplewish|qullamaggie | -1.30 | +1.45 | reversed |
| 2026-11-02 | 2026-11-03 | QXO | stalk | peoplewish | -0.09 | +0.17 | faded |
| 2026-11-02 | 2026-11-03 | RBRK | stalk | peoplewish|qullamaggie | — | +1.66 | up |
| 2026-11-02 | 2026-11-03 | RGEN | stalk | peoplewish | +1.50 | +3.12 | held |
| 2026-11-02 | 2026-11-03 | RNG | stalk | peoplewish | -1.99 | +0.57 | reversed |
| 2026-11-02 | 2026-11-03 | RPD | stalk | qullamaggie | -2.36 | -0.13 | flat |
| 2026-11-02 | 2026-11-03 | RXRX | stalk | peoplewish | +0.65 | -3.92 | reversed |
| 2026-11-02 | 2026-11-03 | SAIL | stalk | peoplewish | -2.40 | -1.04 | faded |
| 2026-11-02 | 2026-11-03 | SDGR | stalk | peoplewish|qullamaggie | +0.88 | +3.78 | held |
| 2026-11-02 | 2026-11-03 | SPHR | stalk | peoplewish | +0.00 | +0.00 | flat |
| 2026-11-02 | 2026-11-03 | SYRE | stalk | peoplewish | +1.60 | +3.94 | held |
| 2026-11-02 | 2026-11-03 | TEM | stalk | peoplewish|qullamaggie | +2.94 | -0.87 | reversed |
| 2026-11-02 | 2026-11-03 | THRM | stalk | peoplewish | +0.54 | -3.44 | reversed |
| 2026-11-02 | 2026-11-03 | TMUS | stalk | stockbee | -0.37 | -3.62 | held |
| 2026-11-02 | 2026-11-03 | TTAN | stalk | qullamaggie|stockbee | -1.53 | +0.31 | reversed |
| 2026-11-02 | 2026-11-03 | TWST | stalk | peoplewish|qullamaggie | +1.09 | +8.76 | held |
| 2026-11-02 | 2026-11-03 | VCYT | stalk | peoplewish | +1.94 | +2.63 | held |
| 2026-11-02 | 2026-11-03 | VSTM | stalk | qullamaggie | +0.10 | +1.88 | up |
| 2026-11-02 | 2026-11-03 | WIX | stalk | peoplewish | — | — | no_bar |
| 2026-11-02 | 2026-11-03 | ZURA | stalk | stockbee | +1.27 | +1.27 | held |
| 2026-11-03 | 2026-11-04 | ACHR | stalk | peoplewish|stockbee | +1.33 | -0.48 | reversed |
| 2026-11-03 | 2026-11-04 | AGNC | stalk | stockbee | +2.34 | +3.99 | held |
| 2026-11-03 | 2026-11-04 | ALGM | stalk | jeff_sun|peoplewish | -0.48 | -7.16 | held |
| 2026-11-03 | 2026-11-04 | APH | stalk | jeff_sun|stockbee | — | -6.04 | down |
| 2026-11-03 | 2026-11-04 | BMY | stalk | stockbee | +2.41 | +4.05 | held |
| 2026-11-03 | 2026-11-04 | BSX | stalk | stockbee | +3.01 | +5.33 | held |
| 2026-11-03 | 2026-11-04 | CAI | tier-a | hernandez|peoplewish|qullamaggie | +2.01 | +1.13 | held |
| 2026-11-03 | 2026-11-04 | CLF | tier-a | peoplewish|qullamaggie|stockbee | +1.56 | -9.27 | reversed |
| 2026-11-03 | 2026-11-04 | COKE | stalk | hernandez|stockbee | +2.62 | -1.02 | reversed |
| 2026-11-03 | 2026-11-04 | COMP | stalk | jeff_sun|stockbee | +5.79 | +7.61 | held |
| 2026-11-03 | 2026-11-04 | COP | stalk | hernandez|stockbee | — | -5.12 | down |
| 2026-11-03 | 2026-11-04 | CPNG | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | CVNA | tier-a | jeff_sun|qullamaggie|stockbee | +2.71 | +8.74 | held |
| 2026-11-03 | 2026-11-04 | CVX | stalk | hernandez|stockbee | -1.20 | -3.68 | held |
| 2026-11-03 | 2026-11-04 | ECG | stalk | jeff_sun|peoplewish | -11.75 | -29.45 | held |
| 2026-11-03 | 2026-11-04 | ENPH | stalk | peoplewish|stockbee | +6.21 | +3.71 | held |
| 2026-11-03 | 2026-11-04 | EQX | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | FICO | stalk | jeff_sun|peoplewish | +1.99 | -2.91 | reversed |
| 2026-11-03 | 2026-11-04 | FIG | stalk | peoplewish|stockbee | +1.62 | +5.51 | held |
| 2026-11-03 | 2026-11-04 | FIGS | stalk, tier-a | hernandez|peoplewish|qullamaggie | +3.36 | +5.23 | held |
| 2026-11-03 | 2026-11-04 | FMC | stalk | peoplewish|qullamaggie|stockbee | +3.79 | +5.85 | held |
| 2026-11-03 | 2026-11-04 | FTAI | tier-a | peoplewish|qullamaggie|stockbee | -2.99 | -10.51 | held |
| 2026-11-03 | 2026-11-04 | FUTU | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | HTFL | stalk | hernandez|peoplewish|qullamaggie | +0.35 | +3.99 | held |
| 2026-11-03 | 2026-11-04 | HWM | stalk | jeff_sun|stockbee | -0.76 | -4.26 | held |
| 2026-11-03 | 2026-11-04 | INIO | stalk | jeff_sun|peoplewish | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | IRON | stalk | peoplewish | +0.42 | +2.61 | held |
| 2026-11-03 | 2026-11-04 | JBLU | stalk | peoplewish|qullamaggie|stockbee | +6.92 | +11.95 | held |
| 2026-11-03 | 2026-11-04 | JOBY | stalk | peoplewish|stockbee | +1.86 | +4.12 | held |
| 2026-11-03 | 2026-11-04 | KMI | stalk | stockbee | -0.82 | -4.13 | held |
| 2026-11-03 | 2026-11-04 | KMT | stalk | jeff_sun|stockbee | -4.32 | -14.00 | held |
| 2026-11-03 | 2026-11-04 | KVYO | tier-a | peoplewish|qullamaggie|stockbee | +0.66 | +0.09 | flat |
| 2026-11-03 | 2026-11-04 | LADR | stalk | jeff_sun|stockbee | +1.92 | +2.69 | held |
| 2026-11-03 | 2026-11-04 | LBTYA | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | LUMN | stalk | peoplewish|stockbee | +3.58 | -5.89 | reversed |
| 2026-11-03 | 2026-11-04 | NBBK | stalk | jeff_sun|stockbee | +2.56 | +1.93 | held |
| 2026-11-03 | 2026-11-04 | NLY | stalk | stockbee | +2.30 | +3.89 | held |
| 2026-11-03 | 2026-11-04 | NTSK | stalk | peoplewish|qullamaggie | +1.42 | +4.26 | held |
| 2026-11-03 | 2026-11-04 | PG | stalk | stockbee | +1.54 | +3.27 | held |
| 2026-11-03 | 2026-11-04 | PR | stalk | hernandez|stockbee | -1.46 | -6.63 | held |
| 2026-11-03 | 2026-11-04 | PRME | stalk | qullamaggie | +4.40 | +9.23 | held |
| 2026-11-03 | 2026-11-04 | QS | stalk | peoplewish|stockbee | +2.67 | +7.52 | held |
| 2026-11-03 | 2026-11-04 | SDGR | stalk | peoplewish|qullamaggie | +0.07 | +4.93 | up |
| 2026-11-03 | 2026-11-04 | SHLS | stalk | jeff_sun|stockbee | +4.60 | +8.15 | held |
| 2026-11-03 | 2026-11-04 | SKYD | stalk | peoplewish|stockbee | +1.49 | +3.65 | held |
| 2026-11-03 | 2026-11-04 | TEM | tier-a | peoplewish|qullamaggie|stockbee | +1.21 | -2.81 | reversed |
| 2026-11-03 | 2026-11-04 | TENB | stalk | peoplewish|qullamaggie | -0.34 | +0.66 | reversed |
| 2026-11-03 | 2026-11-04 | TEVA | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-03 | 2026-11-04 | TXN | stalk | jeff_sun|stockbee | +0.29 | -0.32 | reversed |
| 2026-11-03 | 2026-11-04 | VSEC | stalk | jeff_sun|peoplewish|stockbee | +2.76 | +0.61 | faded |
| 2026-11-03 | 2026-11-04 | VZ | stalk | stockbee | +1.66 | +2.06 | held |
| 2026-11-03 | 2026-11-04 | WING | tier-a | peoplewish|qullamaggie|stockbee | +4.95 | +3.71 | held |
| 2026-11-03 | 2026-11-04 | XMTR | stalk | jeff_sun|peoplewish | -0.72 | +1.98 | reversed |
| 2026-11-03 | 2026-11-04 | XOM | stalk | stockbee | -1.80 | -4.51 | held |
| 2026-11-03 | 2026-11-04 | XPEV | stalk | stockbee | — | — | no_bar |
| 2026-11-04 | 2026-11-05 | AAPL | stalk | jeff_sun|stockbee | +1.26 | -1.52 | reversed |
| 2026-11-04 | 2026-11-05 | ALHC | stalk | peoplewish | +0.98 | -7.13 | reversed |
| 2026-11-04 | 2026-11-05 | BB | stalk | jeff_sun|peoplewish | — | — | no_bar |
| 2026-11-04 | 2026-11-05 | BSP | stalk | jeff_sun|peoplewish | — | — | no_bar |
| 2026-11-04 | 2026-11-05 | CAI | stalk | peoplewish|qullamaggie | -17.22 | -21.64 | held |
| 2026-11-04 | 2026-11-05 | CDNA | tier-a | jeff_sun|peoplewish|qullamaggie | -2.63 | -11.10 | held |
| 2026-11-04 | 2026-11-05 | FISV | tier-a | hernandez|jeff_sun|stockbee | +0.35 | +1.11 | held |
| 2026-11-04 | 2026-11-05 | FN | stalk | peoplewish|stockbee | — | — | no_bar |
| 2026-11-04 | 2026-11-05 | FTAI | tier-a | jeff_sun|peoplewish|qullamaggie | -2.34 | -9.58 | held |
| 2026-11-04 | 2026-11-05 | GKOS | tier-a | hernandez|peoplewish|qullamaggie | +1.34 | -10.82 | reversed |
| 2026-11-04 | 2026-11-05 | GPK | tier-a | jeff_sun|qullamaggie|stockbee | +0.34 | -2.04 | reversed |
| 2026-11-04 | 2026-11-05 | GRAL | stalk | peoplewish|qullamaggie | -16.84 | -17.12 | held |
| 2026-11-04 | 2026-11-05 | HL | stalk | stockbee | +1.94 | -3.34 | reversed |
| 2026-11-04 | 2026-11-05 | HTFL | stalk | peoplewish|qullamaggie | -0.53 | -8.17 | held |
| 2026-11-04 | 2026-11-05 | KVYO | tier-a | jeff_sun|peoplewish|qullamaggie | -4.96 | -2.57 | held |
| 2026-11-04 | 2026-11-05 | LSCC | stalk, tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | -4.94 | -8.55 | held |
| 2026-11-04 | 2026-11-05 | MARA | stalk | peoplewish|stockbee | -2.40 | -14.48 | held |
| 2026-11-04 | 2026-11-05 | MRNA | tier-a | hernandez|peoplewish|qullamaggie | -0.15 | -6.54 | down |
| 2026-11-04 | 2026-11-05 | ODTX | stalk | stockbee | +0.00 | -3.18 | down |
| 2026-11-04 | 2026-11-05 | OPEN | stalk | peoplewish | -2.02 | -9.60 | held |
| 2026-11-04 | 2026-11-05 | SNAP | stalk | jeff_sun|peoplewish|stockbee | -10.49 | -13.87 | held |
| 2026-11-04 | 2026-11-05 | TMO | stalk | hernandez|stockbee | +0.08 | -4.16 | reversed |
| 2026-11-04 | 2026-11-05 | VSAT | stalk | peoplewish | -2.67 | -11.09 | held |
| 2026-11-04 | 2026-11-05 | VSTM | stalk | peoplewish|qullamaggie | +0.10 | -4.77 | reversed |
| 2026-11-05 | 2026-11-06 | AFRM | stalk | jeff_sun|peoplewish|stockbee | -4.84 | -2.23 | faded |
| 2026-11-05 | 2026-11-06 | AG | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-05 | 2026-11-06 | ANET | stalk | jeff_sun|stockbee | +8.54 | +7.29 | held |
| 2026-11-05 | 2026-11-06 | B | stalk | jeff_sun|stockbee | — | — | no_bar |
| 2026-11-05 | 2026-11-06 | BFC | stalk | jeff_sun|stockbee | +0.41 | +0.34 | held |
| 2026-11-05 | 2026-11-06 | DUOL | tier-a | peoplewish|qullamaggie|stockbee | -0.32 | +2.17 | reversed |
| 2026-11-05 | 2026-11-06 | HL | stalk | jeff_sun|stockbee | -0.55 | +1.94 | reversed |
| 2026-11-05 | 2026-11-06 | KD | tier-a | peoplewish|qullamaggie|stockbee | -2.16 | +0.68 | reversed |
| 2026-11-05 | 2026-11-06 | LIVN | tier-a | hernandez|qullamaggie|stockbee | — | — | no_bar |
| 2026-11-05 | 2026-11-06 | LSCC | stalk | jeff_sun|peoplewish | +7.93 | +7.11 | held |
| 2026-11-05 | 2026-11-06 | OUST | tier-a | peoplewish|qullamaggie|stockbee | +4.65 | +13.99 | held |
| 2026-11-05 | 2026-11-06 | TE | stalk | peoplewish|qullamaggie | +6.14 | +3.51 | held |
| 2026-11-05 | 2026-11-06 | VRDN | tier-a | hernandez|peoplewish|qullamaggie|stockbee | +0.56 | -0.21 | faded |
| 2026-11-05 | 2026-11-06 | XNCR | tier-a | hernandez|peoplewish|qullamaggie|stockbee | +0.47 | +4.99 | held |
| 2026-11-06 | 2026-11-09 | ACHC | tier-a | hernandez|peoplewish|qullamaggie|stockbee | +2.70 | +4.35 | held |
| 2026-11-06 | 2026-11-09 | APP | tier-a | jeff_sun|qullamaggie|stockbee | -0.89 | +4.81 | reversed |
| 2026-11-06 | 2026-11-09 | EWTX | stalk | peoplewish|qullamaggie | +2.00 | +8.21 | held |
| 2026-11-06 | 2026-11-09 | FUN | tier-a | peoplewish|qullamaggie|stockbee | -0.10 | +7.49 | reversed |
| 2026-11-06 | 2026-11-09 | MRNA | tier-a | hernandez|peoplewish|qullamaggie|stockbee | +1.89 | +5.82 | held |
| 2026-11-06 | 2026-11-09 | ROKU | stalk | jeff_sun|stockbee | — | — | no_close |
| 2026-11-06 | 2026-11-09 | RUN | tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | +0.10 | -2.40 | reversed |
| 2026-11-06 | 2026-11-09 | SEZL | tier-a | jeff_sun|peoplewish|qullamaggie|stockbee | +2.14 | +0.94 | faded |
| 2026-11-06 | 2026-11-09 | U | tier-a | peoplewish|qullamaggie|stockbee | +1.28 | -0.12 | faded |
| 2026-11-06 | 2026-11-09 | XERS | tier-a | hernandez|jeff_sun|qullamaggie|stockbee | +0.00 | +4.34 | up |

## Rules

| Rule | Value |
|---|---|
| Base | observation-session close, the day the list was published |
| Entry open gap | entry open versus that close |
| Entry close change | entry close versus that close |
| `held` | same sign, close change at least 50% of the open gap |
| `faded` | same sign but under that share, or an opposite move under 0.25 pp |
| `reversed` | opposite sign and a close change of at least 0.25 pp |

