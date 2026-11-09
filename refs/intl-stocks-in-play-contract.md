---
title: International stocks-in-play artifact contract
producer: grok-bot/fundamental-stocks-in-play
contract: intl-stocks-in-play-v1
---

# Purpose

Fundamental's regional stocks-in-play routines publish machine-readable candidate
sets for Australia, Europe, Tokyo, and Taiwan. The contract covers four dated
families and their briefs, candidate JSON/CSV, history, index, and manifest.
Market-specific currency and units remain in the raw strings printed by the
source digest.

# Producers

The Grok Bot agent "Fundamental" produces the `asx`, `europe`, `tokyo`, and
`taiwan` stocks-in-play families. Producer identities use
`grok-bot/<market>-stocks-in-play`.

The emitter is `scripts/emit_intl_stocks_in_play.py`. These families are not
Minimax cron outputs. Supported slots are `open`, `midday`, `preclose`, and
`close`; the available routine may publish only a subset of those slots.

# Layout

Each family root is `<market>-stocks-in-play/` and contains:

- `latest.json`: candidates JSON from the newest dated run.
- `latest.md`: brief from the newest dated run.
- `latest.csv`: candidates CSV from the newest dated run.
- `history.jsonl`: append-only candidate observations.
- `_index.json`: one entry per date, with slot counts.
- `YYYY-MM-DD/`: one canonical brief and candidate files for each published slot.

A dated directory contains `_manifest.json`, `<slot>.md`,
`<slot>-candidates.json`, and `<slot>-candidates.csv`. The date appears only
in the dated directory name. Symbols and source paths may occur in file
contents, never in filenames.

# Invocation

Generate one market/slot/date combination with:

```sh
python3 scripts/emit_intl_stocks_in_play.py --market asx --date 2026-11-09 --slot open --digest-md /path/to/digest.md
```

The equivalent market values are `europe`, `tokyo`, and `taiwan`. Use
`--watchlist refs/watchlist.yaml` to override the watchlist, `--repo-root .` to
set the repository root, and `--generated-at` to pin generation time. Use
`--dry-run` to print planned paths and counts without writing.

Running another slot for the same date adds that slot to the dated directory
and rewrites the manifest. The emitter never fetches anything from the network.

# Candidates JSON schema

`<slot>-candidates.json` uses `_schema: intl-stocks-in-play-v1`.

| Field | Meaning |
|---|---|
| `_schema` | `intl-stocks-in-play-v1` |
| `market` | `asx`, `europe`, `tokyo`, or `taiwan` |
| `date` | Published session date |
| `slot` | `open`, `midday`, `preclose`, or `close` |
| `timezone` | `Asia/Bangkok` |
| `producer` | `grok-bot/<market>-stocks-in-play` |
| `run_id` | `<date>T<slot>` |
| `status` | `ok` or `degraded` |
| `source_digest` | Source box path, stored as plain text |
| `digest_title` | Digest H1 text |
| `counts` | Candidate, tier, watchlist, and unparsed counts |
| `candidates` | Ordered candidate objects |

Each candidate contains `rank`, `tier`, `ticker`, `tv_symbol`, `company`,
`venue`, `segment`, `price_raw`, `chg_pct`, `gap_pct`, `rvol`,
`turnover_raw`, `mcap_raw`, `catalyst`, `flags`, `on_watchlist`, `parse`,
`section`, `raw`, and `cells`.

Ranks are one-based and ordered by tier: A, SOFT_A, TECH_WATCH, B, C.
File order is preserved within each tier. Unknown values are null in JSON.

# CSV columns

`<slot>-candidates.csv` has these columns in order:

```text
rank,tier,ticker,tv_symbol,company,venue,segment,price_raw,chg_pct,gap_pct,rvol,turnover_raw,mcap_raw,catalyst,flags,on_watchlist,parse,section
```

`flags` is semicolon-delimited. Boolean values use lowercase `true` or
`false`; null values are blank.

# Parse rules

Only `##` sections with recognized tier headings are candidate sections.
Sections concerning near misses, annexes, overnight material, skips, source
health, FX, indices, other PS, Poland, changes, rechecks, and exclusions are
not candidate sections.

