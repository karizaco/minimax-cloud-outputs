# Cloud Mavis cron: earnings-reaction-scanner (cron #15) — REPAIRED 2026-10-24

You are running as a Cloud Mavis cron on Mavis. Linux sandbox: no PowerShell, no Windows paths.
Output root: /workspace/ (mkdir -p it if missing).

## SCHEDULE
Fires 08:00 ET on weekdays: cron `0 8 * * 1-5`, timezone America/New_York.
This matches the skill's own spec (`0 8 * * 1-5` ET) — 23 min after the pre-market brief,
~90 min before the US open, ~5h into the EU session, ~6h after the ASX close.

**REPAIR NOTE (2026-10-24):** this task used to fire at 14:30 Europe/Berlin = 08:30 ET while its
window check demanded 09:00-16:00 ET, so it skipped itself every single day and has never
produced an artifact. TWO gates had to be fixed: the timezone anchor AND the `MARKET_HOURS_ONLY`
flag, because this is a PRE-MARKET scan. The schedule is now `0 8 * * 1-5` America/New_York.
Do not "fix" a skip by assuming the market is closed - check the clock and read the reason string. Do not "fix" a skip by assuming the market is closed — check
the clock and read the reason string.

## STEP 1 — WINDOW CHECK (run this first, before anything else)

```bash
WEEKDAYS_ONLY=true
WEEKEND_ONLY=false
MARKET_HOURS_ONLY=false
DAY_OF_WEEK=0   # 1=Mon ... 7=Sun; 0=no constraint
# This cron is a PRE-MARKET scan (08:00 ET), so it must NOT be gated on
# market hours. It IS gated on weekdays: there is no US session to react to.

NOW_ET=$(TZ=America/New_York date '+%Y-%m-%d %H:%M %u')
DOW=$(TZ=America/New_York date +%u)
HOUR=$(TZ=America/New_York date +%H)
MIN=$(TZ=America/New_York date +%M)
SKIP_REASON=
if [ "$WEEKDAYS_ONLY" = "true" ] && [ "$DOW" -ge 6 ]; then
  SKIP_REASON="weekend (day=$DOW, expected Mon-Fri)"
fi
# Accept 08:00-08:59 ET, plus 09:00-09:29 ET to absorb a delayed fire.
# Rationale: the US pre-market session runs 04:00-09:30 ET, so a scan landing
# before 09:30 ET still reads LIVE pre-market prints. A fire at or after 09:30 ET
# would read frozen post-open values instead, so the gate stops there.
# Do NOT widen this window past 09:30 ET - a post-open scan is a different
# artifact, and widening the gate silently is how this task died before.
if [ -z "$SKIP_REASON" ]; then
  if [ "$HOUR" -ne 8 ] && { [ "$HOUR" -ne 9 ] || [ "$MIN" -ge 30 ]; }; then
    SKIP_REASON="off-schedule hour ($HOUR:$MIN ET, expected 08:00-09:29 ET)"
  fi
fi
if [ -n "$SKIP_REASON" ]; then
  DATE=$(TZ=America/New_York date +%Y-%m-%d)
  mkdir -p /workspace/$DATE
  printf '# Cron #15 earnings-reaction-scanner - SKIPPED\n- Date (ET): %s\n- Time (ET): %s\n- Reason: %s\n' \
    "$DATE" "$(TZ=America/New_York date +%H:%M)" "$SKIP_REASON" \
    > /workspace/$DATE/SKIPPED_earnings_reaction_scanner.md
  echo "out-of-window: $SKIP_REASON"
  echo "no artifact; no push"
  exit 0
fi
echo "window-check: OK ($NOW_ET)"
```

If this exits with "out-of-window: <reason>", the run is DONE. Do not fetch the skill, do not
call APIs, do not write any other artifact, do not push. The `SKIPPED_*.md` file IS the artifact.

## STEP 2 — FETCH THE PIPELINE (the skill's MCP tools do not exist in Cloud)

The skill spec at
`https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/skills/earnings-reaction-scanner/SKILL.md`
is the authoritative *procedure* (passes, thresholds, tags, caps, artifact sections). Read it once
for reference.

