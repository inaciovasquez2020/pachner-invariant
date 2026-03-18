import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

-- Single tetrahedron: 1 tet, 4 verts, 6 edges all with deg 1
def singleTet : Triangulation :=
  { numVerts := 4
    tets     := [(0, 1, 2, 3)] }

-- Two tets sharing face (0,1,2), apices at 3 and 4
-- Shared edges (0,1),(0,2),(1,2) have deg 2; outer edges have deg 1
  { numVerts := 5
    tets     := [(0, 1, 2, 3), (0, 1, 2, 4)] }

-- After 2→3 move on twoTets: new edge (3,4) has deg 3 (ideal!)
def afterMove : Triangulation := pachner23 twoTets 0 1 2 3 4

-- Larger triangulation: 3 tets, more varied degrees
  { numVerts := 6
    tets     := [(0,1,2,3), (0,1,2,4), (0,1,3,5)] }

def separator := IO.println "---"

def main : IO Unit := do
  IO.println "=== Edge and vertex degrees ==="
  IO.println s!"singleTet edges         = {allEdges singleTet}"
  IO.println s!"singleTet edge degs     = {(allEdges singleTet).map (edgeDeg singleTet)}"
  IO.println s!"singleTet vert degs     = {(List.range 4).map (vertDeg singleTet)}"
  IO.println s!"twoTets   edge degs     = {(allEdges twoTets).map (edgeDeg twoTets)}"
  IO.println s!"twoTets   vert degs     = {(List.range 5).map (vertDeg twoTets)}"
  separator

  IO.println "=== Theta values lam=1 ==="
  IO.println s!"singleTet  = {theta singleTet 1}"
  IO.println s!"twoTets    = {theta twoTets 1}"
  IO.println s!"afterMove  = {theta afterMove 1}"
  IO.println s!"threeTets  = {theta threeTets 1}"
  separator

  IO.println "=== Effect of 2→3 move on twoTets ==="
  IO.println s!"before     = {theta twoTets 1}"
  IO.println s!"after      = {theta afterMove 1}"
  IO.println s!"improving? = {isImproving twoTets 0 1 2 3 4 1}"
  IO.println s!"new edges  = {allEdges afterMove}"
  IO.println s!"new edge degs = {(allEdges afterMove).map (edgeDeg afterMove)}"
  IO.println s!"new vert degs = {(List.range 5).map (vertDeg afterMove)}"
  separator

  IO.println "=== Move precondition check ==="
  IO.println s!"can apply on twoTets (0,1,2,3,4) = {can_apply_pachner23 twoTets 0 1 2 3 4}"
  IO.println s!"can apply on singleTet (0,1,2,3,4) = {can_apply_pachner23 singleTet 0 1 2 3 4}"
  separator

  IO.println "=== Lambda sensitivity ==="
  for lam in [1, 2, 3, 5, 10] do
    IO.println s!"  twoTets lam={lam}  Θ={theta twoTets lam}"
  separator

  IO.println "=== Optimal lambda ==="
  IO.println s!"singleTet  = {optimize_lam singleTet}"
  IO.println s!"twoTets    = {optimize_lam twoTets}"
  IO.println s!"afterMove  = {optimize_lam afterMove}"
  separator

  IO.println "=== Validity ==="
  IO.println s!"singleTet valid = {is_valid singleTet}"
  IO.println s!"empty     valid = {is_valid { numVerts := 0, tets := [] }}"
  IO.println s!"total simplices singleTet = {total_simplices singleTet}"
  IO.println s!"total simplices twoTets   = {total_simplices twoTets}"
