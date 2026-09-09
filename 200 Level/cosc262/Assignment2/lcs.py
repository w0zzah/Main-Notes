def lcs(s1, s2):
    n = len(s1) + 1
    m = len(s2) + 1
    table = [[0] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if  s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    lcs_characters = []
    i = n - 1
    j = m - 1
    while i > 0 and j > 0:
        # if diagonal are matching
        if s1[i-1] == s2[j-1]:
            lcs_characters.append(s1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] >= table[i][j-1]: # Makes you go up 
            i -= 1
        else: # Makes you go left
            j-= 1
    return "".join(lcs_characters[::-1])

s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)


s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

	

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))


s1 = 1500 * 'x'
s2 = 1500 * 'y'
print(lcs(s1, s2))