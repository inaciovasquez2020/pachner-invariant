from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f5_exact.py"])

def test_surface():
    p = Path("docs/data/f5_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["n"] == 5
    assert data["vertices"] == 5
    assert data["cycle_rank"] >= 1

def test_expected_vertices():
    p = Path("docs/data/f5_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["vertices"] == 5
