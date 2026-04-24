import PachnerInvariant.RawEdgesCommon

namespace PachnerInvariant

theorem pairwiseDistinctTet_abpq
    {a b p q : Vert}
    (hab : a ≠ b)
    (hap : a ≠ p)
    (haq : a ≠ q)
    (hbp : b ≠ p)
    (hbq : b ≠ q)
    (hpq : p ≠ q) :
    pairwiseDistinctTet (a,b,p,q) := by
  exact ⟨hab, hap, haq, hbp, hbq, hpq⟩

theorem pairwiseDistinctTet_acpq
    {a c p q : Vert}
    (hac : a ≠ c)
    (hap : a ≠ p)
    (haq : a ≠ q)
    (hcp : c ≠ p)
    (hcq : c ≠ q)
    (hpq : p ≠ q) :
    pairwiseDistinctTet (a,c,p,q) := by
  exact ⟨hac, hap, haq, hcp, hcq, hpq⟩

theorem pairwiseDistinctTet_bcpq
    {b c p q : Vert}
    (hbc : b ≠ c)
    (hbp : b ≠ p)
    (hbq : b ≠ q)
    (hcp : c ≠ p)
    (hcq : c ≠ q)
    (hpq : p ≠ q) :
    pairwiseDistinctTet (b,c,p,q) := by
  exact ⟨hbc, hbp, hbq, hcp, hcq, hpq⟩

end PachnerInvariant
