from pathlib import Path

def test_A1_star_exact_slot_form_lock():
 d = Path("docs/math/A1_STAR_EXACT_SLOT_FORM.md").read_text()
 assert "tetToEdges_normalized_no_collision" in d
 assert "Pairwise (· ≠ ·) es" in d
 assert "needed for A1*" in d
