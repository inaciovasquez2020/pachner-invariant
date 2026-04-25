#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from create_bounded_g2_cert_data import build_candidate  # noqa: E402


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def edge_key(edges: list[int]) -> tuple[int, ...]:
    return tuple(sorted(set(int(e) for e in edges)))


def relation_key(rel: dict[str, Any]) -> tuple[int, ...]:
    return edge_key(rel["edge_indices_mod2"])


def endpoint_lookup(edges: list[dict[str, Any]]) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    lookup: dict[tuple[int, int], int] = {}
    ambiguous: list[tuple[int, int]] = []

    for e in edges:
        eid = int(e["edge_id"])
        u = int(e["source"])
        v = int(e["target"])
        k = tuple(sorted((u, v)))
        if k in lookup:
            ambiguous.append(k)
        else:
            lookup[k] = eid

    return lookup, sorted(set(ambiguous))


def generator_from_artifact_basis(cert: dict[str, Any]) -> dict[str, Any]:
    relation_sets = sorted(relation_key(rel) for rel in cert["relations"])
    return {
        "generator": "artifact_cycle_basis",
        "status": "generated",
        "relation_count": len(relation_sets),
        "edge_sets": [list(xs) for xs in relation_sets],
    }


def canonical_cycle(vertices: list[int]) -> tuple[int, ...]:
    if vertices[0] == vertices[-1]:
        vertices = vertices[:-1]

    rotations = []
    m = len(vertices)
    for seq in (vertices, list(reversed(vertices))):
        for i in range(m):
            rotations.append(tuple(seq[i:] + seq[:i]))
    return min(rotations)


def enumerate_simple_cycles_4_5(edges: list[dict[str, Any]]) -> dict[str, Any]:
    lookup, ambiguous = endpoint_lookup(edges)
    if ambiguous:
        return {
            "generator": "graph_simple_cycles_4_5",
            "status": "halt",
            "halt_reason": "parallel endpoint pairs prevent unique cycle-vertex to edge-token resolution",
            "ambiguous_endpoint_pairs": [list(x) for x in ambiguous],
            "edge_sets": [],
        }

    adj: dict[int, set[int]] = defaultdict(set)
    for e in edges:
        u = int(e["source"])
        v = int(e["target"])
        adj[u].add(v)
        adj[v].add(u)

    cycles: set[tuple[int, ...]] = set()

    for start in sorted(adj):
        stack: list[tuple[int, list[int]]] = [(start, [start])]
        while stack:
            cur, path = stack.pop()
            if len(path) > 5:
                continue

            for nxt in sorted(adj[cur]):
                if nxt == start and len(path) in (4, 5):
                    cycles.add(canonical_cycle(path))
                elif nxt not in path and len(path) < 5:
                    stack.append((nxt, path + [nxt]))

    edge_sets: set[tuple[int, ...]] = set()
    unresolved: list[list[int]] = []

    for cyc in sorted(cycles):
        ids: list[int] = []
        ok = True
        cyc_list = list(cyc)
        for a, b in zip(cyc_list, cyc_list[1:] + [cyc_list[0]]):
            k = tuple(sorted((a, b)))
            if k not in lookup:
                ok = False
                break
            ids.append(lookup[k])
        if ok:
            edge_sets.add(edge_key(ids))
        else:
            unresolved.append(cyc_list)

    return {
        "generator": "graph_simple_cycles_4_5",
        "status": "generated",
        "cycle_count": len(edge_sets),
        "unresolved_cycle_vertices": unresolved,
        "edge_sets": [list(xs) for xs in sorted(edge_sets)],
    }


def build_spanning_forest(edges: list[dict[str, Any]]) -> tuple[dict[int, int | None], dict[int, int | None], set[int]]:
    adj: dict[int, list[tuple[int, int]]] = defaultdict(list)
    vertices: set[int] = set()

    for e in edges:
        eid = int(e["edge_id"])
        u = int(e["source"])
        v = int(e["target"])
        vertices.add(u)
        vertices.add(v)
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    parent: dict[int, int | None] = {}
    parent_edge: dict[int, int | None] = {}
    tree_edges: set[int] = set()

    for root in sorted(vertices):
        if root in parent:
            continue

        parent[root] = None
        parent_edge[root] = None
        q: deque[int] = deque([root])

        while q:
            u = q.popleft()
            for v, eid in sorted(adj[u]):
                if v in parent:
                    continue
                parent[v] = u
                parent_edge[v] = eid
                tree_edges.add(eid)
                q.append(v)

    return parent, parent_edge, tree_edges


