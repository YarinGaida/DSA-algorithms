from src.graphs.shortest_path.bellman_ford import bellman_ford_formal

def test_bellman_ford():
    print("\n--- Testing Bellman-Ford Algorithm ---")
    
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 2), ('E', 2)],
        'C': [('B', -1), ('D', 4)],
        'D': [],
        'E': []
    }

    distances = bellman_ford_formal(graph, s='A')
    
    print("\nFinal Distances (lambda):", distances)
    
    assert distances['B'] == 1
    
    assert distances['C'] == 2
    
    assert distances['D'] == 3
    
    print("Test Passed: Algorithm handled negative weights correctly.")

if __name__ == "__main__":
    test_bellman_ford()