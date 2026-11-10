# Run ledger — which routine published what, and when

**Source:** derived read of the published artifacts, against the schedule in the migration repo's ROSTER.md (read 2026-11-09); no source file is modified · **Built:** 2026-11-10 · **Covers:** 351 artifact-date rows across 23 routines and 15 trading sessions · read-only

> **Read this before the table.**
>
> 1. **A `missing` row is a fact about THIS REPO, not about the routine.**
>    A routine can fire and fail to push, and a repo cannot tell those
>    apart. The row says the artifact is not here; it does not say the
>    routine did not run.
> 2. **The schedule is the roster's, copied here.** A derived view should not
>    depend on a file in another repo being present. When the roster
>    changes, this constant changes with it.
> 3. **A routine's first publication sets its onset.** A day before a
>    routine had published anything here is not a miss - the fleet was still
>    starting up. Those rows are counted apart.
> 4. **A weekday routine is expected on a TRADING day.** The trading-day
>    calendar is the one `us-eod/` itself records, so a holiday is not a miss.

## Coverage

| State | Rows |
|---|---|
| published, on schedule | 228 |
| published, off schedule | 14 |
| published, before the calendar this repo records | 58 |
| published, after the calendar this repo records | 0 |
| expected but not present in this repo | 24 |
| expected, before the routine had started publishing here | 27 |
| **total** | **351** |

## By routine

| Routine | Fire | Schedule | Published | Missing | Off schedule | Last published here |
|---|---|---|---|---|---|---|
| 01-weekly-mcp-health-check | 02:00 | Sun | 0 | 0 | 2 | — |
| 19-earnings-reminder-daily | 06:00 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |
| 02-asia-pre-market-reactions | 06:30 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |
| 15-earnings-reaction-scanner | 08:00 | Mon-Fri | 8 | 3 | 1 | 2026-11-09 |
| 08-stock-screener-pre-market-gapper | 08:30 | Mon-Fri | 13 | 2 | 0 | 2026-11-09 |
| 26-agentic-pre-market-brief | 08:30 | Mon-Fri | 14 | 1 | 1 | 2026-11-09 |
| 25-ntrt-gap-brief-daily | 09:00 | Mon-Fri | 15 | 1 | 0 | 2026-11-09 |
| 26b-agentic-pre-market-brief-refresh-0920 | 09:20 | Mon-Fri | 4 | 0 | 0 | 2026-11-09 |
| 07-stock-screener-focus-rvol-09:45 | 09:45 | Mon-Fri | 13 | 2 | 0 | 2026-11-09 |
| 17-us-stocks-in-play-open | 09:50 | Mon-Fri | 4 | 11 | 0 | 2026-11-09 |
| 12-cross-asset-correlation-snapshot | 10:00 | Mon-Fri | 9 | 2 | 1 | 2026-11-09 |
| 10-stock-screener-breadth-snapshot | 14:00 | Mon-Fri | 11 | 0 | 0 | 2026-11-09 |
| 13-macro-calendar-midweek | 14:00 | Wed | 3 | 0 | 0 | 2026-11-04 |
| 06-stock-screener-pattern-study-backlog | 15:00 | Sat | 0 | 0 | 3 | — |
| 14-macro-calendar-week-ahead | 15:00 | Sun | 0 | 0 | 2 | — |
| 17-us-stocks-in-play | 15:50 | Mon-Fri | 20 | 0 | 0 | 2026-11-09 |
| 04-reversal-bullish-3:55 | 15:55 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |
| 20-eod-watchlist-csv-snapshot | 16:00 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |
| 05-eod-international-daily | 16:30 | Mon-Fri | 11 | 0 | 0 | 2026-11-09 |
| 16-unusual-options-flow-daily | 16:35 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |
| 22-weekly-market-recap-preview | 17:47 | Sun | 0 | 0 | 4 | — |
| 09-stock-screener-daily-sweep-18:30 | 18:30 | Mon-Fri | 13 | 2 | 0 | 2026-11-09 |
| 23-agentic-post-market-brief | 22:30 | Mon-Fri | 15 | 0 | 0 | 2026-11-09 |

**What this table means.** `Published` counts the artifact-date pairs this
repo holds for that routine on a day its schedule covers. `Missing` counts the
days it should have published and this repo does not hold. The gap between
the two columns and the roster's own `Last delivered` column is the thing
this artifact exists to show.

## Published off schedule

