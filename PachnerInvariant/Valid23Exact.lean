import PachnerInvariant.descent_property

namespace PachnerInvariant

abbrev Tet := Vert × Vert × Vert × Vert

def countTetMod (t : Tet) (ts : List Tet) : Nat :=
  ts.countP (fun u => tetEq t u)

def tetMemModExact (t : Tet) (ts : List Tet) : Prop :=
  countTetMod t ts = 1

def edgeMemNorm (e : Vert × Vert) (es : List (Vert × Vert)) : Prop :=
  (es.map normalizeEdge).contains (normalizeEdge e) = true

def pairwiseDistinct5 (a b c p q : Vert) : Prop :=
  a ≠ b ∧ a ≠ c ∧ a ≠ p ∧ a ≠ q ∧
  b ≠ c ∧ b ≠ p ∧ b ≠ q ∧
  c ≠ p ∧ c ≠ q ∧
  p ≠ q

def Valid23Exact (T : Triangulation) (a b c p q : Vert) : Prop :=
  a < T.numVerts ∧
  b < T.numVerts ∧
  c < T.numVerts ∧
  p < T.numVerts ∧
  q < T.numVerts ∧
  pairwiseDistinct5 a b c p q ∧
  tetMemModExact (a,b,c,p) T.tets ∧
  tetMemModExact (a,b,c,q) T.tets ∧
  countTetMod (a,b,p,q) T.tets = 0 ∧
  countTetMod (a,c,p,q) T.tets = 0 ∧
  countTetMod (b,c,p,q) T.tets = 0 ∧
  ¬ edgeMemNorm (p,q) (allEdges T)

theorem Valid23Exact_removed_p_count
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23Exact T a b c p q) :
    countTetMod (a,b,c,p) T.tets = 1 :=
  h.right.right.right.right.right.right.left

theorem Valid23Exact_removed_q_count
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23Exact T a b c p q) :
    countTetMod (a,b,c,q) T.tets = 1 :=
  h.right.right.right.right.right.right.right.left

end PachnerInvariant
