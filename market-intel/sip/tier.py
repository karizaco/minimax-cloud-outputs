from __future__ import annotations

from typing import Any, Iterable

from .catalyst_gate import is_boilerplate_mops, materiality_score
from .schema import CandidateRow, TIER_ORDER, validate_row

_NOISE_TYPES = {"etf", "warrant", "pref", "emerging", "tdr", "fund_wrapper"}
_C_MATERIAL_FLAGS = {"LIMIT_UP", "LIMIT_DOWN", "TOB_GAP", "HALT"}


def normalize_rows(rows: Iterable[dict[str, Any] | CandidateRow]) -> list[CandidateRow]:
    result: list[CandidateRow] = []
    for row in rows:
        candidate = row if isinstance(row, CandidateRow) else CandidateRow.from_dict(row)
        validate_row(candidate)
        result.append(candidate)
    return result


def _key(row: CandidateRow) -> tuple[str, str]:
    return (row.display_ticker or row.ticker).upper(), row.ticker.upper()


def dedupe(rows: Iterable[CandidateRow]) -> list[CandidateRow]:
    chosen: dict[tuple[str, str], CandidateRow] = {}
    for row in rows:
        key = _key(row)
        if key not in chosen or row.dollar_vol > chosen[key].dollar_vol:
            chosen[key] = row
    return list(chosen.values())


def _floors(cfg: dict[str, Any], slot: str) -> dict[str, float]:
    section = cfg.get(slot, {})
    return section.get("floors", section) if isinstance(section, dict) else {}


def apply_floors(
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any],
    slot: str,
) -> list[CandidateRow]:
    floors = _floors(cfg, slot)
    price_min = float(floors.get("price_min", 0))
    turnover_min = float(floors.get("turnover_min", 0))
    mcap_min = float(floors.get("mcap_min", 0))

    result: list[CandidateRow] = []
    for row in rows:
        if row.last < price_min:
            continue
        if row.dollar_vol < turnover_min:
            continue
        result.append(row)
    return result


def drop_noise(rows: Iterable[CandidateRow]) -> list[CandidateRow]:
    result: list[CandidateRow] = []
    for row in rows:
        if row.instrument_type.lower() in _NOISE_TYPES:
            continue
        if any(flag.lower() in _NOISE_TYPES for flag in row.flags):
            continue
        result.append(row)
    return result


def _has_catalyst(row: CandidateRow) -> bool:
    return bool(row.catalyst and str(row.catalyst).strip())


def _is_material_catalyst(row: CandidateRow, min_score: float = 1) -> bool:
    if not _has_catalyst(row):
        return False
    text = str(row.catalyst)
    if is_boilerplate_mops(text):
        return False

    score = getattr(row, "mops_materiality", None)
    if score is None:
        score = materiality_score(text)
    try:
        return float(score) >= float(min_score)
    except (TypeError, ValueError):
        return False


def _has_flag(row: CandidateRow, *names: str) -> bool:
    wanted = {name.upper() for name in names}
    return any(str(flag).upper() in wanted for flag in row.flags)


def assign_tiers(
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any],
    slot: str,
) -> list[CandidateRow]:
    result: list[CandidateRow] = []
    requires_catalyst = bool(cfg.get("soft_a_requires_catalyst", True))
    catalyst_min_score = float(cfg.get("catalyst_min_score", 1))

    for row in rows:
        move = abs(float(row.chg_pct))
        hard = float(cfg.get("day_move_hard", 4.0))
        soft = float(cfg.get("day_move_soft", 4.0))
        gap_soft = float(cfg.get("gap_soft", 3.0))
        elevated = float(cfg.get("elevated_rvol_min", 1.5))
        rmin = float(cfg.get("tech_watch_rvol_min", 0.3))
        rmax = float(cfg.get("tech_watch_rvol_max", 2.0))
        liquid_turnover_min = float(
            cfg.get("tech_watch_liquid_turnover_min", 2_500_000_000)
        )
        tech_watch_move_min = float(cfg.get("tech_watch_move_min", 2.0))

        catalyst = _has_catalyst(row)
        material_catalyst = _is_material_catalyst(row, catalyst_min_score)
        limit_down = _has_flag(row, "LIMIT_DOWN")
        limit_up = _has_flag(row, "LIMIT_UP")
        limit_move = limit_up or limit_down
        material_move = move >= soft or limit_move
        hard_move = move >= hard or limit_move

        if limit_down:
            tier = "C"
        elif material_catalyst and material_move:
            if row.rvol is not None and row.rvol >= elevated:
                tier = "A"
            elif hard_move:
                tier = "Soft-A"
            else:
                tier = "B"
        elif limit_up:
            # LIMIT_UP without a material catalyst is a limit/halt watch.
            # It must not be promoted into TECH_WATCH/B by the rvol band.
            tier = "C"
        elif (
            catalyst
            and not material_catalyst
            and not requires_catalyst
            and material_move
        ):
            tier = "B"
        elif (
            not catalyst
            or (requires_catalyst and not material_catalyst)
        ):
            is_liquid = float(row.dollar_vol or 0) >= liquid_turnover_min
            move_ok = (
                (move >= tech_watch_move_min or limit_up)
                if is_liquid
                else (move >= gap_soft or limit_up)
            )
            if move_ok:
                r = row.rvol
                if r is not None and r >= rmax:
                    tier = "B"
                elif r is not None and rmin <= r < rmax:
                    tier = "TECH_WATCH"
                else:
                    tier = "C"
            elif (
                row.rvol is not None
                and row.rvol >= elevated
                and move >= 2.0
            ):
                tier = "B"
            else:
                tier = "C"
        else:
            tier = "C"

        row.tier = tier
        result.append(row)
    return result


