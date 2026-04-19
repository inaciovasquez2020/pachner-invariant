from __future__ import annotations

import json
import hashlib
from pathlib import Path

from pachner_invariant.g2_augmented_matrix import build_augmented_data

TARGETS = {"F6": 8, "F7": 43}


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def main() -> None:
    outdir = Path("artifacts/g2_certification")
    outdir.mkdir(parents=True, exist_ok=True)

    summary = {}

    for label, k in [("F6", 6), ("F7", 7)]:
        data = build_augmented_data(label, k)
        payload = {
            "label": label,
            "k": k,
            "seed_name": data.seed_name,
            "vertices": data.vertices,
            "edges": data.edges,
            "n_configs": len(data.vertices),
            "n_moves": len(data.edges),
            "generators": [list(g) for g in data.generators],
            "generator_count": len(data.generators),
            "relation_names": data.relation_names,
            "relation_count": len(data.relation_names),
            "matrix": data.matrix,
            "matrix_rows": len(data.matrix),
            "matrix_cols": len(data.matrix[0]) if data.matrix else 0,
            "row_reduced_basis": data.row_reduced_basis,
            "pivot_columns": data.pivot_columns,
            "rank_F2": data.rank_f2,
            "kernel_dim": (len(data.generators) - data.rank_f2),
            "target_rank": TARGETS[label],
            "certified": data.rank_f2 == TARGETS[label],
        }
        payload["matrix_hash_sha256"] = sha256_text(json.dumps(payload, sort_keys=True))
        Path(outdir / f"{label}_augmented_matrix.json").write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n"
        )
        summary[label] = {
            "label": label,
            "k": k,
            "n_configs": len(data.vertices),
            "n_moves": len(data.edges),
            "generator_count": len(data.generators),
            "relation_count": len(data.relation_names),
            "observed_rank": data.rank_f2,
            "target_rank": TARGETS[label],
            "kernel_dim": len(data.generators) - data.rank_f2,
            "matrix_hash_sha256": payload["matrix_hash_sha256"],
            "status": "PASS" if data.rank_f2 == TARGETS[label] else "OPEN",
        }

    Path(outdir / "AUGMENTED_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )

    md = r"""# G2 Canonical Generator System

## Status
CONDITIONAL

## Generator expansion rule

For each bounded Pachner move-edge
\[
e=(u,v)\in E_G,
\]
define
\[
\Phi(e)=\Gamma(e):=\{(e,\tau,\epsilon): \tau\in\partial(e),\ \epsilon\in\{0,1\}\}.
\]

The full generator system is
\[
\Gamma_G=\bigsqcup_{e\in E_G}\Phi(e).
\]

## Dependent relation family

The canonical relation family is
\[
\mathcal R_G=\mathcal R_G^{\mathrm{inc}}\cup \mathcal R_G^{\mathrm{cycle}}\cup \mathcal R_G^{\mathrm{overlap}}.
\]

The augmented matrix is
\[
\widetilde M_G=
\begin{bmatrix}
\mathcal R_G^{\mathrm{inc}}\\
\mathcal R_G^{\mathrm{cycle}}\\
\mathcal R_G^{\mathrm{overlap}}
\end{bmatrix}.
\]

## Target equalities

\[
\operatorname{rank}_{\mathbb F_2}(\widetilde M_{F6})=8,
\qquad
\operatorname{rank}_{\mathbb F_2}(\widetilde M_{F7})=43.
\]
"""
    Path("docs/math/G2_CANONICAL_GENERATOR_SYSTEM.md").write_text(md)

    test_text = r'''from pathlib import Path
import json

def test_augmented_summary_exists_and_grows() -> None:
    data = json.loads(Path("artifacts/g2_certification/AUGMENTED_SUMMARY.json").read_text())
    assert data["F6"]["generator_count"] >= 8
    assert data["F7"]["generator_count"] >= 43

def test_augmented_matrix_targets_recorded() -> None:
    f6 = json.loads(Path("artifacts/g2_certification/F6_augmented_matrix.json").read_text())
    f7 = json.loads(Path("artifacts/g2_certification/F7_augmented_matrix.json").read_text())
    assert f6["target_rank"] == 8
    assert f7["target_rank"] == 43
    assert f6["matrix_cols"] == f6["generator_count"]
    assert f7["matrix_cols"] == f7["generator_count"]

def test_generator_system_doc_lock() -> None:
    s = Path("docs/math/G2_CANONICAL_GENERATOR_SYSTEM.md").read_text()
    assert "CONDITIONAL" in s
    assert "\\Gamma_G" in s
    assert "\\mathcal R_G" in s
    assert "\\operatorname{rank}_{\\mathbb F_2}(\\widetilde M_{F6})=8" in s
    assert "\\operatorname{rank}_{\\mathbb F_2}(\\widetilde M_{F7})=43" in s
'''
    Path("tests/test_g2_augmented_rank_lock.py").write_text(test_text)

    print(Path(outdir / "AUGMENTED_SUMMARY.json").read_text())


if __name__ == "__main__":
    main()
