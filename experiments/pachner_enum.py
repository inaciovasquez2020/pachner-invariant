import itertools

# Define local Pachner moves: (2->3), (3->2), (1->4), (4->1)
# Edge, tetrahedron, vertex incidence configurations
def delta_theta(edge_degrees, vertex_degrees, lambda_val=1):
    # compute Θ(T') - Θ(T) for local move
    theta_before = sum((d-3)**2 for d in edge_degrees) + lambda_val*sum((d-6)**2 for d in vertex_degrees)
    # example update: simple placeholder for 2->3 move
    edge_degrees_new = [d+1 if i<2 else d for i,d in enumerate(edge_degrees)]
    vertex_degrees_new = [d+1 if i<3 else d for i,d in enumerate(vertex_degrees)]
    theta_after = sum((d-3)**2 for d in edge_degrees_new) + lambda_val*sum((d-6)**2 for d in vertex_degrees_new)
    return theta_after - theta_before

# Enumerate all small local configurations
edges = [2,3,4]
vertices = [5,6,7]
for e_config in itertools.product(edges, repeat=3):
    for v_config in itertools.product(vertices, repeat=4):
        dt = delta_theta(list(e_config), list(v_config))
        print(f"Edges: {e_config}, Vertices: {v_config}, ΔΘ: {dt}")
