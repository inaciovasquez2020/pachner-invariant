from pathlib import Path
import json

doc = Path("docs/math/RA1N_DDYO_COERCIVITY_FRONTIER.md").read_text()
snap = Path("docs/status/RA1N_DDYO_STATUS_SNAPSHOT.md").read_text()
art = json.loads(Path("artifacts/ra1n_ddyo_coercivity/frontier_summary.json").read_text())

def test_status():
    assert "CONDITIONAL" in doc
    assert "CONDITIONAL" in snap
    assert art["status"] == "CONDITIONAL"

def test_gap():
    assert "2^{-2C-9}" in doc

def test_missing():
    assert len(art["missing"]) == 4
