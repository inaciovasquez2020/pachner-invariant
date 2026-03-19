import Lake
open Lake DSL

package «pachner_invariant» {}

lean_lib PachnerInvariant

@[default_target]
lean_exe Main where
  root := `Main

-- Add mathlib4 as a dependency
require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "stable"
