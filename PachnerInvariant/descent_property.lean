namespace PachnerInvariant

abbrev Vert := Nat

/-- A triangulation as an explicit list of tetrahedra (4-tuples of vertex indices).
    All combinatorial data — edge degrees, vertex degrees — is derived from this. -/
structure Triangulation where
  numVerts : Nat
  tets     : List (Vert × Vert × Vert × Vert)

def tetToVerts (t : Vert × Vert × Vert × Vert) : List Vert :=
  [t.1, t.2.1, t.2.2.1, t.2.2.2]

def tetToEdges (t : Vert × Vert × Vert × Vert) : List (Vert × Vert) :=
  let a := t.1; let b := t.2.1; let c := t.2.2.1; let d := t.2.2.2
  [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def edgeEq (e1 e2 : Vert × Vert) : Bool :=
  (e1.1 == e2.1 && e1.2 == e2.2) || (e1.1 == e2.2 && e1.2 == e2.1)

def normalizeEdge (e : Vert × Vert) : Vert × Vert :=
  if e.1 ≤ e.2 then e else (e.2, e.1)

/-- All distinct edges in the triangulation (unordered pairs). -/
def allEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.bind tetToEdges |>.map normalizeEdge).eraseDups

/-- Number of tetrahedra containing vertex v. -/
def vertDeg (T : Triangulation) (v : Vert) : Nat :=
  T.tets.countP (fun t => (tetToVerts t).contains v)

/-- Number of tetrahedra containing edge e. -/
def edgeDeg (T : Triangulation) (e : Vert × Vert) : Nat :=
  T.tets.countP (fun t => (tetToEdges t).any (edgeEq e))

def sumSqDefect (vals : List Nat) (ideal : Nat) : Nat :=
  vals.foldl (fun acc d =>
    let diff := if d ≥ ideal then d - ideal else ideal - d
    acc + diff * diff) 0

/-- Θ(T, λ) = Σ_e(deg_e − 3)² + λ · Σ_v(deg_v − 6)²
    Computed directly from the adjacency structure. -/
def theta (T : Triangulation) (lam : Nat := 1) : Nat :=
  let edgeDs := (allEdges T).map (edgeDeg T)
  let vertDs := (List.range T.numVerts).map (vertDeg T)
  sumSqDefect edgeDs 3 + lam * sumSqDefect vertDs 6

def tetContainsVert (t : Vert × Vert × Vert × Vert) (v : Vert) : Bool :=
  t.1 == v || t.2.1 == v || t.2.2.1 == v || t.2.2.2 == v

/-- Two tetrahedra are equal as sets of vertices. -/
def tetEq (t1 t2 : Vert × Vert × Vert × Vert) : Bool :=
  tetContainsVert t2 t1.1 && tetContainsVert t2 t1.2.1 &&
  tetContainsVert t2 t1.2.2.1 && tetContainsVert t2 t1.2.2.2

/-- Real 2→3 Pachner move.
    Precondition: T contains tets (a,b,c,p) and (a,b,c,q) sharing face (a,b,c).
    Effect: removes those 2 tets, inserts 3 tets sharing new edge (p,q):
      (a,b,p,q), (a,c,p,q), (b,c,p,q)
    Net change: edges +1, faces +2, tets +1, vertices unchanged. -/
def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove : List (Vert × Vert × Vert × Vert) :=
    [(a, b, c, p), (a, b, c, q)]
  let add : List (Vert × Vert × Vert × Vert) :=
    [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let kept := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

/-- A move is improving if it strictly decreases Θ. -/
def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner23 T a b c p q) lam < theta T lam

/-- Θ = 0 iff every edge has degree 3 and every vertex has degree 6 (ideal triangulation). -/
theorem theta_zero_iff_ideal (T : Triangulation) (lam : Nat) :
    theta T lam = 0 ↔
    (∀ e ∈ allEdges T, edgeDeg T e = 3) ∧
    (∀ v ∈ List.range T.numVerts, vertDeg T v = 6) := by
  sorry

end PachnerInvariant
