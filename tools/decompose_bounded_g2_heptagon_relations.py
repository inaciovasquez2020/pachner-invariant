#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from create_bounded_g2_cert_data import build_candidate
from generate_bounded_g2_witness_data import enumerate_simple_cycles_4_5
from local_support_from_relation import local_support_from_relation, relation_indices


def row_bits(indices: list[int]) -> int:
    out = 0
    for i in indices:
        out ^= 1 << int(i)
    return out


def bit_indices(x: int) -> list[int]:
    out = []
    i = 0
    while x:
        if x & 1:
            out.append(i)
        x >>= 1
        i += 1
    return out


def solve_subset_xor(target: int, generators: list[int]) -> list[int] | None:
    basis: dict[int, tuple[int, int]] = {}

    for i, g in enumerate(generators):
        x = g
        mask = 1 << i

        while x:
            p = x.bit_length() - 1
            if p not in basis:
                basis[p] = (x, mask)
                break
            bx, bm = basis[p]
            x ^= bx
            mask ^= bm

    x = target
    mask = 0

    while x:
        p = x.bit_length() - 1
        if p not in basis:
            return None
        bx, bm = basis[p]
        x ^= bx
        mask ^= bm

    return [i for i in range(len(generators)) if (mask >> i) & 1]


def load_candidate(path: Path | None, n: int | None) -> dict[str, Any]:
    if path is not None:
        if not path.exists():
            raise SystemExit(f"HALT: missing candidate certificate file: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    if n is None:
        raise SystemExit("HALT: provide --input or --n")

    return build_candidate(n)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    cert = load_candidate(Path(args.input) if args.input else None, args.n)

    simple = enumerate_simple_cycles_4_5(cert["edges"])
    simple_cycles = [list(map(int, xs)) for xs in simple.get("edge_sets", [])]
    simple_bits = [row_bits(xs) for xs in simple_cycles]

    reports = []

    for rel in cert["relations"]:
        witness = local_support_from_relation(cert, rel)
        if witness is not None:
            continue

        idxs = relation_indices(rel)
        if len(idxs) != 7:
            continue

        target = row_bits(idxs)
        solution = solve_subset_xor(target, simple_bits)

        if solution is None:
            reports.append(
                {
                    "relation_id": rel.get("relation_id"),
                    "witness_id": rel.get("witness_id"),
                    "edge_indices_mod2": idxs,
                    "edge_count": len(idxs),
                    "status": "HALT",
                    "decomposes_into_square_pentagon_cycles": False,
                    "halt_reason": "No F2 decomposition into graph-local 4/5 cycles found.",
                }
            )
            continue

        summands = [
            {
                "summand_index": i,
                "edge_indices_mod2": simple_cycles[i],
                "relation_rule": "bounded_G2_square"
                if len(simple_cycles[i]) == 4
                else "bounded_G2_pentagon",
            }
            for i in solution
        ]

        xor_check = 0
        for s in summands:
            xor_check ^= row_bits(s["edge_indices_mod2"])

        reports.append(
            {
                "relation_id": rel.get("relation_id"),
                "witness_id": rel.get("witness_id"),
                "edge_indices_mod2": idxs,
                "edge_count": len(idxs),
                "status": "PASS" if xor_check == target else "HALT",
                "decomposes_into_square_pentagon_cycles": xor_check == target,
                "decomposition_summand_count": len(summands),
                "decomposition": summands,
                "xor_check_edge_indices_mod2": bit_indices(xor_check),
            }
        )

    passed = all(r["status"] == "PASS" for r in reports)

    result = {
        "schema": "BoundedG2HeptagonDecompositionReport",
        "field": "F2",
        "n": cert.get("n"),
        "simple_cycle_generator_status": simple.get("status"),
        "simple_cycle_count": len(simple_cycles),
        "heptagon_obstruction_count": len(reports),
        "reports": reports,
        "status": "PASS" if passed else "HALT",
        "scope": "Tests whether failed 7-cycles decompose over F2 into graph-local square/pentagon cycles.",
    }

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2, sort_keys=True))

    if not passed:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
