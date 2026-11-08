# Skipped-fire markers

Historical `SKIPPED_*.md` markers written by the cron fleet when a routine's in-prompt window
check skipped a fire. They are kept as an audit trail of when skips happened and why.

**These are fossils.** The day-of-week now lives in the scheduler, so the weekend branches that
produced most of these can no longer fire — the 2026-10-31 window-check rewrite replaced them
with a market-holiday guard, which is the only gate a cron expression cannot express. The
2026-10-03..2026-10-24 cluster is the Token Plan quota wall (error 2067): sessions died at
their scheduled time, and the platform re-dispatched them.

File names carry the original date where the original path did not (`<date>_SKIPPED_*.md`).
