# Earnings-calendar contract

## Purpose

The earnings-calendar family publishes the Grok Bot weekly earnings calendar for
the following earnings week. It preserves the box CSV as the canonical tabular
artifact and provides a normalized JSON representation for downstream consumers.

## Producer

Producer: `grok-bot/weekly-earnings-calendar`

The producer runs on Sundays at approximately 15:30 Asia/Bangkok. It is not a
Minimax cron job. The emitter is `scripts/emit_earnings_calendar.py`.

## Layout

The family is rooted at `earnings-calendar/`:

```text
earnings-calendar/
  latest.json
  latest.md
  latest.csv
  history.jsonl
  _index.json
  YYYY-MM-DD/
    _manifest.json
    brief.md
    calendar.csv
    calendar.json
```

The shared cache is `refs/earnings-next-dates.json`.

Each dated directory is the run date. The calendar window is the following week.
The `latest.*` files are copies of the newest dated run's canonical artifacts.
The dated directory contains the manifest, brief, JSON, and CSV only.

## calendar.json

`calendar.json` has the following top-level keys:

| Key | Meaning |
|---|---|
| `_schema` | Contract schema identifier, `earnings-calendar-v1`. |
| `run_date` | Date on which the calendar run was produced. |
| `timezone` | Calendar timezone, `Asia/Bangkok`. |
| `producer` | Producer identity. |
| `run_id` | Stable run identifier. |
| `status` | `ok`, `degraded`, or `error`. |
| `window` | Object with `from` and `to` session dates. |
| `universe_note` | Universe description from the box markdown. |
| `counts` | Row and confirmation counts. |
| `needs_attention` | Attention note from the source calendar. |
| `rows` | Normalized calendar rows. |

Each row has the following keys:

| Key | Meaning |
|---|---|
| `date` | Earnings session date. |
| `ticker` | Company ticker. |
| `exchange` | Exchange identifier. |
| `symbol` | Composite symbol, such as `NASDAQ:AAPL`. |
| `timing` | `BMO`, `AMC`, or `unknown`. |
| `core` | Whether the company is in the core universe. |
| `confirmed` | TradingView confirmation flag. |
| `sa_confirmed` | StockAnalysis confirmation value. |
| `tv_date` | TradingView source date. |
| `eps_est` | EPS estimate. |
| `eps_growth_est_pct` | EPS growth estimate percentage. |
| `eps_growth_flag` | Flag for non-meaningful EPS growth. |
| `rev_est_display` | Revenue estimate display string. |
| `rev_growth_est_pct` | Revenue growth estimate percentage. |
| `rev_growth_flag` | Flag for non-meaningful revenue growth. |
| `eps_forecast_raw` | Raw EPS forecast. |
| `eps_last_raw` | Raw prior EPS value. |
| `rev_forecast_raw` | Raw revenue forecast. |
| `rev_last_raw` | Raw prior revenue value. |
| `currency` | Reporting currency. |
| `source` | Calendar source. |
| `notes` | Row-specific notes. |

Unknown or empty numeric values are `null` in JSON.

## CSV, history, and cache

`calendar.csv` is the box CSV verbatim, except that CRLF and CR line endings are
normalised to LF. The same normalized bytes are used for `latest.csv`.

Each `history.jsonl` line has these keys:

`run_date`, `symbol`, `date`, `timing`, `confirmed`, and `core`.

The history natural key is the run date plus symbol, so rerunning the same date
replaces that date's entries rather than duplicating them.

`refs/earnings-next-dates.json` is the box cache verbatim, augmented with
`_schema`, `_published_at`, `_producer`, and `_source`.

The cache `symbols[]` entries contain:

- `next_date`, `timing`, `forecasts`, `source`, and `fetched_at`.
- `core` and `sa_confirmed` flags.
- `unconfirmed` and `unconfirmed_reason` when the listing is not confirmed.
- `stale`, `also_listed`, `no_earnings`, and `instrument_type` or `type`.
- `typespecs` where present.

`merged_listings` maps a secondary listing to its primary listing. The
`carry_core` value indicates whether the core flag is carried to the primary.
A `rename` value records a symbol rename.

`no_tv_data` is a consecutive-week counter. A value of three or more weeks
places the symbol in `needs_attention`.

## Consumers

The Minimax #19 earnings reminder and #22 weekly preview may read
`earnings-calendar/latest.json` to resolve watchlist names. This is optional.
The Grok weekly transcript watch reads the shared cache directly.

## Freshness

Consumers should check that `window.to` is at least the current date. The
cache is current as of its `run` value.

## Listing rules

One company is represented by one row. When a secondary listing is known,
normalize it to the primary listing; for example, `TRADEGATE:EI5` becomes
`NYSE:TK`.

## Regeneration

```bash
python scripts/emit_earnings_calendar.py \
  --date YYYY-MM-DD \
  --calendar-md /path/to/calendar.md \
  --calendar-csv /path/to/calendar.csv \
  --cache-json /path/to/next-dates-cache.json \
  --repo-root /path/to/repository
```

Use `--generated-at` to pin the build timestamp and `--dry-run` to inspect the
planned files and counts without writing them.

## Deviations from other families

The CSV keeps the box column names rather than using the JSON row names. The
dated directory is the run date, while the calendar window covers the following
week.
