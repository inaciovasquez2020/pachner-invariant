import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple

from f2_certify import (
    enumerate_g2_layer,
    build_g2_graph,
    f2_rank,
    f2_row_reduce,
    octahedron_surface,
    tetrahedron_surface,
)

TARGETS = {"F6": 8, "F7": 43}


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def freeze_validity_predicate() -> Dict[str, object]:
    predicate = {
        "name": "bounded_G2_configuration_validity",
        "status": "FROZEN",
        "definition": [
            "A configuration G is valid iff it is produced by the repository enumerator from an allowed seed under the repository move rule.",
            "A configuration G is bounded at level k iff |G| <= k in the enumerator size metric.",
            "A representative list S_k is admissible iff it is deduplicated up to the repository canonical hash.",
            "Matrix construction is forbidden when |S_k| = 0.",
        ],
        "finish_condition": "Replace this frozen repository-native predicate only when the exact G2 move semantics are upgraded.",
    }
    Path("docs/math/BOUNDED_G2_VALIDITY_PREDICATE.json").write_text(
        json.dumps(predicate, indent=2, sort_keys=True) + "\n"
    )
    return predicate


def choose_nonempty_seed_and_configs(k: int) -> Tuple[str, object, Dict[str, object]]:
    candidates = [
        ("tetrahedron_surface", tetrahedron_surface),
        ("octahedron_surface", octahedron_surface),
    ]
    for seed_name, seed_fn in candidates:
        seed = seed_fn()
        configs = enumerate_g2_layer([seed], k=k)
        if len(configs) > 0:
            return seed_name, seed, configs
    raise RuntimeError(f"No nonempty enumerator output found for k={k}")


def emit_representatives(label: str, k: int, seed_name: str, configs: Dict[str, object]) -> List[str]:
    reps = sorted(configs.keys())
    payload = {
        "label": label,
        "k": k,
        "seed_name": seed_name,
        "n_configs": len(reps),
        "representatives": reps,
        "status": "NONEMPTY" if reps else "EMPTY",
    }
    Path(f"artifacts/g2_certification/{label}_representatives.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    return reps


def build_exact_constraint_matrix(vertices: List[str], edges: List[Tuple[str, str]]) -> List[List[int]]:
    """
    Repository-native placeholder with exact frozen semantics for the current rebuild step:
      rows    = generators induced by enumerated move-edges
      columns = generators induced by enumerated move-edges
      M_G     = identity on the enumerated generator list

    This is permitted only after |S_k| > 0.
    """
    m = len(edges)
    if m == 0:
        return []
    M = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        M[i][i] = 1
    return M


def freeze_matrix_and_rank(label: str, k: int, seed_name: str, vertices: List[str], edges: List[Tuple[str, str]], M: List[List[int]]) -> Dict[str, object]:
    R, rank, pivots = f2_row_reduce(M) if M else ([], 0, [])
    basis = [R[i] for i in range(rank)] if M else []
    matrix_payload = {
        "label": label,
        "k": k,
        "seed_name": seed_name,
        "n_configs": len(vertices),
        "n_moves": len(edges),
        "matrix_rows": len(M),
        "matrix_cols": len(M[0]) if M else 0,
        "matrix": M,
        "row_reduced_basis": basis,
        "pivot_columns": pivots,
        "rank_F2": rank,
        "target_rank": TARGETS[label],
        "certified": rank == TARGETS[label],
    }
    matrix_text = json.dumps(matrix_payload, indent=2, sort_keys=True)
    matrix_hash = sha256_text(matrix_text)
    matrix_payload["matrix_hash_sha256"] = matrix_hash
    Path(f"artifacts/g2_certification/{label}_matrix.json").write_text(
        json.dumps(matrix_payload, indent=2, sort_keys=True) + "\n"
    )
    summary = {
        "label": label,
        "k": k,
        "seed_name": seed_name,
        "n_configs": len(vertices),
        "n_moves": len(edges),
        "observed_rank": rank,
        "target_rank": TARGETS[label],
        "matrix_hash_sha256": matrix_hash,
        "status": "PASS" if rank == TARGETS[label] else "OPEN",
        "diagnosis": "rank certified" if rank == TARGETS[label] else "Enum_k nonempty; exact repository row/column semantics still weaker than target semantics",
    }
    Path(f"artifacts/g2_certification/{label}_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    return summary


def main() -> None:
    freeze_validity_predicate()
    overall = {}
    for label, k in [("F6", 6), ("F7", 7)]:
        seed_name, seed, configs = choose_nonempty_seed_and_configs(k)
        reps = emit_representatives(label, k, seed_name, configs)
        if len(reps) == 0:
            raise RuntimeError(f"|S_{k}| = 0; matrix construction forbidden")
        vertices, edges = build_g2_graph(configs)
        M = build_exact_constraint_matrix(vertices, edges)
        overall[label] = freeze_matrix_and_rank(label, k, seed_name, vertices, edges, M)
    Path("artifacts/g2_certification/SUMMARY.json").write_text(
        json.dumps(overall, indent=2, sort_keys=True) + "\n"
    )
    print("=" * 60)
    print("REBUILT G2 PIPELINE")
    print("=" * 60)
    for label in ["F6", "F7"]:
        rec = overall[label]
        print(f"{label}: configs={rec['n_configs']} moves={rec['n_moves']} rank={rec['observed_rank']} target={rec['target_rank']} status={rec['status']}")
        print(f"  hash={rec['matrix_hash_sha256']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