But every MCP tool it calls is **absent in Cloud sessions** — verified 2026-10-24:
`mcp__tradingview-advanced__*`, `mcp__tradingview__*`, `mcp__financekit__*`, `mcp__stocktwits__*`
return 0 hits from `tool_search`, and `mcode-tools connector tools` holds only media + credential
tools. Do NOT burn turns re-testing them. A validated replacement pipeline is committed to the
shared output repo. Fetch and run it:

```bash
cd /workspace
mkdir -p scripts
curl -sS -w 'HTTP=%{http_code}\n' --max-time 60 \
  https://raw.githubusercontent.com/karizaco/minimax-cloud-outputs/main/scripts/earnings_reaction_scanner.py \
  -o scripts/earnings_reaction_scanner.py
head -5 scripts/earnings_reaction_scanner.py
```

If that fetch fails, retry once with `-k` (the GitHub cert expires intermittently). If both
attempts fail, write a stub artifact with `_source=skill_fetch_failed`, report `errors: 1`, stop.
Never improvise the procedure from memory.

## STEP 3 — RUN THE PIPELINE

```bash
cd /workspace
python3 scripts/earnings_reaction_scanner.py
```

It writes `/workspace/earnings/<date>-reactions.md` and
`/workspace/earnings/<date>-catalyst-targets.json`. It is self-timing: it takes ~4-6 minutes
because it cross-checks reported movers against Yahoo. **Give it a generous timeout** (at least
560s). If it exceeds that, capture the partial state and report the failure — do not silently
ship a half-written artifact.

What the pipeline does, and why (read this before changing any of it):

* Source is the TradingView **public screener** (`https://scanner.tradingview.com/<market>/scan`),
  which replaces the absent MCP screener. One POST per market per direction, JSON in, JSON out.
* **Stale-reference rows.** On illiquid rows the screener's `change` is computed against a stale
  reference close, producing absurd prints (MRNA on SIX showed +71.77% on 25 shares while the US
  line moved -1.25%). The tell: `change` == `Perf.W` exactly, and `Perf.1D` is always null.
  A **volume floor of 10,000** removes these rows. Do not lower it.
* **Venue codes differ from the skill's priority table.** The public scanner returns EURONEXT for
  FR/NL/BE/PT/IE, EUROTLX for IT, BX for CH, OMXCOP for DK, OMXHEX for FI, GPW for PL, VIE for
  AT, ATHEX for GR, XETR-family for DE, LSE for UK, ASX for AU. The skill's table (AMS/BRU/PAR/
  LIS/DUB/MC/HE/CO/VI/AT/SW/WA) is for the MCP screener. The pipeline maps them explicitly.
* **`country` is the reliable primary-listing filter** — it correctly excludes US ADRs listing on
  EU venues (97 of 200 Swiss rows were `country=United States`).
* **`earnings_release_date` = most recent FULL report date** (WDC 2026-10-22 matches the press),
  `earnings_release_next_date` = next scheduled. These replace the absent financekit calendar.
  **Caveat: this field does NOT capture preliminary, guidance or restructuring releases.** On
  2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while the field still read 2026-07-30.
  The field is a screen, never a verdict — confirm against the headline.
* **Yahoo cross-check.** Yahoo's ASX feed appends a trailing live-stamp bar at a different
  time-of-day than the completed daily bars; naive last-two-bar math makes every ASX move read
  0.00%. The pipeline keeps only bars stamped at the modal time-of-day before differencing.
  Verified 2026-10-24: **27 cross-checks agreed, 0 mismatched.**
* BOD rows (no extended-hours data) go to source health only, not the headline table, per the
  skill. US preferred shares (slash tickers like JPM/PC) are excluded.

## STEP 4 — CATALYSTS (the one step the pipeline cannot do)

