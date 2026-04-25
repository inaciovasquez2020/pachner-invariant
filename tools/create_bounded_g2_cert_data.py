#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DATA = Path("docs/data")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def stable_key(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"))


def normalize_vertices(graph: dict[str, Any]) -> list[Any]:
    vertices = graph.get("vertices")
    if isinstance(vertices, list) and vertices:
        return vertices

    triangulations = graph.get("triangulations")
    if isinstance(triangulations, list) and triangulations:
        return triangulations

    adjacency = graph.get("adjacency")
    if isinstance(adjacency, dict):
        keys = sorted(adjacency.keys(), key=lambda x: int(x) if str(x).isdigit() else str(x))
        return keys

    raise SystemExit("HALT: cannot extract ordered vertices")


def vertex_index_map(vertices: list[Any]) -> dict[str, int]:
    out: dict[str, int] = {}
    for i, v in enumerate(vertices):
        k = stable_key(v)
        if k in out:
            raise SystemExit(f"HALT: duplicate vertex at index {i}")
        out[k] = i
        out[str(i)] = i
        out[i] = i  # type: ignore[index]
    return out


def coerce_vertex_index(x: Any, vmap: dict[Any, int], v_count: int) -> int:
    if isinstance(x, int) and 0 <= x < v_count:
        return x
    if str(x) in vmap:
        return vmap[str(x)]
    k = stable_key(x)
    if k in vmap:
        return vmap[k]
    raise SystemExit(f"HALT: cannot map vertex endpoint {x!r}")


def endpoint_from_edge_obj(edge: Any) -> tuple[Any, Any, str]:
    if isinstance(edge, dict):
        for a, b in [
            ("source", "target"),
            ("src", "dst"),
            ("u", "v"),
            ("from", "to"),
            ("left", "right"),
        ]:
            if a in edge and b in edge:
                token = edge.get("move_token", edge.get("move", edge.get("edge_id", edge.get("id"))))
                return edge[a], edge[b], str(token)

        for key in ["endpoints", "vertices", "edge"]:
            val = edge.get(key)
            if isinstance(val, list) and len(val) == 2:
                token = edge.get("move_token", edge.get("move", edge.get("edge_id", edge.get("id"))))
                return val[0], val[1], str(token)

    if isinstance(edge, (list, tuple)) and len(edge) >= 2:
        return edge[0], edge[1], f"edge-{edge}"

    if isinstance(edge, str):
        nums = re.findall(r"-?\d+", edge)
        if len(nums) >= 2:
            return int(nums[0]), int(nums[1]), edge

    raise SystemExit(f"HALT: cannot parse edge endpoint object: {edge!r}")


def normalize_edges(graph: dict[str, Any], vertices: list[Any]) -> list[dict[str, Any]]:
    raw_edges = graph.get("edges")
    vmap = vertex_index_map(vertices)

    edges: list[dict[str, Any]] = []

    if isinstance(raw_edges, list) and raw_edges:
        for j, raw in enumerate(raw_edges):
            u0, v0, token = endpoint_from_edge_obj(raw)
            u = coerce_vertex_index(u0, vmap, len(vertices))
            v = coerce_vertex_index(v0, vmap, len(vertices))
            if u == v:
                raise SystemExit(f"HALT: degenerate self-loop edge {j}")
            edges.append(
                {
                    "edge_id": j,
                    "source": u,
                    "target": v,
                    "move_token": token if token not in {"None", ""} else f"edge-{j}",
                    "source_artifact": "f_exact_graph.edges",
                }
            )
        return edges

    adjacency = graph.get("adjacency")
    if isinstance(adjacency, dict):
        seen: set[tuple[int, int]] = set()
        for a, nbrs in adjacency.items():
            u = coerce_vertex_index(a, vmap, len(vertices))
            if not isinstance(nbrs, list):
                continue
            for b in nbrs:
                v = coerce_vertex_index(b, vmap, len(vertices))
                if u == v:
                    raise SystemExit(f"HALT: degenerate self-loop adjacency edge {u}")
                key = tuple(sorted((u, v)))
                if key in seen:
                    continue
                seen.add(key)
                edges.append(
                    {
                        "edge_id": len(edges),
                        "source": key[0],
                        "target": key[1],
                        "move_token": f"adjacency-{key[0]}-{key[1]}",
                        "source_artifact": "f_exact_graph.adjacency",
                    }
                )
        if edges:
            return edges

    raise SystemExit("HALT: cannot extract ordered edges")


def edge_endpoint_lookup(edges: list[dict[str, Any]]) -> dict[tuple[int, int], int]:
    lookup: dict[tuple[int, int], int] = {}
    ambiguous: set[tuple[int, int]] = set()

    for e in edges:
        idx = int(e["edge_id"])
        u = int(e["source"])
        v = int(e["target"])
        key = tuple(sorted((u, v)))
        if key in lookup:
            ambiguous.add(key)
        else:
            lookup[key] = idx

    if ambiguous:
        raise SystemExit(
            "HALT: cycle_vertices cannot be resolved because parallel endpoint pairs exist: "
            + ", ".join(map(str, sorted(ambiguous)))
        )

    return lookup


