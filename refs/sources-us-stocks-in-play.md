# Sources — us-stocks-in-play (cron #17)

Tested from the cloud sandbox on 2026-10-25 (Saturday — market closed, so live-only
behaviour could not be confirmed for every source). Status is what the **source actually
returned**, not what it is documented to do.

Evidence base: 9 completed runs of cron #17 (2026-10-13 → 2026-10-23) plus a reconstruction
of three missed fires, and a direct probe of every candidate below.

---

## Repo gotcha — `refs/` is gitignored

The cloud sandbox `.gitignore` excludes `refs/` (line 4), so a plain `git add -A` silently
skips anything written here — `git commit` then reports *"nothing to commit, working tree
clean"* and the file never lands. The existing `refs/*.md` were force-added.

```bash
git add -f refs/<file>.md
git commit -m "..."
git push origin main
```

Verify with `git ls-tree -r --name-only origin/main | grep refs/`.

---

## Working — add these

| Source | Endpoint | Returns | Why it matters |
|---|---|---|---|
| **TradingView scanner** | `POST https://scanner.tradingview.com/america/scan` | movers, `change`, `volume`, `average_volume_10d_calc`, **`relative_volume_10d_calc`**, `market_cap_basic`, **`halted`**, `exchange`, **`premarket_change` / `premarket_volume` / `premarket_close`** | Replaces three broken feeds with one call. No auth. |
| **Yahoo quoteSummary + crumb** | `https://query1.finance.yahoo.com/v10/finance/quoteSummary/<SYM>?modules=defaultKeyStatistics,summaryDetail&crumb=<CRUMB>` | `averageVolume`, `sharesOutstanding`, **`floatShares`**, `marketCap`, **`shortRatio`**, `fiftyTwoWeekHigh/Low` | Makes the skill's own "low float (<10–20M): flag, don't auto-promote" rule enforceable from data instead of from news copy. Adds a short-interest signal. |
| **SEC EDGAR full-text search** | `https://efts.sec.gov/LATEST/search-index?q=<Q>&forms=8-K&startdt=<D>&enddt=<D>` | 8-K hits with filing date, form, CIK, accession no. | Primary-source confirmation of the Tier A catalyst, and the skill already lists EDGAR in Pass 3 — it was simply never wired in. |
| **SEC EDGAR ticker→CIK map** | `https://www.sec.gov/files/company_tickers.json` | ticker → CIK + name | Lookup key for the per-company feed. Verified: BRZE `0001676238`, CRM `0001108524`, LQDA `0001819576`, UTHR `0001082554`, OPK `0000944809`, SKYD `0002041610`, CLF `0000764065`. |
| **SEC EDGAR per-company 8-K Atom** | `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK>&type=8-K&owner=include&count=10&output=atom` | filing date, type, accession no. per filing | Item-level read on 1.01 / 2.01 / 5.02 / 7.01 / 8.01. |
| **Yahoo options chain + crumb** | `https://query2.finance.yahoo.com/v7/finance/options/<SYM>?crumb=<CRUMB>` | IV, strikes, expiry, implied move | A real "is this name actually in play" test — implied vs realised. |

**SEC requires a descriptive User-Agent.** Use something like
`MaxHermes Research maxhermes@example.com`. A generic browser UA is against SEC policy.

### The crumb recipe (both steps required)

```bash
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
curl -s -c ck.txt -A "$UA" "https://fc.yahoo.com" -o /dev/null   # 404 but SETS the cookies
CRUMB=$(curl -s -b ck.txt -A "$UA" "https://query1.finance.yahoo.com/v1/test/getcrumb")
curl -s -b ck.txt -A "$UA" \
  "https://query1.finance.yahoo.com/v10/finance/quoteSummary/EFX?modules=defaultKeyStatistics,summaryDetail&crumb=$CRUMB"
```

`fc.yahoo.com` returning **404 is expected** — it still sets the cookie jar. The 404 is not a
failure signal here; check the crumb, not the status of the cookie request.

### TradingView scanner body

```bash
curl -s -X POST "https://scanner.tradingview.com/america/scan" \
  -H "Content-Type: application/json" -A "$UA" -d '{
  "filter":[
    {"left":"type","operation":"equal","right":"stock"},
    {"left":"active_symbol","operation":"equal","right":true},
    {"left":"exchange","operation":"in_range","right":["NASDAQ","NYSE","AMEX"]},
    {"left":"volume","operation":"egreater","right":500000}],
  "columns":["name","description","close","change","volume",
             "average_volume_10d_calc","relative_volume_10d_calc",
             "market_cap_basic","halted","exchange",
             "premarket_change","premarket_volume","premarket_close"],
  "sort":{"sortBy":"volume","sortOrder":"desc"},"range":[0,100]}'
```

