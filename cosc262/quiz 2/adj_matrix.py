def adjacency_matrix(graph_str):
    
    """    The returned adjacency matrix must be a list of lists. The length of the outer list and the length of all the inner lists are equal to the number of vertices. 
        For unweighted graphs the returned matrix should only include numbers 0 or 1. For weighed graphs, use None when there is no edge and numbers for weights."""
    
    graph = graph_str.splitlines()
    header = graph[0].split()
    if header[0] == 'D':
        directed = True
    else: directed = False
    vert = int(header[1])
    weighted = 'W' in header
    
    if weighted:
        adj = [[(None)for i in range(vert)] for i in range(vert)]
    else: adj = [[0 for i in range(vert)] for i in range(vert)]

    for line in graph[1:]:
        part = line.split()
        v1 = int(part[0])
        v2 = int(part[1])
        if weighted:
            w = int(part[2])
            adj[v1][v2] = w
            if not directed: 
                adj[v2][v1] = w
        else:
            adj[v1][v2] = 1
            if not directed: adj[v2][v1] = 1
    return adj



graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_matrix(graph_string))