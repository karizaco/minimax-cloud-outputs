# Archive

Retired artifact families, kept for the audit trail but moved out of the live tree so they
stop reading as current state.

**The rule.** An artifact family moves here when it is *inert*, not merely *old*. Three
things qualify:

1. The routine that wrote it no longer runs, or no longer writes in that shape.
2. Nothing in the repo reads it, and it is not a source of truth for anything.
3. Its own documentation says so — a README, a manifest, or the brief that replaced it.

**What does not qualify.** A family that is still being written but has been superseded
*in part* stays where it is; the superseded part is fixed in place, not exiled. The
`us-eod/<date>.meta.md` shape is a good example: it was replaced by `<date>.md`, but the
`.meta.md` files are still the only record of how those early runs behaved, and they sit
beside their replacements where a reader will find them.

**How it is archived.** Moved, not deleted — `git mv` preserves the history, and a reader
who wants to know what a routine published in October can still find it. Each archived
family keeps its own files and, where it had one, its own README.

**Who reads it.** Almost nobody, deliberately. That is the point: an audit trail that has
to be read to be useful is not an audit trail, it is a second data source with no owner.

## Contents

This directory holds retired families that were moved *out of* a live tree. Families
retired within a tree they still belong to are archived in place instead — see
`refs/archive/skipped-markers/`, which stayed under `refs/` because `refs/` is where a
reader looks for documentation.

| Directory | What it was | Why it is inert |
|---|---|---|
| `daily-screens-breadth/` | A breadth & regime series written to `daily-screens/breadth/<date>.md` by an earlier version of the breadth routine | Superseded by `daily-screens/<date>/breadth.md` and `breadth-snapshot.md`. It used a *different* universe — S&P 500 membership, 502 tickers — against the live series' 986 names above $10B, so the two are not comparable. The cron #10 prompt now explicitly forbids that path. |

## Not archived, and why

| Path | Why it stays |
|---|---|
| `data2/` | Inert, but it is the only copy of the stale-bar detection output. Worth a decision on whether to archive or delete; left alone rather than moved on a technicality. |
| `data_cross/` (root level) | The root generation is stale (all dated 2026-10-23) while `data_cross/2026-10-27/` is current. The root copy is a candidate for archiving; the dated subdirectory must stay. |
| `us-eod/<date>.meta.md` | Superseded in shape, but still the only record of those early runs, and it sits beside its replacement. |
| `ntrt/_raw/*.log` | Four execution logs from 2026-10-26. Superseded by later briefs, but they are a worked example of the pipeline degrading loudly, which is worth keeping in place. |
| `catalog/catalysts/` | Only two dates against twelve dates of `earnings/*-reactions.md`. That looks like an abandoned splice path — but it is a *live* question about a routine that still runs, not a fossil, so it is an investigation rather than an archive. |

## See also

- `ARTIFACT-INDEX.md` — what the repo holds and which parts still matter
- `refs/artifact-contract.md` — the naming and shape rules
