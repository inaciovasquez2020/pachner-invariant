from pathlib import Path
import json

DOC = Path("docs/math/RA1N_DDYO_COERCIVITY_FRONTIER.md").read_text()
SNAP = Path("docs/status/RA1N_DDYO_STATUS_SNAPSHOT.md").read_text()
ART = json.loads(Path("artifacts/ra1n_ddyo_coercivity/frontier_summary.json").read_text())

def test_frontier_status_lock() -> None:
    assert "## Status" in DOC
    assert "CONDITIONAL" in DOC
    assert "Status: CONDITIONAL" in SNAP
    assert ART["status"] == "CONDITIONAL"

def test_terminal_gap_lock() -> None:
    assert "3\\cdot 2^{-2C-9}" in DOC
    assert "3 * 2^(-2*C-9)" == ART["terminal_gap_lower_bound"]

def test_missing_package_lock() -> None:
    for s in [
        "sigma_{\\mathrm{eff}}",
        "kappa_{\\mathrm{rank\\_defect}}",
        "D_j",
        "kappa^{\\mathrm{DDYO}}",
    ]:
        assert s in DOC
    assert len(ART["missing_package"]) == 4

def test_benchmark_lock() -> None:
    assert ART["benchmark"]["min_gamma_a"] == 0.22426
    assert ART["benchmark"]["max_offdiag_leakage"] == 0.00228
    assert ART["benchmark"]["delta"] == 0.9898
    assert ART["benchmark"]["c_RA1n_benchmark"] == 0.222
