from __future__ import annotations

from typing import Any, Iterable

from .schema import CandidateRow, TIER_ORDER, validate_row

_NOISE_TYPES = {"etf", "warrant", "pref", "emerging", "tdr", "fund_wrapper"}


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

        # Market-cap is a soft warning only. A row below the market-cap
        # minimum remains eligible when it clears the turnover floor.
        if (
            row.mcap_twd is not None
            and row.mcap_twd < mcap_min
            and row.dollar_vol >= turnover_min
        ):
            pass

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


def _has_flag(row: CandidateRow, *names: str) -> bool:
    wanted = {name.upper() for name in names}
    return any(str(flag).upper() in wanted for flag in row.flags)


def assign_tiers(
    rows: Iterable[CandidateRow],
    cfg: dict[str, Any],
    slot: str,
) -> list[CandidateRow]:
    result: list[CandidateRow] = []
    for row in rows:
        if _has_flag(row, "LIMIT_DOWN"):
            row.tier = "C"
            result.append(row)
            continue

        move = abs(float(row.chg_pct))
        hard = float(cfg.get("day_move_hard", 5.0))
        soft = float(cfg.get("day_move_soft", 4.0))
        gap_soft = float(cfg.get("gap_soft", 3.0))
        elevated = float(cfg.get("elevated_rvol_min", 1.5))
        rmax = float(cfg.get("tech_watch_rvol_max", 2.0))

        catalyst = _has_catalyst(row)
        limit_move = _has_flag(row, "LIMIT_UP", "LIMIT_DOWN")
        material_move = move >= soft or limit_move
        hard_move = move >= hard or limit_move

        if catalyst and material_move:
            if row.rvol is not None and row.rvol >= elevated:
                tier = "A"
            elif hard_move:
                tier = "Soft-A"
            else:
                tier = "B"
        elif not catalyst and (move >= gap_soft or limit_move):
            if row.rvol is not None and row.rvol >= elevated:
                tier = "B"
            elif row.chg_pct > 0:
                tier = "B"
            else:
                tier = "TECH_WATCH"
        elif not catalyst and row.rvol is not None and row.rvol >= elevated:
            tier = "B"
        else:
            tier = "C"

        row.tier = tier
        result.append(row)
    return result


def sort_tiers(rows: Iterable[CandidateRow]) -> list[CandidateRow]:
    order = {name: index for index, name in enumerate(TIER_ORDER)}
    return sorted(
        rows,
        key=lambda row: (
            order.get(row.tier or "C", len(order)),
            -row.dollar_vol,
        ),
    )


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
    return sort_tiers(result)
