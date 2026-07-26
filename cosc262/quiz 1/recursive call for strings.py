def concat_strings(strings):
    """Write a recursive function concat_strings(strings) that takes a list of strings as a parameter 
    and returns a single string made up of all the individual strings in strings concatenated together, in order. 
    Your implementation must not use the 'str.join' method.
Notes

    The problem statement implies that the input list will either be empty or have one or more elements, all of which will be of type str.
    As with all recursive algorithms, think about the base case; that is, for what input there is no need for a recursive call. See the example at the 
    beginning of this section.
    Recall that in Python, two strings can be concatenated using the + operator.
"""
    #edge case checl
    if len(strings) == 0:
        return ''
    #return the very first item in the list with the output of this command starting from index 1
    return strings[0] + concat_strings(strings[1:])