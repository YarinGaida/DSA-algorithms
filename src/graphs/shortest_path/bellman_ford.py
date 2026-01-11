def bellman_ford_formal(graph, s):
    """
    Implements Bellman-Ford Algorithm exactly according to the formal procedure.
    Handles graphs with negative weights (but assumes no negative cycles for this specific implementation).
    
    Args:
        graph (dict): Weighted adjacency list. { 'u': [('v', weight), ...] }
        s (str): Start node.
        
    Variables from algorithm:
    lambda_val (dict): Current shortest distance from s (𝜆).
    flag (bool): Indicates if any update was made in the current iteration.
    """

    # --- Initialization ---
    # ∀v ∈ V 𝜆(v) = ∞ ; 𝜆(s) = 0
    lambda_val = {v: float('inf') for v in graph}
    lambda_val[s] = 0

    print(f"--- Starting Bellman-Ford from {s} ---")

    # --- Main Loop ---
    # repeat ... until Flag=FALSE
    # In Python, we simulate 'repeat-until' with 'while True' and a break condition.
    iteration = 1
    while True:
        # Flag = FALSE
        flag = False
        
        print(f"Iteration {iteration}...")

        # ∀e(u,v) ∈ E (Iterate over ALL edges in the graph)
        for u in graph:
            for v, weight in graph[u]:
                
                # if 𝜆(u) < ∞ && (𝜆(v) > 𝜆(u) + w(e))
                if lambda_val[u] != float('inf') and lambda_val[v] > lambda_val[u] + weight:
                    
                    # 𝜆(v) = 𝜆(u) + w(e)
                    lambda_val[v] = lambda_val[u] + weight
                    
                    # Flag = TRUE
                    flag = True
                    
                    # (Optional print to see updates)
                    # print(f"  Updated {v}: new dist {lambda_val[v]} (via {u})")

        # until Flag=FALSE
        if not flag:
            print("No more updates (Flag is False). Finished.")
            break
        
        iteration += 1

    return lambda_val