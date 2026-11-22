# MCP availability ledger

Append-only. One row per probe run. The **diff** between consecutive rows is the signal —
a weekly file alone only shows Sunday's state.

| date (ET) | catalog state | finance tools | bridge packs OK | HTTP endpoints | changed? |
|---|---|---|---|---|---|
| 2026-10-21 | `catalog_unreachable` | unknown | not probed | not probed | Probe failed: `error: invalid signature` on `connectors/connected-tools/list`. **Not** evidence that no MCPs exist. |
| 2026-10-25 | `catalog_ok total=15` | 0 | not probed | not probed | no change — 13 matrix + 2 email only |
| 2026-10-31 | `catalog_ok total=133` | 0 | market-recap, stocktwits, shibui, tradier, fmp | Yahoo 200, TV scanner 200, Nasdaq 200, EDGAR 200 | **+118 `connector__github__*` tools.** Still 0 financial MCPs. Yahoo JSON no longer 429 (contract corrected). |
| 2026-11-01 | `catalog_ok total=133` | 0 | market-recap, stocktwits, shibui, tradier, fmp, cftc-cot | bridge 200, Yahoo chart 200, Yahoo screener 200, TV scanner 200, Nasdaq 200, EDGAR 200, Treasury CSV 200, CoinGecko 200 | no change — same 133-tool catalog (118 github / 13 matrix / 2 email), 0 financial MCPs, all 6 packs answer, 8/8 endpoints 200. Refinements only: exact pack tool counts now measured (tradier 47, fmp 68, cftc-cot 47), and `get_quotes` confirmed to exist in market-recap only — a `get_quotes` request to the stocktwits pack is silently routed to market-recap. |
| 2026-11-08 | `catalog_ok total=135` | 0 | market-recap, stocktwits, shibui, tradier, fmp, cftc-cot | bridge 200, Yahoo chart 200, Yahoo screener 200, TV scanner 200, Nasdaq 200, EDGAR 200, Treasury CSV 200, CoinGecko 200 | **+2 `connector__matrix__*` tools (13→15); github 118 and email 2 unchanged. Still 0 financial MCPs.** stdio unchanged — `tradingview-mcp` 73 tools, `financekit-mcp` 17 tools. All 6 packs answer with identical tool counts (48/53/12/47/68/47), 8/8 endpoints 200. New finding: Nasdaq market movers rejects a non-browser UA (curl exit 92, **no output file written**) — a browser UA is required; the fleet's own scripts already send one. shibui tables require the `shibui.` prefix (probe-shape correction, not a service change). |
| 2026-11-15 | `catalog_ok total=135` | 0 | market-recap, stocktwits, shibui, tradier, fmp, cftc-cot — all 6 answer; tool counts 48/53/12/47/68/47 unchanged | bridge 200, **Yahoo chart 429**, **Yahoo screener 429**, TV scanner 200, **Nasdaq 200 but `data:null` (vendor 3004)**, EDGAR 200, Treasury CSV 200, CoinGecko 200 | **Yahoo chart + screener 200 → 429** — unreachable from this egress in every request shape (the `getcrumb` endpoint itself answers with the literal body `Too Many Requests`, so the cookie+crumb handshake cannot bootstrap). **Nasdaq market movers 200-with-tables → 200-with-null-data** — upstream vendor error 3004, reproduced twice. stdio unchanged — `tradingview-mcp` 73 tools, `financekit-mcp` 17 tools. Still 0 financial MCPs; nothing landed. New probe-shape finding: **Nasdaq answers HTTP 200 with an error body**, so a status-code-only probe reads it as healthy. Quota probe unavailable (no `MINIMAX_API_KEY`) — the 5-hour window headroom was NOT measured (advisory, not an error). Full report: `mcp-health/2026-W46.md`. |
| 2026-11-22 | `catalog_ok total=135` | 0 | **20 packs measured — 16 answer data key-free, 4 key-gated** · key-free: market-recap 48, stocktwits 53, shibui 12, cftc-cot 47, polygon-io 56, tiingo 48, edgar 61, finra 48, finra-fixed-income 46, china-stocks 67, esef-filings 47, rba 48, fred 55, crypto 49, data-sf 47, polymarket 57 · **key-gated**: tradier 47, fmp 68, intrinio 48, marketdata-app 48 | bridge 200, **Yahoo chart 200 (was 429)**, **Yahoo screener 200 (was 429)**, TV scanner 200 (20,409/20,409, complete), **Nasdaq 200 with tables (was `data:null`/vendor 3004)**, EDGAR 200, Treasury CSV 200, CoinGecko 200 | **Yahoo chart + screener 429 → 200 — recovered.** **Nasdaq 200-with-null-data → 200-with-tables — recovered.** stdio unchanged — `tradingview-mcp` 73 tools, `financekit-mcp` 17 tools. Still 0 financial MCPs in the platform catalog. **Pack inventory expanded 6 → 20** — `--list-packs` is relevance-ranked, and six discovery queries surfaced 14 packs this check had never measured; 16 answer real data with **no user key** (polygon-io `grouped_daily` returns 12,688 symbols for 2026-11-20 in ONE call). Gateway quota tier measures **2000 calls/day** (`byo`), not the 200 the contract documents. Quota probe unavailable (no `MINIMAX_API_KEY`) — 5-hour window headroom NOT measured (advisory, not an error). Full report: `mcp-health/2026-W47.md`. |

