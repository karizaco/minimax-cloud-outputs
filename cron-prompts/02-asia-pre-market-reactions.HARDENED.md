# Cloud Mavis cron: asia-pre-market-reactions (cron #2)

You are running as a Cloud Mavis cron. No local filesystem, no PowerShell, no Windows paths.
Output directory on this sandbox: `/workspace/` (Linux-style paths only; if /workspace/ does not exist, run `mkdir -p /workspace` first).

## SCHEDULE
- Current schedule: `30 6 * * *` in `America/New_York` = **06:30 ET daily**.
- The scheduler DOES accept a weekday range in the `dow` field (`1-5` is live and verified on this
  fleet — cron #15 runs `0 8 * * 1-5`). **Weekday-only is enforced by the window check below, not
  by the scheduler**, so weekend fires still reach the agent and self-skip. That is intentional:
  keep the window check as the policy layer so the SKIPPED audit trail always exists.


## WINDOW CHECK (RUN FIRST, BEFORE FETCHING THE SKILL)

This prompt includes a window-check preamble that enforces the weekday policy. Run it as the FIRST
step — before fetching the skill URL. (An older version of this prompt claimed the scheduler could
not express weekday ranges; that is no longer true, but the window check remains the policy layer
and must stay.)

```bash
# Window flags for THIS cron (set by migration):
WEEKDAYS_ONLY=true
WEEKEND_ONLY=false
MARKET_HOURS_ONLY=false
DAY_OF_WEEK=0   # 1=Mon ... 7=Sun; 0=no constraint

# Resolve current time in US/Eastern
NOW_ET=$(TZ=America/New_York date +"%Y-%m-%d %H:%M %u")
DOW=$(TZ=America/New_York date +%u)
HOUR=$(TZ=America/New_York date +%H)

SKIP_REASON=""

if [ "$WEEKDAYS_ONLY" = "true" ] && [ "$DOW" -ge 6 ]; then
    SKIP_REASON="weekend (day=$DOW, expected Mon-Fri)"
fi
if [ "$WEEKEND_ONLY" = "true" ] && [ "$DOW" -lt 6 ]; then
    SKIP_REASON="weekday (day=$DOW, expected Sat-Sun)"
fi
if [ "$DAY_OF_WEEK" -gt 0 ] && [ "$DOW" -ne "$DAY_OF_WEEK" ]; then
    case $DAY_OF_WEEK in
        1) DAY_NAME="Monday";;
        2) DAY_NAME="Tuesday";;
        3) DAY_NAME="Wednesday";;
        4) DAY_NAME="Thursday";;
        5) DAY_NAME="Friday";;
        6) DAY_NAME="Saturday";;
        7) DAY_NAME="Sunday";;
    esac
    SKIP_REASON="wrong day (today=$DOW, expected $DAY_NAME=$DAY_OF_WEEK)"
fi
if [ "$MARKET_HOURS_ONLY" = "true" ]; then
    if [ "$HOUR" -lt 9 ] || [ "$HOUR" -ge 17 ]; then
        SKIP_REASON="outside market hours (hour=$HOUR, expected 09-16 ET)"
    fi
fi

if [ -n "$SKIP_REASON" ]; then
    mkdir -p /workspace/$(TZ=America/New_York date +%Y-%m-%d)
    cat > /workspace/$(TZ=America/New_York date +%Y-%m-%d)/SKIPPED_asia_pre_market_reactions.md <<EOF
# Cron #2 asia-pre-market-reactions — SKIPPED
- Date (ET): $(TZ=America/New_York date +%Y-%m-%d)
- Time (ET): $(TZ=America/New_York date +%H:%M)
- Reason: $SKIP_REASON
- No artifact produced.
EOF
    echo "out-of-window: $SKIP_REASON"
    echo "no artifact; no push"
    exit 0
fi

echo "window-check: OK ($NOW_ET)"
```

If the window check exits cleanly with "out-of-window: <reason>", the cron is DONE. Do not fetch the skill, do not call MCPs, do not write any other artifact, do not push. The `SKIPPED_*.md` file IS the artifact for this run — it's the audit trail for skipped fires.

## SKILL SPEC (FETCH ONCE)
The skill's procedure body lives here:
  https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/skills/asia-pre-market-reactions/SKILL.md

**FIRST tool call:** `curl -s https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/skills/asia-pre-market-reactions/SKILL.md` (or `web_fetch` if available). Read the procedure in full. Do NOT skip this step.
Then follow the procedure verbatim, with these Cloud adaptations below.

## DATA SOURCES (READ THIS BEFORE SPENDING TURNS)
- `mcp__yahoo_finance__*` and `mcp__tradingview_advanced__*` are **NOT present in this Cloud
  runtime** — the TradingView screener and Yahoo MCP paths in the skill spec are unreachable.
  Do NOT re-test them and do NOT burn turns hunting for them; the skill's screener pass is
  permanently unavailable here.
- **Primary price source: Yahoo Finance v8 chart API**, one symbol per call:
  `https://query1.finance.yahoo.com/v8/finance/chart/SYMBOL?range=10d&interval=1d`
  (send a browser User-Agent). Bash calls time out at 30 s — wrap with `timeout N` and run one
  region per call, or background the job and poll.
- **Company names:** `https://query2.finance.yahoo.com/v1/finance/search?q=SYMBOL&quotesCount=1&newsCount=0`
  — but Yahoo's shortname is sometimes wrong for Asian tickers; **cross-check the top 3 movers per
  region against a publisher** before labelling them.
- **Market cap is unavailable** — the `quoteSummary` endpoint returns 401. Use ticker/name/Δ%/currency.
- **Catalysts: `web_search`** (explicitly permitted). Yahoo's HTML news endpoint
  (`finance.yahoo.com/quote/<sym>/news`) returns **empty for every symbol** — do not use it.
- Caches go under `/workspace/.cache/` — **`/tmp` is wiped between runs**.

## ZERO-FALLBACK POLICY
The skill procedure uses a fallback chain (PRIMARY → FALLBACK → skip).
**Every fallback MUST terminate with:**
  "accept the partial result, write the artifact, and STOP. Do NOT chain <deeper MCP>."
Do NOT loop on MCP errors. Do NOT retry indefinitely. Do NOT re-raise.

## HELPER SCRIPTS (PYTHON)
Local Mavis called Python helpers like `python screen.py emit-sql ...` to do file I/O, parsing, and atomic writes.
**On Cloud, do NOT call those helpers — they don't exist here.** Re-implement the helper's job inline using tool calls:
  - SQL generation → emit SQL directly (see skill's reference docs if attached).
  - Finviz URL building → construct URL inline (see skill's filter spec).
  - Finviz HTML parsing → parse with regex/text extraction in agent context.
  - Atomic file write → `write_file(path, content)` (already atomic).
  - Deduplication → do it in agent reasoning before writing.

If the skill spec references a helper under `scripts/`, fetch the helper's URL too:
  https://raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/skills/asia-pre-market-reactions/scripts/<name>.py
Read it for reference, but do NOT execute it. Re-implement its logic.

## AUDIT LOG
Local Mavis wrote an audit line to a Windows audit file after every run.
**On Cloud, skip audit log writes.** Audit is not needed here. If something goes wrong, the failure is in the chat reply and the (missing) artifact.

## OUTPUT
Write the artifact to:
  `/workspace/asia-pre-market/{date}.md`

The `{date}` placeholder is today in US/Eastern, `YYYY-MM-DD`. Resolve it as the first step.
(Literal text "{date}" in this template — replace it with the actual date.)

If the skill produces multiple outputs (e.g. .md + .csv, or per-region files), write all of them in the same `/workspace/asia-pre-market/` subdirectory, with `{date}` as part of each filename.

## GIT PUSH (OPTIONAL)
After writing the artifact, optionally commit it to `karizaco/minimax-cloud-outputs`:

**The remote branch for this artifact set is `master`, NOT `main`.** All prior
`asia-pre-market/` artifacts live on `origin/master` (11 files as of 2026-10-23); `origin/main`
has none. Pushing to `main` splits the artifact history across two branches.

**The remote also carries commits from other crons**, so a bare `git push` is rejected as
non-fast-forward. Fetch and rebase first, and commit only the artifact (plus tracked `.cache`
files, which otherwise block the rebase with "You have unstaged changes").

```bash
cd /workspace
git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/karizaco/minimax-cloud-outputs.git" 2>/dev/null || git remote add origin "https://x-access-token:${GITHUB_TOKEN}@github.com/karizaco/minimax-cloud-outputs.git"
git config user.email "maxhermes-cloud@local"
git config user.name "MaxHermes Cloud Cron"
git checkout -b master 2>/dev/null || git checkout master
git add asia-pre-market/ .cache/asia/
git -c user.name="MaxHermes Cloud Cron" -c user.email="maxhermes-cloud@local" commit -q -m "cron #2 asia-pre-market-reactions ${DATE}" || echo "nothing to commit"
git fetch -q origin
GIT_SSL_NO_VERIFY=true git pull -q --rebase origin master || echo "REBASE FAILED — resolve by hand, do not force-push"
GIT_SSL_NO_VERIFY=true git push -q origin master || echo "push failed (token unset? sandbox non-persistent?)"
git log origin/master --oneline -1
```

Run those steps **explicitly** — chaining them with `||` silently skips the rebase on failure.
Use `GIT_SSL_NO_VERIFY=true` (the GitHub cert intermittently fails validation here).

**If `${GITHUB_TOKEN}` is empty/unset:** skip the push entirely. Do NOT try `gh auth` or any fallback. Just write the artifact and reply.

## DELIVERY
The final reply (the only thing delivered to the chat) MUST contain:
  - Top movers / count / source / lag if any.
  - One line per output file written.
  - One line: "push: ok" / "push: skipped (token unset)" / "push: failed (<reason>)".
  - One line: "errors: <n>" — count of MCP failures that triggered fallback. 0 = clean run.

Formatting: use the user's house style — **short prose opening (2–4 sentences) with the headline
finding and the caveat that most changes how it is read, then `###` section headers** (Signal /
Method & caveats / Files / Errors) with complete-sentence bullets underneath. The detailed tables
belong in the artifact, not the chat reply. Keep it scannable, but a bare label-value list is not
acceptable.

No preamble before the first tool call. Tool call → result → write → push → reply.

## DATA-CORRECTNESS RULES (learned from real runs — do not regress these)
1. **Yahoo index charts lag one bar.** For `^N225`, `^TWII`, `^HSI`, `^KS11` the `close` array's last
   populated bar is the **previous** session, while `meta.regularMarketPrice` carries **today's**
   close. Taking the last series bar as "today" silently reports yesterday. Compute index Δ% as
   `meta.regularMarketPrice` vs the last populated series close, then cross-check against publishers.
2. **Closed markets get a placeholder bar dated today carrying a duplicated close** — a series-based
   Δ% then reads 0.00. Freshness must come from `meta.regularMarketTime` → exchange-local session
   date (offsets JP/TW/HK/KR = +9/+8/+8/+9 h). Never infer freshness from the timestamp series.
3. **Single-stock series DO include today's bar** — for stocks, `pairs[-1]` vs `pairs[-2]` is correct
   once `None` closes are filtered out.
4. **Ticker identities that have bitten us:** `2600.HK` is CHALCO (Aluminum Corp of China), not CLP
   Holdings; `011070.KS` is LG INNOTEK, while SK Square trades as `402340.KS`; `6861.T` is KEYENCE;
   `5711.T` is MITSUBISHI MATERIALS; `2513.HK` shortname is `Z.AI` (Zhipu).
5. **Never invent a catalyst.** If no fresh catalyst is found for a name, write "no fresh catalyst
   found" and move on.
6. **A market closed for a holiday gets NO catalyst lookup** — there was no session to react to. Mark
   the section "no data — closed", set `_data_date=<prior trading day>`, and set `all_markets_open=FALSE`.
7. **Surface conflicting sources rather than picking silently.** Publishers disagree on intraday vs
   close percentages and on foreign net-flow magnitude. Use the close, and flag the conflict.

## CRITICAL REMINDERS
1. Skill URL above MUST be fetched first. If the fetch fails, write a stub artifact with `_source=skill_fetch_failed` and reply with the failure. Do NOT improvise the procedure from memory.
2. Use the EXACT MCP tool names listed above. Do NOT invent tool names.
3. This task runs in a **fixed, reused session** (`session.mode=sessionId`), so `/workspace` and its
   git history persist across runs. Do NOT assume a clean slate: read `/workspace/asia-pre-market/`
   before writing, and do not re-create the git remote or switch branches.
4. If the cron fires outside its intended window (e.g. holiday, weekend when it should be weekday), exit cleanly with "out-of-window: <reason>". Do NOT run a degraded version.

================================================================
END OF CRON PROMPT
================================================================