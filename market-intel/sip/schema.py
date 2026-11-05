from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

TIER_ORDER = ["A", "Soft-A", "TECH_WATCH", "B", "C"]

_REQUIRED_FIELDS = {
    "ticker",
    "venue",
    "instrument_type",
    "last",
    "chg_pct",
    "dollar_vol",
    "rvol",
    "catalyst",
    "catalyst_time",
    "flags",
    "source",
    "asof",
    "tier",
}


@dataclass(slots=True)
class CandidateRow:
    ticker: str
    venue: str
    instrument_type: str
    last: float
    chg_pct: float
    dollar_vol: float
    rvol: float | None
    catalyst: str | None
    catalyst_time: str | None
    flags: list[str] = field(default_factory=list)
    source: str = ""
    asof: str = ""
    tier: str | None = None
    company_en: str | None = None
    company_zh: str | None = None
    board: str | None = None
    mcap_twd: float | None = None
    usd_turnover: float | None = None
    display_ticker: str | None = None
    why: str | None = None
    mops_materiality: int | None = None

    def asdict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CandidateRow":
        missing = _REQUIRED_FIELDS - data.keys()
        if missing:
            raise ValueError(f"missing required fields: {', '.join(sorted(missing))}")
        values = dict(data)
        if not isinstance(values.get("flags"), list):
            values["flags"] = [] if values.get("flags") is None else list(values["flags"])
        return cls(**values)


def validate_row(row: CandidateRow) -> None:
    """Raise ValueError when a candidate violates the shared schema."""
    for name in _REQUIRED_FIELDS:
        if not hasattr(row, name):
            raise ValueError(f"missing required field: {name}")
    if not row.ticker:
        raise ValueError("ticker is required")
    if row.venue not in {"TWSE", "TPEx"}:
        raise ValueError(f"invalid venue: {row.venue}")
    if row.tier is not None and row.tier not in TIER_ORDER:
        raise ValueError(f"invalid tier: {row.tier}")
