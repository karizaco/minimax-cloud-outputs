# SIP staged observations runbook

This is an offline pilot harness. It does not activate routines, schedules, brokers,
network adapters, historical backfill, or catalyst inference.

## Install and test

Python 3.11 and pytest are sufficient. From `market-intel/`, install the test
dependency and run the staged tests with:

```sh
python -m pip install pytest
PYTHONPATH=. python -m pytest -q tests/test_outcomes.py tests/test_change_chat.py
```

The canonical staged entrypoint is `python -m sip.staged_cli`.

Outputs are restricted to `/workspace/stage` or `/tmp`. State and CSV symlink
targets are rejected, as are `/home/box` and `/workspace/market-intel`. The writer
is single-writer; coordinate concurrent callers. Atomic replacement prevents a
partial file, but does not provide a database transaction.

## Outcome CLI and schemas

```sh
python -m sip.staged_cli outcomes --input /tmp/outcomes-input.json \
  --state-dir /workspace/stage/sip-outcomes --retention 0.5 \
  --max-quote-age-seconds 60
```

`--retention` is required and is a **gap retention threshold**, not sampling.
For an up gap `O > P`, down gap `O < P`, observed price `X`, and threshold `r`,
`ratio=(X-P)/(O-P)`. A flat gap is flat. `ratio<=0` is reversed (the observed
price is at or below prior close for an up gap, or at or above it for a down gap);
`0<ratio<r` is faded; `ratio>=r` is held. The signed formula works in both gap
directions. The same threshold controls outcome collection/classification and
midday numeric classification. For example, `.5` is an illustrative caller policy,
not a default.

Input is JSON with `calendars`, `flags`, and `observations`.

A calendar requires `calendar_id`, `market`, `venue`, fixed IANA `timezone`, and
ordered `sessions`. A session requires unique `session_id`, unique local `date`,
and aware `open`/`close` exact instants. Sessions cannot overlap. Calendars are
append-only and immutable: existing session facts and order cannot change.
Calendar price basis is intentionally not required; basis belongs to instrument
observations.

A flag requires `market`, `venue`, `ticker`, `tier`, `catalyst`, `calendar_id`,
`session_id`, aware `flag_timestamp`, `flag_price` (positive number or null),
`quote_timestamp`, `quote_provenance`, `currency`, `price_basis`, and
`adjustment_id`. The timestamp must be inside the declared session. If
`flag_price` is null, quote timestamp and provenance must also be null and no
historical price is manufactured. Otherwise quote time must be no later than the
flag and no older than the finite bound (default 60 seconds). An invalid or stale
quote yields null `same_close_vs_flag_pct`.

An observation requires the complete lookup tuple `market`, `venue`,
`calendar_id`, `ticker`, `session_id`, plus `date`, exact session-close
`timestamp`, `open`, `prior_close`, `close`, `final:true`, `currency`,
`price_basis`, `adjustment_id`, and `provenance`. `close` is positive and finite.
`open` and `prior_close` may be null to state an explicit unknown gap; they are
not silently replaced. Observation lookup includes market, venue, calendar,
ticker, and session. Wrong session/date, nonfinite values, and basis conflicts fail.

The stable ID is SHA-256 over normalized UTC
`market|venue|ticker|flag_timestamp`. Equivalent aware timestamp spellings
therefore identify one flag. All flag facts, including tier and catalyst, are
immutable. Duplicate/conflicting inputs and corrupt persisted schemas are
rejected without overwriting state. Persisted calendars, flags, and observations
are deeply validated before any replacement. Reruns with `flags:[]` refresh every pending
record. Observations are immutable and may fill pending records.

`same_close_vs_flag_pct=(C/F-1)*100` when comparable. Independently,
`next_close_vs_same_close_pct=(N/C-1)*100` whenever own and next-session bars
are comparable, even if `F` is unavailable. Derived rows and CSV retain actual
`same_session_close` and `next_session_close`, tier, catalyst, flag data, basis,
gap cohort, ratio, classification, status, and reasons. These are descriptive
moves, not simulated P&L. Flag direction is never inferred; the gap cohort is
separate. Missing prices and basis mismatches have explicit reasons.

