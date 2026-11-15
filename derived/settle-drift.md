# Settle drift — how far the 08:00 ET EU/UK move travelled by the close

**Source:** derived read of `earnings/<date>-reactions-settled.md` (the 12:15 ET settlement pass) and the morning `earnings/<date>-reactions.md`; no source file is modified · **Built:** 2026-11-15 · **Covers:** 3 settle session(s), 2026-11-11 → 2026-11-13; 58 compared row(s) · read-only

> **Read this before the tables.**
>
> 1. **The comparison only covers rows that are in BOTH tables, and that set is
>    biased.** The settle pass re-selects its rows by the SETTLED move, so a morning
>    row whose reaction faded below the cut is not republished and its drift is never
>    measured: **30 of 88 morning EU/UK row(s) (34%) were not in the settled table.**
>    The measured drift therefore UNDERSTATES fading. 30 settled row(s) grew into the
>    table with no morning move and are not compared either.
> 2. **Small sample.** 3 session(s). A per-market figure with fewer than 5 rows
>    is printed but marked *too few to read* - one large mover sets its median.
> 3. **Descriptive only.** `held`, `extended`, `faded` and `reversed` describe the
>    path between two prints. Nothing here is a direction, a size or a recommendation.

## Summary — every session pooled

| Sessions | Compared rows | Median abs drift (pp) | Max (pp) | Rows > 1pp | Held / extended / faded / reversed |
|---|---|---|---|---|---|
| 3 | 58 | 0.82 | 6.86 | 26 (44.8%) | 32 / 22 / 4 / 0 |

**What this shows.** Of the 58 EU/UK rows that appear in both the 08:00 ET scan and the 12:15 ET settle pass, 26 (44.8%) ended more than 1pp away from the move the morning artifact printed. Of those, 22 extended, 4 faded and 0 reversed. The morning EU/UK move is a snapshot, and this is how far the snapshot was from the session's result.

**What it does not show.** It is not the drift of *every* morning row - see note 1 above: the rows that faded out of the settle table are missing, so fading is under-counted. **The extended-versus-faded split is the number that selection distorts most**: a table re-selected by the settled move keeps the reactions that grew and loses the ones that shrank, so a lopsided split here is what the method would produce even if reactions faded as often as they extended. Do not read it as a tendency. It also says nothing about the US rows, which the settle pass does not republish (the US session is open at 12:15 ET).

## By session

| Session | Compared | Median abs drift (pp) | Artifact's median | Max (pp) | Rows > 1pp | Held / ext / faded / rev | Pipeline |
|---|---|---|---|---|---|---|---|
| 2026-11-11 | 22 | 0.69 | 0.71 | 6.86 | 7 (32%) | 15 / 7 / 0 / 0 | 2026-11-11.2 |
| 2026-11-12 | 19 | 1.26 | 1.26 | 6.81 | 12 (63%) | 7 / 9 / 3 / 0 | 2026-11-12.2 |
| 2026-11-13 | 17 | 0.78 | 0.78 | 4.78 | 7 (41%) | 10 / 6 / 1 / 0 | 2026-11-12.2 |

**How to read it.** The *Artifact's median* is the figure the settle pass printed in its own `scan_to_settle` line. It takes the upper-middle value on an even count, while this view takes the true median, so the two can differ by a few hundredths on an even count; a larger gap would mean the two read different rows. A session-to-session swing in the median is not, on its own, a trend: each session has 15-25 compared rows.

## By market — every session pooled

| Market | Compared | Median abs drift (pp) | Max (pp) | Rows > 1pp | Held / ext / faded / rev | Readable? |
|---|---|---|---|---|---|---|
| sweden | 10 | 1.05 | 2.90 | 5 (50%) | 5 / 4 / 1 / 0 | yes |
| germany | 8 | 1.83 | 6.81 | 7 (88%) | 1 / 7 / 0 / 0 | yes |
| norway | 8 | 0.83 | 2.62 | 3 (38%) | 5 / 3 / 0 / 0 | yes |
| uk | 5 | 0.41 | 1.53 | 2 (40%) | 3 / 2 / 0 / 0 | yes |
| denmark | 4 | 1.26 | 4.40 | 2 (50%) | 2 / 1 / 1 / 0 | too few to read |
| spain | 4 | 0.32 | 1.68 | 1 (25%) | 3 / 1 / 0 / 0 | too few to read |
| switzerland | 4 | 0.96 | 1.26 | 2 (50%) | 2 / 1 / 1 / 0 | too few to read |
| france | 3 | 2.01 | 4.78 | 2 (67%) | 1 / 2 / 0 / 0 | too few to read |
| italy | 3 | 0.64 | 2.66 | 1 (33%) | 2 / 0 / 1 / 0 | too few to read |
| poland | 3 | 0.00 | 0.81 | 0 (0%) | 3 / 0 / 0 / 0 | too few to read |
| austria | 2 | 0.66 | 0.71 | 0 (0%) | 2 / 0 / 0 / 0 | too few to read |
| finland | 2 | 3.79 | 6.86 | 1 (50%) | 1 / 1 / 0 / 0 | too few to read |
| netherlands | 2 | 0.55 | 0.83 | 0 (0%) | 2 / 0 / 0 / 0 | too few to read |

