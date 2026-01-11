from src.graphs.shortest_path.floyd_warshall import floyd_warshall

def test_floyd_warshall():
    print("\n--- Testing Floyd-Warshall Algorithm ---")
    
    graph = {
        'A': [('C', -2)],       
        'B': [('A', 4), ('C', 3)],
        'C': [('D', 2)],
        'D': [('B', -1)]
    }

    dist_matrix = floyd_warshall(graph)
    
    print("All-Pairs Shortest Paths Matrix:")
    for v in dist_matrix:
        print(f"{v}: {dist_matrix[v]}")

    assert dist_matrix['A']['B'] == -1
    
    assert dist_matrix['B']['A'] == 4

    print("\nTest Passed: All pairs calculated correctly.")

if __name__ == "__main__":
    test_floyd_warshall()