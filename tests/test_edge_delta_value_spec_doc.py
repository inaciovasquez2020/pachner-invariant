from pathlib import Path

def test_edge_delta_value_spec_doc():
    s = Path("docs/math/EDGE_DELTA_VALUE_SPEC.md").read_text()
    assert "value(neg2) = -2" in s
    assert "value(pos2) = 2" in s
