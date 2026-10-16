def dfs_tree(adj_list, start):
    """
        Create a single list with each index corresponding to index's parent

        Step 1 : Initialise
            i, Set n = len list
            ii, Initialise parent array
            iii, Initialise Visited array
        
        Step 2: Sort:
            i, Setup recurssive func dfs('Current')
            ii, Set 'Current' as visited
            iii, Iterate through the list for neighbor, weight in list at current index
            iv, If visited at index neighbor is false
            v,      Parent at index neighbor = Current
                    Run with neighbor
            return parents

    """

    n = len(adj_list)
    parents = [None] * n
    visited = [False] * n
    
    def dfs(current_node):
        visited[current_node] = True
        for neighbor, weight in adj_list[current_node]: # question, when it get here but neighbor and weight don't exist?
            if not visited[neighbor]:
                parents[neighbor] = current_node
                dfs(neighbor)

    dfs(start)
    return parents

def is_acyclic_component(adj_list, start):
    """
    Returns True if no cycle is found from start, False if a cycle exists.
    Key idea: if we visit a neighbor that is already visited AND
    is not the direct parent of the current node, a cycle exists.
    """

    n = len(adj_list)
    visited = [False] * n
    parents = [None] * n

    def dfs(current_node):
        visited[current_node] = True
        for neighbor, weight in adj_list[current_node]:
            if not visited[neighbor]:
                parents[neighbor] = current_node
                if not dfs(neighbor):
                    return False
            elif parents[current_node] != neighbor:
                return False
        return True

    return dfs(start)

    dfs(start)


def is_acyclic_component(adj_list, start):
    n = len(adj_list)
    on_stack = [None] * n
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
        on_stack[current_node] = False  # leaving this node, remove from stack
        return True

    return dfs(start)

 	

acyclic_graph = [
    [(1,None), (2,None)],
    [(2,None)],
    []
]
print(is_acyclic_component(acyclic_graph, 0))