def squares(numbers):
    # check for when list is empty
    if len(numbers) == 0:
        return []
    # 
    return [numbers[0]**2] + (squares(numbers[1:]))


print(squares([1, 13, 9, -11]))
squares([1, 13, 9, -11])