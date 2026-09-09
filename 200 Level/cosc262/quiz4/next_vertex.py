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
    """
        EXAMPLE INPUTS:

        in_tree = [False, True, True, False, False]
        distance = [math.inf, 0, 3, 12, 5]


        Initialise:
            i, Set up variable to compare shortest distance and one to decide it's next vertex
        Run:
            i, for each each distance recorded so far
            ii, if the node is True in tree and is shorter than current minimum distance:
            iii, Next node = Current node i, new shortest distance = distance to i
            iv, After checking all nodes, return the next node         (^as it has shortest difference)

    """
    #Initialise -

    #--------------------------------------------------------Initialise-------------------------------------------------------->

    min_dist = math.inf
    next_v = None

    #--------------------------------------------------------Initialise-------------------------------------------------------->

    #--------------------------------------------------------Start Cycle------------------------------------------------------->

    for i in range(len(distance)):

        if not in_tree[i] and distance[i] < min_dist:
            next_v = i
            min_dist = distance[i]

    #-------------------------------------------------------Finish Cycle------------------------------------------------------->

        
    return next_v 

def dijkstra(adj_list, start):
    #--------------------------------------------------------Initialise-------------------------------------------------------->

    n = len(adj_list)
    in_tree = [False] * n
    distance = [math.inf] * n
    parent = [None] * n
    distance[start] = 0

    #--------------------------------------------------------Initialise-------------------------------------------------------->


    #--------------------------------------------------------Start Cycle------------------------------------------------------->

    # will do this for 0--->1--->2

    while True:
        teen = next_vertex(in_tree, distance) #  0 ---> 1    So now 1 = teen
        if teen is None: # if you are reading this i fucked up and it is 1:18 so this patch fix works
            break
        in_tree[teen] = True # [f, ->TRUE<- , f] Set the closest neighbor as visited

        for child, weight in adj_list[teen]: # 1---> 2           Look at 'closest teens' children

            if not in_tree[child] and weight + distance[teen] < distance[child]: # check wether is shorter to go thru teen to get to child
                distance[child] = weight + distance[teen] # if so set that as the prefered route
                parent[child] = teen

                                            # For primms cycle,           
            # if not in_tree[child] and weight < distance[child]: # only need to check if its shortest route 
            #     distance[child] = weight # 
            #     parent[child] = teen                     

    #-------------------------------------------------------Finish Cycle------------------------------------------------------->

    return parent, distance


graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))