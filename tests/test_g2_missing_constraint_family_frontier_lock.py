from pathlib import Path
import json

def test_g2_missing_constraint_family_frontier_lock() -> None:
    s = Path("docs/math/G2_MISSING_CONSTRAINT_FAMILY_FRONTIER.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "Exact repository-native dependent Pachner relation family" in Path("artifacts/g2_certification/AUGMENTATION_GAP.json").read_text()
    assert "\\operatorname{rank}_{\\mathbb F_2}(\\widetilde{M}_{F6})=8" in s
    assert "\\operatorname{rank}_{\\mathbb F_2}(\\widetilde{M}_{F7})=43" in s

def test_g2_augmentation_gap_json_lock() -> None:
    data = json.loads(Path("artifacts/g2_certification/AUGMENTATION_GAP.json").read_text())
    assert data["F6"]["observed_rank"] == 3
    assert data["F6"]["target_rank"] == 8
    assert data["F6"]["required_extra_independent_rows"] == 5
    assert data["F7"]["observed_rank"] == 7
    assert data["F7"]["target_rank"] == 43
    assert data["F7"]["required_extra_independent_rows"] == 36
