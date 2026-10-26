#!/usr/bin/env python3
"""qa_and_crosscheck.py — cron #5 international EOD QA + Yahoo verification.

QA (per region CSV):
  header, width, N/A-style cells, duplicate tickers, OHLC consistency,
  blank-field census, movers with a market-cap floor.

Cross-check (Yahoo Finance /v8/finance/chart):
  Drift-proof comparison. For each sampled row:
    tv_ref   = tv_close / (1 + tv_change/100)      (implied prior close)
    yh_ref   = prior session close from the Yahoo daily bar series
    yh_close = today's Yahoo close (last bar / meta.regularMarketPrice)
  * `ref_agrees`  -> |tv_ref - yh_ref| / yh_ref < 0.3%  => the screener's
    change_pct was measured against the TRUE prior close (not a stale one)
  * `price_agrees`-> |tv_close - yh_close| / yh_close < 0.3%
  * `stale`       -> the Yahoo series has no bar for 2026-10-26 in the
    region's local zone => the symbol did not trade today
  A direct % comparison is NOT used: it produces false alarms whenever the
  live tape moves between the two snapshots.
"""
from __future__ import annotations

import csv
import json
import os
import random
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
UA = "Mozilla/5.0"
DATE = os.environ.get("EOD_DATE", "2026-10-26")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"
NA_TOKENS = {"n/a", "na", "none", "null", "-", "--"}
HEADER = ["date", "ticker", "name", "open", "high", "low", "close", "volume",
          "change_pct", "market_cap", "pe_ratio", "sector", "currency", "exchange"]

# region -> (exchange offset hours, {TV venue -> Yahoo suffix})
REGION_MAP = {
    "au":    (10, {"ASX": ".AX"}),
    "jp":    (9,  {"TSE": ".T", "NAG": ".T", "FSE": ".T", "SAPSE": ".T"}),
    "ca":    (-4, {"TSX": ".TO", "TSXV": ".V", "NEO": ".NE", "CSE": ".CN"}),
    "eu-de": (2,  {"XETR": ".DE"}),
    "eu-fr": (2,  {"EPA": ".PA"}),
    "eu-it": (2,  {"MIL": ".MI"}),
    "eu-es": (2,  {"BME": ".MC"}),
    "eu-nl": (2,  {"AMS": ".AS"}),
    "eu-be": (2,  {"BSE": ".BR"}),
    "eu-pt": (2,  {"LIS": ".LS"}),
    "eu-fi": (2,  {"HEL": ".HE"}),
    "eu-dk": (2,  {"CPH": ".CO"}),
    "eu-gr": (3,  {"ATHEX": ".AT", "ATH": ".AT"}),
}
# FX to USD (fetched from Yahoo, filled at runtime)
FX = {"EUR": None, "JPY": None, "AUD": None, "CAD": None}


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def curl_json(url: str, timeout: int = 30):
    cmd = ["curl", "-sS", "--max-time", str(timeout), "--cacert", CA,
           "-A", UA, url]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl {p.returncode}")
    return json.loads(p.stdout)


