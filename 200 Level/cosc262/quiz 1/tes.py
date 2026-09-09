def f(a, b):
    if a < min(a,b):
        print("a")
    else:
        print("b")
    if max(a, b) > min(a, b):
        print("c")
    else:
        print("d")
    if a*b >= max(a, b):
        print("e")
    else:
        print("f")

print(f(3,1))