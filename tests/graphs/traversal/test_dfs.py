from src.graphs.traversal.dfs import dfs_timestamp_style

def test_dfs_formal():
    print("\n--- Testing Formal DFS (Timestamp & Backtrack) ---")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'], # E מחובר גם ל-F, אבל F יתגלה דרך C או E תלוי בסדר
        'F': []
    }

    K, F = dfs_timestamp_style(graph, s='A')
    
    print("\nFinal Timestamps (K):", K)
    print("Final Parents (F):", F)

if __name__ == "__main__":
    test_dfs_formal()