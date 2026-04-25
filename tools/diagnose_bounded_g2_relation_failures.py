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
from local_support_from_relation import local_support_from_relation, relation_indices  # noqa: E402


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"HALT: missing certificate file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def components(vertices: set[int], adjacency: dict[int, set[int]]) -> list[list[int]]:
    remaining = set(vertices)
    out: list[list[int]] = []

    while remaining:
        start = min(remaining)
        seen = {start}
        q: deque[int] = deque([start])

        while q:
            u = q.popleft()
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        out.append(sorted(seen))
        remaining -= seen

    return out


def diagnose_relation(cert: dict[str, Any], rel: dict[str, Any]) -> dict[str, Any]:
    edges = cert["edges"]
    idxs = relation_indices(rel)

    vertices: set[int] = set()
    degree: dict[int, int] = defaultdict(int)
    adjacency: dict[int, set[int]] = defaultdict(set)
    endpoints = []

    for idx in idxs:
        edge = edges[idx]
        u = int(edge["source"])
        v = int(edge["target"])
        endpoints.append({"edge_index": idx, "source": u, "target": v})
        vertices.add(u)
        vertices.add(v)
        degree[u] += 1
        degree[v] += 1
        adjacency[u].add(v)
        adjacency[v].add(u)

    witness = local_support_from_relation(cert, rel)

    failure_reasons = []
    if witness is None:
        if len(idxs) not in (4, 5):
            failure_reasons.append("edge_count_not_4_or_5")
        if len(vertices) != len(idxs):
            failure_reasons.append("vertex_count_not_equal_edge_count")
        bad_degrees = {str(v): d for v, d in sorted(degree.items()) if d != 2}
        if bad_degrees:
            failure_reasons.append("not_2_regular")
        comps = components(vertices, adjacency)
        if len(comps) != 1:
            failure_reasons.append("not_connected")
    else:
        bad_degrees = {}
        comps = [sorted(vertices)]

    return {
        "relation_id": rel.get("relation_id"),
        "witness_id": rel.get("witness_id"),
        "edge_indices_mod2": idxs,
        "edge_count": len(idxs),
        "vertex_count": len(vertices),
        "vertices": sorted(vertices),
        "endpoints": endpoints,
        "degrees": {str(v): degree[v] for v in sorted(vertices)},
        "bad_degrees": bad_degrees,
        "components": comps,
        "local_support_passed": witness is not None,
        "failure_reasons": failure_reasons,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--only-failures", action="store_true")
    args = parser.parse_args()

    if args.input:
        cert = load_json(Path(args.input))
    elif args.n is not None:
        cert = build_candidate(args.n)
    else:
        raise SystemExit("HALT: provide --input or --n")

    diagnostics = []
    for rel in cert["relations"]:
        diag = diagnose_relation(cert, rel)
        if args.only_failures and diag["local_support_passed"]:
            continue
        diagnostics.append(diag)

    report = {
        "schema": "BoundedG2RelationFailureDiagnostics",
        "n": cert.get("n"),
        "relation_count": len(cert["relations"]),
        "diagnostic_count": len(diagnostics),
        "diagnostics": diagnostics,
        "status": "PASS",
    }

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
