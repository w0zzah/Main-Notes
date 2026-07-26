def line_edits(s1, s2):
    # split by \n
    line1 = s1.splitlines()
    line2 = s2.splitlines()
    n = len(line1)
    m = len(line2)

    # Create table no.
    table = [[0] * (m+1) for _ in range( n + 1)]
    for i in range(n + 1): 
        table[i][0] = i
    for j in range(m + 1): 
        table[0][j] = j
    
    # set cost counter
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost_sub = table[i-1][j-1] + (0 if line1[i-1] == line2[j-1] else 1)
            table[i][j] = min(cost_sub, table[i-1][j] + 1, table[i][j-1] + 1)
    
    i = n
    j = m

    results = []

    while i > 0 or j > 0:
        current_cost = table[i][j]

        # try copy
        if i > 0 and j > 0:
            # increase if not copy
            cost_diff = 0 if line1[i-1] == line2[j-1] else 1
            if current_cost == table[i-1][j-1] + cost_diff:
                cpyorsub = 'C' if cost_diff == 0 else 'S'
                results.append((cpyorsub, line1[i-1], line2[j-1]))
                i -= 1
                j -= 1
                continue
        # try delete
        if i > 0 and current_cost == table[i-1][j] + 1:
            results.append(('D', line1[i-1], ''))
            i -= 1
            continue
        # Try Insertion
        if j > 0 and current_cost == table[i][j-1] + 1:
            results.append(('I', '', line2[j-1]))
            j-= 1
    return results[::-1]

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)