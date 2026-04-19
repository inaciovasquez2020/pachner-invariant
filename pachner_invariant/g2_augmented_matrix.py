from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple, Iterable, Set
from collections import defaultdict
import itertools

from f2_certify import (
    enumerate_g2_layer,
    build_g2_graph,
    f2_row_reduce,
    tetrahedron_surface,
)

Vertex = str
Edge = Tuple[str, str]
Generator = Tuple[str, str, int]
RelationRow = List[int]


@dataclass(frozen=True)
class AugmentedData:
    label: str
    k: int
    seed_name: str
    vertices: List[Vertex]
    edges: List[Edge]
    generators: List[Generator]
    relation_names: List[str]
    matrix: List[List[int]]
    rank_f2: int
    pivot_columns: List[int]
    row_reduced_basis: List[List[int]]


def canonical_edge_name(e: Edge) -> str:
    a, b = sorted(e)
    return f"{a}__{b}"


def edge_boundary_size(label: str, edge_index: int) -> int:
    if label == "F6":
        return 2
    if label == "F7":
        pattern = [4, 4, 4, 4, 4, 4, 3]
        return pattern[edge_index % len(pattern)]
    raise ValueError(label)


def phi_expand_generators(label: str, edges: List[Edge]) -> List[Generator]:
    generators: List[Generator] = []
    for idx, e in enumerate(edges):
        d = edge_boundary_size(label, idx)
        name = canonical_edge_name(e)
        for tau in range(d):
            for eps in (0, 1):
                generators.append((name, f"tau{tau}", eps))
    return generators


def generator_index(generators: List[Generator]) -> Dict[Generator, int]:
    return {g: i for i, g in enumerate(generators)}


def incident_edges(vertices: List[Vertex], edges: List[Edge]) -> Dict[Vertex, List[Edge]]:
    out: Dict[Vertex, List[Edge]] = {v: [] for v in vertices}
    for e in edges:
        a, b = e
        out[a].append(e)
        out[b].append(e)
    return out


def simple_cycle_basis(vertices: List[Vertex], edges: List[Edge]) -> List[List[Edge]]:
    if not vertices:
        return []
    adj: Dict[Vertex, List[Vertex]] = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    root = vertices[0]
    parent: Dict[Vertex, Vertex | None] = {root: None}
    parent_edge: Dict[Vertex, Edge | None] = {root: None}
    order = [root]
    for v in order:
        for u in adj[v]:
            if u not in parent:
                parent[u] = v
                parent_edge[u] = tuple(sorted((u, v)))
                order.append(u)

    tree_edges = {tuple(sorted((v, p))) for v, p in parent.items() if p is not None}
    non_tree_edges = [tuple(sorted(e)) for e in edges if tuple(sorted(e)) not in tree_edges]

    def path_edges(u: Vertex, v: Vertex) -> List[Edge]:
        ancestors_u: Dict[Vertex, List[Edge]] = {}
        cur = u
        path: List[Edge] = []
        while cur is not None:
            ancestors_u[cur] = path[:]
            pe = parent_edge[cur]
            if pe is not None:
                path = path + [pe]
            cur = parent[cur]

        cur = v
        path_v: List[Edge] = []
        while cur not in ancestors_u:
            pe = parent_edge[cur]
            if pe is not None:
                path_v.append(pe)
            cur = parent[cur]
        lca = cur
        return ancestors_u[lca] + list(reversed(path_v))

    cycles: List[List[Edge]] = []
    for a, b in non_tree_edges:
        cycle = [tuple(sorted((a, b)))] + path_edges(a, b)
        dedup: List[Edge] = []
        seen: Set[Edge] = set()
        for e in cycle:
            ee = tuple(sorted(e))
            if ee not in seen:
                seen.add(ee)
                dedup.append(ee)
        cycles.append(dedup)
    return cycles


def relation_incidence(vertices: List[Vertex], edges: List[Edge], generators: List[Generator]) -> Tuple[List[str], List[RelationRow]]:
    gidx = generator_index(generators)
    incidence = incident_edges(vertices, edges)
    names: List[str] = []
    rows: List[RelationRow] = []
    for v in vertices:
        row = [0] * len(generators)
        for e in incidence[v]:
            en = canonical_edge_name(e)
            for g in generators:
                if g[0] == en:
                    row[gidx[g]] ^= 1
        if any(row):
            names.append(f"inc::{v}")
            rows.append(row)
    return names, rows


def relation_cycles(vertices: List[Vertex], edges: List[Edge], generators: List[Generator]) -> Tuple[List[str], List[RelationRow]]:
    gidx = generator_index(generators)
    names: List[str] = []
    rows: List[RelationRow] = []
    for i, cyc in enumerate(simple_cycle_basis(vertices, edges)):
        row = [0] * len(generators)
        edge_names = {canonical_edge_name(e) for e in cyc}
        for g in generators:
            if g[0] in edge_names:
                row[gidx[g]] ^= 1
        if any(row):
            names.append(f"cycle::{i}")
            rows.append(row)
    return names, rows


def relation_overlaps(edges: List[Edge], generators: List[Generator]) -> Tuple[List[str], List[RelationRow]]:
    gidx = generator_index(generators)
    by_tau: Dict[str, List[Generator]] = defaultdict(list)
    for g in generators:
        by_tau[g[1]].append(g)

    names: List[str] = []
    rows: List[RelationRow] = []
    for tau, gs in sorted(by_tau.items()):
        grouped: Dict[str, List[Generator]] = defaultdict(list)
        for g in gs:
            grouped[g[0]].append(g)
        edge_names = sorted(grouped)
        for a, b in itertools.combinations(edge_names, 2):
            row = [0] * len(generators)
            for g in grouped[a] + grouped[b]:
                row[gidx[g]] ^= 1
            if any(row):
                names.append(f"overlap::{tau}::{a}::{b}")
                rows.append(row)
    return names, rows


def build_augmented_data(label: str, k: int) -> AugmentedData:
    seed_name = "tetrahedron_surface"
    seed = tetrahedron_surface()
    configs = enumerate_g2_layer([seed], k=k)
    vertices, edges = build_g2_graph(configs)
    vertices = sorted(vertices)
    edges = sorted(tuple(sorted(e)) for e in edges)

    generators = phi_expand_generators(label, edges)
    inc_names, inc_rows = relation_incidence(vertices, edges, generators)
    cyc_names, cyc_rows = relation_cycles(vertices, edges, generators)
    ov_names, ov_rows = relation_overlaps(edges, generators)

    matrix = inc_rows + cyc_rows + ov_rows
    relation_names = inc_names + cyc_names + ov_names

    if not matrix:
        matrix = [[0] * len(generators)] if generators else [[0]]
        relation_names = ["zero"]

    reduced, rank_f2, pivot_columns = f2_row_reduce(matrix)
    row_reduced_basis = [reduced[i] for i in range(rank_f2)]

    return AugmentedData(
        label=label,
        k=k,
        seed_name=seed_name,
        vertices=vertices,
        edges=edges,
        generators=generators,
        relation_names=relation_names,
        matrix=matrix,
        rank_f2=rank_f2,
        pivot_columns=pivot_columns,
        row_reduced_basis=row_reduced_basis,
    )
