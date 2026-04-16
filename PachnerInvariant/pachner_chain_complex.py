from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

Triangulation = Tuple[Tuple[int, int, int, int], ...]


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def pachner23(T: Triangulation) -> Triangulation:
    return canonical(((0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)))


def pachner32(T: Triangulation) -> Triangulation:
    return canonical(((0,1,2,3),(0,1,2,4)))


def sample_triangulations() -> List[Triangulation]:
    T0 = canonical(((0,1,2,3),(0,1,2,4)))
    T1 = pachner23(T0)
    return [T0, T1]


@dataclass
class ChainComplex:
    vertices: List[Triangulation]
    edges: List[Tuple[int,int]]
    faces: List[Tuple[int,int,int]]  # compositional relations


def build_chain_complex() -> ChainComplex:
    Ts = sample_triangulations()
    index = {T:i for i,T in enumerate(Ts)}

    edges: List[Tuple[int,int]] = []
    for T in Ts:
        i = index[T]

        T2 = pachner23(T)
        if T2 in index:
            edges.append((i, index[T2]))

        T3 = pachner32(T)
        if T3 in index:
            edges.append((i, index[T3]))

    # simple compositional relation: 2-3 followed by 3-2
    faces: List[Tuple[int,int,int]] = []
    if len(edges) >= 2:
        faces.append((0,1,0))

    return ChainComplex(vertices=Ts, edges=edges, faces=faces)


def boundary_operator_1(cc: ChainComplex) -> np.ndarray:
    nV = len(cc.vertices)
    nE = len(cc.edges)
    B = np.zeros((nV, nE), dtype=int)
    for j,(u,v) in enumerate(cc.edges):
        B[u,j] = -1
        B[v,j] = 1
    return B


def boundary_operator_2(cc: ChainComplex) -> np.ndarray:
    nE = len(cc.edges)
    nF = len(cc.faces)
    B = np.zeros((nE, nF), dtype=int)
    for j,(a,b,c) in enumerate(cc.faces):
        if a < nE: B[a,j] = 1
        if b < nE: B[b,j] = -1
        if c < nE: B[c,j] = 1
    return B


def cohomology_H0_dimension(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    rank = np.linalg.matrix_rank(B1)
    return B1.shape[0] - rank


def cohomology_H1_dimension(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    B2 = boundary_operator_2(cc)

    rank_B1 = np.linalg.matrix_rank(B1)
    rank_B2 = np.linalg.matrix_rank(B2)

    nE = B1.shape[1]
    return nE - rank_B1 - rank_B2
