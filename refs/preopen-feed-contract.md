# Pre-open catalyst feed — contract

The append-only catalyst tape that lets the 15:50 ET digest explain **why** a stock moved and
**when** the news broke, not just where it ended up.

## Location

```
karizaco/minimax-cloud-outputs  →  branch main  →  preopen-feed/{YYYY-MM-DD}-{HHMM}.jsonl
```

One file per checkpoint (0830 / 0920 / 0950 ET). Each checkpoint owns its own file, so two
captures can never clobber each other and the consumer merges them oldest-first.

## Record schema

One JSON object per line.

```json
{
  "ts": "2026-11-03T09:15:23-04:00",
  "src": "grok",
  "ticker": "BRZE",
  "name": "Braze",
  "pct": 51.2,
  "price": 45.40,
  "cat": "acquisition",
  "why": "Salesforce to acquire for $47.50/sh cash",
  "ref": "https://…",
  "conf": "high"
}
```

| Field | Type | Notes |
|---|---|---|
| `ts` | string | ISO 8601 with the ET offset. The consumer sorts on it. |
| `src` | `tv` \| `pipeworx` | `tv` = price from `top_movers` (ground truth). `pipeworx` = the row also carries a grounded catalyst. |
| `ticker` | string | Uppercase, required. Rows without one are dropped. |
| `name` | string \| null | Company name, optional. |
| `pct` | number \| null | Percent move. **Always from the scanner**, never from Grok. |
| `price` | number \| null | Price. Same rule. |
| `cat` | vocabulary | `acquisition, merger, earnings, guidance, fda, trial, offering, halt, downgrade, guidance-cut, spin, dividend, other` |
| `why` | string \| null | One clause, ≤200 chars, the specific catalyst. |
| `ref` | string \| null | Source URL. A record without one is `conf: low`. |
| `conf` | `high` \| `medium` \| `low` \| `unverified` | `unverified` ⇒ the feed's `pct` disagreed with `top_movers` by >2pp. |
| `trending_ts` | string \| null | When the narrative source stamped the reason. |
| `trending_score` | number \| null | Retail-attention score for the name. |
| `volume`, `exchange` | number \| string \| null | From the ground-truth movers scan. |

Unknown `cat` values are coerced to `other` on read.

## Who writes what

| Writer | Writes | When |
|---|---|---|
| cron `92a` (platform) | `preopen-feed/{date}-0830.jsonl` | 08:30 ET, Mon–Fri |
| cron `92b` (platform) | `preopen-feed/{date}-0950.jsonl` | 09:50 ET, Mon–Fri |
| n8n workflow (optional) | `preopen-feed/{date}-{HHMM}.jsonl` | your cadence |
| cron `17` (`us-stocks-in-play`) | **reads only** | 15:50 ET |

## Who reads it

`cloud-prompts/_shared/preopen_feed.py` in `karizaco/maxhermes-migration`.

```bash
python3 /workspace/preopen_feed.py feed       --date 2026-11-03   # inspect the feed
python3 /workspace/preopen_feed.py merge      --date 2026-11-03 --symbols BRZE,CCI
python3 /workspace/preopen_feed.py provenance --date 2026-11-03 --symbols BRZE,CCI
python3 /workspace/preopen_feed.py selftest                        # 4 known sessions, must print 4 PASS
```

`provenance` and `merge` work with **no feed at all** — the path and the verdict come from
Yahoo's 5-minute bars. The feed only adds the reason and the timestamp.

## The verdict

| verdict | meaning | treatment |
|---|---|---|
| `reverse` | the opening move flipped sign | strongest in-play signal; the gap and the tape disagree |
| `faded` | the opening move was substantially given back | in play, but the open buyer is gone |
| `held` | the move is largely intact | a trend, not a squeeze-and-fade |
| `no_move` | the open was inside the noise band | no gap to read; judge on the catalyst alone |
| `unknown` | the bars could not be read | say so; never guess |

Reference sessions (the selftest fixtures):

| Session | Open | Now | Verdict |
|---|---|---|---|
| XLAB 2026-10-15 | -5.79% | +48.51% | `reverse` |
| CCI 2026-10-23 | +15.46% | +8.70% | `held` |
| SKYD 2026-10-14 | -18.55% | -25.73% | `held` |
| BRZE 2026-10-23 | -0.02% | +0.04% | `no_move` (merger arb) |

## Ground rules

1. **The feed is optional.** Its absence is `absent`, never a reason to abort a digest.
2. **Prices are never taken from the narrative source.** `top_movers` is the source of truth; a
   >2pp disagreement becomes `unverified`. A narrative answer that merely restates the price
   move, or whose source was a filing index rather than news, is dropped rather than published.
3. **No key ⇒ no tape.** If `PIPEWORX_API_KEY` is unset the capture writes nothing rather than
   an empty file that would read as "no news".

   **The xAI path is retired.** The xAI chat API deprecated live search
   (`search_parameters` → HTTP 410 "Live search is deprecated") across every model that
   supported it, including `grok-4.3`; the replacement Agent Tools API returns 403
   ("agents endpoint is not enabled for this API key") on ordinary keys. The Pipeworx gateway
   supplies the live catalyst layer instead — `trending_symbols` for the reason and the
   timestamp, `top_movers` for the price, `ask_pipeworx_grounded` for a per-name catalyst with
   evidence, URL and confidence.
4. **Append only.** Never rewrite an earlier checkpoint's rows.
5. **No backfilling.** A missing checkpoint is normal.
6. **A liquidity floor applies to the movers scan.** Price ≥ $1 and session $ volume ≥ $1m.
   Without it the scan returns 600+ rows dominated by sub-$1 shells that genuinely moved
   hundreds of percent (measured 2026-11-06: NEXR +742% at $2.01, RCT +68% at $0.0505,
   SITC -83% at $0.61) — real numbers, unusable universe.
7. **The scanner's `premarket_*` columns are LIVE ONLY** — blank for a past date. The 09:30 /
   10:00 / 12:00 path from 5-minute bars is historical and always valid.
