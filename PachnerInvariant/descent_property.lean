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

def tetToFaces (t : Vert × Vert × Vert × Vert) : List (Vert × Vert × Vert) :=
  let a := t.1; let b := t.2.1; let c := t.2.2.1; let d := t.2.2.2
  [(a,b,c),(a,b,d),(a,c,d),(b,c,d)]

def edgeEq (e1 e2 : Vert × Vert) : Bool :=
  (e1.1 == e2.1 && e1.2 == e2.2) || (e1.1 == e2.2 && e1.2 == e2.1)

def normalizeEdge (e : Vert × Vert) : Vert × Vert :=
  if e.1 ≤ e.2 then e else (e.2, e.1)

def minMax2 (a b : Nat) : Nat × Nat :=
  if a ≤ b then (a, b) else (b, a)

def sortThree (a b c : Nat) : Nat × Nat × Nat :=
  let (a₁, b₁) := minMax2 a b
  let (b₂, c₁) := minMax2 b₁ c
  let (a₂, b₃) := minMax2 a₁ b₂
  (a₂, b₃, c₁)

def normalizeFace (f : Vert × Vert × Vert) : Vert × Vert × Vert :=
  sortThree f.1 f.2.1 f.2.2

def allEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.flatMap tetToEdges |>.map normalizeEdge).eraseDups

def allFaces (T : Triangulation) : List (Vert × Vert × Vert) :=
  (T.tets.flatMap tetToFaces |>.map normalizeFace).eraseDups

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

/-- 2→3 Pachner move -/
def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove := [(a, b, c, p), (a, b, c, q)]
  let add    := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

/-- 3→2 inverse Pachner move -/
def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let add    := [(a, b, c, p), (a, b, c, q)]
  let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner23 T a b c p q) lam < theta T lam

def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner32 T a b c p q) lam < theta T lam

/-- Euler characteristic: V − E + F − T (= 0 for a closed 3-manifold triangulation) -/
def eulerChar (T : Triangulation) : Int :=
  (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length

-- ---------------------------------------------------------------
-- Concrete triangulations
-- ---------------------------------------------------------------

def twoTets : Triangulation :=
  { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }

def threeTets : Triangulation :=
  { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }

def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4

-- ---------------------------------------------------------------
-- 1. Concrete descent (2→3)
-- ---------------------------------------------------------------

theorem twoTets_move_improves :
    theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by
  native_decide

theorem twoTets_move_improves_all_lam :
    ∀ lam ∈ [1, 2, 3, 4, 5],
      theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by
  native_decide

theorem threeTets_move_improves :
    theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by
  native_decide

theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by
  native_decide

theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by
  native_decide

-- ---------------------------------------------------------------
-- 2. 3→2 inverse move: recovers original theta
-- ---------------------------------------------------------------

theorem pachner32_recovers :
    theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by
  native_decide

theorem pachner32_roundtrip :
    (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by
  native_decide

-- ---------------------------------------------------------------
-- 3. Euler characteristic preserved by 2→3 move
--    2→3: V+0, E+1, F+2, T+1 → ΔV−ΔE+ΔF−ΔT = 0−1+2−1 = 0
-- ---------------------------------------------------------------

theorem eulerChar_preserved_twoTets :
    eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by
  native_decide

theorem eulerChar_preserved_threeTets :
    eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by
  native_decide

-- ---------------------------------------------------------------
-- 4. theta = 0 iff all degrees are ideal
--    Proof requires foldl-sum induction; sketch:
--    sumSqDefect = 0 iff every (d−ideal)² = 0 iff every d = ideal.
--    Full proof needs: foldl (acc + f d) 0 = 0 ↔ ∀ d, f d = 0
--    which follows from Nat add_eq_zero and List induction.
-- ---------------------------------------------------------------

theorem sumSqDefect_zero_iff (vals : List Nat) (ideal : Nat) :
    sumSqDefect vals ideal = 0 ↔ ∀ d ∈ vals, d = ideal := by
  sorry

theorem theta_zero_iff_ideal (T : Triangulation) (lam : Nat) (_ : lam > 0) :
    theta T lam = 0 ↔
    (∀ e ∈ allEdges T, edgeDeg T e = 3) ∧
    (∀ v ∈ List.range T.numVerts, vertDeg T v = 6) := by
  sorry

end PachnerInvariant
