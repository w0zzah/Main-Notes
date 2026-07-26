def num_rushes(slope_height, rush_height_gain, back_slidin, i = 0, c = 0):
    if c + rush_height_gain >= slope_height:
        return i + 1
    return num_rushes(slope_height,rush_height_gain,back_slidin,i+1,c+rush_height_gain-back_slidin)

ans = num_rushes(100, 10, 5)
print(ans)