from pathlib import Path

DOC = Path("docs/math/PACHNER23_THETA_REDUCTION_CHAIN.md")

def test_theta_reduction_chain_doc_exists():
    assert DOC.exists()

def test_theta_reduction_chain_status_is_conditional():
    text = DOC.read_text()
    assert "Status: Conditional." in text
    assert "No unconditional theta decrease or nonincrease is claimed" in text

def test_theta_reduction_chain_records_degree_bridge():
    text = DOC.read_text()
    assert "edgeDeg_pachner23_eq_expected" in text
    assert "vertexDeg_pachner23_eq_expected" in text
    assert "theta_pachner23_eq_expected" in text

def test_theta_reduction_chain_locks_exact_missing_lemmas():
    text = DOC.read_text()
    assert "edgePenaltyExpected23_le_edgePenalty" in text
    assert "vertexPenaltyExpected23_le_vertexPenalty" in text
    assert "theta_pachner23_nonincreasing" in text
