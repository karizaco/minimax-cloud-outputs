# Ledger — what every routine saw on 2026-10-24

**Source:** derived join over 1 artifact(s): `earnings/2026-10-24-reactions.md` · **Built:** 2026-11-09 · **Covers:** 54 name(s) any routine mentioned; 0 seen by two or more · read-only

> **Read this before the table.**
> 
> 1. **This artifact joins; it does not restate.** Every field is copied from
>    one of the sources above. Nothing is computed from scratch, nothing is
>    scored, and no name is recommended.
> 2. **A blank is a blank, and it is counted.** Where a routine did not see a
>    name, the field is null and appears in the coverage table below. A ledger
>    that filled gaps with guesses would look like the authoritative artifact in
>    this repo while being the least trustworthy one.
> 3. **`unusual_options_flow: null` is not `false`.** Null means the flow screen
>    did not run for this date; false means it ran and did not surface the name.
> 4. **Deviations and degraded paths.**
>    - No settled EOD file for 2026-10-24 (`us-eod/<date>.csv`), so no settled close, change or sector is available for any row.
>    - No options-flow artifact for 2026-10-24 (`options-flow/<date>.md`), so `unusual_options_flow` is null rather than false — the screen's silence cannot be distinguished from it not having run.
>    - No in-play candidate file for this date, so no RVol or gap verdict is available.
>    - No readable screen board for this date, so no tier or stylist count is available.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 0 | 0% |
| `earnings` | 54 | 100% |
| `eod` | 0 | 0% |
| `in_play` | 0 | 0% |
| `options_flow` | 0 | 0% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 53 | 1 |
| `settled_change_pct` | 0 | 54 |
| `catalyst` | 0 | 54 |
| `sector` | 0 | 54 |
| `rvol` | 0 | 54 |
| `gap_verdict` | 0 | 54 |
| `options_own_history_ratio` | 0 | 54 |
| `gap_outcome` | 54 | 0 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `absent` | 54 | the scanner had a row for the name but no catalyst text |

`not_looked_up` is the row that matters. **It is a budget decision, not a
finding** — the scanner did not check, so the absence of a catalyst says
nothing about whether one exists. No other artifact in this repo distinguishes
those two cases, and a reader of a brief would reasonably assume the second.

## Names three or more routines saw

No name on this date was seen by three or more routines.

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-24/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

