from pathlib import Path

def test_structural_stack_doc():
    s = Path("docs/structure/STRUCTURAL_STACK.md").read_text()
    assert "Matveev" in s
    assert "Rourke–Sanderson" in s
    assert "Hatcher" in s
    assert "Benedetti–Petronio" in s
