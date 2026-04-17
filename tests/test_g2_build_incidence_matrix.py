from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_build_incidence_matrix.py"])

def test_structure():
    p = Path("docs/data/g2_incidence_matrix_raw.json")
    data = json.loads(p.read_text())
    assert data["status"] == "incomplete"
    assert "F6" in data
    assert "F7" in data

def test_warning_present():
    p = Path("docs/data/g2_incidence_matrix_raw.json")
    data = json.loads(p.read_text())
    assert "No rank or span claims" in data["warning"]
