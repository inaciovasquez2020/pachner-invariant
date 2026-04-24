from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

def test_status_conditional():
    assert data["status"] == "promoted"

def test_tested_n():
    assert data["tested_n"] == [4, 5, 6, 7]

def test_required_keys():
    assert set(data["cycles_found"]) == {"4","5","6","7"}
    assert set(data["generated_by_candidate_G2"]) == {"4","5","6","7"}
