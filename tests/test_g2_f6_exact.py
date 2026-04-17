from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f6_exact.py"])

def test_surface():
    p = Path("docs/data/f6_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["n"] == 6
    assert data["vertices"] == 14
    assert data["components"] == 1

def test_rank_positive():
    p = Path("docs/data/f6_exact_graph.json")
    data = json.loads(p.read_text())
    assert data["cycle_rank"] >= 1
