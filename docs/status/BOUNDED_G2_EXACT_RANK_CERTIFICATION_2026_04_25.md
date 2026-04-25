# Bounded-G2 Exact-Rank Certification — 2026-04-25

Status: EXECUTABLE-CERTIFIED for n in {6,7}.

Scope: bounded-G2 exact-rank certification only.

This document does not claim full PachnerInvariant theorem-layer completion.

## Certified artifacts

- `docs/data/Cert_6.with_witnesses.json`
- `docs/data/Cert_7.with_witnesses.json`

## Verified predicates

Each certificate passes:

1. `tools/verify_admissible_bounded_g2_predicate.py`
2. `tools/classify_bounded_g2_relation_witnesses.py`
3. `tools/verify_bounded_g2_rank_cert.py`

## Exact certified ranks

For n = 6:

- vertex_count = 14
- edge_count = 21
- relation_count = 8
- rank_d1 = 13
- nullity_d1 = 8
- rank_M = 8
- rank_equals_nullity = true
- target_rank_passed = true

Therefore:

\[
\dim_{\mathbb F_2} Z_1(F_6;\mathbb F_2)=8.
\]

For n = 7:

- vertex_count = 42
- edge_count = 84
- relation_count = 43
- rank_d1 = 41
- nullity_d1 = 43
- rank_M = 43
- rank_equals_nullity = true
- target_rank_passed = true

Therefore:

\[
\dim_{\mathbb F_2} Z_1(F_7;\mathbb F_2)=43.
\]

## Certification theorem

For n in {6,7}, the executable certificate verifies:

\[
\partial_1 M_n^T = 0,
\]

\[
\operatorname{rank}_{\mathbb F_2}(M_n)=\operatorname{nullity}_{\mathbb F_2}(\partial_1),
\]

and the target rank values:

\[
\operatorname{rank}_{\mathbb F_2}(M_6)=8,
\qquad
\operatorname{rank}_{\mathbb F_2}(M_7)=43.
\]

Hence:

\[
\operatorname{rowspan}_{\mathbb F_2}(M_n)=Z_1(F_n;\mathbb F_2)
\]

for n in {6,7}.

## Boundary statement

This closes the bounded-G2 exact-rank certification surface for n in {6,7}.

It does not close unrelated PachnerInvariant obligations.
