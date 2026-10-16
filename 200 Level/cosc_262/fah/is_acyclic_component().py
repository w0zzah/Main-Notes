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

def is_acyclic_component(adj_list, vertex):
    state = {}

    def dfs(v):
        state[v] = 1  # discovered

        for neighbour, weight in adj_list[v]:  # unpack the tuple
            if state.get(neighbour) == 1:
                return False
            if state.get(neighbour) is None:
                if not dfs(neighbour):
                    return False

        state[v] = 2  # processed
        return True

    return dfs(vertex)
    
def is_acyclic(adj_list):
    state = {}

    def dfs(v):
        state[v] = 1  # discovered

        for neighbour, weight in adj_list[v]:
            if state.get(neighbour) == 1:
                return False
            if state.get(neighbour) is None:
                if not dfs(neighbour):
                    return False

        state[v] = 2  # processed
        return True

    for vertex in range(len(adj_list)):
        if state.get(vertex) is None:  # only start DFS from unvisited nodes
            if not dfs(vertex):
                return False

    return True

    return dfs(vertex)

acyclic_graph = [
    [(1,None), (2,None)],
    [(2,None)],
    []
]
print(is_acyclic_component(acyclic_graph, 0))