import heapq  # Python's built-in min-heap (priority queue)
def adjacency_list(graph_str):
    lines = graph_str.strip().split('\n')
    header = lines[0].split()
    direction = header[0]
    is_directed = (direction == 'D')
    is_weighted = (len(header) == 3 and header[2] == 'W')
    n = int(header[1])

    adj = [[] for _ in range(n)]

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        u = int(parts[0])
        v = int(parts[1])

        if is_weighted:
            w = int(parts[2])
            adj[u].append((v, w))
            if not is_directed:
                adj[v].append((u, w))
        else:
            adj[u].append(v)
            if not is_directed:
                adj[v].append(u)
    return n, adj


def which_segments(city_map):
    """
    Find the minimum spanning tree — the smallest set of road segments
    that connects every location while minimising total road length.
    Uses Prim's algorithm with a min-heap (priority queue).
    """
    n, adj = adjacency_list(city_map)

    if n == 1:
        return []
        # Only one location — no roads needed to "connect" it to itself

    in_mst = [False] * n
    # in_mst[i] = True once location i has been added to the MST

    # Min-heap entries are: (edge_weight, from_vertex, to_vertex)
    # heapq always gives us the smallest weight entry first
    heap = []

    result = []
    # Will hold the chosen road segments as (smaller_vertex, larger_vertex) tuples

    # Start from vertex 0 (arbitrary; the MST is the same regardless of start)
    in_mst[0] = True

    for (neighbour, weight) in adj[0]:
        # Push all edges from vertex 0 into the heap to consider them
        heapq.heappush(heap, (weight, 0, neighbour))
        # heappush maintains the heap property (smallest weight at top)

    while heap:
        weight, u, v = heapq.heappop(heap)
        # heappop removes and returns the SMALLEST weight edge
        # u = vertex already in MST, v = vertex we might be adding

        if in_mst[v]:
            continue
            # v is already in the MST — adding this edge would create a cycle
            # Skip it and look at the next cheapest edge

        # This edge is the cheapest way to connect v to the MST
        in_mst[v] = True
        edge = (min(u, v), max(u, v))
        # Store with smaller vertex first, as required by the problem
        result.append(edge)

        for (neighbour, w) in adj[v]:
            if not in_mst[neighbour]:
                heapq.heappush(heap, (w, v, neighbour))
                # Add all edges from v to non-MST vertices for future consideration

    return result

city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))