import heapq
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


def min_shipping_costs(adj_list, transit_cost, source):
    # Initialize distances as infinity for all nodes
    dist = {node: float('inf') for node in range(len(adj_list))}
    dist[source] = 0
    
    # Min-heap: (cost, node)
    heap = [(0, source)]
    visited = set()
    
    while heap:
        cost, u = heapq.heappop(heap)
        
        if u in visited:
            continue
        visited.add(u)
        
        # Relax all edges from u
        for v, edge_weight in adj_list[u]:
            if v in visited:
                continue
            
            # Transit cost applies to u if it's an intermediate node
            # (i.e., u is not the source)
            transit = transit_cost.get(u, 0) if u != source else 0
            new_cost = cost + edge_weight + transit
            
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    
    # Return sorted list of (port, cost) for ALL reachable ports INCLUDING source
    return sorted(
        [(node, d) for node, d in dist.items() if d < float('inf')]
    )

graph_string = """\
D 4 W
0 1 2
0 2 3
1 3 1
2 3 2
"""

transit_cost = {1: 4, 2: 1}

for source in range(4):
    print(min_shipping_costs(adjacency_list(graph_string), transit_cost, source))