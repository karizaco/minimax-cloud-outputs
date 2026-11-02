# Cron #5 eod-international-daily — SKIPPED (pre-market fire)
- Date (ET): 2026-10-13
- Fire time (ET): 05:57  (UTC: 2026-10-13T09:57:53Z)
- Reason: cron fired at 05:57 ET, ~10.5h before the intended 16:35 ET post-close window.
  No EOD data is yet available for any of the 16 regions:
    - EU cash close (today): ~11:30 ET (still ~5.5h away)
    - JP cash close (today): ~10:00 ET (still ~4h away)
    - US cash close (today): 16:00 ET (still ~10h away)
- Window-check flags: WEEKDAYS_ONLY=true (today=Tue, ok), MARKET_HOURS_ONLY=false,
  DAY_OF_WEEK=0. No post-close hour gate configured — scheduler coarse.
- Action: exit cleanly per cron rule #4 (no degraded version on out-of-window fires).
- _source: out_of_window_pre_market
