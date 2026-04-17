from pathlib import Path
import json
import subprocess
import sys

def test_seed_runs():
    subprocess.check_call([sys.executable, "tools/g2_manual_seed.py"])

def test_n4_seeded():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["cycles_found"]["4"] == 0
    assert data["generated_by_candidate_G2"]["4"] is True
    assert "4" in data["certificates"]