def sort_tiers(rows: Iterable[CandidateRow]) -> list[CandidateRow]:
    order = {name: index for index, name in enumerate(TIER_ORDER)}
    return sorted(
        rows,
        key=lambda row: (order.get(row.tier or "C", len(order)), -row.dollar_vol),
    )


def _has_material_c_flag(row: CandidateRow) -> bool:
    for flag in row.flags:
        normalized = str(flag).upper()
        if normalized in _C_MATERIAL_FLAGS:
            return True
        if normalized.startswith("OVERNIGHT_PROMOTED"):
            return True
        if normalized.startswith("TOB_GAP"):
            return True
        if normalized.startswith("HALT"):
            return True
    return False


def _has_non_limit_material_c_flag(row: CandidateRow) -> bool:
    for flag in row.flags:
        normalized = str(flag).upper()
        if normalized in {"TOB_GAP", "HALT"}:
            return True
        if normalized.startswith("OVERNIGHT_PROMOTED"):
            return True
        if normalized.startswith("TOB_GAP"):
            return True
        if normalized.startswith("HALT"):
            return True
    return False


def _c_limit_usd_turnover(row: CandidateRow, cfg: dict[str, Any]) -> float | None:
    value = getattr(row, "usd_turnover", None)
    if value is not None:
        try:
            parsed = float(value)
            return parsed if parsed >= 0 else None
        except (TypeError, ValueError):
            pass

    fx = cfg.get("fx")
    try:
        rate = float(fx)
    except (TypeError, ValueError):
        return None
    if rate <= 0:
        return None
    return float(row.dollar_vol or 0) / rate


def trim_c_watch(
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any],
) -> list[CandidateRow]:
    """Keep material C watches.

    The explicit ``c_limit_usd_min`` setting enables the Taiwan-style USD
    floor. Without that setting, retain the prior count-capped behavior.
    """
    result = list(rows)

    if "c_limit_usd_min" not in cfg:
        cap_value = (cfg.get("engine_top_n") or {}).get(
            "C", (cfg.get("digest_top_n") or {}).get("C", 8)
        )
        cap = max(0, int(cap_value))
        selected_c = sorted(
            [
                row
                for row in result
                if row.tier == "C" and _has_material_c_flag(row)
            ],
            key=lambda row: (-float(row.dollar_vol or 0), row.ticker),
        )[:cap]
        selected_ids = {id(row) for row in selected_c}
        return [
            row
            for row in result
            if row.tier != "C" or id(row) in selected_ids
        ]

    threshold = float(cfg.get("c_limit_usd_min", 50_000_000))
    selected_c: list[CandidateRow] = []
    for row in result:
        if row.tier != "C" or not _has_material_c_flag(row):
            continue

        flags = {str(flag).upper() for flag in row.flags}
        daily_limit = "LIMIT_UP" in flags or "LIMIT_DOWN" in flags
        if not daily_limit:
            selected_c.append(row)
            continue

        usd_turnover = _c_limit_usd_turnover(row, cfg)
        if usd_turnover is not None and usd_turnover >= threshold:
            selected_c.append(row)
        elif _has_non_limit_material_c_flag(row):
            selected_c.append(row)

    selected_c = sorted(
        selected_c,
        key=lambda row: (-float(row.dollar_vol or 0), row.ticker),
    )
    selected_ids = {id(row) for row in selected_c}
    return [
        row
        for row in result
        if row.tier != "C" or id(row) in selected_ids
    ]


def run_pipeline(
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any],
    slot: str,
) -> list[CandidateRow]:
    result = normalize_rows(rows)
    result = drop_noise(result)
    result = dedupe(result)
    result = apply_floors(result, cfg, slot)
    result = assign_tiers(result, cfg, slot)
    result = trim_c_watch(result, cfg)
    return sort_tiers(result)
