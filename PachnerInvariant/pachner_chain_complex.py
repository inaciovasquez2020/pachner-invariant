from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

Triangulation = Tuple[Tuple[int, int, int, int], ...]


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def pachner23(T: Triangulation) -> Triangulation:
    return canonical(((0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)))


def sample_triangulations() -> List[Triangulation]:
    T0 = canonical(((0,1,2,3),(0,1,2,4)))
    T1 = pachner23(T0)
    return [T0, T1]


@dataclass
class ChainComplex:
    vertices: List[Triangulation]
    edges: List[Tuple[int,int]]  # directed moves


def build_chain_complex() -> ChainComplex:
    Ts = sample_triangulations()
    index = {T:i for i,T in enumerate(Ts)}
    edges: List[Tuple[int,int]] = []
    for T in Ts:
        T2 = pachner23(T)
        if T2 in index:
            edges.append((index[T], index[T2]))
    return ChainComplex(vertices=Ts, edges=edges)


def boundary_operator_1(cc: ChainComplex) -> np.ndarray:
    nV = len(cc.vertices)
    nE = len(cc.edges)
    B = np.zeros((nV, nE), dtype=int)
    for j,(u,v) in enumerate(cc.edges):
        B[u,j] = -1
        B[v,j] = 1
    return B


def cohomology_H0_dimension(cc: ChainComplex) -> int:
    B = boundary_operator_1(cc)
    rank = np.linalg.matrix_rank(B)
    nV = B.shape[0]
    return nV - rank
