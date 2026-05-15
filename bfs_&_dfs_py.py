
#BFS 

import collections # Import the collections module for deque, which is optimized for appending and popping from both ends.

def bfs(graph, root):
    visited = {root} # Initialize a set to keep track of visited nodes to prevent cycles and redundant processing.
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        print(vertex,end=" ")
        # The `visited` set is updated when a node is added to the queue, as shown below.

        for neighbour in graph[vertex]: # Iterate through all neighbors of the current vertex.
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    print(visited) # Print the set of all visited nodes after the BFS completes.

if __name__ == "__main__":
    # Define the graph using a dictionary
    graph = {0: [1, 2, 3], 1: [0, 2,4], 2: [0, 1], 3: [0], 4: [1]}
    bfs(graph, 0) # Start the BFS traversal from node 0.

#DFS
graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]} # Define the graph using a dictionary.
visited =set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node) # Mark the node as visited.
        for neighbour in graph[node]: # Recursively call DFS for each unvisited neighbour.
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A') # Start the DFS traversal from node 'A'.
