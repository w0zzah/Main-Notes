def adjacency_list(graph_str):
    #split up the string based of of \n (every new line is turned into its own string in the list)
    lines = graph_str.splitlines()
    #Take the top line off
    header = lines[0].split()
    directed = header[0] == 'D'
    weighted = 'W' in header
    n = int(header[1])
    #sets up an empty lis for the data to be put in
    adj = [[] for i in range(n)]
    #go through each line and arrange
    for line in lines[1:]:
        parts = line.split()
        if not parts:
            continue
        vertex1 = int(parts[0])
        vertex2 = int(parts[1])
        weight = int(parts[2]) if weighted else None

        adj[vertex1].append((vertex2, weight))

        if not directed:
            adj[vertex2].append((vertex1, weight))
    return adj


def initial_distance_matrix(adj_list):

    # Count all nodes in the adj_list
    totalNodes = len(adj_list)

    # Initialise the matrix with a [inf] * totalNodes for every single node "For every node, make a list of inf that contains enough for every node"
    matrix = [[float('inf')] * totalNodes for _ in range(totalNodes)]    
    
    # Setup a loop that goes through every single node
    for currentNode in range(totalNodes):

        # Set the distance for current node to itself = 0
        matrix[currentNode][currentNode] = 0

        # The path and weight from a node is stored as a tuple e.g "[[(1, 5)], [], [(1, 7)]]" where the index equals current node,
        # and the tuples in side contain all of the possible paths. (in e.g, Node 0 has a path to node 1 with weight 5)

        # We loop through each of these connections and set the distance from current node to JUST the "1 path" connected nodes 
        # (1-2-3-4, if this was the diagram and we are looking at node 2, we would only look at the weights of 3 and 4)
        for neighbor, weight in adj_list[currentNode]:

            # if weight is None then all weights should be equal
            w = weight if weight is not None else 1
            matrix[currentNode][neighbor] = w
    return matrix


# Code goes through and checks if A - > B -> C is easier than A -> C
def floyd(matrix):

    dist = copy.deepcopy(matrix)
    n = len(dist)
    # Middle Node 
    for B in range(n):
        # Source Node
        for A in range(n):
            # Destination Node 
            for C in range(n):
                
                # If the distance from i -> j -> k is less than i -> k :
                # Then replace the path from i -> j (default) to i -> j -> k
                if dist[A][B] + dist[B][C] < dist[A][C]:
                    dist[A][C] = dist[A][B] + dist[B][C]
    # After checking all nodes set the easiest path as the bridging path
    return dist

import copy
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_list = adjacency_list(graph_str)
dist_matrix = initial_distance_matrix(adj_list)
print("Initial distance matrix:", dist_matrix)
dist_matrix = floyd(dist_matrix)
print("Shortest path distances:", dist_matrix)