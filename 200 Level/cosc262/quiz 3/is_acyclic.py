def adjacency_list(string):
    graph = string.splitlines()
    header = graph[0].split()
    Undirected = 'U' in header
    vertices = int(header[1])
    weighted = 'W' in header
    adj_list = [[] for i in range(vertices)]
    for parts in graph[1:]:
        part = parts.split()
        v1 = int(part[0])
        v2 = int(part[1])
        if weighted:
            weight = part[3]
            adj_list[v1].append((v2, weight))
            if Undirected:
                adj_list[v2].append((v1, weight))
        adj_list[v1].append((v2, None))
        if Undirected:
            adj_list[v2].append((v1, None))
    return adj_list

def is_acyclic(adj_list):
    n = len(adj_list)
    visited = [False] * n
    on_stack = [False] * n
    finish_order = []
    def dfs(current_node):
        visited[current_node] = True
        on_stack[current_node] = True
        for neighbor, _ in adj_list[current_node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            elif on_stack[neighbor]:
                return False
        on_stack[current_node] = False
        finish_order.append(current_node)
        return True

    for node in range(n):
        print(finish_order[::-1])
        if not visited[node]:          # skip nodes already explored
            if not dfs(node):
                return False
    return finish_order[::-1] 
        

 	

graph_string = """\
D 5
0 2
1 2
2 4
2 3
"""


print(is_acyclic(adjacency_list(graph_string)))