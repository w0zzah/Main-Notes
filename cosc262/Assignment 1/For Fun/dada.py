from adj import adjacency_list # Will need to put in adj_list on learn
from collections import deque


def format_sequence(converters_info, source_format, destination_format):

    """
        KEY NOTES:
            This function takes an adj list, a start point and finish point. We are trying to see how we can go from point a
            to point b. Speed and weight do NOT need to be considered.

            Step 1: Base Case
                Are we already on the node? if so return the current node as we are on desired node
                    (this serves more as an edge case and will only ever be called at the start)
            
            Step 2: Initialise
                Initialise a deque(double ended queue) that holds all current potential paths as lists.

    """
    adjlist = adjacency_list(converters_info)
    
    if source_format == destination_format: # edge - case
        return [source_format]
    
    queue = deque([[source_format]]) # Contains a (tuple) for each edge from the start <-----------------------------------|
    visited = [False] * len(adjlist) #                                    |                                                |
#                                                                         |                                                |
    while queue:#                                                         |                                                |
        path = queue.popleft() # adds last node visited                : [1] --> [1, 0] --> [1, 2]                         |
        current = path[-1] # set current as the node we are sitting on :  1  -->     0      --> 2                          |
        print(f"Current coice of path {path}")
            # Example: I want to convert my mp3 to mp5, but can only convert to mp5 if its an mp4    (mp3 --> mp4)  (mp4 --> mp5)
            #
            # Step 1: Go through all possible convertions from mp3                                                         |
            #                                 
        if adjlist[current] == []:
            print("    There's nowhere to go!")
            print("    Remove me from the list!")

        for neighbour, _ in adjlist[current]: # Starts through adj_list from source format,--------------------------------|
            
            # Step 2 : Check if convertion path is the one we are looking for
            if neighbour == destination_format: # mp4 != mp5 so we pass
                return path + [neighbour]

            # Step 3 : If current convertion isn't the one we are looking for, set it as a possible path to required format
            #  
            if not visited[neighbour]:  # Check if we have already checked mp4's convertions
                visited[neighbour] = True # Set that we have / will 
                queue.append(path + [neighbour])
                print(f"    Looking at {current} ' s neighbout: {neighbour}")   #  add it to the possible connections to our desired convertion
        print(f"All possible paths : {queue}\n")
    return None

# Why use deque()? ----> deque (or dEck) is great as we can take the first value off and set it to variable e.g x = deque.popleft (line 55)
# How does it work?
    # say we have paths from 1 as 1 --> 2 --> 3  and 1 --> 4
    # First while loop: deque([[1]]) |THEN POP ME|  -->  deque([[1, 2]])  --> deque([[1, 2], [1, 4]])
    # Second while loop: deque([[1, 2], [1, 4]]) |THEN POP ME| ---> deque([[1, 4]])  ---> deque([[1, 2], [1, 2, 4]])

converters_info_str = """\
D 6
0 5
1 2
1 3
2 4
2 0
"""

print(format_sequence(converters_info_str, 1, 5))