import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

def singleTet : Triangulation :=
  { numVerts := 4, tets := [(0,1,2,3)] }

def afterMove : Triangulation := pachner23 twoTets 0 1 2 3 4

def separator := IO.println "---"

def main : IO Unit := do
  IO.println "=== Edge and vertex degrees ==="
  IO.println s!"singleTet edge degs  = {(allEdges singleTet).map (edgeDeg singleTet)}"
  IO.println s!"singleTet vert degs  = {(List.range 4).map (vertDeg singleTet)}"
  IO.println s!"twoTets   edge degs  = {(allEdges twoTets).map (edgeDeg twoTets)}"
  IO.println s!"twoTets   vert degs  = {(List.range 5).map (vertDeg twoTets)}"
  IO.println s!"afterMove edge degs  = {(allEdges afterMove).map (edgeDeg afterMove)}"
  IO.println s!"afterMove vert degs  = {(List.range 5).map (vertDeg afterMove)}"
  separator

  IO.println "=== Theta values lam=1 ==="
  IO.println s!"singleTet  = {theta singleTet 1}"
  IO.println s!"twoTets    = {theta twoTets 1}"
  IO.println s!"threeTets  = {theta threeTets 1}"
  IO.println s!"afterMove  = {theta afterMove 1}"
  separator

  IO.println "=== Effect of 2→3 move ==="
  IO.println s!"twoTets before = {theta twoTets 1}"
  IO.println s!"twoTets after  = {theta afterMove 1}"
  IO.println s!"improving?     = {isImproving twoTets 0 1 2 3 4 1}"
  separator

  IO.println "=== Precondition check ==="
  IO.println s!"can apply twoTets   = {can_apply_pachner23 twoTets 0 1 2 3 4}"
  IO.println s!"can apply singleTet = {can_apply_pachner23 singleTet 0 1 2 3 4}"
  separator

  IO.println "=== Lambda sensitivity ==="
  for lam in [1, 2, 3, 5, 10] do
    IO.println s!"  twoTets lam={lam} Θ={theta twoTets lam}"
  separator

  IO.println "=== Optimal lambda ==="
  IO.println s!"singleTet = {optimize_lam singleTet}"
  IO.println s!"twoTets   = {optimize_lam twoTets}"
  IO.println s!"afterMove = {optimize_lam afterMove}"
  separator

  IO.println "=== Validity ==="
  IO.println s!"singleTet valid = {is_valid singleTet}"
  IO.println s!"empty valid     = {is_valid { numVerts := 0, tets := [] }}"
  IO.println s!"total singleTet = {total_simplices singleTet}"
  IO.println s!"total twoTets   = {total_simplices twoTets}"
