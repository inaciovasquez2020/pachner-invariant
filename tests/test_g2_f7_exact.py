from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f7_exact.py"])

def test_schema():
    p = Path("docs/data/f7_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["n"] == 7

def test_expected_vertices():
    p = Path("docs/data/f7_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["vertices"] == 42
    assert data["components"] == 1

def test_positive_rank():
    p = Path("docs/data/f7_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["cycle_rank"] >= 1
