# Ledger — what every routine saw on 2026-11-06

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-06/{master,focus,tier-a}.csv`, `earnings/2026-11-06-reactions.md`, `us-eod/2026-11-06.csv`, `us-stocks-in-play/2026-11-06-candidates.csv`, `options-flow/2026-11-06.md` · **Built:** 2026-11-10 · **Covers:** 1370 name(s) any routine mentioned; 1178 seen by two or more · read-only

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
>    - 193 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 200 | 15% |
| `earnings` | 198 | 14% |
| `eod` | 1157 | 84% |
| `in_play` | 1254 | 92% |
| `options_flow` | 42 | 3% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 198 | 1172 |
| `settled_change_pct` | 1157 | 213 |
| `catalyst` | 198 | 1172 |
| `sector` | 1170 | 200 |
| `rvol` | 1251 | 119 |
| `gap_verdict` | 148 | 1222 |
| `options_own_history_ratio` | 34 | 1336 |
| `gap_outcome` | 198 | 1172 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1172 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 193 | the scanner states the lookup was outside its per-run budget |
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
| IONQ | 5 | +8.02 | +23.16 | `extended` | B | 2.16 | yes | not_looked_up |
| CIFR | 5 | +11.53 | +17.93 | `extended` | TECH_WATCH | 1.40 | yes | not_looked_up |
| WULF | 5 | +7.84 | +12.80 | `extended` | B | 2.02 | yes | not_looked_up |
| AMD | 5 | +7.74 | +11.04 | `extended` | TECH_WATCH | 1.42 | yes | not_looked_up |
| MARA | 5 | +5.20 | +8.09 | `extended` | B | 0.91 | yes | not_looked_up |
| MU | 5 | +7.23 | +5.12 | `held` | TECH_WATCH | 1.41 | yes | not_looked_up |
| CORZ | 5 | +6.68 | +3.34 | `faded` | TECH_WATCH | 1.73 | yes | not_looked_up |
| ORCL | 5 | +2.90 | +0.87 | `faded` | SOFT_A | 0.81 | yes | not_looked_up |
| FROG | 4 | +22.96 | +35.33 | `extended` | A | 3.36 | no | sourced |
| OKLO | 4 | +7.40 | +22.73 | `extended` | A | 2.56 | no | not_looked_up |
| LUNR | 4 | +4.99 | +21.46 | `extended` | B | 1.59 | no | not_looked_up |
| INFQ | 4 | +5.38 | +19.49 | `extended` | B | 1.76 | no | not_looked_up |
| RGTI | 4 | +4.26 | +19.29 | `extended` | B | 2.06 | no | not_looked_up |
| ONDS | 4 | — | +18.03 | — | B | 0.99 | yes | — |
| QBTS | 4 | +3.98 | +18.01 | `extended` | TECH_WATCH | 1.96 | no | not_looked_up |
| RDW | 4 | +3.71 | +16.40 | `extended` | B | 1.12 | no | not_looked_up |
| SMR | 4 | — | +16.13 | — | B | 1.40 | yes | — |
| XE | 4 | +4.78 | +15.89 | `extended` | B | 1.16 | no | not_looked_up |
| FRVO | 4 | +6.68 | +15.85 | `extended` | B | 1.22 | no | not_looked_up |
| RKLB | 4 | +4.59 | +15.39 | `extended` | TECH_WATCH | 1.16 | no | not_looked_up |
| SEI | 4 | +8.09 | +14.26 | `extended` | B | 1.18 | no | not_looked_up |
| COHR | 4 | +9.38 | +13.74 | `extended` | SOFT_A | 1.75 | no | not_looked_up |
| RIOT | 4 | — | +13.21 | — | TECH_WATCH | 1.42 | yes | — |
| JOBY | 4 | — | +11.85 | — | B | 1.62 | yes | — |
| ABNB | 4 | +14.32 | +11.67 | `held` | A | 2.90 | no | not_looked_up |
| CBRS | 4 | +4.92 | +9.75 | `extended` | B | 0.84 | no | not_looked_up |
| APLD | 4 | +9.53 | +9.74 | `held` | TECH_WATCH | 1.24 | no | not_looked_up |
| NVTS | 4 | +5.86 | +9.54 | `extended` | B | 0.87 | no | not_looked_up |
| ARDT | 4 | -2.89 | +8.74 | `reversed` | B | 5.26 | no | not_looked_up |
| SPCX | 4 | +4.69 | +8.62 | `extended` | SOFT_A | 1.07 | yes | not_looked_up |
| CLSK | 4 | +5.93 | +8.45 | `extended` | B | 1.15 | no | not_looked_up |
| VIAV | 4 | +5.09 | +8.25 | `extended` | TECH_WATCH | 1.83 | no | not_looked_up |
| LRCX | 4 | +10.96 | +8.23 | `held` | SOFT_A | 1.26 | no | not_looked_up |
| IBRX | 4 | +2.12 | +7.80 | `extended` | B | 1.04 | no | not_looked_up |
| INTC | 4 | +4.88 | +7.71 | `extended` | B | 0.97 | no | not_looked_up |
| CRDO | 4 | +10.20 | +7.28 | `held` | TECH_WATCH | 1.01 | no | not_looked_up |
| ASTS | 4 | — | +7.05 | — | B | 2.10 | yes | — |
| AAOI | 4 | +4.50 | +6.91 | `extended` | SOFT_A | 1.53 | no | not_looked_up |
| TTMI | 4 | +7.46 | +6.89 | `held` | B | 0.89 | no | not_looked_up |
| SLS | 4 | +2.92 | +6.85 | `extended` | B | 0.87 | no | not_looked_up |

*184 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-06/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

