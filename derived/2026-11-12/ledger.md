# Ledger — what every routine saw on 2026-11-12

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-12/{master,focus,tier-a}.csv`, `earnings/2026-11-12-reactions.md`, `us-eod/2026-11-12.csv`, `us-stocks-in-play/2026-11-12-candidates.csv`, `options-flow/2026-11-12.md` · **Built:** 2026-11-15 · **Covers:** 1938 name(s) any routine mentioned; 1549 seen by two or more · read-only

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
>    - 110 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 1173 | 61% |
| `earnings` | 115 | 6% |
| `eod` | 1480 | 76% |
| `in_play` | 1170 | 60% |
| `options_flow` | 37 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 115 | 1823 |
| `settled_change_pct` | 1478 | 460 |
| `catalyst` | 115 | 1823 |
| `sector` | 1638 | 300 |
| `rvol` | 1156 | 782 |
| `gap_verdict` | 1170 | 768 |
| `options_own_history_ratio` | 28 | 1910 |
| `gap_outcome` | 115 | 1823 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1823 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 110 | the scanner states the lookup was outside its per-run budget |
| `sourced` | 5 | the scanner published a catalyst with a source |

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
| CRWV | 5 | -9.45 | -6.86 | `held` | SOFT_A | 1.53 | yes | not_looked_up |
| APLD | 5 | -5.08 | -5.36 | `extended` | B | 0.83 | yes | not_looked_up |
| NVDA | 5 | -7.56 | -4.32 | `held` | A | 3.15 | yes | not_looked_up |
| INTC | 5 | -2.96 | -2.03 | `held` | SOFT_A | 0.39 | yes | not_looked_up |
| MU | 5 | -4.31 | -1.59 | `faded` | SOFT_A | 0.70 | yes | not_looked_up |
| CTVA | 4 | — | -24.11 | — | A | 2.64 | yes | — |
| MANE | 4 | -4.20 | -13.55 | `extended` | B | 3.89 | no | not_looked_up |
| AVEX | 4 | +11.29 | +13.44 | `extended` | B | 3.35 | no | sourced |
| SMCI | 4 | -5.75 | -11.30 | `extended` | A | 2.22 | no | not_looked_up |
| FRVO | 4 | -2.70 | -9.97 | `extended` | B | 0.77 | no | not_looked_up |
| FPS | 4 | -5.98 | -9.77 | `extended` | SOFT_A | 1.32 | no | not_looked_up |
| PLUG | 4 | — | -8.86 | — | B | 0.56 | yes | — |
| QNT | 4 | -2.97 | -7.67 | `extended` | B | 0.63 | no | not_looked_up |
| TE | 4 | — | -7.53 | — | SOFT_A | 1.55 | yes | — |
| KDP | 4 | — | -7.40 | — | TECH_WATCH | 1.64 | yes | — |
| AXTI | 4 | -5.98 | -7.30 | `extended` | SOFT_A | 0.80 | no | not_looked_up |
| AEHR | 4 | -4.03 | -7.21 | `extended` | B | 0.60 | no | not_looked_up |
| ONDS | 4 | — | -7.16 | — | SOFT_A | 1.55 | yes | — |
| LUNR | 4 | — | +6.98 | — | A | 2.91 | yes | — |
| TWST | 4 | -8.23 | -6.85 | `held` | A | 2.22 | no | not_looked_up |
| AMD | 4 | — | +5.86 | — | SOFT_A | 1.25 | yes | — |
| ASTS | 4 | -2.91 | -5.79 | `extended` | B | 0.46 | no | not_looked_up |
| EROC | 4 | -9.98 | -5.61 | `held` | SOFT_A | 1.36 | no | sourced |
| AVGO | 4 | — | +5.56 | — | SOFT_A | 1.41 | yes | — |
| AAOI | 4 | -5.96 | -5.39 | `held` | B | 0.58 | no | not_looked_up |
| JBLU | 4 | — | -5.22 | — | TECH_WATCH | 1.33 | yes | — |
| HIMS | 4 | -3.89 | -5.19 | `extended` | B | 0.53 | no | not_looked_up |
| RKT | 4 | — | -5.12 | — | B | 0.50 | yes | — |
| NVTS | 4 | -3.67 | -5.07 | `extended` | B | 0.61 | no | not_looked_up |
| GLXY | 4 | -4.82 | -4.95 | `held` | B | 0.79 | no | not_looked_up |
| INOD | 4 | -3.07 | -4.92 | `extended` | B | 0.57 | no | not_looked_up |
| FLY | 4 | -2.67 | -4.88 | `extended` | B | 0.78 | no | not_looked_up |
| ACMR | 4 | -3.84 | -4.86 | `extended` | B | 0.47 | no | not_looked_up |
| CDE | 4 | — | -4.85 | — | B | 0.60 | yes | — |
| TTEK | 4 | +10.77 | +4.84 | `faded` | TECH_WATCH | 1.87 | no | sourced |
| VSH | 4 | -2.88 | -4.57 | `extended` | B | 0.58 | no | not_looked_up |
| SNDK | 4 | -6.00 | -4.11 | `held` | SOFT_A | 0.84 | no | not_looked_up |
| ASST | 4 | -5.60 | -4.09 | `held` | B | 0.81 | no | not_looked_up |
| BMNR | 4 | -5.15 | -4.05 | `held` | B | 0.65 | no | not_looked_up |
| WOLF | 4 | -4.19 | -3.94 | `held` | B | 0.31 | no | not_looked_up |

*348 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-12/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

