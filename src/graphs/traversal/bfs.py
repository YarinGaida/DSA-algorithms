import collections

def bfs_connected(graph, start_node):
    """
    Performs a Breadth-First Search on a connected graph
    starting from a specified node.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node: The node to start the traversal from.
    """

    # 1. Create a set to store visited nodes
    visited = set()

    # 2. Create a queue for BFS. 'deque' is efficient.
    queue = collections.deque()

    # 3. Add the starting node to the queue and mark it as visited
    queue.append(start_node)
    visited.add(start_node)

    print(f"--- Starting BFS from: {start_node} ---")

    # 4. Loop as long as the queue is not empty
    while queue:
        # 5. Dequeue a vertex from the front of the queue
        current_node = queue.popleft()

        # 6. Process the node (in this case, just print it)
        print(f"Visiting: {current_node}")

        # 7. Get all adjacent vertices (neighbors) of the dequeued vertex
        for neighbor in graph.get(current_node, []):

            # 8. If a neighbor has not been visited yet
            if neighbor not in visited:
                # 9. Mark it as visited
                visited.add(neighbor)
                # 10. Enqueue the neighbor
                queue.append(neighbor)

    print("--- BFS traversal complete ---")