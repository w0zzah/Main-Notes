def adjacency_list(graph_string):

    lines = graph_string.splitlines()
    header = lines[0].split()
    v = int(header[1])
    weighted = 'W' in header
    directed = 'D' in header
    adj_list = [[] for i in range(v)]


    for line in lines[1:]:
        parts = line.split()
        v1 = int(parts[0])
        v2 = int(parts[1])
        if weighted:
            weight = int(parts[2])
            adj_list[v1].append((v2, weight))
            if not directed:
                adj_list[v2].append((v1, weight))
        else:
            adj_list[v1].append((v2, None))
            if not directed:
                adj_list[v2].append((v1, None))
    return adj_list

def transpose(adj_list):
    tp_ls = [[] for i in range(len(adj_list))]
    index = 0
    for parent in adj_list:
        for child, _ in parent:
            tp_ls[child].append((index, _))
        index += 1

    return tp_ls
    
    # takes a directed graph with at least one vertex and returns wether or not it is strongly conencted. Otherwise it returns false
    # For a graph to be strongly conencted, you must be able to reach every vertex from any other vertex.
    # An easy test for this in code is to run a bfs on on both the original graph and the transpose and if all nodes are not
    # reached by both then it is not strongly conencted.

def bfs(adj_list, start = 0):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for neighbor, _ in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def is_strongly_connected(adj_list):
    n = len(adj_list)
    if n == 0:
        return
    else:
        if len(bfs(adj_list)) != n:
            return False
        elif len(bfs(transpose(adj_list))) != n:
            return False
        return True
 	

 	

graph_string = """\
D 4
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))