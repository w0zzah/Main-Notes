def almost_all(numbers):
    tot = sum(numbers)
    return [tot - x for x in numbers]