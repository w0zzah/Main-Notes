from c import Vec, signed_area, is_ccw

def classify_points(line_start, line_end, points):
    l = 0
    r = 0
    for point in points:
        if is_ccw(line_start, line_end, point):
            l += 1
        else:
            r += 1
    return (r, l)

points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]

print(classify_points(Vec(0, 49), Vec(100, 49), points))