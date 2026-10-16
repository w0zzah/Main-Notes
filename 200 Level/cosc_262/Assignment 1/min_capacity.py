import heapq
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

def min_capacity(city_map, depot_position):
    """
    Find the minimum battery capacity so a vehicle can make a round trip
    from the depot to ANY location and return with ≥25% charge remaining.

    Key facts:
      - Travel rate: 2 units distance per 3 units battery
        → battery used per unit distance = 3/2
      - Round trip distance = 2 × shortest_path_distance
      - Battery used for round trip = 2 × distance × (3/2) = 3 × distance
      - Must have 25% left: used ≤ 75% of capacity
        → 3 × distance ≤ 0.75 × capacity
        → capacity ≥ 3 × distance / 0.75
        → capacity ≥ 4 × distance   (multiply both sides by 4/3)

    So: required capacity = 4 × max_shortest_path_distance (integer, no fractions!)
    """
    n, adj = adjacency_list(city_map)


    dist = [float('inf')] * n
    # dist[i] = shortest known distance from depot_position to vertex i
    # Start with infinity (unknown/unreachable)

    dist[depot_position] = 0
    # Distance from depot to itself is 0

    heap = [(0, depot_position)]
    # Min-heap: (distance_so_far, vertex)
    # We always process the currently closest unvisited vertex next

    while heap:
        d, u = heapq.heappop(heap)
        # d = distance we used to reach u; u = current vertex

        if d > dist[u]:
            continue
            # We already found a shorter path to u earlier.
            # This is a stale entry in the heap — skip it.
            # (Dijkstra can have duplicate heap entries; this check handles that)

        for (v, w) in adj[u]:
            # Consider each neighbour v reachable from u with edge weight w
            new_dist = dist[u] + w
            # Tentative shortest distance to v via u

            if new_dist < dist[v]:
                dist[v] = new_dist
                # Found a shorter path to v — update it
                heapq.heappush(heap, (new_dist, v))
                # Add to heap so we process v's neighbours with this new distance

    # ── Battery calculation ───────────────────────────────────────────
    # From the derivation above: required_capacity = 4 × distance
    # We need the capacity to handle the WORST CASE (farthest location)

    max_dist = 0
    for i in range(n):
        if dist[i] != float('inf'):
            # Only consider reachable vertices (problem guarantees connectivity)
            if dist[i] > max_dist:
                max_dist = dist[i]
                # Track the maximum shortest-path distance

    capacity = 4 * max_dist
    # 4 × max_dist is pure integer arithmetic — no floating point needed!
    # Derivation: capacity ≥ (3 × 2 × max_dist) / 0.75
    #           = 6 × max_dist / (3/4)
    #           = 6 × max_dist × (4/3)
    #           = 8 × max_dist / 2... let's redo cleanly:
    # used_battery = (3/2) × 2 × max_dist = 3 × max_dist
    # 3 × max_dist ≤ 0.75 × capacity  →  capacity ≥ 3×max_dist/0.75 = 4×max_dist ✓

    return capacity


city_map = """\
U 4 W
0 2 5
0 3 2
3 2 1
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))