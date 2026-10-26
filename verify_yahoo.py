#!/usr/bin/env python3
"""Yahoo Finance cross-check + blank-fill for the EOD snapshot.

Cloud adaptation: the `mcp__yahoo-finance__compare_stocks` MCP binding is not
exposed in this session, so this uses Yahoo's public spark endpoint (same
underlying quote service) to (a) independently verify close / change_pct /
volume against the TradingView screener values, and (b) record Yahoo values
for rows whose change_pct the screener left blank.

TV -> Yahoo mapping follows scripts/yahoo_enrich.py (TV_TO_YAHOO_SUFFIX +
EURONEXT_SYMBOL_MAP), extended with the venues the screener actually returns.
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys
import time
import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
DATA = "/workspace/data"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-20"

TV_TO_YAHOO_SUFFIX = {
    "ASX": ".AX", "TSE": ".T", "NAG": ".T", "FSE": ".T", "SAPSE": ".T",
    "TWSE": ".TW", "TPEX": ".TWO", "NEO": ".TO", "TSX": ".TO", "TSXV": ".V",
    "CSE": ".CN", "XETR": ".DE", "XETRA": ".DE", "FWB": ".DE", "MUN": ".DE",
    "DUS": ".DE", "HAM": ".DE", "HAN": ".DE", "SWB": ".DE", "GETTEX": ".DE",
    "TRADEGATE": ".DE", "LSX": ".L", "LS": ".L", "BME": ".MC", "MIL": ".MI",
    "EUROTLX": ".MI", "VIE": ".VI", "ATHEX": ".AT", "ATH": ".AT",
    "OMXCOP": ".CO", "CPH": ".CO", "OMXHEX": ".HE", "HEL": ".HE", "AMS": ".AS",
    "BSE": ".BR", "BRU": ".BR", "LIS": ".LS", "ISE": ".IR", "Dublin": ".IR",
    "EPA": ".PA",
}
EURONEXT_SYMBOL_MAP = {
    "ASML": ".AS", "SHELL": ".AS", "UNA": ".AS", "INGA": ".AS", "ADYEN": ".AS",
    "AD": ".AS", "HEIA": ".AS", "PHIA": ".AS", "REN": ".AS", "KPN": ".AS",
    "MT": ".AS", "BESI": ".AS", "AKZA": ".AS", "IMCD": ".AS", "ASRNL": ".AS",
    "NN": ".AS", "RAND": ".AS", "AGN": ".AS", "UMG": ".AS", "AALB": ".AS",
    "VPK": ".AS", "CTPNV": ".AS", "EXO": ".AS", "DSFIR": ".AS", "WKL": ".AS",
    "FLOW": ".AS", "PRX": ".AS", "ASM": ".AS", "CVC": ".AS", "CCEP": ".AS",
    "ABI": ".BR", "KBC": ".BR", "ARGX": ".BR", "UCB": ".BR", "AGS": ".BR",
    "ELI": ".BR", "LOTB": ".BR", "ACKB": ".BR", "GBLB": ".BR", "SOF": ".BR",
    "DIE": ".BR", "UMI": ".BR", "WDP": ".BR", "SYENS": ".BR", "SOLB": ".BR",
    "COBH": ".BR", "MELE": ".BR", "TUB": ".BR", "ONTEX": ".BR",
    "OR": ".PA", "MC": ".PA", "SAN": ".PA", "BNP": ".PA", "AI": ".PA",
    "AIR": ".PA", "BN": ".PA", "CA": ".PA", "SU": ".PA", "ENGI": ".PA",
    "VIE": ".PA", "DG": ".PA", "EL": ".PA", "SIE": ".PA", "RMS": ".PA",
    "CAP": ".PA", "PUB": ".PA", "DSY": ".PA", "LR": ".PA",
    "EDP": ".LS", "GALP": ".LS", "BCP": ".LS", "EDPR": ".LS", "JMT": ".LS",
    "A5G": ".IR", "RYA": ".IR", "BIRG": ".IR", "KRX": ".IR", "KRZ": ".IR",
    "GL9": ".IR",
}
REGION_EURONEXT_SUFFIX = {
    "eu-fr": ".PA", "eu-nl": ".AS", "eu-be": ".BR", "eu-pt": ".LS",
    "eu-ie": ".IR", "eu-it": ".MI",
}
STOP = {"inc", "plc", "ltd", "corp", "corporation", "company", "the", "and",
        "sa", "ag", "nv", "co", "group", "holdings", "limited", "llc", "lp",
        "se", "ab", "as", "oy", "kk", "gmbh", "class", "warr", "adr"}


def to_yahoo(tv: str, region: str = "") -> str | None:
    if ":" not in tv:
        return tv
    exch, sym = tv.split(":", 1)
    if exch == "EURONEXT":
        return sym + EURONEXT_SYMBOL_MAP.get(
            sym, REGION_EURONEXT_SUFFIX.get(region, ".AS"))
    if exch in ("NASDAQ", "NYSE", "AMEX", "CBOE", "OTC"):
        return sym.replace(".", "-")
    if exch in ("NEO", "TSX"):
        base = sym.split(".PR")[0]          # RY.PR.S -> RY
        return base.replace(".", "-") + ".TO"
    suffix = TV_TO_YAHOO_SUFFIX.get(exch)
    if suffix is None:
        return None
    return sym + suffix


def norm_tokens(name):
    if not name:
        return set()
    s = re.sub(r"[^a-z0-9 ]", " ", name.lower())
    return {t for t in s.split() if len(t) > 2 and t not in STOP}


def same_entity(tv_name, yahoo_name):
    ta, tb = norm_tokens(tv_name), norm_tokens(yahoo_name)
    if not ta or not tb:
        return True
    if ta & tb:
        return True
    return ta <= tb or tb <= ta


def _spark_once(symbols: list[str], tries: int = 3) -> dict:
    url = ("https://query1.finance.yahoo.com/v7/finance/spark?symbols="
           + ",".join(symbols) + "&range=1d&interval=1d")
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = json.loads(r.read().decode())
            out = {}
            for item in data.get("spark", {}).get("result", []) or []:
                resp = item.get("response", [{}])
                meta = (resp[0] or {}).get("meta", {}) if resp else {}
                if meta:
                    out[meta.get("symbol")] = meta
            return out
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                raise
            last = e
            time.sleep(1.2 * (attempt + 1))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.2 * (attempt + 1))
    raise last


def spark(symbols: list[str], tries: int = 3) -> dict:
    """Fetch spark metas; bisect on 400/404 so one bad symbol can't kill a batch."""
    symbols = list(symbols)
    try:
        return _spark_once(symbols, tries)
    except urllib.error.HTTPError as e:
        if e.code not in (400, 404) or len(symbols) == 1:
            print(f"  WARN spark failed: {str(e)[:70]} ({len(symbols)} syms)")
            return {}
    except Exception as e:  # noqa: BLE001
        print(f"  WARN spark failed: {str(e)[:70]} ({len(symbols)} syms)")
        return {}
    mid = len(symbols) // 2
    out = spark(symbols[:mid], tries)
    out.update(spark(symbols[mid:], tries))
    return out


