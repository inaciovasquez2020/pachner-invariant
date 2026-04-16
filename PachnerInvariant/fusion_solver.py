from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import Eq, Integer, solve

from PachnerInvariant.fusion_category_input import fibonacci_category
from PachnerInvariant.pachner23_categorical import (
    categorical_amplitude,
    categorical_amplitude_rhs,
    default_pachner23_instance,
)
from PachnerInvariant.pentagon_constraints import build_pentagon_constraints


@dataclass(frozen=True)
class SolverResult:
    variable_count: int
    pentagon_equation_count: int
    solution_count: int
    has_nontrivial_solution: bool


def solve_fusion_category_system() -> SolverResult:
    fc = fibonacci_category()
    system = build_pentagon_constraints(fc)
    instance = default_pachner23_instance(fc)

    f_symbols = system.variables
    invariance_eq = Eq(
        categorical_amplitude(instance, f_symbols),
        categorical_amplitude_rhs(instance, f_symbols),
    )

    nonzero_anchor_key = next(iter(f_symbols))
    anchored_eq = Eq(f_symbols[nonzero_anchor_key], Integer(1))

    equations = list(system.pentagon_equations) + [invariance_eq, anchored_eq]
    unknowns = list(f_symbols.values())
    sols = solve(equations, unknowns, dict=True)

    return SolverResult(
        variable_count=len(unknowns),
        pentagon_equation_count=len(system.pentagon_equations),
        solution_count=len(sols),
        has_nontrivial_solution=bool(sols),
    )
