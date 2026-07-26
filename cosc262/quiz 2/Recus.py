def rec(i):
    ls = []
    def rec2(i):
        if i == []: return
        ls.append(i[-1])
        rec2(i[-1::-1])
        print(i )
    rec2(i)
    return ls





ls = [1, 2, 3, 4, 5]
print(rec(ls))