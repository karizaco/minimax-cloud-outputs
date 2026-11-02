# Plan — data sources without registered MCPs, and tracking for MCP arrival

**Status:** proposal, not executed. Two decisions needed from the owner (§6).
**Scope:** cron #17 `us-stocks-in-play`, plus the fleet-wide MCP health picture.
**Evidence date:** 2026-10-31 (Sat — market closed, so live-only behaviour is marked unverified).
**Repos:** `karizaco/maxhermes-migration` (source of truth for prompts/skills — I hold admin),
`karizaco/minimax-cloud-outputs` (shared artifact bus).

---

## 1. The headline

The premise — "we can't use custom MCPs here" — is true but not decisive. **The MCP *tool names*
don't exist in agent.minimax.io, but the MCP *servers* are reachable over plain HTTPS JSON-RPC from
the sandbox.** The fleet already shipped `mcp_bridge.py` for exactly this, and the deployed cron #17
prompt now names the bridge as its PRIMARY source.

So the answer to #1 is not "build a relay". It's **"use the bridge that already exists, and point it at
one more pack."**

Separately: the mechanism for #2 **already exists as a prompt and was never switched on.**

---

## 2. What I verified live today (2026-10-31)

| Path | Endpoint | Result |
|---|---|---|
| Bridge → **market-recap** | `https://gateway.pipeworx.io/market-recap/mcp` | **48 tools.** `get_quotes` → SPY 755.72, QQQ 690.49, AAPL with `previous_close`, `change_pct`, `volume`, `day_high/low`, `as_of`, `market_state` |
| Bridge → stocktwits | `https://gateway.pipeworx.io/stocktwits/mcp` | 53 tools |
| Bridge → shibui | `https://mcp.shibui.finance/mcp` | 12 tools |
| Bridge pack discovery | `discover_tools` on the gateway | finds packs by natural-language query — surfaced **market-recap** and **cftc-cot** (CFTC positioning, unused by anyone) |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | 200 — movers, `relative_volume_10d_calc`, **`halted`**, **`premarket_change`/`volume`/`close`** |
| Yahoo quoteSummary | `v10/finance/quoteSummary` + crumb | 200 — `floatShares`, `sharesOutstanding`, `shortRatio`, 52-week range |
| Yahoo options chain | `v7/finance/options` + crumb | 200 — IV, implied move |
| Nasdaq market movers | `https://api.nasdaq.com/api/marketmovers?market=stocks` | 200 |
| SEC EDGAR | `efts.sec.gov` full-text + `company_tickers.json` + 8-K Atom | 200 — 168 8-Ks for a 4-day window |

**Implication:** Finviz, Barchart and the TradingView/Yahoo MCPs are **not needed**. Their content
is covered by market-recap (quotes), TradingView scanner (movers/RVol/premarket/halts), Yahoo
(float/short/options), Nasdaq and EDGAR (filings). The only genuinely blocked thing is Finviz's
Cloudflare challenge — and Finviz's content is a subset of the other five.

The bridge's `SERVERS` dict only lists `stocktwits` and `shibui`. **`market-recap` is missing and
it's the best source on the list.**

---

## 3. Point #1 — plan of actions

### A1. Generalise `mcp_bridge.py` to any gateway pack  *(highest value, smallest diff)*

`_shared/mcp_bridge.py` currently hardcodes two servers. Make the server argument resolve to a
pack path, so any pack on the gateway works without a code change:

```python
SERVERS = {
    "stocktwits":  "https://gateway.pipeworx.io/stocktwits/mcp",
    "shibui":      "https://mcp.shibui.finance/mcp",
    "market-recap":"https://gateway.pipeworx.io/market-recap/mcp",
    "cftc-cot":    "https://gateway.pipeworx.io/cftc-cot/mcp",
}
# fallback for an unknown pack:
#   https://gateway.pipeworx.io/{pack}/mcp
```

Usage after the change: `python3 mcp_bridge.py market-recap get_quotes args.json`, with
`{"symbols": "SPY,QQQ,AAPL"}`. Keep the "args as a FILE" rule — shell quoting corrupts JSON.
Add a `--list-packs` mode that calls `discover_tools` so pack discovery is self-service.

**Why it matters:** `get_quotes` returns exactly the fields the skill's Pass 2 wants (last, prior
close, %chg, volume, day high/low, `as_of`, `market_state`) for many symbols in one call, and it is
**not rate-limited**. It becomes the primary quote source, displacing the Yahoo path that the
RUNTIME-CONTRACT currently says is 429.

### A2. Promote the bridge in the cron #17 source ladder

The deployed prompt already says "Order of attack: MCP bridge → `web_search` → curl ladder". Extend
the curl ladder with the newly verified endpoints so nothing has to be re-derived:

