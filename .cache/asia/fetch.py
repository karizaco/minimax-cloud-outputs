import urllib.request, json, time, datetime, sys
from concurrent.futures import ThreadPoolExecutor

universe = {
    "JP": ["7203.T","6758.T","9984.T","8306.T","6861.T","7974.T","6902.T","9432.T","9433.T","7267.T",
        "8058.T","8035.T","4063.T","7741.T","6367.T","6503.T","6501.T","7269.T","7751.T","6594.T",
        "8766.T","4502.T","4503.T","6901.T","7261.T","3382.T","5401.T","2914.T","2802.T","4452.T",
        "4507.T","4519.T","4523.T","4568.T","4578.T","4901.T","4902.T","4911.T","5019.T","5108.T",
        "5201.T","5233.T","5301.T","5411.T","5706.T","5711.T","5713.T","5801.T","5802.T","5803.T",
        "6005.T","6103.T","6134.T","6178.T","6235.T","6301.T","6302.T","6326.T","6361.T","6383.T",
        "6407.T","6471.T","6472.T","6473.T","6479.T","6504.T","6526.T","6532.T","6544.T","6562.T",
        "6574.T","6588.T","6619.T","6701.T","6702.T","6703.T","6723.T","6727.T","6728.T","6740.T",
        "6741.T","6752.T","6753.T","6758.T","6762.T","6779.T","6787.T","6794.T","6797.T","6803.T",
        "6806.T","6810.T"],
    "TW": ["2330.TW","2454.TW","2317.TW","2308.TW","2303.TW","2881.TW","2882.TW","2884.TW","2886.TW","2891.TW",
        "2892.TW","1101.TW","1102.TW","1216.TW","1301.TW","1303.TW","1326.TW","2002.TW","2207.TW","2301.TW",
        "2311.TW","2327.TW","2337.TW","2357.TW","2379.TW","2382.TW","2395.TW","2408.TW","2409.TW","2412.TW",
        "2474.TW","2603.TW","2609.TW","2615.TW","2618.TW","2633.TW","2801.TW","2823.TW","2880.TW","2883.TW",
        "2885.TW","2887.TW","2888.TW","2890.TW","2894.TW","2912.TW","3008.TW","3034.TW","3036.TW","3037.TW",
        "3045.TW","3231.TW","3481.TW","4904.TW","4958.TW","5871.TW","5876.TW","5882.TW","6239.TW","6271.TW"],
    "HK": ["0700.HK","9988.HK","3690.HK","9618.HK","1810.HK","0941.HK","1299.HK","0883.HK","0388.HK","1398.HK",
        "3988.HK","2628.HK","0823.HK","0669.HK","1109.HK","0005.HK","0001.HK","0016.HK","0017.HK","0027.HK",
        "0066.HK","0101.HK","0175.HK","0267.HK","0386.HK","0688.HK","0857.HK","0868.HK","0902.HK","0992.HK",
        "1024.HK","1038.HK","1044.HK","1088.HK","1093.HK","1099.HK","1113.HK","1177.HK","1211.HK","1288.HK",
        "1336.HK","1378.HK","1448.HK","1655.HK","1686.HK","1876.HK","1918.HK","1928.HK","1929.HK","1972.HK",
        "2007.HK","2015.HK","2018.HK","2020.HK","2057.HK","2076.HK","2121.HK","2269.HK","2313.HK","2318.HK",
        "2331.HK","2382.HK","2388.HK","2410.HK","2423.HK","2459.HK","2513.HK","2533.HK","2600.HK","2688.HK"],
    "KR": ["005930.KS","000660.KS","005380.KS","035420.KS","051910.KS","005490.KS","028260.KS","105560.KS","055550.KS","012330.KS",
        "096770.KS","017670.KS","003550.KS","066570.KS","034730.KS","015760.KS","033780.KS","018260.KS","003490.KS","009150.KS",
        "024110.KS","011170.KS","000270.KS","010130.KS","028050.KS","030200.KS","036570.KS","004020.KS","086790.KS","009540.KS",
        "000810.KS","021240.KS","032830.KS","006400.KS","139480.KS","010950.KS","002790.KS","000720.KS","005940.KS","034020.KS",
        "005830.KS","001740.KS","005385.KS","002380.KS","006800.KS","009830.KS","011790.KS","014680.KS","016360.KS"],
}

def fetch_one(sym):
    for attempt in range(3):
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=5d&interval=1d"
            req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            data = json.loads(urllib.request.urlopen(req, timeout=6).read())
            r = data["chart"]["result"]
            if not r:
                return None
            meta = r[0]["meta"]
            ts = r[0].get("timestamp", [])
            lc = datetime.datetime.utcfromtimestamp(ts[-1]).isoformat() if ts else None
            return {"symbol":sym,"price":meta.get("regularMarketPrice"),
                    "pct":meta.get("regularMarketChangePercent"),
                    "currency":meta.get("currency"),"exchange":meta.get("fullExchangeName"),
                    "last_close_utc":lc}
        except Exception:
            time.sleep(0.8*(attempt+1))
    return None

region = sys.argv[1]
got=[]
with ThreadPoolExecutor(max_workers=12) as ex:
    for r in ex.map(fetch_one, universe[region]):
        if r: got.append(r)
with open(f"/tmp/asia/res_{region}.json","w") as f:
    json.dump(got,f,indent=2)
TODAY="2026-10-21"
fresh=[x for x in got if (x.get("last_close_utc") or "").startswith(TODAY)]
fresh.sort(key=lambda x: abs(x.get('pct') or 0), reverse=True)
print(f"=== {region}: {len(got)}/{len(universe[region])} ok, {len(fresh)} fresh ===")
for x in fresh[:18]:
    print(f"  {x['symbol']:14s} pct={x['pct']:+6.2f}  px={x['price']}")