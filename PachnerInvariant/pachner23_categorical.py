from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from sympy import Expr, Integer

from PachnerInvariant.fusion_category_input import FKey, FusionCategoryInput
from PachnerInvariant.pentagon_constraints import build_f_symbols


@dataclass(frozen=True)
class Pachner23Instance:
    left_keys: Tuple[FKey, ...]
    right_keys: Tuple[FKey, ...]


def categorical_amplitude(instance: Pachner23Instance, f_symbols: Dict[FKey, Expr]) -> Expr:
    prod = Integer(1)
    for key in instance.left_keys:
        prod *= f_symbols[key]
    return prod


def categorical_amplitude_rhs(instance: Pachner23Instance, f_symbols: Dict[FKey, Expr]) -> Expr:
    prod = Integer(1)
    for key in instance.right_keys:
        prod *= f_symbols[key]
    return prod


def default_pachner23_instance(fc: FusionCategoryInput) -> Pachner23Instance:
    f_symbols = build_f_symbols(fc)
    keys = tuple(sorted(f_symbols))
    if len(keys) < 2:
        raise ValueError("Need at least two F-symbol variables for categorical Pachner 2-3 test.")
    left = (keys[0],)
    right = (keys[1],)
    return Pachner23Instance(left_keys=left, right_keys=right)
