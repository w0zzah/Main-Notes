import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, start_index = 0):
    """Takes a list of numbers and does weird stuff with it"""
    if start_index >= len(data):
        return 0
    current_value = data[start_index]
    if (current_value // 100) % 3 != 0:
        return 1 + dumbo_func(data, start_index + 1)
    else:
        return dumbo_func(data, start_index + 1)

data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))