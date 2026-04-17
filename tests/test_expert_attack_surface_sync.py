from pathlib import Path

def test_expert_attack_surface_sync():
    s = Path("docs/status/EXPERT_ATTACK_SURFACE.md").read_text()
    assert "edge_incidence_delta_lemma" in s
    assert "general ΔΘ expansion is proved, but the general descent theorem is not yet formalized." in s
    assert "Toy-to-general attack" in s
