from pathlib import Path
import json
import subprocess
import sys

def test_seed_runs():
    subprocess.check_call([sys.executable, "tools/g2_seed_n5.py"])

def test_n5_keys_present():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert "5" in data["cycles_found"]
    assert "5" in data["generated_by_candidate_G2"]
    assert "5" in data["certificates"]

def test_n5_partial_only():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["generated_by_candidate_G2"]["5"]["full_coverage_verified"] is None
