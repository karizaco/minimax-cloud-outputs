"""Fetching helpers for Taiwan market sources."""

from __future__ import annotations

import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .parse import ParseError, parse_yahoo_rank_html


@dataclass
class SourceHealth:
    source: str
    status: str
    count: int = 0
    detail: str = ""
    url: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def fetch_url(url: str, timeout: int = 30) -> tuple[str, int]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; SIP Taiwan market adapter)",
            "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        return body.decode(charset, errors="replace"), int(response.status)


def _fixture_candidates(fixtures_dir: Path, stem: str) -> list[Path]:
    """Return local Yahoo HTML fixture files for the requested source."""
    names = [
        stem,
        f"{stem}.html",
    ]
    found: list[Path] = []
    for name in names:
        path = fixtures_dir / name
        if path.is_file() and path not in found:
            found.append(path)

    for path in sorted(fixtures_dir.glob(f"{stem}*.html")):
        if path.is_file() and path not in found:
            found.append(path)

    return found


def fetch_yahoo_ranks(
    session: str | Path = "live",
) -> tuple[list[dict[str, Any]], list[SourceHealth]]:
    health: list[SourceHealth] = []

    fixture_directory: Path | None = None
    if isinstance(session, Path):
        fixture_directory = session
    elif isinstance(session, str) and session != "live":
        candidate = Path(session)
        if candidate.is_dir():
            fixture_directory = candidate

    if fixture_directory is not None:
        paths = _fixture_candidates(fixture_directory, "yahoo-tai-turnover")
        if not paths:
            health.append(
                SourceHealth(
                    "yahoo_rank",
                    "empty",
                    detail="fixture not found: expected yahoo-*.html files",
                )
            )
            return [], health

        try:
            text = "\n".join(path.read_text(encoding="utf-8") for path in paths)
            rows = parse_yahoo_rank_html(text, allow_empty=False)
        except (OSError, ParseError) as exc:
            health.append(
                SourceHealth(
                    "yahoo_rank",
                    "blocked",
                    detail=str(exc),
                )
            )
            return [], health

        health.append(
            SourceHealth(
                "yahoo_rank",
                "ok",
                count=len(rows),
                detail=", ".join(path.name for path in paths),
            )
        )
        return rows, health

    url = "https://tw.stock.yahoo.com/quote/2330.TW/table"
    try:
        text, status_code = fetch_url(url)
        rows = parse_yahoo_rank_html(text, allow_empty=True)
        health.append(
            SourceHealth(
                "yahoo_rank",
                "ok" if rows else "empty",
                count=len(rows),
                url=url,
                detail=str(status_code),
            )
        )
        return rows, health
    except urllib.error.HTTPError as exc:
        health.append(
            SourceHealth("yahoo_rank", "blocked", detail=str(exc), url=url)
        )
    except (OSError, urllib.error.URLError, ParseError) as exc:
        health.append(
            SourceHealth("yahoo_rank", "blocked", detail=str(exc), url=url)
        )
    return [], health
