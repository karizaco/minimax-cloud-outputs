#!/usr/bin/env python3
"""
Rebuild the option row set from the RAW chain JSON using contractSymbol as the
authoritative expiry key, then cross-validate against Cboe's independent chain.

Why the rebuild: Yahoo's `expirationDate` epoch is 00:00 **UTC** of the true
expiry date (e.g. epoch 1793145600 = 2026-10-28T00:00Z, and the contracts in
that chain are named AAPL261028C*). Rendering that epoch in US/Eastern yields
the previous calendar day, so an ET-rendered label is off by one. The OCC
contract symbol encodes YYMMDD, which is unambiguous - use that.

Second finding: Yahoo drops a just-expired 0DTE expiry from `expirationDates`
after the close, so the session-date 0DTE (2026-10-27) is absent for IWM/GLD
even though Cboe shows real volume in it. Cboe supplies those rows.
"""
import json, os, re, datetime, collections

UTC = datetime.timezone.utc
ET = datetime.timezone(datetime.timedelta(hours=-4))
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
SESSION = "2026-10-27"          # ET trading date
MIN_VOLUME = 100                # skill's min_volume
TICKERS = ["IWM", "GLD", "TLT", "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
CBOE_DIR = os.path.join(DATA, "cboe")

def cboe_chain(u):
    p = os.path.join(CBOE_DIR, f"{u}.json")
    if not os.path.exists(p):
        return {}
    d = json.load(open(p))
    out = {}
    for o in d["data"]["options"]:
        out[o["option"]] = o
    return out

def main():
    meta = json.load(open(os.path.join(DATA, "rows.json")))["meta"]
    rows = []
    seen = set()
    for sym in TICKERS:
        price = meta[sym]["price"]
        regtime = meta[sym]["regularMarketTime"]
        sdate = datetime.datetime.fromtimestamp(regtime, ET).date()
        for fn in sorted(os.listdir(DATA)):
            if not (fn.startswith(f"chain_{sym}_") and fn.endswith(".json")):
                continue
            try:
                d = json.load(open(os.path.join(DATA, fn)))
            except Exception:
                continue
            r = (d.get("optionChain", {}).get("result") or [])
            if not r:
                continue
            for o in r[0].get("options", []):
                for side_key, side in (("calls", "call"), ("puts", "put")):
                    for c in o.get(side_key, []):
                        cs = c.get("contractSymbol")
                        m = re.match(r"^[A-Z]+(\d{6})([CP])(\d{8})$", cs or "")
                        if not m:
                            continue
                        expiry = datetime.datetime.strptime(m.group(1), "%y%m%d").strftime("%Y-%m-%d")
                        vol = c.get("volume") or 0
                        oi = c.get("openInterest")
                        if vol < MIN_VOLUME or not oi:
                            continue
                        key = cs
                        if key in seen:
                            continue
                        seen.add(key)
                        strike = c.get("strike")
                        rows.append({
                            "ticker": sym, "side": side, "strike": strike,
                            "expiry": expiry, "contract": cs,
                            "dte": (datetime.datetime.strptime(expiry, "%Y-%m-%d").date() - sdate).days,
                            "volume": vol, "open_interest": oi,
                            "v_oi": round(vol / oi, 4),
                            "last_price": c.get("lastPrice"),
                            "iv": c.get("impliedVolatility"),
                            "in_the_money": c.get("inTheMoney"),
                            "underlying_price": price,
                            "moneyness_pct": round(((price - strike) if side == "call" else (strike - price)) / price * 100, 2) if price else None,
                            "_source": "yahoo_chain",
                        })
    yahoo_n = len(rows)

    # --- fill gaps from Cboe ---
    # Yahoo drops the just-expired session-date 0DTE from `expirationDates`
    # after the close, so today's 0DTE is unreachable through the chain path
    # even though it carried the bulk of IWM/GLD volume. Cboe keeps it.
    # Scope of the fill: the session-date expiry plus any expiry inside the
    # ticker-specific 4-expiry window Yahoo listed. Nothing outside that.
    yahoo_exp = collections.defaultdict(set)
    for r in rows:
        yahoo_exp[r["ticker"]].add(r["expiry"])
    added = []
    for sym in TICKERS:
        cc = cboe_chain(sym)
        if not cc:
            continue
        price = meta[sym]["price"]
        regtime = meta[sym]["regularMarketTime"]
        sdate = datetime.datetime.fromtimestamp(regtime, ET).date()
        for cs, o in cc.items():
            m = re.match(rf"^{sym}(\d{{6}})([CP])(\d{{8}})$", cs)
            if not m:
                continue
            expiry = datetime.datetime.strptime(m.group(1), "%y%m%d").strftime("%Y-%m-%d")
            if expiry != SESSION and expiry not in yahoo_exp[sym]:
                continue
            vol = o.get("volume") or 0
            oi = o.get("open_interest")
            if vol < MIN_VOLUME or not oi:
                continue
            if cs in seen:
                continue
            seen.add(cs)
            strike = int(m.group(3)) / 1000
            side = "call" if m.group(2) == "C" else "put"
            added.append({
                "ticker": sym, "side": side, "strike": strike, "expiry": expiry,
                "contract": cs,
                "dte": (datetime.datetime.strptime(expiry, "%Y-%m-%d").date() - sdate).days,
                "volume": int(vol), "open_interest": int(oi), "v_oi": round(vol / oi, 4),
                "last_price": o.get("last_trade_price"),
                "iv": o.get("iv"),
                "in_the_money": (strike < price) if side == "call" else (strike > price),  # call ITM if strike<spot
                "underlying_price": price,
                "moneyness_pct": round(((price - strike) if side == "call" else (strike - price)) / price * 100, 2),
                "_source": "cboe_chain",
            })
    rows.extend(added)

    # --- reconstruct the expiries=4 window as it stood at the 09:55 ET target ---
    # Yahoo drops the just-expired session-date 0DTE from `expirationDates`
    # after the close, so today's list is shifted one slot later than it was
    # during the session. Taking the 4 EARLIEST expiries per ticker across
    # {Yahoo's list} U {session-date expiry} therefore reproduces the window a
    # 09:55 ET run would have pulled, and matches the prior run's structure
    # (session 0DTE + next three by date).
    by_tick_exp = collections.defaultdict(set)
    for r in rows:
        by_tick_exp[r["ticker"]].add(r["expiry"])
    keep_exp = {}
    for t in TICKERS:
        exp = sorted(by_tick_exp[t])
        keep_exp[t] = set(exp[:4])
    dropped = {t: sorted(by_tick_exp[t] - keep_exp[t]) for t in TICKERS}
    rows = [r for r in rows if r["expiry"] in keep_exp[r["ticker"]]]
    # Cboe reports iv=0.0 for contracts it could not mark -> treat as missing
    for r in rows:
        if r.get("iv") is not None and not r["iv"]:
            r["iv"] = None

    # --- cross-validation: Yahoo vs Cboe on the same contract symbol ---
    cboemap = {}
    for sym in TICKERS:
        for cs, o in cboe_chain(sym).items():
            cboemap[cs] = o
    agree = tot = 0
    vol_diff = []
    oi_agree = 0
    oi_diff = []
    zero_cboe = 0
    for r in rows:
        if r["_source"] != "yahoo_chain":
            continue          # Cboe-sourced rows would compare against themselves
        c = cboemap.get(r["contract"])
        if not c:
            continue
        cv = c.get("volume") or 0
        co = c.get("open_interest") or 0
        tot += 1
        if abs((r["volume"] or 0) - cv) <= max(5, 0.01 * cv):
            agree += 1
        else:
            if cv == 0 and (r["volume"] or 0) > 0:
                zero_cboe += 1
            vol_diff.append((r["contract"], r["volume"], cv))
        if abs((r["open_interest"] or 0) - co) <= 1:
            oi_agree += 1
        else:
            oi_diff.append((r["contract"], r["open_interest"], co))
    xval = {
        "contracts_compared": tot, "volume_agree": agree,
        "volume_agree_pct": round(agree / tot * 100, 2) if tot else None,
        "volume_mismatch_n": len(vol_diff), "volume_mismatch_cboe_zero": zero_cboe,
        "volume_mismatches": vol_diff[:20],
        "oi_agree": oi_agree, "oi_agree_pct": round(oi_agree / tot * 100, 2) if tot else None,
        "oi_mismatch_n": len(oi_diff), "oi_mismatches": oi_diff[:10],
    }

    json.dump({"rows": rows, "xval": xval, "yahoo_n": yahoo_n, "cboe_added_n": len(added),
               "dropped_expiries": dropped, "keep_exp": {k: sorted(v) for k, v in keep_exp.items()}},
              open(os.path.join(DATA, "rows_final.json"), "w"), indent=1)

    print("yahoo rows:", yahoo_n, "| cboe-added:", len(added), "| total:", len(rows))
    print("XVAL volume agree: %s/%s = %s%%" % (agree, tot, xval["volume_agree_pct"]))
    print("OI mismatches:", len(oi_diff))
    for m in vol_diff[:10]:
        print("   vol diff:", m)
    for m in oi_diff[:10]:
        print("   oi diff:", m)
    print()
    print("expiry histogram (ticker:expiry -> n, vol):")
    agg = collections.Counter()
    volagg = collections.Counter()
    for r in rows:
        k = (r["ticker"], r["expiry"])
        agg[k] += 1
        volagg[k] += r["volume"]
    for k in sorted(agg, key=lambda x: (x[1], x[0])):
        print(f"   {k[0]:6s} {k[1]}  n={agg[k]:3d} vol={volagg[k]:,}")
    print()
    print("DTE histogram:", collections.Counter(r["dte"] for r in rows))


if __name__ == "__main__":
    main()
