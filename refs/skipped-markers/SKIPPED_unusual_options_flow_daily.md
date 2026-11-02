# Cron #16 unusual-options-flow-daily — SKIPPED

- Date (ET): 2026-10-11
- Time (ET): 16:53
- Day (ET): Sunday
- Reason: weekend / market closed — skill is a weekday job; no intraday options volume exists
- No artifact produced.
- Skill spec: `_source=skill_fetch_ok` (SKILL.md fetched from karizaco/maxhermes-migration)

## Why this was skipped (2 independent blockers)

### 1. Window: weekend, but the skill is Mon–Fri
`SKILL.md` documents its own schedule as `55 9 * * 1-5` America/New_York (weekdays).
The migration flags in this cron's preamble set `WEEKDAYS_ONLY=false`, `DAY_OF_WEEK=0`,
so the literal window-check passes. That contradicts the skill spec and the cron's own
CRITICAL REMINDER #4 ("weekend when it should be weekday" → exit cleanly, do not run a
degraded version).

Market state verified against Yahoo chart data for NVDA:

    2026-10-09 (Fri)  close 229.28  vol 84,470,000   <- last regular session
    2026-10-10 (Sat)  no session
    2026-10-11 (Sun)  no session  <- today

`regularMarketTime` = 2026-10-09 20:00 UTC = 2026-10-09 16:00 EDT (Friday close).
US equity + options markets are closed. A "V/OI > 1" unusual-activity scan is undefined
with zero intraday volume; any output would be stale Friday data mislabeled as today's flow.

### 2. Data source: the skill's PRIMARY MCP does not exist in this runtime
The procedure is built on `mcp__tradingview-advanced__stock_options_unusual_activity`.

| Probe | Result |
|---|---|
| Default model tool list | absent |
| `tool_search` "tradingview options unusual activity" | 0 hits |
| `tool_search` "yahoo finance options chain volume open interest" | 0 hits |
| `tool_search` regex `tradingview\|yahoo\|finance\|quote\|option\|mcp__` | 0 hits (only `cron_read`) |
| `mcode-tools connector tools` (unfiltered) | 13 tools, all Matrix media gen/understanding — no market data |
| `mcode-tools connector tools --keyword tradingview` | 0 tools |
| `mcode-tools connector tools --keyword finance` | 0 tools |

Also unresolved: the cron preamble advertises `mcp__yahoo_finance__*` as available.
Those tools are **not** present either. Treat that line as stale.

Direct HTTP fallback was attempted and is not viable:
- `query2.finance.yahoo.com/v7/finance/options/NVDA` → **HTTP 401 `{"code":"Unauthorized","description":"Invalid Crumb"}`**
  (options-chain endpoint requires an authenticated crumb/cookie; the `v8/finance/chart`
  endpoint works unauthenticated but returns only price/volume — no chain, no open interest.)
- No crumb/cookie broker is available in this sandbox, so per-strike volume + open
  interest cannot be sourced.

This blocker is independent of the window and **will fail on a valid Tuesday fire too.**
It needs an operator fix, not a retry.

## Recommended fixes (operator)

1. **Data source** — re-enable the `tradingview-advanced` MCP for this cron, OR restore
   `mcp__yahoo_finance__*`, OR provision a Yahoo crumb/cookie. Without one of these the
   job cannot produce a real scan on any day.
2. **Window flags** — set `WEEKDAYS_ONLY=true` in the migration preamble so weekend
   fires self-skip without a manual window-check override.
3. **Watchlist** — `research/watchlist.yaml` is absent in this runtime and 404s at all
   three expected repo paths. Per the skill's hard rules that forces "Pass B only"
   (mega-cap sweep). Worth restoring so Pass A runs.
4. **CRON_HOUR** — the skill targets 09:55 ET (~25 min after open, so volume settles).
   The current window (09:00–16:59 ET) allows fires at any hour, including after the
   close, which yields a partial session.

## Hard rules honored
- Read-only; no trade or sizing language anywhere.
- Excluded per spec: SPY, QQQ, SOXL, SOXS, SMH, TQQQ, SQQQ, UVXY, VXX.
- No fabricated or substituted data written: no web-search results were passed off as
  MCP/App results, and no stale Friday chain data was presented as today's flow.
