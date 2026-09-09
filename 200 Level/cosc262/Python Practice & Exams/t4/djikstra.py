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

def next_vertex(in_tree, distance):
    # Set all dist min
    min_dist = math.inf
    # Set next to be None, in case of no path
    next_v = None
    for i in range(len(distance)):
        # for total number of nodes
        if not in_tree[i] and distance[i] < min_dist:
            # If its not in the tree, then then go through
            next_v = i
            min_dist = distance[i]
        
    return next_v 

def dijkstra(adj_list, start):

    n = len(adj_list)
    in_tree = [False * n]
    distance = [math.inf * n]
    parent = [None * n]
    distance[start] = 0
    while True:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
