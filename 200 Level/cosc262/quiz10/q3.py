def compute(numbers):
    n = len(numbers)
    output = [0] * n # a list of length n filled with zeros
    for i in range(n):
        j = 0
        while j <= i:
            output[i] += numbers[j]
            j += 1
    return output

def compute1(numbers):
    l = 0
    k = 0
    n = len(numbers)
    output = [0] * n
    for i in numbers:
        k += i
        output[l] += k
        l += 1
    return output


print(compute([1,2,3,4,5,6]))
print(compute1([1,2,3,4,5,6]))


