def product(numbers):
    if numbers == []:
        return 1

    return numbers[0] * product(numbers[1:])

print(product([1, 13, 9, -11]))