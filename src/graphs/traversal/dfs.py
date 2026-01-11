def dfs_timestamp_style(graph, s):
    """
    Implements the formal DFS algorithm using Time Stamps and Parent Pointers.
    Based on the iterative procedure: DFS(G, s; K, F).

    Variables Mapping:
    - K (dict): Time stamp array (serves as 'visited'). K[v]=0 means 'new'.
    - F (dict): Parent pointer array. F[v] stores the node we came from.
    - edge_ptrs (dict): Keeps track of the next neighbor to visit for each node.
                        This simulates marking edges as "old".
    """
    
    # --- 1. Initialization ---
    # ∀v ∈ V do K[v] = 0 ; F[v] = ∅
    # We initialize all vertices in the graph
    K = {v: 0 for v in graph} 
    F = {v: None for v in graph}
    
    # To implement 'mark edge as old', we use an index pointer for each node.
    # edge_ptrs[u] tells us which neighbor index is the next "new" edge.
    edge_ptrs = {v: 0 for v in graph}

    # K[s] = 1; u = s; i = 2;
    K[s] = 1        # Mark start node with time 1
    u = s           # 'u' is the current vertex pointer
    i = 2           # 'i' is the global time counter
    
    print(f"--- Starting DFS from {s} (Time: 1) ---")

    # --- 2. Main Loop ---
    # Loop condition: while ∃ "new" e(u,v) || F[u] ≠ ∅
    while True:
        neighbors = graph.get(u, [])
        ptr = edge_ptrs[u]
        
        # Check if there is a "new" edge e(u,v)
        # We do this by checking if the pointer is within the neighbors list range
        if ptr < len(neighbors):
            v = neighbors[ptr]
            
            # mark e "old" (Increment the pointer so we don't visit this edge again)
            edge_ptrs[u] += 1
            
            # if K[v] = 0 (Check if neighbor is visited for the first time)
            if K[v] == 0:
                print(f"Visiting: {v} (Time: {i}), Parent: {u}")
                
                # Update tables and move forward:
                F[v] = u        # Set parent
                K[v] = i        # Set time stamp
                i += 1          # Increment time counter
                u = v           # Update current vertex to v (Step forward)
            
            # If K[v] != 0, the edge is effectively ignored (loop continues)
            
        else:
            # --- 3. Backtracking ---
            # This block executes when there are no more "new" edges from u.
            # else u = F[u]
            
            if F[u] is not None:
                print(f"Backtracking from {u} to {F[u]}")
                u = F[u]    # Return to the parent node
            else:
                # Logic: If F[u] is None and we have no new edges, 
                # we have finished traversing the connected component.
                break
                
    print("--- DFS Complete ---")
    return K, F