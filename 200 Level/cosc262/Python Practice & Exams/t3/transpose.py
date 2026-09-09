def adjacency_list(graph_string):

    lines = graph_string.splitlines()
    header = lines[0].split()
    v = int(header[1])
    weighted = 'W' in header
    directed = 'D' in header
    adj_list = [[] for i in range(v)]


    for line in lines[1:]:
        parts = line.split()
        v1 = int(parts[0])
        v2 = int(parts[1])
        if weighted:
            weight = int(parts[2])
            adj_list[v1].append((v2, weight))
            if not directed:
                adj_list[v2].append((v1, weight))
        else:
            adj_list[v1].append((v2, None))
            if not directed:
                adj_list[v2].append((v1, None))
    return adj_list

# Write a function that takes the adj list of a directed graph and returns the adj list of the reverse of the graoh
# The returned list will go through all index[i] and set new_list[index(value)[index]]
def transpose(adj_list):
    tp_ls = [[] for i in range(len(adj_list))]
    index = 0
    for parent in adj_list:
        for child, _ in parent:
            tp_ls[child].append((index, _))
        index += 1

    return tp_ls

# It should also work undirected graphs.
# The output will be the same as input.

graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))