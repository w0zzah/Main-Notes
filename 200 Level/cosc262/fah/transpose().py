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

def transpose(adj_list):
    n = len(adj_list)
    nl = [[] for i in range(n)]
    for vertex in range(n):
        edges = adj_list[vertex]
        for edge in edges:
            dest = edge[0]
            w = edge[1]
            nl[dest].append((vertex, w))
    return nl

def bfs(adj_list, start = 0):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for neighbor, i in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def is_strongly_connected(adj_list):
    n = len(adj_list)
    if not n:
        return True
    if bfs(adj_list) !=set(range(n)):
        return False
    
    if bfs(transpose(adj_list)) != set(range(n)):
        return False
    return True

graph_string = """\
D 3
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))
