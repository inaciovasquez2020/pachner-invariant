import PachnerInvariant.Valid23Exact

namespace PachnerInvariant

def expectedVertexDeg23ExactDelta (a b c p q : Vert) (v : Vert) : Nat :=
  if v = p then 2 else if v = q then 2 else 0

/--
Open target.

This is the first theorem needed before the old frontier vertex-degree chain
can be repaired. It is intentionally not imported by the root module.
-/
def vertexDegreeExactTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    vertexDeg (pachner23 T a b c p q) v =
      vertexDeg T v + expectedVertexDeg23ExactDelta a b c p q v

end PachnerInvariant
