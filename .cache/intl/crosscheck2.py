#!/usr/bin/env python3
"""crosscheck2.py — cron #5 international EOD: movers + Yahoo verification (v2).

Fixes over v1:
  * Yahoo daily bars are grouped by LOCAL SESSION DATE. Yahoo appends a
    duplicate "live quote" bar (e.g. ASX 10-26 05:13Z) whose close equals the
    session close; taking bars[-2] as the prior close then yields a phantom
    ~1% disagreement. Grouping by local date and taking the last value of
    the previous session group is drift-proof.
  * TradingView EU venue codes are EURONEXT / OMXHEX / OMXCOP (not EPA /
    HEL / CPH), so the v1 venue map silently produced zero cross-check
    coverage for 6 EU regions.
  * DKK added to the FX table (EUR/DKK cross if USDDKK=X is missing).
  * Movers are computed on a common-share subset: the original MCP call
    used stock_type=common, but the TV screener has no such filter, so
    exchange-listed certificates / warrants / funds are classified out.
"""
from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
UA = "Mozilla/5.0"
DATE = os.environ.get("EOD_DATE", "2026-10-26")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"

# region -> (local UTC offset hours, {TV venue -> Yahoo suffix})
REGION_MAP = {
    "au":    (10, {"ASX": ".AX"}),
    "jp":    (9,  {"TSE": ".T", "NAG": ".T", "FSE": ".T", "SAPSE": ".T"}),
    "ca":    (-4, {"TSX": ".TO", "TSXV": ".V", "NEO": ".NE", "CSE": ".CN"}),
    "eu-de": (2,  {"XETR": ".DE", "LSX": ".L", "LS": ".L"}),
    "eu-fr": (2,  {"EURONEXT": ".PA"}),
    "eu-nl": (2,  {"EURONEXT": ".AS"}),
    "eu-be": (2,  {"EURONEXT": ".BR"}),
    "eu-pt": (2,  {"EURONEXT": ".LS"}),
    "eu-fi": (2,  {"OMXHEX": ".HE"}),
    "eu-dk": (2,  {"OMXCOP": ".CO"}),
    "eu-es": (2,  {"BME": ".MC"}),
    "eu-it": (2,  {"MIL": ".MI"}),
    "eu-gr": (3,  {"ATHEX": ".AT", "ATH": ".AT"}),
}
FX = {"EUR": None, "JPY": None, "AUD": None, "CAD": None, "DKK": None}

# Non-common instrument markers (certificates, warrants, funds, trackers).
# Matched against the company name / description, case-insensitively.
NON_COMMON_PAT = re.compile(
    r"\b(warrant|warrants|leveraged|uncapped|capped|turbo|open end|open-end|"
    r"knock ?out|knockout|certificate|certificates|zertifikat|"
    r"tracker|index fund|indexfonds|exchange traded fund|\betf\b|"
    r"fonds|fund\b|etf\b|basket|bond\b|notes?\b|"
    r"equity linked|equity-linked|inflation linked|"
    r"depositary receipt|adr\b|gdx|gold share)\b", re.I)
# ISIN-like / purely numeric symbols are certificates or funds, not common shares
NON_COMMON_SYM = re.compile(r"^[0-9]{4,}$|^[A-Z0-9]{6}$")


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def curl_json(url: str, timeout: int = 30):
    cmd = ["curl", "-sS", "--max-time", str(timeout), "--cacert", CA, "-A", UA, url]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl {p.returncode}")
    return json.loads(p.stdout)


