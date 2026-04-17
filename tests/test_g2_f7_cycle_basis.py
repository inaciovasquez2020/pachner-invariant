from pathlib import Path
import json
import subprocess
import sys

def test_run_basis():
    subprocess.check_call([sys.executable, "tools/g2_f7_cycle_basis.py"])

def test_schema():
    p = Path("docs/data/f7_cycle_basis.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["n"] == 7
    assert data["cycle_rank"] == 43

def test_lengths_nonempty():
    p = Path("docs/data/f7_cycle_basis.json")
    data = json.loads(p.read_text())
    assert len(data["basis_cycle_lengths"]) == 43
