def compute(numbers):
    n = len(numbers)
    output = [0]  * n
    output[0] = numbers[0]
    for i in range(1, n):
        current = numbers[i]
        output[i] = numbers[i] + output[i-1]
    return output


compute([1,2,3,4,5])