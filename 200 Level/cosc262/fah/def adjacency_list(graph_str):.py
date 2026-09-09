def adjacency_list(graph_str):
    #split up the string based of of \n (every new line is turned into its own string in the list)
    lines = graph_str.splitlines()
    #Take the top line off
    header = lines[0].split()
    directed = header[0] == 'D'
    weighted = 'W' in header
    n = int(header[1])
    #sets up an empty lis for the data to be put in
    adj = [[] for i in range(n)]
    #go through each line and arrange
    for line in lines[1:]:
        parts = line.split()
        if not parts:
            continue
        vertex1 = int(parts[0])
        vertex2 = int(parts[1])
        weight = int(parts[2]) if weighted else None

        adj[vertex1].append((vertex2, weight))

        if not directed:
            adj[vertex2].append((vertex1, weight))
    return adj

def adjacency_matrix(graph_str):
    #remove hanging white space, split each line into seperate portions dependant on each call to \n, remove excess white space again
    lines = [line.strip() for line in graph_str.strip().splitlines()
             if line.strip()]
    #split first line to read
    header = lines[0].split()
    #assign bool value if head == D
    directed = header[0] == 'D'
    #assign weighted if len = 3 and w is present in [2]
    weighted = len(header) == 3 and header[2] == 'W'
    #set total vertices
    n = int(header[1])
    if weighted:
        #creates and n x n matrix filled with None variable
        matrix = [[None for i in range(n)] for i in range(n)]
    else:
        #creates an n x n matrix fileld with 0 variable
        matrix = [[0 for i in range(n)] for i in range(n)]
    #loop through the list, skipping the first info segment
    for line in lines[1:]:
        #split each variable up
        parts = line.split()
        #set first and second variables to represent the two vertices at end of edge
        vertex1 = int(parts[0])
        vertex2 = int(parts[1])
        """This code is used to actually place the values inside of the matrix. if its weighted it needs to put the weight value associated in there
        if its not weighted then it just puts one in the respective location. After a number has been place it checks whether it is directed or not.
        if it isnt then it need to add another value on the other side of the matrix. so we go from x,y placements to y,x placements"""
        if weighted:
            w = int(parts[2])
            #set weight value at v1,v2 location = w
            matrix[vertex1][vertex2] = w
            if not directed:
                #set val @ v2,v1 == to the place at previous value
                matrix[vertex2][vertex1] = w
        else:
            matrix[vertex1][vertex2] = 1
            if not directed:
                matrix[vertex2][vertex1] = 1
    return matrix

graph_string = """\
D 3 W 0 1 7 1 0 -2 0 2 0
"""
print(adjacency_matrix(graph_string))