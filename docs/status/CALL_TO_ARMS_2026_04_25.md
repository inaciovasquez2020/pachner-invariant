# Call to Arms — Independent Verification of the PachnerInvariant Executable Surface

Status: PUBLIC VERIFICATION INVITATION.

Scope: bounded-G2 exact-rank certification and repository executable-surface verification.

This is not a claim of full PachnerInvariant theorem-layer completion.

## What is now certified

The repository now contains executable certificates for the bounded-G2 exact-rank surface for n in {6,7}.

Certified artifacts:

- `docs/data/Cert_6.with_witnesses.json`
- `docs/data/Cert_7.with_witnesses.json`

Verified results:

\[
\dim_{\mathbb F_2} Z_1(F_6;\mathbb F_2)=8
\]

\[
\dim_{\mathbb F_2} Z_1(F_7;\mathbb F_2)=43
\]

These are certified by:

1. admissible bounded-G2 witness verification,
2. relation-witness classification,
3. rank/nullity verification over \(\mathbb F_2\),
4. repository tests.

## Reproduction commands

```bash
python3 tools/verify_admissible_bounded_g2_predicate.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json

python3 tools/classify_bounded_g2_relation_witnesses.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json

python3 tools/verify_bounded_g2_rank_cert.py docs/data/Cert_6.with_witnesses.json docs/data/Cert_7.with_witnesses.json

python3 -m pytest -q
Independent verification requested
External reviewers are invited to check:
that the certificate data is internally consistent;
that every relation witness satisfies the declared admissibility predicate;
that ∂ 
1
​	
 M 
n
T
​	
 =0 holds for n in {6,7};
that rank(M_6)=nullity(∂_1)=8;
that rank(M_7)=nullity(∂_1)=43;
that the status documents do not overclaim beyond the executable surface.
Extension challenge
The remaining gap is external/general theorem-layer work outside the bounded-G2 n in {6,7} certification surface.
Concrete next research directions:
generalize the bounded-G2 certificate schema beyond n in {6,7};
prove structural criteria explaining why the observed square, pentagon, decomposed-heptagon, and decomposed-composite witnesses suffice;
formalize the certificate predicate in Lean;
construct independent enumerators producing the same F6 and F7 certificates;
identify whether higher-n bounded-G2 layers stabilize, branch, or produce new relation types.
Boundary
This call is for independent verification and extension.
It does not claim:
full PachnerInvariant theorem-layer completion;
general n closure;
completion of all future topology obligations.
It claims only that the current executable bounded-G2 exact-rank surface for n in {6,7} is certified and reproducible.
