# Client-render contract — what the chat reply can show, and what to change

**Status:** proposal. **Applies to:** the chat reply of every routine, and the
`## DELIVERY` block in `karizaco/maxhermes-migration`.
**Built:** 2026-11-09. **Covers:** the reply format and the prose rules.
**Ready to apply:** `refs/maxhermes-client-render.patch` — see *Applying it* below.

> **What this is.** The Minimax Code desktop client renders the routine's chat
> reply with a narrow markdown subset: **bold, italics, and ordered/unordered
> lists**. It does not render coloured text, and flag glyphs arrive as a tofu
> box or as nothing at all.
>
> **What it is not.** This is not a claim that the artifacts are wrong. The
> artifacts are read in a file viewer that renders full markdown, where a wide
> table and an emoji band are exactly right. The problem is that the reply and
> the artifact are two different documents, and the house format currently
> makes them share one.

---

## The measurement

Taken over the 148 published narrative artifacts in this repo
(`scripts/check_reply_format.py --scan-repo --profile reply`):

| Finding | Count | What it means for the reply |
|---|---|---|
| `RENDER_HEADING` | 2,019 | `###` headings may not render |
| `RENDER_LONG_BULLET` | 1,620 | bullets over the length a column can hold |
| `RENDER_LONG_SENTENCE` | 1,363 | sentences too long to scan |
| `RENDER_TABLE` | 1,267 | tables are not available |
| `RENDER_GLYPH` | 1,108 | flag glyphs lose their meaning |
| `RENDER_LONG_PARAGRAPH` | 913 | **30% of all prose words sit in paragraphs of 80+ words** |
| `RENDER_EMOJI` | 58 | decorative emoji with no word behind them |

The emoji are concentrated: **cross-asset alone carries 804 of 1,166**, because
its correlation matrix encodes magnitude as a colour band (🟥 ≥ 0.70 strong,
🟦 < 0.20 uncorrelated). That encoding is deliberate and good — in the
artifact. The skill's own note says it plainly: *"GitHub strips `style=` from
markdown and the chat renders GFM, so ANSI/HTML colour is impossible."* The
first half still holds. **The second half is the assumption that broke**: the
desktop chat client is not that GFM chat.

The prose finding is the one that matches your "long hard to read paragraphs".
**30% of the 60,675 prose words in the published artifacts sit in paragraphs of
80 words or more**, and 25% of bullets run past 40 words. The house rule in
`PROMPT-BLOCKS.md` already says *"Keep every bullet to one short line. Never
cram three facts into a 300-character line"* — it is a good rule, it has no
number attached to it, and nothing checks it.

---

## The change, in three parts

### 1. The reply and the artifact stop sharing a format

The `## DELIVERY` block currently says:

> Use a compact markdown **table** whenever there are 3+ comparable numeric rows
> (index levels, sector rotation, futures, breadth).

That is right for the artifact and wrong for the reply. The patch replaces it
with a rule that works in both: the **artifact keeps the table**, and the
**reply carries the same rows as a list**, one line per row.

No reply checker asserts the presence of a table, so this is a style rule, not
a contract — which is why the blast radius is one section of one file.

### 2. Words instead of glyphs

The patch adds: *no colour and no flag glyph in the reply — write the word, not
the symbol.* `strong` / `elevated` / `moderate` / `mild` / `uncorrelated` for a
correlation band, `ok` / `warning` / `failed` / `critical` for a status, `+` /
`-` for a delta. Where a skill's **artifact** uses a glyph, the reply spells the
word.

Five skills carry a glyph today: `cross-asset-correlation-snapshot`,
`asia-pre-market-reactions`, `earnings-reaction-scanner`,
`stock-screener-suite` and `stocks-in-play-pipeline`. Their glyphs sit in
**artifact** tables (the source-health table, the correlation matrix, the legend),
which is the right place for them. What the patch changes is the rule that
governs the reply.

### 3. A number on the bullet rule, and a checker that enforces it

The patch replaces *"one short line"* with *"at most 30 words"*, and says where
to split: at a clause boundary — a semicolon, a colon, a dash, or a comma that
is not inside brackets — never mid-sentence. 30 words is roughly one screen
line in the client, and it sits inside the house's existing 300-character
intent.

The enforcement half is `tools/check_reply_format.py` in the patch: a standalone
verifier, in the same shape as the per-routine checkers already in
`maxhermes-migration/tools/`. It asserts the rules above against the saved
reply text and exits 1 on any finding.

```
python3 tools/check_reply_format.py --reply /workspace/reply.txt
```

On a reply with a 3-column table, two flag glyphs, two `###` headings, a
34-word bullet and two multi-ticker bullets, it reports exactly those eight
findings and names the fix for each.

---

## The dependency map — what a bigger change would cost

If you also want the **section headers** to stop being `###`, the blast radius
is much larger, and this is the map:

