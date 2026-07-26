from adj import adjacency_list # Will need to put in adj_list on learn
from collections import deque


def bubbles(physical_contact_info):

    """
        KEY NOTES:
            This function finds all connected components (bubbles) in an UNDIRECTED graph.
            A "bubble" = a group of people who can reach each other directly or indirectly.
            We use BFS, starting from every unvisited vertex.

            Step 1: Base Case
                Is the graph empty? If so, return [] — no people, no bubbles.

            Step 2: Initialise
                visited[]   → tracks which people have already been placed in a bubble
                result      → the final list of bubbles, each bubble is its own list

            Step 3: Outer loop
                Try every vertex as a potential start of a NEW bubble.
                If already visited: skip it — it was caught by a previous BFS.

            Step 4: Inner BFS
                From the starting vertex, flood-fill outward through all contacts.
                Everyone reachable in this flood = same bubble.

            Step 5: Save bubble
                Append the fully-discovered bubble to result, then move on.
    """

    adj_list = adjacency_list(physical_contact_info)
    n = len(adj_list)

    visited = [False] * n   # visited[i] = True once person i is assigned to a bubble
    result = []             # Will hold all discovered bubbles e.g. [[0, 1], [2, 3, 4]]

    print(f"Graph has {n} people (vertices)")
    print(f"Adjacency list: {adj_list}\n")

    for start in range(n):  # Try every vertex as a possible bubble starting point

        if visited[start]:
            print(f"  Person {start} already in a bubble, skipping!")
            continue        # Already assigned — skip

        print(f"Starting new bubble from person {start}")
        bubble = []
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.popleft()   # take from the FRONT 
            bubble.append(current)
            print(f"    Visiting person {current}, bubble so far: {bubble}")

            for neighbour, _ in adj_list[current]:  # check all direct contacts
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)         # Spread through contact chain
                    print(f"        Adding person {neighbour} to queue")

        print(f"  Bubble complete: {bubble}\n")
        result.append(bubble)   # bubble fully discovered, save it

    print(f"All bubbles found: {result}")
    return result


# -- Test Cases ----------------------------------------------------------------

physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# Expected: [[0, 1]]  →  0 and 1 are in contact, so same bubble
