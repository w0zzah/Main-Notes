def find(data, value, result = 0):
    if data == []:
        return None
    elif (data[0] == value):
        return result
    return find(data[1:], value, result + 1)



""" or use counter as index """

def find_c(data, value, i = 0):
    if data == []:
        return []
    if data[i] == value:
        return i
    return find_c(data, value, i + 1)

print(find_c([10, 20, 30, 0], 0))