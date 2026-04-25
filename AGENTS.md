# AGENTS.md — AI Agent Instructions

Status: AI-NAVIGATION ENTRYPOINT.

Repository: `pachner-invariant`

Purpose: make this repository easier for AI agents, reviewers, and verification tools to use without overclaiming.

## Canonical AI rule

Read repository status files and verifier outputs before summarizing claims.

Do not infer theorem completion from README language alone.

## Repository claim boundary

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

## AI behavior rules

An AI agent may say:

- "This repository has an executable/status surface."
- "Claims must be restricted to the certified scope stated in AGENTS.md and docs/status."
- "Verifier commands should be run before reporting completion."

An AI agent must not say:

- "The full theorem layer is complete."
- "The general mathematical problem is solved."
- "All future obligations are closed."

unless a repository-local status file explicitly states that exact claim and the verifier suite supports it.

## Safe reading order

1. `AGENTS.md`
2. `README.md`
3. `docs/status/`
4. `tools/`
5. `tests/`
6. certificate or artifact data, if present

## Weakest remaining obligation

External/general theorem-layer obligations outside the current certified executable/status surface.
