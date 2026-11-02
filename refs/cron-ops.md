# Fleet cron ops — pointer

The authoritative reference for task IDs, scheduler-API workarounds, and the available
data sources (GitHub connector, `market-recap` MCP pack, Barchart-via-headless-chromium,
`uv`/`uvx` MCP packages) lives in the **migration repo**:

    https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/cron-ops.md

Machine-readable task-ID map (regenerated from the live scheduler):
`https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/cron-prompts/roster.json`

Endpoint status + measured fallback chain:
`https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/_shared/RUNTIME-CONTRACT.md`

**Do not hard-code a task ID** — the fleet recreates tasks regularly. Resolve at use time with
`cron_read {view: list, agent_name: "<agent>", limit: 100}` (pass `agent_name`, never `cursor`:
a numeric-string cursor is rejected by the schema's coercion step).

Current cron #17: task `457954144674016`, `50 15 * * 1-5` America/New_York (15:50 ET pre-close
slot — intentional), project 13832.
