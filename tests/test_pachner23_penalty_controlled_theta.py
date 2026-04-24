from pathlib import Path

DOC = Path("docs/math/PACHNER23_PENALTY_CONTROLLED_THETA.md")

def test_penalty_controlled_theta_doc_exists():
    assert DOC.exists()

def test_penalty_controlled_theta_status_is_conditional():
    text = DOC.read_text()
    assert "Status: Conditional." in text
    assert "No unconditional global theta nonincrease is claimed" in text

def test_penalty_control_class_is_recorded():
    text = DOC.read_text()
    assert "class Valid23PenaltyControlled" in text
    assert "edge_nonincrease" in text
    assert "vertex_nonincrease" in text

def test_conditional_theta_theorem_is_recorded():
    text = DOC.read_text()
    assert "theta_pachner23_nonincreasing_of_penalty_controlled" in text
    assert "theta_pachner23_eq_expected" in text
    assert "Nat.add_le_add" in text
    assert "Nat.mul_le_mul_left" in text

def test_unconditional_frontier_remains_locked():
    text = DOC.read_text()
    assert "edgePenaltyExpected23_le_edgePenalty" in text
    assert "vertexPenaltyExpected23_le_vertexPenalty" in text
