# `derived/` — views joined from the cron artifacts

**Source:** `scripts/build_derived.py` over the artifact families named below.
**Built:** regenerate with one command; nothing here is written by a cron.
**Covers:** sessions 2026-10-22 → 2026-11-06, plus two undated renders in `charts/`.

> **The three things to know before reading anything in here.**
>
> 1. **No cron writes into this directory.** Every file is derived from artifacts
>    that a cron did write, and it is only as current as the last time the builders
>    were run. A dated directory here does **not** mean a routine fired that day.
> 2. **These views join; they do not restate.** Every value is copied from a named
>    source artifact. Where a value cannot be filled it is left blank and counted,
>    so each view's own coverage is visible inside the view.
> 3. **Read-only, and no trade language.** Nothing here states a direction, a size
>    or a recommendation. The labels that look like judgements (`held`, `faded`,
>    `reversed`) describe a session's price path and nothing else.

## Why this directory exists rather than files inside `daily-screens/<date>/`

Every file under `daily-screens/<date>/` is a cron product, and that directory's
file set is already load-bearing — `scripts/build_screen_manifest.py` classifies
it, and a routine's own logic globs it. Dropping derived files in beside them
would mean a second writer in a directory a cron owns, in a repo that several
crons commit to. Keeping them here makes the provenance unambiguous: if it is in
`derived/`, no routine produced it.

## What is here

| View | Files | What it answers | Joined from |
|---|---|---|---|
| **Persistence** | `persistence.md`, `persistence.json` | How long has each name actually been on the board, and what left today? | `daily-screens/<date>/{tier-a,focus}.csv` |
| **Gap reconciliation** | `<date>/gap-reconciliation.{md,csv}` | Did this morning's pre-market gaps hold into the close? | `earnings/<date>-reactions.md`, `us-eod/<date>.csv` |
| **Sector flow** | `<date>/sector-flow.{md,csv}` | Which sectors gained the board today, and does the board agree with the tape? | `daily-screens/<date>/master.csv`, `us-stocks-in-play/<date>.md` |
| **Ledger** | `<date>/ledger.{md,jsonl}` | What do we know about one name today, across every routine that saw it? | five families — see the ledger's own source line |
| **Setup card** | `<date>/setup-card.{md,csv}` | Which published Stalk and Tier-A names are actually a setup, and which morning gaps were never looked up? | `daily-screens/<date>/{stalk,tier-a}.csv`, `earnings/<date>-reactions.md`, `us-eod/<date>.csv` |
| **Setup journal** | `setup-journal.{md,csv}` | What did the next session do to each published setup? | the same boards, joined to the next `us-eod/<date>.csv` |
| **Charts** | `charts/*.html` | The correlation matrix and the regime series, drawn | `cross-asset/<date>.md`, `daily-screens/<date>/_regime.json` |
| **Client-safe twins** | `client-safe/<same path as the original>` | The same artifacts, rendered for a client that shows bold, italics and lists only | every narrative artifact — see `refs/client-render-contract.md` |
| **Confirmation** | `<date>/confirmation.{md,csv}` | How many of the five pre-market routines saw each name, and where they agree | the screen, the gap brief, the flow screen, the reminders and the reaction scanner |
| **Thesis score** | `thesis-score.{md,csv}` | Did yesterday's published thesis hold — and which briefs score at all? | the thesis-verdict tables in the published briefs |
| **Run ledger** | `run-ledger.{md,csv}` | Which routine published what, on which day, and which are missing | every published artifact, against the roster's schedule |

Each dated directory carries a `_manifest.json` naming its files and what each
view was joined from, per `refs/artifact-contract.md` Rule 3.

## The gap the ledger closes

The ledger is the only artifact in this repo that answers *what do we know about X
today* in one row, and the only one that measures its own blind spots. On
2026-11-06 it records that the earnings scanner published **5** sourced catalysts
and **193** rows marked `not_looked_up` — the scanner's own words are "no catalyst
lookup (outside the per-run budget)".

That distinction matters more than it looks. A reader of a brief sees an empty
catalyst cell and reasonably concludes *nothing happened*. The real meaning is
*nobody checked*. Those are different facts and only one of them is evidence.

## Regenerating

```bash
python3 scripts/build_derived.py              # every view, then the manifests
python3 scripts/build_derived.py --check      # report, write nothing
python3 scripts/build_derived.py --manifest   # manifests only
```

Individual builders take the same `--check` flag:

```bash
python3 scripts/build_persistence.py --check
python3 scripts/build_gap_reconciliation.py --check
python3 scripts/build_sector_flow.py --check
python3 scripts/build_ledger.py --check
python3 scripts/build_charts.py --check
```

A rebuild that changes nothing writes nothing: the provenance line carries the
build **date**, not a clock time, so re-running the builders on the same day
produces no diff. That is deliberate — this repo is shared across crons, and
timestamp churn would bury real changes.

## The client-safe twins

`derived/client-safe/` holds a second copy of every narrative artifact, rendered
for the Minimax Code desktop client - which shows **bold, italics and lists
only**, so a markdown table arrives as raw pipe characters and a flag glyph
arrives as a tofu box.

The original stays canonical and is untouched. The twin is the one to open when
you are reading in the client: headings become bold labels, tables become bullet
lists, the correlation bands become the words they stood for (`strong`,
`moderate`, `mild`), and long prose is broken at clause boundaries into
bullets.

The renderer removes 86% of the reply-profile findings across the published
artifacts, and **every** finding that is a hard rendering failure - glyphs,
emoji, headings, tables, over-long paragraphs, over-long sentences - goes to
zero. What remains are long bullets that are a single atomic clause, which are
left whole because splitting them would mangle them.

`refs/client-render-contract.md` has the measurement, the dependency map, and
the reviewable patch for the routine definitions in the migration repo.

## Caveats that apply to everything here

- **The sources drift, and the builders say so rather than hiding it.** The ticker
  column is `symbol`, `ticker` or `name` depending on the date; the session-change
  column has had five names; `us-eod/` keyed tickers as `NASDAQ:NVDA` until
  2026-10-28 and bare afterwards; sectors come in two taxonomies that are never
  blended. Each view prints the columns it actually read.
- **Coverage is partial and stated.** Only 12 dates carry a readable Tier-A board;
  three dates publish no sector column and have one recovered from `us-eod/` by a
  join that the artifact labels; two reactions files cannot be verified against any
  settled session and say so at the top.
- **A blank is never a zero.** Every view distinguishes *not measured* from
  *measured as nothing*, because the two support opposite conclusions.
