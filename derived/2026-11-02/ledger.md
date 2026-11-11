# Ledger — what every routine saw on 2026-11-02

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-02/{master,focus,tier-a}.csv`, `earnings/2026-11-02-reactions.md`, `us-eod/2026-11-02.csv`, `us-stocks-in-play/2026-11-02-candidates.csv`, `options-flow/2026-11-02.md` · **Built:** 2026-11-11 · **Covers:** 1409 name(s) any routine mentioned; 1216 seen by two or more · read-only

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

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 200 | 14% |
| `earnings` | 73 | 5% |
| `eod` | 1198 | 85% |
| `in_play` | 1283 | 91% |
| `options_flow` | 8 | 1% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 73 | 1336 |
| `settled_change_pct` | 1197 | 212 |
| `catalyst` | 0 | 1409 |
| `sector` | 1198 | 211 |
| `rvol` | 198 | 1211 |
| `gap_verdict` | 193 | 1216 |
| `options_own_history_ratio` | 0 | 1409 |
| `gap_outcome` | 73 | 1336 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1336 | the earnings scanner did not cover this name at all |
| `absent` | 73 | the scanner had a row for the name but no catalyst text |

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
| PGEN | 4 | -30.55 | -25.94 | `held` | B | — | no | absent |
| TXG | 4 | +2.13 | -12.10 | `reversed` | B | 1.45 | no | absent |
| NTSK | 4 | +3.29 | -9.46 | `reversed` | B | — | no | absent |
| TEM | 4 | +3.85 | +8.67 | `extended` | A | 3.03 | no | absent |
| CRWV | 4 | +3.43 | -8.60 | `reversed` | B | 0.65 | no | absent |
| RIVN | 4 | +3.21 | +8.47 | `extended` | A | 2.03 | no | absent |
| GRAL | 4 | +3.21 | -6.74 | `reversed` | B | — | no | absent |
| WULF | 4 | +3.75 | -6.74 | `reversed` | B | 0.77 | no | absent |
| ULH | 3 | — | +26.34 | — | B | — | no | — |
| TWST | 3 | — | -15.54 | — | B | 1.08 | no | — |
| ABSI | 3 | +2.43 | -12.94 | `reversed` | B | — | no | absent |
| MRVL | 3 | — | -12.72 | — | A | 2.57 | no | — |
| AXTI | 3 | +3.03 | -12.46 | `reversed` | B | 1.41 | no | absent |
| PURR | 3 | — | -11.81 | — | B | — | no | — |
| PTEN | 3 | -2.33 | -11.41 | `extended` | B | — | no | absent |
| OKTA | 3 | — | -11.22 | — | B | 1.71 | no | — |
| REPL | 3 | — | +10.68 | — | B | — | no | — |
| P | 3 | — | -10.40 | — | B | 1.22 | no | — |
| RPD | 3 | — | -10.30 | — | B | — | no | — |
| VAL | 3 | -2.28 | -10.08 | `extended` | B | — | no | absent |
| AAOI | 3 | +2.24 | -9.49 | `reversed` | TECH_WATCH | 1.30 | no | absent |
| NSP | 3 | — | +9.24 | — | B | — | no | — |
| ONDS | 3 | — | -9.02 | — | B | 0.92 | no | — |
| APLD | 3 | +2.09 | -8.95 | `reversed` | B | 0.83 | no | absent |
| WING | 3 | — | +8.89 | — | SOFT_A | 1.49 | no | — |
| SAIL | 3 | — | -8.88 | — | B | — | no | — |
| REAL | 3 | — | +8.86 | — | B | — | no | — |
| INTC | 3 | — | -8.80 | — | B | 1.69 | no | — |
| NTRA | 3 | — | -8.54 | — | B | 1.75 | no | — |
| PENG | 3 | +2.91 | -8.53 | `reversed` | B | — | no | absent |
| VICR | 3 | +2.23 | -8.44 | `reversed` | B | — | no | absent |
| QMCO | 3 | — | -8.43 | — | B | — | no | — |
| CVLG | 3 | — | +8.25 | — | B | — | no | — |
| KVYO | 3 | — | +8.24 | — | TECH_WATCH | 2.25 | no | — |
| DDOG | 3 | +2.02 | -8.15 | `reversed` | B | 1.44 | no | absent |
| HTFL | 3 | — | -7.72 | — | B | — | no | — |
| SMP | 3 | — | +7.64 | — | B | — | no | — |
| RBRK | 3 | — | -7.64 | — | B | 1.09 | no | — |
| RKT | 3 | — | +7.58 | — | TECH_WATCH | 1.18 | no | — |
| AMD | 3 | — | -7.52 | — | B | 1.34 | no | — |

*89 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-02/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

