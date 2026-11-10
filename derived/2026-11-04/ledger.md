# Ledger — what every routine saw on 2026-11-04

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-04/{master,focus,tier-a}.csv`, `earnings/2026-11-04-reactions.md`, `us-eod/2026-11-04.csv`, `us-stocks-in-play/2026-11-04-candidates.csv`, `options-flow/2026-11-04.md` · **Built:** 2026-11-10 · **Covers:** 2097 name(s) any routine mentioned; 1731 seen by two or more · read-only

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
| `screen` | 200 | 10% |
| `earnings` | 171 | 8% |
| `eod` | 1696 | 81% |
| `in_play` | 2048 | 98% |
| `options_flow` | 8 | 0% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 171 | 1926 |
| `settled_change_pct` | 1696 | 401 |
| `catalyst` | 0 | 2097 |
| `sector` | 1718 | 379 |
| `rvol` | 2043 | 54 |
| `gap_verdict` | 70 | 2027 |
| `options_own_history_ratio` | 0 | 2097 |
| `gap_outcome` | 171 | 1926 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1926 | the earnings scanner did not cover this name at all |
| `absent` | 171 | the scanner had a row for the name but no catalyst text |

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
| AMZN | 5 | +3.56 | +6.12 | `extended` | SOFT_A | 1.42 | yes | absent |
| KD | 4 | +11.67 | +30.06 | `extended` | A | 3.18 | no | absent |
| ECG | 4 | -7.30 | -29.29 | `extended` | A | 3.52 | no | absent |
| DUOL | 4 | +19.51 | +25.99 | `extended` | A | 7.04 | no | absent |
| HUT | 4 | -10.90 | -23.23 | `extended` | A | 2.26 | no | absent |
| CIFR | 4 | -15.52 | -19.95 | `extended` | SOFT_A | 1.90 | no | absent |
| FPS | 4 | -5.75 | -17.34 | `extended` | TECH_WATCH | 1.26 | no | absent |
| GLXY | 4 | -7.84 | -16.99 | `extended` | TECH_WATCH | 1.51 | no | absent |
| SEI | 4 | -6.30 | -16.92 | `extended` | B | 2.62 | no | absent |
| CLSK | 4 | -9.13 | -16.56 | `extended` | SOFT_A | 1.89 | no | absent |
| AGX | 4 | -3.80 | -16.54 | `extended` | TECH_WATCH | 1.39 | no | absent |
| FIX | 4 | -11.01 | -15.22 | `extended` | SOFT_A | 1.99 | no | absent |
| PFGC | 4 | +3.00 | +13.63 | `extended` | B | 2.68 | no | absent |
| MRNA | 4 | +2.75 | +13.11 | `extended` | B | 0.65 | no | absent |
| VRT | 4 | -7.09 | -12.88 | `extended` | SOFT_A | 1.27 | no | absent |
| POWL | 4 | -4.71 | -12.39 | `extended` | TECH_WATCH | 1.16 | no | absent |
| PWR | 4 | -5.18 | -11.67 | `extended` | SOFT_A | 1.80 | no | absent |
| SEZL | 4 | +4.72 | +11.65 | `extended` | TECH_WATCH | 1.29 | no | absent |
| EROC | 4 | -2.79 | -11.44 | `extended` | B | 2.44 | no | absent |
| NXT | 4 | +6.23 | +11.12 | `extended` | SOFT_A | 2.90 | no | absent |
| CORZ | 4 | -6.60 | -10.39 | `extended` | TECH_WATCH | 1.45 | no | absent |
| HCA | 4 | +5.86 | +10.39 | `extended` | SOFT_A | 1.89 | no | absent |
| ALHC | 4 | +2.58 | +10.15 | `extended` | B | 0.54 | no | absent |
| CRWV | 4 | -6.96 | -9.90 | `extended` | B | 0.91 | no | absent |
| ZG | 4 | +4.66 | +9.89 | `extended` | B | 2.12 | no | absent |
| MMM | 4 | +3.36 | +9.57 | `extended` | SOFT_A | 1.82 | no | absent |
| CRDO | 4 | -4.83 | -9.55 | `extended` | SOFT_A | 1.04 | no | absent |
| MYRG | 4 | -2.26 | -9.50 | `extended` | TECH_WATCH | 1.05 | no | absent |
| ISRG | 4 | +3.23 | +9.38 | `extended` | TECH_WATCH | 1.32 | no | absent |
| TLN | 4 | -4.84 | -8.54 | `extended` | TECH_WATCH | 1.85 | no | absent |
| SHLS | 4 | +6.26 | +8.15 | `extended` | B | 5.50 | no | absent |
| MRVL | 4 | -2.62 | -7.08 | `extended` | C | 1.33 | no | absent |
| WDC | 4 | -2.97 | -6.77 | `extended` | B | 0.62 | no | absent |
| APLD | 4 | -6.18 | -6.74 | `extended` | TECH_WATCH | 1.16 | no | absent |
| MSFT | 4 | +2.28 | +6.68 | `extended` | SOFT_A | 1.56 | yes | absent |
| WULF | 4 | -4.87 | -6.62 | `extended` | TECH_WATCH | 1.42 | no | absent |
| AEHR | 4 | -2.83 | -6.56 | `extended` | TECH_WATCH | 1.12 | no | absent |
| AAPL | 4 | — | +5.31 | — | SOFT_A | 1.34 | yes | — |
| FRVO | 4 | +2.58 | -4.51 | `reversed` | TECH_WATCH | 1.23 | no | absent |
| MARA | 4 | -5.59 | -4.05 | `held` | TECH_WATCH | 1.17 | no | absent |

*209 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-04/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

