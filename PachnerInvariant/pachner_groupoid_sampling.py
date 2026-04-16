from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Dict

import sympy as sp

Triangulation = Tuple[Tuple[int, int, int, int], ...]
Move = Tuple[int, int]


def canonical(T: Triangulation) -> Triangulation:
    return tuple(sorted(tuple(sorted(t)) for t in T))


def generate_extended_triangulations() -> List[Triangulation]:
    base = [
        ((0,1,2,3),(0,1,2,4)),
        ((0,1,2,3),(0,1,3,4),(1,2,3,4)),
        ((0,1,2,4),(0,2,3,4),(1,2,3,4)),
        ((0,1,3,4),(0,2,3,4),(1,2,3,4)),
        ((0,1,2,5),(0,2,3,5),(1,2,4,5),(2,3,4,5)),
        ((0,1,3,5),(0,3,4,5),(1,2,3,5),(2,3,4,5)),
        ((0,2,3,6),(0,1,2,6),(1,2,4,6),(2,3,4,6)),
    ]
    return [canonical(T) for T in base]


@dataclass
class GroupoidSample:
    vertices: List[Triangulation]
    edges: List[Move]


def build_groupoid_sample() -> GroupoidSample:
    vertices = generate_extended_triangulations()

    edges: List[Move] = []
    n = len(vertices)

    # naive connectivity: connect all pairs differing in size
    for i in range(n):
        for j in range(n):
            if i != j:
                if abs(len(vertices[i]) - len(vertices[j])) <= 1:
                    edges.append((i, j))

    return GroupoidSample(vertices=vertices, edges=edges)


def incidence_matrix(sample: GroupoidSample) -> sp.Matrix:
    nV = len(sample.vertices)
    nE = len(sample.edges)
    B = sp.zeros(nV, nE)
    for j, (u, v) in enumerate(sample.edges):
        B[u, j] = -1
        B[v, j] = 1
    return B


def kernel_dimension(B: sp.Matrix) -> int:
    return len(B.nullspace())


def rank(B: sp.Matrix) -> int:
    return B.rank()
