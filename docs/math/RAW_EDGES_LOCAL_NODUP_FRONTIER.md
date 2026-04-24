# RawEdges local no-duplicate frontier

Status: BLOCKED BY IMPORT CYCLE.

The desired local theorem is:

```lean
theorem pairwiseDistinctTet_normalized_edges_pairwise
    (t : Vert × Vert × Vert × Vert)
    (h : pairwiseDistinctTet t) :
    List.Pairwise (· ≠ ·) ((tetToEdges t).map normalizeEdge)
The proof should reuse the existing theorem:
tetToEdges_normalized_no_collision
However, tetToEdges_normalized_no_collision currently lives in PachnerInvariant.frontier, while frontier imports the old count bridge path. Importing frontier from the rawEdges layer creates a build cycle.
Weakest sufficient next step:
Move `normalizeEdge_eq_iff` and `tetToEdges_normalized_no_collision` into a lower dependency file that imports only descent_property, then import that lower file from both frontier and RawEdgesCount.
No multiplicity-count closure is claimed yet.
