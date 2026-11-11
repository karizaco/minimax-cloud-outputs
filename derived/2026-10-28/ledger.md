# Ledger — what every routine saw on 2026-10-28

**Source:** derived join over 4 artifact(s): `daily-screens/2026-10-28/{master,focus,tier-a}.csv`, `us-eod/2026-10-28.csv`, `us-stocks-in-play/2026-10-28-candidates.csv`, `options-flow/2026-10-28.md` · **Built:** 2026-11-11 · **Covers:** 600 name(s) any routine mentioned; 533 seen by two or more · read-only

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
>    - No reactions artifact for 2026-10-28 (`earnings/<date>-reactions.md`), so no pre-market gap or catalyst is available for any row.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 200 | 33% |
| `earnings` | 0 | 0% |
| `eod` | 525 | 88% |
| `in_play` | 446 | 74% |
| `options_flow` | 8 | 1% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 0 | 600 |
| `settled_change_pct` | 525 | 75 |
| `catalyst` | 0 | 600 |
| `sector` | 525 | 75 |
| `rvol` | 0 | 600 |
| `gap_verdict` | 0 | 600 |
| `options_own_history_ratio` | 0 | 600 |
| `gap_outcome` | 0 | 600 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 600 | the earnings scanner did not cover this name at all |

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
| PRME | 3 | — | +23.22 | — | master,focus,tier-a | — | no | — |
| REPL | 3 | — | +23.07 | — | master | — | no | — |
| SDGR | 3 | — | +15.53 | — | master,focus | — | no | — |
| SLS | 3 | — | -14.71 | — | B | — | no | — |
| ULCC | 3 | — | +11.57 | — | master | — | no | — |
| VSAT | 3 | — | +11.32 | — | master | — | no | — |
| GLXY | 3 | — | +11.12 | — | master | — | no | — |
| AXTI | 3 | — | +10.56 | — | master | — | no | — |
| TWST | 3 | — | +8.51 | — | master | — | no | — |
| NTLA | 3 | — | +8.47 | — | master | — | no | — |
| SNDK | 3 | — | +7.66 | — | SOFT_A | — | no | — |
| ARCT | 3 | — | +7.48 | — | master | — | no | — |
| RXRX | 3 | — | +7.41 | — | master | — | no | — |
| TXG | 3 | — | +7.18 | — | master | — | no | — |
| PRIM | 3 | — | +6.71 | — | master | — | no | — |
| KNSA | 3 | — | +6.70 | — | master,focus,tier-a | — | no | — |
| RIOT | 3 | — | +6.56 | — | master | — | no | — |
| HRI | 3 | — | +6.52 | — | master | — | no | — |
| KOD | 3 | — | +6.26 | — | master | — | no | — |
| TEM | 3 | — | +6.18 | — | master | — | no | — |
| WULF | 3 | — | +6.00 | — | master | — | no | — |
| TLS | 3 | — | +5.82 | — | master | — | no | — |
| AMKR | 3 | — | +5.68 | — | master | — | no | — |
| SEI | 3 | — | +5.66 | — | master | — | no | — |
| LITE | 3 | — | +5.52 | — | TECH_WATCH | — | no | — |
| CAI | 3 | — | +5.29 | — | master | — | no | — |
| CORZ | 3 | — | +5.15 | — | master | — | no | — |
| HIMS | 3 | — | +5.12 | — | master | — | no | — |
| RGEN | 3 | — | +5.06 | — | master | — | no | — |
| GRAL | 3 | — | +4.83 | — | master | — | no | — |
| QNT | 3 | — | -4.68 | — | master | — | no | — |
| SOFI | 3 | — | +4.51 | — | TECH_WATCH | — | no | — |
| STX | 3 | — | +4.51 | — | TECH_WATCH | — | no | — |
| BE | 3 | — | +4.34 | — | TECH_WATCH | — | no | — |
| THRM | 3 | — | +4.21 | — | master | — | no | — |
| IRON | 3 | — | +4.13 | — | master | — | no | — |
| WDC | 3 | — | +4.08 | — | TECH_WATCH | — | no | — |
| VG | 3 | — | +3.98 | — | master | — | no | — |
| CRDO | 3 | — | +3.74 | — | master | — | no | — |
| PNR | 3 | — | +3.37 | — | master | — | no | — |

*6 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-28/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

