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

def minMax2 (a b : Nat) : Nat × Nat := if a ≤ b then (a, b) else (b, a)

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

def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove := [(a, b, c, p), (a, b, c, q)]
  let add    := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
  let remove := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
  let add    := [(a, b, c, p), (a, b, c, q)]
  let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
  { T with tets := kept ++ add }

def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner23 T a b c p q) lam < theta T lam

def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
  theta (pachner32 T a b c p q) lam < theta T lam

def eulerChar (T : Triangulation) : Int :=
  (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length

def twoTets : Triangulation :=
  { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }

def threeTets : Triangulation :=
  { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }

def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4

-- ---------------------------------------------------------------
-- Helper lemmas
-- ---------------------------------------------------------------

private theorem mul_self_eq_zero (n : Nat) : n * n = 0 ↔ n = 0 := by
  simp [Nat.mul_eq_zero]

-- Fix 1: use simp to reduce to n=0 form, then split_ifs + omega
private theorem sqDiff_eq_zero_iff (d ideal : Nat) :
    (if d ≥ ideal then d - ideal else ideal - d) *
    (if d ≥ ideal then d - ideal else ideal - d) = 0 ↔ d = ideal := by
  rw [mul_self_eq_zero]
  by_cases h : d ≥ ideal
  · simp only [h, ite_true]; omega
  · simp only [h, ite_false]; omega

-- Fix 2: remove unused Nat.zero_eq from simp call
private theorem foldl_add_eq_zero (f : Nat → Nat) (l : List Nat) (init : Nat) :
    l.foldl (fun acc x => acc + f x) init = 0 ↔
    init = 0 ∧ ∀ x ∈ l, f x = 0 := by
  induction l generalizing init with
  | nil => simp
  | cons hd tl ih =>
    simp only [List.foldl, List.mem_cons]
    rw [ih (init + f hd)]
    constructor
    · rintro ⟨h, ht⟩
      exact ⟨by omega, fun x hx => by
        cases hx with
        | inl heq => subst heq; omega
        | inr hmem => exact ht x hmem⟩
    · rintro ⟨hinit, hall⟩
      exact ⟨by have := hall hd (.inl rfl); omega,
             fun x hx => hall x (.inr hx)⟩

theorem sumSqDefect_zero_iff (vals : List Nat) (ideal : Nat) :
    sumSqDefect vals ideal = 0 ↔ ∀ d ∈ vals, d = ideal := by
  simp only [sumSqDefect]
  rw [show (fun acc d =>
      let diff := if d ≥ ideal then d - ideal else ideal - d
      acc + diff * diff) =
    (fun acc d => acc +
      (if d ≥ ideal then d - ideal else ideal - d) *
      (if d ≥ ideal then d - ideal else ideal - d)) from rfl]
  rw [foldl_add_eq_zero _ vals 0]
  simp [sqDiff_eq_zero_iff]

-- Fix 3: theta_zero_iff_ideal — use Nat.add_eq_zero_iff (not deprecated),
-- handle lam*x=0 via Nat.mul_eq_zero, fix membership proof usage
theorem theta_zero_iff_ideal (T : Triangulation) (lam : Nat) (hlam : lam > 0) :
    theta T lam = 0 ↔
    (∀ e ∈ allEdges T, edgeDeg T e = 3) ∧
    (∀ v ∈ List.range T.numVerts, vertDeg T v = 6) := by
  simp only [theta, Nat.add_eq_zero_iff]
  constructor
  · rintro ⟨h1, h2⟩
    have hv : sumSqDefect ((List.range T.numVerts).map (vertDeg T)) 6 = 0 := by
      rcases Nat.mul_eq_zero.mp h2 with h | h
      · omega
      · exact h
    rw [sumSqDefect_zero_iff] at h1 hv
    exact ⟨fun e he => h1 _ (List.mem_map.mpr ⟨e, he, rfl⟩),
           fun v hvm => hv _ (List.mem_map.mpr ⟨v, hvm, rfl⟩)⟩
  · rintro ⟨he, hv⟩
    refine ⟨?_, ?_⟩
    · rw [sumSqDefect_zero_iff]
      intro d hd
      rcases List.mem_map.mp hd with ⟨e, hem, rfl⟩
      exact he e hem
    · have : sumSqDefect ((List.range T.numVerts).map (vertDeg T)) 6 = 0 := by
        rw [sumSqDefect_zero_iff]
        intro d hd
        rcases List.mem_map.mp hd with ⟨v, hvm, rfl⟩
        exact hv v hvm
      simp [this]

-- ---------------------------------------------------------------
-- Concrete theorems
-- ---------------------------------------------------------------

theorem twoTets_move_improves :
    theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by native_decide

theorem twoTets_move_improves_all_lam :
    ∀ lam ∈ [1, 2, 3, 4, 5],
      theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by native_decide

theorem threeTets_move_improves :
    theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by native_decide

theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by native_decide
theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by native_decide

theorem pachner32_recovers :
    theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by native_decide

theorem pachner32_roundtrip :
    (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide

theorem eulerChar_preserved_twoTets :
    eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by native_decide

theorem eulerChar_preserved_threeTets :
    eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by native_decide

end PachnerInvariant
