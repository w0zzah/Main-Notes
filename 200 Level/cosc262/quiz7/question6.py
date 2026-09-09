def num_rushes1(slope_height, rush_height_gain, back_slidin, i = 0, c = 0, l = 0.95):
    if c + rush_height_gain >= slope_height:
        return i + 1
    return num_rushes(slope_height,rush_height_gain * l,back_slidin,i+1,c+rush_height_gain-back_slidin, l*l)

def num_rushes(slope_height, rush_height_gain, back_slidin, i=0, c=0):
    if current_height + rush_height_gain >= slope_height:
        return i + 1
    new_height = current_height + rush_height_gain - back_slidin
    fatigue = 0.95  
    return num_rushes(slope_height, rush_height_gain * fatigue, back_slidin * fatigue, i + 1, new_height)

ans = num_rushes(100, 15, 7)
print(ans)