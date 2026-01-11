def floyd_warshall(graph):
    """
    Implements Floyd-Warshall Algorithm for All-Pairs Shortest Path.
     Complexity: O(V^3) - Very slow for large graphs, but perfect for small ones.
    
    Args:
        graph (dict): Weighted adjacency list.
        
    Returns:
        dist (dict of dicts): dist[u][v] is the shortest distance from u to v.
    """
    
    # 1. Initialize distance matrix
    # We create a table where dist[u][v] = infinity initially
    vertices = list(graph.keys())
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}

    # 2. Set distance to self to 0, and fill initial edge weights
    for v in vertices:
        dist[v][v] = 0
        for neighbor, weight in graph[v]:
            dist[v][neighbor] = weight

    # 3. The Algorithm (3 Nested Loops)
    # k = intermediate node (התחנה בדרך)
    # i = source node (מאיפה יצאנו)
    # j = destination node (לאן הגענו)
    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                # The Core Logic:
                # Is it shorter to go from i to j DIRECTLY?
                # OR is it shorter to go i -> k -> j ?
                
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist