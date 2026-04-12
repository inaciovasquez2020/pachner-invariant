from pathlib import Path

def test_frontier_registry_sync():
    s = Path("PachnerInvariant/frontier.lean").read_text()
    expected = [
        "axiom vertDeg_pachner23_eq_expected",
        "axiom theta_pachner23_delta_expanded",
        "axiom allEdges_pachner23_count_delta",
        "axiom expectedEdgeDeg23_delta_normal_form",
        "axiom edgeDeg_pachner23_delta",
        "axiom allEdges_count_eq_edgeDeg_countP",
    ]
    for item in expected:
        assert item in s, item

    reg = Path("docs/status/PACHNER_FRONTIER_REGISTRY.md").read_text()
    for name in [
        "vertDeg_pachner23_eq_expected",
        "theta_pachner23_delta_expanded",
        "allEdges_pachner23_count_delta",
        "expectedEdgeDeg23_delta_normal_form",
        "edgeDeg_pachner23_delta",
        "allEdges_count_eq_edgeDeg_countP",
    ]:
        assert name in reg, name
