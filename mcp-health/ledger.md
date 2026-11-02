# MCP availability ledger

Append-only. One row per probe run. The **diff** between consecutive rows is the signal —
a weekly file alone only shows Sunday's state.

| date (ET) | catalog state | finance tools | bridge packs OK | HTTP endpoints | changed? |
|---|---|---|---|---|---|
| 2026-10-21 | `catalog_unreachable` | unknown | not probed | not probed | Probe failed: `error: invalid signature` on `connectors/connected-tools/list`. **Not** evidence that no MCPs exist. |
| 2026-10-25 | `catalog_ok total=15` | 0 | not probed | not probed | no change — 13 matrix + 2 email only |
| 2026-10-31 | `catalog_ok total=133` | 0 | market-recap, stocktwits, shibui, tradier, fmp | Yahoo 200, TV scanner 200, Nasdaq 200, EDGAR 200 | **+118 `connector__github__*` tools.** Still 0 financial MCPs. Yahoo JSON no longer 429 (contract corrected). |
| 2026-11-01 | `catalog_ok total=133` | 0 | market-recap, stocktwits, shibui, tradier, fmp, cftc-cot | bridge 200, Yahoo chart 200, Yahoo screener 200, TV scanner 200, Nasdaq 200, EDGAR 200, Treasury CSV 200, CoinGecko 200 | no change — same 133-tool catalog (118 github / 13 matrix / 2 email), 0 financial MCPs, all 6 packs answer, 8/8 endpoints 200. Refinements only: exact pack tool counts now measured (tradier 47, fmp 68, cftc-cot 47), and `get_quotes` confirmed to exist in market-recap only — a `get_quotes` request to the stocktwits pack is silently routed to market-recap. |

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