## Reading this table

- `catalog_ok total=N finance_tools=0` — catalog healthy, no financial MCP registered yet.
- `catalog_ok total=N finance_tools=K` — a financial MCP landed. Every digest routine should
  switch its source stack to it.
- `catalog_unreachable` — the probe failed. **Never** read this as "no MCPs exist".

## Bridge packs seen (2026-10-31)

| pack | endpoint | tools | notes |
|---|---|---|---|
| `market-recap` | `gateway.pipeworx.io/market-recap/mcp` | 48 | `get_quotes`, `top_movers`, `market_snapshot`, `price_history`. Yahoo-sourced, not rate-limited. |
| `stocktwits` | `gateway.pipeworx.io/stocktwits/mcp` | 53 | chart_data, sentiment, trending |
| `shibui` | `mcp.shibui.finance/mcp` | 12 | history to 1962, fundamentals, screeners, EDGAR |
| `tradier` | `gateway.pipeworx.io/tradier/mcp` | 1+ | `tradier_quote` |
| `cftc-cot` | `gateway.pipeworx.io/cftc-cot/mcp` | — | CFTC positioning |
| `fmp` | `gateway.pipeworx.io/fmp/mcp` | — | `stock_screener` — **needs the user's own FMP API key** as `_apiKey` |

Discover packs with `python3 mcp_bridge.py --list-packs`.

**Note added 2026-11-01:** `--list-packs` is query-dependent and returns a relevance-ranked sample,
not an inventory — the default query surfaced only 3 of the 6 live packs this run. Confirm a pack by
calling its own tool. Exact tool counts measured 2026-11-01 (`tradier` 47, `fmp` 68, `cftc-cot` 47)
and the full pack/endpoint tables are in `mcp-health/2026-W44.md`.

**Note added 2026-11-08:** two probe-shape traps, both confirmed by measurement. (1)
`api.nasdaq.com/api/marketmovers` **requires a browser-like User-Agent** — with a plain
`mavis-health-check/1.0` UA curl exits **92** (`HTTP/2 stream 1 was not closed cleanly:
INTERNAL_ERROR`) and **writes no output file**, so a file-existence check would read it as "no
data" rather than "probe failed"; `--http1.1` times out instead. The fleet's own scripts already
send browser UAs. (2) shibui SQL **must** qualify tables as `shibui.<table>` — the tool's own
`inputSchema` has always required it, and an unqualified `FROM stock_quotes` fails with *"Table
with name stock_quotes does not exist"*. Full report: `mcp-health/2026-W45.md`.


**Note added 2026-11-15:** two probe-shape traps, both confirmed by measurement. (1)
`api.nasdaq.com/api/marketmovers` now answers **HTTP 200 with `data: null`** and a vendor error
`{"code":3004,"errorMessage":"Error while calling vendor"}` (150 B) — the endpoint is UP and its
**upstream vendor is failing**. Reproduced twice with different browser UAs and `Accept` headers,
so this is NOT the 2026-11-08 User-Agent trap. **A status-code-only probe records it as healthy**,
and any routine reading it then publishes an empty movers board instead of an error. Check the
body, not the status code. (2) The routine's own step-2 sample loop calls `get_quotes` on the
**`shibui`** pack, which has no such tool and answers `Unknown tool: 'get_quotes'` — shibui's
real tool is `stock_data_query` (and its SQL must qualify tables as `shibui.<table>`); measured
directly this run, shibui is **alive** (`[{"1":1}]`). The sample loop would report a healthy pack
as broken.

Also recorded 2026-11-15: **Yahoo was unreachable (429) from this egress in every request
shape** — bare curl, browser UA on both `query1` and `query2`, the full cookie+crumb handshake
(the `getcrumb` endpoint itself answers with the literal body `Too Many Requests`), and the
no-crumb screener. That is a **per-egress flip, not a standing block** — on 2026-11-08 both
Yahoo surfaces answered 200 with data. And the **Token Plan quota probe could not run at all**
(`MINIMAX_API_KEY` is not in the cron sandbox's environment), so the 5-hour window headroom is
**UNKNOWN** for this week, which is not the same as healthy. Full report:
`mcp-health/2026-W46.md`.
