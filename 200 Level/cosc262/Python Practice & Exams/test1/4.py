def backwards(s):
    if len(s) == 1:
        return s[0]
    return s[-1] + backwards(s[:-1:])

print(backwards("Hi there!"))