## Runnable synthetic outcome fixture

```json
{
  "calendars": [{
    "calendar_id":"NYSE","market":"US","venue":"NYSE","timezone":"America/New_York",
    "sessions":[
      {"session_id":"2024-11-04","date":"2024-11-04","open":"2024-11-04T09:30:00-05:00","close":"2024-11-04T16:00:00-05:00"},
      {"session_id":"2024-11-05","date":"2024-11-05","open":"2024-11-05T09:30:00-05:00","close":"2024-11-05T16:00:00-05:00"}
    ]
  }],
  "flags":[{
    "market":"US","venue":"NYSE","ticker":"AAA","tier":"A","catalyst":"synthetic",
    "calendar_id":"NYSE","session_id":"2024-11-04","flag_timestamp":"2024-11-04T10:00:00-05:00",
    "flag_price":100,"quote_timestamp":"2024-11-04T10:00:00-05:00","quote_provenance":"fixture",
    "currency":"USD","price_basis":"raw","adjustment_id":"none"
  }],
  "observations":[]
}
```

Save it as `/tmp/outcomes-input.json` and run the command above. To complete the
example, replace it with the following JSON and rerun the same command:

```json
{
  "calendars": [{
    "calendar_id":"NYSE","market":"US","venue":"NYSE","timezone":"America/New_York",
    "sessions":[
      {"session_id":"2024-11-04","date":"2024-11-04","open":"2024-11-04T09:30:00-05:00","close":"2024-11-04T16:00:00-05:00"},
      {"session_id":"2024-11-05","date":"2024-11-05","open":"2024-11-05T09:30:00-05:00","close":"2024-11-05T16:00:00-05:00"}
    ]
  }],
  "flags":[{
    "market":"US","venue":"NYSE","ticker":"AAA","tier":"A","catalyst":"synthetic",
    "calendar_id":"NYSE","session_id":"2024-11-04","flag_timestamp":"2024-11-04T10:00:00-05:00",
    "flag_price":100,"quote_timestamp":"2024-11-04T10:00:00-05:00","quote_provenance":"fixture",
    "currency":"USD","price_basis":"raw","adjustment_id":"none"
  }],
  "observations":[
    {
      "market":"US","venue":"NYSE","calendar_id":"NYSE","ticker":"AAA",
      "session_id":"2024-11-04","date":"2024-11-04",
      "timestamp":"2024-11-04T16:00:00-05:00",
      "open":101,"prior_close":100,"close":102,"final":true,
      "currency":"USD","price_basis":"raw","adjustment_id":"none","provenance":"fixture"
    },
    {
      "market":"US","venue":"NYSE","calendar_id":"NYSE","ticker":"AAA",
      "session_id":"2024-11-05","date":"2024-11-05",
      "timestamp":"2024-11-05T16:00:00-05:00",
      "open":102,"prior_close":102,"close":103,"final":true,
      "currency":"USD","price_basis":"raw","adjustment_id":"none","provenance":"fixture"
    }
  ]
}
```

The first run creates pending state. The second run completes the same flag.
The pytest fixture is an executable example.

## Midday chat

```sh
python -m sip.staged_cli midday --open /tmp/open.json --midday /tmp/midday.json \
  --retention 0.5 --max-open-age-hours 6
```

Snapshots require `market`, `session_id`, `calendar_id`, IANA `timezone`, explicit
`session_date`, aware `asof`, `slot`, and `rows`. The local `asof` date must equal
`session_date`. Market, session, calendar, timezone, and date must match across
snapshots; the open must precede midday. A missing or stale baseline is
conspicuously `BASELINE_UNAVAILABLE`, allows conservative current rows, and makes
no comparison claim.

Each row requires `ticker`, `tier`, `session_open`, `prior_close`, `price`,
`currency`, `price_basis`, and `adjustment_id`. Values may be null to produce a
clear warning. Supplied `held`, `faded`, `reversed`, and `gap_state` fields are
never trusted or required. Numeric old and new states are independently computed
from each snapshot's actual same-day open, prior close, and price using the gap
threshold. Basis/currency or open/prior-close mismatches warn and prevent a gap
claim.

