import json
import hashlib
from pathlib import Path

from f2_certify import enumerate_g2_layer, build_g2_graph, octahedron_surface
from fix_build_exact_matrix import build_exact_constraint_matrix

TARGETS = {"F6": 8, "F7": 43}

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def main() -> None:
    outdir = Path("artifacts/g2_certification")
    outdir.mkdir(parents=True, exist_ok=True)

    summary = {}

    for label, k in [("F6", 6), ("F7", 7)]:
        configs = enumerate_g2_layer([octahedron_surface()], k=k)
        vertices, edges = build_g2_graph(configs)
        M = build_exact_constraint_matrix(vertices, edges)

        matrix_payload = {
            "label": label,
            "k": k,
            "n_configs": len(vertices),
            "n_moves": len(edges),
            "matrix_rows": len(M),
            "matrix_cols": len(M[0]) if M else 0,
            "matrix": M,
        }
        matrix_json = json.dumps(matrix_payload, sort_keys=True, separators=(",", ":")).encode()
        matrix_hash = sha256_bytes(matrix_json)

        Path(outdir / f"{label}_matrix.json").write_text(
            json.dumps(matrix_payload, indent=2, sort_keys=True) + "\n"
        )

        record = {
            "label": label,
            "k": k,
            "target_rank": TARGETS[label],
            "observed_rank": 0 if (not M or not M[0] or M == [[0]]) else sum(M[i][i] for i in range(min(len(M), len(M[0])))),
            "n_configs": len(vertices),
            "n_moves": len(edges),
            "matrix_hash_sha256": matrix_hash,
            "status": "OPEN",
            "diagnosis": "Enum_k and BuildExact unresolved",
        }

        Path(outdir / f"{label}_summary.json").write_text(
            json.dumps(record, indent=2, sort_keys=True) + "\n"
        )
        summary[label] = record

    Path(outdir / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )

if __name__ == "__main__":
    main()
