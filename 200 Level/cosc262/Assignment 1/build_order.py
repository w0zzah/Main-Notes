from collections import deque
import heapq
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

def is_acyclic(adj_list):
    state = {}

    def dfs(v):
        state[v] = 1  # discovered

        for neighbour, weight in adj_list[v]:
            if state.get(neighbour) == 1:
                return False
            if state.get(neighbour) is None:
                if not dfs(neighbour):
                    return False

        state[v] = 2  # processed
        return True

    for vertex in range(len(adj_list)):
        if state.get(vertex) is None:  # only start DFS from unvisited nodes
            if not dfs(vertex):
                return False
    return True

    return dfs(vertex)


def build_order(dependencies):


    """
        KEY NOTES:
            if any cycle is present: return None
            else, from 0 find the next lowest number
                if next lowest number doesnt exist: return base order list [0, 1, 2...]
                else append lowest number, then find next lowest number append etc           
            
    """
    adjlist = adjacency_list(dependencies)
    if not is_acyclic(adjlist):
        return None
    n = len(adjlist)
    ind = [0] * n
    for current in range(n):
        for neighbour, _ in adjlist[current]:
            ind[neighbour] += 1

    heap = [current for current in range(n) if ind[current] == 0]
    heapq.heapify(heap)

    order = []
    while heap:
        current = heapq.heappop(heap)
        order.append(current)
        for neighbour, _ in adjlist[current]:
            ind[neighbour] -= 1
            if ind[neighbour] == 0:
                heapq.heappush(heap, neighbour)
    return order if len(order) == n else None


dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""

print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])


dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))

dependencies = """\
D 3
0 1
1 2
2 0
"""

print(build_order(dependencies))



