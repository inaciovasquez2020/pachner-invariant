# Repository Completion Snapshot — 2026-04-25

Status: EXECUTABLE-SURFACE COMPLETE.

Scope: repository-level executable certification surface.

This document does not claim full PachnerInvariant theorem-layer completion.

## Closed executable surfaces

0. bounded-G2 exact-rank certification is executable-certified for n in {6,7}.
1. Pachner Survival Protocol is present.
2. Bounded-G2 exact-rank certification is executable-certified for n in {6,7}.
3. F6 certificate is present and verified.
4. F7 certificate is present and verified.
5. No-overclaim certificate gates are present.
6. Local-support witness extraction is present.
7. Composite decomposition witness support is present.
8. Rank/nullity verifier is present.
9. Status documentation is present and tested.

## Certified bounded-G2 results

For n = 6:

- certificate: `docs/data/Cert_6.with_witnesses.json`
- vertex_count = 14
- edge_count = 21
- relation_count = 8
- rank_d1 = 13
- nullity_d1 = 8
- rank_M = 8
- target_rank_passed = true

Therefore:

\[
\dim_{\mathbb F_2} Z_1(F_6;\mathbb F_2)=8.
\]

For n = 7:

- certificate: `docs/data/Cert_7.with_witnesses.json`
- vertex_count = 42
- edge_count = 84
- relation_count = 43
- rank_d1 = 41
- nullity_d1 = 43
- rank_M = 43
- target_rank_passed = true

Therefore:

\[
\dim_{\mathbb F_2} Z_1(F_7;\mathbb F_2)=43.
\]

## Required verification commands

```bash
python3 tools/verify_admissible_bounded_g2_predicate.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 tools/classify_bounded_g2_relation_witnesses.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 tools/verify_bounded_g2_rank_cert.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json
python3 -m pytest -q
Boundary statement
This closes the repository executable certification surface currently represented by tests, status files, and bounded-G2 certificates.
It does not close unrelated or future PachnerInvariant theorem-layer obligations.
