def adjacency_list(graph_str):
    lines = graph_str.splitlines()
    
    # ----- parse header -----
    header = lines[0].split()
    
    directed = header[0] == 'D'
    weighted = 'W' in header
    n = int(header[1])
    
    # create list of distinct empty lists
    adj = [[] for _ in range(n)]
    
    # ----- read edges -----
    for line in lines[1:]:
        parts = line.split()
        if not parts:          # skip blank lines
            continue
        
        u = int(parts[0])
        v = int(parts[1])
        w = int(parts[2]) if weighted else None
        
        adj[u].append((v, w))
        
        if not directed:
            adj[v].append((u, w))
    
    return adj


graph_string = """\
D 3
0 1
1 0
0 2
"""
print(adjacency_list(graph_string))