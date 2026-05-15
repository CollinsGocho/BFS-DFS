# Graph Traversal Algorithms: BFS & DFS

This repository contains Python implementations of two fundamental graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. The code was originally written in Google Colab and demonstrates how to traverse a graph structure using iterative (queue-based) and recursive approaches.

## Files

- `bfs_&_dfs_py.py` – Contains both BFS and DFS implementations with sample graphs.

## Algorithms Overview

### Breadth-First Search (BFS)

BFS explores a graph level by level, starting from a given root node. It uses a **queue** (via `collections.deque`) to manage the traversal order and a `visited` set to prevent revisiting nodes.

**Key Features:**
- Iterative approach
- Uses `deque` for efficient popleft operations
- Visits neighbors in FIFO order

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking. This implementation uses **recursion** and a `visited` set.

**Key Features:**
- Recursive approach
- Simple and compact code
- Uses system call stack implicitly

##  Example Graphs

### BFS Example (Graph 1)
python
graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1],
    3: [0],
    4: [1]
}
### DFS Example (Graph 2)
python
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}
