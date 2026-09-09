from adj import adjacency_list # Will need to put in adj_list on learn
import heapq

def which_segments(city_map):

    """
        KEY NOTES:
            Find the MINIMUM SPANNING TREE (MST) — the smallest set of road segments
            that connects every location while minimising total road length.
            Uses PRIM'S ALGORITHM with a min-heap (priority queue).

            Think of it like: building a road network as cheaply as possible.
            At each step, we always add the CHEAPEST road that connects a new location.

            Step 1: Base Case
                Only 1 location? No roads needed — return [].

            Step 2: Initialise
                in_mst[] → tracks which locations are already in our road network
                heap     → min-heap of candidate edges: (weight, from, to)
                result   → the road segments we've chosen for the MST

            Step 3: Seed
                Start from vertex 0 (arbitrary — MST is the same regardless of start).
                Push all edges from vertex 0 into the heap as initial candidates.

            Step 4: Prim's main loop
                Always pick the CHEAPEST candidate edge (heappop = smallest weight).
                Is the destination already in the MST? Skip it (would create a cycle).
                Otherwise: add it to the MST, then push all its outgoing edges as new candidates.

            Step 5: Return road segments
                Each segment stored as (smaller_vertex, larger_vertex) for consistency.
    """

    adj = adjacency_list(city_map)
    n = len(adj)
    
    print(f"Graph has {n} locations")
    print(f"Adjacency list: {adj}\n")

    # -- Step 1: Base Case -----------------------------------------------------
    if n == 1:
        print("Only 1 location — no roads needed!")
        return []   # Can't have roads between 1 point

    # -- Step 2: Initialise ----------------------------------------------------
    in_mst = [False] * n    # in_mst[i] = True once location i is part of our network
    heap   = []             # Min-heap: (edge_weight, from_vertex, to_vertex)
    result = []             # Final list of chosen road segments

    # -- Step 3: Seed the heap from vertex 0 ----------------------------------
    in_mst[0] = True        # Start from vertex 0 (arbitrary choice)
    print("Step 3: Seeding heap from vertex 0...")

    for (neighbour, weight) in adj[0]:
        heapq.heappush(heap, (weight, 0, neighbour))
        # heappush maintains heap property — smallest weight always at the top
        print(f"  Candidate road: 0 → {neighbour}  (length {weight})")

    # -- Step 4: Prim's main loop ----------------------------------------------
    print("\nStep 4: Building MST with Prim's algorithm...")

    while heap:
        weight, u, v = heapq.heappop(heap)
        # heappop removes and returns the CHEAPEST available candidate road
        # u = location already in network, v = location we might be connecting

        print(f"  Checking cheapest candidate: {u} → {v}  (length {weight})")

        if in_mst[v]:
            print(f"    Location {v} already in MST, skipping! (would create a cycle)")
            continue
            # v is already connected — adding this road would create a loop
            # Prim's: we only ever add a vertex to the MST ONCE

        # -- This is the cheapest road to connect v to our existing network ----
        in_mst[v] = True
        edge = (min(u, v), max(u, v))   # Store with smaller vertex first (consistent format)
        result.append(edge)
        print(f"    Adding road: {edge}  (cheapest connection to location {v})")
        print(f"    MST so far: {result}")

        for (neighbour, w) in adj[v]:   # Push all new candidate roads from v
            if not in_mst[neighbour]:
                heapq.heappush(heap, (w, v, neighbour))
                print(f"    New candidate from {v}: {v} → {neighbour}  (length {w})")

    print(f"\nFinal MST segments: {result}")
    return result
    # Returns e.g. [(0, 1), (1, 2)] — the road segments that form the minimum spanning tree


# -- Test Cases ----------------------------------------------------------------

city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))
# Expected: [(0, 1), (1, 2)]
# 0-1 costs 1, 1-2 costs 2 → total 3 (cheaper than using 0-2 which costs 4)
