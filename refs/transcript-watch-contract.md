# Weekly transcript watch contract

## Purpose

The weekly transcript watch is a Sunday Content analyzer publication for Grok Bot. It records new StockAnalysis earnings-call, conference, and material-update transcripts for watchlist companies, publishes the weekly digest, and publishes only short auto-briefs in the public repository.

A run covers one lookback window and is dated in Asia/Bangkok. A transcript is identified by its StockAnalysis URL within a run.

## Producer

Producer: `grok-bot/weekly-transcript-watch`

- Role: Content analyzer, Sundays.
- Sources: StockAnalysis transcript pages and the shared earnings cache refs/earnings-next-dates.json (added by the watchlist/earnings-calendar PR).
- Model: Minimax writes the long summaries on the Grok box. Its model identifier is copied into each short brief when a metadata file is available.
- Public output: the digest, a machine-readable transcript index, and short briefs only.

## Public-repository rule

No transcript text and no long summary may be published in this repository. A short brief may contain its YAML front matter, the box summary H1, and only the box summary TL;DR bullets, capped at the box summary's stated maximum. It ends with the StockAnalysis source URL and a notice that the full summary remains on the Grok box.

If a box summary has no TL;DR section, publish only its H1 and source line and record the omission as a manifest note. Never copy any other section from the box summary.

## Layout

```text
transcript-watch/
  latest.json
  latest.md
  latest.csv
  history.jsonl
  _index.json
  YYYY-MM-DD/
    _manifest.json
    brief.md
    transcripts.json
    transcripts.csv
    summary-<slug>.md
```

The dated directory is the run date in Asia/Bangkok. `latest.json`, `latest.md`, and `latest.csv` are copies of the newest dated run's canonical artifacts. The basename `summary-<slug>.md` is Windows-safe and contains no date.

## Schemas

### transcripts.json

`_schema` is `transcript-watch-v1`. The object contains:

| Field | Meaning |
|---|---|
| `run_date` | Bangkok run date |
| `timezone` | `Asia/Bangkok` |
| `producer` | Producer identity |
| `run_id` | `<run_date>Tweekly` |
| `status` | `ok`, `degraded`, or `error` |
| `lookback` | Inclusive `[from, to]` dates |
| `sweep` | Copy of the last-run sweep object |
| `tv_calls` | TradingView calls used by the run |
| `counts` | New transcript, brief, core, tag, and watchlist counts |
| `transcripts` | Ordered transcript records |
| `core_status` | Copy of the last-run core status |
| `notes` | Copy of the last-run notes |

Each transcript record contains `rank`, `ticker`, `symbol`, `date`, `title`, `tag`, `url`, `core`, `briefed`, `brief_file`, `tldr`, and `on_watchlist`. Auto-briefed records appear first in `auto_briefed` order; other records follow by date and ticker. `brief_file` is null when no brief was emitted. `tldr` is empty for non-briefed records.

### transcripts.csv

Columns are `rank,ticker,date,title,tag,core,briefed,brief_file,url,on_watchlist`. Unknown values are blank. Booleans use `true` and `false`.

### history.jsonl

Each line is one JSON object with `run_date`, `ticker`, `date`, `title`, `tag`, `core`, `briefed`, and `url`. There is one line per `(run_date, url)`. Re-running a date is idempotent for that date.

### _index.json

`_schema` is `transcript-watch-index-v1`. `runs` contains one entry per date, sorted by date. Each entry contains `date`, `run_id`, `status`, `counts`, and the relative dated-directory `path`. A rerun replaces the entry for that date.

### _manifest.json

The manifest identifies the producer, run, provenance, canonical files, every published dated-directory file, counts, and degradation notes. `_manifest.json` lists itself with role `provenance`.

## Brief and digest rules

`brief.md` has YAML front matter, one provenance line, and a Deviations / degraded paths section near the top. The copied weekly digest keeps its H1. Box-summary links become relative `summary-<slug>.md` links when a brief was published; otherwise the link is removed while its text is retained. HTTPS links remain unchanged. File-like backticked tokens are unbackticked unless they identify an existing repository file.

The digest must not expose the contents of a long box summary. Only the short summary files described above may contain TL;DR bullets.

## Consumers

Minimax #22's weekly preview may cite TL;DR bullets for watchlist names. Any routine can de-duplicate previously seen transcripts by URL using `history.jsonl`.

Consumers should use `transcripts.json` as the canonical index, read `brief_file` before citing a TL;DR, and treat `on_watchlist` as the emitter's membership signal. Unknown values remain null in JSON or blank in CSV.

## Freshness

A new family is produced after the Sunday StockAnalysis sweep. The run date and transcript dates use Bangkok calendar dates. The lookback records the inclusive covered session. A rerun with the same date replaces that date's dated artifacts and index entry.

## Regeneration

```bash
python3 scripts/emit_transcript_watch.py --date YYYY-MM-DD --digest-md PATH --last-run-json PATH --summaries-dir PATH --watchlist refs/watchlist.yaml --out-dir transcript-watch
```

Use `--generated-at` to pin the build timestamp and `--dry-run` to print the planned files and counts without writing. The emitter refuses a last-run JSON file whose `run_date_bkk` differs from `--date`.
