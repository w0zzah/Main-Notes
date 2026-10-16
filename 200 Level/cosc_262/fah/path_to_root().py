def path_to_root(vertex, parent):
    path = []
    current = vertex
    while current is not None:
        path.append(current)
        current = parent[current]
    return path


parent = [None, 0, 0]
for i in range(len(parent)):
    print(path_to_root(i, parent))