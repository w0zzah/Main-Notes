def compute(numbers):
    n = len(numbers)
    out = [0 for i in range(n)]
    total = 0 
    for i, number in enumerate(numbers):
        out[i] = number + total
        total += number
    return out

print(compute([1,2,3,4,5]))