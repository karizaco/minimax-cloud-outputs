# Artifact Index — minimax-cloud-outputs

**Source:** direct read of the working tree at `C:\Users\admin\Projects\minimax-cloud-outputs`, 2026-11-08.
**Build time:** 2026-11-08. **Covers:** artifacts dated 2026-09-28 → 2026-11-06 (the full tracked range).
**Standard applied:** `AGENTS.md` (provenance line, deviations near the top, tables for data + prose for interpretation).

> **Deviations and known gaps in this index, stated up front.**
>
> 1. **This is a hand-written map, not a generated one.** No build script regenerates it, so it will
>    go stale as routines are added or directories retired. Treat it as accurate as of the date above.
> 2. **Directory file counts are approximate** for the large families. The shape of every directory is
>    verified from files that were opened; the counts are not shell-verified.
> 3. **This index does not re-derive any number.** Every figure quoted below is copied from the artifact
>    named next to it. Where two artifacts disagree, both are cited and the disagreement is stated.
> 4. **The routines' own prompts and skills live in another repo** (`karizaco/maxhermes-migration`).
>    Several files in `refs/` are pointers to it rather than copies — see *Pointers vs content* below.

---

## What this repo is

`minimax-cloud-outputs` is the **shared artifact bus** for a fleet of roughly twenty cron-driven market
screening and analysis routines covering the US, Asia-Pacific and Europe. The routines run on a
schedule, write one artifact per fire, and push here. Multiple crons commit to `main` on the same day,
so this repo is a **ledger of what was produced and published**, not a codebase with a build.

Two things are true here that are not true of most repos:

