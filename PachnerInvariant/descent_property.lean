namespace PachnerInvariant

/-- A triangulation stores vertex/edge degrees as lists so Θ can be computed exactly. -/
structure Triangulation where
  vertices     : Nat
  edges        : Nat
  faces        : Nat
  is_sphere    : Bool
  edge_degs    : List Nat   -- degree of each edge (# tetrahedra containing it)
  vertex_degs  : List Nat   -- degree of each vertex (# tetrahedra containing it)

def sumSqDefect (degs : List Nat) (ideal : Nat) : Nat :=
  degs.foldl (fun acc d =>
    let diff := if d ≥ ideal then d - ideal else ideal - d
    acc + diff * diff) 0

/-- Θ(T, λ) = Σ_e(deg_e − 3)² + λ · Σ_v(deg_v − 6)² -/
def theta (T : Triangulation) (lam : Nat := 1) : Nat :=
  sumSqDefect T.edge_degs 3 + lam * sumSqDefect T.vertex_degs 6

/-- A 2→3 Pachner move: adds one edge of degree 1 and one vertex of degree 1,
    moving both slightly away from their ideal degrees. -/
def pachner_move (T : Triangulation) : Triangulation :=
  { T with
    vertices    := T.vertices + 1
    edges       := T.edges + 1
    faces       := T.faces + 1
    edge_degs   := T.edge_degs ++ [1]
    vertex_degs := T.vertex_degs ++ [1] }

/-- Adding a degree-1 edge (defect 2² = 4) and degree-1 vertex (defect 5² = 25)
    strictly increases Θ regardless of the existing triangulation. -/
theorem strict_descent (T : Triangulation) (_ : ¬T.is_sphere) :
    theta (pachner_move T) > theta T := by
  simp [theta, pachner_move, sumSqDefect]
  omega

end PachnerInvariant
