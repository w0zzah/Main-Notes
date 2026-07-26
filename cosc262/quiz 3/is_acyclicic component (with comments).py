def is_acyclic_component(adj_list, vertex):
    
        #--------------------------------------------------------Initialise-------------------------------------------------------->

    n = len(adj_list) #-------------> [Node 0[()], Node 1[()], Node 2[()]]  1 + 1 + 1 = 3 = n
    parent = [None] * n #-----------> [None]  * 3 ---> [None, None, None]
    visited = [False] * n #---------> [False] * 3 ---> [False, False, False]
    recStack = [False] * n #--------> Tracks nodes in current DFS path ---> [False, False, False]

        #--------------------------------------------------------Initialise-------------------------------------------------------->

        #-----------------------------------------------------Read through list---------------------------------------------------->

    def dfs(current_node):
        visited[current_node] = True #----> mark node as visited
        recStack[current_node] = True #--> add node to current recursion stack

        for neighbor, with_weight in adj_list[current_node]: #---> iterate through neighbors (tuple unpacking)

            if not visited[neighbor]: #---------------------------> if neighbor not visited
                parent[neighbor] = current_node #-----------------> track where we came from

                if not dfs(neighbor): #---------------------------> recurse into neighbor
                    return False #--------------------------------> cycle found deeper

            elif recStack[neighbor]: #----------------------------> neighbor is in current path
                return False #------------------------------------> cycle detected!

        recStack[current_node] = False #--------------------------> remove node from recursion stack (backtrack)
        return True #---------------------------------------------> no cycle found from this node

        #-----------------------------------------------------Run DFS------------------------------------------------------------->

    return dfs(vertex) #------------------------------------------> start DFS from given vertex