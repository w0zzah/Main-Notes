def bubbles(physical_contact_info):
    """
    Find all connected components (bubbles) in an undirected graph.
    Each person who can reach each other (directly or indirectly) is
    in the same bubble. Uses BFS from every unvisited vertex.
    """
    n, adj, _, _ = read_graph(physical_contact_info)

    if n == 0:
        return []
        # Edge case: empty graph — no people, no bubbles

    visited = [False] * n
    # visited[i] = True once person i has been assigned to a bubble

    result = []
    # Will hold a list of sets (or lists), one per bubble

    for start in range(n):
        # Try every vertex as a potential starting point
        # If it's already visited, it belongs to an earlier bubble — skip it

        if visited[start]:
            continue    # Already in a bubble found earlier

        # Start a new bubble from this unvisited vertex
        bubble = []         # Accumulate all members of this bubble
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.popleft()
            bubble.append(current)
            # Add this person to the current bubble

            for neighbour in adj[current]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
                    # Spread through all direct contacts
                    # BFS ensures everyone reachable is included

        result.append(bubble)
        # One bubble fully discovered; add it to the result list

    return result
    # Returns e.g. [[0], [1, 2, 3, 4, 5, 6]]