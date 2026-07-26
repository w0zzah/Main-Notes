def is_acyclic_component(adj_list, vertex):
    
    n = len(adj_list)
    on_stack = [False] * n
    visited = [False] * n

    def dfs(current_node):
        visited[current_node] = True
        on_stack[current_node] = True
        for neighbor, weight in adj_list[current_node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            elif on_stack[neighbor]:
                return False
        on_stack[current_node] = False
        return True


    return dfs(vertex)

        

cyclic_graph = [
    [(1,None)],
    [(2,None)],
    [(0,None)]
]

print(is_acyclic_component(cyclic_graph, 0))