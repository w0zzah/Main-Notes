import heapq
import math
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


def dijkstra(adj_list, start):
    n = len(adj_list)
    distance = [math.inf] * n
    parent = [None] * n
    distance[start] = 0
    
    # Min-heap: (distance, vertex)
    heap = [(0, start)]
    
    while heap:
        dist_u, u = heapq.heappop(heap)
        
        # Skip if we've already found a better path
        if dist_u > distance[u]:
            continue
        
        for v, weight in adj_list[u]:
            new_dist = distance[u] + weight
            if new_dist < distance[v]:
                distance[v] = new_dist
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))
    
    return (parent, distance)


graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))