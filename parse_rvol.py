#!/usr/bin/env python3
"""Cron #7 - focus RVOL snapshot (09:45 ET).

Primary path: Yahoo Finance chart API (5m, range=1d) for the intraday numerator,
TradingView public scanner average_volume_10d_calc for the 10d average-volume denominator.
The Yahoo chart API rejects unauthenticated requests with HTTP 429, so a fc.yahoo.com
cookie jar plus a /v1/test/getcrumb crumb is established first.
"""
import datetime as dt
import gzip
import http.cookiejar
import io
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

OUT = "/workspace/data/rvol"
os.makedirs(OUT, exist_ok=True)

SESSION_OPEN = dt.time(9, 30)
SESSION_CLOSE = dt.time(16, 0)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ---------------------------------------------------------------- http plumbing
class Yahoo:
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        ctx = ssl.create_default_context()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.jar),
            urllib.request.HTTPSHandler(context=ctx),
        )
        self.crumb = None
        self.errors = []

    def _get(self, url, retry_429=True):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "application/json,text/plain,*/*",
            "Accept-Language": "en-US,en;q=0.9",
        })
        try:
            with self.opener.open(req, timeout=30) as r:
                body = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    body = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
                return r.status, body.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, ""
        except Exception as e:  # noqa: BLE001
            self.errors.append(f"{url}: {e}")
            return 0, ""

    def handshake(self):
        # fc.yahoo.com returns 404 but still sets the cookie jar.
        st, _ = self._get("https://fc.yahoo.com/")
        log(f"  cookie seed http={st}")
        st, crumb = self._get("https://query1.finance.yahoo.com/v1/test/getcrumb")
        crumb = crumb.strip()
        if st != 200 or len(crumb) < 8 or "{" in crumb or "<" in crumb:
            self.crumb = None
            self.errors.append(f"crumb fetch failed http={st} body={crumb[:80]!r}")
            return False
        self.crumb = crumb
        log(f"  crumb ok ({len(crumb)} chars)")
        return True

    def chart(self, symbol):
        base = "https://query1.finance.yahoo.com/v8/finance/chart/" + symbol
        params = "?interval=5m&range=1d&includePrePost=false"
        if self.crumb:
            params += "&crumb=" + urllib.parse.quote(self.crumb)
        st, body = self._get(base + params)
        if st == 429 and retry_429:
            log(f"  {symbol}: 429, refreshing crumb and retrying once")
            time.sleep(1.5)
            if self.handshake():
                params = "?interval=5m&range=1d&includePrePost=false&crumb=" + urllib.parse.quote(self.crumb)
                st, body = self._get(base + params)
        if st != 200:
            self.errors.append(f"{symbol}: chart http={st}")
            return None
        try:
            return json.loads(body)
        except Exception as e:  # noqa: BLE001
            self.errors.append(f"{symbol}: json {e}")
            return None


import urllib.parse  # noqa: E402  (used above)


