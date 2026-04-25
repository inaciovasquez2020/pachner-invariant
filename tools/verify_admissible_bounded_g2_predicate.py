#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_RULES = {
    "bounded_G2_square",
    "bounded_G2_pentagon",
}


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"HALT: missing certificate file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def relation_edge_set(rel: dict[str, Any]) -> set[int]:
    xs = rel.get("edge_indices_mod2")
    if not isinstance(xs, list) or not xs:
        raise AssertionError("relation has no nonempty edge_indices_mod2")
    out = set()
    for x in xs:
        if not isinstance(x, int):
            raise AssertionError(f"relation edge index is not int: {x!r}")
        out.add(x)
    if len(out) != len(xs):
        raise AssertionError("relation edge_indices_mod2 is not parity-normalized")
    return out


def check_witness(rel: dict[str, Any], witness: dict[str, Any], edge_count: int) -> None:
    edges = relation_edge_set(rel)

    for idx in edges:
        if idx < 0 or idx >= edge_count:
            raise AssertionError(f"relation edge index out of range: {idx}")

    if witness.get("admissible_bounded_G2") is not True:
        raise AssertionError("witness does not assert admissible_bounded_G2=true")

    rule = witness.get("relation_rule")
    if rule not in ALLOWED_RULES:
        raise AssertionError(f"relation_rule must be one of {sorted(ALLOWED_RULES)}, got {rule!r}")

    local_support = witness.get("local_support")
    if not isinstance(local_support, list) or not local_support:
        raise AssertionError("local_support must be a nonempty list")

    bounded_layer = witness.get("bounded_G2_layer")
    if bounded_layer is not True:
        raise AssertionError("bounded_G2_layer must be true")

    uses_only_local_flips = witness.get("uses_only_local_flips")
    if uses_only_local_flips is not True:
        raise AssertionError("uses_only_local_flips must be true")

    closed_local_loop = witness.get("closed_local_loop")
    if closed_local_loop is not True:
        raise AssertionError("closed_local_loop must be true")

    if witness.get("edge_indices_mod2") is not None:
        witness_edges = set(int(x) for x in witness["edge_indices_mod2"])
        if witness_edges != edges:
            raise AssertionError("witness edge_indices_mod2 does not match relation")


def verify(path: Path) -> dict[str, Any]:
    cert = load(path)

    if cert.get("certificate_schema") != "BoundedG2RankCert":
        raise SystemExit(f"HALT: invalid certificate schema in {path}")

    edges = cert.get("edges")
    relations = cert.get("relations")
    witnesses = cert.get("relation_witnesses")

    if not isinstance(edges, list):
        raise SystemExit(f"HALT: edges field is not a list in {path}")
    if not isinstance(relations, list):
        raise SystemExit(f"HALT: relations field is not a list in {path}")
    if not isinstance(witnesses, list):
        raise SystemExit(f"HALT: relation_witnesses field is not a list in {path}")

    witness_by_id = {}
    for witness in witnesses:
        wid = witness.get("witness_id")
        if not wid:
            raise SystemExit(f"HALT: witness without witness_id in {path}")
        if wid in witness_by_id:
            raise SystemExit(f"HALT: duplicate witness_id {wid!r} in {path}")
        witness_by_id[wid] = witness

    failures = []

    for rel in relations:
        rid = rel.get("relation_id")
        wid = rel.get("witness_id")
        witness = witness_by_id.get(wid)
        if witness is None:
            failures.append({"relation_id": rid, "witness_id": wid, "error": "missing witness"})
            continue
        try:
            check_witness(rel, witness, len(edges))
        except AssertionError as e:
            failures.append({"relation_id": rid, "witness_id": wid, "error": str(e)})

    report = {
        "path": str(path),
        "n": cert.get("n"),
        "relation_count": len(relations),
        "checked_predicate": "admissible_bounded_G2",
        "allowed_rules": sorted(ALLOWED_RULES),
        "failure_count": len(failures),
        "failures": failures[:10],
        "status": "PASS" if not failures else "HALT",
    }

    if failures:
        raise SystemExit(json.dumps(report, indent=2, sort_keys=True))

    return report


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: verify_admissible_bounded_g2_predicate.py Cert_6.json Cert_7.json", file=sys.stderr)
        return 2

    reports = [verify(Path(arg)) for arg in argv[1:]]
    print(json.dumps({"reports": reports, "status": "PASS"}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
