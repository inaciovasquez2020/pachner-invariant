from pathlib import Path
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
