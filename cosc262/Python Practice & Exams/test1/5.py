def odds(numbers):
    if numbers== []:
        return []
    elif numbers[0] % 2 != 0:
        return [numbers[0]] + odds(numbers[1:])
    return odds(numbers[1:])

    
print(odds([0, 1, 12, 13, 14, 9, -11, -20]))