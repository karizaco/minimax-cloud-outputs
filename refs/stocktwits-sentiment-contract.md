# StockTwits sentiment contract

## Purpose

This family publishes Grok Bot's weekday StockTwits crowd-sentiment scans for the Portfolio analyst agent. It is a dated, reproducible publication of two supplied lists: the approximately 19-name core list and the smart-daily general deep set selected from the standing watchlist.

## Producer

Producer: `grok-bot/stocktwits-sentiment-scan`. The Portfolio analyst agent runs scans on weekday mornings, approximately 08:30–08:50 Asia/Bangkok, using StockTwits MCP. This is not a Minimax cron. The emitter is local and does not fetch data.

The publication date is the Asia/Bangkok date represented by `ts_bkk`.

## Layout

The family root is `stocktwits-sentiment/`:

- `latest.json`, `latest.md`, and `latest.csv` are copies of the newest dated run.
- `history.jsonl` contains one line per date, list, and ticker.
- `_index.json` contains one run entry per date, with the newest run replacing a same-date rerun.
- `YYYY-MM-DD/` contains `_manifest.json`, `brief.md`, `sentiment.json`, and `sentiment.csv`.

The dated directory contains the canonical files. Filenames contain no clock time and use Windows-safe basenames.

## Canonical schema

`sentiment.json` has `_schema` equal to `stocktwits-sentiment-v1`, plus `date`, `timezone`, `producer`, `run_id`, `status`, `lists`, `counts`, and `rows`.

The `lists` object contains `core` and/or `general`. Core metadata includes `ts_bkk`, `path`, `quiet_ok`, `selected_count`, `trending_intersect`, and `notable_count`. General metadata includes `ts_bkk`, `path`, `mode`, `deep_n`, `trending_intersect`, `trending_board_top50`, `promoted_from_vol`, `dropped_from_prior_deep`, `notable_count`, and `material_tickers`.

Each row has:

| Field | Meaning |
|---|---|
| `list` | `core` or `general` |
| `ticker` | Ticker symbol without an exchange prefix |
| `tv_symbol` | TradingView symbol, when supplied or matched |
| `sent_label` | StockTwits sentiment label |
| `sent_score` | StockTwits sentiment score |
| `bull_pct`, `bear_pct` | Bullish and bearish post percentages |
| `vol_label`, `vol_score` | Current volume label and score |
| `vol_change_1d` | One-day volume change |
| `vol_1d_label`, `vol_1d_score` | One-day volume fields for core rows |
| `trending_rank` | StockTwits trending rank, or null |
| `watchers` | Watcher count, or null |
| `price`, `price_change_pct`, `price_time` | Price context and timestamp |
| `prior_sent_label`, `prior_sent_score` | Prior sentiment |
| `prior_vol_label`, `prior_vol_score` | Prior volume |
| `vs_prior_text` | Raw prior comparison text for general rows |
| `notable`, `notable_why` | Notable flags and core explanations |
| `material`, `material_reason` | General material flags |
| `themes`, `claims` | General post themes and claims |
| `on_watchlist` | Whether `tv_symbol` occurs in the watchlist |

Rows are sorted by list, descending sentiment score, and ticker. Unknown or unavailable values are null in JSON and blank in CSV.

## Labels

Sentiment labels are `EXTREMELY_BEARISH`, `BEARISH`, `NEUTRAL`, `BULLISH`, and `EXTREMELY_BULLISH`.

Volume labels are `EXTREMELY_LOW`, `LOW`, `NORMAL`, `HIGH`, and `EXTREMELY_HIGH`. Labels are printed by StockTwits and are not independently normalized by this emitter.

## Caveats

Crowd sentiment is not a signal of fact. Claims are unverified posts and should not be treated as confirmed information. Weekend runs carry Friday prices and related price context. Core themes are present only in the brief, not as row-level themes.

## Privacy

The account identity must never be published. The emitter removes `whoami`, `mcp_notes`, and `run_dir` from published data and removes account-bearing `whoami` segments from supplied summary markdown. Removed identity segments are counted in manifest notes. Box paths are not published.

## Consumers

Minimax #26 pre-market brief and #23 post-market may show sentiment for watchlist names from `latest.json`. Consumers are read-only and must not modify the family.

## Freshness

The latest date in the family must equal the session date being briefed. A stale or absent daily run is a degraded path, not a reason to invent data.

## Regeneration

Run:

`python3 scripts/emit_stocktwits_sentiment.py --date YYYY-MM-DD --core-json PATH --core-summary-md PATH --general-json PATH --general-summary-md PATH --watchlist refs/watchlist.yaml --out-dir stocktwits-sentiment`

Either list pair may be omitted. Use `--allow-stale` only when explicitly accepting a degraded stale input, and use `--generated-at` to pin deterministic output.
