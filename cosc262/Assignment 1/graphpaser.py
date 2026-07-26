from collections import deque

# ─────────────────────────────────────────
# SHARED GRAPH PARSER  (used by all questions)
# ─────────────────────────────────────────

def adjacency_list(graph_str):
    """
    Parse the textual graph representation into an adjacency list.
    Returns (num_vertices, adjacency_list, is_directed, is_weighted)
    """
    lines = graph_str.strip().split('\n')
    # strip() removes leading/trailing whitespace from the whole string
    # split('\n') breaks it into a list of lines

    header = lines[0].split()
    # lines[0] is the first line, e.g. "D 5" or "U 4 W"
    # .split() splits on any whitespace into a list like ['D', '5'] or ['U', '4', 'W']

    direction = header[0]          # 'D' for directed, 'U' for undirected
    is_directed = (direction == 'D')
    is_weighted = (len(header) == 3 and header[2] == 'W')
    # len(header) == 3 means there are 3 tokens on the header line
    # header[2] == 'W' checks if the third token is 'W' (weighted)

    n = int(header[1])
    # header[1] is the vertex count as a string, e.g. '5'; int() converts it

    adj = [[] for _ in range(n)]
    # Create a list of n empty lists — one per vertex
    # adj[i] will hold the neighbours of vertex i

    for line in lines[1:]:
        # lines[1:] skips the header and iterates over edge lines
        line = line.strip()
        if not line:
            continue        # skip blank lines (e.g. trailing newline)
        parts = line.split()
        u = int(parts[0])   # source vertex
        v = int(parts[1])   # destination vertex

        if is_weighted:
            w = int(parts[2])       # edge weight (only present if 'W' in header)
            adj[u].append((v, w))   # store (neighbour, weight) tuple
            if not is_directed:
                adj[v].append((u, w))   # undirected: add reverse edge too
        else:
            adj[u].append(v)        # store just the neighbour
            if not is_directed:
                adj[v].append(u)    # undirected: add reverse edge too

    return n, adj, is_directed, is_weighted