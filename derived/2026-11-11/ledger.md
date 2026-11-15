# Ledger — what every routine saw on 2026-11-11

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-11/{master,focus,tier-a}.csv`, `earnings/2026-11-11-reactions.md`, `us-eod/2026-11-11.csv`, `us-stocks-in-play/2026-11-11-candidates.csv`, `options-flow/2026-11-11.md` · **Built:** 2026-11-15 · **Covers:** 1610 name(s) any routine mentioned; 1372 seen by two or more · read-only

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
>    - 114 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 1125 | 70% |
| `earnings` | 120 | 7% |
| `eod` | 1315 | 82% |
| `in_play` | 865 | 54% |
| `options_flow` | 36 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 120 | 1490 |
| `settled_change_pct` | 1310 | 300 |
| `catalyst` | 120 | 1490 |
| `sector` | 1312 | 298 |
| `rvol` | 804 | 806 |
| `gap_verdict` | 865 | 745 |
| `options_own_history_ratio` | 31 | 1579 |
| `gap_outcome` | 120 | 1490 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1490 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 114 | the scanner states the lookup was outside its per-run budget |
| `sourced` | 6 | the scanner published a catalyst with a source |

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
| MU | 5 | +6.49 | +11.89 | `extended` | SOFT_A | 0.99 | yes | not_looked_up |
| CORZ | 5 | +7.31 | +10.97 | `extended` | TECH_WATCH | 1.39 | yes | not_looked_up |
| ORCL | 5 | +5.15 | +8.81 | `extended` | B | 0.59 | yes | not_looked_up |
| RGTI | 5 | +2.96 | -8.56 | `reversed` | TECH_WATCH | 1.89 | yes | not_looked_up |
| AMD | 5 | +5.48 | +7.32 | `extended` | TECH_WATCH | 1.03 | yes | not_looked_up |
| AVGO | 5 | +4.10 | +3.98 | `held` | TECH_WATCH | 1.09 | yes | not_looked_up |
| NVDA | 5 | +3.57 | +2.84 | `held` | TECH_WATCH | 1.28 | yes | not_looked_up |
| SMR | 5 | +5.84 | +0.19 | `flat` | TECH_WATCH | 1.07 | yes | not_looked_up |
| GEVO | 4 | — | +30.94 | — | A | 10.08 | yes | — |
| CRWV | 4 | — | +24.71 | — | A | 2.61 | yes | — |
| AXTI | 4 | +9.47 | +19.49 | `extended` | SOFT_A | 1.08 | no | sourced |
| EQPT | 4 | +3.07 | +18.18 | `extended` | TECH_WATCH | 1.89 | no | not_looked_up |
| FRMI | 4 | — | +17.53 | — | TECH_WATCH | 1.13 | yes | — |
| AAOI | 4 | +6.73 | +15.60 | `extended` | SOFT_A | 0.94 | no | not_looked_up |
| FPS | 4 | +8.01 | +14.34 | `extended` | B | 0.93 | no | not_looked_up |
| SNDK | 4 | +7.88 | +13.69 | `extended` | TECH_WATCH | 1.08 | no | not_looked_up |
| BE | 4 | +7.32 | +13.00 | `extended` | B | 0.93 | no | not_looked_up |
| EROC | 4 | +8.01 | +12.20 | `extended` | TECH_WATCH | 1.06 | no | not_looked_up |
| DELL | 4 | +7.30 | +11.75 | `extended` | TECH_WATCH | 1.10 | no | not_looked_up |
| STX | 4 | +8.83 | +9.99 | `extended` | TECH_WATCH | 1.11 | no | not_looked_up |
| MRVL | 4 | +8.93 | +9.33 | `extended` | B | 0.79 | no | not_looked_up |
| COHR | 4 | +9.66 | +9.27 | `held` | SOFT_A | 0.93 | no | sourced |
| FUN | 4 | +7.78 | +9.05 | `extended` | B | 0.73 | no | not_looked_up |
| TTMI | 4 | +7.16 | +8.96 | `extended` | B | 0.60 | no | not_looked_up |
| INOD | 4 | +5.04 | +8.90 | `extended` | B | 0.73 | no | not_looked_up |
| CIFR | 4 | +9.49 | +8.88 | `held` | B | 0.82 | no | sourced |
| ASTS | 4 | +3.00 | +8.70 | `extended` | B | 0.82 | no | not_looked_up |
| WDC | 4 | +8.00 | +8.33 | `extended` | B | 0.90 | no | not_looked_up |
| SHLS | 4 | +3.19 | +8.24 | `extended` | B | 0.58 | no | not_looked_up |
| INTC | 4 | +5.98 | +7.47 | `extended` | B | 0.65 | no | not_looked_up |
| GLW | 4 | +6.66 | +7.40 | `extended` | B | 0.78 | no | not_looked_up |
| APLD | 4 | — | +7.37 | — | B | 0.97 | yes | — |
| TDW | 4 | +4.93 | +6.66 | `extended` | TECH_WATCH | 1.01 | no | not_looked_up |
| REPL | 4 | +2.04 | -6.44 | `reversed` | B | 0.66 | no | not_looked_up |
| WULF | 4 | — | +6.37 | — | B | 0.78 | yes | — |
| IBKR | 4 | +2.17 | +6.32 | `extended` | TECH_WATCH | 1.22 | no | not_looked_up |
| LRCX | 4 | +5.76 | +6.07 | `extended` | B | 0.68 | no | not_looked_up |
| PBF | 4 | +2.26 | +5.81 | `extended` | B | 0.60 | no | not_looked_up |
| FROG | 4 | +2.37 | +5.70 | `extended` | B | 0.89 | no | not_looked_up |
| MRCY | 4 | +2.97 | +5.68 | `extended` | TECH_WATCH | 1.84 | no | not_looked_up |

*353 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-11/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

