#!/usr/bin/env python3
"""Fetch non-stock symbols needed by the regime/breadth layer and merge into the bar cache.

Covers: the 5 regime indices (SPY/RSP/QQQ/QQQE/IWM), the extra index funds the breadth
cross-check uses (DIA/VTI/VOO), the 11 sector ETFs, VIX and the two VXV legs, plus every
S&P 500 constituent (so the breadth above/below-20-DMA cross-check has a full sample
instead of only the names that survived the prefilter).
Written to a separate file so it cannot be lost when the concurrent universe fetch
writes yahoo_bars.json.
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/workspace/data")
from yahoo_enrich import fetch, ysym  # noqa: E402

EXTRA = "/workspace/data/yahoo_bars_extra.json"
MERGE = "/workspace/data/yahoo_bars.json"

INDICES = ["SPY", "RSP", "QQQ", "QQQE", "IWM", "DIA", "VTI", "VOO"]
SECTOR_ETFS = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]
VOL = ["^VIX", "^VXV", "^VXVCLS"]


def main():
    sp500 = json.load(open("/workspace/data/sp500_tickers.json"))
    names = list(dict.fromkeys(INDICES + SECTOR_ETFS + VOL + sp500))
    cache = json.load(open(EXTRA)) if os.path.exists(EXTRA) else {}
    todo = [n for n in names if not cache.get(n, {}).get("bars")]
    print(f"extras={len(names)} to_fetch={len(todo)}", file=sys.stderr)
    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=5) as ex:
        for d in ex.map(fetch, todo):
            cache[d["symbol"]] = d
            done += 1
            if done % 100 == 0:
                print(f"  {done}/{len(todo)} ({time.time()-t0:.0f}s)", file=sys.stderr)
    json.dump(cache, open(EXTRA, "w"))
    fails = [n for n in names if not cache.get(n, {}).get("bars")]
    print(f"done in {time.time()-t0:.0f}s; no bars for {len(fails)}: {fails[:25]}", file=sys.stderr)

    # merge (only after the concurrent universe fetch has written its file)
    if os.path.exists(MERGE):
        main_cache = json.load(open(MERGE))
        added = 0
        for k, v in cache.items():
            if k not in main_cache:
                main_cache[k] = v
                added += 1
        json.dump(main_cache, open(MERGE, "w"))
        print(f"merged extras into {MERGE}: +{added} symbols, total {len(main_cache)}", file=sys.stderr)
    else:
        print("MERGE DEFERRED: yahoo_bars.json not present yet", file=sys.stderr)


if __name__ == "__main__":
    main()
