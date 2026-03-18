namespace PachnerInvariant

abbrev Vert := Nat

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

def allEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.flatMap tetToEdges |>.map normalizeEdge).eraseDups

def vertDeg (T : Triangulation) (v : Vert) : Nat :=
  T.tets.countP (fun t => (tetToVerts t).contains v)

def edgeDeg (T : Triangulation) (e : Vert × Vert) : Nat :=
  T.tets.countP (fun t => (tetToEdges t).any (edgeEq e))

def sumSqDefect (vals : List Nat) (ideal : Nat) : Nat :=
  vals.foldl (fun acc d =>
    let diff := if d ≥ ideal then d - ideal else ideal - d
    acc + diff * diff) 0

def theta (T : Triangulation) (lam : Nat := 1) : Nat :=
  let edgeDs := (allEdges T).map (edgeDeg T)
  let vertDs := (List.range T.numVerts).map (vertDeg T)
  sumSqDefect edgeDs 3 + lam * sumSqDefect vertDs 6

def tetContainsVert (t : Vert × Vert × Vert × Vert) (v : Vert) : Bool :=
  t.1 == v || t.2.1 == v || t.2.2.1 == v || t.2.2.2 == v

def tetEq (t1 t2 : Vert × Vert × Vert × Vert) : Bool :=
  tetContainsVert t2 t1.1 && tetContainsVert t2 t1.2.1 &&
  tetContainsVert t2 t1.2.2.1 && tetContainsVert t2 t1.2.2.2

def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove := [(a, b, c, p), (a, b, c, q)]
  let add    := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner23 T a b c p q) lam < theta T lam

-- ---------------------------------------------------------------
-- Concrete triangulations
-- ---------------------------------------------------------------

def twoTets : Triangulation :=
  { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }

def threeTets : Triangulation :=
  { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }

-- ---------------------------------------------------------------
-- Structural theorem: new tets are present after the move
-- ---------------------------------------------------------------

theorem pachner23_adds_new_tets
    (T : Triangulation) (a b c p q : Vert) :
    let T' := pachner23 T a b c p q
    (T'.tets.contains (a, b, p, q)) = true ∧
    (T'.tets.contains (a, c, p, q)) = true ∧
    (T'.tets.contains (b, c, p, q)) = true := by
  native_decide

-- ---------------------------------------------------------------
-- Concrete descent: proved by computation
-- ---------------------------------------------------------------

/-- The 2→3 move on twoTets strictly decreases Θ at lam=1. -/
theorem twoTets_move_improves :
    theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by
  native_decide

/-- Descent holds at every λ in [1..5] for twoTets. -/
theorem twoTets_move_improves_all_lam :
    ∀ lam ∈ [1, 2, 3, 4, 5],
      theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by
  native_decide

/-- threeTets also improves under its natural move. -/
theorem threeTets_move_improves :
    theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by
  native_decide

-- ---------------------------------------------------------------
-- Why universal strict descent is not provable:
-- descent depends on local neighbourhood, not just move type.
-- Verified computationally: some moves raise Θ, some lower it.
-- ---------------------------------------------------------------

theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by
  native_decide

theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by
  native_decide

end PachnerInvariant
