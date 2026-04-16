from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import List, Tuple

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

Triangulation = Tuple[Tuple[int, int, int, int], ...]
Move = Tuple[int, int]
Face = Tuple[int, ...]


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def sample_triangulations() -> List[Triangulation]:
    T0 = canonical(((0, 1, 2, 3), (0, 1, 2, 4)))
    T1 = canonical(((0, 1, 2, 3), (0, 1, 3, 4), (1, 2, 3, 4)))
    T2 = canonical(((0, 1, 2, 4), (0, 2, 3, 4), (1, 2, 3, 4)))
    T3 = canonical(((0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4)))
    return [T0, T1, T2, T3]


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
        (1, 3),  # e6
        (3, 1),  # e7
        (2, 3),  # e8
        (3, 2),  # e9
        (0, 3),  # e10
        (3, 0),  # e11
    ]

    candidate_faces: List[Face] = [
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),    # 0->1->0
        (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),    # 1->2->1
        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),    # 0->2->0
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),    # 1->3->1
        (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0),    # 2->3->2
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),    # 0->3->0
        (1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),    # 0->1->2->0
        (0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1),    # 0->2->3->0
        (1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),    # 0->1->3->0
        (0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0),    # invalid on purpose; filtered out
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, -1),   # 1->2->3->0 with sign mismatch; filtered if invalid
        (0, 0, 1, 0, 0, 0, 1, 0, 0, -1, -1, 0),  # 1->2->3->1: e2 + e8 + e7
    ]

    temp = ChainComplex(vertices=vertices, edges=edges, faces=[])
    B1 = boundary_operator_1(temp)

    faces: List[Face] = []
    for face in candidate_faces:
        col = sp.Matrix(face)
        if B1 * col == sp.zeros(B1.rows, 1):
            faces.append(face)

    return ChainComplex(vertices=vertices, edges=edges, faces=faces)


def boundary_operator_1(cc: ChainComplex) -> sp.Matrix:
    nV = len(cc.vertices)
    nE = len(cc.edges)
    B1 = sp.zeros(nV, nE)
    for j, (u, v) in enumerate(cc.edges):
        B1[u, j] = -1
        B1[v, j] = 1
    return B1


def boundary_operator_2(cc: ChainComplex) -> sp.Matrix:
    nE = len(cc.edges)
    nF = len(cc.faces)
    B2 = sp.zeros(nE, nF)
    for j, face in enumerate(cc.faces):
        for i, coeff in enumerate(face):
            if i < nE:
                B2[i, j] = int(coeff)
    return B2


def _primitive_integer_vector(v: sp.Matrix) -> sp.Matrix:
    vals = [int(x) for x in list(v)]
    g = 0
    for x in vals:
        g = gcd(g, abs(x))
    if g == 0:
        return v
    vals = [x // g for x in vals]
    for x in vals:
        if x != 0:
            if x < 0:
                vals = [-y for y in vals]
            break
    return sp.Matrix(vals)


def kernel_basis_B1(cc: ChainComplex) -> List[sp.Matrix]:
    B1 = boundary_operator_1(cc)
    basis = [_primitive_integer_vector(v) for v in B1.nullspace()]
    out: List[sp.Matrix] = []
    seen = set()
    for v in basis:
        key = tuple(int(x) for x in list(v))
        if key not in seen:
            seen.add(key)
            out.append(v)
    return out


def image_generators_B2(cc: ChainComplex) -> List[sp.Matrix]:
    B2 = boundary_operator_2(cc)
    cols = [_primitive_integer_vector(B2[:, j]) for j in range(B2.cols)]
    out: List[sp.Matrix] = []
    current_cols: List[sp.Matrix] = []
    current_rank = 0
    for col in cols:
        trial_cols = current_cols + [col]
        trial = sp.Matrix.hstack(*trial_cols)
        new_rank = trial.rank()
        if new_rank > current_rank:
            out.append(col)
            current_cols = trial_cols
            current_rank = new_rank
    return out


def smith_data_B1(cc: ChainComplex):
    B1 = boundary_operator_1(cc)
    D = smith_normal_form(B1, domain=sp.ZZ)
    diag = []
    for i in range(min(D.rows, D.cols)):
        if D[i, i] != 0:
            diag.append(int(D[i, i]))
    return D, diag


def smith_data_B2(cc: ChainComplex):
    B2 = boundary_operator_2(cc)
    D = smith_normal_form(B2, domain=sp.ZZ)
    diag = []
    for i in range(min(D.rows, D.cols)):
        if D[i, i] != 0:
            diag.append(int(D[i, i]))
    return D, diag


def kernel_dimension_B1(cc: ChainComplex) -> int:
    return len(kernel_basis_B1(cc))


def rank_B2(cc: ChainComplex) -> int:
    return len(image_generators_B2(cc))


def cohomology_H0_dimension(cc: ChainComplex) -> int:
    B1 = boundary_operator_1(cc)
    return B1.rows - B1.rank()


def vector_in_span(v: sp.Matrix, basis: List[sp.Matrix]) -> bool:
    if not basis:
        return all(int(x) == 0 for x in list(v))
    A = sp.Matrix.hstack(*basis)
    try:
        A.gauss_jordan_solve(v)
        return True
    except ValueError:
        return False


def cohomology_H1_dimension(cc: ChainComplex) -> int:
    return kernel_dimension_B1(cc) - rank_B2(cc)


def explicit_H1_representative(cc: ChainComplex) -> sp.Matrix | None:
    ker_basis = kernel_basis_B1(cc)
    im_basis = image_generators_B2(cc)
    for w in ker_basis:
        if not vector_in_span(w, im_basis):
            return w
    return None


def homology_H1_torsion_invariants(cc: ChainComplex) -> List[int]:
    ker_basis = kernel_basis_B1(cc)
    im_basis = image_generators_B2(cc)

    if not ker_basis or not im_basis:
        return []

    K = sp.Matrix.hstack(*ker_basis)
    coords: List[sp.Matrix] = []
    for g in im_basis:
        try:
            sol, _ = K.gauss_jordan_solve(g)
        except ValueError:
            continue
        if any(not x.is_Integer for x in sol):
            continue
        coords.append(sp.Matrix([int(x) for x in list(sol)]))

    if not coords:
        return []

    C = sp.Matrix.hstack(*coords)
    D = smith_normal_form(C, domain=sp.ZZ)

    torsion: List[int] = []
    for i in range(min(D.rows, D.cols)):
        d = int(D[i, i])
        if d not in (0, 1):
            torsion.append(abs(d))
    return torsion
