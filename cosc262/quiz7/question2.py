def recursive_divide(x, y):
    if x < 0:
        return -1
    else:
        return 1 + recursive_divide(x-y, y)
    

print(recursive_divide(1251, 5))
print(1251 // 5)