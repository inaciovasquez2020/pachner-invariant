from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

Triangulation = Tuple[Tuple[int, int, int, int], ...]
Move = Tuple[int, int]
Face = Tuple[int, ...]


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def sample_triangulations() -> List[Triangulation]:
    T0 = canonical(((0, 1, 2, 3), (0, 1, 2, 4)))
    T1 = canonical(((0, 1, 2, 3), (0, 1, 3, 4), (1, 2, 3, 4)))
    T2 = canonical(((0, 1, 2, 4), (0, 2, 3, 4), (1, 2, 3, 4)))
    return [T0, T1, T2]


@dataclass
class ChainComplex:
    vertices: List[Triangulation]
    edges: List[Move]
    faces: List[Face]


def build_chain_complex() -> ChainComplex:
    vertices = sample_triangulations()

    edges: List[Move] = [
        (0, 1),  # e0
        (1, 0),  # e1
        (1, 2),  # e2
        (2, 1),  # e3
        (0, 2),  # e4
        (2, 0),  # e5
    ]

    faces: List[Face] = [
        (1, 1, 0, 0, 0, 0),   # e0 + e1
        (0, 0, 1, 1, 0, 0),   # e2 + e3
        (0, 0, 0, 0, 1, 1),   # e4 + e5
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


def integer_nullspace_basis(M: np.ndarray) -> List[np.ndarray]:
    M = np.asarray(M, dtype=float)
    u, s, vh = np.linalg.svd(M)
    rank = int((s > 1e-10).sum())
    basis: List[np.ndarray] = []
    for row in vh[rank:]:
        rounded = np.rint(row).astype(int)
        if np.allclose(M @ rounded, 0):
            basis.append(rounded)
        else:
            scaled = row / np.max(np.abs(row[np.abs(row) > 1e-12]))
            candidate = np.rint(10 * scaled).astype(int)
            if np.allclose(M @ candidate, 0):
                basis.append(candidate)
    cleaned: List[np.ndarray] = []
    for v in basis:
        if not any(np.array_equal(v, w) for w in cleaned):
            cleaned.append(v)
    return cleaned


def kernel_basis_B1(cc: ChainComplex) -> List[np.ndarray]:
    B1 = boundary_operator_1(cc)
    return integer_nullspace_basis(B1)


def image_basis_B2(cc: ChainComplex) -> List[np.ndarray]:
    B2 = boundary_operator_2(cc)
    cols = [B2[:, j].astype(int) for j in range(B2.shape[1])]
    basis: List[np.ndarray] = []
    if not cols:
        return basis
    current = np.zeros((B2.shape[0], 0), dtype=int)
    current_rank = 0
    for col in cols:
        trial = np.column_stack([current, col]) if current.size else col.reshape(-1, 1)
        rank = np.linalg.matrix_rank(trial.astype(float))
        if rank > current_rank:
            basis.append(col)
            current = trial
            current_rank = rank
    return basis


def kernel_dimension_B1(cc: ChainComplex) -> int:
    return len(kernel_basis_B1(cc))


def rank_B2(cc: ChainComplex) -> int:
    return len(image_basis_B2(cc))


def cohomology_H0_dimension(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    rank_im_d1 = np.linalg.matrix_rank(B1.astype(float))
    return B1.shape[0] - rank_im_d1


def vector_in_span(v: np.ndarray, basis: List[np.ndarray]) -> bool:
    if not basis:
        return np.all(v == 0)
    A = np.column_stack(basis).astype(float)
    x, _, _, _ = np.linalg.lstsq(A, v.astype(float), rcond=None)
    return np.allclose(A @ x, v.astype(float))


def cohomology_H1_dimension(cc: ChainComplex) -> int:
    return kernel_dimension_B1(cc) - rank_B2(cc)


def explicit_H1_representative(cc: ChainComplex) -> np.ndarray | None:
    ker_basis = kernel_basis_B1(cc)
    im_basis = image_basis_B2(cc)
    for w in ker_basis:
        if not vector_in_span(w, im_basis):
            return w
    return None
