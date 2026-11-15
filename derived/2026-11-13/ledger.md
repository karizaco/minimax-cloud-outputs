# Ledger — what every routine saw on 2026-11-13

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-13/{master,focus,tier-a}.csv`, `earnings/2026-11-13-reactions.md`, `us-eod/2026-11-13.csv`, `us-stocks-in-play/2026-11-13-candidates.csv`, `options-flow/2026-11-13.md` · **Built:** 2026-11-15 · **Covers:** 1558 name(s) any routine mentioned; 1319 seen by two or more · read-only

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
>    - 20 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 1188 | 76% |
| `earnings` | 25 | 2% |
| `eod` | 1271 | 82% |
| `in_play` | 594 | 38% |
| `options_flow` | 41 | 3% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 25 | 1533 |
| `settled_change_pct` | 1268 | 290 |
| `catalyst` | 25 | 1533 |
| `sector` | 1450 | 108 |
| `rvol` | 594 | 964 |
| `gap_verdict` | 594 | 964 |
| `options_own_history_ratio` | 33 | 1525 |
| `gap_outcome` | 25 | 1533 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1533 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 20 | the scanner states the lookup was outside its per-run budget |
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
| AMD | 5 | -2.78 | -8.75 | `extended` | SOFT_A | 1.01 | yes | not_looked_up |
| CSCO | 5 | -3.62 | -6.24 | `extended` | SOFT_A | 1.12 | yes | not_looked_up |
| AVGO | 5 | -2.27 | -4.78 | `extended` | B | 0.88 | yes | not_looked_up |
| FRMI | 4 | — | +26.70 | — | A | 2.07 | yes | — |
| VIR | 4 | -16.67 | -17.82 | `extended` | C | 7.04 | no | sourced |
| CBRS | 4 | — | +11.20 | — | A | 3.20 | yes | — |
| STLN | 4 | — | -6.67 | — | TECH_WATCH | 3.94 | yes | — |
| AEHR | 4 | -2.52 | -6.65 | `extended` | B | 0.53 | no | not_looked_up |
| GLXY | 4 | -2.04 | -5.27 | `extended` | B | 0.64 | no | not_looked_up |
| MRVL | 4 | — | -4.68 | — | B | 0.58 | yes | — |
| OPEN | 4 | — | -3.64 | — | B | 0.73 | yes | — |
| SMR | 4 | — | -3.22 | — | B | 0.70 | yes | — |
| TE | 4 | — | -3.05 | — | TECH_WATCH | 1.56 | yes | — |
| SLS | 4 | +8.66 | -2.12 | `reversed` | TECH_WATCH | 1.66 | no | sourced |
| NBIS | 4 | -2.44 | — | `no_close` | TECH_WATCH | 1.57 | yes | not_looked_up |
| SBC | 3 | — | +37.64 | — | A | 8.74 | no | — |
| SPCE | 3 | — | -31.66 | — | A | 6.02 | yes | — |
| NMAX | 3 | — | +31.23 | — | A | 6.58 | no | — |
| LFTO | 3 | — | +30.63 | — | A | 10.76 | no | — |
| MOD | 3 | — | +27.87 | — | C | 2.68 | no | — |
| HAWK | 3 | — | +24.06 | — | A | 3.68 | no | — |
| HTFL | 3 | — | -19.13 | — | SOFT_A | 1.81 | no | — |
| OBIO | 3 | — | +17.89 | — | TECH_WATCH | 2.84 | no | — |
| NUAI | 3 | — | +17.65 | — | SOFT_A | 1.68 | no | — |
| MRLN | 3 | — | +17.17 | — | C | 15.51 | yes | — |
| TNDM | 3 | — | +14.62 | — | SOFT_A | 1.46 | no | — |
| CDNL | 3 | — | +14.54 | — | TECH_WATCH | 3.51 | no | — |
| PEPG | 3 | — | -13.49 | — | B | 0.41 | no | — |
| UNIT | 3 | — | +13.49 | — | SOFT_A | 1.33 | no | — |
| BRCB | 3 | — | +11.93 | — | TECH_WATCH | 1.07 | no | — |
| LRMR | 3 | — | +11.85 | — | TECH_WATCH | 2.17 | no | — |
| PLUG | 3 | — | -10.12 | — | B | 0.77 | no | — |
| PRME | 3 | — | +9.77 | — | TECH_WATCH | 1.08 | no | — |
| AQST | 3 | — | +9.52 | — | TECH_WATCH | 1.33 | no | — |
| LCID | 3 | — | -9.22 | — | TECH_WATCH | 1.27 | no | — |
| AVEX | 3 | — | -9.08 | — | B | 0.89 | no | — |
| WWW | 3 | — | +8.82 | — | TECH_WATCH | 2.14 | no | — |
| OUST | 3 | — | -8.53 | — | B | 0.71 | no | — |
| CVLT | 3 | — | -8.48 | — | TECH_WATCH | 1.58 | no | — |
| PUBM | 3 | — | +8.36 | — | TECH_WATCH | 2.54 | no | — |

*184 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-13/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

