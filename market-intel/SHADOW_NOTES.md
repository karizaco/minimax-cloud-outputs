# SIP Taiwan shadow notes

Live digests/routines stay untouched. Shadow writes **only** under `/home/box/taiwan-in-play/shadow/`.

## Hand-shadow week runbook (~1 week)

### 1) Grok TradingView prep (optional each open/midday)
Using `user-TradingView Local` within the TV rate budget (~20/min, ≤12–15 calls/slot):
1. Prefer **one** `run_screener` for Taiwan movers (or skip if HTML/fixture movers already cover discovery). On HTTP 429: stop further screener retries.
2. One `get_symbol_data_batch` (≤50, `EXCHANGE:TICKER`) on the merged candidate set; serial `get_symbol_data` only for batch `missing` (cap ≤10).
3. `get_news` only for top floor-cleared names (cap ~5–8). Prefer local MOPS first.
4. Write the dump to a path under the shadow tree or a pytest/tmp dir, e.g.  
   `/home/box/taiwan-in-play/shadow/tv_dump_YYYY-MM-DD-<slot>.json`  
   (must pass the path guard — never write under live `/home/box/taiwan-in-play/` root).

### 2) Shadow CLI
```bash
ROOT=/workspace/market-intel   # or gh-repo/market-intel checkout
export PYTHONPATH="$ROOT"
DATE=YYYY-MM-DD
SLOT=open   # or midday
FIXTURES=/path/to/fixtures-or-live-fetch-dir
OUT=/home/box/taiwan-in-play/shadow

/home/box/venvs/sip/bin/python -m sip.cli shadow \
  --market taiwan \
  --slot "$SLOT" \
  --date "$DATE" \
  --fixtures "$FIXTURES" \
  --out-root "$OUT" \
  ${TV_DUMP:+--tv-dump "$TV_DUMP"}

# Optional Minimax chat draft + number-trace (propagates mmx exit codes):
/home/box/venvs/sip/bin/python -m sip.cli shadow ... --require-mmx-chat
```

The runtime can be overridden with `SIP_MMX_CHAT` or `MMX_CHAT_BIN`. These values
are resolved to absolute paths. If neither environment variable is set, the
resolver prefers `/workspace/market-intel/bin/mmx_chat.py` and then the
repository-local `bin/mmx_chat.py`. A missing executable returns exit code 2.

Or: `scripts/shadow_dry_taiwan.sh` (derives `DATE` from fixture dirname `taiwan-YYYY-MM-DD-*`).

Outputs:
- `$OUT/$DATE-$SLOT.json`
- `$OUT/$DATE-$SLOT.md` (digest; tables capped by `digest_top_n`)
- `$OUT/$DATE-$SLOT.chat.md` (chat; capped by `chat_top_n`)

### 3) Compare vs live
```bash
/home/box/venvs/sip/bin/python -m sip.cli compare \
  --shadow "$OUT/$DATE-$SLOT.md" \
  --live "/home/box/taiwan-in-play/$DATE-$SLOT.md" \
  --json-out "$OUT/$DATE-$SLOT.compare.json"
```
`--json-out` must also sit under the shadow root (path guard).

### 4) What to report each day
- Shadow exit code (nonzero → fall back to live flow; see `sip/EXIT_CODES.md`)
- Compare summary: `both` / `only_live` / `only_shadow` / `catalyst_diffs`
- Per-tier counts (A, Soft-A, TECH_WATCH, B, C) for shadow vs live
- Soft-A / TECH_WATCH within ~2× of live? A still matching?
- Any Source health `blocked` / `coverage_failed` / path-guard / number-trace (5) / quota (3) / rate-limit (4)
- Do **not** flip the live Taiwan routine until Hypnotoad confirms after the shadow week

## Quality gates (Soft-A / digest-cap follow-up)
- MOPS attach requires materiality score ≥1 and not boilerplate (取得有價證券 / 機器設備 / 董事改派 / …)
- `soft_a_requires_catalyst: true` enforced; Soft-A/A need material catalyst
- TECH_WATCH uses `tech_watch_rvol_min/max` (~1.0–2.0); rvol ≥ max → B
- Missing MOPS remains a coverage cascade for TECH_WATCH; no heuristic change was made
- Digest tables capped via `digest_top_n` (chat via `chat_top_n`)
- LIMIT_DOWN → C first
- Overnight carry promotions tagged `OVERNIGHT_PROMOTED` and returned in rows
- Percentage number tracing uses `PERCENT_TOLERANCE = 0.05` percentage points and preserves sign checks
- MOPS discovery checks `mops_items.json`, `mops-browser.txt`, `mops_browser.txt`, and `mops-browser.md`
- If none exists, MOPS source health is `coverage_failed`, not `skipped`
- C watches are retained only for LIMIT_UP, LIMIT_DOWN, TOB_GAP, HALT, and OVERNIGHT_PROMOTED variants; residual C filler is dropped
- The remaining C watches are capped by `engine_top_n.C`, falling back to `digest_top_n.C`, in descending dollar volume
- A, Soft-A, TECH_WATCH, and B are not trimmed by the C-watch rule
- Activation has **not** been flipped; this remains a shadow-only change

## 2026-11-05 open (pre / post Soft-A follow-up)
See latest compare numbers in the PR / agent report after re-run.
