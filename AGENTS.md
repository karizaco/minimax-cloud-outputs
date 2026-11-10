# Workspace instructions — `/workspace`

Standing conventions for this cloud workspace. Applies to every session run here, not just cron jobs.

## Output formatting

### Chat replies

- **Lead with prose, not a label list.** Open with a short paragraph — 2–4 sentences — stating the headline
  finding and the one caveat that most changes how it should be read.
- **Use section headers.** Group the substance under `###` headers after the lead paragraph
  (e.g. `### Signal`, `### Method & caveats`, `### Files`, `### Errors`). Headers are expected, not optional.
- **Complete sentences, not fragments.** A bullet should read as a sentence
  ("Coverage was Pass B only — `research/watchlist.yaml` is absent.") rather than a clipped label-value pair.
- **No hard line cap.** Length scales with how much there is to say. Stay scannable: a reader should be able
  to skim the headers and stop at any point.
- **Consistent skeleton:** headline paragraph → what the data shows → method & caveats → files → push/errors.

### Report artifacts (the `.md` files)

- **Tables for the data, prose for the interpretation.** Every table gets a following paragraph saying what
  it means, what it does *not* mean, and what a reader should not conclude from it.
- **Consistent sections:** summary → data tables → per-item detail → caveats & method → source health.
- **Put deviations, fallbacks and degraded data paths near the top**, not buried at the bottom — a reader
  should not have to reach section 9 to learn that the primary source was missing.
- **One provenance line per artifact:** source, build time, and the session/date the data covers.
- Keep the `.meta.md`-style long detail in the artifact files; the chat reply summarizes and points to them.

## Evidence and data-path rules

- Every figure gets a source, a row count, and a freshness stamp.
- If a feed is degraded, a fallback was used, or a data path failed, **say so plainly** — in the artifact
  *and* in the chat reply. Never smooth over a broken path.
- Never present web-search results as MCP/App results, and never present a prior session's data as current.
- Flag methodology that materially changes a headline number (e.g. a selection rule that flips a bias tag)
  in the artifact body, not only in a deviations list.
- Read-only by default. No trade, direction, or sizing language unless the task explicitly asks for it.

### Artifact naming and shape

- **Basenames must be Windows-safe** — no `: < > " | ? *`, and never a bare clock time.
  `:` is illegal in a Windows filename and this repo is checked out on Windows, while
  the crons run on Linux and will emit one without complaint. The routine's *name*
  (`04-reversal-bullish-3:55`) keeps its colon — that is a task id, not a filename.
- **No filename inside a dated directory repeats that directory's date.** The date is
  already in the directory name.
- **A dated directory carries a `_manifest.json`** naming the brief, the machine
  artifacts, and any screen published as components rather than as an aggregate.
- **A rename updates the prose that references it, in the same commit.** A renamed file
  with stale in-text references is a broken link, not a rename.
- **A routine may leave a machine-readable decision record** — the rules it applied
  and what they excluded — beside the artifact it explains.

Full rules: `refs/artifact-contract.md` and `refs/decisions-contract.md`.
Check them all with `python3 scripts/check_artifacts.py`.

## Git — shared outputs repo

`karizaco/minimax-cloud-outputs` is **shared across crons** — several other cron jobs commit to `main`.

- A fresh `git init` produces an unrelated history, so a plain `git push` is **rejected** with
  "fetch first". This is expected, not a credential or TLS problem.
- Correct procedure:

  ```bash
  git fetch origin main
  git merge origin/main --no-edit
  git push origin main
  ```

  **Do NOT use `-X ours`.** That strategy silently discards every commit the
  other crons pushed since your last fetch. It is appropriate when histories are
  genuinely unrelated and you want to keep yours outright — it is **not**
  appropriate for a shared repo where the other commits are real artifacts you
  must keep. The error it causes (cron artifacts disappearing from `origin/main`)
  is silent and only visible by diffing tree counts after the push.

  If you see `--allow-unrelated-histories` needed, your clone has lost the shared
  base; do **not** combine it with `-X ours` — use it with the default merge
  strategy and then inspect the result before pushing.

- **Never force-push** to that repo — it would destroy other crons' artifacts.
- **Always verify** after pushing that other crons' work survived:
  ```bash
  git log --oneline origin/main | head -6   # other crons still present
  git ls-tree -r --name-only origin/main | grep <your-dir>   # your work landed
  ```

## Git hooks

Two hooks live in `scripts/hooks/` and are **tracked in the repo**. They are
not active until they are installed:

```bash
python3 scripts/install_hooks.py          # install into .git/hooks/
python3 scripts/install_hooks.py --check  # report what is installed
```

| Hook | When | What it does |
|---|---|---|
| `pre-commit` | every commit | runs the test suite, regenerates `daily-screens/<date>/{_manifest,_decisions}.json` from the artifacts the cron published, runs `check_artifacts.py`, and blocks the commit on a failure or a finding (`--no-verify` is the escape) |
| `post-merge` | every merge and every `git pull` | regenerates `derived/` and commits it if the builders wrote anything. It does not push. |

**`core.hooksPath` overrides `.git/hooks/` entirely.** A clone with that
setting pointing at a scratch directory has no working hooks at all — the
files in `.git/hooks/` are never consulted. `install_hooks.py` clears an
override that points outside the repo. Check the state at any time with
`python3 scripts/install_hooks.py --check`; it says which hook is installed,
and whether the tracked copy has drifted from it.

The builders are idempotent and carry the build **date**, not a clock time, so
the `post-merge` hook produces no diff when nothing changed and a same-day
rebuild is silent.

## Tests

The tooling in `scripts/` has a test suite. It is **stdlib-only and offline** —
the Cloud sandbox has no PyPI access, so there is no pytest.

```bash
python3 scripts/run_tests.py            # every suite, one verdict
python3 scripts/run_tests.py joinlib    # only the suites matching a name
```

| Suite | What it pins |
|---|---|
| `scripts/test_joinlib.py` | the shared column-drift reader — the ticker column across its four spellings, the escaped-pipe row split, the number and sector parsers |
| `scripts/test_builders.py` | each derived-view builder, against a synthetic mini-repo in a temp directory: streaks, the canonical stylist grouping, the gap-reconciliation session resolution, the thesis contracts, the ledger states |
| `scripts/test_render.py` | the client-safe renderer — the three table shapes, and that **every data row produces a bullet** |
| `scripts/test_hooks.py` | the hooks, against a real scratch repository: the post-merge commit exits 0, leaves no staged residue, and does not sweep unrelated staged content |

**A test that cannot fail is a failure.** The house rule, from the migration
repo's contract tests: a fixture or mutation that does not change anything is
itself reported as a failure, not a silent pass. When you add a test, check
that it fails when the behaviour it covers is broken.
