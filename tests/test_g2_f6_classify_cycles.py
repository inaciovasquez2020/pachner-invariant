from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f6_classify_cycles.py"])

def test_schema():
    p = Path("docs/data/f6_cycle_classification.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["n"] == 6
    assert data["cycle_rank"] == 8

def test_counts():
    p = Path("docs/data/f6_cycle_classification.json")
    data = json.loads(p.read_text())
    assert data["counts"]["square_commutation"] == 1
    assert data["counts"]["pentagon"] == 4
    assert data["counts"]["derived_candidate"] == 3

def test_pending_three():
    p = Path("docs/data/f6_cycle_classification.json")
    data = json.loads(p.read_text())
    assert data["coverage_known"]["pending"] == 3
