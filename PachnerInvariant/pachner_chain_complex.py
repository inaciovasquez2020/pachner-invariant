from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

Triangulation = Tuple[Tuple[int, int, int, int], ...]
Move = Tuple[int, int]          # directed edge in sampled move graph
Face = Tuple[int, ...]          # signed move-composition relation on C1 basis


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def pachner23(T: Triangulation) -> Triangulation:
    if canonical(T) != canonical(((0, 1, 2, 3), (0, 1, 2, 4))):
        return canonical(T)
    return canonical(((0, 1, 2, 3), (0, 1, 3, 4), (1, 2, 3, 4)))


def pachner32(T: Triangulation) -> Triangulation:
    if canonical(T) != canonical(((0, 1, 2, 3), (0, 1, 3, 4), (1, 2, 3, 4))):
        return canonical(T)
    return canonical(((0, 1, 2, 3), (0, 1, 2, 4)))


def sample_triangulations() -> List[Triangulation]:
    T0 = canonical(((0, 1, 2, 3), (0, 1, 2, 4)))
    T1 = pachner23(T0)
    return [T0, T1]


@dataclass
class ChainComplex:
    vertices: List[Triangulation]
    edges: List[Move]
    faces: List[Face]


def build_chain_complex() -> ChainComplex:
    vertices = sample_triangulations()
    index = {T: i for i, T in enumerate(vertices)}

    T0, T1 = vertices
    assert pachner23(T0) == T1
    assert pachner32(T1) == T0

    edges: List[Move] = [
        (index[T0], index[T1]),  # e0 : T0 -> T1
        (index[T1], index[T0]),  # e1 : T1 -> T0
    ]

    # Genuine move-composition relation:
    # the loop (T0 -> T1 -> T0) has zero boundary in C0.
    faces: List[Face] = [
        (1, 1),   # e0 + e1
    ]

    return ChainComplex(vertices=vertices, edges=edges, faces=faces)


def boundary_operator_1(cc: ChainComplex) -> np.ndarray:
    nV = len(cc.vertices)
    nE = len(cc.edges)
    B1 = np.zeros((nV, nE), dtype=int)
    for j, (u, v) in enumerate(cc.edges):
        B1[u, j] = -1
        B1[v, j] = 1
    return B1


def boundary_operator_2(cc: ChainComplex) -> np.ndarray:
    nE = len(cc.edges)
    nF = len(cc.faces)
    B2 = np.zeros((nE, nF), dtype=int)
    for j, face in enumerate(cc.faces):
        for i, coeff in enumerate(face):
            if i < nE:
                B2[i, j] = coeff
    return B2


def kernel_dimension_B1(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    rank_B1 = np.linalg.matrix_rank(B1)
    return B1.shape[1] - rank_B1


def rank_B2(cc: ChainComplex) -> int:
    B2 = boundary_operator_2(cc)
    return np.linalg.matrix_rank(B2)


def cohomology_H0_dimension(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    rank_im_d1 = np.linalg.matrix_rank(B1)
    return B1.shape[0] - rank_im_d1


def cohomology_H1_dimension(cc: ChainComplex) -> int:
    kdim = kernel_dimension_B1(cc)
    r2 = rank_B2(cc)
    return kdim - r2
