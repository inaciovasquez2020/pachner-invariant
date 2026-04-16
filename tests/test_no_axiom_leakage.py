from pathlib import Path
import os

def test_no_axiom_leakage():
    for root, _, files in os.walk("PachnerInvariant"):
        for f in files:
            if f.endswith(".lean") and "frontier" not in f and "theta_delta" not in f:
                s = Path(os.path.join(root, f)).read_text()
                assert "axiom" not in s