def main() -> int:
    regions = [f[:-5] for f in sorted(os.listdir(DATA))
               if f.endswith(".json") and not f.startswith("_")]
    report, yahoo_by_tv = {}, {}
    for region in regions:
        blob = json.load(open(f"{DATA}/{region}.json", encoding="utf-8"))
        rows = blob["rows"]
        def mcap(r):
            v = r["values"][8]
            return -(v if isinstance(v, (int, float)) else 0)
        def chg(r):
            v = r["values"][7]
            return -(abs(v) if isinstance(v, (int, float)) else 0)
        by_mcap = sorted(rows, key=mcap)
        movers = sorted(rows, key=chg)
        blanks = [r for r in rows
                  if r["values"][7] in (None, "") or r["values"][6] in (None, "")]
        cand = {r["ticker"]: r for r in (by_mcap[:40] + movers[:40] + blanks)}
        pairs = []
        for tv in cand:
            yt = to_yahoo(tv, region)
            if yt:
                pairs.append((tv, yt))
        metas = {}
        for i in range(0, len(pairs), 20):
            metas.update(spark([y for _, y in pairs[i:i + 20]]))

        matched = same_name = other_name = 0
        diffs, yahoo_vals = [], {}
        for tv, yt in pairs:
            m = metas.get(yt)
            if not m:
                continue
            matched += 1
            yname = m.get("longName") or m.get("shortName") or ""
            tvname = cand[tv]["values"][1] or ""
            same = same_entity(tvname, yname)
            same_name += 1 if same else 0
            other_name += 0 if same else 1
            rec = {"yahoo_symbol": yt, "tv_name": tvname,
                   "yahoo_name": yname, "same_entity": same,
                   "price": m.get("regularMarketPrice"),
                   "change_pct": m.get("regularMarketChangePercent"),
                   "volume": m.get("regularMarketVolume"),
                   "day_high": m.get("regularMarketDayHigh"),
                   "day_low": m.get("regularMarketDayLow"),
                   "prev_close": m.get("chartPreviousClose"),
                   "currency": m.get("currency"),
                   "exchange": m.get("fullExchangeName")}
            yahoo_vals[tv] = rec
            yahoo_by_tv[tv] = rec
            tv_ch = cand[tv]["values"][7]
            if (same and isinstance(tv_ch, (int, float))
                    and m.get("regularMarketChangePercent") is not None):
                diffs.append(abs(tv_ch - m["regularMarketChangePercent"]))
        report[region] = {
            "checked": len(pairs), "matched": matched,
            "matched_same_entity": same_name,
            "matched_other_entity": other_name,
            "median_abs_change_diff_pp": (round(statistics.median(diffs), 4)
                                           if diffs else None),
            "max_abs_change_diff_pp": (round(max(diffs), 4) if diffs else None),
            "n_within_0_5pp": sum(1 for d in diffs if d <= 0.5),
            "n_over_1pp": sum(1 for d in diffs if d > 1.0),
            "yahoo": yahoo_vals}
        print(f"{region}: checked={len(pairs)} matched={matched} "
              f"same={same_name} other={other_name} "
              f"median|d|={report[region]['median_abs_change_diff_pp']}pp "
              f">1pp={report[region]['n_over_1pp']}", flush=True)

    json.dump(report, open(f"{DATA}/_yahoo_verify.json", "w"), indent=1)
    json.dump(yahoo_by_tv, open(f"{DATA}/_yahoo_values.json", "w"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
