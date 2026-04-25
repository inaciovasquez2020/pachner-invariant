#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"HALT: missing candidate certificate file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def classify(path: Path) -> dict[str, Any]:
    cert = load(path)

    if cert.get("certificate_schema") != "BoundedG2RankCert":
        raise SystemExit(f"HALT: invalid certificate schema in {path}")

    n = cert.get("n")
    if n not in (6, 7):
        raise SystemExit(f"HALT: unsupported n in {path}: {n}")

    relations = cert.get("relations")
    witnesses = cert.get("relation_witnesses")

    if not isinstance(relations, list):
        raise SystemExit(f"HALT: relations field is not a list in {path}")
    if not isinstance(witnesses, list):
        raise SystemExit(f"HALT: relation_witnesses field is not a list in {path}")

    witness_by_id = {}
    duplicate_witness_ids = []

    for w in witnesses:
        wid = w.get("witness_id")
        if not wid:
            raise SystemExit(f"HALT: witness without witness_id in {path}")
        if wid in witness_by_id:
            duplicate_witness_ids.append(wid)
        witness_by_id[wid] = w

    missing = []
    inadmissible = []
    untyped = []

    for rel in relations:
        rid = rel.get("relation_id")
        wid = rel.get("witness_id")

        if wid not in witness_by_id:
            missing.append({"relation_id": rid, "witness_id": wid})
            continue

        witness = witness_by_id[wid]

        if witness.get("admissible_bounded_G2") is not True:
            inadmissible.append(
                {
                    "relation_id": rid,
                    "witness_id": wid,
                    "status": witness.get("status"),
                    "halt_reason": witness.get("halt_reason"),
                }
            )

        if not witness.get("relation_rule") and not rel.get("relation_type"):
            untyped.append({"relation_id": rid, "witness_id": wid})

    passed = not duplicate_witness_ids and not missing and not inadmissible and not untyped

    report = {
        "path": str(path),
        "n": n,
        "relation_count": len(relations),
        "witness_count": len(witnesses),
        "duplicate_witness_ids": duplicate_witness_ids,
        "missing_witnesses": missing,
        "inadmissible_witnesses": inadmissible,
        "untyped_witnesses": untyped,
        "status": "PASS" if passed else "HALT",
    }

    if not passed:
        raise SystemExit(json.dumps(report, indent=2, sort_keys=True))

    return report


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(
            "usage: classify_bounded_g2_relation_witnesses.py Cert_6.candidate.json Cert_7.candidate.json",
            file=sys.stderr,
        )
        return 2

    reports = [classify(Path(arg)) for arg in argv[1:]]
    print(json.dumps({"reports": reports, "status": "PASS"}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
