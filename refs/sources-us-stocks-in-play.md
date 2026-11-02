# Sources — us-stocks-in-play (cron #17)

**Source of truth for endpoint status:** `cloud-prompts/_shared/RUNTIME-CONTRACT.md` in
`karizaco/maxhermes-migration` (section 2a, re-measured 2026-10-31 and 2026-11-02).

That file records what each endpoint actually returned, per endpoint, with the HTTP status and
the shape of the response. Read it there rather than keeping a second copy here — a copy is what
goes stale.

The per-source detail for this routine (what each source is used for, and how it is read) is in
the routine's own skill: `cloud-prompts/skills/us-stocks-in-play/SKILL.md`.