def yahoo_chart(sym: str):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?range=7d&interval=1d")
    doc = curl_json(url)
    res = (doc.get("chart") or {}).get("result")
    if not res:
        raise RuntimeError("no result")
    r = res[0]
    meta = r.get("meta") or {}
    ts = r.get("timestamp") or []
    closes = ((r.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []
    bars = [(t, c) for t, c in zip(ts, closes) if c is not None]
    return {"meta": meta, "bars": bars}


def fetch_fx():
    pairs = {"EUR": "EURUSD=X", "JPY": "USDJPY=X", "AUD": "AUDUSD=X",
             "CAD": "USDCAD=X"}
    for cur, sym in pairs.items():
        try:
            d = yahoo_chart(sym)
            bars = d["bars"]
            if not bars:
                continue
            last = bars[-1][1]
            FX[cur] = last if cur != "JPY" else 1.0 / last
        except Exception as e:  # noqa: BLE001
            print(f"  FX {cur} failed: {str(e)[:60]}")
    print("FX:", {k: (round(v, 5) if v else None) for k, v in FX.items()})


def to_usd(mcap, ccy):
    if mcap is None or not ccy or not FX.get(ccy):
        return None
    return mcap * FX[ccy]


def yahoo_symbol(tv: str, suffix_map: dict) -> str | None:
    if ":" not in tv:
        return None
    venue, sym = tv.split(":", 1)
    suf = suffix_map.get(venue)
    if not suf:
        return None
    sym = sym.replace(".", "-")
    return f"{sym}{suf}"


def main() -> int:
    print("== FX table ==")
    fetch_fx()

    problems, summary = [], {}
    allrows = {}
    for region in sorted(REGION_MAP):
        path = f"{OUT}/{region}.csv"
        if not os.path.exists(path):
            problems.append(f"{region}: MISSING {path}")
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            rd = csv.reader(fh)
            head = next(rd)
            rows = list(rd)
        if head != HEADER:
            problems.append(f"{region}: header mismatch")
        bad_w = sum(1 for r in rows if len(r) != len(HEADER))
        if bad_w:
            problems.append(f"{region}: {bad_w} rows with wrong width")
        na = sum(1 for r in rows for c in r if c.strip().lower() in NA_TOKENS)
        if na:
            problems.append(f"{region}: {na} N/A-style cells")
        d = {h: i for i, h in enumerate(head)}
        dupes = len(rows) - len({r[d["ticker"]] for r in rows})
        if dupes:
            problems.append(f"{region}: {dupes} duplicate tickers")
        bad_ohlc = 0
        for r in rows:
            o, h, l, c = (num(r[d[k]]) for k in ("open", "high", "low", "close"))
            if None in (o, h, l, c):
                continue
            if h < max(o, l, c) - 1e-9 or l > min(o, h, c) + 1e-9:
                bad_ohlc += 1
        if bad_ohlc:
            problems.append(f"{region}: {bad_ohlc} rows with inconsistent OHLC")
        recs = []
        for r in rows:
            recs.append({
                "ticker": r[d["ticker"]], "name": r[d["name"]],
                "close": num(r[d["close"]]), "change": num(r[d["change_pct"]]),
                "volume": num(r[d["volume"]]),
                "mcap": num(r[d["market_cap"]]), "ccy": r[d["currency"]],
                "sector": r[d["sector"]], "venue": r[d["exchange"]],
            })
        allrows[region] = recs
        for rec in recs:
            rec["mcap_usd"] = to_usd(rec["mcap"], rec["ccy"])
        liquid = [x for x in recs if (x["mcap_usd"] or 0) >= 5e9]
        liquid.sort(key=lambda x: -(x["change"] if x["change"] is not None else 0))
        summary[region] = {
            "rows": len(rows), "dupes": dupes, "bad_ohlc": bad_ohlc,
            "with_change": sum(1 for x in recs if x["change"] is not None),
            "liquid_rows": len(liquid),
            "up_3": sum(1 for x in recs if (x["change"] or 0) >= 3),
            "dn_3": sum(1 for x in recs if (x["change"] or 0) <= -3),
            "up_3_liquid": sum(1 for x in liquid if (x["change"] or 0) >= 3),
            "dn_3_liquid": sum(1 for x in liquid if (x["change"] or 0) <= -3),
            "top_up": liquid[:5], "top_dn": liquid[-5:][::-1],
            "file_kb": round(os.path.getsize(path) / 1024, 1),
        }

    # ---- Yahoo cross-check sample -------------------------------------
    print("== Yahoo cross-check ==")
    tasks = []
    for region, recs in allrows.items():
        withc = [x for x in recs if x["change"] is not None and x["close"]]
        movers = sorted(withc, key=lambda x: -abs(x["change"]))[:12]
        liquid = sorted([x for x in withc if (x["mcap_usd"] or 0) >= 1e9],
                        key=lambda x: -(x["mcap_usd"] or 0))[:18]
        rnd = random.Random(7)
        pool = [x for x in withc if (x["mcap_usd"] or 0) >= 2e8]
        rnd.shuffle(pool)
        picked, seen = [], set()
        for x in movers + liquid + pool[:10]:
            if x["ticker"] in seen:
                continue
            seen.add(x["ticker"])
            picked.append(x)
        for x in picked:
            ys = yahoo_symbol(x["ticker"], REGION_MAP[region][1])
            if ys:
                tasks.append((region, x, ys))

    def run(t):
        region, x, ys = t
        try:
            d = yahoo_chart(ys)
        except Exception as e:  # noqa: BLE001
            return {"region": region, "ticker": x["ticker"], "error": str(e)[:80]}
        meta, bars = d["meta"], d["bars"]
        off = REGION_MAP[region][0]
        last_date = None
        if bars:
            last_date = datetime.fromtimestamp(bars[-1][0], timezone.utc) + \
                timedelta(hours=off)
        yh_close = bars[-1][1] if bars else None
        yh_ref = bars[-2][1] if len(bars) >= 2 else None
        if yh_close is None:
            yh_close = meta.get("regularMarketPrice")
        tv_ref = None
        if x["change"] is not None and x["close"] is not None:
            tv_ref = x["close"] / (1 + x["change"] / 100)
        res = {"region": region, "ticker": x["ticker"], "yahoo": ys,
               "tv_close": x["close"], "tv_change": x["change"],
               "yh_close": yh_close, "yh_ref": yh_ref, "tv_ref": tv_ref,
               "last_bar_local": last_date.isoformat() if last_date else None,
               "stale": bool(last_date and last_date.date().isoformat() != DATE)}
        if tv_ref and yh_ref:
            res["ref_diff_pct"] = abs(tv_ref - yh_ref) / yh_ref * 100
            res["ref_agrees"] = res["ref_diff_pct"] < 0.3
        if x["close"] and yh_close:
            res["price_diff_pct"] = abs(x["close"] - yh_close) / yh_close * 100
            res["price_agrees"] = res["price_diff_pct"] < 0.3
        return res

    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(run, tasks))

    per_region = {}
    for r in results:
        p = per_region.setdefault(r["region"], {
            "attempted": 0, "fetch_error": 0, "ref_agrees": 0, "ref_testable": 0,
            "price_agrees": 0, "price_testable": 0, "stale": 0,
            "ref_diffs": [], "price_diffs": [], "mismatches": []})
        p["attempted"] += 1
        if r.get("error"):
            p["fetch_error"] += 1
            continue
        if r.get("stale"):
            p["stale"] += 1
        if "ref_agrees" in r:
            p["ref_testable"] += 1
            p["ref_diffs"].append(r["ref_diff_pct"])
            if r["ref_agrees"]:
                p["ref_agrees"] += 1
            else:
                p["mismatches"].append(r)
        if "price_agrees" in r:
            p["price_testable"] += 1
            p["price_diffs"].append(r["price_diff_pct"])
            if r["price_agrees"]:
                p["price_agrees"] += 1
    for p in per_region.values():
        for k in ("ref_diffs", "price_diffs"):
            v = sorted(p.pop(k))
            p[k.replace("_diffs", "_median")] = round(v[len(v) // 2], 4) if v else None
            p[k.replace("_diffs", "_max")] = round(v[-1], 4) if v else None

    json.dump({"date": DATE, "fx": FX, "qa": summary,
               "crosscheck": per_region, "crosscheck_rows": results},
              open(f"{DATA}/_qa_intl.json", "w"), indent=1, default=str)

    print(f"files={len(summary)} total_rows={sum(v['rows'] for v in summary.values())}")
    print("PROBLEMS: " + ("; ".join(problems) if problems else "none"))
    for region in sorted(summary):
        s = summary[region]
        up = ", ".join(f"{x['ticker'].split(':')[-1]} {x['change']:+.2f}%" for x in s["top_up"][:3])
        dn = ", ".join(f"{x['ticker'].split(':')[-1]} {x['change']:+.2f}%" for x in s["top_dn"][:3])
        c = per_region.get(region, {})
        print(f"  {region:6s} rows={s['rows']:5d} liq($5b+)={s['liquid_rows']:5d} "
              f"up>=3%={s['up_3']:4d} dn<=-3%={s['dn_3']:4d} | up {up} | dn {dn}")
        print(f"         xcheck n={c.get('attempted')} ref_ok={c.get('ref_agrees')}/{c.get('ref_testable')} "
              f"med|dref|={c.get('ref_median')} max={c.get('ref_max')} "
              f"price_ok={c.get('price_agrees')}/{c.get('price_testable')} "
              f"med|dpx|={c.get('price_median')} stale={c.get('stale')} err={c.get('fetch_error')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
