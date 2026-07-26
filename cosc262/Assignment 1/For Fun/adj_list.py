from collections import deque

# adjacency list reexplained 


def adjacency_list(graph_str):

    """
        KEY NOTES:
            Parses a textual graph description into an adjacency list we can work with.
            Returns: (num_vertices, adjacency_list, is_directed, is_weighted)

            Input format examples:
                "D 5"       →  directed, 5 vertices, unweighted
                "U 4 W"     →  undirected, 4 vertices, weighted
                "0 1"       →  edge from vertex 0 to vertex 1 (unweighted)
                "0 1 7"     →  edge from 0 to 1 with weight 7

            Step 1: Parse header
                First line tells us: direction (D/U), vertex count, and if weighted (W).

            Step 2: Build adjacency list
                adj[i] = list of neighbours reachable from vertex i.
                Unweighted: adj[u] stores just v  (the neighbour)
                Weighted:   adj[u] stores (v, w)  (neighbour, weight) tuples

            Step 3: Handle undirected edges
                If undirected: every edge u→v also adds v→u (both directions).
                If directed:   only add u→v (one way).
    """

    lines = graph_str.strip().split('\n')
    # strip() removes leading/trailing whitespace from the whole string
    # split('\n') breaks it into a list of individual lines
    print(f"Parsing graph string, {len(lines)} lines total")

    # ── Step 1: Parse the header ──────────────────────────────────────────────
    header = lines[0].split()
    # lines[0] = first line e.g. "D 5" or "U 4 W"
    # .split() on whitespace → ['D', '5'] or ['U', '4', 'W']

    direction   = header[0]                         # 'D' (directed) or 'U' (undirected)
    is_directed = (direction == 'D')
    is_weighted = (len(header) == 3 and header[2] == 'W')
    # len == 3 means 3 tokens on the header line (direction, count, 'W')
    # header[2] == 'W' confirms the third token is the weighted flag

    n = int(header[1])  # Number of vertices, e.g. '5' → 5

    print(f"  Direction: {'Directed' if is_directed else 'Undirected'}")
    print(f"  Vertices:  {n}")
    print(f"  Weighted:  {is_weighted}")

    # ── Step 2: Build adjacency list ──────────────────────────────────────────
    adj = [[] for _ in range(n)]
    # Create n empty lists — one per vertex
    # adj[i] will hold all neighbours of vertex i

    for line in lines[1:]:  # Skip the header, process edge lines
        line = line.strip()
        if not line:
            continue        # Skip blank lines (e.g. trailing newline at end of string)

        parts = line.split()
        u = int(parts[0])   # Source vertex
        v = int(parts[1])   # Destination vertex

        # ── Step 3: Add edges (direction-aware) ──────────────────────────────
        if is_weighted:
            w = int(parts[2])       # Edge weight (only present if 'W' in header)
            adj[u].append((v, w))   # Store (neighbour, weight) tuple
            print(f"  Weighted edge: {u} → {v}  (weight {w})")
            if not is_directed:
                adj[v].append((u, w))   # Undirected: add reverse edge too
                print(f"  Weighted edge: {v} → {u}  (weight {w})  [reverse]")
        else:
            adj[u].append(v)        # Store just the neighbour (no weight)
            print(f"  Edge: {u} → {v}")
            if not is_directed:
                adj[v].append(u)    # Undirected: add reverse edge too
                print(f"  Edge: {v} → {u}  [reverse]")

    print(f"  Adjacency list built: {adj}\n")
    return n, adj, is_directed, is_weighted
    # Returns all 4 values — callers can unpack only what they need:
    # e.g. n, adj, _, _ = adjacency_list(s)   ← discard directed/weighted flags
