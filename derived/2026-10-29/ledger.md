# Ledger — what every routine saw on 2026-10-29

**Source:** derived join over 5 artifact(s): `daily-screens/2026-10-29/{master,focus,tier-a}.csv`, `earnings/2026-10-29-reactions.md`, `us-eod/2026-10-29.csv`, `us-stocks-in-play/2026-10-29-candidates.csv`, `options-flow/2026-10-29.md` · **Built:** 2026-11-10 · **Covers:** 532 name(s) any routine mentioned; 452 seen by two or more · read-only

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
| `screen` | 456 | 86% |
| `earnings` | 124 | 23% |
| `eod` | 439 | 83% |
| `in_play` | 37 | 7% |
| `options_flow` | 8 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 124 | 408 |
| `settled_change_pct` | 439 | 93 |
| `catalyst` | 0 | 532 |
| `sector` | 519 | 13 |
| `rvol` | 0 | 532 |
| `gap_verdict` | 0 | 532 |
| `options_own_history_ratio` | 0 | 532 |
| `gap_outcome` | 124 | 408 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 408 | the earnings scanner did not cover this name at all |
| `absent` | 124 | the scanner had a row for the name but no catalyst text |

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
| GOOGL | 5 | -11.30 | -12.64 | `extended` | A | — | yes | absent |
| MRVL | 4 | -11.38 | -13.24 | `extended` | C | — | no | absent |
| SNDK | 4 | -2.49 | -5.32 | `extended` | B | — | no | absent |
| MU | 4 | -2.58 | -4.98 | `extended` | B | — | no | absent |
| AMZN | 4 | — | -4.25 | — | B | — | yes | — |
| BE | 4 | -4.20 | -2.52 | `held` | B | — | no | absent |
| VRT | 4 | -3.04 | +1.24 | `reversed` | CARRY | — | no | absent |
| LITE | 4 | +5.80 | +0.61 | `faded` | A | — | no | absent |
| PRCH | 3 | +20.61 | +28.16 | `extended` | master | — | no | absent |
| NOW | 3 | -19.81 | -26.97 | `extended` | A | — | no | absent |
| TDOC | 3 | +14.10 | +26.82 | `extended` | master | — | no | absent |
| FTNT | 3 | -26.04 | -20.09 | `held` | A | — | no | absent |
| FTAI | 3 | +6.05 | +17.27 | `extended` | master | — | no | absent |
| FTRE | 3 | -7.34 | -10.61 | `extended` | master | — | no | absent |
| CIFR | 3 | -4.74 | -8.68 | `extended` | master | — | no | absent |
| LLY | 3 | +4.46 | +6.57 | `extended` | master | — | no | absent |
| WOLF | 3 | -4.28 | -6.38 | `extended` | master | — | no | absent |
| SAIA | 3 | +2.58 | +5.68 | `extended` | master | — | no | absent |
| AXTI | 3 | -7.19 | -5.44 | `held` | master | — | no | absent |
| GLXY | 3 | -4.61 | -5.03 | `extended` | master | — | no | absent |
| CRWV | 3 | -6.54 | -4.99 | `held` | master | — | no | absent |
| CSTL | 3 | +3.46 | +4.99 | `extended` | master | — | no | absent |
| WULF | 3 | -4.25 | -4.99 | `extended` | master | — | no | absent |
| WING | 3 | — | +4.92 | — | CARRY | — | no | — |
| RIOT | 3 | -4.36 | -4.91 | `extended` | master | — | no | absent |
| CRDO | 3 | -3.93 | -4.84 | `extended` | master | — | no | absent |
| APLD | 3 | -4.22 | -4.81 | `extended` | master | — | no | absent |
| PWR | 3 | +5.62 | +4.66 | `held` | master | — | no | absent |
| CRM | 3 | -6.24 | -4.61 | `held` | B | — | no | absent |
| CLSK | 3 | -3.27 | -4.43 | `extended` | master | — | no | absent |
| LPLA | 3 | — | +3.84 | — | CARRY | — | no | — |
| CORZ | 3 | -3.67 | -3.80 | `held` | master | — | no | absent |
| INTC | 3 | -3.12 | -3.62 | `extended` | master | — | no | absent |
| RRC | 3 | — | -3.56 | — | C | — | no | — |
| TYL | 3 | -6.27 | +3.54 | `reversed` | master | — | no | absent |
| PANW | 3 | -6.84 | -3.53 | `held` | B | — | no | absent |
| TTMI | 3 | -3.07 | -3.48 | `extended` | master | — | no | absent |
| ORCL | 3 | — | -3.45 | — | CARRY | — | no | — |
| VIAV | 3 | -2.99 | -3.31 | `extended` | master | — | no | absent |
| MOD | 3 | -4.42 | -3.30 | `held` | master | — | no | absent |

*31 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-29/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

