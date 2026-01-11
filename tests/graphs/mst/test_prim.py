from src.graphs.mst.prim import prim_formal

def test_prim():
    print("\n--- Testing Prim's Algorithm (MST) ---")
    
    
    graph = {
        'A': [('B', 1), ('C', 10)],
        'B': [('A', 1), ('C', 2)],
        'C': [('A', 10), ('B', 2), ('D', 5)],
        'D': [('C', 5)]
    }
    

    mst_edges = prim_formal(graph, s='A')
    
    print("\nFinal MST Edges (T):", mst_edges)
    
    total_weight = sum(edge[2] for edge in mst_edges)
    print(f"Total MST Weight: {total_weight}")
    
    assert total_weight == 8
    for u, v, w in mst_edges:
        assert w != 10
        
    print("Test Passed: Minimum Spanning Tree constructed correctly.")

if __name__ == "__main__":
    test_prim()