# ---------------------------------------------------------------- tv scanner
def tv_scan(symbols):
    """One POST for the whole batch; returns {name: row-dict}.

    The scanner response is {"totalCount": N, "data": [{"s": "NASDAQ:ORKA", "d": [...]}]}.
    There is NO "columns" array in the response -- each row's "d" is positional and
    matches the order of the requested columns. (Parsing it as if "columns" were
    present silently collapses every row to a single empty record.)
    """
    columns = [
        "name", "description", "exchange", "close", "volume",
        "average_volume_10d_calc", "relative_volume_10d_calc",
    ]
    body = {
        "filter": [
            # NB: an "active_symbol" filter is rejected by the scanner with HTTP 400.
            {"left": "name", "operation": "in_range", "right": symbols},
            {"left": "type", "operation": "equal", "right": "stock"},
        ],
        "options": {"lang": "en"},
        "markets": ["america"],
        "columns": columns,
        "range": [0, 200],
        "sort": {"sortBy": "name", "sortOrder": "asc"},
    }
    req = urllib.request.Request(
        "https://scanner.tradingview.com/america/scan",
        data=json.dumps(body).encode(),
        headers={
            "User-Agent": UA,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": "https://www.tradingview.com",
            "Referer": "https://www.tradingview.com/",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            payload = json.loads(r.read().decode())
    except Exception as e:  # noqa: BLE001
        log(f"  TV scan failed: {e}")
        return {}
    resp_cols = payload.get("columns") or columns
    out = {}
    for row in payload.get("data", []) or []:
        d = row.get("d") or []
        if not d:
            continue
        rec = dict(zip(resp_cols, d))
        rec["tv_symbol"] = row.get("s")
        out.setdefault(rec.get("name"), rec)
    log(f"  TV scan returned {len(out)} rows for {len(symbols)} requested "
        f"(totalCount={payload.get('totalCount')})")
    return out


# ---------------------------------------------------------------- rvol parse
def parse_chart(payload, session_date):
    """Returns dict with close, cum_volume, bars, timestamps, flags."""
    res = payload.get("chart", {}).get("result")
    if not res:
        err = (payload.get("chart", {}).get("error") or {}).get("description")
        return {"status": "no_intraday_bars", "error": err}
    r = res[0]
    meta = r.get("meta", {}) or {}
    ts = r.get("timestamp") or []
    q = ((r.get("indicators", {}) or {}).get("quote") or [{}])[0]
    vols = q.get("volume") or []
    closes = q.get("close") or []

    rows = []
    dropped_future = 0
    dropped_outside = 0
    for i, t in enumerate(ts):
        v = vols[i] if i < len(vols) else None
        c = closes[i] if i < len(closes) else None
        d = dt.datetime.fromtimestamp(t, ET)
        if d.date() > session_date:
            dropped_future += 1
            continue
        if d.date() != session_date:
            dropped_outside += 1
            continue
        if not (SESSION_OPEN <= d.time() <= SESSION_CLOSE):
            dropped_outside += 1
            continue
        rows.append((d, v, c))

    if not rows:
        return {
            "status": "no_intraday_bars",
            "bars": 0,
            "dropped_future": dropped_future,
            "dropped_outside": dropped_outside,
            "regular_market_time": meta.get("regularMarketTime"),
            "exchange_tz": meta.get("exchangeTimezoneName"),
            "prev_close": meta.get("chartPreviousClose") or meta.get("previousClose"),
            "meta_price": meta.get("regularMarketPrice"),
        }

    cum = 0.0
    for _, v, _c in rows:
        if v is not None:
            cum += float(v)
    last_c = None
    for _d, _v, c in rows:
        if c is not None:
            last_c = c
    rmt = meta.get("regularMarketTime")
    return {
        "status": "ok",
        "bars": len(rows),
        "cum_volume": cum,
        "close": last_c,
        "first_bar": rows[0][0].strftime("%Y-%m-%d %H:%M:%S"),
        "last_bar": rows[-1][0].strftime("%Y-%m-%d %H:%M:%S"),
        "last_bar_volume": rows[-1][1],
        "dropped_future": dropped_future,
        "dropped_outside": dropped_outside,
        "regular_market_time": (dt.datetime.fromtimestamp(rmt, ET).strftime("%Y-%m-%d %H:%M:%S")
                                if rmt else None),
        "exchange_tz": meta.get("exchangeTimezoneName"),
        "prev_close": meta.get("chartPreviousClose") or meta.get("previousClose"),
        "meta_price": meta.get("regularMarketPrice"),
    }


def main():
    focus_csv = sys.argv[1] if len(sys.argv) > 1 else "/workspace/daily-screens/2026-10-26/focus.csv"
    session_date = dt.datetime.now(ET).date()
    import csv
    with open(focus_csv) as fh:
        focus = list(csv.DictReader(fh))
    symbols = [r["name"] for r in focus]
    prior_rvol = {r["name"]: r.get("rvol10") for r in focus}
    print(f"focus: {len(symbols)} symbols, session_date={session_date}", file=sys.stderr)

    y = Yahoo()
    if not y.handshake():
        log("handshake failed: " + "; ".join(y.errors))

    tv = tv_scan(symbols)

    results = []
    for i, sym in enumerate(symbols):
        p = y.chart(sym)
        info = parse_chart(p, session_date) if p else {"status": "no_intraday_bars", "error": "no payload"}
        tvrow = tv.get(sym) or {}
        avg10 = tvrow.get("average_volume_10d_calc")
        info["symbol"] = sym
        info["avg_volume_10d"] = avg10
        info["tv_exchange"] = tvrow.get("exchange")
        info["tv_description"] = tvrow.get("description")
        info["tv_relative_volume_10d"] = tvrow.get("relative_volume_10d_calc")
        info["prior_rvol10_upstream"] = prior_rvol.get(sym)
        if info["status"] == "ok" and avg10:
            info["rvol"] = info["cum_volume"] / float(avg10)
        else:
            info["rvol"] = None
        results.append(info)
        log(f"  {sym}: bars={info.get('bars')} cumvol={info.get('cum_volume')} "
            f"avg10={avg10} rvol={info.get('rvol')}")
        if i < len(symbols) - 1:
            time.sleep(1.0)

    out = {
        "generated_et": dt.datetime.now(ET).strftime("%Y-%m-%d %H:%M:%S"),
        "session_date": str(session_date),
        "focus_csv": focus_csv,
        "yahoo_errors": y.errors,
        "results": results,
    }
    path = os.path.join(OUT, f"rvol_{session_date}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(path)


if __name__ == "__main__":
    main()
