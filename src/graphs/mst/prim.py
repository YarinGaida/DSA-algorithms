def prim_formal(graph, s):
    """
    Implements Prim's Algorithm for MST exactly according to the formal procedure.
    
    Args:
        graph (dict): Weighted adjacency list. { 'u': [('v', weight), ...] }
        s (str): Start node (Root of MST).
        
    Variables from algorithm:
    lambda_val (dict): Distance to the MST (not from start node!).
    epsilon (dict): The edge that connects node v to the MST (𝜀).
    T (list): The result set of MST edges.
    Q (set): Vertices not yet in MST.
    """
    
    # --- Initialization ---
    # ∀v ∈ V 𝜆(v) = ∞
    lambda_val = {v: float('inf') for v in graph}
    
    # 𝜆(s) = 0 ; 𝜀(s) = ∅
    lambda_val[s] = 0
    epsilon = {v: None for v in graph}
    
    # T = ∅ ; Q = V
    T = []
    Q = set(graph.keys())

    print(f"--- Starting Prim's Algorithm from {s} ---")

    # --- Main Loop ---
    # while Q ≠ ∅
    while Q:
        # get v ∈ Q s.t. 𝜆(v) is minimum
        # (Finding the "nearest" vertex to the MST)
        v = min(Q, key=lambda node: lambda_val[node])
        
        # Q = Q \ {v}
        Q.remove(v)
        
        # T = T ∪ 𝜀(v)
        # Note: We don't add anything for the first node (root) because epsilon is None
        if epsilon[v] is not None:
            T.append(epsilon[v])
            print(f"Added edge to MST: {epsilon[v]}")

        # ∀e(v,u) do (Update edge-cut)
        for u, weight in graph.get(v, []):
            
            # if u ∈ Q && 𝜆(u) > w(e)
            if u in Q and lambda_val[u] > weight:
                
                # 𝜆(u) = w(e)
                lambda_val[u] = weight
                
                # 𝜀(u) = e (We store the edge as a tuple: source, dest, weight)
                epsilon[u] = (v, u, weight)

    print("--- Prim's Algorithm Complete ---")
    return T