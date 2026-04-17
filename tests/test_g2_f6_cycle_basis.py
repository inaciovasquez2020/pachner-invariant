from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f6_cycle_basis.py"])

def test_schema():
    p = Path("docs/data/f6_cycle_basis.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["n"] == 6
    assert data["cycle_rank"] == 8

def test_basis_count_matches_rank():
    p = Path("docs/data/f6_cycle_basis.json")
    data = json.loads(p.read_text())
    assert len(data["basis_cycles"]) == data["cycle_rank"]

def test_cycle_lengths_are_at_least_four():
    p = Path("docs/data/f6_cycle_basis.json")
    data = json.loads(p.read_text())
    assert all(c["cycle_length"] >= 4 for c in data["basis_cycles"])
