from pathlib import Path

DOC = Path("docs/math/PACHNER23_PENALTY_BOUND_FROM_VALID23.md")

def test_penalty_bound_doc_exists():
    assert DOC.exists()

def test_penalty_bound_status_open():
    text = DOC.read_text()
    assert "Status: Open." in text
    assert "No unconditional proof is claimed here." in text

def test_weakest_missing_theorem_locked():
    text = DOC.read_text()
    assert "lemma penalty_bound_from_valid23" in text
    assert "edgePenaltyExpected23 T a b c d e ≤ edgePenalty T ∧" in text
    assert "vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T" in text

def test_immediate_consequences_recorded():
    text = DOC.read_text()
    assert "pachner23_local_edge_penalty_nonincrease" in text
    assert "pachner23_local_vertex_penalty_nonincrease" in text
    assert "valid23_implies_penalty_controlled" in text
    assert "theta_pachner23_nonincreasing" in text

def test_equivalence_frontier_locked():
    text = DOC.read_text()
    assert "equivalent, within the current proof chain" in text
    assert "penalty_bound_from_valid23" in text
