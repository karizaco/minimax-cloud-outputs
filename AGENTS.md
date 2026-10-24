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

## Git — shared outputs repo

`karizaco/minimax-cloud-outputs` is **shared across crons** — several other cron jobs commit to `main`.

- A fresh `git init` produces an unrelated history, so a plain `git push` is **rejected** with
  "fetch first". This is expected, not a credential or TLS problem.
- Correct procedure:

  ```bash
  git fetch origin main
  git merge origin/main --allow-unrelated-histories -X ours
  git push origin main
  ```

- **Never force-push** to that repo — it would destroy other crons' artifacts.
- Verify after pushing: `git ls-tree -r --name-only origin/main | grep <your-dir>`.