| Date | Routine | Artifact |
|---|---|---|
| 2026-10-24 | 06-stock-screener-pattern-study-backlog | `daily-screens/2026-10-24/weekly-ipo.md` |
| 2026-10-24 | 15-earnings-reaction-scanner | `earnings/2026-10-24-reactions.md` |
| 2026-10-25 | 12-cross-asset-correlation-snapshot | `cross-asset/2026-10-25.md` |
| 2026-10-25 | 26-agentic-pre-market-brief | `daily-briefs/2026-10-25-pre-market.md` |
| 2026-10-31 | 06-stock-screener-pattern-study-backlog | `daily-screens/2026-10-31/weekly-ipo.md` |
| 2026-11-01 | 14-macro-calendar-week-ahead | `macro-calendar/2026-11-01-week-ahead.md` |
| 2026-11-01 | 22-weekly-market-recap-preview | `weekly/2026-11-01-preview-tldr.md` |
| 2026-11-01 | 22-weekly-market-recap-preview | `weekly/2026-11-01-preview.md` |
| 2026-11-07 | 06-stock-screener-pattern-study-backlog | `daily-screens/2026-11-07/weekly-ipo.md` |
| 2026-11-08 | 14-macro-calendar-week-ahead | `macro-calendar/2026-11-08-week-ahead.md` |
| 2026-11-08 | 22-weekly-market-recap-preview | `weekly/2026-11-08-preview-tldr.md` |
| 2026-11-08 | 22-weekly-market-recap-preview | `weekly/2026-11-08-preview.md` |
| 2026-W44 | 01-weekly-mcp-health-check | `mcp-health/2026-W44.md` |
| 2026-W45 | 01-weekly-mcp-health-check | `mcp-health/2026-W45.md` |

An artifact on a day the schedule does not cover is not an error - a
routine can be re-run manually, and a holiday can shift a fire. It is
counted apart from the scheduled runs so the two are not confused.

## Expected but not present here

| Date | Routine | Fire |
|---|---|---|
| 2026-10-20 | 09-stock-screener-daily-sweep-18:30 | 18:30 |
| 2026-10-20 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-20 | 25-ntrt-gap-brief-daily | 09:00 |
| 2026-10-21 | 09-stock-screener-daily-sweep-18:30 | 18:30 |
| 2026-10-21 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-22 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-23 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-26 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-27 | 15-earnings-reaction-scanner | 08:00 |
| 2026-10-27 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-28 | 15-earnings-reaction-scanner | 08:00 |
| 2026-10-28 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-29 | 07-stock-screener-focus-rvol-09:45 | 09:45 |
| 2026-10-29 | 08-stock-screener-pre-market-gapper | 08:30 |
| 2026-10-29 | 12-cross-asset-correlation-snapshot | 10:00 |
| 2026-10-30 | 07-stock-screener-focus-rvol-09:45 | 09:45 |
| 2026-10-30 | 08-stock-screener-pre-market-gapper | 08:30 |
| 2026-10-30 | 12-cross-asset-correlation-snapshot | 10:00 |
| 2026-10-30 | 15-earnings-reaction-scanner | 08:00 |
| 2026-10-30 | 17-us-stocks-in-play-open | 09:50 |
| 2026-10-30 | 26-agentic-pre-market-brief | 08:30 |
| 2026-11-02 | 17-us-stocks-in-play-open | 09:50 |
| 2026-11-03 | 17-us-stocks-in-play-open | 09:50 |
| 2026-11-04 | 17-us-stocks-in-play-open | 09:50 |

## Every published artifact

