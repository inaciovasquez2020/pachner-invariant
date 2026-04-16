from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

Simple = str
Triple = Tuple[Simple, Simple, Simple]
Quad = Tuple[Simple, Simple, Simple, Simple]
FKey = Tuple[Simple, Simple, Simple, Simple, Simple, Simple, Simple]


@dataclass(frozen=True)
class FusionCategoryInput:
    simples: Tuple[Simple, ...]
    unit: Simple
    fusion: Dict[Triple, Tuple[Simple, ...]]

    def fusion_outputs(self, a: Simple, b: Simple, c: Simple) -> Tuple[Simple, ...]:
        return tuple(self.fusion.get((a, b, c), ()))


def all_fs_keys(fc: FusionCategoryInput) -> List[FKey]:
    keys: List[FKey] = []
    S = fc.simples
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    lhs = set(fc.fusion_outputs(a, b, d))
                    mid = set(fc.fusion_outputs(b, c, d))
                    for e in lhs:
                        for f in mid:
                            for u in fc.fusion_outputs(a, f, d):
                                if u == e:
                                    for x in fc.fusion_outputs(a, b, e):
                                        if x == f:
                                            keys.append((a, b, c, d, e, f, u))
    out = sorted(set(keys))
    return out


def fibonacci_category() -> FusionCategoryInput:
    tau = "tau"
    one = "1"
    fusion = {
        (one, one, one): (one,),
        (one, tau, tau): (tau,),
        (tau, one, tau): (tau,),
        (tau, tau, one): (one,),
        (tau, tau, tau): (tau,),
    }
    return FusionCategoryInput(simples=(one, tau), unit=one, fusion=fusion)
