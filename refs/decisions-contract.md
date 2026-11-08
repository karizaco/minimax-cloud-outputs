# Decisions contract — the machine-readable reasoning record

**Status:** active. **Applies to:** `daily-screens/<date>/_decisions.json`.
**Last revised:** 2026-11-08.

---

## Why this exists

This repo stores **outputs, not reasoning transcripts**. There is no model transcript,
no chain-of-thought and no agent message log anywhere in the tree — a repo-wide
search for `I will`, `Let me`, `thinking`, `reasoning`, `assistant`, `tool_use`,
`tool_call`, `Thinking:` and `<thinking>` returns no content hits.

That is not necessarily a defect: storing transcripts would be large, mostly
uninteresting, and hard to keep. But it does leave a gap. A reader six weeks later
can see *what* was published and *what the numbers were*, and can reconstruct *why*
only by reading English.

Some briefs already close that gap well. The `ntrt` brief of 2026-11-06 names the 729
names that failed on volume, the 76 that cleared the %ADV test but sat under the
$200M cap, the ten with no confirmed driver, and the two whose prints had gone stale.
That is a real reasoning trail. No other family publishes anything comparable.

`_decisions.json` is the attempt to make that trail machine-readable, in a fixed shape
a consumer can rely on. It records **decisions** — which rule produced a published
set, what a cap dropped, which branch did not complete, which session the numbers
describe — not content.

**What is deliberately not in it.** No catalyst text, no prices, no interpretation, no
model reasoning. A decision record says *what rule ran and what it excluded*; the
artifact it sits beside says *what that means*. Keeping the two apart is what stops
the record from becoming a second, divergent copy of the data.

## Coverage — and where it stops

`_decisions.json` exists only for a dated directory that has a `_results.json`. As of
2026-11-08 that is **4 of the 31** dated directories (2026-11-03 through 2026-11-06).
The earlier 27 predate `_results.json`, and a decision record cannot be built for
them without inventing one — so none is.

There is a second limit, inside a run. A record is only as good as the `_results.json`
it came from. The 2026-11-04 file predates the current schema: it carries no
thresholds, no per-branch coverage and no tier-A pool members. Its record says so,
rather than presenting `null` thresholds as if they were a rule and an empty dropped
list as if nothing had been dropped. **A record that states what it does not know is
useful; one that silently omits it is worse than no record at all.**

## The schema

`_schema: "daily-screens-decisions-v1"`. Written by `scripts/build_decisions.py`,
derived from `daily-screens/<date>/_results.json`.

| Field | Type | Meaning |
|---|---|---|
| `date` | string | The directory's date — the date of the fire, which may be later than the session it describes |
| `data_as_of` | string \| null | The session the screen metrics describe |
| `session_lag_days` | int \| null | `date − data_as_of`. 0 means the screen and the settled close are the same session |
| `derived_from` | string | The file every value was copied from |
| `rules` | object | The thresholds that produced each published tier |
| `rules.stylists` | list | The stylist names that were counted — the "how many distinct sources" the tiers count |
| `rules.focus` | object | `min_stylists`, `max_names` |
| `rules.tier_a` | object | `min_stylists`, `max_names` |
| `counts` | object | The published counts, as the routine recorded them |
| `dropped` | object | What a cap removed |
| `dropped.tier_a_truncated` | bool | Whether the Tier-A cap actually cut anything |
| `dropped.tier_a_pool_size` | int | Names that met the ≥N-stylist rule |
| `dropped.tier_a_published` | int | Names actually published |
| `dropped.tier_a` | list | **The names the cap dropped.** This is the reason the record exists |
| `screen_coverage` | object | Per branch: `rows_passing`, `rows_kept`, `complete` |
| `regime` | object | The three regime flags and the breadth figure behind them |
| `source_health` | object | `machine_file` — whether a `_source-health.json` exists; `prose_only` when it does not |
| `notes` | list | Plain-language statements of anything the reader would otherwise have to infer |

`complete` is `rows_passing == rows_kept`. A branch where the two differ lost rows to
a cap or a filter, and the record says so rather than letting the count look clean.

## Reading it

```python
import json
d = json.load(open("daily-screens/2026-11-06/_decisions.json"))

if d["session_lag_days"]:
    print("these metrics describe", d["data_as_of"], "not", d["date"])

if d["dropped"]["tier_a_truncated"]:
    print("dropped by the cap:", d["dropped"]["tier_a"])

for branch, s in d["screen_coverage"].items():
    if not s["complete"]:
        print("incomplete branch:", branch, s)
```

## The two facts it exists to carry

**The dropped names.** A Tier-A list capped at 8 that is actually drawn from a pool of
12 is not the same artifact as one drawn from a pool of 8, and the brief says so in a
sentence while a consumer reading the CSV cannot tell. `dropped.tier_a` names them.
For 2026-11-06 the pool was `RUN, SEZL, XERS, ACHC, MRNA, APP, U, FUN, JOBY, WRBY,
VRDN, XNCR` and the published eight were the first eight — so the record carries
`JOBY, WRBY, VRDN, XNCR` as the names the cap removed.

**The session lag.** The screen metrics describe the previous session while the
"today" columns are the current settled close. Every artifact that mixes the two
says so in prose, and the column naming convention (`*_resolved` vs `today_*`) is the
only machine-readable trace. `session_lag_days` makes it a single integer.

## Extending it to other families

The shape generalises. What each family needs before it can emit a record:

| Family | Already machine-readable | What a record would add |
|---|---|---|
| `daily-screens/` | `_results.json` — thresholds, pool, coverage | **Implemented** |
| `ntrt/` | the brief's CSV has `pct_of_adv`, `mkt_cap_usd`, `premarket_change_pct` | The gate thresholds are stated in prose per run, so the record must carry them as data, not as a constant; then per-name exclusion reasons are derivable |
| `us-eod/` | the CSV's `data_quality` column is a closed vocabulary | Per-flag row counts and the reason each flag excludes a row from the movers table — the brief publishes this as a table but the CSV carries the flags without the rule |
| `international-eod/` | `_excluded.json` — every excluded row with a reason | The per-region floor that produced the exclusion; the manifest already carries the floor, so this is a join |
| `earnings/`, `options-flow/`, `daily-briefs/` | composite scores, bias tags | Which candidates were checked for a catalyst and which were not — `ntrt` publishes this ("10 published names have no confirmed driver"), the others do not |

The rule for extending it: **a decision record states a rule and its exclusions. It
never restates the data.** If a field could be copied out of the artifact's own table
unchanged, it does not belong here.

## See also

- `refs/artifact-contract.md` — naming and shape rules
- `ARTIFACT-INDEX.md` — where the process trail actually lives today
