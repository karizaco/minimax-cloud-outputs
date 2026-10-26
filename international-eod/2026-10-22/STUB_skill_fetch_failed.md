# Cron #5 eod-international-daily — STUB (no data collected)

- Date (ET): 2026-10-22 (Thursday)
- Fire time (ET): 05:31  (UTC 09:31)
- Intended schedule: 16:35 ET weekdays (post-close)
- `_source`: skill_fetch_failed
- Rows written: 0 | Regions written: 0/16 | MCP calls made: 0

## Blocker 1 — Skill spec unreachable (network egress down)

`SKILL.md` fetch failed on all paths tried:

| Path | Result |
|---|---|
| `curl` (direct) | HTTP 000, 3 retries, ~0.05s each — connection never established |
| `web_fetch` (archon-server) | `timed out after 15000ms` |
| `mcode-tools connector tools` | `fetch failed (CERT_HAS_EXPIRED)` |
| `mcode-tools connector tools --keyword tradingview` | same |
| `mcode-tools connector tools --keyword yahoo` | same |

Control probes confirm this is sandbox-wide, not GitHub-specific:
- `https://github.com` → HTTP 000
- `https://example.com` → HTTP 000

TLS probe of `raw.githubusercontent.com:443` shows the sandbox egress
certificate **expired ~9h before this run**:

```
notBefore=Oct 21 00:37:52 2026 GMT
notAfter=Oct 22 00:37:52 2026 GMT     <- run time was Oct 22 09:31 UTC
```

**Likely single root cause:** an expired TLS certificate in the sandbox egress path
breaks both the skill fetch and the Connector discovery call. This needs an
infrastructure fix (renew cert / re-provision sandbox egress), not a cron change.

## Blocker 2 — Declared MCP tools are not present in this session

The cron prompt declares `mcp__tradingview_advanced__*`, `mcp__tradingview__*`,
`mcp__yahoo_finance__*` as available. None are registered in this session's tool
list, and discovery could not enumerate them (Blocker 1). So even with the spec in
hand there is currently **no working price/enrichment path**.

## Blocker 3 — Fire time is ~11h before the post-close window

Window check passed (Thursday, `WEEKDAYS_ONLY=true` passes) because the preamble
carries no hour-of-day gate (`MARKET_HOURS_ONLY=false`). Fire at 05:31 ET is ~11h
before the intended 16:35 ET run. At this hour no 16-region cash close has settled
for today: JP ~10:00 ET, EU ~11:30 ET, AU ~16:00 ET. A "degraded" pre-market run
would produce stale-or-empty rows, which the skill's hard rules forbid
("do not invent values for missing fields").

## Note on action taken

Per CRITICAL REMINDER 1, the spec fetch failed → write stub, reply with failure,
do **not** improvise the procedure from memory. No substitute data source was used
and no rows were synthesized. This is the 15th consecutive pre-market skip
(2026-09-28 → 2026-10-22); prior skips cited only the window, but today's run shows
the data path itself is additionally unavailable.