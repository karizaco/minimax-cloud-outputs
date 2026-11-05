from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


_CONFIG_DIR = Path(__file__).resolve().parent


def load_yaml(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        result = yaml.safe_load(handle)
    return result if isinstance(result, dict) else {}


def load_market(name: str) -> dict[str, Any]:
    market = str(name).strip().lower()
    defaults = load_yaml(_CONFIG_DIR / "defaults.yaml")
    market_config = load_yaml(_CONFIG_DIR / f"{market}.yaml")
    merged = dict(defaults)
    merged.update(market_config)
    return merged


__all__ = ["load_market", "load_yaml"]