def path_edges_to_root(
    v: int,
    parent: dict[int, int | None],
    parent_edge: dict[int, int | None],
) -> dict[int, list[int]]:
    out: dict[int, list[int]] = {}
    cur = v
    edges: list[int] = []

    while True:
        out[cur] = list(edges)
        p = parent[cur]
        if p is None:
            break
        pe = parent_edge[cur]
        if pe is None:
            break
        edges.append(pe)
        cur = p

    return out


def enumerate_fundamental_cycles(edges: list[dict[str, Any]]) -> dict[str, Any]:
    parent, parent_edge, tree_edges = build_spanning_forest(edges)

    edge_sets: set[tuple[int, ...]] = set()

    for e in edges:
        eid = int(e["edge_id"])
        if eid in tree_edges:
            continue

        u = int(e["source"])
        v = int(e["target"])

        u_paths = path_edges_to_root(u, parent, parent_edge)
        v_paths = path_edges_to_root(v, parent, parent_edge)

        common = set(u_paths).intersection(v_paths)
        if not common:
            continue

        lca = min(common, key=lambda x: len(u_paths[x]) + len(v_paths[x]))
        cyc_edges = u_paths[lca] + v_paths[lca] + [eid]
        edge_sets.add(edge_key(cyc_edges))

    return {
        "generator": "spanning_tree_fundamental_cycles",
        "status": "generated",
        "cycle_count": len(edge_sets),
        "edge_sets": [list(xs) for xs in sorted(edge_sets)],
    }


def suggested_rule(edge_count: int, present_in_simple_cycle_generator: bool) -> str:
    if not present_in_simple_cycle_generator:
        return "unclassified"
    if edge_count == 4:
        return "bounded_G2_square"
    if edge_count == 5:
        return "bounded_G2_pentagon"
    return "unclassified"


def build_witness_data(n: int) -> dict[str, Any]:
    cert = build_candidate(n)

    basis = generator_from_artifact_basis(cert)
    simple = enumerate_simple_cycles_4_5(cert["edges"])
    fundamental = enumerate_fundamental_cycles(cert["edges"])

    basis_sets = {tuple(xs) for xs in basis["edge_sets"]}
    simple_sets = {tuple(xs) for xs in simple["edge_sets"]}
    fundamental_sets = {tuple(xs) for xs in fundamental["edge_sets"]}

    witness_candidates = []

    for rel in cert["relations"]:
        key = relation_key(rel)
        in_basis = key in basis_sets
        in_simple = key in simple_sets
        in_fundamental = key in fundamental_sets
        rule = suggested_rule(len(key), in_simple)

        witness_candidates.append(
            {
                "relation_id": rel["relation_id"],
                "witness_id": rel["witness_id"],
                "edge_indices_mod2": list(key),
                "generator_evidence": {
                    "artifact_cycle_basis": in_basis,
                    "graph_simple_cycles_4_5": in_simple,
                    "spanning_tree_fundamental_cycles": in_fundamental,
                },
                "three_generator_agreement": in_basis and in_simple and in_fundamental,
                "suggested_relation_rule": rule,
                "admissible_bounded_G2": False,
                "status": "candidate_only",
                "halt_reason": "Three generators produce evidence, but no local bounded-G2 elementary witness has been proved.",
            }
        )

    return {
        "schema": "BoundedG2WitnessData",
        "field": "F2",
        "n": n,
        "source_certificate_status": cert["status"],
        "expected_rank": cert["expected_rank"],
        "generators": [basis, simple, fundamental],
        "witness_candidates": witness_candidates,
        "summary": {
            "relation_count": len(cert["relations"]),
            "three_generator_agreement_count": sum(
                1 for w in witness_candidates if w["three_generator_agreement"]
            ),
            "suggested_square_count": sum(
                1 for w in witness_candidates if w["suggested_relation_rule"] == "bounded_G2_square"
            ),
            "suggested_pentagon_count": sum(
                1 for w in witness_candidates if w["suggested_relation_rule"] == "bounded_G2_pentagon"
            ),
            "unclassified_count": sum(
                1 for w in witness_candidates if w["suggested_relation_rule"] == "unclassified"
            ),
        },
        "status": "candidate_only",
        "halt_reason": "Generated data is not a certificate until admissible_bounded_G2 witnesses are proved.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, nargs="+", default=[6, 7])
    ap.add_argument("--output-dir", default="docs/data")
    args = ap.parse_args()

    out_dir = Path(args.output_dir)

    for n in args.n:
        data = build_witness_data(n)
        out = out_dir / f"bounded_g2_witness_data_n{n}.json"
        write_json(out, data)
        print(f"WROTE {out}")

    print("HALT: generated three-generator witness data only; certification remains conditional.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
