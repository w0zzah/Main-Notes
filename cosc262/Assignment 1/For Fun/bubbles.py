def bubbles(s):
    graph = s.splitlines()
    header = graph[0].split()
    directed = header[0] == 'D'
    vertex = int(header[1])
    weighted = len(header) == 3
    ls = [[i] for i in range(vertex)]
    visited = [False] * vertex
    pointer = [i for i in range(vertex)]
    for i in graph[1:]:
        part = i.split()
        v1 = int(part[0])
        v2 = int(part[1])
        point = int(pointer[v1])
        if not visited[v2]:
            if ls[v1] == []:
                ls[point].append(v2)
                ls[v2].remove(v2)
                visited[v2] = True
                pointer[v2] = point

            else:
                ls[v1].append(v2)
                ls[v2].remove(v2)
                visited[v2] = True
                pointer[v2] = v1
        elif not visited[v1]:
            point = int(pointer[v2])
            ls[point].append(v1)

    nls = [x for x in ls if x != []]
    return nls

def bubbles1(physical_contact_info):
    adj = adjacency_list(physical_contact_info)
    n = len(adj)
    visited = set()
    result = []

    for i in range(n):
        if i not in visited:
            bubble = []
            queue = [i]
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.add(current)
                    bubble.append(current)
                    for neighbour in adj[current]:
                        if neighbour not in visited:
                            queue.append(neighbour)
            result.append(bubble)
    return result



physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))