| Date | Routine | State | Artifact | Names |
|---|---|---|---|---|
| 2026-09-28 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-09-28.md` | — |
| 2026-09-28 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-09-28/reversal-bullish-3_55.md` | — |
| 2026-09-28 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-09-28/focus-rvol-snapshot.md` | — |
| 2026-09-28 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-09-28/pre-market-gapper.md` | — |
| 2026-09-29 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-09-29.md` | — |
| 2026-09-29 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-09-29/reversal-bullish-3_55.md` | — |
| 2026-09-29 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-09-29/focus-rvol-snapshot.md` | — |
| 2026-09-29 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-09-29/pre-market-gapper.md` | — |
| 2026-09-30 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-09-30.md` | — |
| 2026-09-30 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-09-30/reversal-bullish-3_55.md` | — |
| 2026-09-30 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-09-30/focus-rvol-snapshot.md` | — |
| 2026-09-30 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-09-30/pre-market-gapper.md` | — |
| 2026-10-01 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-10-01.md` | — |
| 2026-10-01 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-01/reversal-bullish-3_55.md` | — |
| 2026-10-01 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-01/focus-rvol-snapshot.md` | — |
| 2026-10-01 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-01/pre-market-gapper.md` | — |
| 2026-10-02 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-10-02.md` | — |
| 2026-10-02 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-02/reversal-bullish-3_55.md` | — |
| 2026-10-02 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-02/focus-rvol-snapshot.md` | — |
| 2026-10-02 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-02/pre-market-gapper.md` | — |
| 2026-10-03 | 06-stock-screener-pattern-study-backlog | published_before_calendar | `daily-screens/2026-10-03/weekly-ipo.md` | — |
| 2026-10-05 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-05/reversal-bullish-3_55.md` | — |
| 2026-10-05 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-05/focus-rvol-snapshot.md` | — |
| 2026-10-05 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-05/pre-market-gapper.md` | — |
| 2026-10-06 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-10-06.md` | — |
| 2026-10-06 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-06/reversal-bullish-3_55.md` | — |
| 2026-10-06 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-06/focus-rvol-snapshot.md` | — |
| 2026-10-06 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-06/pre-market-gapper.md` | — |
| 2026-10-07 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-07/reversal-bullish-3_55.md` | — |
| 2026-10-07 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-07/focus-rvol-snapshot.md` | — |
| 2026-10-08 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-08/reversal-bullish-3_55.md` | — |
| 2026-10-08 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-08/focus-rvol-snapshot.md` | — |
| 2026-10-08 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-08/pre-market-gapper.md` | — |
| 2026-10-09 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-09/reversal-bullish-3_55.md` | — |
| 2026-10-12 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-12/reversal-bullish-3_55.md` | — |
| 2026-10-12 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-12/focus-rvol-snapshot.md` | — |
| 2026-10-13 | 17-us-stocks-in-play | published_before_calendar | `us-stocks-in-play/2026-10-13-open.md` | — |
| 2026-10-13 | 17-us-stocks-in-play-open | published_before_calendar | `us-stocks-in-play/2026-10-13-open.md` | — |
| 2026-10-13 | 25-ntrt-gap-brief-daily | published_before_calendar | `ntrt/2026-10-13.md` | — |
| 2026-10-14 | 17-us-stocks-in-play | published_before_calendar | `us-stocks-in-play/2026-10-14.md` | — |
| 2026-10-14 | 19-earnings-reminder-daily | published_before_calendar | `earnings/2026-10-14-reminders.md` | — |
| 2026-10-15 | 17-us-stocks-in-play | published_before_calendar | `us-stocks-in-play/2026-10-15.md` | — |
| 2026-10-15 | 25-ntrt-gap-brief-daily | published_before_calendar | `ntrt/2026-10-15.md` | — |
| 2026-10-16 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-16/reversal-bullish-3_55.md` | — |
| 2026-10-16 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-16/focus-rvol-snapshot.md` | — |
| 2026-10-16 | 16-unusual-options-flow-daily | published_before_calendar | `options-flow/2026-10-16.md` | — |
| 2026-10-16 | 17-us-stocks-in-play | published_before_calendar | `us-stocks-in-play/2026-10-16.md` | — |
| 2026-10-18 | 14-macro-calendar-week-ahead | published_before_calendar | `macro-calendar/2026-10-18-week-ahead.md` | — |
| 2026-10-19 | 02-asia-pre-market-reactions | published_before_calendar | `asia-pre-market/2026-10-19.md` | — |
| 2026-10-19 | 04-reversal-bullish-3:55 | published_before_calendar | `daily-screens/2026-10-19/reversal-bullish-3_55.md` | — |
| 2026-10-19 | 07-stock-screener-focus-rvol-09:45 | published_before_calendar | `daily-screens/2026-10-19/focus-rvol-snapshot.md` | — |
| 2026-10-19 | 08-stock-screener-pre-market-gapper | published_before_calendar | `daily-screens/2026-10-19/pre-market-gapper.md` | — |
| 2026-10-19 | 09-stock-screener-daily-sweep-18:30 | published_before_calendar | `daily-screens/2026-10-19/daily-sweep.md` | — |
| 2026-10-19 | 16-unusual-options-flow-daily | published_before_calendar | `options-flow/2026-10-19.md` | — |
| 2026-10-19 | 17-us-stocks-in-play | published_before_calendar | `us-stocks-in-play/2026-10-19.md` | — |
| 2026-10-19 | 19-earnings-reminder-daily | published_before_calendar | `earnings/2026-10-19-reminders.md` | — |
| 2026-10-19 | 25-ntrt-gap-brief-daily | published_before_calendar | `ntrt/2026-10-19.md` | — |
| 2026-10-19 | 26-agentic-pre-market-brief | published_before_calendar | `daily-briefs/2026-10-19-pre-market.md` | — |
| 2026-10-20 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-20.md` | — |
| 2026-10-20 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-20/reversal-bullish-3_55.md` | — |
| 2026-10-20 | 05-eod-international-daily | before_onset | `None` | — |
| 2026-10-20 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-20/focus-rvol-snapshot.md` | — |
| 2026-10-20 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-20/pre-market-gapper.md` | — |
| 2026-10-20 | 10-stock-screener-breadth-snapshot | before_onset | `None` | — |
| 2026-10-20 | 12-cross-asset-correlation-snapshot | before_onset | `None` | — |
| 2026-10-20 | 15-earnings-reaction-scanner | before_onset | `None` | — |
| 2026-10-20 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-20.md` | — |
| 2026-10-20 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-20.md` | — |
| 2026-10-20 | 19-earnings-reminder-daily | published | `earnings/2026-10-20-reminders.md` | — |
| 2026-10-20 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-20.csv` | 5714 |
| 2026-10-20 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-20-post-market.md` | — |
| 2026-10-20 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-20-pre-market.md` | — |
| 2026-10-20 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-21 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-21.md` | — |
| 2026-10-21 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-21/reversal-bullish-3_55.md` | — |
| 2026-10-21 | 05-eod-international-daily | before_onset | `None` | — |
| 2026-10-21 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-21/focus-rvol-snapshot.md` | — |
| 2026-10-21 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-21/pre-market-gapper.md` | — |
| 2026-10-21 | 10-stock-screener-breadth-snapshot | before_onset | `None` | — |
| 2026-10-21 | 12-cross-asset-correlation-snapshot | before_onset | `None` | — |
| 2026-10-21 | 13-macro-calendar-midweek | published | `macro-calendar/2026-10-21-midweek.md` | — |
| 2026-10-21 | 15-earnings-reaction-scanner | before_onset | `None` | — |
| 2026-10-21 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-21.md` | — |
| 2026-10-21 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-21.md` | — |
| 2026-10-21 | 19-earnings-reminder-daily | published | `earnings/2026-10-21-reminders.md` | — |
| 2026-10-21 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-21.csv` | 5714 |
| 2026-10-21 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-21-post-market.md` | — |
| 2026-10-21 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-21.md` | — |
| 2026-10-21 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-21-pre-market.md` | — |
| 2026-10-21 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-22 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-22.md` | — |
| 2026-10-22 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-22/reversal-bullish-3_55.md` | — |
| 2026-10-22 | 05-eod-international-daily | before_onset | `None` | — |
| 2026-10-22 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-22/focus-rvol-snapshot.md` | — |
| 2026-10-22 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-22/pre-market-gapper.md` | — |
| 2026-10-22 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-22/daily-sweep.md` | — |
| 2026-10-22 | 10-stock-screener-breadth-snapshot | before_onset | `None` | — |
| 2026-10-22 | 12-cross-asset-correlation-snapshot | before_onset | `None` | — |
| 2026-10-22 | 15-earnings-reaction-scanner | before_onset | `None` | — |
| 2026-10-22 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-22.md` | — |
| 2026-10-22 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-22.md` | — |
| 2026-10-22 | 19-earnings-reminder-daily | published | `earnings/2026-10-22-reminders.md` | — |
| 2026-10-22 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-22.csv` | 5718 |
| 2026-10-22 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-22-post-market.md` | — |
| 2026-10-22 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-22.md` | — |
| 2026-10-22 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-22-pre-market.md` | — |
| 2026-10-22 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-23 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-23.md` | — |
| 2026-10-23 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-23/reversal-bullish-3_55.md` | — |
| 2026-10-23 | 05-eod-international-daily | before_onset | `None` | — |
| 2026-10-23 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-23/focus-rvol-snapshot.md` | — |
| 2026-10-23 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-23/pre-market-gapper.md` | — |
| 2026-10-23 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-23/daily-sweep.md` | — |
| 2026-10-23 | 10-stock-screener-breadth-snapshot | before_onset | `None` | — |
| 2026-10-23 | 12-cross-asset-correlation-snapshot | before_onset | `None` | — |
| 2026-10-23 | 15-earnings-reaction-scanner | before_onset | `None` | — |
| 2026-10-23 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-23.md` | — |
| 2026-10-23 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-23.md` | — |
| 2026-10-23 | 19-earnings-reminder-daily | published | `earnings/2026-10-23-reminders.md` | — |
| 2026-10-23 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-23.csv` | 5718 |
| 2026-10-23 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-23-post-market.md` | — |
| 2026-10-23 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-23-session.md` | — |
| 2026-10-23 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-23.md` | — |
| 2026-10-23 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-23-pre-market.md` | — |
| 2026-10-23 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-24 | 06-stock-screener-pattern-study-backlog | published_off_schedule | `daily-screens/2026-10-24/weekly-ipo.md` | — |
| 2026-10-24 | 15-earnings-reaction-scanner | published_off_schedule | `earnings/2026-10-24-reactions.md` | — |
| 2026-10-25 | 12-cross-asset-correlation-snapshot | published_off_schedule | `cross-asset/2026-10-25.md` | — |
| 2026-10-25 | 26-agentic-pre-market-brief | published_off_schedule | `daily-briefs/2026-10-25-pre-market.md` | — |
| 2026-10-26 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-26.md` | — |
| 2026-10-26 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-26/reversal-bullish-3_55.md` | — |
| 2026-10-26 | 05-eod-international-daily | published | `international-eod/2026-10-26/summary.md` | — |
| 2026-10-26 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-26/focus-rvol-snapshot.md` | — |
| 2026-10-26 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-26/pre-market-gapper.md` | — |
| 2026-10-26 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-26/daily-sweep.md` | — |
| 2026-10-26 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-10-26/breadth-snapshot.md` | — |
| 2026-10-26 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-10-26.md` | — |
| 2026-10-26 | 15-earnings-reaction-scanner | published | `earnings/2026-10-26-reactions.md` | — |
| 2026-10-26 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-26.md` | — |
| 2026-10-26 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-26.md` | — |
| 2026-10-26 | 19-earnings-reminder-daily | published | `earnings/2026-10-26-reminders.md` | — |
| 2026-10-26 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-26.csv` | 5716 |
| 2026-10-26 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-26-post-market.md` | — |
| 2026-10-26 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-26.md` | — |
| 2026-10-26 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-26-pre-market.md` | — |
| 2026-10-26 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-27 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-27.md` | — |
| 2026-10-27 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-27/reversal-bullish-3_55.md` | — |
| 2026-10-27 | 05-eod-international-daily | published | `international-eod/2026-10-27/summary.md` | — |
| 2026-10-27 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-27/focus-rvol-snapshot.md` | — |
| 2026-10-27 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-27/pre-market-gapper.md` | — |
| 2026-10-27 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-27/daily-sweep.md` | — |
| 2026-10-27 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-10-27/breadth-snapshot.md` | — |
| 2026-10-27 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-10-27.md` | — |
| 2026-10-27 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-27.md` | — |
| 2026-10-27 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-27.md` | — |
| 2026-10-27 | 19-earnings-reminder-daily | published | `earnings/2026-10-27-reminders.md` | — |
| 2026-10-27 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-27.csv` | 5716 |
| 2026-10-27 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-27-post-market.md` | — |
| 2026-10-27 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-27.md` | — |
| 2026-10-27 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-27-pre-market.md` | — |
| 2026-10-27 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-28 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-28.md` | — |
| 2026-10-28 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-28/reversal-bullish-3_55.md` | — |
| 2026-10-28 | 05-eod-international-daily | published | `international-eod/2026-10-28/summary.md` | — |
| 2026-10-28 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-10-28/focus-rvol-snapshot.md` | — |
| 2026-10-28 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-10-28/pre-market-gapper.md` | — |
| 2026-10-28 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-28/daily-sweep.md` | — |
| 2026-10-28 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-10-28/breadth-snapshot.md` | — |
| 2026-10-28 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-10-28.md` | — |
| 2026-10-28 | 13-macro-calendar-midweek | published | `macro-calendar/2026-10-28-midweek.md` | — |
| 2026-10-28 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-28.md` | — |
| 2026-10-28 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-28.md` | — |
| 2026-10-28 | 19-earnings-reminder-daily | published | `earnings/2026-10-28-reminders.md` | — |
| 2026-10-28 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-28.csv` | 4899 |
| 2026-10-28 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-28-post-market.md` | — |
| 2026-10-28 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-28.md` | — |
| 2026-10-28 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-28-pre-market.md` | — |
| 2026-10-28 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-29 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-29.md` | — |
| 2026-10-29 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-29/reversal-bullish-3_55.md` | — |
| 2026-10-29 | 05-eod-international-daily | published | `international-eod/2026-10-29/summary.md` | — |
| 2026-10-29 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-29/daily-sweep.md` | — |
| 2026-10-29 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-10-29/breadth-snapshot.md` | — |
| 2026-10-29 | 15-earnings-reaction-scanner | published | `earnings/2026-10-29-reactions.md` | — |
| 2026-10-29 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-29.md` | — |
| 2026-10-29 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-29-pre-open.md` | — |
| 2026-10-29 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-29.md` | — |
| 2026-10-29 | 17-us-stocks-in-play-open | published | `us-stocks-in-play/2026-10-29-pre-open.md` | — |
| 2026-10-29 | 19-earnings-reminder-daily | published | `earnings/2026-10-29-reminders.md` | — |
| 2026-10-29 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-29.csv` | 4899 |
| 2026-10-29 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-29-post-market.md` | — |
| 2026-10-29 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-29.md` | — |
| 2026-10-29 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-10-29-pre-market.md` | — |
| 2026-10-29 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-30 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-10-30.md` | — |
| 2026-10-30 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-10-30/reversal-bullish-3_55.md` | — |
| 2026-10-30 | 05-eod-international-daily | published | `international-eod/2026-10-30/summary.md` | — |
| 2026-10-30 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-10-30/daily-sweep.md` | — |
| 2026-10-30 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-10-30/breadth-snapshot.md` | — |
| 2026-10-30 | 16-unusual-options-flow-daily | published | `options-flow/2026-10-30.md` | — |
| 2026-10-30 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-30-midday.md` | — |
| 2026-10-30 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-10-30.md` | — |
| 2026-10-30 | 19-earnings-reminder-daily | published | `earnings/2026-10-30-reminders.md` | — |
| 2026-10-30 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-10-30.csv` | 4898 |
| 2026-10-30 | 23-agentic-post-market-brief | published | `daily-briefs/2026-10-30-post-market.md` | — |
| 2026-10-30 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-10-30.md` | — |
| 2026-10-30 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-10-31 | 06-stock-screener-pattern-study-backlog | published_off_schedule | `daily-screens/2026-10-31/weekly-ipo.md` | — |
| 2026-11-01 | 14-macro-calendar-week-ahead | published_off_schedule | `macro-calendar/2026-11-01-week-ahead.md` | — |
| 2026-11-01 | 22-weekly-market-recap-preview | published_off_schedule | `weekly/2026-11-01-preview-tldr.md` | — |
| 2026-11-01 | 22-weekly-market-recap-preview | published_off_schedule | `weekly/2026-11-01-preview.md` | — |
| 2026-11-02 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-02.md` | — |
| 2026-11-02 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-02/reversal-bullish-3_55.md` | — |
| 2026-11-02 | 05-eod-international-daily | published | `international-eod/2026-11-02/summary.md` | — |
| 2026-11-02 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-02/focus-rvol-snapshot.md` | — |
| 2026-11-02 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-02/pre-market-gapper.md` | — |
| 2026-11-02 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-02/daily-sweep.md` | — |
| 2026-11-02 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-02/breadth-snapshot.md` | — |
| 2026-11-02 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-02.md` | — |
| 2026-11-02 | 15-earnings-reaction-scanner | published | `earnings/2026-11-02-reactions.md` | — |
| 2026-11-02 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-02.md` | — |
| 2026-11-02 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-02.md` | — |
| 2026-11-02 | 19-earnings-reminder-daily | published | `earnings/2026-11-02-reminders.md` | — |
| 2026-11-02 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-02.csv` | 4899 |
| 2026-11-02 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-02-post-market.md` | — |
| 2026-11-02 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-02.md` | — |
| 2026-11-02 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-02-pre-market.md` | — |
| 2026-11-02 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-11-03 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-03.md` | — |
| 2026-11-03 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-03/reversal-bullish-3_55.md` | — |
| 2026-11-03 | 05-eod-international-daily | published | `international-eod/2026-11-03/summary.md` | — |
| 2026-11-03 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-03/focus-rvol-snapshot.md` | — |
| 2026-11-03 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-03/pre-market-gapper.md` | — |
| 2026-11-03 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-03/daily-sweep.md` | — |
| 2026-11-03 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-03/breadth-snapshot.md` | — |
| 2026-11-03 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-03.md` | — |
| 2026-11-03 | 15-earnings-reaction-scanner | published | `earnings/2026-11-03-reactions.md` | — |
| 2026-11-03 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-03.md` | — |
| 2026-11-03 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-03.md` | — |
| 2026-11-03 | 19-earnings-reminder-daily | published | `earnings/2026-11-03-reminders.md` | — |
| 2026-11-03 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-03.csv` | 4896 |
| 2026-11-03 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-03-post-market.md` | — |
| 2026-11-03 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-03.md` | — |
| 2026-11-03 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-03-pre-market.md` | — |
| 2026-11-03 | 26b-agentic-pre-market-brief-refresh-0920 | before_onset | `None` | — |
| 2026-11-04 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-04.md` | — |
| 2026-11-04 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-04/reversal-bullish-3_55.md` | — |
| 2026-11-04 | 05-eod-international-daily | published | `international-eod/2026-11-04/summary.md` | — |
| 2026-11-04 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-04/focus-rvol-snapshot.md` | — |
| 2026-11-04 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-04/pre-market-gapper.md` | — |
| 2026-11-04 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-04/daily-sweep.md` | — |
| 2026-11-04 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-04/breadth-snapshot.md` | — |
| 2026-11-04 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-04.md` | — |
| 2026-11-04 | 13-macro-calendar-midweek | published | `macro-calendar/2026-11-04-midweek.md` | — |
| 2026-11-04 | 15-earnings-reaction-scanner | published | `earnings/2026-11-04-reactions.md` | — |
| 2026-11-04 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-04.md` | — |
| 2026-11-04 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-04.md` | — |
| 2026-11-04 | 19-earnings-reminder-daily | published | `earnings/2026-11-04-reminders.md` | — |
| 2026-11-04 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-04.csv` | 4895 |
| 2026-11-04 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-04-post-market.md` | — |
| 2026-11-04 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-04.md` | — |
| 2026-11-04 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-04-pre-market.md` | — |
| 2026-11-04 | 26b-agentic-pre-market-brief-refresh-0920 | published | `daily-briefs/2026-11-04-pre-market-refresh.md` | — |
| 2026-11-05 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-05.md` | — |
| 2026-11-05 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-05/reversal-bullish-3_55.md` | — |
| 2026-11-05 | 05-eod-international-daily | published | `international-eod/2026-11-05/summary.md` | — |
| 2026-11-05 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-05/focus-rvol-snapshot.md` | — |
| 2026-11-05 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-05/pre-market-gapper.md` | — |
| 2026-11-05 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-05/daily-sweep.md` | — |
| 2026-11-05 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-05/breadth-snapshot.md` | — |
| 2026-11-05 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-05.md` | — |
| 2026-11-05 | 15-earnings-reaction-scanner | published | `earnings/2026-11-05-reactions.md` | — |
| 2026-11-05 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-05.md` | — |
| 2026-11-05 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-05-open.md` | — |
| 2026-11-05 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-05.md` | — |
| 2026-11-05 | 17-us-stocks-in-play-open | published | `us-stocks-in-play/2026-11-05-open.md` | — |
| 2026-11-05 | 19-earnings-reminder-daily | published | `earnings/2026-11-05-reminders.md` | — |
| 2026-11-05 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-05.csv` | 4896 |
| 2026-11-05 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-05-post-market.md` | — |
| 2026-11-05 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-05.md` | — |
| 2026-11-05 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-05-pre-market.md` | — |
| 2026-11-05 | 26b-agentic-pre-market-brief-refresh-0920 | published | `daily-briefs/2026-11-05-pre-market-refresh.md` | — |
| 2026-11-06 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-06.md` | — |
| 2026-11-06 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-06/reversal-bullish-3_55.md` | — |
| 2026-11-06 | 05-eod-international-daily | published | `international-eod/2026-11-06/summary.md` | — |
| 2026-11-06 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-06/focus-rvol-snapshot.md` | — |
| 2026-11-06 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-06/pre-market-gapper.md` | — |
| 2026-11-06 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-06/daily-sweep.md` | — |
| 2026-11-06 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-06/breadth-snapshot.md` | — |
| 2026-11-06 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-06.md` | — |
| 2026-11-06 | 15-earnings-reaction-scanner | published | `earnings/2026-11-06-reactions.md` | — |
| 2026-11-06 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-06.md` | — |
| 2026-11-06 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-06-open.md` | — |
| 2026-11-06 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-06.md` | — |
| 2026-11-06 | 17-us-stocks-in-play-open | published | `us-stocks-in-play/2026-11-06-open.md` | — |
| 2026-11-06 | 19-earnings-reminder-daily | published | `earnings/2026-11-06-reminders.md` | — |
| 2026-11-06 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-06.csv` | 4892 |
| 2026-11-06 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-06-post-market.md` | — |
| 2026-11-06 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-06.md` | — |
| 2026-11-06 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-06-pre-market.md` | — |
| 2026-11-06 | 26b-agentic-pre-market-brief-refresh-0920 | published | `daily-briefs/2026-11-06-pre-market-refresh.md` | — |
| 2026-11-07 | 06-stock-screener-pattern-study-backlog | published_off_schedule | `daily-screens/2026-11-07/weekly-ipo.md` | — |
| 2026-11-08 | 14-macro-calendar-week-ahead | published_off_schedule | `macro-calendar/2026-11-08-week-ahead.md` | — |
| 2026-11-08 | 22-weekly-market-recap-preview | published_off_schedule | `weekly/2026-11-08-preview-tldr.md` | — |
| 2026-11-08 | 22-weekly-market-recap-preview | published_off_schedule | `weekly/2026-11-08-preview.md` | — |
| 2026-11-09 | 02-asia-pre-market-reactions | published | `asia-pre-market/2026-11-09.md` | — |
| 2026-11-09 | 04-reversal-bullish-3:55 | published | `daily-screens/2026-11-09/reversal-bullish-3_55.md` | — |
| 2026-11-09 | 05-eod-international-daily | published | `international-eod/2026-11-09/summary.md` | — |
| 2026-11-09 | 07-stock-screener-focus-rvol-09:45 | published | `daily-screens/2026-11-09/focus-rvol-snapshot.md` | — |
| 2026-11-09 | 08-stock-screener-pre-market-gapper | published | `daily-screens/2026-11-09/pre-market-gapper.md` | — |
| 2026-11-09 | 09-stock-screener-daily-sweep-18:30 | published | `daily-screens/2026-11-09/daily-sweep.md` | — |
| 2026-11-09 | 10-stock-screener-breadth-snapshot | published | `daily-screens/2026-11-09/breadth-snapshot.md` | — |
| 2026-11-09 | 12-cross-asset-correlation-snapshot | published | `cross-asset/2026-11-09.md` | — |
| 2026-11-09 | 15-earnings-reaction-scanner | published | `earnings/2026-11-09-reactions.md` | — |
| 2026-11-09 | 16-unusual-options-flow-daily | published | `options-flow/2026-11-09.md` | — |
| 2026-11-09 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-09-open.md` | — |
| 2026-11-09 | 17-us-stocks-in-play | published | `us-stocks-in-play/2026-11-09.md` | — |
| 2026-11-09 | 17-us-stocks-in-play-open | published | `us-stocks-in-play/2026-11-09-open.md` | — |
| 2026-11-09 | 19-earnings-reminder-daily | published | `earnings/2026-11-09-reminders.md` | — |
| 2026-11-09 | 20-eod-watchlist-csv-snapshot | published | `us-eod/2026-11-09.csv` | 4895 |
| 2026-11-09 | 23-agentic-post-market-brief | published | `daily-briefs/2026-11-09-post-market.md` | — |
| 2026-11-09 | 25-ntrt-gap-brief-daily | published | `ntrt/2026-11-09.md` | — |
| 2026-11-09 | 26-agentic-pre-market-brief | published | `daily-briefs/2026-11-09-pre-market.md` | — |
| 2026-11-09 | 26b-agentic-pre-market-brief-refresh-0920 | published | `daily-briefs/2026-11-09-pre-market-refresh.md` | — |
| 2026-W44 | 01-weekly-mcp-health-check | published_off_schedule | `mcp-health/2026-W44.md` | — |
| 2026-W45 | 01-weekly-mcp-health-check | published_off_schedule | `mcp-health/2026-W45.md` | — |

## Method and caveats

| Field | Value |
|---|---|
| Trading-day calendar | the `us-eod/*.csv` file set |
| Schedule | the migration repo's ROSTER.md, copied into this script |
| Date of an artifact | the date in its path |
| Names published | the row count of a CSV, or the count the artifact states |