```
bridge.market-recap.get_quotes   →  quotes for a batch of symbols
scanner.tradingview.com/america/scan → movers + RVol + premarket + halted
api.nasdaq.com/api/marketmovers  →  session movers
efts.sec.gov full-text + 8-K Atom →  primary-source catalysts (items 1.01/2.01/5.02/7.01/8.01)
query1.finance.yahoo.com quoteSummary + options → float, short ratio, implied move
```

### A3. Close the halt blind spot

Every digest in the series since 2026-10-13 carries "halts unverified" — the NASDAQ RSS feed has
returned an empty HTML shell on 6/6 attempts, and `api.nasdaq.com/api/quote-list/halt-directory`
404s. The TradingView scanner exposes a `halted` column. **Caveat: my test returned `total: 0`
because the market was closed on a Saturday, so this is unverified until a live session.** Validate
on the next live run before removing the caveat from the digest template.

### A4. Correct the RUNTIME-CONTRACT

The contract (measured 2026-10-28) states Yahoo JSON returns a **persistent 429** from this egress.
My live evidence contradicts it: the screener, chart, quoteSummary and options endpoints all
returned 200 on every run from 10-13 to 10-23 and again today. Either the egress changed or the 429
was transient. **As written, the contract pushes every reader down a fallback path they don't
need.** Re-measure and correct it, and fold in the newly verified endpoints. This is a
documentation fix, not a behaviour change — the ladder should be tried in cost order, not
hardcoded to a stale verdict.

### A5. n8n — use it for egress, not for data

**Do not relay Yahoo / TradingView scanner / Nasdaq / EDGAR / market-recap through n8n.** They work
from the sandbox; a relay adds a failure mode for zero gain.

n8n is worth it for exactly two things:

1. **An egress relay for Cloudflare-challenged sources** (Finviz-class). n8n runs in your cloud
   with a different IP; the challenge that blocks the sandbox doesn't block you.
2. **A general "hard-to-reach feed" slot** — anything that needs a residential path.

**Recommended transport: n8n commits to the outputs repo.** The repo is already the fleet's shared
data bus, the push procedure is solved, and it needs no inbound endpoint or new credential in the
sandbox. Suggested layout: `data/feed/{date}.json`, written by n8n, read by cron #17 at 09:50 and
treated as one more source with its own Source health row.

