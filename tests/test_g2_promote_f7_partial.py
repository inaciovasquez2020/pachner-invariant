from pathlib import Path
import json
import subprocess
import sys

def test_run_promote():
    subprocess.check_call([sys.executable, "tools/g2_promote_f7_partial.py"])

def test_registry_updated():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["cycles_found"]["7"]["exact_cycle_rank"] == 43
    assert data["generated_by_candidate_G2"]["7"]["full_coverage_verified"] is True
