"""Shared materiality and boilerplate checks for MOPS catalysts."""

from __future__ import annotations

import re


_MATERIAL_TERMS = (
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "QUARTER",
    "EARNINGS",
    "EPS",
    "GUIDANCE",
    "MERGER",
    "ACQUISITION",
    "M&A",
    "DIVIDEND",
    "RESTRUCTUR",
    "SWAP",
    "HALT",
    "MATERIAL",
    "SIGNIFICANT",
    "BUYBACK",
    "REPURCHASE",
    "TREASURY",
    "財報",
    "財務報告",
    "獲利",
    "每股盈餘",
    "EPS",
    "營收",
    "營業額",
    "營業收入",
    "業績",
    "展望",
    "財測",
    "併購",
    "增資",
    "收購",
    "交換",
    "協議安排",
    "重大訊息",
    "重大消息",
    "停牌",
    "配息",
    "重整",
    "庫藏股",
    "買回",
)

_ACQUISITION_TERMS = (
    "收購",
    "併購",
    "ACQUISITION",
    "MERGER",
    "M&A",
    "BUYBACK",
    "REPURCHASE",
    "TREASURY",
    "庫藏股",
    "買回",
    "協議安排",
)

_EARNINGS_TERMS = (
    "財報",
    "財務報告",
    "EPS",
    "EARNINGS",
    "QUARTER",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "業績",
    "獲利",
    "每股盈餘",
    "營收",
    "營業額",
    "營業收入",
)

_BOILERPLATE_PATTERNS = (
    r"取得有價證券",
    r"處分有價證券",
    r"取得機器設備",
    r"廠務工程",
    r"內部稽核主管",
    r"法人董事改派",
    r"董事改派",
    r"限制員工權利新股",
    r"轉換公司債",
    r"到期還本",
    r"從事衍生性商品",
    r"受邀參加.*法人說明會",
    r"announcement of attendance",
    r"attendance.*(?:investor|analyst).*conference",
    r"(?:investor|analyst).*conference.*attendance",
)

_MEDIA_CLARIFICATION = re.compile(
    r"(?:說明|澄清).*?(?:媒體.*?)?報導",
    re.IGNORECASE,
)

_QUOTED_TEXT = re.compile(
    r"[「『“\"'][\s\S]*?[」』”\"']",
)

_LEGAL_FOOTER = re.compile(
    r"本則重大訊息同時符合[\s\S]*",
    re.IGNORECASE,
)

_TEMPLATE_PHRASES = re.compile(
    r"(?:發佈|發布)重大(?:訊息|消息)(?:澄清)?",
    re.IGNORECASE,
)

_MATERIAL_EXCERPT_TERMS = tuple(
    dict.fromkeys(_ACQUISITION_TERMS + _EARNINGS_TERMS)
)


def _is_media_clarification(headline: str) -> bool:
    return bool(_MEDIA_CLARIFICATION.search(str(headline or "")))


def _clean_explanation(headline: str, explanation: str = "") -> str:
    """Remove MOPS template/footer text and quoted press-report content."""
    text = str(explanation or "")
    text = _LEGAL_FOOTER.sub("", text)
    text = _TEMPLATE_PHRASES.sub("", text)

    if _is_media_clarification(headline):
        text = _QUOTED_TEXT.sub(" ", text)
        text = re.sub(
            r"(?:媒體)?報導內容\s*[:：][^\n]*",
            " ",
            text,
            flags=re.IGNORECASE,
        )

    # A field containing only this generic label carries no catalyst signal.
    text = re.sub(
        r"(?m)^\s*(?:重大訊息|重大消息)\s*[:：]?\s*$",
        " ",
        text,
    )
    return re.sub(r"\s+", " ", text).strip()


def _text(headline: str, explanation: str = "") -> str:
    return f"{str(headline or '')} {_clean_explanation(headline, explanation)}".upper()


def materiality_class(headline: str, explanation: str = "") -> int:
    """Return a filing class: acquisition, earnings, ordinary, or immaterial."""
    text = _text(headline, explanation)

    # 合併營收 / 合併營業額 is consolidated revenue, not a merger.
    if re.search(r"合併\s*(?:營收|營業額|營業收入|收入)", text):
        text = re.sub(
            r"合併\s*(?:營收|營業額|營業收入|收入)",
            " ",
            text,
        )

    if any(term in text for term in _ACQUISITION_TERMS):
        return 3
    if any(term in text for term in _EARNINGS_TERMS):
        return 2
    return 1 if text.strip() else 0


def materiality_score(headline: str, explanation: str = "") -> int:
    """Return a simple count of material catalyst indicators."""
    text = _text(headline, explanation)
    return sum(1 for term in _MATERIAL_TERMS if term in text)


def is_boilerplate_mops(headline: str, explanation: str = "") -> bool:
    """Return True when a MOPS filing is known non-material fluff."""
    text = str(headline or "").strip().casefold()
    if not text:
        return False
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in _BOILERPLATE_PATTERNS)


def visible_excerpt(headline: str, explanation: str = "", limit: int = 120) -> str:
    """Return a short, sourced explanation suitable for a visible catalyst."""
    text = _clean_explanation(headline, explanation)
    if not text:
        return ""

    segments = [
        segment.strip()
        for segment in re.split(r"[。；;\n]+", text)
        if segment.strip()
    ]
    matching = [
        segment
        for segment in segments
        if any(term.casefold() in segment.casefold() for term in _MATERIAL_EXCERPT_TERMS)
    ]
    excerpt = matching[0] if matching else segments[0]

    if len(excerpt) > limit:
        focus = re.search(
            r"收購|併購|協議安排|合併\s*(?:營收|營業額|營業收入)|營收|營業額|業績|財報",
            excerpt,
            re.IGNORECASE,
        )
        if focus:
            start = max(0, focus.start() - 35)
            excerpt = excerpt[start : start + limit]
        else:
            excerpt = excerpt[:limit]
    return excerpt.strip()


__all__ = [
    "is_boilerplate_mops",
    "materiality_class",
    "materiality_score",
    "visible_excerpt",
]
