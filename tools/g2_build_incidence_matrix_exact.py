from __future__ import annotations

import json
from collections import deque
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

Graph = Dict[str, object]
Edge = Tuple[int, int]


def load_graph(name: str) -> Graph:
    return json.loads((DATA / name).read_text())


def normalize_edge(u: int, v: int) -> Edge:
    return (u, v) if u < v else (v, u)


def edge_list_from_adjacency(adj: Dict[str, List[int]]) -> List[Edge]:
    edges = set()
    for su, nbrs in adj.items():
        u = int(su)
        for v in nbrs:
            edges.add(normalize_edge(u, int(v)))
    return sorted(edges)


def bfs_tree_edges(num_vertices: int, adj: Dict[str, List[int]], root: int = 0) -> List[Edge]:
    seen = {root}
    q = deque([root])
    tree: List[Edge] = []
    while q:
        u = q.popleft()
        for v in sorted(int(x) for x in adj[str(u)]):
            if v not in seen:
                seen.add(v)
                q.append(v)
                tree.append(normalize_edge(u, v))
    if len(seen) != num_vertices:
        raise ValueError("graph is not connected")
    return tree


def parent_map_from_tree(num_vertices: int, tree_edges: List[Edge], root: int = 0) -> Dict[int, int | None]:
    tadj: Dict[int, List[int]] = {v: [] for v in range(num_vertices)}
    for u, v in tree_edges:
        tadj[u].append(v)
        tadj[v].append(u)

    parent: Dict[int, int | None] = {root: None}
    q = deque([root])
    while q:
        u = q.popleft()
        for v in sorted(tadj[u]):
            if v not in parent:
                parent[v] = u
                q.append(v)
    if len(parent) != num_vertices:
        raise ValueError("tree does not span graph")
    return parent


def path_edges_in_tree(u: int, v: int, parent: Dict[int, int | None]) -> List[Edge]:
    ancestors_u: Dict[int, int] = {}
    x = u
    depth = 0
    while x is not None:
        ancestors_u[x] = depth
        px = parent[x]
        x = px if px is not None else None
        depth += 1

    y = v
    path_v_nodes = []
    while y not in ancestors_u:
        path_v_nodes.append(y)
        py = parent[y]
        if py is None:
            raise ValueError("no common ancestor in tree")
        y = py
    lca = y

    path_u: List[int] = []
    x = u
    while x != lca:
        path_u.append(x)
        px = parent[x]
        if px is None:
            raise ValueError("broken parent chain")
        x = px
    path_u.append(lca)

    path_v = [lca] + list(reversed(path_v_nodes))
    node_path = path_u + path_v[1:]
    return [normalize_edge(node_path[i], node_path[i + 1]) for i in range(len(node_path) - 1)]


def row_from_cycle(cycle_edges: List[Edge], edge_index: Dict[Edge, int], m: int) -> List[int]:
    row = [0] * m
    for e in cycle_edges:
        row[edge_index[e]] ^= 1
    return row


def build_exact_matrix(graph_name: str) -> Dict[str, object]:
    g = load_graph(graph_name)
    n = int(g["n"])
    adj = g["adjacency"]
    edges = edge_list_from_adjacency(adj)
    m = len(edges)
    edge_index = {e: i for i, e in enumerate(edges)}

    tree_edges = bfs_tree_edges(int(g["vertices"]), adj, root=0)
    tree_set = set(tree_edges)
    parent = parent_map_from_tree(int(g["vertices"]), tree_edges, root=0)
    chords = [e for e in edges if e not in tree_set]

    generators = []
    for idx, (u, v) in enumerate(chords):
        tree_path = path_edges_in_tree(u, v, parent)
        cycle_edges = tree_path + [normalize_edge(u, v)]
        row = row_from_cycle(cycle_edges, edge_index, m)
        generators.append(
            {
                "generator_id": idx,
                "type": "fundamental_cycle",
                "pivot_chord": [u, v],
                "cycle_length": int(sum(row)),
                "edge_incidence_row": row,
            }
        )

    return {
        "status": "conditional",
        "field": "F2",
        "construction": "fundamental_cycle_rows_from_spanning_tree",
        "claim_level": "exact_rows",
        "n": n,
        "vertices": int(g["vertices"]),
        "edges": m,
        "components": int(g["components"]),
        "cycle_rank_target": int(g["cycle_rank"]),
        "edge_order": [list(e) for e in edges],
        "tree_edges": [list(e) for e in tree_edges],
        "generator_rows": generators,
    }


def main() -> None:
    out = {
        "status": "conditional",
        "field": "F2",
        "artifacts": {
            "F6": build_exact_matrix("f6_exact_graph.json"),
            "F7": build_exact_matrix("f7_exact_graph.json"),
        },
        "note": "Explicit generator row vectors are written in edge-order coordinates over F2.",
    }
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "g2_incidence_matrix_exact.json").write_text(json.dumps(out, indent=2))
    print("wrote docs/data/g2_incidence_matrix_exact.json")


if __name__ == "__main__":
    main()
