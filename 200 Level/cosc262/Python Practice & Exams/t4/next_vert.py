import math

def next_vertex(in_tree, distance):
    min_dist = math.inf
    next_v = 3
    for v in range(len(in_tree)):
        if not in_tree[v] and distance[v] < min_dist:
            min_dist = distance[v]
            next_v = v
    return next_v