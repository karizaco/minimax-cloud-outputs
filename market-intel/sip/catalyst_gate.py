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
    "財報",
    "獲利",
    "每股盈餘",
    "EPS",
    "營收",
    "展望",
    "財測",
    "合併",
    "併購",
    "增資",
    "收購",
    "交換",
    "重大訊息",
    "重大消息",
    "停牌",
    "配息",
    "重整",
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


def materiality_score(headline: str) -> int:
    """Return a simple count of material catalyst indicators."""
    text = f" {str(headline or '').upper()} "
    return sum(1 for term in _MATERIAL_TERMS if term in text)


def is_boilerplate_mops(headline: str) -> bool:
    """Return True when a MOPS headline is known non-material fluff."""
    text = str(headline or "").strip().casefold()
    if not text:
        return False
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in _BOILERPLATE_PATTERNS)


__all__ = ["is_boilerplate_mops", "materiality_score"]
