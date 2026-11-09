# Simply Wall St new companies artifact contract

## Purpose

`swst-new-companies/` is the permanent, git-versioned weekly publish for the
Simply Wall St "new companies" screen. Minimax cloud routines consume this
artifact to discover companies without turning a Grok skill publish into a
Minimax cron.

The family uses schema `swst-new-companies-v1` and lives at
`swst-new-companies/` in `karizaco/minimax-cloud-outputs`.

## Producer

The producer is `grok-bot/simply-wall-st-new-companies`. It is not a Minimax
cron.

The canonical emitter is `scripts/emit_swst_new_companies.py`. It writes the
files in this contract to the repository and records provenance for the run.

## Layout

```text
swst-new-companies/
  latest.json
  latest.md
  latest.csv
  history.jsonl
  _index.json
  YYYY-MM-DD/
    _manifest.json
    brief.md
    companies.json
    fundamentals.csv
```

- `latest.json`, `latest.md`, and `latest.csv` represent the latest successful
  or explicitly degraded publish.
- `history.jsonl` is the full append-only ticker ledger copied from the Grok
  box. It contains one row per company-discovery, not one record per run.
- `_index.json` indexes published runs.
- `YYYY-MM-DD/` contains the immutable files for one run.
- Directory and file basenames must be Windows-safe. Do not use colons,
  backslashes, or other path-hostile characters.
- Put the date only in the directory name. Do not duplicate dates into nested
  basenames.

## `companies.json` schema

The top-level object has these fields:

| Field | Type | Rule |
|---|---|---|
| `_schema` | string | Must be `swst-new-companies-v1`. |
| `found_at` | string | Calendar date in `YYYY-MM-DD` format for the `Asia/Bangkok` session date. |
| `timezone` | string | Must be `Asia/Bangkok`. |
| `producer` | string | Must be `grok-bot/simply-wall-st-new-companies`. |
| `run_id` | string | Unique run identifier. |
| `status` | string | One of `ok`, `degraded`, or `error`. |
| `screeners` | array of objects | Screener results included in the run. |
| `counts` | object | Run counts with the keys defined below. |
| `repeats_skipped` | array | Records for companies excluded because they were previously published. |
| `notes` | array of strings | Run notes, warnings, and explanations for degraded output. |
| `companies` | array of objects | Company records described below. |

Each object in `screeners[]` has these fields:

| Field | Type | Rule |
|---|---|---|
| `id` | string | Screener identifier. |
| `region` | string | Screener region. |
| `found` | number | Companies found by the screener. |
| `new` | number | New companies found by the screener. |
| `url` | string | Source screener URL. |

The `counts` object has exactly these keys:

| Key | Type | Rule |
|---|---|---|
| `found` | number | Companies found in the run. |
| `new` | number | New companies included in the run. |
| `repeats_skipped` | number | Companies skipped because they were previously published. |
| `on_watchlist` | number | Companies matching the repository watchlist. |
| `by_region` | object | Counts broken down by region. |

Each object in `companies[]` has these fields:

| Field | Type | Rule |
|---|---|---|
| `region` | string | Market region or exchange geography. |
| `ticker` | string | Company ticker as reported by the source. |
| `tv_symbol` | string | TradingView symbol when known. |
| `company` | string | Company display name. |
| `screener` | string | Screener that found the company. |
| `screener_url` | string | Source screener URL. |
| `on_watchlist` | boolean | Whether the company matched the repository watchlist. |
| `what_they_do` | string | Short business description. |
| `mkt_cap_display` | string | Market capitalization as displayed by the source, including currency where available. |
| `mkt_cap_usd` | number or null | USD market capitalization only when a defensible USD value is known. |
| `valuation_kind` | string or null | Exactly one of `P/E`, `P/S`, `n/m`, or `null`. |
| `valuation_value` | number or null | Numeric multiple when `valuation_kind` is `P/E` or `P/S`; otherwise `null`. |
| `rev_growth_yoy_pct` | number or null | Year-over-year revenue growth percentage. |
| `net_margin_ttm` | number or null | Trailing-twelve-month net margin percentage. |
| `flags` | array of strings | Machine-readable qualifications or data-quality warnings. |
| `currency` | string | Currency for monetary values when known. |

Numeric rules are strict:

- Never invent a numeric value.
- Use `null` when a value is unavailable, ambiguous, stale, or not comparable.
- `mkt_cap_usd` must be `null` for a non-USD market capitalization unless a
  reliable, dated FX conversion is available. Do not silently treat a value in
  another currency as USD.
- `valuation_value` must be the numeric multiple when `valuation_kind` is `P/E`
  or `P/S`. It must be `null` when `valuation_kind` is `n/m` or `null`.
- Percentages are numeric percentage values, not fractions multiplied by 100
  again. State the unit in the field name or accompanying note.
- Missing facts are `null`; they are not zero, an empty string, or an inferred
  estimate.

## Consumer guidance

Consumers should prefer `swst-new-companies/latest.json`. The dated directory is
the immutable run artifact, but `latest.json` is the stable discovery point.

To find watchlist matches:

1. Read the ticker identifiers in `refs/watchlist.yaml`.
2. Intersect them with `companies[].tv_symbol` or, when appropriate, the bare
   `companies[].ticker`.
3. Match carefully. The watchlist currently uses bare US symbols, while
   TradingView symbols for some European and Japanese listings include a
   market prefix or exchange suffix. Do not strip prefixes or suffixes without
   validating the market and ticker.

A symbol match is a candidate, not proof of identity. Confirm the company and
market when the available fields do not make the match unambiguous.

## Manifest and index

Each dated directory contains `_manifest.json` with schema
`swst-new-companies-manifest-v1`. The manifest has these fields:

| Field | Type | Rule |
|---|---|---|
| `date` | string | Publish date in `YYYY-MM-DD` format. |
| `producer` | string | Must be `grok-bot/simply-wall-st-new-companies`. |
| `run_id` | string | Unique run identifier. |
| `canonical` | object | Canonical artifact references. |
| `canonical.brief` | string | Canonical brief artifact reference. |
| `canonical.machine` | string | Canonical machine-readable artifact reference. |
| `files` | array | Files included in the dated publish. |
| `counts` | object | Run counts. |
| `notes` | array of strings | Run notes and warnings. |

Checksums are optional and are not required by this contract.

The repository-level `_index.json` uses schema `swst-new-companies-index-v1`.
It lists published runs and points to their dated directories and manifest
files. It is an index, not a replacement for `latest.json` or `history.jsonl`.

## Provenance and status

The `found_at` date is the calendar date for the `Asia/Bangkok` session. It is
not an ISO timestamp with a timezone offset.

`status` has one of these values:

- `ok`: required source data was collected and the publish passed validation.
- `degraded`: the artifact is usable, but one or more screeners, fields, or
  required checks were incomplete.
- `error`: the publish did not produce a valid usable artifact.

Record partial failures and skipped repeats in `notes[]` and
`repeats_skipped[]`. Do not present a degraded run as complete.

## Non-goals

- This artifact is not trade advice.
- It does not replace `refs/watchlist.yaml`; watchlist membership is evaluated
  against that file and recorded in `on_watchlist`.
- The Grok skill publish hook is out of band. It may trigger this artifact
  publish, but it is not part of the artifact schema or delivery mechanism.
