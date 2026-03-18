import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

def singleTet : Triangulation := { numVerts := 4, tets := [(0,1,2,3)] }

def sep := IO.println "---"

def main : IO Unit := do
  IO.println "=== 1. theta and degrees ==="
  IO.println s!"twoTets   edge degs = {(allEdges twoTets).map (edgeDeg twoTets)}"
  IO.println s!"twoTets   vert degs = {(List.range 5).map (vertDeg twoTets)}"
  IO.println s!"afterMove edge degs = {(allEdges afterMove23).map (edgeDeg afterMove23)}"
  IO.println s!"afterMove vert degs = {(List.range 5).map (vertDeg afterMove23)}"
  IO.println s!"theta twoTets   = {theta twoTets 1}"
  IO.println s!"theta afterMove = {theta afterMove23 1}"
  sep

  IO.println "=== 2. 3→2 inverse move ==="
  IO.println s!"can apply 3→2 on afterMove = {can_apply_pachner32 afterMove23 0 1 2 3 4}"
  IO.println s!"theta after 3→2            = {theta (pachner32 afterMove23 0 1 2 3 4) 1}"
  IO.println s!"3→2 improves afterMove?    = {isImproving32 afterMove23 0 1 2 3 4 1}"
  IO.println s!"roundtrip restores twoTets = {(pachner32 afterMove23 0 1 2 3 4).tets == twoTets.tets}"
  sep

  IO.println "=== 3. Greedy improvement sequence ==="
  IO.println s!"improving moves in twoTets   = {countImprovingMoves twoTets 1}"
  IO.println s!"improving moves in afterMove = {countImprovingMoves afterMove23 1}"
  let g0 := twoTets
  let g1 := greedyImprove twoTets 1 1
  let g2 := greedyImprove twoTets 1 2
  let g3 := greedyImprove twoTets 1 5
  IO.println s!"greedy steps 0→1→2→5: theta = [{theta g0 1}, {theta g1 1}, {theta g2 1}, {theta g3 1}]"
  IO.println s!"greedy step 1 tets    = {g1.tets}"
  sep

  IO.println "=== 4. Euler characteristic ==="
  IO.println s!"eulerChar singleTet  = {eulerChar singleTet}"
  IO.println s!"eulerChar twoTets    = {eulerChar twoTets}"
  IO.println s!"eulerChar afterMove  = {eulerChar afterMove23}"
  IO.println s!"eulerChar threeTets  = {eulerChar threeTets}"
  IO.println s!"Δ(2→3) on twoTets   = {eulerChar afterMove23 - eulerChar twoTets}"
  sep

  IO.println "=== 5. Lambda optimization ==="
  for lam in [1, 2, 3, 5, 10] do
    IO.println s!"  twoTets lam={lam} Θ={theta twoTets lam}"
  IO.println s!"optimal lam twoTets   = {optimize_lam twoTets}"
  IO.println s!"optimal lam afterMove = {optimize_lam afterMove23}"
  sep

  IO.println "=== 6. Validity and simplices ==="
  IO.println s!"twoTets valid   = {is_valid twoTets}"
  IO.println s!"empty   valid   = {is_valid { numVerts := 0, tets := [] }}"
  IO.println s!"total singleTet = {total_simplices singleTet}"
  IO.println s!"total twoTets   = {total_simplices twoTets}"
  IO.println s!"total afterMove = {total_simplices afterMove23}"