- **Artifacts are dated by the session they describe, not the day they were written.** A `2026-11-06`
  artifact may describe the `2026-11-05` session. Several artifacts carry two dates explicitly (for
  example `daily-screens/2026-11-06/daily-sweep.md` reads "the screen itself is one session behind:
  shibui's newest settled session at fire time was **2026-11-05**, so every screen metric below
  describes the 2026-11-05 tape while every 'today' figure is the 2026-11-06 settled close").
  Always read the date line before trusting a number.
- **The repo has no history of the routines themselves.** Only their outputs. If you want to know what
  a routine does, read `cron-prompts/` and `scripts/`, or the skill in the migration repo.

## The three artifact kinds

Almost every file in this repo falls into one of three kinds. Telling them apart is the fastest way
to know what to do with a file you have found.

| Kind | File shapes | What it gives you | Rule of thumb |
|---|---|---|---|
| **Narrative brief** | `.md` with tables + prose | The **read**: what happened, why, what was excluded, what is uncertain | Read this first. It is the only layer that explains itself. |
| **Data snapshot** | `.csv`, most `.json` | The **numbers**: wide universe tables at a point in time | Read only when you need to recompute. Stale on arrival; never has caveats attached. |
| **Provenance record** | `_manifest.json`, `ledger.md`, `.acceptance.txt`, `.log`, `SKIPPED_*.md`, `_excluded.json` | The **audit trail**: floors, exclusions, QC results, skip reasons | Read when you doubt the brief. This is where the failure modes live. |

**A fourth kind sits alongside them: the specification.** `cron-prompts/*.HARDENED.md`,
`scripts/*.py` and `ntrt/_pipeline/*.py` encode the routines' actual decision rules — window gates,
volume floors, caps, ranking order. These are not artifacts; they are the procedures the artifacts
were produced by, and they are the closest thing this repo has to a record of how the routines think.

## Directory map

All 21 top-level directories. "Live" means the routine is still producing into it.

| Directory | Written by | Contents | Live? |
|---|---|---|---|
| `daily-screens/` | cron #09 daily screener sweep (18:30 ET), #10 intraday breadth | Dated dirs, each with ~40 files: `daily-sweep.md`, `_summary.md`, `_regime.json`, `_results.json`, `_cache.json`, `breadth.md`, `_manifest.json`, `_decisions.json`, and per-stylist `.md`+`.csv` pairs | **Yes** — largest family (~500 files) |
| `daily-briefs/` | cron #26 pre-market brief (+09:20 refresh), #23 post-market | `<date>-pre-market.md` + `.csv`, `<date>-pre-market-refresh.md`, `<date>-post-market.md` | **Yes** |
| `ntrt/` | cron #17 pre-open gap brief | `<date>.md` + `<date>.csv`; `_pipeline/` (10 scripts); `_raw/` (~30 JSON intermediates + 4 logs) | **Yes** |
| `us-eod/` | cron #20 EOD US snapshot (16:00 ET) | `<date>.csv` + `<date>.md` (early days used `.meta.md`), per-market subdirs, `2026-11-06.manifest.json` + `.acceptance.txt` | **Yes** |
| `international-eod/` | cron #05 EOD international | Per-date dir: 16 region `.csv`, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json` | **Yes** |
| `us-stocks-in-play/` | cron #17 (pre-close / open / midday) | `<date>.md`, `-open.md`, `-midday.md`, `-candidates.csv`, `-open-candidates.csv`, `-close-candidates.csv`, `logs.jsonl` | **Yes** |
| `earnings/` | cron #15 reaction scanner, #19 reminder | `<date>-reactions.md`, `<date>-reminders.md`, `<date>-catalyst-targets.json` | **Yes** |
| `preopen-feed/` | cron 92a / 92b checkpoints (08:30, 09:50 ET) | `<date>-<HHMM>.jsonl` tape + `<date>-<HHMM>.md` digest | **Yes** |
| `options-flow/` | cron #16 unusual options flow | `<date>.md` | **Yes** |
| `stocktwits-sentiment/` | Grok Bot (Portfolio analyst) daily StockTwits core + general lists | Dated dir with `brief.md`, `sentiment.json`, `sentiment.csv`, `_manifest.json`; account identity stripped; contract `refs/stocktwits-sentiment-contract.md`; consumers should read `stocktwits-sentiment/latest.json` | **Yes** — weekdays |
| `asia-pre-market/` | cron #02 Asia pre-market reactions | `<date>.md` (+ one `.csv`) | **Yes** |
| `cross-asset/` | cross-asset routine | `<date>.md` | **Yes** |
| `macro-calendar/` | macro calendar routine | `week-ahead` / `midweek` `.md` (6 files) | **Yes**, low cadence |
| `mcp-health/` | cron #01 weekly MCP health check | `2026-W44.md` + `ledger.md` (append-only) | **Yes**, weekly |
| `data_cross/` | cross-asset compute pipeline | Per-ticker JSON (`SPY`, `QQQ`, `IWM`, `TLT`, `GLD`, `UUP`, `EEM`, `VIX`) + `compute.py`, `mats.json`, `meta.json` at the root; `2026-10-27/` subdir holds the dated CSVs plus `compute.py` and `compute_qc.py` | **Partly** — root copy is stale |
| `catalog/` | cron #15 catalyst table (spliced into reactions) | `catalysts/<date>.md` — **2 files only** | Partly — see *Fossils* |
| `pattern-study/` | cron #06 Saturday pattern-study backlog | `peoplewish-1000pct-backlog.md` — one cumulative ledger | **Yes** (1 file by design) |
| `research/` | ad-hoc research | `047040-jan-2026-catalyst.md` — one note | **No** — one-off |
| `weekly/` | weekly recap routine | Two editions: `2026-11-01-preview.{md,csv}` and `2026-11-08-preview.md`; the second lacks the movers CSV that the first carries | **Active** — weekly cadence established |
| `data2/` | earlier data work | `_stale_bars.json`, `_assemble_stats.json`, `yahoo_prices_2026-10-21.json` | **No** — superseded |
| `derived/` | **not a cron** — `scripts/build_derived.py` | Views joined from the families above: `persistence.{md,json}`, per-date `gap-reconciliation.*`, `sector-flow.*`, `ledger.*`, and `charts/*.html`. See `derived/README.md` | **Yes**, on demand |
| `refs/` | standing documentation | Contracts, pointers, `watchlist.yaml`, `artifact-contract.md`, `decisions-contract.md`, and `archive/skipped-markers/` | **Yes** (mixed) |
| `cron-prompts/` | prompt engineering | 3 `.HARDENED.md` prompt files | **Yes** |
| `scripts/` | routine engineering | 5 pipeline scripts plus 3 repo-consistency tools | **Yes** |
| `archive/` | retired artifact families | `README.md` (the convention) and `daily-screens-breadth/` | **No** — by design |

Read the "Live?" column as a statement about the **routine**, not about the files. A directory can be
live and still contain fossils inside it (`us-eod/` is live and still carries the superseded
`.meta.md` shape), and a directory can be dead and still hold its best content (`research/`). The
column tells you whether new files will keep arriving; it does not tell you whether what is already
there is worth reading. For that, use *Fossils, one-offs and superseded shapes* below — and note that
two of the smallest directories on this list, `pattern-study/` and `research/`, hold some of the most
substantive prose in the repo.

## How to read an artifact

The newest artifacts use YAML front matter. It is the fastest way to know what you are holding.

```yaml
---
date: 2026-11-06
cron: 26-agentic-pre-market-brief
contract: premarket-brief-artifact-v2
fire_time_et: 2026-11-06 08:30
snapshot_et: 08:36
source: TradingView america scanner + MCP-bridge market-recap
status: ok
---
```

- `fire_time_et` — when the routine woke up. `snapshot_et` — when the data was pulled. These differ
  (the 08:30 brief pulled at 08:36), and the gap matters when you are judging staleness.
- `status` — `ok` means the routine completed its contract. Anything else is worth reading.
- `source` — the data path, not the format. Check this before trusting a number.

Older artifacts have no front matter and instead carry a provenance line inside the first few lines
(`_summary.md` style: "**Cron date**: … · **Data session**: … · **Fired at**: … · **Generated**: …").
Both styles carry the same information; `daily-screens/2026-10-22/_summary.md` is the clearest
example of the older form, including an explicit "**Schedule deviation**" note.

## High-value entry points

If you are new to this repo, open these in order. Each is a full artifact; together they cover the
routine, the pre-market, the close, the international session, the option flow and the weekly synthesis.

| # | File | Why it is worth the time |
|---|---|---|
| 1 | `daily-screens/2026-11-06/daily-sweep.md` | The richest artifact in the repo. Regime read with the rule stated, leadership table where each theme carries its contradicting evidence, catalyst table with live source URLs, per-endpoint source health, coverage assertions for all 11 screen branches, 11 numbered caveats. |
| 2 | `ntrt/2026-11-06.md` | The only brief that publishes its own **funnel**: 834 names screened → 28 clear the actionable gate, with the 729 volume failures and the 76 sub-floor names shown rather than hidden. Flags section names ten names with no confirmed driver. |
| 3 | `us-eod/2026-11-06.md` | Full universe snapshot with a column-by-column coverage table, a closed `data_quality` vocabulary, and a **self-reported repair** (233 rows had published a change that was not the session's price change). |
| 4 | `daily-briefs/2026-11-06-pre-market.md` | The only artifact that scores **yesterday's own published thesis** against its invalidation level — HELD / BROKE / PARTIAL / UNJUDGED per name. Nothing else here closes that loop. |
| 5 | `international-eod/2026-11-06/summary.md` | 16 regions in one read, with a coverage/exclusion table read from `_excluded.json` rather than estimated, plus per-region USD floors and the JT limit-down detail. |
| 6 | `options-flow/2026-11-06.md` | Front matter documents the entire method (composite formula, filters, bias thresholds, universe definitions) before a single row of output. |
| 7 | `us-eod/2026-11-06.acceptance.txt` | 28 machine QC checks, "28 checks passed, 0 failed". The only programmatic acceptance gate in the repo. |
| 8 | `weekly/2026-11-01-preview-tldr.md` | The only cross-week synthesis: sector table, best/worst with market caps, cross-asset strip, and a caveat about the unreachable watchlist. |

Two more are worth knowing about even though they are single files:
`refs/preopen-feed-contract.md` (the tape's schema and tolerances, including a named regression
signature) and `research/047040-jan-2026-catalyst.md` (the best-written research note here — a catalyst
chain, a day-by-day tape, and an explicit resolution of a source conflict).

## Tooling

Three scripts keep the repo honest about itself. All are read-only against the artifacts
and safe to run on any checkout; none of them invents a value.

| Script | What it does | When it fails |
|---|---|---|
| `scripts/check_artifacts.py` | Three checks: `index` (this file names every top-level directory and every path it cites resolves), `links` (every backticked file reference inside every `.md` resolves), `convention` (basenames are Windows-safe; no filename in a dated directory repeats that directory's date) | `index` and `convention` exit non-zero on a finding; `links` exits non-zero on any in-repo reference that does not resolve |
| `scripts/build_screen_manifest.py` | Writes `daily-screens/<date>/_manifest.json` for every dated directory: the brief, the machine artifacts, which screens are present, whether each has a matching `.csv`, whether a screen is split into components, and the session lag | Never — it reports shape differences as notes, because they are real properties of the data, not errors |
| `scripts/build_decisions.py` | Writes `daily-screens/<date>/_decisions.json`: the thresholds that produced each published tier, the names a cap dropped, the per-branch coverage assertion, the regime flags, and the session lag | Never |
| `scripts/build_derived.py` | Runs the derived-view builders and writes a `_manifest.json` into each dated `derived/` directory | Reports a builder that raised, and keeps going |
| `scripts/check_reply_format.py` | Measures any reply or artifact against what the Minimax Code desktop client can render: glyphs, headings, tables, bullet and sentence length | Nothing — it reports; it never fails a build on its own |
| `scripts/render_client_safe.py` | Renders an artifact into the client's subset: headings become bold labels, tables become lists, glyphs become words | Nothing — it writes a new file and leaves the original alone |
| `scripts/install_hooks.py` | Installs the tracked git hooks into `.git/hooks/` and clears a `core.hooksPath` that points outside the repo | Never — it reports; it never removes a hook it did not write |
| `scripts/build_confirmation.py` | Counts how many of the five pre-market routines saw each name, and which of them agreed | Never |
| `scripts/build_thesis_score.py` | Extracts the published thesis verdicts from the briefs, by contract, and reports which briefs score | Never |
| `scripts/build_run_ledger.py` | Joins every published artifact to the roster's schedule: published, missing, off-schedule, before onset | Never |

```bash
python3 scripts/check_artifacts.py                    # all three checks
python3 scripts/check_artifacts.py links              # find broken in-text references
python3 scripts/build_screen_manifest.py              # regenerate the dated manifests
python3 scripts/build_decisions.py                    # regenerate the decision records
python3 scripts/build_derived.py                      # regenerate every derived view
```

### The derived views — joins the routines never make

The builders under `derived/` answer questions that no single routine can,
because each one is a join across families that fire at different times of day.
They are described in `derived/README.md`; the short version:

| View | The question it answers | Why no routine answers it |
|---|---|---|
| `derived/persistence.md` | How long has this name been on the board, and what left today? | Every dated screen is a snapshot with no memory of yesterday's |
| `derived/<date>/gap-reconciliation.md` | Did the morning's pre-market gaps hold into the close? | The 08:30 scanner, the 15:50 digest and the 18:30 sweep each hold one piece |
| `derived/<date>/sector-flow.md` | Which sectors gained the board, and does the board agree with the ETF tape? | The sweep describes the rotation in prose and never tabulates it |
| `derived/<date>/ledger.md` | What do we know about one name today, across every routine? | Each routine is a column; nothing is a row |
| `derived/<date>/setup-card.md` | Which published names are a setup, and which morning gaps were never looked up? | The sweep leads with Tier-A. The skill's setup tier is Stalk, and the catalyst budget is invisible in the brief |
| `derived/<date>/confirmation.md` | How many of the five pre-market routines saw each name? | Every routine is a column; nothing aggregates agreement |
| `derived/thesis-score.md` | Did yesterday's published thesis hold, and which briefs score at all? | Only 2 of 59 briefs carry a verdict table |
| `derived/run-ledger.md` | Which routine published what, on which day, and which are missing? | The roster in the migration repo is a snapshot and nothing refreshes it |
| `derived/setup-journal.md` | What did the next session do to each published setup? | The skill names a setup-journal. No routine writes one |
| `derived/charts/*.html` | What does the correlation matrix actually look like? | `cross-asset/` computes it and renders it as a table of 28 numbers |
| `derived/client-safe/**` | How does this artifact read in a chat client that shows bold, italics and lists only? | The artifacts are written for a file viewer. The reply is not |

**The measurement that motivated them.** Across the 12 dates that carry a readable
Tier-A board, the most persistent name appears **4 times and most appear once** —
the published lists had no way to show which names were converging and which were
one-day visitors. And on 2026-11-06 the earnings scanner published **5** sourced
catalysts against **193** rows marked "no catalyst lookup (outside the per-run
budget)". Both facts were in the artifacts already; neither was legible until a
join put them in one place.

**What they are not.** None of them is a cron product, none is a new measurement,
and none states a direction. A dated directory under `derived/` does not mean a
routine fired that day — it means the builders found enough sources to join.

The `links` check is the one that pays for itself. Commit `6569109` renamed 76 colon
paths to underscores but left the prose pointing at the old names; twenty in-repo
references were still broken when it landed, and this check finds that class of rot
before the next commit rather than a reader finding it later. It earned its keep the
first time it ran: it caught that archiving `daily-screens/breadth/` had invalidated two
references to it, in the 2026-10-26 and 2026-10-27 briefs.

**State as of 2026-11-08:** all three checks are clean. The link check examines 619
in-repo references, skips 205 that point at another repo or at a host path, 2 that
are templated, and 557 that are not paths in this repo at all — each category is
counted and printed rather than silently dropped. The convention check records 112
shape differences across the dated directories; none is an error, and all are now
visible in `_manifest.json` instead of only in a glob's silence.

**The decision records cover less than you might expect.** Only 4 of the 31 dated
directories have a `_results.json` — 2026-11-03 through 2026-11-06 — and only those
4 have a `_decisions.json`. The earlier 27 directories predate that artifact, and no
decision record can be built for them without inventing one. The 2026-11-04 record
shows the other limit: that run's `_results.json` predates the current schema, so it
carries no thresholds, no per-branch coverage and no tier-A pool members, and the
record says so rather than presenting nulls as facts.

Two contracts govern the shape of what these scripts check:

- **`refs/artifact-contract.md`** — the naming rules (Windows-safe basenames, no clock
  time in a filename, one filename shape per dated directory, a `_manifest.json` per
  dated directory, cross-repo references keeping their own repo's spelling) and the
  rule that a rename updates the prose in the same commit.
- **`refs/decisions-contract.md`** — the `_decisions.json` schema, and why the record
  holds *decisions* (the rule, and what it excluded) rather than a second copy of the
  data.

## Where the decision trail lives

This repo stores **outputs, not reasoning transcripts**. There is no model transcript, no
chain-of-thought and no agent message log anywhere in the tree — a repo-wide search for
`I will`, `Let me`, `thinking`, `reasoning`, `assistant`, `tool_use`, `tool_call`, `Thinking:` and
`<thinking>` returns no content hits. What exists instead, in descending order of fidelity:

| Tier | Where | What it preserves |
|---|---|---|
| **Decision records** | `international-eod/<date>/_manifest.json`, `_excluded.json`, `_calendar_correction.json`; `us-eod/<date>.manifest.json`; `daily-screens/<date>/_regime.json`, `_source-health.json`, `_results.json`; `us-stocks-in-play/logs.jsonl` | Per-region floors, FX tables with corrections, exclusion counts by reason, calendar/holiday notes, restatement notes, regime flags, run ledger with error counts |
| **Reasoning in prose** | The caveat sections of every narrative brief | Why a screen did or did not run, what was degraded, what a flag means. E.g. `daily-screens/2026-10-22/_summary.md`: "**Not run.** The skill gates this scan to weekdays 15:30–16:00 ET. This fire landed at 07:32 ET, outside the window. No names are reported rather than a loose substitute being presented as the real scan." |
| **Post-hoc reviews** | `refs/preopen-feed-contract.md`, `refs/plan-sources-and-mcp-tracking.md`, `refs/cron19-earnings-reminder-review.md` | Contracts and proposals written *about* the routines, including live probe evidence and an explicit "Decisions needed" list. Not run traces. |
| **Execution traces** | `ntrt/_raw/{cc,yc,run2,final_run}.log` | Tool-level retries and rate-limit events. Four files, all from 2026-10-26, 4–130 lines. No reasoning. |
| **The procedure itself** | `cron-prompts/*.HARDENED.md`, `scripts/*.py`, `ntrt/_pipeline/*.py` | The encoded decision rules — window gates with rationale comments, volume floors, caps, ranking order. `ntrt/_pipeline/write_brief.py` contains the QC classifier verbatim (`REF MISMATCH`, `stale print`, `thin book`, `cross-checked`). |

**The useful consequence:** the *rules* are fully recoverable from this repo. The *deliberation* that
applied them is not. If you need to know why a particular number appeared, the manifest and the
caveat section are where to look — not a transcript, because there isn't one.

## Fossils, one-offs and superseded shapes

| Path | What it is | Why it is inert |
|---|---|---|
| `refs/archive/skipped-markers/` (32 files) | Skip markers from when the day-of-week gate lived in the prompt | **Self-declared fossil**, and archived as such. Its own README: "These are fossils. The day-of-week now lives in the scheduler, so the weekend branches that produced most of these can no longer fire." Historical audit value only — kept out of `refs/` so it does not read as live state. |
| `data2/` (4 files) | `_stale_bars.json` (4,497-line list of stale bar stamps), `_assemble_stats.json`, one Yahoo price dump | No consumer; superseded by `us-eod/`, which does the same job with provenance. |
| `data_cross/` root level | Per-ticker JSON + `mats.json` + `meta.json`, all dated 2026-10-23 | A stale generation sitting beside the live one. The `data_cross/2026-10-27/` subdir is current; the root is not. |
| `weekly/` | One edition (2026-11-01) | A **weekly** routine that produced exactly one issue. High-quality content, no cadence. |
| `catalog/catalysts/` | 2 files (2026-10-24, 2026-10-26) against 12 dates of `earnings/*-reactions.md` | The splice path the cron #15 prompt specifies was effectively abandoned. Worth checking if you rely on it. |
| `research/` | One note | A single deep-dive, not a recurring family. The content is excellent; the family has no repeat. |
| `us-eod/<date>.meta.md` (2026-10-20 → 2026-10-27) | The earlier run-metadata format | Superseded by `<date>.md`, which folds the same content into a fuller report. |
| `ntrt/_raw/*.log` | Four execution logs from 2026-10-26 | Superseded by later briefs. Kept as a worked example of the pipeline degrading loudly. |

Two families look thin but are **not** disposable. `pattern-study/peoplewish-1000pct-backlog.md` is one
file by design — it is an explicitly cumulative ledger ("a long-lived log", with methodology, run
manifest, carried-forward table and a saturation note). `research/047040-jan-2026-catalyst.md` is a
single self-contained note whose value is in its content, not its repeatability.

## Pointers vs content

Several `refs/` files deliberately hold a URL instead of a copy. `refs/cron-ops.md`,
`refs/sources-us-stocks-in-play.md` and `refs/cron19-earnings-reminder-review.md` all point into
`karizaco/maxhermes-migration`. The stated reason is sound — `refs/sources-us-stocks-in-play.md`
says "Read it there rather than keeping a second copy here — a copy is what goes stale" — but the
practical consequence is that **this repo cannot be read standalone**. If the migration repo is
unreachable, those three files are links to nowhere.

The files in `refs/` that hold real content are `preopen-feed-contract.md` (the tape contract),
`plan-sources-and-mcp-tracking.md` (a 268-line proposal with live probe evidence), `watchlist.yaml`
(the published source of truth for four routines' watchlist sections — note it is currently a **seed**
list of 8 tickers, not the real 12-name personal list) and `refs/archive/skipped-markers/README.md`.

## Conventions and known drift

Things that are true for most of the repo but not all of it. Worth knowing before you write a script
against these files.

- **`daily-screens/` filename convention (normalised 2026-11-08).** Inside a dated directory the
  convention is now **unprefixed** for both `.md` and `.csv`: `focus.md`, `focus.csv`, `master.csv`,
  `reversal-bullish-3_55.md`, and so on. Two exceptions were normalised on 2026-11-08:
  `daily-screens/2026-10-23/` carried nine CSVs with a `2026-10-23-` prefix that no other date's
  CSVs carry, and the `reversal-bullish-3:55` **filenames** had already been renamed to
  `reversal-bullish-3_55` (commit `6569109`, for Windows validity) while the **in-text references**
  still pointed at the old colon form. All 20 in-repo references were rewritten.
  **Do not blanket-replace `3:55` → `3_55`.** The remaining `3:55` occurrences are correct and must
  stay: the cron *name* (`cron: "#4 reversal-bullish-3:55"`), the clock time ("3:55 PM
  reversal-bullish scan"), and the external migration-repo prompt path
  (`cloud-prompts/cron-prompts/04-reversal-bullish-3:55.md` — that repo lives on a Linux sandbox,
  where the colon is valid and the filename is unchanged).
- **Screen output still changes shape across dates.** `2026-10-22` has `stockbee_4pct` /
  `stockbee_coil` / `stockbee_ep9m` as separate files, while `2026-11-06` has a single `stockbee`
  file whose branches are listed inside it. `2026-10-19` is markdown-only with no screen CSVs at
  all. Do not assume a fixed file set per date.
- **`daily-screens/breadth/` was a separate, unrelated series — now archived.** Two files
  (`2026-10-26.md`, `2026-10-27.md`) held a *different* breadth universe (S&P 500 membership,
  502 tickers) from the dated directories' breadth (986 names above $10B), and the cron #10
  prompt explicitly forbids that path. It moved to `archive/daily-screens-breadth/` on
  2026-11-08. Treat the two breadth series as distinct products, not as drift.
- **`us-eod/` format evolution.** Early days are `<date>.csv` + `<date>.meta.md`; later days are
  `<date>.csv` + `<date>.md`. The 2026-11-06 edition adds `2026-11-06.manifest.json` and
  `2026-11-06.acceptance.txt` — the first file in the repo to carry a machine acceptance gate.
- **`daily-briefs/` three shapes.** `-pre-market.md` (the brief), `-pre-market-refresh.md` (a 09:20 ET
  re-pull that explicitly carries "no catalysts and no news"), and `-pre-market.csv` (the morning
  screen the refresh diffs against). The refresh is not a second brief.
- **`international-eod/` manifest churn.** `_manifest.json` appears from 2026-10-26; `_excluded.json`
  and `_carryover.json` from 2026-11-03; `_calendar_correction.json` from 2026-10-27; `_cap_findings.json`
  and `_digest.json` only on 2026-11-05. Earlier dates have `STUB_*.md` placeholders instead —
  `international-eod/2026-10-22/STUB_skill_fetch_failed.md` is a well-written no-data declaration
  naming three blockers (expired TLS cert in the sandbox egress, MCP tools not registered, fire 11h
  before the post-close window) and explicitly declining to synthesise rows.
- **`.gitignore` ignores `*.log`, but `ntrt/_raw/*.log` is tracked.** Those four files were added
  before the ignore rule and gitignore does not affect already-tracked paths. Any *new* execution log
  will therefore be silently untracked unless the rule is negated.
- **This clone uses a sparse checkout that excludes colon-named paths.** `core.sparseCheckout=true`
  with the pattern `/*` + `!*:*`, which is a deliberate Windows workaround: `:` is illegal in a
  Windows filename, so any artifact named `…3:55…` is excluded from materialising on disk. Two
  consequences to know before you trust `git status` here:
  1. **The index can go stale against HEAD.** A sparse checkout that was materialised before a
     rename leaves the index holding the old (colon) paths with the `skip-worktree` bit set, while
     HEAD holds the new ones. `git status` then reports a *staged rename in the wrong direction* and
     shows nothing wrong with the worktree. On 2026-11-08 this state was found: 84 artifacts appeared
     staged for renaming back to `3:55`, which would have re-introduced the Windows-invalid names
     that commit `6569109` had just fixed. The repair is `git reset` (index ← HEAD) followed by
     `git checkout -- <path>` to restore the files that the stale index had hidden.
  2. **A stale checkout can silently roll a file back.** `pattern-study/peoplewish-1000pct-backlog.md`
     and `refs/preopen-feed-contract.md` were present on disk at an *older* revision than HEAD
     (the 2026-10-31 backlog run instead of the 2026-11-07 one). Committing the worktree as-is
     would have reverted live fleet output. Always `git checkout --` a file whose worktree copy looks
     older than the commit you are building on.
- **The upstream fix for colon-named artifacts already exists, and its deployment is still
  pending.** In `karizaco/maxhermes-migration` the generator writes `reversal-bullish-3_55.*`
  (`tools/reversal_bullish.py`, `ARTIFACT_STEM`), the skill documents the Windows-safe basename,
  `push_artifact.sh` sanitises illegal basenames before a push, and the migration repo uses the
  same sparse-checkout trick to exclude the three colon-named prompt files from a Windows checkout.
  `docs/DEPLOY-HANDOFF-windows-safe-filenames.md` lists the five remaining steps, which all need
  MiniMax Cloud access (`cron_update`, `cron_read`) that this machine does not have. So the
  colon-named **files** are gone from this repo, but the **deployment** that stops the fleet
  producing them is not finished. Until it is, expect another manual rename.

## Maintenance notes

- This index is hand-written, but `scripts/check_artifacts.py --mode index` now fails if it
  stops naming a top-level directory, and if any path it cites stops resolving. That is
  the check that keeps this file from becoming the kind of stale map it warns about
  elsewhere in this repo.
- The repo is shared across crons and several jobs commit to `main` daily. **Check
  `git merge-base HEAD origin/main` before merging.** The recipe in `AGENTS.md`
  (`git merge origin/main --allow-unrelated-histories -X ours`) is written for a fresh
  `git init` with unrelated history; on a clone that shares a common ancestor, `-X ours`
  discards the other crons' commits and silently drops their artifacts. Use a plain
  `git merge origin/main` and verify with
  `git diff --diff-filter=D --name-only <merge-base> origin/main` that nothing was
  deleted. **Never force-push** — it would destroy other crons' artifacts.
- When reviewing an artifact, read the front matter or the provenance line first, then the caveats
  section, then the tables. In this repo the caveats section is where the real information is, and it
  is deliberately near the top for that reason.