**How to read it.** A market's drift mixes two things this table cannot separate: how much of the session was still to run at 08:00 ET (close times differ by venue - most close at 11:30 ET in winter, a few earlier) and which names the per-market cap let into the table. A high figure on a thin row count is one name, not a market property.

## Coverage — morning table vs settled table

| Session | Morning EU/UK rows | Settled rows | Compared | New at settle | Morning rows not republished |
|---|---|---|---|---|---|
| 2026-11-11 | 29 | 30 | 22 | 8 | 7 (AKAST, COTN, HUBN, ICOS, IFCN, IFX, VWS) |
| 2026-11-12 | 30 | 30 | 19 | 11 | 11 (ANDF, BELA, CMB, ERA, LBW, NCOD, OHB, RAND, ...) |
| 2026-11-13 | 29 | 28 | 17 | 11 | 12 (ATS, CFR, EOLU_B, GOMX, III, MMK, MOL, OBCK, ...) |

**What the last column means.** These morning rows had a printed 08:00 ET move and no settled move in this view. Most fell below the settle pass's selection cut, and some may have been dropped by its reference-close gate. Their drift is unknown here, not zero.

## Every compared row

| Session | Ticker | Market | Move @08:00 | Settled | Δ (pp) | Path |
|---|---|---|---|---|---|---|
| 2026-11-11 | SENSO | finland | +4.33 | +11.19 | +6.86 | extended |
| 2026-11-11 | BICO | sweden | -30.12 | -32.15 | -2.03 | extended |
| 2026-11-11 | SOI | france | +9.92 | +11.93 | +2.01 | extended |
| 2026-11-11 | ENR | germany | +9.01 | +10.78 | +1.77 | extended |
| 2026-11-11 | CAF | spain | -10.19 | -11.87 | -1.68 | extended |
| 2026-11-11 | DRW3 | germany | +8.32 | +9.93 | +1.61 | extended |
| 2026-11-11 | AIXA | germany | +7.13 | +8.33 | +1.20 | extended |
| 2026-11-11 | BWE | norway | +4.87 | +5.75 | +0.88 | held |
| 2026-11-11 | FLS | denmark | +4.72 | +5.59 | +0.87 | held |
| 2026-11-11 | BESI | netherlands | +5.11 | +5.94 | +0.83 | held |
| 2026-11-11 | ATS | austria | +11.17 | +11.88 | +0.71 | held |
| 2026-11-11 | YPSN | switzerland | +4.26 | +4.92 | +0.66 | held |
| 2026-11-11 | TPRO | italy | +7.09 | +7.73 | +0.64 | held |
| 2026-11-11 | ERA | france | +6.87 | +7.43 | +0.56 | held |
| 2026-11-11 | FNM | sweden | +10.70 | +11.23 | +0.53 | held |
| 2026-11-11 | SIVE | sweden | +11.27 | +10.76 | -0.51 | held |
| 2026-11-11 | HNSA | sweden | +14.48 | +14.95 | +0.47 | held |
| 2026-11-11 | KOMPL | norway | +5.45 | +5.15 | -0.30 | held |
| 2026-11-11 | ASM | netherlands | +6.70 | +6.97 | +0.27 | held |
| 2026-11-11 | APR | norway | -12.79 | -12.53 | +0.26 | held |
| 2026-11-11 | DVL | poland | +5.00 | +5.00 | +0.00 | held |
| 2026-11-11 | GNS | poland | +12.23 | +12.23 | +0.00 | held |
| 2026-11-12 | OBCK | germany | -9.79 | -16.60 | -6.81 | extended |
| 2026-11-12 | STG | denmark | +9.33 | +13.73 | +4.40 | extended |
| 2026-11-12 | SUS | sweden | -8.18 | -10.83 | -2.65 | extended |
| 2026-11-12 | ENDUR | norway | +5.69 | +8.31 | +2.62 | extended |
| 2026-11-12 | MEKO | sweden | -16.38 | -18.81 | -2.43 | extended |
| 2026-11-12 | YSN | germany | -15.20 | -17.09 | -1.89 | extended |
| 2026-11-12 | MTHH | denmark | +12.11 | +10.45 | -1.66 | faded |
| 2026-11-12 | FG | sweden | +13.42 | +11.85 | -1.57 | faded |
| 2026-11-12 | EDV | uk | -6.93 | -8.46 | -1.53 | extended |
| 2026-11-12 | ALCE | switzerland | +7.21 | +5.95 | -1.26 | faded |
| 2026-11-12 | YPSN | switzerland | +4.35 | +5.60 | +1.25 | extended |
| 2026-11-12 | NORBT | norway | +12.95 | +14.11 | +1.16 | extended |
| 2026-11-12 | BITTI | finland | -4.20 | -4.93 | -0.73 | held |
| 2026-11-12 | FLS | denmark | -5.05 | -5.55 | -0.50 | held |
| 2026-11-12 | WAC | germany | -9.61 | -10.04 | -0.43 | held |
| 2026-11-12 | BRBY | uk | +8.42 | +8.01 | -0.41 | held |
| 2026-11-12 | ADEN | switzerland | +15.00 | +14.74 | -0.26 | held |
| 2026-11-12 | BME | uk | +20.84 | +20.93 | +0.09 | held |
| 2026-11-12 | SIVE | sweden | -8.33 | -8.39 | -0.06 | held |
| 2026-11-13 | ERA | france | -5.86 | -10.64 | -4.78 | extended |
| 2026-11-13 | HEM | sweden | -10.50 | -13.40 | -2.90 | extended |
| 2026-11-13 | CMB | italy | +9.30 | +6.64 | -2.66 | faded |
| 2026-11-13 | OHB | germany | -5.50 | -8.10 | -2.60 | extended |
| 2026-11-13 | S92 | germany | -5.64 | -8.23 | -2.59 | extended |
| 2026-11-13 | GENO | norway | -5.41 | -6.82 | -1.41 | extended |
| 2026-11-13 | WISE | uk | +6.41 | +7.68 | +1.27 | extended |
| 2026-11-13 | TOR | poland | -6.05 | -6.86 | -0.81 | held |
| 2026-11-13 | BOUV | norway | +4.52 | +5.30 | +0.78 | held |
| 2026-11-13 | BMAG | austria | -5.61 | -5.01 | +0.60 | held |
| 2026-11-13 | FCT | italy | -3.73 | -4.28 | -0.55 | held |
| 2026-11-13 | PAX | sweden | +7.52 | +8.00 | +0.48 | held |
| 2026-11-13 | ANA | spain | -7.62 | -7.98 | -0.36 | held |
| 2026-11-13 | ANE | spain | -7.17 | -6.89 | +0.28 | held |
| 2026-11-13 | CNA | uk | +3.59 | +3.81 | +0.22 | held |
| 2026-11-13 | AKAST | norway | -22.71 | -22.63 | +0.08 | held |
| 2026-11-13 | GRE | spain | -4.51 | -4.51 | +0.00 | held |

## Method & caveats

| Field | Value |
|---|---|
| Drift | `Chg %` (settled) minus `Move @08:00`, recomputed from the two moves |
| Drift line | 1pp - the line the scanner's own settle summary uses |
| Paths | held ≤ 1pp; otherwise reversed (sign change), extended (further from zero), faded (back toward zero) |
| Median | the true median; the artifact prints the upper-middle value |
| Readable market | at least 5 compared rows |
| Not covered | the US rows (open at 12:15 ET), and the ASX and APAC/Gulf rows (already settled at 08:00 ET) |

## Source health

| Session | Settled file | Settled table | Morning file | Δ disagreements |
|---|---|---|---|---|
| 2026-11-11 | `earnings/2026-11-11-reactions-settled.md` | found | found | 0 |
| 2026-11-12 | `earnings/2026-11-12-reactions-settled.md` | found | found | 0 |
| 2026-11-13 | `earnings/2026-11-13-reactions-settled.md` | found | found | 0 |

