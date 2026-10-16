def radix_key(d):
    return lambda number: (number // (10**(d - 1))) % 10

def counting_sort_by_digit(numbers, d):
    key_func = radix_key(d)
    
    counts = [0] * 10
    for x in numbers:
        digit = key_func(x)
        counts[digit] += 1
        
    for i in range(1, 10):
        counts[i] += counts[i-1]
        
    output = [0] * len(numbers)
    for x in reversed(numbers):
        digit = key_func(x)
        counts[digit] -= 1
        output[counts[digit]] = x
        
    return output

def radix_sort(numbers, d):

    current_list = list(numbers)
    
    for i in range(1, d + 1):
        current_list = counting_sort_by_digit(current_list, i)
        
    return current_list
    


input_list = [329, 457, 657, 839, 436, 720, 355]
print(radix_sort(input_list, 1))
print(radix_sort(input_list, 2))
print(radix_sort(input_list, 3))
