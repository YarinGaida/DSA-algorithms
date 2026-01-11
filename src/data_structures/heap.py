import math
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Any

class MaxHeap:
    """
    A Max-Heap implementation using an array.
    In a Max-Heap, the key of each node is >= the keys of its children.
    """
    def __init__(self):
        self.heap = []

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def max_heapify(self, i: int, n: int):
        """
        Maintains the Max-Heap property for a subtree rooted at index i.
        Time Complexity: O(log n) - height of the tree.
        """
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        # Check if left child exists and is greater than root
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not root, swap and continue heapifying down
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest, n)

    def build_max_heap(self, arr: List[int]):
        """
        Converts a random array into a Max-Heap.
        Crucial: We iterate from the last non-leaf node down to 0.
        Time Complexity: O(n) (mathematically proven, clearer than O(n log n)).
        """
        self.heap = arr
        n = len(self.heap)
        
        # Start from the last parent node and go up to the root
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i, n)

    def insert(self, key: int):
        """Inserts a new key into the heap."""
        self.heap.append(key)
        # Bubble up logic (optional for this exercise, but good to have)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # --- Visualization Tools (Keeping your cool code) ---
    def plot_heap(self):
        """Visualizes the heap as a tree using NetworkX and Matplotlib."""
        G = nx.DiGraph()
        n = len(self.heap)

        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n:
                G.add_edge(self.heap[i], self.heap[left])
            if right < n:
                G.add_edge(self.heap[i], self.heap[right])

        if not self.heap:
            print("Heap is empty, nothing to plot.")
            return

        try:
            pos = self._hierarchy_pos(G, self.heap[0])
            plt.figure(figsize=(8, 6))
            nx.draw(G, pos, with_labels=True, node_size=2000, 
                   node_color="lightblue", font_size=12, font_weight="bold", arrows=False)
            plt.title("Max Heap Visualization")
            plt.show()
        except Exception as e:
            print(f"Could not plot heap: {e}")

    def _hierarchy_pos(self, G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """Helper function to calculate node positions for a tree layout."""
        pos = {root: (xcenter, vert_loc)}
        neighbors = list(G.neighbors(root))
        if len(neighbors) != 0:
            dx = width / len(neighbors)
            nextx = xcenter - width / 2 - dx / 2
            for neighbor in neighbors:
                nextx += dx
                pos.update(self._hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap,
                                             vert_loc=vert_loc - vert_gap, xcenter=nextx))
        return pos