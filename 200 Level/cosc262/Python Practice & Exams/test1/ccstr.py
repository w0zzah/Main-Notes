def concat_strings(strings):
    if len(strings) == 0: return ""
    def addstring(strings):
        if len(strings) == 1:
            return strings[0]
        else:
            return strings[0] + addstring(strings[1:])
    return addstring(strings)

print(concat_strings([]))
ans = concat_strings(['a', 'hot', 'day'])
print(ans)