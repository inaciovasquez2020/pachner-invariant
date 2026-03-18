import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

-- Standard tetrahedron: all edges deg 2, all verts deg 3
def tetrahedron : Triangulation :=
  { vertices    := 4,  edges := 6,  faces := 4,  is_sphere := true
    edge_degs   := [2, 2, 2, 2, 2, 2]
    vertex_degs := [3, 3, 3, 3] }

-- Regular-ish: edges near deg 3, verts near deg 6 (low Θ)
def nearIdeal : Triangulation :=
  { vertices    := 6,  edges := 9,  faces := 6,  is_sphere := false
    edge_degs   := [3, 3, 3, 3, 3, 3, 3, 3, 3]
    vertex_degs := [6, 6, 6, 6, 6, 6] }

-- Highly irregular: large degree variance (high Θ)
def irregular : Triangulation :=
  { vertices    := 8,  edges := 14, faces := 8,  is_sphere := false
    edge_degs   := [3, 3, 4, 2, 3, 5, 2, 3, 3, 4, 2, 3, 3, 2]
    vertex_degs := [5, 6, 7, 4, 6, 6, 5, 7] }

-- Extreme: all edges and verts far from ideal
def extreme : Triangulation :=
  { vertices    := 4,  edges := 6,  faces := 4,  is_sphere := false
    edge_degs   := [1, 1, 7, 7, 1, 7]
    vertex_degs := [1, 1, 12, 12] }

def separator := IO.println "---"

def main : IO Unit := do
  IO.println "=== Theta values at lam=1 ==="
  IO.println s!"tetrahedron   = {theta tetrahedron 1}"
  IO.println s!"nearIdeal     = {theta nearIdeal 1}"
  IO.println s!"irregular     = {theta irregular 1}"
  IO.println s!"extreme       = {theta extreme 1}"
  separator

  IO.println "=== Lambda sensitivity on irregular ==="
  for lam in [1, 2, 3, 5, 10] do
    IO.println s!"  lam={lam}  Θ={theta irregular lam}"
  separator

  IO.println "=== Single Pachner move ==="
  IO.println s!"tetrahedron before={theta tetrahedron 1}  after={theta (pachner_move tetrahedron) 1}"
  IO.println s!"nearIdeal   before={theta nearIdeal 1}    after={theta (pachner_move nearIdeal) 1}"
  IO.println s!"irregular   before={theta irregular 1}    after={theta (pachner_move irregular) 1}"
  IO.println s!"extreme     before={theta extreme 1}      after={theta (pachner_move extreme) 1}"
  separator

  IO.println "=== Descent holds after single move ==="
  IO.println s!"tetrahedron = {decide (theta (pachner_move tetrahedron) 1 > theta tetrahedron 1)}"
  IO.println s!"nearIdeal   = {decide (theta (pachner_move nearIdeal) 1 > theta nearIdeal 1)}"
  IO.println s!"irregular   = {decide (theta (pachner_move irregular) 1 > theta irregular 1)}"
  IO.println s!"extreme     = {decide (theta (pachner_move extreme) 1 > theta extreme 1)}"
  separator

  IO.println "=== Theta after sequence of moves ==="
  for n in [1, 2, 3, 5, 10] do
    IO.println s!"  tetrahedron after {n} moves = {theta (apply_moves tetrahedron n) 1}"
  separator

  IO.println "=== Monotone growth across 5 moves ==="
  let steps := (List.range 6).map (fun n => theta (apply_moves irregular n) 1)
  IO.println s!"  irregular Θ sequence: {steps}"
  separator

  IO.println "=== Optimal lambda per triangulation ==="
  IO.println s!"tetrahedron = {optimize_lam tetrahedron}"
  IO.println s!"nearIdeal   = {optimize_lam nearIdeal}"
  IO.println s!"irregular   = {optimize_lam irregular}"
  IO.println s!"extreme     = {optimize_lam extreme}"
  separator

  IO.println "=== Validity checks ==="
  IO.println s!"tetrahedron valid = {is_valid tetrahedron}"
  IO.println s!"empty       valid = {is_valid { vertices := 0, edges := 0, faces := 0, is_sphere := false, edge_degs := [], vertex_degs := [] }}"