**Cross-check that passed.** For the 2026-10-23 session the scanner's premarket columns
independently returned CCI `pm_chg +17.20% @ $92.39` and AMT `+11.25% @ $202.00` — matching
TheStockCatalyst's `+16.58% @ $91.90` and `+11.25% @ $202.00`. Two independent PM feeds, same
numbers. That is the value: PM is currently a single point of failure.

**Caveats.**
- The scanner's `halted` filter returned `total: 0` and the `halted` column returned `None`
  for every row — **but the market was closed (Saturday) when tested.** The filter is
  syntactically accepted; whether it returns live halt rows is **unverified**. Validate on the
  next live session before relying on it to close the halt blind spot.
- Sorting by `relative_volume_10d_calc` surfaces microcap junk (AIOK, BOLT, CLRO). Apply the
  skill's own floors — dollar volume, price, market cap — or the RVol sort is noise.
- `totalCount` for US-exchange + vol>500k was 2,412; premarket movers >100k vol was 175.

---

## Dead — stop spending calls on these

| Source | Observed | Notes |
|---|---|---|
| **Finviz screener** | 403 → 000 → 503 → 403 across 4 runs | Never worked once. The 503 body was an upstream TLS `CERTIFICATE_VERIFY_FAILED` from the sandbox egress proxy, not a Finviz block — but either way it is unreachable. |
| **NASDAQ Trade Halt RSS** | HTTP 200, **0 RSS items**, 6/6 attempts | Serves an HTML XHTML shell, byte-identical every time. |
| `api.nasdaq.com/api/quote-list/halt-directory` | 404 (with and without `exchange`) | Path is wrong or gone. |
| `nasdaqtrader.com/Trader.aspx?id=TradeHalts` | HTTP 200 but **0 table rows** | JS-rendered; not scrapeable via HTTP. |
| **StockTitan** | DNS failure, 2/2 | `stocktitan.net` does not resolve. |
| **Barchart** | 000, 1/1 | Connection failure. |
| **Yahoo quoteSummary without crumb** | 401, 9/9 | Fixed by the crumb recipe above. |
| EDGAR daily index | 403 | Use the full-text search endpoint instead. |
| EDGAR Atom `browse-edgar` with a **numeric** CIK | 403 | Pad the CIK to 10 digits with leading zeros. |

---

## Still unavailable — and it cannot be fixed

| Gap | Why |
|---|---|
| **Historical pre-market feed** | No free source serves PM history. This is structural, not a block. Any reconstruction of a past session is missing its PM annex permanently. |
| **Historical LULD halts** | No free source serves halt history. The 2026-10-14 reconstruction could not evidence SKYD's pre-market halt except from wire copy. |

---

## Coverage the skill assumes but the cloud cannot provide

The skill's Pass 1 lists Finviz, Pass 1b lists Barchart, Pass 3 lists the NASDAQ halt RSS. In
this runtime **all three are dead**, and the TradingView-advanced / Yahoo MCPs named in the
cron prompt are not in the session tool list (connector catalog: 15 tools, zero
finance/trading matches).

That means the digest's discovery path has been Yahoo-JSON-only since 2026-10-13, and its
halt feed has never worked. Every digest in this series therefore carries an
"unverified halts" caveat. The additions above are what would remove it.

---

## Recommended insertion points in the skill procedure

| Skill step | Add |
|---|---|
| Pass 1 (movers) | TradingView scanner as a second discovery path alongside Yahoo JSON; use `relative_volume_10d_calc` for RVol instead of deriving it from `averageDailyVolume3Month`. |
| Pass 1b (premarket) | TradingView scanner `premarket_*` columns as the second PM source; TheStockCatalyst stays primary. |
| Pass 2 (confirm) | Yahoo quoteSummary + crumb for float, shares outstanding, short ratio, 52-week range. |
| Pass 3 (catalysts) | EDGAR full-text search + per-company 8-K Atom, replacing the Finviz-news leg. Filter on items 1.01 / 2.01 / 5.02 / 7.01 / 8.01. |
| Pass 3 (halts) | TradingView scanner `halted` column, **pending live validation**. |
| Optional | Yahoo options chain for implied-vs-realised move. |

**Highest-value single change:** EDGAR. It is already in the skill spec, it works from this
sandbox, and it would have converted the BRZE inference on 2026-10-13 (deal terms read off
wire copy) into a filing-confirmed fact on the day.
