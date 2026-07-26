from collections import deque

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

def bubbles(physical_contact_info):
    adj_list = adjacency_list(physical_contact_info)
    n = len(adj_list)
    nl = [[i]for i in range(n)]

    visited = [False] * len(adj_list)

    for neighbour in adj_list:
        print(neighbour)

    # while queue:
    #     path = queue.popleft()
    #     current = path[-1]
        
    #     for neighbour, _ in adj_list[current]:
    #         if neighbour == :
    #             return path + [neighbour]
    #         if not visited[neighbour]:
    #             visited[neighbour] = True
    #             queue.append(path + [neighbour])




physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

	

[[0, 1]]