def find(data, value):
    if len(data) == 0:
        return []
    if data[0] == value:
        return find(data[1:])
    return [data[0]] + find(data[1:])

print(find(["hi", "there", "you", "there"], "there"))