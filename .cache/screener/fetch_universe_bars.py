#!/usr/bin/env python3
"""Fetch Yahoo daily bars for EVERY prefiltered universe name (Cloud cron #9).

The ADR / velocity / ATR-shrink gates need real bars, so any prefiltered name without
bars would be silently dropped from every screen. This closes that coverage hole.
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/workspace/data")
from yahoo_enrich import fetch  # noqa: E402

DATA = "/workspace/data"
CACHE = f"{DATA}/yahoo_bars.json"


def prefiltered_names():
    raw = json.load(open(f"{DATA}/tv_universe_raw.json"))
    cols = raw["columns"]
    idx = {c: i for i, c in enumerate(cols)}
    out = set()
    for r in raw["rows"]:
        d = r["d"]
        if d[idx["type"]] != "stock":
            continue
        if d[idx["exchange"]] not in ("NYSE", "NASDAQ", "AMEX"):
            continue
        if not (d[idx["close"]] and d[idx["close"]] > 3):
            continue
        if not (d[idx["market_cap_basic"]] and d[idx["market_cap_basic"]] > 300_000_000):
            continue
        if not (d[idx["average_volume_30d_calc"]] and d[idx["average_volume_30d_calc"]] > 100_000):
            continue
        out.add(d[idx["name"]])
    return sorted(out)


def main():
    names = prefiltered_names()
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [n for n in names if not cache.get(n, {}).get("bars")]
    print(f"prefiltered={len(names)} already_cached={len(names)-len(todo)} to_fetch={len(todo)}",
          file=sys.stderr)
    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=5) as ex:
        for d in ex.map(fetch, todo):
            cache[d["symbol"]] = d
            done += 1
            if done % 250 == 0:
                print(f"  fetched {done}/{len(todo)} ({time.time()-t0:.0f}s)", file=sys.stderr)
    json.dump(cache, open(CACHE, "w"))
    fails = [n for n in names if not cache.get(n, {}).get("bars")]
    print(f"done in {time.time()-t0:.0f}s; universe bars missing for {len(fails)} names: {fails[:20]}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
