def key_positions(seq, key):
    # check empty set 
    if not seq:
        return []
    # Set up empty set for key calcs [9, 4, 1, 0, 1, 4]
    kp = [key(x) for x in seq]

    # 9
    maxKey = max(kp)

    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c = [0] * (maxKey + 1)

    # [1, 2, 0, 0, 2, 0, 0, 0, 0, 1]
    for x in kp:
        c[x] += 1

    
    start_pos = [0] * (maxKey + 1)
    current_sum = 0
    for i in range(len(c)):
        start_pos[i] = current_sum
        current_sum += c[i]
    
    return start_pos

def sorted_array(seq, key, positions):
    result = [None] * len(seq)

    for item in seq:
        k = key(item)
        target_index = positions[k]
        result[target_index] = item
        positions[k] += 1
    return result


print(key_positions([3, 1, 2], lambda x: x))
print(sorted_array(range(-3,3), lambda x: x**2, [0, 1, 3, 3, 3, 5, 5, 5, 5, 5]))



P0  	P1  	P2  	P3 	    P4  	P5  	P6  	P7  	P8
(30, 5)(7, 20)(15, 1)(25, 19)(22, 11)(5, 22)(17, 3)(30, 30)(12, 32)