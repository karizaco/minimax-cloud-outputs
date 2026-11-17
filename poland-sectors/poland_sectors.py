#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a ticker-to-sector-and-industry map for Polish GPW and NewConnect equities."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlparse
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
GPW_URL = "https://www.biznesradar.pl/gielda/akcje_gpw"
NC_URL = "https://www.biznesradar.pl/gielda/newconnect"
BRANZA_RE = re.compile(r'href=["\']([^"\']*/gielda/branza:([a-z0-9-]+))["\']', re.I)
NOTOWANIA_RE = re.compile(r'href=["\']([^"\']*/notowania/[^"\'#?]+)["\']', re.I)
ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.I | re.S)
ANCHOR_RE = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.I | re.S)
TITLE_RE = re.compile(r'\btitle\s*=\s*["\'](.*?)["\']', re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")

SECTOR_MAP = {
    "Artykuły spożywcze": "Dobra konsumpcyjne",
    "Banki": "Finanse",
    "Biotechnologia": "Ochrona zdrowia",
    "Budownictwo": "Budownictwo i nieruchomości",
    "Chemia": "Przemysł",
    "Drewno i papier": "Przemysł",
    "Dystrybucja ciepła i wody": "Energia i utility",
    "Dystrybucja leków": "Ochrona zdrowia",
    "Działalność inwestycyjna": "Finanse",
    "Energia": "Energia i utility",
    "Górnictwo": "Surowce",
    "Gry": "Technologie",
    "Guma i tworzywa sztuczne": "Przemysł",
    "Handel hurtowy": "Handel i usługi",
    "Handel internetowy": "Handel i usługi",
    "Hutnictwo": "Surowce",
    "Informatyka": "Technologie",
    "Leasing i faktoring": "Finanse",
    "Media": "Media i telekomunikacja",
    "Motoryzacja": "Przemysł",
    "Nieruchomości": "Budownictwo i nieruchomości",
    "Nowe technologie": "Technologie",
    "Odzież i kosmetyki": "Dobra konsumpcyjne",
    "Paliwa i gaz": "Energia i utility",
    "Pośrednictwo finansowe": "Finanse",
    "Pozostałe": "Pozostałe",
    "Produkcja leków": "Ochrona zdrowia",
    "Przemysł elektromaszynowy": "Przemysł",
    "Recykling": "Przemysł",
    "Rekreacja i wypoczynek": "Handel i usługi",
    "Rynek kapitałowy": "Finanse",
    "Sieci handlowe": "Handel i usługi",
    "Sprzęt i materiały medyczne": "Ochrona zdrowia",
    "Szpitale i przychodnie": "Ochrona zdrowia",
    "Telekomunikacja": "Media i telekomunikacja",
    "Transport i logistyka": "Handel i usługi",
    "Ubezpieczenia": "Finanse",
    "Usługi dla przedsiębiorstw": "Handel i usługi",
    "Wierzytelności": "Finanse",
    "Wyposażenie domu": "Dobra konsumpcyjne",
    "Zaopatrzenie przedsiębiorstw": "Handel i usługi",
}


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAG_RE.sub(" ", value))).strip()