def relation_edges_from_obj(obj: Any, endpoint_lookup: dict[tuple[int, int], int]) -> list[int]:
    if isinstance(obj, dict):
        for key in [
            "edge_indices_mod2",
            "edge_indices",
            "edges",
            "cycle_edges",
            "basis_edges",
            "non_tree_cycle",
        ]:
            val = obj.get(key)
            if isinstance(val, list):
                return [int(x) for x in val]

        cycle_vertices = obj.get("cycle_vertices")
        if isinstance(cycle_vertices, list) and len(cycle_vertices) >= 2:
            out: list[int] = []
            for a, b in zip(cycle_vertices, cycle_vertices[1:]):
                key = tuple(sorted((int(a), int(b))))
                if key not in endpoint_lookup:
                    raise SystemExit(f"HALT: cycle edge {key} not found in endpoint lookup")
                out.append(endpoint_lookup[key])
            return out

    if isinstance(obj, list):
        return [int(x) for x in obj]

    raise SystemExit(f"HALT: cannot parse relation object: {obj!r}")


def normalize_relations(basis: dict[str, Any], edges: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    raw = basis.get("basis_cycles")
    if not isinstance(raw, list) or not raw:
        raise SystemExit("HALT: cannot extract basis_cycles")

    relations: list[dict[str, Any]] = []
    witnesses: list[dict[str, Any]] = []

    endpoint_lookup = edge_endpoint_lookup(edges)
    edge_count = len(edges)

    for i, item in enumerate(raw):
        indices = relation_edges_from_obj(item, endpoint_lookup)

        parity: dict[int, int] = {}
        for idx in indices:
            if idx < 0 or idx >= edge_count:
                raise SystemExit(f"HALT: relation {i} edge index out of range: {idx}")
            parity[idx] = parity.get(idx, 0) ^ 1

        normalized = sorted(idx for idx, bit in parity.items() if bit)
        if not normalized:
            raise SystemExit(f"HALT: relation {i} is zero after F2 normalization")

        witness_id = f"candidate_relation_witness_{i}"

        relations.append(
            {
                "relation_id": i,
                "edge_indices_mod2": normalized,
                "relation_type": "cycle_basis_candidate",
                "witness_id": witness_id,
                "source_artifact": "f_cycle_basis.basis_cycles",
            }
        )

        witnesses.append(
            {
                "witness_id": witness_id,
                "admissible_bounded_G2": False,
                "status": "candidate_only",
                "halt_reason": "Existing cycle basis has not been classified as admissible bounded-G2 elementary relations.",
            }
        )

    return relations, witnesses


def graph_path(n: int) -> Path:
    candidates = [
        DATA / f"f{n}_exact_graph.json",
        DATA / f"F{n}_exact_graph.json",
    ]
    for p in candidates:
        if p.exists():
            return p
    raise SystemExit(f"HALT: missing exact graph artifact for n={n}")


def basis_path(n: int) -> Path:
    candidates = [
        DATA / f"f{n}_cycle_basis.json",
        DATA / f"F{n}_cycle_basis.json",
    ]
    for p in candidates:
        if p.exists():
            return p
    raise SystemExit(f"HALT: missing cycle basis artifact for n={n}")


def build_candidate(n: int) -> dict[str, Any]:
    gpath = graph_path(n)
    bpath = basis_path(n)
    graph = read_json(gpath)
    basis = read_json(bpath)

    vertices = normalize_vertices(graph)
    edges = normalize_edges(graph, vertices)
    relations, witnesses = normalize_relations(basis, edges)

    expected = 8 if n == 6 else 43

    return {
        "certificate_schema": "BoundedG2RankCert",
        "field": "F2",
        "n": n,
        "vertices": vertices,
        "edges": edges,
        "relations": relations,
        "relation_witnesses": witnesses,
        "expected_rank": expected,
        "status": "raw_candidate_unverified",
        "source_artifacts": [str(gpath), str(bpath)],
        "warning": "This is exported finite data from existing artifacts, not a certified bounded-G2 relation certificate.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, nargs="+", default=[6, 7])
    ap.add_argument("--output-dir", default="docs/data")
    args = ap.parse_args()

    out_dir = Path(args.output_dir)
    wrote: list[str] = []

    for n in args.n:
        try:
            cert = build_candidate(n)
        except SystemExit as e:
            print(str(e), file=sys.stderr)
            continue

        out = out_dir / f"Cert_{n}.candidate.json"
        write_json(out, cert)
        wrote.append(str(out))
        print(f"WROTE {out}")

    if not wrote:
        raise SystemExit("HALT: no candidate certificate data could be created")

    print("HALT: created candidate data only; admissible bounded-G2 relation witnesses remain missing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
