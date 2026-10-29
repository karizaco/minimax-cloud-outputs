# Pre-Market Gapper — 2026-10-21  (NO DATA — SKILL FETCH FAILED)

**Run time (ET):** 2026-10-21 21:34 EDT  
**Result: DEGRADED — no pre-market gapper rows produced.**  
**`_source=skill_fetch_failed`**

## Why this run is empty

Per CRITICAL REMINDER #1, the skill spec must be fetched first and the procedure must **not**
be improvised from memory. The fetch failed, so this stub is the artifact.

| Attempt | Target | Result |
|---|---|---|
| 1 | `curl raw.githubusercontent.com/.../stock-screener-suite/SKILL.md` | HTTP 000, 0 bytes |
| 2 | `curl` retried with 20s timeout + status code | HTTP 000, 0 bytes |
| 3 | `web_fetch` on the same URL | archon-server request timed out after 15000ms |

## Sandbox egress status (diagnostic)

DNS resolves fine, but **all outbound HTTPS is failing** — this is a sandbox-level network
outage, not a host-specific block:

| Host | Result |
|---|---|
| `example.com` (control) | HTTP 000 |
| `github.com` | HTTP 000 |
| `raw.githubusercontent.com` | HTTP 000 |
| `scanner.tradingview.com` (DNS OK: 18.165.83.x) | HTTP 000 |
| `query1.finance.yahoo.com` | HTTP 000 |

Yesterday's run (2026-10-20) failed for a *different* reason: TradingView scanner returned
HTTP 000 while Yahoo's chart endpoint still returned HTTP 200, i.e. a host-level block.
Today the control host is also down, which means the failure has escalated to full egress loss.

## Criteria that WOULD have been applied (carried over for continuity, not re-derived from a fetched spec)
- Pre-market change > **+4%**
- Pre-market volume > **50,000** shares
- Universe: US-listed equities (NYSE / NASDAQ / AMEX)
- Preferred source: TradingView public scanner `POST https://scanner.tradingview.com/america/scan`
  (columns: name, close, premarket_change, premarket_volume, premarket_gap, volume,
  market_cap_basic, sector, industry; filter premarket_change > 4 ∧ premarket_volume > 50000)
- Fallback 1: Finviz `f=sh_avgvol_o1000,ta_premarket_up`
- Fallback 2: Yahoo pre/post screener `query1.finance.yahoo.com/v1/finance/screener/pre/post`

## Top movers
none — 0 rows. Nothing was screened.