def norm_key(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def get_attr(attrs: str, name: str) -> str:
    match = re.search(r'\b' + re.escape(name) + r'\s*=\s*["\'](.*?)["\']', attrs, re.I | re.S)
    return html.unescape(match.group(1)).strip() if match else ""


def fetch(url: str, cache_dir: Path, refresh: bool, sleep: float) -> str:
    key = hashlib.sha256(url.encode("utf-8")).hexdigest()
    cache_file = cache_dir / (key + ".html")
    if not refresh and cache_file.is_file():
        return cache_file.read_text(encoding="utf-8", errors="replace")

    last_error: Optional[Exception] = None
    for attempt in range(2):
        try:
            request = Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
            with urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", errors="replace")
            cache_dir.mkdir(parents=True, exist_ok=True)
            tmp = cache_file.with_suffix(".tmp")
            tmp.write_text(body, encoding="utf-8")
            os.replace(tmp, cache_file)
            time.sleep(max(0.0, sleep))
            return body
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt == 0:
                time.sleep(5)
    raise RuntimeError(f"HTTP request failed after retry: {url}: {last_error}")


def parse_rows(document: str) -> List[Tuple[str, str]]:
    rows: List[Tuple[str, str]] = []
    for row_match in ROW_RE.finditer(document):
        row_html = row_match.group(1)
        for anchor_match in ANCHOR_RE.finditer(row_html):
            attrs, visible = anchor_match.groups()
            href = get_attr(attrs, "href")
            if not re.search(r"/notowania/[^/]+", href, re.I):
                continue
            text = clean_text(visible)
            if not text:
                continue
            ticker = text.split()[0]
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", ticker):
                continue
            title = clean_text(get_attr(attrs, "title"))
            if title:
                name = title
            else:
                name = re.sub(r"^\s*" + re.escape(ticker) + r"\s*(?:\([^)]*\))?", "", text).strip()
            rows.append((ticker.upper(), name))
    return rows


def parse_market(document: str, market: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for ticker, name in parse_rows(document):
        result.setdefault(ticker, name)
    return result


def discover_industries(document: str, base_url: str) -> Dict[str, str]:
    found: Dict[str, str] = {}
    for match in ANCHOR_RE.finditer(document):
        attrs, visible = match.groups()
        href = html.unescape(get_attr(attrs, "href"))
        if not re.search(r"/gielda/branza:[a-z0-9-]+/?$", href, re.I):
            continue
        slug = re.search(r"/gielda/branza:([a-z0-9-]+)", href, re.I).group(1).lower()
        label = clean_text(visible)
        if label and slug not in found:
            found[slug] = label
    return found


def fetch_market(url: str, cache_dir: Path, refresh: bool, sleep: float) -> Tuple[Dict[str, str], str]:
    pages = [url]
    seen: Set[str] = set()
    rows: Dict[str, str] = {}
    while pages:
        page_url = pages.pop(0)
        if page_url in seen:
            continue
        seen.add(page_url)
        document = fetch(page_url, cache_dir, refresh, sleep)
        for ticker, name in parse_rows(document):
            rows.setdefault(ticker, name)
        # Follow only ordinary pagination links, never comma-suffix sort links.
        for match in re.finditer(r'href=["\']([^"\']+)["\']', document, re.I):
            candidate = urljoin(page_url, html.unescape(match.group(1)))
            parsed = urlparse(candidate)
            if "," in parsed.path or parsed.query.startswith("sort"):
                continue
            if parsed.path == urlparse(page_url).path and (
                re.search(r"(?:^|&)page=\d+", parsed.query, re.I)
                or re.search(r"/page/\d+", parsed.path, re.I)
            ):
                if candidate not in seen:
                    pages.append(candidate)
    return rows, document


def fetch_industry_pages(
    industries: Dict[str, str], cache_dir: Path, refresh: bool, sleep: float
) -> Tuple[Dict[str, str], List[str], List[Tuple[str, str, str]]]:
    assignments: Dict[str, str] = {}
    failed: List[str] = []
    collisions: List[Tuple[str, str, str]] = []
    for slug, label in industries.items():
        url = f"https://www.biznesradar.pl/gielda/branza:{quote(slug)}"
        try:
            document = fetch(url, cache_dir, refresh, sleep)
            for ticker, _ in parse_rows(document):
                prev = assignments.get(ticker)
                if prev and prev != label:
                    collisions.append((ticker, prev, label))
                else:
                    assignments.setdefault(ticker, label)
        except RuntimeError as exc:
            print(f"WARNING: failed branża page {slug}: {exc}", file=sys.stderr)
            failed.append(slug)
    return assignments, failed, collisions


def write_readme(path: Path) -> None:
    text = """# Polish sectors and industries

This file maps Polish equities listed on the GPW main market and NewConnect to Biznesradar branża classifications.

- Source: Biznesradar market list pages and dynamically discovered branża pages.
- Refresh: `python3 /workspace/market-intel/bin/poland_sectors.py --refresh`
- `ticker`: exchange ticker.
- `name`: company/security name from the list page.
- `market`: `GPW` or `NC`.
- `sector`: macro-sector derived from the Branża; this is not a Biznesradar field.
- `industry`: Biznesradar branża display name.
- `isin`: intentionally blank by design; no per-ticker profile requests are made.
- `source`: data source.
- `fetched_at`: timezone-aware ISO-8601 timestamp in Asia/Bangkok.
"""
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/home/box/agent-data/shared-research/poland-sectors/poland_sectors.csv")
    parser.add_argument("--cache-dir", default="/tmp/poland-sectors-cache")
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    cache_dir = Path(args.cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    warnings: List[str] = []

    gpw, gpw_doc = fetch_market(GPW_URL, cache_dir, args.refresh, args.sleep)
    nc, nc_doc = fetch_market(NC_URL, cache_dir, args.refresh, args.sleep)

    industries = {}
    industries.update(discover_industries(gpw_doc, GPW_URL))
    industries.update(discover_industries(nc_doc, NC_URL))
    assignments, failed, collisions = fetch_industry_pages(industries, cache_dir, args.refresh, args.sleep)
    if failed:
        warnings.append("failed branża pages: " + ", ".join(failed))
    if collisions:
        warnings.append(
            "dual-industry tickers: "
            + ", ".join(f"{ticker} ({first} vs {second})" for ticker, first, second in collisions)
        )

    universe: Dict[str, Tuple[str, str]] = {}
    for ticker, name in gpw.items():
        universe[ticker] = ("GPW", name)
    for ticker, name in nc.items():
        if ticker in universe:
            warnings.append(f"ticker {ticker} appears on both markets; GPW preferred")
        else:
            universe[ticker] = ("NC", name)

    list_only = sum(1 for ticker in universe if ticker not in assignments)
    industry_counts: Counter[str] = Counter()
    sector_counts: Counter[str] = Counter()
    rows = []
    dual = []
    for ticker, (market, name) in universe.items():
        industry = assignments.get(ticker, "")
        sector_lookup = {norm_key(key): value for key, value in SECTOR_MAP.items()}
        sector = sector_lookup.get(norm_key(industry), "") if industry else ""
        if industry and norm_key(industry) not in sector_lookup:
            warnings.append(f"unmapped branża: {industry}")
            sector = "Pozostałe"
        if industry:
            industry_counts[industry] += 1
        if sector:
            sector_counts[sector] += 1
        rows.append({
            "ticker": ticker, "name": name, "market": market, "sector": sector,
            "industry": industry, "isin": "", "source": "biznesradar",
            "fetched_at": datetime.now(ZoneInfo("Asia/Bangkok")).isoformat(timespec="seconds"),
        })

    market_counts = Counter(row["market"] for row in rows)
    if list_only:
        warnings.append(f"list-only tickers without industry: {list_only}")

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_name(output.name + ".tmp")
    fields = ["ticker", "name", "market", "sector", "industry", "isin", "source", "fetched_at"]
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: (0 if row["market"] == "GPW" else 1, row["ticker"])))
    os.replace(tmp, output)
    write_readme(output.parent / "README.md")

    missing_industry = sum(not row["industry"] for row in rows)
    missing_sector = sum(not row["sector"] for row in rows)
    total = len(rows)
    print(output)
    print(f"GPW count: {market_counts['GPW']}")
    print(f"NC count: {market_counts['NC']}")
    print(f"Total: {total}")
    print(f"Missing industry: {missing_industry} ({missing_industry / total:.2%})" if total else "Missing industry: 0 (0.00%)")
    print(f"Missing sector: {missing_sector} ({missing_sector / total:.2%})" if total else "Missing sector: 0 (0.00%)")
    print("Industry counts: " + ", ".join(f"{k}={v}" for k, v in sorted(industry_counts.items())))
    print("Sector counts: " + ", ".join(f"{k}={v}" for k, v in sorted(sector_counts.items())))
    print("Warnings: " + ("; ".join(warnings) if warnings else "none"))
    return 0 if market_counts["GPW"] >= 300 and market_counts["NC"] >= 300 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
