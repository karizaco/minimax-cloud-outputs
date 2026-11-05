from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


_CONFIG_DIR = Path(__file__).resolve().parent

_REQUIRED_KEYS = (
    "gap_hard",
    "unusual_rvol",
    "soft_a_requires_catalyst",
    "catalyst_min_score",
    "tech_watch_rvol_min",
    "tech_watch_rvol_max",
    "elevated_rvol_min",
    "stale_halt_sessions",
    "overnight_carry_max_age_sessions",
    "day_move_hard",
    "day_move_soft",
    "gap_soft",
)

_REQUIRED_NESTED_KEYS = (
    ("open", "floors"),
    ("midday", "floors"),
)


def load_yaml(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        result = yaml.safe_load(handle)
    return result if isinstance(result, dict) else {}


def _require_mapping(
    config: dict[str, Any],
    key: str,
) -> dict[str, Any]:
    value = config.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"missing required configuration mapping: {key}")
    return value


def _validate(config: dict[str, Any]) -> None:
    missing = [key for key in _REQUIRED_KEYS if key not in config]
    if missing:
        raise ValueError(
            "missing required configuration keys: " + ", ".join(sorted(missing))
        )

    for parent, child in _REQUIRED_NESTED_KEYS:
        mapping = _require_mapping(config, parent)
        if child not in mapping:
            raise ValueError(
                f"missing required configuration key: {parent}.{child}"
            )

    for slot in ("open", "midday"):
        floors = _require_mapping(config, slot)["floors"]
        if not isinstance(floors, dict) or not floors:
            raise ValueError(
                f"configuration mapping {slot}.floors must not be empty"
            )


def load_market(name: str) -> dict[str, Any]:
    market = str(name).strip().lower()
    defaults = load_yaml(_CONFIG_DIR / "defaults.yaml")
    market_config = load_yaml(_CONFIG_DIR / f"{market}.yaml")
    merged = dict(defaults)
    merged.update(market_config)
    _validate(merged)
    return merged


__all__ = ["load_market", "load_yaml"]
