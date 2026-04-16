import PachnerInvariant.frontier

namespace PachnerInvariant

def isLocalMoveEdge
  (a b c p q : Nat) (e : Edge) : Prop :=
  e = (a,b) ∨ e = (b,c) ∨ e = (c,a) ∨
  e = (a,p) ∨ e = (b,p) ∨ e = (c,p) ∨
  e = (a,q) ∨ e = (b,q) ∨ e = (c,q) ∨
  e = (p,q)

end PachnerInvariant
