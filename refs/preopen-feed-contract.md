# Pre-open catalyst feed — contract

The append-only catalyst tape that lets the 15:50 ET digest explain **why** a stock moved and
**when** the news broke, not just where it ended up.

## Location

```
karizaco/minimax-cloud-outputs  →  branch main  →  preopen-feed/{YYYY-MM-DD}-{HHMM}.jsonl
```

One file per checkpoint (0830 / 0920 / 0950 ET). Each checkpoint owns its own file, so two
captures can never clobber each other and the consumer merges them oldest-first.

## The companion files

Each checkpoint writes up to THREE files, all named for the same `{YYYY-MM-DD}-{HHMM}` slot:

| File | What it is | Written when |
|---|---|---|
| `{date}-{HHMM}.jsonl` | the tape — the machine contract below | every successful checkpoint |
| `{date}-{HHMM}.md` | the **human digest** — the top movers, their catalyst and their `conf` | every successful checkpoint |
| `{date}-{HHMM}.SKIPPED.md` | the trail a fail-closed checkpoint leaves behind | when `XAI_API_KEY` is unset |

**Only the `.jsonl` is the machine contract.** The `.md` digest is for a person; the consumer
(`preopen_feed.py`) reads the JSONL and never the digest. The `.SKIPPED.md` marker means no tape
was written on purpose — it is NOT a missing artifact.

### The digest

```
| Ticker | % | Conf | Catalyst | When it broke |
```

Top 15 rows by `|%|` descending. The header carries the record count, the Grok-vs-scanner
split, the `unverified` count and the measured Grok cost. `conf` is the tape's own token
(`high | medium | low | unverified`); an `unverified` row is marked `⚠ unverified` so it is
obvious that the catalyst could not be tied to a scanner price.

### The expected tape size

**≈678 rows** on a normal 08:30 checkpoint (measured 2026-11-04: 406 gainers / 271 losers /
1 flat; the 2026-11-05 08:30 tape was 700). A quiet session lands lower, a violent one higher.

**A tape of ~120 rows is the REGRESSION SIGNATURE**, not a quiet market: it means the scanner
call went back to sorting by `premarket_volume` (the pre-2026-11-05 procedure), which buries
the biggest movers under a wall of noise. The digest of such a tape carries a `DEVIATION`
banner. Do not publish it as if it were complete.

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
| `src` | `grok` \| `tv` | `grok` = narrative source. `tv` = scanner-only row, no reason yet. |
| `ticker` | string | Uppercase, required. Rows without one are dropped. |
| `name` | string \| null | Company name, optional. |
| `pct` | number \| null | Percent move. **Always from the scanner**, never from Grok. |
| `price` | number \| null | Price. Same rule. |
| `cat` | vocabulary | `acquisition, merger, earnings, guidance, fda, trial, offering, halt, downgrade, guidance-cut, spin, dividend, other` |
| `why` | string \| null | One clause, ≤200 chars, the specific catalyst. |
| `ref` | string \| null | Source URL. A record without one is `conf: low`. |
| `conf` | `high` \| `medium` \| `low` \| `unverified` | `unverified` ⇒ the feed's `pct` disagreed with the scanner by >2pp. |

Unknown `cat` values are coerced to `other` on read.

## Who writes what

| Writer | Writes | When |
|---|---|---|
| cron `92a` (platform) | `preopen-feed/{date}-0830.jsonl` + `.md` | 08:30 ET, Mon–Fri |
| cron `92b` (platform) | `preopen-feed/{date}-0950.jsonl` + `.md` | 09:50 ET, Mon–Fri |
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
2. **Prices are never taken from Grok.** The scanner is the source of truth; a >2pp disagreement
   becomes `unverified`.
3. **No key ⇒ no tape, but a trail.** If `XAI_API_KEY` is unset the capture writes NO JSONL
   (an empty tape would read as "no news" to the consumer) and writes
   `preopen-feed/{date}-{HHMM}.SKIPPED.md` naming the reason. A consumer that sees the marker
   must treat the checkpoint as *deliberately declined*, never as missing.
7. **One snapshot per checkpoint.** Every number in a tape comes from the same scanner snapshot,
   taken movers-sorted in BOTH directions. A record whose price came from a different call than
   its neighbours is a spliced tape (measured 2026-11-04: four records drifted, CRIS +93.3 →
   +97.5 and DKI +48.0 → +69.9, purely because the tape moved between two calls).
4. **Append only.** Never rewrite an earlier checkpoint's rows.
5. **No backfilling.** A missing checkpoint is normal.
6. **The scanner's `premarket_*` columns are LIVE ONLY** — blank for a past date. The 09:30 /
   10:00 / 12:00 path from 5-minute bars is historical and always valid.
