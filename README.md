# 🐍 DSA Implementations in Python

This repo is my personal collection of Data Structures and Algorithms, built from scratch.
The main goal here wasn't just to write code that works, but to understand the logic and complexity "under the hood" without relying on external libraries.

Everything here is written in pure Python.

## 📂 What's Inside

### 1. Sorting
Classic sorting algorithms implemented to visualize $O(n^2)$ vs $O(n \log n)$.
- [x] [Insertion Sort](src/sorting/insertion_sort.py)
- [x] [Merge Sort](src/sorting/merge_sort.py)
- [x] [Quick Sort](src/sorting/quick_sort.py)
- [ ] Bucket Sort [planned]

### 2. Data Structures
Building the foundations.
- [x] [Linked Lists](src/data_structures/linked_list.py)
- [x] [Stack](src/data_structures/stack.py) & [Queue](src/data_structures/queue.py)
- [x] [Binary Heaps](src/data_structures/heap.py)
- [ ] Binary Search Trees (BST) [planned]

### 3. Graphs & Traversal
Basic navigation of nodes and edges.
- [x] [BFS (Breadth-First Search)](src/graphs/traversal/bfs.py)
- [x] [DFS (Depth-First Search)](src/graphs/traversal/dfs.py)
- [x] [Topological Sort](src/graphs/traversal/dfs_topo.py)

### 4. Shortest Path (Weighted Graphs)
Solvers for weighted graph problems.
- [x] [Dijkstra](src/graphs/shortest_path/dijkstra.py)
- [x] [Bellman-Ford](src/graphs/shortest_path/bellman_ford.py)
- [x] [Floyd-Warshall](src/graphs/shortest_path/floyd_warshall.py)

### 5. Network Flow & MST
Advanced graph theory implementations.
- [x] [Prim's Algorithm](src/graphs/mst/prim.py)
- [ ] [Ford-Fulkerson](src/graphs/flow/ford_fulkerson.py) [planned]
- [ ] [Edmonds-Karp](src/graphs/flow/edmonds_karp.py) [planned]
