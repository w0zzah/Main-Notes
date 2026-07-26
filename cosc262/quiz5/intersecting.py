from c import Vec, is_ccw, signed_area

def intersecting(a, b, c, d):

    return is_ccw(a, d, b) != is_ccw(a, c, b) and is_ccw(c, a, d) != is_ccw(c, b, d)
    


a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(99, 1)
d = Vec(99, -1)
print(intersecting(a, b, c, d))