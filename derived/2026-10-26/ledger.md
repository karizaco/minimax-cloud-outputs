# Ledger — what every routine saw on 2026-10-26

**Source:** derived join over 5 artifact(s): `daily-screens/2026-10-26/{master,focus,tier-a}.csv`, `earnings/2026-10-26-reactions.md`, `us-eod/2026-10-26.csv`, `us-stocks-in-play/2026-10-26-candidates.csv`, `options-flow/2026-10-26.md` · **Built:** 2026-11-10 · **Covers:** 428 name(s) any routine mentioned; 387 seen by two or more · read-only

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
| `screen` | 200 | 47% |
| `earnings` | 33 | 8% |
| `eod` | 387 | 90% |
| `in_play` | 319 | 75% |
| `options_flow` | 0 | 0% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 33 | 395 |
| `settled_change_pct` | 387 | 41 |
| `catalyst` | 0 | 428 |
| `sector` | 387 | 41 |
| `rvol` | 0 | 428 |
| `gap_verdict` | 0 | 428 |
| `options_own_history_ratio` | 0 | 428 |
| `gap_outcome` | 33 | 395 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 395 | the earnings scanner did not cover this name at all |
| `absent` | 33 | the scanner had a row for the name but no catalyst text |

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
| XP | 4 | -47.65 | -47.68 | `held` | A | — | no | absent |
| RRC | 4 | +10.83 | +17.25 | `extended` | C | — | no | absent |
| NN | 4 | -2.28 | +14.29 | `reversed` | B | — | no | absent |
| WGS | 4 | +2.49 | +9.03 | `extended` | B | — | no | absent |
| BE | 4 | +2.15 | +6.26 | `extended` | TECH_WATCH | — | no | absent |
| TSLA | 4 | +2.38 | +5.71 | `extended` | SOFT_A | — | no | absent |
| SMTC | 4 | +3.03 | +4.48 | `extended` | B | — | no | absent |
| SGRY | 3 | — | +47.65 | — | C | — | no | — |
| AGBK | 3 | -21.50 | -38.19 | `extended` | ANNEX | — | no | absent |
| INTR | 3 | -37.13 | -35.33 | `held` | A | — | no | absent |
| ORIC | 3 | -2.20 | -31.47 | `extended` | A | — | no | absent |
| AVBP | 3 | +2.38 | -28.07 | `reversed` | A | — | no | absent |
| XNCR | 3 | — | +15.85 | — | SOFT_A | — | no | — |
| BLSM | 3 | — | +13.67 | — | B | — | no | — |
| RGC | 3 | +2.83 | -12.65 | `reversed` | B | — | no | absent |
| ORKA | 3 | — | +12.33 | — | B | — | no | — |
| VICR | 3 | — | +11.20 | — | B | — | no | — |
| INIO | 3 | — | +10.55 | — | B | — | no | — |
| CD | 3 | — | +10.10 | — | B | — | no | — |
| AXTI | 3 | — | +8.97 | — | B | — | no | — |
| LITE | 3 | — | +8.91 | — | TECH_WATCH | — | no | — |
| AAOI | 3 | — | +8.83 | — | B | — | no | — |
| ANGX | 3 | — | +8.74 | — | B | — | no | — |
| REPL | 3 | — | +8.65 | — | B | — | no | — |
| ASST | 3 | — | -8.42 | — | B | — | no | — |
| TTMI | 3 | — | +8.23 | — | TECH_WATCH | — | no | — |
| MELI | 3 | -14.49 | -8.14 | `held` | B | — | no | absent |
| VSAT | 3 | — | +8.12 | — | B | — | no | — |
| TSEM | 3 | — | +8.03 | — | B | — | no | — |
| FIX | 3 | — | +7.43 | — | TECH_WATCH | — | no | — |
| TENB | 3 | — | +7.42 | — | B | — | no | — |
| DOCN | 3 | — | +7.41 | — | B | — | no | — |
| PARR | 3 | — | +7.38 | — | B | — | no | — |
| RMBS | 3 | — | +7.31 | — | B | — | no | — |
| CRCL | 3 | — | -7.21 | — | B | — | no | — |
| P | 3 | — | +7.19 | — | B | — | no | — |
| BAH | 3 | — | +7.16 | — | B | — | no | — |
| WULF | 3 | — | +6.80 | — | B | — | no | — |
| CVI | 3 | — | +6.73 | — | B | — | no | — |
| ACDC | 3 | — | +6.63 | — | B | — | no | — |

*77 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-10-26/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

