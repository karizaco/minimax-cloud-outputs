# Ledger — what every routine saw on 2026-11-09

**Source:** derived join over 4 artifact(s): `earnings/2026-11-09-reactions.md`, `us-eod/2026-11-09.csv`, `us-stocks-in-play/2026-11-09-candidates.csv`, `options-flow/2026-11-09.md` · **Built:** 2026-11-10 · **Covers:** 1523 name(s) any routine mentioned; 1296 seen by two or more · read-only

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
>    - No readable screen board for this date, so no tier or stylist count is available.
>    - 78 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 0 | 0% |
| `earnings` | 83 | 5% |
| `eod` | 1283 | 84% |
| `in_play` | 1501 | 99% |
| `options_flow` | 39 | 3% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 83 | 1440 |
| `settled_change_pct` | 1283 | 240 |
| `catalyst` | 83 | 1440 |
| `sector` | 1282 | 241 |
| `rvol` | 1495 | 28 |
| `gap_verdict` | 1501 | 22 |
| `options_own_history_ratio` | 32 | 1491 |
| `gap_outcome` | 83 | 1440 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1440 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 78 | the scanner states the lookup was outside its per-run budget |
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
| IBRX | 4 | -13.72 | -17.66 | `extended` | A | 4.87 | yes | sourced |
| AMD | 4 | +4.32 | +13.27 | `extended` | SOFT_A | 1.42 | yes | not_looked_up |
| HIMS | 4 | -2.12 | -11.77 | `extended` | TECH_WATCH | 3.77 | yes | not_looked_up |
| AVGO | 4 | +3.45 | +8.78 | `extended` | TECH_WATCH | 1.31 | yes | not_looked_up |
| SPCX | 4 | +2.76 | +5.81 | `extended` | B | 0.95 | yes | not_looked_up |
| NVDA | 4 | -4.81 | -4.23 | `held` | A | 3.28 | yes | not_looked_up |
| CIFR | 4 | -3.14 | +4.05 | `reversed` | B | 0.82 | yes | not_looked_up |
| AMZN | 4 | +3.28 | +2.93 | `held` | B | 0.82 | yes | not_looked_up |
| ZURA | 3 | — | -69.68 | — | A | 18.43 | yes | — |
| QXO | 3 | — | +19.20 | — | A | 2.27 | yes | — |
| FPS | 3 | +2.82 | +16.20 | `extended` | B | 0.86 | no | not_looked_up |
| EROC | 3 | +3.09 | +15.87 | `extended` | B | 0.56 | no | not_looked_up |
| TTD | 3 | — | +15.47 | — | TECH_WATCH | 4.60 | yes | — |
| IMVT | 3 | +9.66 | +15.13 | `extended` | TECH_WATCH | 2.93 | no | sourced |
| LUNR | 3 | +2.39 | +15.00 | `extended` | TECH_WATCH | 2.42 | no | not_looked_up |
| ASTS | 3 | +5.94 | +14.10 | `extended` | SOFT_A | 1.45 | no | not_looked_up |
| ETON | 3 | +2.73 | +13.97 | `extended` | TECH_WATCH | 2.20 | no | not_looked_up |
| HYMC | 3 | +4.16 | +13.32 | `extended` | TECH_WATCH | 1.25 | no | not_looked_up |
| RDW | 3 | +2.36 | +13.12 | `extended` | TECH_WATCH | 1.33 | no | not_looked_up |
| REF | 3 | +10.08 | +12.44 | `extended` | B | 0.78 | no | sourced |
| ONDS | 3 | +3.28 | +11.90 | `extended` | TECH_WATCH | 1.03 | no | not_looked_up |
| VIR | 3 | +15.09 | +11.79 | `held` | A | 3.84 | no | sourced |
| AUGO | 3 | +3.06 | +11.78 | `extended` | TECH_WATCH | 1.08 | no | not_looked_up |
| AMAT | 3 | +2.55 | +11.36 | `extended` | TECH_WATCH | 1.23 | no | not_looked_up |
| VICR | 3 | +2.94 | +11.30 | `extended` | B | 0.71 | no | not_looked_up |
| RKLB | 3 | +2.34 | +10.91 | `extended` | TECH_WATCH | 1.36 | no | not_looked_up |
| LRCX | 3 | +2.62 | +10.43 | `extended` | TECH_WATCH | 1.09 | no | not_looked_up |
| NRG | 3 | +4.20 | +10.36 | `extended` | B | 0.99 | no | not_looked_up |
| CRDO | 3 | +2.53 | +10.29 | `extended` | B | 0.95 | no | not_looked_up |
| UEC | 3 | +3.47 | +10.20 | `extended` | B | 0.65 | no | not_looked_up |
| CENX | 3 | +2.75 | +9.41 | `extended` | TECH_WATCH | 1.37 | no | not_looked_up |
| PENG | 3 | +2.22 | +9.25 | `extended` | B | 0.76 | no | not_looked_up |
| ANET | 3 | +2.45 | +9.02 | `extended` | B | 0.92 | no | not_looked_up |
| WULF | 3 | — | +8.88 | — | B | 0.95 | yes | — |
| APPS | 3 | +2.12 | +8.86 | `extended` | TECH_WATCH | 1.92 | no | not_looked_up |
| IONQ | 3 | — | +8.57 | — | TECH_WATCH | 1.27 | yes | — |
| ACHR | 3 | — | +8.55 | — | TECH_WATCH | 1.62 | yes | — |
| SEI | 3 | +2.30 | +8.40 | `extended` | B | 0.66 | no | not_looked_up |
| PPTA | 3 | +3.33 | +8.35 | `extended` | TECH_WATCH | 1.02 | no | not_looked_up |
| HUT | 3 | -2.79 | +8.30 | `reversed` | B | 0.62 | no | not_looked_up |

*39 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-09/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

