from c import *

def is_on_segment(p, a, b):
    if signed_area(p, a, b) != 0: # if a 3 points have no area, then all points must be in a line
        return False
    return (min(a.x, b.x) <= p.x <= max(a.x, b.x) and # check if it is between point a and b
          min(a.y, b.y) <= p.y <= max(a.y, b.y))    # comment out both to check collinear
    return True # for colinear (remove above)

a = Vec(0, 0)
b = Vec(1000, 2000)
p = Vec(-1, -2)
print(is_on_segment(p, a, b))