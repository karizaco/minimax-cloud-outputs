# Standing watchlist contract

## Purpose

`refs/watchlist.yaml` publishes Hypnotoad’s real standing TradingView watchlist for the routine fleet. It is generated from TradingView Positions, a maintained core-symbol list, and the earnings next-dates cache. The published file is short where the legacy cron consumers require a US-tradable list, while preserving the complete primary-listing inventory in additive sections.

## Producer

The producer is `grok-bot/watchlist-sync`, implemented by `scripts/emit_watchlist.py`. The emitter is regenerated weekly before the Sunday earnings calendar; the box keeps the inputs. The same inputs and date produce byte-identical output.

## Consumers

The four Minimax crons read the top-level `watchlist` list only:

- #16 unusual-options-flow-daily: Pass A leg, using the watchlist’s option chains.
- #19 earnings-reminder-daily: “Your watchlist” section.
- #23 agentic-post-market-brief: “Watchlist EOD review” section.
- #26 agentic-pre-market-brief: the brief’s watchlist section.

Grok families such as swst-new-companies and finviz-screener-merge intersect against `extended[].tv_symbol`. The `watchlist_intl` and `extended` sections are additive and are not required to be read by the four legacy crons.

## Schema

| Key | Type | Rules |
|---|---|---|
| `version` | integer | `2` for this schema. |
| `updated` | string | Publication date in `YYYY-MM-DD` form. |
| `source` | string | Positions identifier and fetch time, plus the core list and cache merge source. |
| `generated_by` | string | `scripts/emit_watchlist.py`. |
| `counts` | object | Counts for `watchlist`, `watchlist_intl`, `extended`, `positions_raw`, and `collapsed_secondaries`. |
| `watchlist` | list of mappings | Core names with a NYSE, NASDAQ, AMEX, or CBOE line. `ticker` is the bare US symbol; `earnings_flag` is true for every row. `tv_symbol`, `us_symbol`, `region`, `tags`, and `note` are additive metadata. |
| `watchlist_intl` | list of mappings | Core names without a US exchange line. Contains `ticker`, `tv_symbol`, `region`, `tags`, `also_listed`, and optionally `note`. OTC is not considered a US exchange for this key. |
| `extended` | list of mappings | Every primary in Positions, including core names, one row per company, sorted by `tv_symbol`. Fields are `tv_symbol`, `ticker`, `exchange`, `region`, `core`, `instrument_type`, `also_listed`, and optional `note`. `also_listed` contains collapsed secondaries, sorted. |

Unknown keys are ignored so the file can grow without a routine change.

## Back compatibility

The v1 `watchlist` keys remain unchanged. The new keys are additive, and the `version` value is bumped to 2 because the crons ignore unknown keys. A consumer that hard-checks `version == 1` must be updated to accept version 2; consumers that only read the `watchlist` list can continue unchanged.

## Primary-listing rule

Every Positions symbol and core symbol is mapped through the cache’s `merged_listings` chains, with a maximum of five hops, to its primary listing. A rename mapping such as `NASDAQ:DOMO -> NASDAQ:HUCK` maps the old symbol to the new one. Secondary venues such as TRADEGATE, GETTEX, SWB, and LS never become separate rows. For example, `TRADEGATE:EI5` is collapsed onto `NYSE:TK`, and the extended inventory contains one `NYSE:TK` row.

Core status is the union of the core text file mapped to primaries, cache `symbols[primary].core == true`, and merged secondary entries whose `carry_core` is true. A core primary not present in Positions is retained in `extended` with the note “core list only (not in Positions)”.

For a core primary outside the US, a NYSE, NASDAQ, AMEX, or CBOE listing among the primary or collapsed secondaries places it in `watchlist`; otherwise it is placed in `watchlist_intl`. Regions derive from the primary exchange prefix. Unknown prefixes produce `other` and an emitter warning.

## Regeneration command

Run the emitter with the local box inputs, for example:

```text
python3 scripts/emit_watchlist.py --positions-json /path/to/positions.json --core-txt /path/to/core.txt --cache-json /path/to/earnings-cache.json --out refs/watchlist.yaml --date YYYY-MM-DD --csv-out /path/to/watchlist-extended.csv
```

The YAML and optional CSV are written only after all inputs have been parsed and the complete output has been built in memory.

## Failure rules

The emitter exits with status 2 and does not write output when the Positions export has fewer than 20 symbols, when a required input is missing or garbled, or when the resulting `watchlist` would be empty. It never publishes an empty list, because that would turn an honest “no watchlist today” into an empty section that reads as a bug. The emitter never fetches anything from the network.
