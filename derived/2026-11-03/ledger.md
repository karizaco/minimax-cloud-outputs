# Ledger — what every routine saw on 2026-11-03

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-03/{master,focus,tier-a}.csv`, `earnings/2026-11-03-reactions.md`, `us-eod/2026-11-03.csv`, `us-stocks-in-play/2026-11-03-candidates.csv`, `options-flow/2026-11-03.md` · **Built:** 2026-11-09 · **Covers:** 914 name(s) any routine mentioned; 780 seen by two or more · read-only

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
| `screen` | 200 | 22% |
| `earnings` | 6 | 1% |
| `eod` | 769 | 84% |
| `in_play` | 788 | 86% |
| `options_flow` | 8 | 1% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 6 | 908 |
| `settled_change_pct` | 769 | 145 |
| `catalyst` | 0 | 914 |
| `sector` | 768 | 146 |
| `rvol` | 786 | 128 |
| `gap_verdict` | 157 | 757 |
| `options_own_history_ratio` | 0 | 914 |
| `gap_outcome` | 6 | 908 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 908 | the earnings scanner did not cover this name at all |
| `absent` | 6 | the scanner had a row for the name but no catalyst text |

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
| UPWK | 4 | +4.64 | +2.16 | `faded` | B | 2.63 | no | absent |
| AEHR | 3 | — | +26.50 | — | A | 3.63 | no | — |
| GPK | 3 | — | +21.54 | — | A | 2.30 | no | — |
| RIOT | 3 | — | +18.41 | — | TECH_WATCH | 1.94 | no | — |
| CIFR | 3 | — | +18.37 | — | TECH_WATCH | 1.39 | no | — |
| XMTR | 3 | — | +16.55 | — | A | 3.49 | no | — |
| GLXY | 3 | — | +15.35 | — | TECH_WATCH | 0.96 | no | — |
| WULF | 3 | — | +14.53 | — | TECH_WATCH | 1.06 | no | — |
| CLSK | 3 | — | +13.99 | — | TECH_WATCH | 1.18 | no | — |
| CORZ | 3 | — | +13.87 | — | TECH_WATCH | 1.44 | no | — |
| CVI | 3 | — | -13.10 | — | B | 4.06 | no | — |
| ULCC | 3 | -2.42 | -12.92 | `extended` | B | 1.49 | no | absent |
| FISV | 3 | — | +12.46 | — | A | 3.09 | no | — |
| ULH | 3 | — | +12.12 | — | B | 2.01 | no | — |
| PAY | 3 | — | -11.50 | — | B | 2.02 | no | — |
| SHLS | 3 | — | +11.45 | — | B | 2.19 | no | — |
| MARA | 3 | — | +11.35 | — | TECH_WATCH | 0.98 | no | — |
| IOVA | 3 | — | +10.10 | — | TECH_WATCH | 0.77 | no | — |
| RSI | 3 | — | +10.00 | — | TECH_WATCH | 1.28 | no | — |
| APLD | 3 | — | +9.80 | — | TECH_WATCH | 1.09 | no | — |
| ECG | 3 | — | +9.74 | — | B | 2.60 | no | — |
| BE | 3 | — | +9.05 | — | SOFT_A | 0.72 | no | — |
| ENPH | 3 | — | +8.91 | — | TECH_WATCH | 0.91 | no | — |
| NVTS | 3 | — | +7.95 | — | TECH_WATCH | 1.58 | no | — |
| TLN | 3 | — | +7.29 | — | B | 2.48 | no | — |
| CRWV | 3 | — | +7.16 | — | TECH_WATCH | 0.54 | no | — |
| FMC | 3 | — | -6.62 | — | B | 0.59 | no | — |
| DXC | 3 | — | -6.57 | — | B | 0.71 | no | — |
| AXTI | 3 | — | +6.49 | — | TECH_WATCH | 1.03 | no | — |
| IONQ | 3 | — | +6.46 | — | TECH_WATCH | 0.78 | no | — |
| SITM | 3 | — | +6.46 | — | TECH_WATCH | 1.90 | no | — |
| RBLX | 3 | — | +6.04 | — | TECH_WATCH | 0.78 | no | — |
| REPL | 3 | — | +5.95 | — | TECH_WATCH | 1.24 | no | — |
| TXG | 3 | — | +5.94 | — | TECH_WATCH | 0.78 | no | — |
| ORCL | 3 | — | +5.86 | — | TECH_WATCH | 1.77 | no | — |
| RDDT | 3 | — | +5.72 | — | TECH_WATCH | 0.69 | no | — |
| KDP | 3 | — | -5.65 | — | SOFT_A | 1.75 | no | — |
| NWL | 3 | — | -5.54 | — | B | 1.13 | no | — |
| COIN | 3 | — | +5.53 | — | TECH_WATCH | 1.24 | no | — |
| APH | 3 | — | +5.40 | — | TECH_WATCH | 0.80 | no | — |

*36 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-03/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