The skill caps catalysts at 5 US + 3 EU + 2 AU = 10 per run. Read
`/workspace/earnings/<date>-catalyst-targets.json` for the ticker list, then use `web_search` to
find the headline for each (cap 10 searches; 1-2 per ticker). For US names, the earnings-driven
test is: did `earnings_release_date` land within 7 days of today? If yes, mark `Y` and use the
earnings headline as the catalyst. If not, mark `N` and find a non-earnings catalyst. For EU/AU
names apply the skill's keyword test (earnings / results / Q1-Q4 / beats / misses / reports /
guidance; plus interim, half-year, full-year, dividend, ASIC, iron ore, lithium, gold for AU).

**Then write the catalyst table to `/workspace/catalog/catalysts/<date>.md`** (mkdir -p first)
and re-run the pipeline, which splices that file into the artifact's `## Catalysts` section.
Doing it this way means a re-run never wipes your work. You may also edit the table in place
instead, but then do not re-run the pipeline afterwards.

**Never fabricate a headline.** If a search returns nothing usable, write "no fresh catalyst found".

## STEP 5 — WRITE THE ARTIFACT

The pipeline writes `/workspace/earnings/<date>-reactions.md` with the TL;DR, the US headline
table, US QUIET one-liners, the EU/UK table, the ASX table, source health and the audit line.
Keep every other section as the pipeline wrote it — it carries the row counts, the cross-check
result and the freshness stamps.

If the script failed and no artifact exists, write a stub with `_source=skill_fetch_failed` and
report the error. Never improvise the tables from memory.

## STEP 6 — PUSH (only if GITHUB_TOKEN is set)

`karizaco/minimax-cloud-outputs` is **shared across crons**. Never force-push. The repo's branch
is `main` while a fresh `git init` creates `master`, so push `HEAD:main`. Fetch first, or the
push is rejected as "fetch first".

```bash
cd /workspace
git init -q 2>/dev/null || true
git remote remove origin 2>/dev/null || true
git remote add origin https://x-access-token:${GITHUB_TOKEN}@github.com/karizaco/minimax-cloud-outputs.git 2>/dev/null || true
git config user.email maxhermes-cloud@local
git config user.name 'MaxHermes Cloud Cron'
DATE=$(TZ=America/New_York date +%Y-%m-%d)
mkdir -p earnings/$DATE catalog/catalysts
git add earnings/$DATE catalog/catalysts scripts
git commit -q -m "cron #15 earnings-reaction-scanner $DATE" || echo 'nothing to commit'
GIT_SSL_NO_VERIFY=true git fetch -q origin main
GIT_SSL_NO_VERIFY=true git merge origin/main --allow-unrelated-histories -X ours 2>&1 | head -3
GIT_SSL_NO_VERIFY=true git push -q origin HEAD:main 2>&1 | head -3 || echo 'push failed'
```

If `${GITHUB_TOKEN}` is unset, skip the push entirely. Do NOT try `gh auth` or any fallback.

## DELIVERY (the only thing delivered to the chat)
Six lines, no preamble:
earnings-reaction-scanner (cron #15) - DATE TIME_ET
window: passed | skipped (reason)
top movers: <name> <pct>% (region) | none | counts
candidates: N | AMC: N | PRE_GAP: N | EU: N | AU: N | cross-check: agree N / mismatch N
file: PATH (BYTES B, written) | no artifact
push: ok | skipped (token unset) | failed (reason)
errors: N

## CRITICAL REMINDERS
1. Window check first. If it says out-of-window, exit cleanly — the SKIPPED file is the artifact.
2. The MCP tools in the skill spec do not exist in Cloud. Use the pipeline from the shared repo.
3. Do not lower the volume floor of 10,000. Without it, illiquid rows report 30-90% phantom moves.
4. Read-only. No trade ideas. Never fabricate a catalyst headline or a data value.
5. Every number in the artifact must come from a payload you actually received. If a pass returned
   too few rows to be credible, report the row count rather than padding the table.
6. If the cross-check reports any mismatch, say so in the chat reply. A mismatch means the
   screener and Yahoo disagree on a move you are about to publish — investigate before shipping.
7. Never widen or narrow the window gate to make a run "pass". If the gate rejects the fire,
   report the skip. A silently-skipped cron is the failure mode this task was repaired to escape.
