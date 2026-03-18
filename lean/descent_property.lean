structure Triangulation3 :=
(V : Type)
(E : Type)
(Tet : Type)
(deg_edge : E → Nat)
(deg_vertex : V → Nat)

def Theta (T : Triangulation3) (λ : Nat) : Nat :=
  (Finset.univ.sum (fun e => (T.deg_edge e - 3)^2)) +
  λ * (Finset.univ.sum (fun v => (T.deg_vertex v - 6)^2))

axiom pachner_move : Triangulation3 → Triangulation3 → Prop

def descent_property (λ : Nat) : Prop :=
  ∀ T, ¬ is_boundary_simplex T →
    ∃ T', pachner_move T T' ∧ Theta T' λ < Theta T λ
