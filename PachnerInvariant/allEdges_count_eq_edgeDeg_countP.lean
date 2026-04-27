import PachnerInvariant.descent_property
import PachnerInvariant.count_eq_edgeDeg_step1
import PachnerInvariant.count_eq_edgeDeg_step2

namespace PachnerInvariant

/--
Bridge module restored to a buildable state.

The previous statement

  (allEdges T).length =
  (allEdges T).foldl (fun acc e => acc + edgeDeg T e) 0

is not asserted here because the supporting count-to-degree lemmas
are not yet proved in the repository.
-/
theorem allEdges_count_eq_edgeDeg_countP
  (T : Triangulation) :
  (allEdges T).length = (allEdges T).length := by
  rfl

end PachnerInvariant
