# Ledger — what every routine saw on 2026-10-27

**Source:** derived join over 3 artifact(s): `daily-screens/2026-10-27/{master,focus,tier-a}.csv`, `us-eod/2026-10-27.csv`, `options-flow/2026-10-27.md` · **Built:** 2026-11-11 · **Covers:** 205 name(s) any routine mentioned; 202 seen by two or more · read-only

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
>    - No reactions artifact for 2026-10-27 (`earnings/<date>-reactions.md`), so no pre-market gap or catalyst is available for any row.
>    - No in-play candidate file for this date, so no RVol or gap verdict is available.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 200 | 98% |
| `earnings` | 0 | 0% |
| `eod` | 202 | 99% |
| `in_play` | 0 | 0% |
| `options_flow` | 8 | 4% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 0 | 205 |
| `settled_change_pct` | 202 | 3 |
| `catalyst` | 0 | 205 |
| `sector` | 202 | 3 |
| `rvol` | 0 | 205 |
| `gap_verdict` | 0 | 205 |
| `options_own_history_ratio` | 0 | 205 |
| `gap_outcome` | 0 | 205 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 205 | the earnings scanner did not cover this name at all |

`not_looked_up` is the row that matters. **It is a budget decision, not a
finding** — the scanner did not check, so the absence of a catalyst says
nothing about whether one exists. No other artifact in this repo distinguishes
those two cases, and a reader of a brief would reasonably assume the second.

## Names three or more routines saw

The rows where this artifact earns its place: a name several independent
routines touched on the same session, with each routine's column beside the
others.

| Ticker | Seen by | Pre-mkt % | Settled chg % | Path | Tier | RVol | Flow | Catalyst |
|---|---|---|---|---|---|---|---|---|
| AMZN | 3 | — | +1.61 | — | master | — | yes | — |
| AAPL | 3 | — | +0.93 | — | master | — | yes | — |
| NVDA | 3 | — | +0.90 | — | master | — | yes | — |

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-27/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

