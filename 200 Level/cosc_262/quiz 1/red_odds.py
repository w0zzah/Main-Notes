def odds (numbers):
    #basecase
    if numbers == []:
        return []
    #if odd
    elif (numbers[0] % 2 != 0):
        #return val + func
        return [numbers[0]] + odds(numbers[1:])
    #rerun func
    return odds(numbers[1:])

print(odds([0, 1, 12, 13, 14, 9, -11, -20]))