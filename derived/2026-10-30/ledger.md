# Ledger — what every routine saw on 2026-10-30

**Source:** derived join over 4 artifact(s): `daily-screens/2026-10-30/{master,focus,tier-a}.csv`, `us-eod/2026-10-30.csv`, `us-stocks-in-play/2026-10-30-candidates.csv`, `options-flow/2026-10-30.md` · **Built:** 2026-11-11 · **Covers:** 449 name(s) any routine mentioned; 385 seen by two or more · read-only

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
>    - No reactions artifact for 2026-10-30 (`earnings/<date>-reactions.md`), so no pre-market gap or catalyst is available for any row.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 409 | 91% |
| `earnings` | 0 | 0% |
| `eod` | 379 | 84% |
| `in_play` | 89 | 20% |
| `options_flow` | 8 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 0 | 449 |
| `settled_change_pct` | 379 | 70 |
| `catalyst` | 0 | 449 |
| `sector` | 441 | 8 |
| `rvol` | 80 | 369 |
| `gap_verdict` | 0 | 449 |
| `options_own_history_ratio` | 0 | 449 |
| `gap_outcome` | 0 | 449 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 449 | the earnings scanner did not cover this name at all |

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
| NVDA | 4 | — | -4.22 | — | A | 0.65 | yes | — |
| AMZN | 4 | — | -1.41 | — | A | 1.42 | yes | — |
| GDYN | 3 | — | +40.78 | — | SOFT_A | 2.73 | no | — |
| ULH | 3 | — | +29.68 | — | SOFT_A | — | no | — |
| INTC | 3 | — | -28.58 | — | A | 2.67 | no | — |
| OSPN | 3 | — | +27.34 | — | SOFT_A | 2.51 | no | — |
| ACCO | 3 | — | +26.03 | — | SOFT_A | 2.94 | no | — |
| CDNA | 3 | — | +22.22 | — | SOFT_A | 1.64 | no | — |
| ILMN | 3 | — | -18.64 | — | SOFT_A | 1.38 | no | — |
| CVEO | 3 | — | +17.68 | — | SOFT_A | 3.47 | no | — |
| TWLO | 3 | — | -15.13 | — | SOFT_A | 1.52 | no | — |
| FDXF | 3 | — | +14.84 | — | SOFT_A | 0.97 | no | — |
| SNDK | 3 | — | -13.47 | — | A | 1.03 | no | — |
| REGN | 3 | — | +13.33 | — | SOFT_A | 2.45 | no | — |
| CVCO | 3 | — | +13.11 | — | SOFT_A | 1.65 | no | — |
| TWST | 3 | — | -11.92 | — | B | 0.85 | no | — |
| DDOG | 3 | — | -11.50 | — | TECH_WATCH | 0.98 | no | — |
| IOVA | 3 | — | -11.30 | — | B | — | no | — |
| BTSG | 3 | — | +11.08 | — | SOFT_A | 1.26 | no | — |
| ALAB | 3 | — | -10.93 | — | SOFT_A | — | no | — |
| AMD | 3 | — | -10.88 | — | A | 0.92 | no | — |
| DELL | 3 | — | -10.80 | — | A | 0.86 | no | — |
| SMP | 3 | — | +10.75 | — | SOFT_A | 1.11 | no | — |
| COIN | 3 | — | -10.62 | — | A | 1.54 | no | — |
| MRVL | 3 | — | -10.05 | — | A | 0.91 | no | — |
| GRAL | 3 | — | -9.75 | — | B | — | no | — |
| CRWV | 3 | — | -9.66 | — | A | 0.38 | no | — |
| AXTI | 3 | — | -9.56 | — | SOFT_A | 0.74 | no | — |
| NET | 3 | — | -9.54 | — | TECH_WATCH | 0.79 | no | — |
| CRCL | 3 | — | -9.41 | — | SOFT_A | 0.85 | no | — |
| BE | 3 | — | -8.61 | — | A | — | no | — |
| LITE | 3 | — | -8.57 | — | A | 0.86 | no | — |
| MDB | 3 | — | -8.31 | — | TECH_WATCH | 0.42 | no | — |
| ANET | 3 | — | -8.28 | — | SOFT_A | 0.49 | no | — |
| STX | 3 | — | -7.98 | — | A | 0.39 | no | — |
| MSTR | 3 | — | -7.84 | — | B | 1.06 | no | — |
| WDC | 3 | — | -7.41 | — | B | 0.35 | no | — |
| RBRK | 3 | — | -7.11 | — | TECH_WATCH | 0.60 | no | — |
| VLTO | 3 | — | +6.76 | — | SOFT_A | 0.78 | no | — |
| HIMS | 3 | — | -6.71 | — | TECH_WATCH | — | no | — |

*9 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-30/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

