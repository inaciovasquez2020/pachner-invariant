from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_generator_matrix_wall.py"])

def test_schema():
    p = Path("docs/data/g2_generator_matrix_wall.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["field"] == "F2"

def test_f6_target():
    p = Path("docs/data/g2_generator_matrix_wall.json")
    data = json.loads(p.read_text())
    assert data["targets"]["F6"]["edges"] == 21
    assert data["targets"]["F6"]["cycle_rank_required"] == 8

def test_f7_target():
    p = Path("docs/data/g2_generator_matrix_wall.json")
    data = json.loads(p.read_text())
    assert data["targets"]["F7"]["edges"] == 84
    assert data["targets"]["F7"]["cycle_rank_required"] == 43

def test_wall_present():
    p = Path("docs/data/g2_generator_matrix_wall.json")
    data = json.loads(p.read_text())
    assert "edge-incidence row vector" in data["single_remaining_wall"]
