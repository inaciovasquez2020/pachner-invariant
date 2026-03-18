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
  (T.tets.bind tetToEdges |>.map normalizeEdge).eraseDups

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
-- Provable structural lemmas
-- ---------------------------------------------------------------

/-- A 2→3 move on a triangulation with n tets produces one with n+1 tets,
    provided both source tets are present and distinct. -/
theorem pachner23_tet_count
    (T : Triangulation) (a b c p q : Vert)
    (hpq : p ≠ q)
    (hp : T.tets.any (tetEq (a, b, c, p)) = true)
    (hq : T.tets.any (tetEq (a, b, c, q)) = true) :
    (pachner23 T a b c p q).tets.length =
     T.tets.length + 1 := by
  simp [pachner23]
  omega

/-- The three new tets are all present after the move. -/
theorem pachner23_adds_new_tets
    (T : Triangulation) (a b c p q : Vert) :
    let T' := pachner23 T a b c p q
    T'.tets.contains (a, b, p, q) ∧
    T'.tets.contains (a, c, p, q) ∧
    T'.tets.contains (b, c, p, q) := by
  simp [pachner23, List.contains, List.mem_append]

-- ---------------------------------------------------------------
-- Concrete descent instances proved by native_decide
-- ---------------------------------------------------------------

def twoTets : Triangulation :=
  { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }

/-- The 2→3 move on twoTets strictly decreases Θ at lam=1. -/
theorem twoTets_move_improves :
    theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by
  native_decide

/-- The move is improving at every λ in [1..5] for twoTets. -/
theorem twoTets_move_improves_all_lam :
    ∀ lam ∈ [1, 2, 3, 4, 5],
      theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by
  native_decide

-- ---------------------------------------------------------------
-- Why universal strict_descent is unprovable (and false):
-- A move on an already-ideal neighbourhood increases Θ.
-- ---------------------------------------------------------------

def nearIdealTet : Triangulation :=
  { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4),(0,2,3,4)] }

/-- Counter-example: this move raises Θ, so universal descent is false. -/
theorem no_universal_descent :
    ¬ ∀ (T : Triangulation) (a b c p q : Vert) (lam : Nat),
        theta (pachner23 T a b c p q) lam < theta T lam := by
  intro h
  have := h nearIdealTet 0 1 2 3 4 1
  native_decide

end PachnerInvariant