Alternative (if you'd rather not have n8n hold a repo PAT): n8n POSTs to a webhook URL stored as a
secret, and the sandbox polls it. Workable, but it adds an inbound surface and a polling step.

### A6. Grok — a catalyst oracle, not a quote source

`api.x.ai` is reachable from the sandbox (401 without a key), and x.com / nitter.net return 200.
Grok's unique edge for this digest is **X and breaking news in the 09:00–09:50 window** — the exact
gap my digests have had to reconstruct from wire copy afterwards (the BRZE deal, LQDA's settlement
and SKYD's warrant halt were all found *after* the fact, not during).

Put the Grok call inside the n8n workflow: one n8n cron → Grok "what is in play in US equities
right now" → normalise to JSON → commit to the repo. Cron #17 reads it as a catalyst source with a
normalised schema (ticker, reason, timestamp, confidence).

**This is the single highest-value n8n use**, because it fills the pre-open information hole that
no quote API can fill.

---

## 4. Point #2 — plan of actions

### The gap

`cloud-prompts/01-weekly-mcp-health-check.md` is a finished prompt for a weekly (Sun 02:00 ET)
MCP/API health check writing `mcp-health/YYYY-Wnn.md`. **It was never staged:** there is no
`mcp-health/` directory on the outputs repo and it does not appear among the roster's 21 tracked
routines. The mechanism exists; the switch was never thrown.

### B1. Self-detection inside cron #17 — minutes of latency

The deployed prompt says *"Do not attempt an MCP call and do not wait for one to appear."* That is
correct for the digest (an MCP call that tool-not-founds aborts the run with no artifact), but it
means **nothing notices when an MCP arrives**.

Add a fixed, non-blocking probe step at the top of the run:
- enumerate the connector catalog;
- **distinguish three states** — "catalog healthy, 0 finance tools" / "catalog unreachable" (I hit
  `error: invalid signature` on 10-21) / "catalog healthy, N finance tools";
- write the state into the digest's Source health.

Then the very first digest after an MCP lands says so, without waiting for Sunday.

### B2. Stage the weekly health check — ≤7 days latency

Before staging, upgrade the prompt: it must probe **three layers** now, not one.

| Layer | Probe |
|---|---|
| Platform | agent.minimax.io connector catalog — finance tools present? catalog reachable? |
| Bridge | `discover_tools` on the gateway + each configured pack endpoint (stocktwits, shibui, market-recap, cftc-cot) |
| HTTP | the endpoint ladder — Yahoo screener/chart/quoteSummary/options, TradingView scanner, Nasdaq marketmovers, EDGAR, CoinGecko, Treasury CSV |

Output stays `mcp-health/YYYY-Wnn.md` (the prompt already specifies it).

### B3. A running ledger — the thing that actually answers the question

A weekly file shows you Sunday's state. What answers *"has TradingView been added yet?"* is a
**ledger whose diff is the signal**:

`mcp-health/ledger.md` — one row per run:

| date | catalog finance tools | catalog state | bridge packs OK | Yahoo | TV scanner | Nasdaq | EDGAR | notes |
|---|---|---|---|---|---|---|---|---|

This is also where the transient `invalid signature` catalog error belongs, so a catalog outage is
never mistaken for "no MCPs exist".

### B4. Repo-diff as a cheap secondary signal

MCP availability is a *platform* property; the repo is a *documented proxy* of it. But the prompt
will be edited when Minimax Cloud adds MCPs, and that edit is exactly the moment to re-verify the
digest's source stack. So: L1 + L2 + L3, plus a one-line repo-diff check inside the weekly health
check (compare the `MCP TOOLS AVAILABLE` block and `RUNTIME-CONTRACT.md` against last week's copy).

### B5. Where the changes land

All of B1–B4 plus A1/A2/A4 belong in **`karizaco/maxhermes-migration`** — that is the source of
truth for prompts and skills, and I have admin on it (`main` branch, unprotected). The outputs repo
holds artifacts; a `refs/` note pointing at the mechanism is the right cross-reference.

---

## 5. Two defects found along the way

### D1 — cron #17's schedule looks wrong *(high impact, needs a decision)*

The deployed task is `50 15 * * 1-5` America/New_York → **fires 15:50 ET**. But:

- the skill says the open slot is `50 9 * * 1-5` America/New_York = **09:50 ET**;
- every run from 10-13 to 10-23 fired at **09:50 ET**;
- the previous task was `50 15 * * *` **Europe/Berlin** = 09:50 ET during CEST;
- all 21 crons are now `America/New_York`, and every other cron's `fire_et` matches its documented
  ET time — this one is the only exception.

The timezone migration appears to have carried the Berlin wall-clock across unchanged, moving the
routine from the post-open slot to **ten minutes before the close**. That breaks the product: the
skill's tiering depends on post-open gaps and first-30-minute volume, none of which exists at
15:50. The roster faithfully reports "15:50", so nothing flags it.

**Recommended: set it back to `50 9 * * 1-5` America/New_York.** Needs your nod, because it is
your scheduled task and the README warns that a concurrent session has been writing to the same
crons.

### D2 — `git add -A` in a shared repo

The README records cron #12 staging **283 deletions** of other crons' files on 2026-10-25. My eight
commits show `deletions=0`, so nothing was lost — but my first commit did use `git add -A` and
pulled `.plugin-cache/` and `.skills/` junk into the shared repo. Untidied, not harmful.

Going forward I'll use the documented procedure: git worktree of `origin/main`, `git add <own-dir>`
only, abort on any staged deletion, push `HEAD:main`, verify with `git cat-file -e`.

---

## 6. Decisions needed

1. **Fix cron #17 back to 09:50 ET?** (D1) — I recommend yes.
2. **n8n lane: in or not?** My recommendation is **yes but narrow** — one workflow, two jobs:
   Grok → catalyst JSON, and (optionally) a Finviz-class relay. Both land in the outputs repo via
   GitHub. Skip it entirely if you don't want a repo PAT in n8n; the bridge + scanner + EDGAR path
   is already sufficient for everything except the 09:00–09:50 news gap.
3. **Who applies the scheduler change?** The deployed prompt is a byte-for-byte mirror of the repo
   file, so a repo edit alone does not change the live task — that needs `cron_update`, and the
   `task_id` coercion bug in `cron_read`/`cron_update` makes precise targeting unreliable. I can
   do the repo-side work immediately; the scheduler-side change needs either the real task_id
   confirmed or a manual click.

---

## 7. Execution order

1. Repo: extend `mcp_bridge.py` with pack routing + `market-recap` + `--list-packs`; add
   `market-recap`/`cftc-cot` to the prompt's bridge block; add the new endpoints to the
   RUNTIME-CONTRACT; correct the stale Yahoo-429 claim.
2. Repo: upgrade `01-weekly-mcp-health-check.md` to the three-layer probe.
3. Repo: add `mcp-health/ledger.md` and the `refs/` cross-reference.
4. Scheduler: fix cron #17's schedule to 09:50 ET (D1, pending your nod); stage the weekly health
   check; update the deployed cron #17 prompt with the self-detection probe (B1).
5. n8n: stand up the Grok catalyst workflow → `data/feed/{date}.json` (pending your call).
6. Verify: next live run — confirm the bridge resolves `market-recap` through the published
   `mcp_bridge.py`, the `halted` column returns rows with the market open, and the digest's Source
   health shows the new rows.

**Acceptance bar for step 6:** a digest whose Source health shows `market-recap` as the quote
source with no Yahoo 429, a non-empty halt list, and an EDGAR-confirmed Tier A catalyst.
