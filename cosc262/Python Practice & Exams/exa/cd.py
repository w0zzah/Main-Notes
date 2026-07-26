def compute(nums):
    if nums == []:
        return []
    out = [] 
    out.append(nums[0])
    for i in range(len(nums) - 1):
        f = nums[i]
        k = out[i]
        out.append(out[i] + nums[i + 1])
    return out

 	

print(compute([1, -1, -1, 1, 1, -1]))