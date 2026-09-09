from adj import adjacency_list # Will need to put in adj_list on learn
import heapq

def min_capacity(city_map, depot_position):

    """
        KEY NOTES:
            Find the MINIMUM battery capacity so a vehicle can make a round trip
            from the depot to ANY location and return with ≥25% charge remaining.

            Battery math (worked out once here so we don't redo it in the code):
                Travel rate:          2 units distance per 3 units battery
                Battery per distance: 3/2 units battery per unit distance
                Round trip distance:  2 × shortest_path_distance
                Battery used:         (3/2) × 2 × d  =  3d

                Must have 25% left →  used ≤ 75% of capacity:
                    3d ≤ 0.75 × capacity
                    capacity ≥ 3d / 0.75
                    capacity ≥ 4d          ← clean integer, no fractions needed!

            So: required_capacity = 4 × max_shortest_path_distance (pure integer!)

            Algorithm: Dijkstra's from depot_position to find shortest paths to all vertices.
            Then return 4 × the MAXIMUM of those shortest paths.

            Step 1: Initialise distances to ∞, depot to 0, push depot onto min-heap.
            Step 2: Dijkstra — always process the currently closest unvisited vertex.
            Step 3: Find maximum shortest path (worst-case round trip destination).
            Step 4: Return 4 × max distance (the minimum capacity that covers all trips).
    """

    adj = adjacency_list(city_map)
    n = len(adj)

    print(f"Graph has {n} locations")
    print(f"Depot is at position {depot_position}")
    print(f"Adjacency list: {adj}\n")

    # -- Step 1: Initialise ----------------------------------------------------
    dist = [float('inf')] * n
    # dist[i] = shortest known distance from depot_position to vertex i
    # Start with infinity = "not yet reached"

    dist[depot_position] = 0    # Distance from depot to itself is 0
    print(f"Step 1: Initial distances: {dist}")

    heap = [(0, depot_position)]
    # Min-heap: entries are (distance_so_far, vertex)
    # heapq always pops the smallest distance first — this is what makes it Dijkstra's

    # -- Step 2: Dijkstra ------------------------------------------------------
    print("\nStep 2: Running Dijkstra...")
    while heap:
        distance, current = heapq.heappop(heap)
        # distance we used to reach current; current = current vertex

        if distance > dist[current]:
            continue
            # This is a STALE heap entry — we already found a shorter path to current earlier.
            # Dijkstra can leave outdated entries in the heap; this check skips them.
            # Example: we push (5, 2) then find (3, 2) later — when we pop the old (5, 2),
            #          dist[2] is already 3, so 5 > 3 → skip it.

        print(f"  Processing vertex {current} at distance {distance}")

        for (neighor, w) in adj[current]:  # Look at all neighbours of current
            new_dist = dist[current] + w      # Tentative distance to neighor via current

            if new_dist < dist[neighor]:      # check if its the sortest path
                dist[neighor] = new_dist      # if so set it
                heapq.heappush(heap, (new_dist, neighor))
                # Add to heap so we explore neighor's neighbours with this improved distance
                print(f"    Updated dist[{neighor}] = {new_dist}  (via vertex {current})")

    print(f"\nFinal shortest distances from depot {depot_position}: {dist}")

    # -- Step 3: Find maximum shortest path -----------------------------------
    # We need capacity to handle the WORST CASE = the farthest reachable location
    max_dist = 0
    for i in range(n):
        if dist[i] != float('inf'):             # Only consider reachable locations
            if dist[i] > max_dist:
                max_dist = dist[i]
                print(f"Step 3: New max distance = {max_dist}  (vertex {i})")

    # -- Step 4: Calculate minimum capacity -----------------------------------
    capacity = 4 * max_dist
    print(f"\nStep 4: max_dist = {max_dist}, minimum capacity = 4 × {max_dist} = {capacity}")
    return capacity


# -- Test Cases ----------------------------------------------------------------

city_map = """\
current 4 W
0 2 5
0 3 2
3 2 1
"""

print(min_capacity(city_map, 0))   # Expected: 12  (farthest reachable = 3, capacity = 4×3)
print(min_capacity(city_map, 1))   # Expected: 0   (vertex 1 is isolated → only dest = itself)
print(min_capacity(city_map, 2))   # Expected: 12
print(min_capacity(city_map, 3))   # Expected: 12
