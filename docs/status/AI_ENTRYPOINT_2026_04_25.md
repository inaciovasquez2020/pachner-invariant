# AI Entrypoint — pachner-invariant

Status: CANONICAL AI ENTRYPOINT.

This file exists so that AI agents can use the repository safely without reading only the README.

## Repository

`pachner-invariant`

## Current certified scope

Current certified scope:
- bounded-G2 exact-rank executable certification for n in {6,7}
- F6 rank_M = nullity_d1 = 8
- F7 rank_M = nullity_d1 = 43
- executable-surface complete for the current certified scope

Does not claim:
- full PachnerInvariant theorem-layer completion
- general-n closure
- closure of unrelated topology obligations

Canonical verification:
python3 tools/verify_admissible_bounded_g2_predicate.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 tools/classify_bounded_g2_relation_witnesses.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 tools/verify_bounded_g2_rank_cert.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 -m pytest -q

## Safe one-line summary

This repository should be interpreted through its executable/status surface and explicit claim-boundary files. It should not be summarized as full theorem-layer completion unless that exact claim is explicitly certified.

## Machine-readable status

```json
{
  "repository": "pachner-invariant",
  "ai_entrypoint": true,
  "full_theorem_layer_complete": false,
  "general_problem_complete": false,
  "claim_boundary_required": true,
  "canonical_files": [
    "AGENTS.md",
    "README.md",
    "docs/status/"
  ]
}
```
