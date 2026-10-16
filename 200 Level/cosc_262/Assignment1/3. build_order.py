from adj import adjacency_list # Will need to put in adj_list on learn
from collections import deque
import heapq
def adjacency_list(s):

    graph = s.splitlines()
    header = graph[0].split()
    directed = header[0] == 'D'
    vertex = int(header[1])
    weighted = len(header) == 3
    ls = [[] for i in range(vertex)]
    for i in graph[1:]:
        part = i.split()
        v1 = int(part[0])
        v2 = int(part[1])
        if weighted:
            w = int(part[2])
            ls[v1].append((v2, w))
            if not directed:
                ls[v2].append((v1, w))
        else:
            ls[v1].append((v2, None))
            if not directed:
                ls[v2].append((v1, None))
    return ls


def is_acyclic(adj_list):

    """
        KEY NOTES:
            Uses DFS with a 3-colour system to detect cycles in a directed graph.
            Each vertex gets a STATE:
                None  → unvisited (never touched)
                1     → discovered (currently in the DFS call stack / being explored)
                2     → processed (fully done, all descendants explored)

            If we visit a neighbour that is currently in state 1 (still on the call stack),
            we've found a BACK EDGE → there is a cycle → graph is NOT acyclic.

            Think of it like: if we're still exploring A and we loop back to A → cycle!
    """

    state = {}  # state[v] = None (unseen), 1 (in progress), 2 (done)

    def dfs(v):
        state[v] = 1   # Mark as "currently being explored"
        print(f"    DFS visiting vertex {v} (state → 1: in progress)")

        for neighbour, weight in adj_list[v]:
            if state.get(neighbour) == 1:
                print(f"    !! Back edge found: {v} → {neighbour}. CYCLE DETECTED!")
                return False    # Neighbour is on the current call stack = CYCLE

            if state.get(neighbour) is None:    # Neighbour is unvisited
                if not dfs(neighbour):          # Recurse — if cycle found below, bubble up
                    return False

        state[v] = 2   # Mark as "fully processed"
        print(f"    DFS finished vertex {v} (state → 2: processed)")
        return True     # No cycle found from this vertex

    for vertex in range(len(adj_list)):
        if state.get(vertex) is None:   # Only start DFS from unvisited nodes
            print(f"  Starting DFS from vertex {vertex}")
            if not dfs(vertex):
                return False    # Cycle found somewhere in this component

    return True     # All vertices processed with no cycle found


def build_order(dependencies):

    """
        KEY NOTES:
            Produces a valid build order using Kahn's Algorithm (BFS-based topological sort).
            "Build order" = an order to process all tasks so every dependency comes BEFORE
            the task that depends on it.

            If any CYCLE exists: return None (impossible — circular dependency!)
            Otherwise, always pick the LOWEST-numbered available task next (min-heap).

            Step 1: Check for cycles
                Run is_acyclic() first. If there's a cycle → return None immediately.

            Step 2: Compute in-degrees
                in-degree[v] = number of tasks that MUST come before v.
                A task is "ready" when its in-degree reaches 0 (all prereqs done).

            Step 3: Seed the heap
                Start by pushing all tasks with in-degree 0 into a min-heap.
                Min-heap ensures we always pick the smallest-numbered ready task.

            Step 4: Process
                Pop smallest task from heap → add to order → reduce in-degree of its neighbours.
                If a neighbour's in-degree hits 0 → it's now ready → push to heap.

            Step 5: Validate
                If order contains all n tasks → valid topological order → return it.
                Otherwise → cycle exists (shouldn't happen after Step 1 check) → return None.
    """

    adjlist = adjacency_list(dependencies)
    n = len(adjlist)

    print(f"Graph has {n} tasks")
    print(f"Adjacency list: {adjlist}\n")

    # -- Step 1: Cycle check ---------------------------------------------------
    print("Step 1: Checking for cycles...")
    if not is_acyclic(adjlist):
        print("  Cycle detected! No valid build order possible.\n")
        return None     # Circular dependency → impossible to build
    print("  No cycles found! Continuing...\n")

    # -- Step 2: Compute in-degrees --------------------------------------------
    ind = [0] * n   # ind[v] = how many tasks must be completed before v
    for current in range(n):
        for neighbour, _ in adjlist[current]:
            ind[neighbour] += 1     # current → neighbour means neighbour has one more prereq
    print(f"Step 2: In-degrees = {ind}\n")

    # -- Step 3: Seed the heap with all tasks that have no prerequisites -------
    heap = [current for current in range(n) if ind[current] == 0]
    heapq.heapify(heap)     # Turn the list into a proper min-heap in O(n)
    print(f"Step 3: Starting tasks (in-degree 0): {heap}\n")

    # -- Step 4: Process tasks in order ---------------------------------------
    order = []
    while heap:
        current = heapq.heappop(heap)   # Always pick the LOWEST-numbered ready task
        order.append(current)
        print(f"Step 4: Processing task {current}, order so far: {order}")

        for neighbour, _ in adjlist[current]:
            ind[neighbour] -= 1     # One more prereq of neighbour is now done
            if ind[neighbour] == 0:
                heapq.heappush(heap, neighbour)  # Neighbour is now ready!
                print(f"    Task {neighbour} is now ready (in-degree reached 0)")

    # -- Step 5: Validate ------------------------------------------------------
    print(f"\nFinal order: {order}")
    return order if len(order) == n else None
    # If not all tasks made it in → there was a cycle we didn't catch → return None


# -- Test Cases ----------------------------------------------------------------

dependencies = """\
D 2
0 1
"""
print(build_order(dependencies))
# Expected: [0, 1]  →  must do 0 before 1

dependencies = """\
D 3
1 2
0 2
"""
print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])
# Expected: True  →  either [0,1,2] or [1,0,2] are valid (but we pick lowest = [0,1,2])

dependencies = """\
D 3
"""
# No edges → any order is valid, but we pick [0, 1, 2] (sorted by number)
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
# Expected: [0, 1, 2]

dependencies = """\
D 3
0 1
1 2
2 0
"""
print(build_order(dependencies))
# Expected: None  →  0→1→2→0 is a cycle, no valid build order exists
