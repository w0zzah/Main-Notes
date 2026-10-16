def format_sequence(converters_info, source_format, destination_format):
    """
    Find the shortest sequence of formats to convert source → destination.
    Uses BFS because every edge has equal cost (1 conversion).
    Returns a list of vertex numbers, or None if unreachable.
    """
    n, adj, _, _ = read_graph(converters_info)
    # Unpack only n and adj; we don't need the directed/weighted flags here
    # (we trust the graph is directed, as per the problem)

    # Edge case: source and destination are the same — no conversion needed
    if source_format == destination_format:
        return [source_format]
    # e.g. format_sequence("D 2\n0 1\n", 1, 1) → [1]

    # BFS setup
    visited = [False] * n
    # visited[i] = True once we've seen vertex i (prevents revisiting)

    parent = [-1] * n
    # parent[i] stores which vertex we came FROM to reach vertex i
    # This lets us reconstruct the path backwards at the end

    queue = deque()
    # A deque (double-ended queue) is used so we can append on the right
    # and pop from the left in O(1) — essential for efficient BFS

    queue.append(source_format)
    visited[source_format] = True
    # Mark the starting vertex as visited immediately so it's not added again

    found = False   # will flip to True when we reach destination_format

    while queue:
        # Keep going while there are vertices still to process
        current = queue.popleft()
        # popleft() takes from the FRONT of the queue (FIFO order)
        # This is what makes BFS explore level-by-level (nearest nodes first)

        for neighbour in adj[current]:
            # Iterate over all direct neighbours of current vertex
            # adj[current] is the list we built during parsing

            if not visited[neighbour]:
                # Only process unvisited neighbours to avoid cycles/redundancy
                visited[neighbour] = True
                parent[neighbour] = current
                # Record: "we reached `neighbour` by coming from `current`"

                if neighbour == destination_format:
                    found = True
                    break   # Stop as soon as we hit the destination
                queue.append(neighbour)
                # Add unvisited neighbour to the back of the queue
                # It will be processed after all closer vertices

        if found:
            break   # Also break out of the outer while loop

    if not found:
        return None
        # destination is unreachable from source

    # Reconstruct path by walking backwards through parent[]
    path = []
    node = destination_format
    while node != -1:
        # Walk: destination → ... → source, following parent pointers
        # source's parent is -1 (we never set it), so the loop stops there
        path.append(node)
        node = parent[node]

    path.reverse()
    # We built the path backwards (destination first), so reverse it
    return path
    # Returns e.g. [1, 0, 2] meaning: convert 1→0 then 0→2