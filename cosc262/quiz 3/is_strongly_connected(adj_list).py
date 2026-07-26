from collections import deque

def ifyoutriedtokillyourselfyouwouldntmakeitpasthedoor():
    """
        This code must take a string --> Convert to an adj_list --> perform a bfs ---> transpose ---> perform another bfs
        
        Function 1: adj_list ---> String convertion /
        Function 2: BFS
        Function 3: Transpose /
        Function 2: BFS
        Function 3: if all index != None, then return True


    """

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

def transpose(adj_list):
    n = len(adj_list)
    transposed_list = [[] for i in range(n)]
    for vertex1 in range(n):
        edges = adj_list[vertex1]
        for edge in edges:
            vertex2 = edge[0]
            weight = edge[1]
            transposed_list[vertex2].append((vertex1, weight))
    return transposed_list

def bfs(adj_list, start = 0):


    n = len(adj_list)
    parent_array = [None] * n
    discovered = [False] * n
    queue = deque()

    discovered[start] = True
    queue.append(start)

    while queue:
        parent = queue.popleft()
        for neighbor, _ in adj_list[parent]:
            if discovered[neighbor] != True:
                discovered[neighbor] = True
                queue.append(neighbor)
                parent_array[neighbor] = parent
    return parent_array


def is_strongly_connected(adj_list):
    first_bfs = bfs(adj_list)
    second_bfs = bfs(transpose(adj_list))
    total = first_bfs[1:] + second_bfs[1:]
    for i in total[1:]:
        if i is not None:
            return False
    return True

def is_strongly_connected_refined(adj_list):
    first_bfs = bfs(adj_list)
    second_bfs = bfs(transpose(adj_list))
    
    return all(node is not None for node in first_bfs[1:] + second_bfs[1:])






graph_string = """\
D 4
0 1
1 2
2 0
"""


print(is_strongly_connected(adjacency_list(graph_string)))


# -----------------> to see each individual item (ctrl + / to uncomment selected text)
#
# sections = [
#     ("Adjacency List",       adjacency_list(graph_string)),
#     ("BFS of Adjacency List", bfs(adjacency_list(graph_string))),
#     ("Transposed List",       transpose(adjacency_list(graph_string))),
#     ("BFS of Transposed List", bfs(transpose(adjacency_list(graph_string)))),
# ]

# for title, result in sections:
#     print(f"\n{'─' * 40}")
#     print(f"  {title}")
#     print(f"{'─' * 40}")
#     print(result)

# print(f"\n{'─' * 40}\n")