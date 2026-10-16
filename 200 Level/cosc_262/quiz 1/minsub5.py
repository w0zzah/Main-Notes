def min_subset_size(n, target):
    total = 0
    count = 0
    for number in range(n, 0, -1):
        if number % 5 != 0 and total + number <= target:
            count += 1
            total += number
    if total == target:
        return count


print(min_subset_size(31, 61))