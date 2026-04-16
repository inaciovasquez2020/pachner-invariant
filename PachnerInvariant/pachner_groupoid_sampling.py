from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import sympy as sp

Triangulation = Tuple[Tuple[int, int, int, int], ...]
Move = Tuple[int, int]
Path2 = Tuple[int, int]


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
    paths2: List[Path2]


def build_groupoid_sample() -> GroupoidSample:
    vertices = generate_extended_triangulations()
    n = len(vertices)

    edges: List[Move] = []
    for i in range(n):
        for j in range(n):
            if i != j and abs(len(vertices[i]) - len(vertices[j])) <= 1:
                edges.append((i, j))

    paths2: List[Path2] = []
    for a, (u, v) in enumerate(edges):
        for b, (v2, w) in enumerate(edges):
            if v == v2:
                paths2.append((a, b))

    return GroupoidSample(vertices=vertices, edges=edges, paths2=paths2)


def incidence_matrix(sample: GroupoidSample) -> sp.Matrix:
    nV = len(sample.vertices)
    nE = len(sample.edges)
    B = sp.zeros(nV, nE)
    for j, (u, v) in enumerate(sample.edges):
        B[u, j] = -1
        B[v, j] = 1
    return B


def path_boundary_matrix(sample: GroupoidSample) -> sp.Matrix:
    nE = len(sample.edges)
    nP = len(sample.paths2)
    B2 = sp.zeros(nE, nP)
    for j, (a, b) in enumerate(sample.paths2):
        u, v = sample.edges[a]
        v2, w = sample.edges[b]
        if v != v2:
            continue
        for k, (x, y) in enumerate(sample.edges):
            if (x, y) == (u, w):
                B2[k, j] += 1
        B2[a, j] -= 1
        B2[b, j] -= 1
    return B2


def kernel_dimension(B: sp.Matrix) -> int:
    return len(B.nullspace())


def rank(B: sp.Matrix) -> int:
    return B.rank()


def connected_components(sample: GroupoidSample) -> int:
    n = len(sample.vertices)
    adj = [[] for _ in range(n)]
    for u, v in sample.edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * n
    comps = 0
    for i in range(n):
        if seen[i]:
            continue
        comps += 1
        stack = [i]
        seen[i] = True
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    stack.append(y)
    return comps
