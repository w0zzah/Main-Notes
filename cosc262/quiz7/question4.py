#Define a function my_enumerate(items) that behaves in a similar way to the built-in enumerate. 
# It should return a list of tuples (i, item) where item is the ith item, with a 0 origin, of the list items (see the examples below). 
# Check the test cases for how the function should work. Your function must not call either of python's inbuilt enumerate or zip functions 
# and cannot use any slices or loops nor import anything.

#Because slices are disallowed, you will need to pass in an extra parameter as explained in the above info panel.

#A O(n2) solution is acceptable here, though a O(n) solution is better (and perfectly possible).

def my_enumerate(items, i = 0):
    if i >= len(items):
        return []
    return [(i, items[i])] + my_enumerate(items, i + 1)

ans = my_enumerate([10, 20, 30])
print(ans)

ans = my_enumerate(['dog', 'pig', 'cow'])
print(ans)

ans = my_enumerate([])
print(ans)