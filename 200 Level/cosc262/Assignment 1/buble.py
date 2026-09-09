def bubbles(s):
    graph = s.splitlines()
    header = graph[0].split()
    vertex = int(header[1])
    
    # Build adjacency list directly
    adj = [[] for _ in range(vertex)]
    for line in graph[1:]:
        part = line.split()
        v1, v2 = int(part[0]), int(part[1])
        adj[v1].append(v2)
        adj[v2].append(v1)  # undirected
    
    # BFS to find connected components (bubbles)
    visited = set()
    result = []
    
    for i in range(vertex):
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
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

	

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
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