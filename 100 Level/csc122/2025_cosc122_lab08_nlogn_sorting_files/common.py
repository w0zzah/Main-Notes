from quicksort import *


def read_data(filename):
    """ Returns a list of integers read from the file """
    with open(filename) as infile:
        values = [int(line.strip()) for line in infile]
    return values


def common_items(list_x, list_y):
    """ Takes two sorted lists as input (ie, both lists are in ascending order).
    Returns a list containing all the items in list_x that are also in list_y.
    Returns an empty list if there are none.

    The resulting list should be in order and only contain one instance of each
    item that appears in both lists, ie, common items should only be listed once.
    NOTE: You should use a method similar to the merge function in mergesort,
    that is, use a while loop and a couple of indices. Don't use any for loops!

    First write code for dealing with two lists that each contain only uniques values.
    When you have that running, update it so that it deals with lists that don't
    contain all unique values, see the commented doctests below

    NOTES:
    Your function will need to use only one while loop.
    Your function shouldn't use expressions like:
       - item in alist
       - for item in alist

    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[0,1,2,3])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3,4,5,6,7],[0,2,7])
    [0, 2, 7]
    >>> common_items([0,2,7], [0,1,2,3,4,5,6,7])
    [0, 2, 7]
    >>> common_items([4,6,11], [0,1,2,3,4,5,6,7])
    [4, 6]
    >>> common_items([4,6,11], [5,6,7,11,20,100,200])
    [6, 11]
    >>> common_items([5,6,7,11,20,100,200], [4,6,11])
    [6, 11]
    >>> common_items([11], [0,1,2,3,4,5,6,7])
    []
    >>> common_items([0,1,2,3,4,5,6,7], [11])
    []
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    """
    # add the following doctests (AND some of your own!)
    # when ready for lists of non-unique items
    # >>> common_items([0,1,2,3],[0,0,2,4])
    # [0, 2]
    # >>> common_items([0,1,2,2,5,5,6,6,7],[0,0,2,4,5,5,5,7])
    # [0, 2, 5, 7]
    
    """Return a list of all items in both lists, only once."""
    i, j = 0, 0
    result = []
    while i < len(list_x) and j < len(list_y):
        if list_x[i] == list_y[j]:
            if not result or result[-1] != list_x[i]:
                result.append(list_x[i])
            i += 1
            j += 1
        elif list_x[i] < list_y[j]:
            i += 1
        else:
            j += 1
    return result
    
def common_unique(list_x, list_y):
    """Return sorted list of unique common items."""
    i, j = 0, 0
    result = []
    while i < len(list_x) and j < len(list_y):
        if list_x[i] == list_y[j]:
            if not result or result[-1] != list_x[i]:
                result.append(list_x[i])
            i += 1
            j += 1
        elif list_x[i] < list_y[j]:
            i += 1
        else:
            j += 1
    return result

# filenames
pairs = [
    ('ordered_unique_12.txt', 'ordered_unique_13.txt'),
    ('ordered_unique_17.txt', 'ordered_unique_19.txt'),
    ('ordered_unique_8.txt',  'ordered_unique_9.txt'),
    ('ordered_17.txt', 'ordered_19.txt'),
    ('ordered_12.txt', 'ordered_13.txt'),
    ('ordered_11.txt', 'ordered_14.txt')
]

for a, b in pairs:
    A = read_data('./data/' + a)
    B = read_data('./data/' + b)
    common = common_unique(A, B)
    print(a, b)
    if common:
        print("  smallest common =", common[0])
        print("  biggest common  =", common[-1])
        print("  count unique common =", len(common))
    else:
        print("  no common elements")



if __name__ == "__main__":
    doctest.testmod()
