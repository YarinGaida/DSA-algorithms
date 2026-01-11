from collections import deque

def dfs_topo_formal(graph):
    """
    Implements DFS-Based Topological Sort 
    
    Variables from the algorithm:
    Q = Queue of start nodes (in-degree = 0)
    F = Parent pointer array (Where visited from)
    S = Stack for the result (Topology order)
    edge_ptrs = Simulates marking edges as "old"
    """
    
    # --- 1. Initialization (Find start nodes) ---
    # ∀s ∈ V s.t. d+(s) = 0 ENQUEUE(Q, s)
    
    # Calculate in-degrees
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            # Ensure v is in our dictionary (handle nodes with no outgoing edges)
            if v not in in_degree: in_degree[v] = 0
            in_degree[v] += 1
            
    # Initialize Queue with nodes having in-degree 0
    Q = deque([u for u in graph if in_degree[u] == 0])
    
    # ∀v ∈ V do F[v] = ∅
    F = {u: None for u in graph}
    
    # S = Empty Stack
    S = []
    
    # ∀e ∈ E mark e "new" (We use pointers to track current edge)
    edge_ptrs = {u: 0 for u in graph}
    
    # We need a visited set to correctly implement "if F[v] = ∅" logic safely
    visited = set()

    print(f"--- Starting DFS-TOPO with Q: {list(Q)} ---")

    # --- 2. Main Loop ---
    # while s = DEQUEUE(Q) ≠ ∅
    while Q:
        s = Q.popleft()
        
        # Safety check: skip if somehow already visited
        if s in visited:
            continue
            
        u = s
        visited.add(u)
        
        # Inner Loop: while u has "new" edge OR F[u] ≠ ∅
        # (We interpret F[u] ≠ ∅ as 'we can backtrack', or if u is start node s)
        while True:
            neighbors = graph.get(u, [])
            ptr = edge_ptrs[u]
            
            # Check if u has "new" edge e(u,v)
            if ptr < len(neighbors):
                v = neighbors[ptr]
                
                # mark e "old"
                edge_ptrs[u] += 1
                
                # if F[v] = ∅ (Meaning: First time visit)
                if v not in visited:
                    # F[v] = u ; u = v
                    F[v] = u
                    u = v
                    visited.add(v) # Mark as visited
                
                # else: edge is old/visited, loop continues to next edge
                
            else:
                # --- Backtrack Phase ---
                # else PUSH(S, u) ; u = F[u]
                
                # We finished all neighbors of u, so we push u to Stack
                S.append(u)
                
                if F[u] is not None:
                    # Backtrack to parent
                    u = F[u]
                elif u == s:
                    # If we are at start node 's' and have no parent, we are done with this component
                    break
                else:
                    break

    # The result is the stack S read from top to bottom (LIFO)
    # Since we appended to list, the end is the top. 
    # Usually Topo Sort returns the reverse of the finishing times.
    return S[::-1]