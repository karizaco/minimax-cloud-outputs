# Ledger — what every routine saw on 2026-11-05

**Source:** derived join over 5 artifact(s): `daily-screens/2026-11-05/{master,focus,tier-a}.csv`, `earnings/2026-11-05-reactions.md`, `us-eod/2026-11-05.csv`, `us-stocks-in-play/2026-11-05-candidates.csv`, `options-flow/2026-11-05.md` · **Built:** 2026-11-10 · **Covers:** 2002 name(s) any routine mentioned; 1707 seen by two or more · read-only

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
>    - 159 row(s) carry `catalyst_status: not_looked_up` — the earnings scanner states "no catalyst lookup (outside the per-run budget)" for them. That is a budget decision, not a finding of no catalyst.

## Coverage — what this ledger actually knows

| Routine | Rows it contributed to | Share |
|---|---|---|
| `screen` | 202 | 10% |
| `earnings` | 164 | 8% |
| `eod` | 1672 | 84% |
| `in_play` | 1933 | 97% |
| `options_flow` | 39 | 2% |

| Field | Filled | Null |
|---|---|---|
| `pre_mkt_pct` | 164 | 1838 |
| `settled_change_pct` | 1672 | 330 |
| `catalyst` | 164 | 1838 |
| `sector` | 1692 | 310 |
| `rvol` | 1933 | 69 |
| `gap_verdict` | 73 | 1929 |
| `options_own_history_ratio` | 30 | 1972 |
| `gap_outcome` | 164 | 1838 |

**What the coverage table means.** A low fill rate is not a fault in the
ledger — it is the actual overlap between routines that screen different
universes for different reasons. The daily sweep publishes 200 names, the
in-play digest over a thousand, the earnings scanner only names that reacted to
a print. A name in one and not the others is the normal case, and the point of
this table is that the gap is now measurable instead of being invisible.

### Catalyst coverage

| Status | Rows | Meaning |
|---|---|---|
| `no_earnings_row` | 1838 | the earnings scanner did not cover this name at all |
| `not_looked_up` | 159 | the scanner states the lookup was outside its per-run budget |
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
| MRVL | 5 | -4.41 | -16.43 | `extended` | C | 2.06 | yes | not_looked_up |
| ONDS | 5 | -3.42 | -14.23 | `extended` | B | 1.51 | yes | not_looked_up |
| RIOT | 5 | -2.08 | -3.97 | `extended` | B | 1.70 | yes | not_looked_up |
| APP | 4 | +21.47 | +31.04 | `extended` | A | 4.40 | no | sourced |
| AXTI | 4 | -5.97 | -22.76 | `extended` | B | 1.70 | no | not_looked_up |
| SNDK | 4 | -6.32 | -22.26 | `extended` | B | 3.00 | no | not_looked_up |
| AAOI | 4 | -4.40 | -20.89 | `extended` | B | 2.11 | no | not_looked_up |
| FPS | 4 | -4.19 | -18.85 | `extended` | B | 1.96 | no | not_looked_up |
| LITE | 4 | -4.72 | -18.68 | `extended` | C | 1.31 | no | not_looked_up |
| CRDO | 4 | -4.48 | -17.71 | `extended` | B | 1.85 | no | not_looked_up |
| MU | 4 | -4.55 | -17.46 | `extended` | B | 2.79 | yes | not_looked_up |
| AMD | 4 | -4.56 | -17.26 | `extended` | B | 2.54 | yes | not_looked_up |
| ENOV | 4 | +8.52 | +17.20 | `extended` | B | 2.62 | no | not_looked_up |
| BE | 4 | -5.64 | -16.41 | `extended` | TECH_WATCH | 1.93 | no | not_looked_up |
| FRMI | 4 | — | -15.93 | — | B | 1.89 | yes | — |
| NVTS | 4 | -4.82 | -15.76 | `extended` | B | 1.56 | no | not_looked_up |
| CIEN | 4 | -5.21 | -15.22 | `extended` | B | 1.97 | no | not_looked_up |
| VICR | 4 | -5.70 | -15.07 | `extended` | B | 1.77 | no | not_looked_up |
| DELL | 4 | -5.33 | -14.96 | `extended` | B | 2.26 | no | not_looked_up |
| APLD | 4 | -3.78 | -14.69 | `extended` | B | 1.95 | no | not_looked_up |
| CIFR | 4 | -4.14 | -14.62 | `extended` | B | 1.49 | no | not_looked_up |
| MARA | 4 | — | -14.48 | — | B | 1.13 | yes | — |
| SNAP | 4 | — | -14.02 | — | B | 1.66 | yes | — |
| VRT | 4 | -3.81 | -14.02 | `extended` | B | 2.11 | no | not_looked_up |
| IESC | 4 | -2.70 | -13.89 | `extended` | B | 1.82 | no | not_looked_up |
| STRL | 4 | -4.82 | -13.86 | `extended` | B | 1.63 | no | not_looked_up |
| VCEL | 4 | +7.50 | +13.85 | `extended` | B | 3.67 | no | not_looked_up |
| WULF | 4 | -2.91 | -13.85 | `extended` | B | 1.95 | no | not_looked_up |
| SEZL | 4 | +29.49 | +13.40 | `faded` | B | 3.17 | no | sourced |
| AMC | 4 | — | -12.50 | — | B | 1.67 | yes | — |
| ANET | 4 | -3.63 | -10.82 | `extended` | SOFT_A | 1.83 | no | not_looked_up |
| TSLA | 4 | -2.30 | -10.77 | `extended` | TECH_WATCH | 1.94 | yes | not_looked_up |
| AVGO | 4 | -2.56 | -10.43 | `extended` | B | 2.34 | yes | not_looked_up |
| INTC | 4 | -2.68 | -10.33 | `extended` | TECH_WATCH | 1.61 | no | not_looked_up |
| ASST | 4 | -2.13 | -10.17 | `extended` | B | 1.41 | no | not_looked_up |
| CRWV | 4 | -3.80 | -9.83 | `extended` | TECH_WATCH | 1.48 | no | not_looked_up |
| PLTR | 4 | -2.70 | -9.73 | `extended` | TECH_WATCH | 1.81 | yes | not_looked_up |
| DASH | 4 | -2.85 | -9.40 | `extended` | A | 2.93 | no | not_looked_up |
| SPCX | 4 | -2.51 | -9.05 | `extended` | TECH_WATCH | 1.53 | yes | not_looked_up |
| OUST | 4 | -6.05 | -9.00 | `extended` | B | 1.66 | no | not_looked_up |

*206 further row(s) in `ledger.jsonl`.*

## How to read `ledger.jsonl`

The first line is a `_meta` record carrying the sources, the coverage counts
and the deviations. Every line after it is one name.

```python
import json
with open('derived/2026-11-05/ledger.jsonl', encoding='utf-8') as fh:
    meta = json.loads(fh.readline())['_meta']
    rows = [json.loads(line) for line in fh]

# names the flow screen surfaced AND the earnings scanner had a catalyst for
both = [r for r in rows
        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']

# where the ledger does not know, rather than knows 'no'
print(meta['coverage']['fields']['catalyst'])
```

