from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Eq, Symbol

from PachnerInvariant.fusion_category_input import FKey, FusionCategoryInput, all_fs_keys


@dataclass(frozen=True)
class PentagonConstraintSystem:
    variables: Dict[FKey, Symbol]
    pentagon_equations: Tuple[Eq, ...]


def build_f_symbols(fc: FusionCategoryInput) -> Dict[FKey, Symbol]:
    out: Dict[FKey, Symbol] = {}
    for key in all_fs_keys(fc):
        a, b, c, d, e, f, u = key
        name = f"F_{a}_{b}_{c}_{d}_{e}_{f}_{u}"
        out[key] = Symbol(name)
    return out


def build_pentagon_constraints(fc: FusionCategoryInput) -> PentagonConstraintSystem:
    vars_by_key = build_f_symbols(fc)
    eqs: List[Eq] = []

    S = fc.simples
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    for u in S:
                        for x in S:
                            lhs_terms = []
                            rhs_terms = []

                            for e in fc.fusion_outputs(a, b, x):
                                for f in fc.fusion_outputs(x, c, u):
                                    k1 = (a, b, c, u, e, f, x)
                                    if k1 in vars_by_key:
                                        lhs_terms.append(vars_by_key[k1])

                            for y in S:
                                for g in fc.fusion_outputs(b, c, y):
                                    for h in fc.fusion_outputs(a, y, u):
                                        k2 = (b, c, d, u, g, h, y)
                                        if k2 in vars_by_key:
                                            rhs_terms.append(vars_by_key[k2])

                            if lhs_terms or rhs_terms:
                                eqs.append(Eq(sum(lhs_terms), sum(rhs_terms)))

    return PentagonConstraintSystem(
        variables=vars_by_key,
        pentagon_equations=tuple(eqs),
    )
