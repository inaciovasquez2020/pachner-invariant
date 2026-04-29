from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FRONTIER = ROOT / "PachnerInvariant" / "frontier.lean"
THETAZ = ROOT / "PachnerInvariant" / "ThetaZ.lean"

frontier = FRONTIER.read_text()
thetaz = THETAZ.read_text()

required_frontier_tokens = [
    "WellFormedTets T",
    "theorem Valid23.wellFormedTets",
    "def Valid23WF",
    "theorem valid23RawReady_of_valid23WF",
    "theorem edgeDeg_pachner23_delta_of_valid23WF",
    "theorem edgeDeg_pachner23_eq_expected_of_valid23WF",
    "theorem theta_pachner23_delta_expanded_of_valid23WF",
]

required_thetaz_tokens = [
    "theorem thetaZ_pachner23_delta_expanded_of_valid23WF",
    "theorem pachner23_descent_of_vertex_sum_of_valid23WF",
]

for token in required_frontier_tokens:
    assert token in frontier, f"missing frontier theorem-surface token: {token}"

for token in required_thetaz_tokens:
    assert token in thetaz, f"missing thetaZ theorem-surface token: {token}"

for forbidden in ["sorry", "admit"]:
    assert forbidden not in frontier, f"forbidden token in frontier.lean: {forbidden}"
    assert forbidden not in thetaz, f"forbidden token in ThetaZ.lean: {forbidden}"

print("pachner Valid23 theorem surface: PASS")
