def is_acyclic(graph):
    # Create a new dictionary to hold the state of the algorithim
    state = {}

    def rec(v):
        # Set the current nodes state to 1
        state[v] = 1
        for neighbor, _ in graph[v]:
            if state.get(neighbor) == 1:
                return False
            if state.get(neighbor) is None:
                if not rec(neighbor):
                    return False
        state[v] = 2
        return True
    i = 0
    n = len(graph)
    while i < n:
        if rec(i) is False:
            return False
        else:
            i += 1
    return True

cyclic_graph = [
    [(1,None)],
    [(2,None)],
    [(0,None)]
]

print(is_acyclic(cyclic_graph))