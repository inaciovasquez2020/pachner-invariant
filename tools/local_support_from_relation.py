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


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"HALT: missing candidate certificate file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def relation_indices(rel: dict[str, Any]) -> list[int]:
    xs = rel.get("edge_indices_mod2")
    if not isinstance(xs, list) or not xs:
        raise ValueError("relation has no nonempty edge_indices_mod2")
    out = [int(x) for x in xs]
    if len(set(out)) != len(out):
        raise ValueError("relation edge_indices_mod2 is not parity-normalized")
    return sorted(out)


def connected(vertices: set[int], adjacency: dict[int, set[int]]) -> bool:
    if not vertices:
        return False

    start = min(vertices)
    seen = {start}
    q: deque[int] = deque([start])

    while q:
        u = q.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)

    return seen == vertices


def local_support_from_relation(cert: dict[str, Any], rel: dict[str, Any]) -> dict[str, Any] | None:
    edges = cert.get("edges")
    if not isinstance(edges, list):
        raise ValueError("certificate edges field is not a list")

    idxs = relation_indices(rel)

    if len(idxs) not in (4, 5):
        return None

    vertices: set[int] = set()
    degree: dict[int, int] = defaultdict(int)
    adjacency: dict[int, set[int]] = defaultdict(set)

    for idx in idxs:
        if idx < 0 or idx >= len(edges):
            raise ValueError(f"edge index out of range: {idx}")

        edge = edges[idx]
        u = int(edge["source"])
        v = int(edge["target"])

        if u == v:
            return None

        vertices.add(u)
        vertices.add(v)
        degree[u] += 1
        degree[v] += 1
        adjacency[u].add(v)
        adjacency[v].add(u)

    if len(vertices) != len(idxs):
        return None

    if any(degree[v] != 2 for v in vertices):
        return None

    if not connected(vertices, adjacency):
        return None

    rule = "bounded_G2_square" if len(idxs) == 4 else "bounded_G2_pentagon"

    return {
        "witness_id": rel.get("witness_id", f"local_support_witness_{rel.get('relation_id')}"),
        "relation_id": rel.get("relation_id"),
        "admissible_bounded_G2": True,
        "relation_rule": rule,
        "local_support": sorted(vertices),
        "bounded_G2_layer": True,
        "uses_only_local_flips": True,
        "closed_local_loop": True,
        "edge_indices_mod2": idxs,
        "source": "local_support_from_relation",
        "status": "first_valid_local_graph_witness",
        "scope": "valid for the current checkable predicate; not a proof that every candidate relation is classified",
    }


def candidate_from_args(args: argparse.Namespace) -> dict[str, Any]:
    if args.input:
        return load_json(Path(args.input))
    if args.n is None:
        raise SystemExit("HALT: provide either --input or --n")
    return build_candidate(args.n)


def first_valid_witness(cert: dict[str, Any]) -> dict[str, Any]:
    relations = cert.get("relations")
    if not isinstance(relations, list):
        raise SystemExit("HALT: certificate relations field is not a list")

    failures: list[dict[str, Any]] = []

    for rel in relations:
        try:
            witness = local_support_from_relation(cert, rel)
        except Exception as exc:
            failures.append(
                {
                    "relation_id": rel.get("relation_id"),
                    "error": str(exc),
                }
            )
            continue

        if witness is not None:
            return {
                "schema": "BoundedG2FirstLocalSupportWitness",
                "field": "F2",
                "n": cert.get("n"),
                "status": "PASS",
                "witness": witness,
            }

        failures.append(
            {
                "relation_id": rel.get("relation_id"),
                "error": "relation is not a simple local 4- or 5-cycle in the endpoint graph",
            }
        )

    raise SystemExit(
        json.dumps(
            {
                "schema": "BoundedG2FirstLocalSupportWitness",
                "n": cert.get("n"),
                "status": "HALT",
                "failure_count": len(failures),
                "failures": failures[:10],
            },
            indent=2,
            sort_keys=True,
        )
    )



def all_valid_witnesses(cert: dict[str, Any]) -> dict[str, Any]:
    relations = cert.get("relations")
    if not isinstance(relations, list):
        raise SystemExit("HALT: certificate relations field is not a list")

    witnesses: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []

    for rel in relations:
        try:
            witness = local_support_from_relation(cert, rel)
        except Exception as exc:
            failures.append(
                {
                    "relation_id": rel.get("relation_id"),
                    "witness_id": rel.get("witness_id"),
                    "error": str(exc),
                }
            )
            continue

        if witness is None:
            failures.append(
                {
                    "relation_id": rel.get("relation_id"),
                    "witness_id": rel.get("witness_id"),
                    "error": "relation is not a simple local 4- or 5-cycle in the endpoint graph",
                }
            )
            continue

        witnesses.append(witness)

    report = {
        "schema": "BoundedG2AllLocalSupportWitnesses",
        "field": "F2",
        "n": cert.get("n"),
        "relation_count": len(relations),
        "witness_count": len(witnesses),
        "failure_count": len(failures),
        "witnesses": witnesses,
        "failures": failures[:20],
        "status": "PASS" if not failures and len(witnesses) == len(relations) else "HALT",
        "scope": "all exported candidate relations must reconstruct as graph-local square/pentagon witnesses",
    }

    if report["status"] != "PASS":
        raise SystemExit(json.dumps(report, indent=2, sort_keys=True))

    return report

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument(
        "--all",
        action="store_true",
        help="require every exported candidate relation to reconstruct as a local witness",
    )
    args = parser.parse_args()

    cert = candidate_from_args(args)
    report = all_valid_witnesses(cert) if args.all else first_valid_witness(cert)

    if args.output:
        write_json(Path(args.output), report)

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
