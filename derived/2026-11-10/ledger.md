# Ledger — what every routine saw on 2026-11-10

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-10/{master,focus,tier-a}.csv`, `earnings/2026-11-10-reactions.md`, `us-eod/2026-11-10.csv`, `us-stocks-in-play/2026-11-10-candidates.csv`, `options-flow/2026-11-10.md` · **Built:** 2026-11-11 · **Covers:** 1912 name(s) any routine mentioned; 1552 seen by two or more · read-only

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
>    - 64 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 1356 | 71% |
| `earnings` | 69 | 4% |
| `eod` | 1485 | 78% |
| `in_play` | 943 | 49% |
| `options_flow` | 38 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 69 | 1843 |
| `settled_change_pct` | 1475 | 437 |
| `catalyst` | 69 | 1843 |
| `sector` | 1672 | 240 |
| `rvol` | 891 | 1021 |
| `gap_verdict` | 943 | 969 |
| `options_own_history_ratio` | 32 | 1880 |
| `gap_outcome` | 69 | 1843 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1843 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 64 | the scanner states the lookup was outside its per-run budget |
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
| ASTS | 5 | -2.82 | -8.67 | `extended` | TECH_WATCH | 1.34 | yes | not_looked_up |
| RKLB | 5 | -7.78 | +6.54 | `reversed` | TECH_WATCH | 1.56 | yes | sourced |
| APPS | 4 | -23.89 | -35.84 | `extended` | A | 5.15 | no | sourced |
| AAON | 4 | +15.52 | +19.31 | `extended` | A | 3.14 | no | sourced |
| HIMS | 4 | — | -16.61 | — | A | 3.88 | yes | — |
| HYMC | 4 | -3.62 | -11.28 | `extended` | TECH_WATCH | 1.03 | no | not_looked_up |
| MARA | 4 | — | +10.54 | — | TECH_WATCH | 1.69 | yes | — |
| PLUG | 4 | — | -9.00 | — | B | 0.92 | yes | — |
| QBTS | 4 | — | -8.63 | — | TECH_WATCH | 1.65 | yes | — |
| AXTI | 4 | -3.78 | -8.39 | `extended` | B | 0.70 | no | not_looked_up |
| TTWO | 4 | +3.47 | +8.31 | `extended` | B | 2.35 | no | not_looked_up |
| QUBT | 4 | -4.81 | -8.16 | `extended` | TECH_WATCH | 1.16 | no | not_looked_up |
| SKYD | 4 | -2.11 | -7.59 | `extended` | TECH_WATCH | 1.42 | no | not_looked_up |
| CDE | 4 | — | -7.05 | — | B | 0.90 | yes | — |
| SRRK | 4 | -6.83 | -6.89 | `held` | TECH_WATCH | 1.42 | no | sourced |
| ONDS | 4 | -2.51 | -6.70 | `extended` | B | 0.87 | no | not_looked_up |
| AUGO | 4 | -2.30 | -6.53 | `extended` | B | 0.85 | no | not_looked_up |
| OKLO | 4 | -2.57 | -6.52 | `extended` | B | 0.88 | no | not_looked_up |
| RGTI | 4 | -2.93 | -6.39 | `extended` | TECH_WATCH | 1.08 | no | not_looked_up |
| LEU | 4 | -3.45 | -6.33 | `extended` | B | 0.75 | no | not_looked_up |
| NVDA | 4 | — | -5.49 | — | A | 2.43 | yes | — |
| FPS | 4 | -2.70 | -4.96 | `extended` | B | 0.58 | no | not_looked_up |
| CLSK | 4 | -2.17 | -4.92 | `extended` | B | 0.71 | no | not_looked_up |
| COHR | 4 | -3.43 | -4.68 | `extended` | B | 0.98 | no | not_looked_up |
| TEM | 4 | -2.17 | -4.62 | `extended` | B | 0.60 | no | not_looked_up |
| BE | 4 | -3.00 | -4.37 | `extended` | B | 0.69 | no | not_looked_up |
| TTMI | 4 | -2.11 | -4.12 | `extended` | B | 0.87 | no | not_looked_up |
| SMR | 4 | — | -4.04 | — | B | 1.13 | yes | — |
| AVGO | 4 | — | +3.91 | — | B | 0.98 | yes | — |
| SANM | 4 | +13.95 | +3.90 | `faded` | B | 3.33 | no | sourced |
| GEV | 4 | -6.19 | -3.89 | `held` | SOFT_A | 1.25 | no | not_looked_up |
| MXL | 4 | -2.72 | -3.72 | `extended` | B | 0.59 | no | not_looked_up |
| TTD | 4 | -5.44 | +3.28 | `reversed` | master,focus | — | yes | not_looked_up |
| GLW | 4 | -2.26 | -3.25 | `extended` | B | 0.55 | no | not_looked_up |
| INFQ | 4 | -2.38 | -3.21 | `extended` | B | 0.57 | no | not_looked_up |
| CLMT | 4 | -6.54 | -3.19 | `faded` | B | 1.38 | no | not_looked_up |
| VRT | 4 | -3.41 | -3.13 | `held` | B | 0.62 | no | not_looked_up |
| CEG | 4 | -2.02 | -3.02 | `extended` | B | 0.72 | no | not_looked_up |
| JHX | 4 | — | -2.97 | — | B | 8.35 | yes | — |
| FLY | 4 | -3.62 | -2.51 | `held` | B | 1.15 | no | not_looked_up |

*335 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-10/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

