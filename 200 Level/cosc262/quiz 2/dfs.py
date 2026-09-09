def dfs_tree(adj_list, start):
    """
        Create a single list with each index corresponding to index's parent

        Step 1 : Initialise
            i, Set n = len list
            ii, Initialise parent array
            iii, Initialise Visited array
        
        Step 2: Sort:
            i, Setup recurssive func dfs('Current')
            ii, Set 'Current' as visited
            iii, Iterate through the list for neighbor, weight in list at current index
            iv, If visited at index neighbor is false
            v,      Parent at index neighbor = Current
                    Run with neighbor
            return parents

    """

    #--------------------------------------------------------Initialise-------------------------------------------------------->

    n = len(adj_list) #-------------> [Node 0[()], Node 1[()], Node 2[()]]  1 + 1 + 1 = 3 = n
    parent = [None] * n #-----------> [None]  * 3 ---> [None, None, None]
    visited = [False] * n #---------> [False] * 3 ---> [False, False, False]

    #--------------------------------------------------------Initialise-------------------------------------------------------->

    #-----------------------------------------------------Read through list---------------------------------------------------->

    def dfs(current_node):
        visited[current_node] = True #----> [False, False, False] -----> [False, False, True]
        for neighbor, with_weight in adj_list[current_node]: #---> for (neighbor, with_weight) KEY NOTE: The statement is taking a TUPLE with values (neighbor, with_weight). Then
#                                                                     [(1, None), (2, None)],            for each tuple in adj_list[starting at the current_node] goes through. 
#                                                                     [(0, None), (2, None)],            e.g (0, None) ----> (1, None) ----> finish
# (neighbor, with_weight) the first instance in adj_list[c_n] ------> [(0, None), (1, None)] <--- current_node = 2  
#                                                                       ^                                         |
#                                                                  (This guy)                                     |
#                                                                       |                                         |
            if not visited[neighbor]: #--------------------------->  [False, False, True]                         |
                parent[neighbor] = current_node #----------------->  [None, None, 2] -----------------------------


    #-----------------------------------------------------ALL CURRENT VARIABLES ---------------------------------------------------->
#                                                 current_node --> [2]
#                                                 neighbor     --> [0]
#                                                 PARENT LIST ---> [None, None, 2]
#                                                 VISITED LIST --> [False, False, True]
    #-----------------------------------------------------ALL CURRENT VARIABLES ---------------------------------------------------->

                dfs(neighbor) #----------------------------------->  dfs(0)

            visited[current_node] = True #----> [False, False, True] -----> [True, False, True]
            for neighbor, with_weight in adj_list[current_node]: #---> for (neighbor, with_weight)
    #(neighbor, with_weight) the first instance in adj_list[c_n] ------>  [(1, None), (2, None)], <--- current_node = 0        
    #                                                                     [(^, None), (2, None)],                     |           
    #                                                                     [(|, None), (1, None)]                      |
    #                                                                       |                                         |  
    #                                                                       |                                         |
    #                                                                       -------|                                  |
                if not visited[neighbor]: #--------------------------->  [False, False, True]                         |
                    parent[neighbor] = current_node #----------------->  [None, None, 2] -----------------------------|
        dfs(start)
        return parent

    #-----------------------------------------------------Read through list---------------------------------------------------->


# an undirected graph


adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]


print(dfs_tree(adj_list, 2))
Vertex 0[None, 0, 1]
#Vertex 1[1, None, 0]
#Vertex 2[2, 0, None]