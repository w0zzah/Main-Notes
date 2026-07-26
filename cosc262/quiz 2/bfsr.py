from collections import deque

def bfs_tree(adj_list, start):

    """
    edges = len
    parents = None * edges
    visisted = False * edges
    create a deck

    #start

    vi[s] = T
    p[s] = N

    deckappend s

    while qdeck

    u = q.popleft
    for v _ in ad[u]
        if not vi[v]
        vi[v] T
        p[v] U
        q.ap(v)
    
    return p
    """

    e = len(adj_list)
    Parents = [None] * e
    Visited = [False] * e
    queue = deque()

    Visited[start] = True
    Parents[start] = None

    queue.append(start)
    while queue:
        u = queue.popleft()
        for v, _ in adj_list[u]:
            if not Visited[v]:
                Visited[v] = True
                Parents[v] = u
                queue.append(v)

    return Parents

adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj_list, 0))