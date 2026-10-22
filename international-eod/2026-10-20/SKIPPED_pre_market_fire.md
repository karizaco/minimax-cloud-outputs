# Cron #5 eod-international-daily — SKIPPED (pre-market fire)
- Date (ET): 2026-10-20
- Fire time (ET): 05:32  (UTC: 2026-10-20T09:32:13Z)
- Intended schedule: 16:35 ET weekdays (post-close)
- Reason: cron fired ~11h before the post-close window. No EOD data exists yet for any
  of the 16 regions:
    - JP cash close (today): ~10:00 ET (still ~4.5h away)
    - AU cash close (today): ~16:00 ET (still ~10.5h away)
    - EU cash close (today): ~11:30 ET (still ~6h away)
- Window-check flags: WEEKDAYS_ONLY=true (today=Tue, ok), MARKET_HOURS_ONLY=false,
  DAY_OF_WEEK=0. No post-close hour gate configured — scheduler is coarse (daily).
- Action: exit cleanly per cron rule #4 (no degraded version on out-of-window fires).
- _source: out_of_window_pre_market
- Note: 12th consecutive pre-market fire. Scheduler lacks an hour-of-day gate;
  a post-close hour check in the window preamble would silence these silently.