With a valid baseline, output contains only changed/new/removed names and
warnings, never every current row. Unchanged fully-known rows yield only
`No material changes`. New, removed, tier upgrades/downgrades, and gap state
changes are shown with old and new labels. Removed rows preserve the old row.
Rows are ordered A, Soft-A, TECH_WATCH, B, C, then descending supplied USD
turnover, then ticker. Taiwan `.TW` names are not automatically displayed as `.TPEX`; Tokyo uses
`company_en` or explicit unavailable. USD turnover is labelled USD and local
turnover keeps its supplied currency. TECH_WATCH has one ticker per line.

Example open snapshot:

```json
{
  "market":"US","session_id":"2024-11-04","calendar_id":"NYSE",
  "timezone":"America/New_York","session_date":"2024-11-04",
  "asof":"2024-11-04T09:30:00-05:00","slot":"open",
  "rows":[{
    "ticker":"AAA","tier":"A","session_open":101,"prior_close":100,
    "price":101,"currency":"USD","price_basis":"raw","adjustment_id":"none",
    "usd_turnover":5000000
  }]
}
```

Example midday snapshot:

```json
{
  "market":"US","session_id":"2024-11-04","calendar_id":"NYSE",
  "timezone":"America/New_York","session_date":"2024-11-04",
  "asof":"2024-11-04T12:00:00-05:00","slot":"midday",
  "rows":[{
    "ticker":"AAA","tier":"A","session_open":101,"prior_close":100,
    "price":102,"currency":"USD","price_basis":"raw","adjustment_id":"none",
    "usd_turnover":5000000
  }]
}
```

Save the files as `/tmp/open.json` and `/tmp/midday.json`, then run the command
above. Chat is written only to stdout; diagnostics go to stderr.

## Errors, integration, and rollback

Invalid schemas, immutable conflicts, duplicate identities, unsafe paths, and
corrupt state fail nonzero without replacing authoritative state. Correct source
data and rerun; quarantine corrupt state before retry. Adapters must supply
provenance for timestamps, opens, prior closes, and prices. The data-source
adapter must supply comparable adjusted `prior_close`, `actual_open`, and
`close` values on the same basis, including on split days. The provider is
responsible for supplying complete exchange calendars; this module cannot infer
omitted exchange sessions from arbitrary opaque session IDs and therefore
cannot verify market-calendar authenticity. CandidateRow `last` and `asof` are
not historical flag prices. Markdown is not parsed and no live backfill exists.

All five existing midday routines and the Nov 8 resume remain untouched and
paused. Manual integration is: run tests; run both synthetic commands; inspect
state/CSV/chat; select and record the gap threshold and quote/open ages; then
submit adapter output for separate activation approval. Rollback is to stop any
separately approved activation and remove only the staged directory. This change
does not activate anything.


## Supplemental outcome contract

- The persisted `params` object records the numeric `retention` and
  `max_quote_age_seconds` used for the run. These are run parameters, not
  immutable policy. Retention is the required gap retention threshold `r`, not
  a sampling metric. For a non-flat gap, `ratio=(X-prior_close)/(actual_open-prior_close)`:
  `ratio<=0` is reversed, `0<ratio<r` is faded, and `ratio>=r` is held. A flat
  gap is flat.
- `gap_cohort` and `flag_cohort` are separate classifications. `gap_cohort`
  describes the observation gap, while `flag_cohort` is `up`, `down`, `flat`,
  or `unknown` from the optional `flag_change_pct` field.
- A null catalyst is permitted only for `TECH_WATCH` flags and means that the
  catalyst is unavailable. No synthetic catalyst text is created, and null
  catalysts do not change the separate gap or flag cohorts.
- Market suffixes and display names are venue-aware. Taiwan `.TPEX` suffixes
  are appended only when the supplied venue or board says TPEx or an explicit
  display ticker is supplied; TWSE tickers remain bare canonical tickers.
  Tokyo uses `company_en` or the explicit text `English name unavailable`.
  Accepted market aliases are `asx`/`ASX`, `tokyo`/`JP`, `taiwan`/`TW`,
  `europe`/`EU`, and `us`/`US`.
- Every `.TW` ticker is not automatically a `.TPEX` ticker; the venue or board
  must support the suffix.
