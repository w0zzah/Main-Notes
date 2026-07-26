def bubbles(s):

    """
        KEY NOTES:
            Finds all connected components (bubbles) in an undirected graph.
            Builds its own adjacency list inline (does not use a separate parser).
            Uses BFS from every unvisited vertex to discover each bubble.

            Step 1: Parse the header
                Get the vertex count, build the adjacency list from the edge lines.
                Since undirected: every edge u-v adds BOTH u→v and v→u.

            Step 2: Initialise
                visited (set) → tracks which vertices have been placed in a bubble
                result        → list of all completed bubbles

            Step 3: Outer Loop
                Try every vertex i as a potential new bubble start.
                If already in visited: skip — already claimed by an earlier BFS.

            Step 4: Inner BFS
                Flood-fill from vertex i. Every reachable vertex = same bubble.
                Use a plain list as queue (queue.pop(0) = FIFO = BFS).

            Step 5: Append the bubble to result.
    """

    graph = s.splitlines()
    header = graph[0].split()
    vertex = int(header[1])     # Total number of people/vertices
    print(f"Graph has {vertex} vertices")

    # ── Build adjacency list ──────────────────────────────────────────────────
    adj = [[] for _ in range(vertex)]  # adj[i] = list of people i is in contact with

    for line in graph[1:]:             # Skip the header line
        part = line.split()
        if not part:
            continue                   # Skip any blank lines
        v1, v2 = int(part[0]), int(part[1])
        adj[v1].append(v2)
        adj[v2].append(v1)             # Undirected: add both directions
        print(f"  Edge added: {v1} <--> {v2}")

    print(f"Adjacency list: {adj}\n")

    # ── BFS to find connected components ─────────────────────────────────────
    visited = set()     # set() gives O(1) membership checks (faster than a list for this)
    result = []         # Final list of all bubbles

    for i in range(vertex):    # Try every vertex as a potential new bubble start

        if i in visited:
            print(f"  Vertex {i} already visited, skipping!")
            continue            # Already in a bubble — skip

        # ── New bubble found! BFS from vertex i ──────────────────────────────
        print(f"Starting new bubble from vertex {i}")

        bubble = []
        queue = [i]             # Plain list used as a queue here (pop(0) = FIFO)

        while queue:
            current = queue.pop(0)  # Take from FRONT — this is what makes it BFS

            if current not in visited:  # Double-check (may have been added twice)
                visited.add(current)
                bubble.append(current)
                print(f"    Visiting {current}, bubble so far: {bubble}")

                for neighbour in adj[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)     # Spread to unvisited contacts
                        print(f"        Queueing neighbour {neighbour}")

        print(f"  Bubble complete: {bubble}\n")
        result.append(bubble)   # Save this bubble and move to the next unvisited vertex

    print(f"All bubbles: {result}")
    return result


# ── Test Cases ────────────────────────────────────────────────────────────────

physical_contact_info = """\
U 2
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: [[0], [1]]  →  no edges, each person is their own bubble

physical_contact_info = """\
U 2
0 1
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: [[0, 1]]  →  0 and 1 in contact = one shared bubble

physical_contact_info = """\
U 0
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: []  →  zero people = no bubbles

physical_contact_info = """\
U 1
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: [[0]]  →  one person with no contacts = one bubble of size 1

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: [[0], [1, 2, 3, 4, 5, 6]]
# 0 is isolated; everyone else is connected through the contact chain
