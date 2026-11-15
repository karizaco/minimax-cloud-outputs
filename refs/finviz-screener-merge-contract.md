# Finviz screener merge artifact contract

## Purpose

`finviz-screener-merge/` is the permanent, git-versioned weekly publish for
Grok Bot's merged Finviz multi-screener output. Minimax cloud routines consume
this artifact without turning a Grok skill publish into a Minimax cron.

The family uses schema `finviz-screener-merge-v1` and lives at
`finviz-screener-merge/` in `karizaco/minimax-cloud-outputs`.

## Producer

The producer is `grok-bot/finviz-screener-merge`. It is not a Minimax cron.

The canonical emitter is `scripts/emit_finviz_screener_merge.py`. It publishes
the files in this contract and records provenance for the run.

## Layout

```text
finviz-screener-merge/
  latest.json
  latest.md
  latest.csv
  history.jsonl
  _index.json
  YYYY-MM-DD/
    _manifest.json
    brief.md
    merge.json
    tickers.csv
```

- `latest.json`, `latest.md`, and `latest.csv` represent the newest dated
  publish.
- `history.jsonl` contains one record per dated ticker observation.
- `_index.json` contains one entry per published date.
- `YYYY-MM-DD/` contains the immutable files for one weekly run.
- Directory and file basenames must be Windows-safe.
- Put the date only in the directory name, never in a nested basename.

## `merge.json` schema

The top-level object has these fields:

| Field | Type | Rule |
|---|---|---|
| `_schema` | string | Must be `finviz-screener-merge-v1`. |
| `found_at` | string | Weekly session date in `YYYY-MM-DD` format. |
| `timezone` | string | Must be `Asia/Bangkok`. |
| `producer` | string | Must be `grok-bot/finviz-screener-merge`. |
| `run_id` | string | Must be `<date>Tweekly`. |
| `status` | string | One of `ok`, `degraded`, or `error`. |
| `data_as_of` | string or null | Market-data date stated by the source. |
| `screeners` | array | Screener ledger, in source-file order. |
| `counts` | object | Run counts defined below. |
| `full_overlap` | array | Tickers present in every unique screener. |
| `tickers` | array | Unique ticker records defined below. |
| `stocktwits_note` | string | StockTwits section text. |
| `coverage_notes` | array | Coverage bullets with Markdown removed. |

Each object in `screeners[]` has these fields:

| Field | Type | Rule |
|---|---|---|
| `name` | string | Screener display name. |
| `url` | string or null | URL from the standing bookmark file. |
| `unique` | boolean | Whether this is the first occurrence of its URL. |
| `duplicate_of` | string or null | First screener with the identical URL. |
| `tickers_page1` | number or null | Number of page-one tickers. |
| `finviz_total` | number or null | Finviz-reported total. |
| `notes` | string | Per-screener notes from the source. |
| `tickers` | array | Page-one ticker symbols. |

The `counts` object has exactly these keys:

| Key | Type | Rule |
|---|---|---|
| `screeners` | number | Named screeners in the source. |
| `unique_screeners` | number | Unique URL sets. |
| `union` | number | Unique tickers across unique screeners. |
| `full_overlap` | number | Tickers in every unique screener. |
| `multi_hit_3plus` | number | Tickers with at least three unique hits. |
| `multi_hit_2plus` | number | Tickers with at least two unique hits. |
| `new_this_week` | number | Tickers absent from the previous seeded run. |
| `on_watchlist` | number | Tickers matching eligible watchlist symbols. |

Each object in `tickers[]` has these fields:

| Field | Type | Rule |
|---|---|---|
| `ticker` | string | US ticker symbol. |
| `hits` | number | Number of unique screeners containing the ticker. |
| `screeners` | array | Unique screener names in source-file order. |
| `first_seen` | string | Earliest observation date, including this run. |
| `new_this_week` | boolean or null | Null when no previous seeded run exists. |
| `on_watchlist` | boolean or null | Null when the watchlist has no `tv_symbol` keys. |

Rows are sorted by descending `hits`, then ascending `ticker`. Missing numeric
or boolean facts are null. Values are never inferred.

## History semantics

`history.jsonl` contains one JSON object per `(found_at, ticker)` pair:

| Field | Type | Rule |
|---|---|---|
| `found_at` | string | Observation date in `YYYY-MM-DD` format. |
| `ticker` | string | Observed ticker. |
| `hits` | number | Unique-screener hits for that observation. |
| `screeners` | array | Unique screeners containing the ticker. |

Older `--seed-md` files contribute dated observations and establish
`first_seen`. Re-running the same date replaces that date's dated artifacts and
history observations; it must not duplicate history rows. A ticker is new when
it was absent from the immediately previous seeded run. Newness is null if no
previous seeded run was supplied.

## Watchlist matching

Finviz symbols are US symbols. A ticker is on the watchlist when it equals the
symbol part of a `tv_symbol` in `refs/watchlist.yaml` whose exchange is NYSE,
NASDAQ, AMEX, CBOE, or OTC. If the YAML has no `tv_symbol` keys, all
`on_watchlist` values are null rather than false.

## Consumer guidance

Consumers should prefer `finviz-screener-merge/latest.json`. Use
`latest.csv` for a compact ticker table and `latest.md` for human-readable
coverage and provenance. Read `_index.json` to enumerate weekly runs.

Minimax job #22, weekly preview, and Minimax job #09, daily sweep, MAY
intersect `tickers[].ticker` with their own boards. This access is read-only.
They must not modify the family, reinterpret missing values, or treat first-page
membership as a complete Finviz result.

Freshness is first page only. Data is expected to reflect the prior Friday
close; consult `data_as_of` and the coverage notes for the exact statement.

## Regeneration command

```bash
python3 scripts/emit_finviz_screener_merge.py \
  --date YYYY-MM-DD \
  --merge-md PATH_TO_MERGE.md \
  --screeners-md PATH_TO_SCREENERS.md \
  --seed-md PATH_TO_OLDER_RUN.md \
  --watchlist refs/watchlist.yaml \
  --out-dir finviz-screener-merge
```

`--seed-md` is repeatable. Use `--generated-at` to pin timestamps in tests and
`--dry-run` to inspect the planned files and counts without writing.
