from adj import adjacency_list # Will need to put in adj_list on learn
from collections import deque

def format_sequence(converters_info, source_format, destination_format):

    """
        KEY NOTES:
            Stripped-down BFS to find the shortest conversion path from source → destination.
            Stores FULL PATHS in the queue (simpler than parent[] reconstruction, uses more memory).
            Returns a list of format IDs, or None if unreachable.

            Step 1: Base Case
                Already at destination? Return [source_format] immediately.

            Step 2: Initialise
                queue   → deque of paths, seeded with [[source_format]]
                          Each entry IS a full path (not just a vertex)
                visited → prevents re-exploring the same format twice

            Step 3: BFS
                Pop the leftmost path from queue (FIFO = shortest path found first).
                For each neighbour of the path's current endpoint:
                    Is it the destination? → return path + [neighbour] immediately (done!)
                    Not yet visited?       → extend the path and add to queue for later

            Why store full paths instead of parent[]?
                Simpler code, but uses more memory.
                For large graphs, parent[] reconstruction (see format_sequance.py) is better.
    """

    adjlist = adjacency_list(converters_info)
    print(f"Adjacency list: {adjlist}")
    print(f"Converting from {source_format} → {destination_format}\n")

    # ── Step 1: Base Case ─────────────────────────────────────────────────────
    if source_format == destination_format:
        print("Already at destination!")
        return [source_format]

    # ── Step 2: Initialise ────────────────────────────────────────────────────
    queue   = deque([[source_format]])  # Each entry is a FULL PATH (list of format IDs)
    visited = [False] * len(adjlist)    # visited[i] prevents reprocessing format i
    # Note: we don't mark source as visited here — it's the start,
    # but we don't want to block returning through it in edge cases

    # ── Step 3: BFS ───────────────────────────────────────────────────────────
    while queue:
        path    = queue.popleft()   # Take the oldest (shortest) path from the front
        current = path[-1]          # The last format in the path = where we are now
        print(f"Current path: {path}  (sitting at format {current})")

        for neighbour, _ in adjlist[current]:   # Try all conversions from current format
            # Example: mp3 → mp4 → mp5
            #          On first loop: current=mp3, neighbour=mp4
            #          On second loop: current=mp4, neighbour=mp5 → FOUND!

            if neighbour == destination_format:
                print(f"    Destination {destination_format} found! Returning path.")
                return path + [neighbour]       # We made it — return the completed path

            if not visited[neighbour]:          # Only explore formats we haven't seen
                visited[neighbour] = True       # Mark as visited before adding to queue
                queue.append(path + [neighbour])    # Extend this path and enqueue it
                print(f"    Queuing path to {neighbour}: {path + [neighbour]}")

        print(f"  All paths in queue: {list(queue)}\n")

    print("No path found!")
    return None     # Destination is unreachable from source


