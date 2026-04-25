#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any



def popcount(x: int) -> int:
    x = int(x)
    if hasattr(x, "bit_count"):
        return x.bit_count()
    return bin(x).count("1")

def gf2_rank(rows: list[int]) -> int:
    rows = [r for r in rows if r]
    rank = 0
    while rows:
        pivot = max(rows)
        p = pivot.bit_length() - 1
        rank += 1
        rest = []
        for r in rows:
            if r == pivot:
                continue
            if (r >> p) & 1:
                r ^= pivot
            if r:
                rest.append(r)
        rows = rest
    return rank


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"HALT: missing raw certificate file: {path}")
    cert = json.loads(path.read_text(encoding="utf-8"))
    if cert.get("status") == "raw_missing":
        raise SystemExit(f"HALT: {path} is a skeleton, not a raw certificate")
    return cert


def matrix_row_bits_from_relations(relations: list[dict[str, Any]], edge_count: int) -> list[int]:
    rows: list[int] = []
    for rel in relations:
        bits = 0
        counts: dict[int, int] = {}
        for idx in rel.get("edge_indices_mod2", rel.get("edge_indices", [])):
            if not isinstance(idx, int):
                raise AssertionError(f"relation edge index is not int: {idx!r}")
            if idx < 0 or idx >= edge_count:
                raise AssertionError(f"relation edge index out of range: {idx}")
            counts[idx] = counts.get(idx, 0) ^ 1
        for idx, parity in counts.items():
            if parity:
                bits ^= 1 << idx
        rows.append(bits)
    return rows


def boundary_rows(vertices: list[Any], edges: list[dict[str, Any]]) -> list[int]:
    v_count = len(vertices)
    rows = [0 for _ in range(v_count)]
    for j, e in enumerate(edges):
        source = e["source"]
        target = e["target"]
        if not isinstance(source, int) or not isinstance(target, int):
            raise AssertionError(f"edge {j} source/target must be integer indices")
        if source < 0 or source >= v_count:
            raise AssertionError(f"edge {j} source out of range")
        if target < 0 or target >= v_count:
            raise AssertionError(f"edge {j} target out of range")
        if source == target:
            raise AssertionError(f"edge {j} is degenerate self-loop")
        rows[source] ^= 1 << j
        rows[target] ^= 1 << j
    return rows


def transpose_product_zero(boundary: list[int], gen_rows: list[int]) -> bool:
    for b in boundary:
        for g in gen_rows:
            if popcount(b & g) % 2:
                return False
    return True


def verify(path: Path) -> dict[str, Any]:
    cert = load(path)

    assert cert.get("certificate_schema") == "BoundedG2RankCert"
    assert cert.get("field") == "F2"

    n = cert["n"]
    assert n in (6, 7)

    expected_rank = cert.get("expected_rank")
    assert expected_rank == (8 if n == 6 else 43)

    vertices = cert["vertices"]
    edges = cert["edges"]
    relations = cert["relations"]

    assert isinstance(vertices, list)
    assert isinstance(edges, list)
    assert isinstance(relations, list)

    if len(set(map(json.dumps, vertices))) != len(vertices):
        raise AssertionError("vertices are not uniquely indexed")

    edge_ids = [e.get("edge_id", i) for i, e in enumerate(edges)]
    if len(set(edge_ids)) != len(edge_ids):
        raise AssertionError("edges are not uniquely indexed")

    witnesses = {w.get("witness_id"): w for w in cert.get("relation_witnesses", [])}
    for rel in relations:
        wid = rel.get("witness_id")
        if wid is not None:
            if wid not in witnesses:
                raise AssertionError(f"missing relation witness: {wid}")
            if witnesses[wid].get("admissible_bounded_G2") is not True:
                raise AssertionError(f"relation witness is not admissible bounded-G2: {wid}")

    d1_rows = boundary_rows(vertices, edges)
    m_rows = matrix_row_bits_from_relations(relations, len(edges))

    rank_d1 = gf2_rank(d1_rows)
    nullity_d1 = len(edges) - rank_d1
    rank_m = gf2_rank(m_rows)
    legal = transpose_product_zero(d1_rows, m_rows)

    passed = legal and rank_m == nullity_d1 and rank_m == expected_rank

    report = {
        "path": str(path),
        "n": n,
        "vertex_count": len(vertices),
        "edge_count": len(edges),
        "relation_count": len(relations),
        "cycle_legality_d1_Mt_zero": legal,
        "rank_d1": rank_d1,
        "nullity_d1": nullity_d1,
        "rank_M": rank_m,
        "expected_rank": expected_rank,
        "rank_equals_nullity": rank_m == nullity_d1,
        "target_rank_passed": rank_m == expected_rank,
        "status": "PASS" if passed else "FAIL",
    }

    if not passed:
        raise AssertionError(json.dumps(report, indent=2))

    return report


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: verify_bounded_g2_rank_cert.py docs/data/Cert_6.json docs/data/Cert_7.json", file=sys.stderr)
        return 2

    reports = [verify(Path(arg)) for arg in argv[1:]]
    print(json.dumps({"reports": reports, "status": "PASS"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
