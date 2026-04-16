import PachnerInvariant.frontier

open List

lemma edgesOfTet_nodup (t : Tet) :
  (edgesOfTet t).Nodup := by
  classical
  -- edgesOfTet is a fixed 6-edge list of a tetrahedron with no repetitions
  -- reduce by explicit enumeration (definition of edgesOfTet)
  unfold edgesOfTet
  -- goal becomes Nodup on a concrete 6-element list
  decide
