from src.graphs.traversal.bfs import bfs_connected

def test_bfs_run():
    print("\n--- Testing BFS ---")
    
    # גרף לדוגמה
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Running BFS starting from 'A':")
    bfs_connected(graph, start_node='A')

if __name__ == "__main__":
    test_bfs_run()