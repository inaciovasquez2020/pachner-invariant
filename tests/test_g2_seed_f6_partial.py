from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_seed_f6_partial.py"])

def test_n6_partial_seed_present():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["cycles_found"]["6"]["exact_cycle_rank"] == 8
    assert data["cycles_found"]["6"]["basis_cycle_lengths"] == [5, 4, 5, 7, 7, 5, 5, 7]
    assert data["generated_by_candidate_G2"]["6"]["full_coverage_verified"] is None
    assert data["certificates"]["6"]["basis_artifact"] == "docs/data/f6_cycle_basis.json"