| Thing | Files |
|---|---|
| Asserts `### Signal` in a reply | `check_postmarket_brief.py` (×6), `check_premarket_artifact.py`, `check_breadth_artifact.py`, `check_cross_asset_artifact.py` |
| Asserts the section set in a test | `test_postmarket_contract.py`, `test_premarket_contract.py`, `test_breadth_contract.py`, `test_cross_asset_contract.py`, `test_ntrt_contract.py`, `test_reaction_contract.py` |
| Names the section format | `PROMPT-BLOCKS.md` and 10 skill/prompt files |

**Recommendation: do not do this yet.** A `###` heading that does not render
shows up as the literal text `### Signal` — ugly, but the section is still
findable and still distinguishable. Trading that for a fleet-wide change to 17
files, six of which are the contract tests that gate publication, is a bad
trade for a cosmetic gain. If you do want it later, the safe route is to relax
the checkers to accept **either** form (`### Signal` or `**Signal**`) rather than
to swap one for the other, so old and new replies both pass.

---

## The readability rules, if you want them in the artifact too

The artifact is read in a file viewer, where a paragraph is fine. But 30% of
prose words in 80+ word paragraphs is hard to read in any viewer, and the brief
families show it. The house has already solved this once, and the answer is
worth copying rather than inventing:

**`agentic-pre-market-brief/SKILL.md` §C1 — the `## Bottom line` block.** Three
lines, above the analysis, each carrying a level and an invalidation. The
reasoning is recorded in the skill itself: *"The 2026-11-03 brief was a 44 KB map
of the day with no decision in it: six themes, excellent analysis, no call."*

It has a contract clause and a checker (`check_premarket_brief.py` asserts it).
**The post-market brief and the in-play digest do not have it.** That is the
single highest-value change for readability, and it is a copy of a pattern that
is already proven and already enforced.

The two paragraphs that hurt most are in `us-stocks-in-play/<date>.md` — the
"headline" section is three essay-length paragraphs before any table. The
`## Bottom line` shape would replace them with three bullets and lose nothing.

---

## What was built here, and what was not

**Built in this repo, working today:**

- `scripts/check_reply_format.py` — the checker, with a `--scan-repo` mode that
  measures the whole published set against both a `reply` profile (the client's
  subset) and an `artifact` profile (GitHub's).
- `scripts/render_client_safe.py` — renders any artifact into the client's
  subset: headings become bold labels, tables become bullet lists, glyphs
  become the words they stood for, and long prose is broken at clause
  boundaries into bullets.
- `scripts/build_client_safe.py` — writes a client-safe **twin** of every
  narrative artifact under `derived/client-safe/`. The original is untouched and
  stays canonical; the twin is the version to open in the client.
- `refs/maxhermes-client-render.patch` — the reviewable patch.

**Measured effect of the renderer** over the 138 narrative artifacts:

| | before | after |
|---|---|---|
| reply-profile findings | 7,794 | **1,081** (86% removed) |
| glyphs, emoji, headings, tables, long paragraphs, long sentences | 6,323 | **0** |

The residual 1,081 are long bullets that are a single atomic clause — a
sentence with no semicolon, colon, dash or comma to break on. Splitting those
would mangle them, so they are left whole.

**Not done, deliberately:**

- **Nothing in `karizaco/maxhermes-migration` was edited.** The patch is
  proposed, not applied. The routines are live and pull their instructions from
  GitHub on a schedule, so changing them changes the next fire — that is your
  call, not mine.
- **No routine behaviour changed.** No threshold, no screen, no tier, no
  artifact format. The artifact keeps its tables and its glyphs.
- **The `###` headers stay `###`.** See *The dependency map*.

---

## Applying it

```bash
# in karizaco/maxhermes-migration
git apply -p1 /path/to/maxhermes-client-render.patch
```

Then, per routine that emits a reply, save the reply text and check it before
sending:

```bash
python3 tools/check_reply_format.py --reply /workspace/reply.txt
```

`PROMPT-BLOCKS.md` is fetched at **run** time by the routines, so the DELIVERY
change takes effect on the next fire with **no prompt edit and no prompt
drift** — the skills say so explicitly. That is the cheap half.

The skills that name their own chat rules — `agentic-post-market-brief`,
`ntrt-gap-brief`, `us-stocks-in-play`, `cross-asset-correlation-snapshot` and
`unusual-options-flow-daily` — are the ones to read next, because a skill that
says *"follow the skill's chat rules for tier order, flags and the audit line
where the skill defines them"* can re-introduce a glyph the shared block banned.
Each of those skills needs one line added to its chat rules: *the reply writes
the word, not the glyph; the artifact keeps the glyph.*

---

## See also

- `refs/artifact-contract.md` — the naming and shape rules for this repo
- `refs/decisions-contract.md` — the machine-readable decision record
- `ARTIFACT-INDEX.md` — what the repo holds
