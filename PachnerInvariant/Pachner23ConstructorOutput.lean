import PachnerInvariant.descent_property

namespace PachnerInvariant

theorem pachner23_tets_eq_old_filter_append_new
    (T : Triangulation) (a b c p q : Vert) :
    (pachner23 T a b c p q).tets =
      T.tets.filter
          (fun t =>
            !([(a, b, c, p), (a, b, c, q)]).any (tetEq t)) ++
        [(a, b, p, q), (a, c, p, q), (b, c, p, q)] := by
  rfl

end PachnerInvariant
