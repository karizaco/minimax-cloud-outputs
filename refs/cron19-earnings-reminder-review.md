# Cron #19 earnings-reminder — improvement review & cross-check (pointer)

The 10-improvement review for `19-earnings-reminder-daily` and the 2026-11-01 verification
pass live in the **migration repo**, next to the routine's prompt and `SKILL.md`:

    https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/docs/IMPROVEMENTS-cron19-earnings-reminder.md
    https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/docs/CROSSCHECK-cron19-earnings-reminder.md

They are analysis documents, not run artifacts, so they do not belong in this repo's
`earnings/` directory — cron #15 (`earnings-reaction-scanner`) stages that whole directory
with `git add earnings`, and per-run artifacts belong to the cron that produced them.

This repo holds the routine's **outputs**: `earnings/{date}-reminders.md` for each trading
day, and `AGENTS.md` (the standing workspace conventions). The routine's **spec** — prompt
and `SKILL.md`, including the corrected S&P 500 constituent parse — is in the migration repo
at `cloud-prompts/cron-prompts/19-earnings-reminder-daily.md` and
`cloud-prompts/skills/earnings-reminder/SKILL.md`.

Deployed task: resolve the id at use time via `cron_read {view: list, agent_name: "..."}` —
the fleet recreates tasks regularly, so `cloud-prompts/cron-prompts/roster.json` is the
authoritative map. See `refs/cron-ops.md`.
