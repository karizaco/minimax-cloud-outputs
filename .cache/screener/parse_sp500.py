#!/usr/bin/env python3
"""Parse the Wikipedia S&P 500 constituent list (wikitext table) into a ticker list.

Wikitext rows look like:  | {{NyseSymbol|MMM}} | 3M | ...
We need the raw ticker in Yahoo form (BRK.B -> BRK-B, which ysym() handles downstream).
"""
import json
import re

RAW = "/workspace/data/sp500_wiki.json"
OUT = "/workspace/data/sp500_tickers.json"

j = json.load(open(RAW))
text = j["parse"]["wikitext"]["*"]

# tickers are wrapped in {{NyseSymbol|X}} / {{NasdaqSymbol|X}} / {{IndexSymbol|X}}
tickers = []
for m in re.finditer(r"\{\{(?:Nyse|Nasdaq|BATS|Cboe|Index)Symbol\|([^}|]+)", text):
    t = m.group(1).strip()
    if t and re.match(r"^[A-Z0-9.\-]+$", t):
        tickers.append(t)

# dedupe, keep order
seen = set()
out = []
for t in tickers:
    if t not in seen:
        seen.add(t)
        out.append(t)

json.dump(out, open(OUT, "w"))
print(f"parsed {len(out)} unique tickers -> {OUT}")
print("first 10:", out[:10])
print("BRK entries:", [t for t in out if "BRK" in t or "BF" in t])
