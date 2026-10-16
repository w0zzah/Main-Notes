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

def format_sequence(converters_info, source_format, destination_format):
    adjlist = adjacency_list(converters_info)
    
    if source_format == destination_format:
        return [source_format]
    
    queue = deque([[source_format]])
    visited = [False] * len(adjlist)
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        
        for neighbour, _ in adjlist[current]:
            if neighbour == destination_format:
                return path + [neighbour]
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(path + [neighbour])
    
    return None