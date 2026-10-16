def lcs(s1, s2):

    n = len(s1) + 1
    m = len(s2) + 1

    table = [[0] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    lcs_characters = []
    i = n - 1
    j = m -1
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_characters.append(s1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] >= table[i][j-1]:
            i-= 1
        else:
            j -= 1
    return "".join(lcs_characters[::-1])

def wrap_helper(string, lcs_str):
    p = 0
    result = ""
    for character in string:
        if p < len(lcs_str) and lcs_str[p] == character:
            result += character
            p += 1
        else:
            result += f"[[{character}]]"
    return result

def line_edits(s1, s2): 
    line1 = s1.splitlines()
    line2 = s2.splitlines()
    t = [[0] * (len(line2) + 1) for _ in range(len(line1) + 1)]

    for i in range(len(line1) + 1):
        t[i][0] = i
    for j in range(len(line2) + 1):
        t[0][j] = j
    
    for i in range(1, len(line1) + 1):
        for j in range(1, len(line2) + 1):
            cost = 0 if line1[i-1] == line2[j-1] else 1
            t[i][j] = min(t[i-1][j-1] + cost,
            t[i-1][j] + 1, t[i][j-1] + 1)
    
    results = []
    i = len(line1)
    j = len(line2)

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = 0 if line1[i-1] == line2[j-1] else 1
            if t[i][j] == t[i-1][j-1]+cost and t[i][j]<t[i-1][j]+1 and t[i][j]<t[i][j-1]+1:
                temp1 = line1[i-1]
                temp2 = line2[j-1]
                if cost == 1:
                    common = lcs(temp1, temp2)
                    results.append(("S", wrap_helper(temp1, common), wrap_helper(temp2, common)))
                else: 
                    results.append(("C", temp1, temp2))
                i -= 1
                j -= 1
                continue
        if i > 0 and t[i][j] == t[i-1][j] + 1:
            results.append(("D", line1[i-1], ""))
            i -= 1
        else:
            results.append(("I", "", line2[j-1]))
            j -= 1
    return results[::-1]

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
t = line_edits(s1, s2)
for row in t:
    print(row)
