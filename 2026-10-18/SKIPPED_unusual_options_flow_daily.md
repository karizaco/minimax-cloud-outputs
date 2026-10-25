# Cron #16 unusual-options-flow-daily — SKIPPED

- Date (ET): 2026-10-18
- Time (ET): 16:31
- Day (ET): Sunday
- Reason: weekend — skill is a weekday job (`55 9 * * 1-5`); US equity/options markets closed
- No artifact produced. No scan run, no push (skip branch exits before push).

## Window-check discrepancy

The migration preamble's window check exits `window-check: OK` because its flags cannot
express a weekday constraint:

    WEEKDAYS_ONLY=false      <- should be true
    WEEKEND_ONLY=false
    MARKET_HOURS_ONLY=true   <- hour 16 passes
    DAY_OF_WEEK=0            <- no day constraint

Only the hour is enforced, so a Sunday 16:31 ET fire reads as "in window". The skill
specification this cron wraps states its own schedule as:

    Cron: `55 9 * * 1-5` America/New_York (weekdays, 09:55 ET — ~25 min after open so vol settles)

The cron's own CRITICAL REMINDER #4 covers this case directly — "If the cron fires outside
its intended window (e.g. holiday, **weekend when it should be weekday**), exit cleanly
with 'out-of-window: <reason>'. Do NOT run a degraded version." This run is that case, so
the literal script result was overridden on that rule.

**This is the second consecutive weekend skip** (previous: 2026-10-11, Sunday). The flags
have not been corrected between fires.

## Market state (verified, not assumed)

Yahoo chart data for NVDA, last 7 sessions:

    2026-10-08 Thu   230.48   118,697,400
    2026-10-09 Fri   229.28    84,645,600
    2026-10-12 Mon   226.32    70,690,300
    2026-10-13 Tue   228.52    84,036,900
    2026-10-14 Wed   221.30   118,730,100
    2026-10-15 Thu   217.23   127,087,900
    2026-10-16 Fri   214.13   120,855,100   <- last regular session

    2026-10-17 Sat   no session
    2026-10-18 Sun   no session   <- today

`regularMarketTime` = 2026-10-16 20:00 UTC = 2026-10-16 16:00 EDT (Friday close).

There is zero intraday options volume for 2026-10-18. A V/OI > 1 "unusual activity" scan
is undefined with no session; any output would be Friday's settled chain re-presented as
today's flow, which would be materially misleading.

## Data-source status (changed since the last weekend skip)

Re-checked this run:

- `mcp__tradingview-advanced__stock_options_unusual_activity` — still **absent** from the
  runtime. Not in the model tool list; `tool_search` returns 0 hits across tradingview /
  option / finance queries; the App/Connector catalog holds media-generation and credential
  tools only, with no market-data capability.
- The cron's advertised `mcp__yahoo_finance__*` — still **absent**. That preamble line
  remains stale and should be corrected in the cron definition.
- **Fallback now resolved:** on the previous weekday fire (2026-10-16) a working data path
  was established — the crumb-authenticated Yahoo Finance options chain
  (`fc.yahoo.com` cookie → `query1/v1/test/getcrumb` → `query2/v7/finance/options/<sym>`),
  which yields real per-strike volume, open interest and IV. That run completed cleanly:
  8 underlyings, 32 HTTP calls, 0 errors, 0×429, 69 kept strikes, artifact at
  `options-flow/2026-10-16.md`.

So the data-source blocker that made the 2026-10-11 skip unrecoverable is **resolved**.
The only reason this fire cannot run is the window.

## Recommended fix (operator)

Set `WEEKDAYS_ONLY=true` in the migration preamble. That makes weekend fires self-skip
through the script's own logic instead of relying on the agent to catch the contradiction,
and stops a silent "window-check: OK" on Saturdays and Sundays.

Secondary, still outstanding:

- **CRON_HOUR** — the skill targets 09:55 ET (~25 min after open, so volume settles). The
  current `MARKET_HOURS_ONLY` window admits any hour 09–16, so fires land after the close
  and yield a full-session sample rather than the intended post-open one. The 2026-10-16 run
  landed at 16:57 ET for this reason.
- **Pass A has never run in cloud** — `research/watchlist.yaml` is absent from this workspace,
  so every successful run has been Pass B only (8 mega-cap/ETF names).
- **Primary MCP** — re-enable `tradingview-advanced`, or correct the preamble to describe
  the Yahoo crumb fallback that is actually doing the work.

## Hard rules honored

- Read-only; no trade, direction, or sizing language anywhere.
- Excluded per spec (not scanned on any run): SPY, QQQ, SOXL, SOXS, SMH, TQQQ, SQQQ, UVXY, VXX.
- No fabricated data: no stale Friday chain was re-presented as Sunday flow, and no
  web-search results were passed off as MCP/App results.