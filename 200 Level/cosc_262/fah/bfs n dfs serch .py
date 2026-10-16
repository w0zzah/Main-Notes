from collections import deque
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

def bfs_tree(adj_list, start):
    """    
    adj_list: list of lists where each element is (neighbour, weight)
    start: starting vertex (integer)
    
    Returns:
        parent: list where parent[Neighbor] is the parent of Neighbor in BFS tree, None if no parent
    """
    n = len(adj_list)
    parent = [None] * n          # Initialize all parents as None
    visited = [False] * n        # Track visited vertices
    queue = deque()              # BFS queue
    
    # Start BFS
    visited[start] = True
    parent[start] = None
    queue.append(start)
    
    while queue:
        Current = queue.popleft()
        for Neighbor, _ in adj_list[Current]:   # ignore weights
            if not visited[Neighbor]:
                visited[Neighbor] = True
                parent[Neighbor] = Current
                queue.append(Neighbor)
    
    return parent


def dfs_tree(adj_list, start):
    """    
    adj_list: list of lists where each element is (neighbour, weight)
    start: starting vertex (integer)
    
    Returns:
        parent: list where parent[Neighbor] is the parent of Neighbor in BFS tree, None if no parent
    """
    n = len(adj_list)
    parent = [None] * n        # Initialize all parents as None
    visited = [False] * n      # Track visited vertices

    def dfs(Current):
        e = 0
        visited[Current] = True
        for Neighbor, weight in adj_list[Current]:
            e += 1
            print(f"Current: {Current} ------ Neighbor: {Neighbor} {e}")
            if not visited[Neighbor]:
                parent[Neighbor] = Current
                dfs(Neighbor)

    dfs(start)
    return parent
# a directed graph (note the asymmetrical adjacency list)


adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 2))