def yahoo_chart(sym: str):
    doc = curl_json(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
                     f"?range=10d&interval=1d")
    res = (doc.get("chart") or {}).get("result")
    if not res:
        raise RuntimeError("no result")
    r = res[0]
    ts = r.get("timestamp") or []
    closes = ((r.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []
    return {"meta": r.get("meta") or {},
            "bars": [(t, c) for t, c in zip(ts, closes) if c is not None]}


def session_groups(bars, offset_h: int):
    """Group Yahoo daily bars by local session date -> {date: [closes]}."""
    g: dict[str, list[float]] = {}
    for t, c in bars:
        d = (datetime.fromtimestamp(t, timezone.utc)
             + timedelta(hours=offset_h)).date().isoformat()
        g.setdefault(d, []).append(c)
    return g


def fetch_fx():
    for cur, sym in {"EUR": "EURUSD=X", "JPY": "USDJPY=X", "AUD": "AUDUSD=X",
                     "CAD": "USDCAD=X", "DKK": "USDDKK=X"}.items():
        try:
            d = yahoo_chart(sym)
            if not d["bars"]:
                continue
            last = d["bars"][-1][1]
            FX[cur] = last if cur != "JPY" else 1.0 / last
        except Exception as e:  # noqa: BLE001
            print(f"  FX {cur} direct failed: {str(e)[:50]}")
    if not FX.get("DKK"):                       # EUR/DKK cross
        try:
            eurdkk = yahoo_chart("EURDKK=X")["bars"][-1][1]
            if FX.get("EUR") and eurdkk:
                FX["DKK"] = FX["EUR"] / eurdkk
        except Exception as e:  # noqa: BLE001
            print(f"  FX DKK cross failed: {str(e)[:50]}")
    print("FX:", {k: (round(v, 6) if v else None) for k, v in FX.items()})


def is_common(ticker: str, name: str) -> bool:
    sym = ticker.split(":", 1)[-1]
    if NON_COMMON_SYM.match(sym):
        return False
    if NON_COMMON_PAT.search(name or ""):
        return False
    return True


def main() -> int:
    print("== FX ==")
    fetch_fx()

    recs_by_region, noncommon = {}, {}
    for region in sorted(REGION_MAP):
        path = f"{OUT}/{region}.csv"
        if not os.path.exists(path):
            continue
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        recs = []
        for r in rows:
            rec = {"ticker": r["ticker"], "name": r["name"],
                   "close": num(r["close"]), "change": num(r["change_pct"]),
                   "volume": num(r["volume"]), "mcap": num(r["market_cap"]),
                   "ccy": r["currency"], "sector": r["sector"],
                   "venue": r["exchange"], "pe": num(r["pe_ratio"])}
            rec["common"] = is_common(r["ticker"], r["name"])
            f = FX.get(r["currency"])
            rec["mcap_usd"] = rec["mcap"] * f if (rec["mcap"] and f) else None
            recs.append(rec)
        recs_by_region[region] = recs
        noncommon[region] = sum(1 for x in recs if not x["common"])

    # ---- movers on the common-share subset ---------------------------
    movers = {}
    for region, recs in recs_by_region.items():
        common = [x for x in recs if x["common"] and x["change"] is not None]
        liq = [x for x in common if (x["mcap_usd"] or 0) >= 1e9]
        liq.sort(key=lambda x: -x["change"])
        movers[region] = {
            "rows": len(recs), "common": len(common),
            "non_common": noncommon[region],
            "liquid_common": len(liq),
            "up_3": sum(1 for x in common if x["change"] >= 3),
            "dn_3": sum(1 for x in common if x["change"] <= -3),
            "up_3_liquid": sum(1 for x in liq if x["change"] >= 3),
            "dn_3_liquid": sum(1 for x in liq if x["change"] <= -3),
            "top_up": liq[:6], "top_dn": liq[-6:][::-1],
        }

    # ---- Yahoo cross-check -------------------------------------------
    import random
    tasks = []
    for region, recs in recs_by_region.items():
        smap = REGION_MAP[region][1]
        cand = [x for x in recs if x["common"] and x["change"] is not None
                and x["close"] and x["ticker"].split(":", 1)[0] in smap]
        by_abs = sorted(cand, key=lambda x: -abs(x["change"]))[:12]
        by_cap = sorted([x for x in cand if (x["mcap_usd"] or 0) >= 5e8],
                        key=lambda x: -(x["mcap_usd"] or 0))[:18]
        rnd = random.Random(11)
        pool = [x for x in cand if (x["mcap_usd"] or 0) >= 1e8]
        rnd.shuffle(pool)
        picked, seen = [], set()
        for x in by_abs + by_cap + pool[:12]:
            if x["ticker"] in seen:
                continue
            seen.add(x["ticker"])
            picked.append(x)
        for x in picked:
            venue, sym = x["ticker"].split(":", 1)
            tasks.append((region, x, f"{sym.replace('.', '-')}{smap[venue]}"))

    def run(t):
        region, x, ys = t
        try:
            d = yahoo_chart(ys)
        except Exception as e:  # noqa: BLE001
            return {"region": region, "ticker": x["ticker"], "yahoo": ys,
                    "error": str(e)[:80]}
        off = REGION_MAP[region][0]
        g = session_groups(d["bars"], off)
        dates = sorted(g)
        today_close = g.get(DATE, [None])[-1] if DATE in g else None
        prior_dates = [dt for dt in dates if dt < DATE]
        prior_close = g[prior_dates[-1]][-1] if prior_dates else None
        tv_ref = x["close"] / (1 + x["change"] / 100) if x["change"] is not None else None
        res = {"region": region, "ticker": x["ticker"], "yahoo": ys,
               "tv_close": x["close"], "tv_change": x["change"],
               "yh_close": today_close, "yh_ref": prior_close, "tv_ref": tv_ref,
               "last_session": dates[-1] if dates else None,
               "no_session_bar": DATE not in g}
        if tv_ref and prior_close:
            res["ref_diff_pct"] = abs(tv_ref - prior_close) / prior_close * 100
            res["ref_agrees"] = res["ref_diff_pct"] < 0.3
        if x["close"] and today_close:
            res["price_diff_pct"] = abs(x["close"] - today_close) / today_close * 100
            res["price_agrees"] = res["price_diff_pct"] < 0.3
        return res

    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(run, tasks))

    per = {}
    for r in results:
        p = per.setdefault(r["region"], {
            "attempted": 0, "fetch_error": 0, "no_session_bar": 0,
            "ref_testable": 0, "ref_agrees": 0, "price_testable": 0,
            "price_agrees": 0, "ref_diffs": [], "price_diffs": [], "mismatches": [],
            "no_bar_examples": []})
        p["attempted"] += 1
        if r.get("error"):
            p["fetch_error"] += 1
            continue
        if r.get("no_session_bar"):
            p["no_session_bar"] += 1
            if len(p["no_bar_examples"]) < 6:
                p["no_bar_examples"].append(
                    {"ticker": r["ticker"], "last_session": r.get("last_session")})
        if "ref_agrees" in r:
            p["ref_testable"] += 1
            p["ref_diffs"].append(r["ref_diff_pct"])
            if r["ref_agrees"]:
                p["ref_agrees"] += 1
            else:
                p["mismatches"].append(
                    {"ticker": r["ticker"], "tv_ref": r["tv_ref"],
                     "yh_ref": r["yh_ref"], "diff_pct": round(r["ref_diff_pct"], 4),
                     "last_session": r.get("last_session")})
        if "price_agrees" in r:
            p["price_testable"] += 1
            p["price_diffs"].append(r["price_diff_pct"])
            if r["price_agrees"]:
                p["price_agrees"] += 1
    for p in per.values():
        for k in ("ref_diffs", "price_diffs"):
            v = sorted(p.pop(k))
            base = k.replace("_diffs", "")
            p[base + "_median"] = round(v[len(v) // 2], 4) if v else None
            p[base + "_max"] = round(v[-1], 4) if v else None

    json.dump({"date": DATE, "fx": FX, "movers": movers, "crosscheck": per,
               "crosscheck_rows": results},
              open(f"{DATA}/_qa_intl2.json", "w"), indent=1, default=str)

    for region in sorted(movers):
        m = movers[region]
        c = per.get(region, {})
        up = ", ".join(f"{x['ticker'].split(':')[-1]} {x['change']:+.2f}%"
                       for x in m["top_up"][:3])
        dn = ", ".join(f"{x['ticker'].split(':')[-1]} {x['change']:+.2f}%"
                       for x in m["top_dn"][:3])
        print(f"{region:6s} rows={m['rows']:5d} common={m['common']:5d} "
              f"noncommon={m['non_common']:4d} liq$1b={m['liquid_common']:4d} "
              f"up3={m['up_3']:4d} dn3={m['dn_3']:4d} | up {up} | dn {dn}")
        print(f"       xcheck n={c.get('attempted')} "
              f"ref_ok={c.get('ref_agrees')}/{c.get('ref_testable')} "
              f"med|dref|={c.get('ref_median')} max={c.get('ref_max')} | "
              f"price_ok={c.get('price_agrees')}/{c.get('price_testable')} "
              f"med|dpx|={c.get('price_median')} | no_bar={c.get('no_session_bar')} "
              f"err={c.get('fetch_error')}")
        if c.get("mismatches"):
            for mm in c["mismatches"][:4]:
                print("         MISMATCH", mm)
    return 0


if __name__ == "__main__":
    sys.exit(main())