Markdown table headers are matched case-insensitively. Supported fields are
ticker/code/symbol, company, venue, segment, price/last/price ¥,
chg/chg%/move, gap%, rvol/relvol, turnover*/€vt, mcap, and
why/catalyst*/note. Every original table cell is retained in `cells`.

Bullet rows and plain pipe-separated rows are list-shaped. List-shaped rows
retain the complete item in `raw` and have a null `catalyst`; consumers must
read the digest for catalyst details. A missing ticker makes the item
unparsed. Tokyo mixed B/C rows strip their B: or C: prefix and split on
semicolons.

The first signed percentage becomes `chg_pct`. Gap is read from gap% or a
parenthesized gap percentage in the change text. RVol is the first number
before `×` or `x`. The emitter never derives values absent from the digest.

`tv_symbol` mapping is:

| Market | Mapping |
|---|---|
| ASX | `ASX:<ticker>` |
| Tokyo | `TSE:<ticker>` |
| Taiwan TWSE | `TWSE:<ticker>` |
| Taiwan TPEX | `TPEX:<ticker>` |
| Europe | Venue-specific TradingView symbol |

European venue mappings are Borsa Italiana to `MIL`, Xetra to `XETR`, LSE and
LSE (AIM) to `LSE`, the named Euronext markets to `EURONEXT`, SIX to `SIX`,
Oslo to `OSL`, Helsinki to `OMXHEX`, Stockholm and Nasdaq Stockholm to
`OMXSTO`, Copenhagen to `OMXCOP`, Warsaw and GPW to `GPW`, Madrid and BME to
`BME`, and Vienna to `VIE`.

`on_watchlist` is true when `tv_symbol` occurs in any `tv_symbol` value in
`refs/watchlist.yaml`. If the watchlist has no `tv_symbol` keys, the field is
null and the manifest records that deviation.

# Briefs and provenance

Each `<slot>.md` begins with YAML front matter, followed by a provenance line,
a deviations line, and the source digest. The digest is otherwise verbatim.
Backticked box-local file paths that do not exist in the repository are
written without backticks and counted in the manifest.

`_manifest.json` lists every file in the dated directory. The manifest names
all briefs as canonical, all candidate JSON and CSV files as machine output,
records per-slot counts, and lists degradation notes.

# History and index

`history.jsonl` contains one object per date, slot, tier, and ticker:
`date`, `slot`, `tier`, `ticker`, `tv_symbol`, and `chg_pct`. Re-running a
slot replaces that slot's history records rather than duplicating them.

`_index.json` has one run per date. Its `slots` array records each published
slot, status, and counts. Dates and slots are sorted.

# Relationship to us-stocks-in-play

This contract uses the same tier vocabulary—A, SOFT_A, TECH_WATCH, B, and C—
and slot names as `us-stocks-in-play/logs.jsonl`. Unlike that family, these
outputs use dated directories, retain per-market currency in raw strings, and
do not normalize pace or RVol. RVol is not time-of-day adjusted unless the
digest explicitly says so.

# Consumers

Minimax `#02 asia-pre-market` and `#05 international-eod` MAY join these
artifacts on `tv_symbol`. They are read-only consumers and must not mutate
published files. Consumers should inspect `parse`, `raw`, and `cells` when
catalyst or source detail is required.

# Freshness

Freshness is determined by the dated run and slot, not by file modification
time. `latest.json`, `latest.md`, and `latest.csv` select the greatest date,
then slot order `open`, `midday`, `preclose`, `close`. A missing or incomplete
source section should be treated as degraded rather than backfilled.

# Regeneration

```sh
python3 scripts/emit_intl_stocks_in_play.py --market asx --date 2026-11-09 --slot open --digest-md /path/to/asx.md
python3 scripts/emit_intl_stocks_in_play.py --market europe --date 2026-11-09 --slot open --digest-md /path/to/europe.md
python3 scripts/emit_intl_stocks_in_play.py --market tokyo --date 2026-11-09 --slot open --digest-md /path/to/tokyo.md
python3 scripts/emit_intl_stocks_in_play.py --market taiwan --date 2026-11-09 --slot open --digest-md /path/to/taiwan.md
```

Use the corresponding source digest and slot for every regeneration. The
general artifact rules are in `refs/artifact-contract.md`, and watchlist
membership is read from `refs/watchlist.yaml`.
