def  adjacency_list(graph_str):
    """Step 1: Initialise

        Split string(theres a cmd) .split()  -> 
        Split top on first line, set it to header -> 
        Set type and number of vertices -> 
        Create new list adj = [ [][][] ]

    Step 2: Read through list
        Go through each line (skipping first one)
        Split Line 
        Assign index to v1, v2, W (None if not weighted)
        Append v2, w to adj.v1
        If undirected Append v1, w to adj.v2

    Step 3: Return

    ---Initial preview graph
        D 3 W
        0 1 7
        1 0 -2
        0 2 0
    """

    #--------------------------------------------------------Initialise-------------------------------------------------------->

    graph = graph_str.splitlines() #--------> ['D 3 W', '0 1 7', '1 0 -2', '0 2 0']    "Splits graph string spaced by \n "
    line1 = graph[0].split() #--------------> ['D', '3', 'W']                          "Splits the [0]'th line to read individual properties"
    directed = line1[0] == 'D' #------------> ['D']  |                                 "Directed Check"
    vertices = int(line1[1]) #--------------> ['-', '^', '-']                          "Set vertices equal to an integer located at [1] of line 1"
    adj = [[] for i in range(vertices)] #---> [[], [], []]                             "Creates a list filled with empty lists for range 0 ->  vertices"     
    weighted = 'W' in line1 #---------------> ['-', '-', 'W']                          "Weighted Check"

    #--------------------------------------------------------Initialise-------------------------------------------------------->


    #-----------------------------------------------------Read through list---------------------------------------------------->

    for line in graph[1:]:
        part = line.split() #----------------> ['0', '1', '7']
        v1 = int(part[0]) #------------------> ['0', '-', '-']
        v2 = int(part[1]) #------------------> ['-', '1', '-']
        weight = int(part[2]) if weighted else None
        
        adj[v1].append((v2, weight))
        if not directed: adj[v2].append((v1, weight))
    return adj





def transpose(adj_list):
    """
    Step 1: Initialise
        i, set n = len
        ii, new list fill [] for n
        iii, for vertex in range(len)
            set edges = ad_ls[vertex]
                for edge in dges
                destination = [0]
                weight = [1]
                nl[dest] app (v, w)
        return nl
    """
    total_vertices = len(adj_list)
    transposed_list = [[] for i in range(total_vertices)]

    for vertex in range(total_vertices):
        edges = adj_list[vertex]
        for edge in edges:
            edge_destination = edge[0]
            edge_weight = edge[1]
            transposed_list[edge_destination].append((vertex, edge_weight))
    return transposed_list




# [[(1, None), (2, None)], [(0, None)], []]



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