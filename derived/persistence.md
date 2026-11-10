# Persistence — how long a name stays on the board

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv (no source file is modified) · **Built:** 2026-11-10 · **Covers:** boards dated 2026-10-22 → 2026-11-06 (12 dates) · read-only

> **Deviations, stated up front.**
> 
> 1. **This file is not written by a cron.** It is derived from artifacts that are.
>    It is as current as the newest dated directory when it was built, and it will not
>    update itself when the next screen lands. Regenerate with
>    `python3 scripts/build_persistence.py`.
> 2. **It does not modify `daily-sweep.md`.** The streak column a reader wants in the
>    sweep lives here instead, because that file is a cron product and this builder
>    must not become a second writer on it.
> 3. **20 date(s) published no readable Tier-A board** and are not counted
>    as boards — see *Coverage* below. A streak spanning one of them is not broken
>    by a run that produced nothing.

## What this says

Across 12 Tier-A boards the names that recur are:

| Ticker | Days on Tier-A | First seen | Last seen | Current streak | Longest streak |
|---|---|---|---|---|---|
| MRNA | 4 | 2026-10-30 | 2026-11-06 | 1 | 2 |
| CDNA | 3 | 2026-10-30 | 2026-11-04 | 0 | 2 |
| FIGS | 3 | 2026-10-29 | 2026-11-03 | 0 | 2 |
| FTAI | 3 | 2026-10-30 | 2026-11-04 | 0 | 2 |
| CAI | 2 | 2026-11-02 | 2026-11-03 | 0 | 2 |
| HTFL | 2 | 2026-10-30 | 2026-11-02 | 0 | 2 |
| KOD | 2 | 2026-10-30 | 2026-11-02 | 0 | 2 |
| KVYO | 2 | 2026-11-03 | 2026-11-04 | 0 | 2 |
| PRME | 2 | 2026-10-28 | 2026-10-29 | 0 | 2 |
| PURR | 2 | 2026-10-30 | 2026-11-02 | 0 | 2 |

The table above is a **count of appearances**, not a judgement about the names.
A name on a long streak has been converging across several screens; a name with
`days 1` appeared once and may not be back. The two are different signals and a
single-day sweep cannot tell them apart.

### New to the 2026-11-06 board

| Ticker | Board |
|---|---|
| ACHC | tier-a |
| APP | tier-a |
| FUN | tier-a |
| MRNA | tier-a |
| RUN | tier-a |
| SEZL | tier-a |
| U | tier-a |
| XERS | tier-a |
| ACHC | focus |
| APP | focus |
| FUN | focus |
| JOBY | focus |
| MRNA | focus |
| RUN | focus |
| SEZL | focus |
| U | focus |
| WRBY | focus |
| XERS | focus |

### Off the board as of 2026-11-06

The mirror of the arrivals table: what left, and after how long.

| Ticker | Board | Last seen | Streak at exit | Days on board |
|---|---|---|---|---|
| DUOL | tier-a | 2026-11-05 | 1 | 1 |
| KD | tier-a | 2026-11-05 | 1 | 1 |
| LIVN | tier-a | 2026-11-05 | 1 | 1 |
| OUST | tier-a | 2026-11-05 | 1 | 1 |
| VRDN | tier-a | 2026-11-05 | 1 | 1 |
| XNCR | tier-a | 2026-11-05 | 1 | 1 |
| ARRY | focus | 2026-11-05 | 1 | 1 |
| CRCT | focus | 2026-11-05 | 1 | 1 |
| DUOL | focus | 2026-11-05 | 1 | 1 |
| ENOV | focus | 2026-11-05 | 1 | 1 |
| HELE | focus | 2026-11-05 | 1 | 1 |
| KD | focus | 2026-11-05 | 1 | 1 |
| LIVN | focus | 2026-11-05 | 1 | 1 |
| OUST | focus | 2026-11-05 | 1 | 2 |
| XYZ | focus | 2026-11-05 | 1 | 1 |
| YOU | focus | 2026-11-05 | 1 | 1 |

## The latest board, with streaks

Tier-A on 2026-11-06, with the persistence column a sweep table does not carry.

| Ticker | Days on Tier-A | Current streak | Longest streak | Focus days |
|---|---|---|---|---|
| RUN | 1 | 1 | 1 | 1 |
| SEZL | 1 | 1 | 1 | 1 |
| XERS | 1 | 1 | 1 | 1 |
| ACHC | 1 | 1 | 1 | 1 |
| MRNA | 4 | 1 | 2 | 5 |
| APP | 1 | 1 | 1 | 1 |
| U | 1 | 1 | 1 | 1 |
| FUN | 1 | 1 | 1 | 1 |

## Coverage

| Board | Dated directories | Readable boards |
|---|---|---|
| tier-a | 32 | 12 |
| focus | 32 | 12 |

Dates that published no readable Tier-A board:

| Date | Why it is not counted |
|---|---|
| 2026-09-28 | no tier-a.csv |
| 2026-09-29 | no tier-a.csv |
| 2026-09-30 | no tier-a.csv |
| 2026-10-01 | no tier-a.csv |
| 2026-10-02 | no tier-a.csv |
| 2026-10-03 | no tier-a.csv |
| 2026-10-05 | no tier-a.csv |
| 2026-10-06 | no tier-a.csv |
| 2026-10-07 | no tier-a.csv |
| 2026-10-08 | no tier-a.csv |
| 2026-10-09 | no tier-a.csv |
| 2026-10-12 | no tier-a.csv |
| 2026-10-16 | no tier-a.csv |
| 2026-10-19 | no tier-a.csv (tier-a.md exists - the run published no rows) |
| 2026-10-20 | no tier-a.csv |
| 2026-10-21 | no tier-a.csv |
| 2026-10-24 | no tier-a.csv |
| 2026-10-31 | no tier-a.csv |
| 2026-11-07 | no tier-a.csv |
| 2026-11-09 | no tier-a.csv (tier-a.md exists - the run published no rows) |

## How to read it

`persistence.json` beside this file carries the same join with every date a
name appeared.
The rule for this artifact is the one the decision-record contract states:
**it joins, it does not restate.** Every value here is a count or a date copied
from a dated CSV. No name is scored, ranked or interpreted.

Column drift the builder tolerates, and reports rather than hides: the ticker is
`symbol` on 2026-10-22/23 and 2026-11-04 onward, `ticker` on 2026-10-28 through
2026-11-03, and `name` on 2026-10-26/27 where that column holds symbols.

