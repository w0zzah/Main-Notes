from c import *


def is_strictly_convex(vertices):
    n = len(vertices)
    if n < 3:
        return False
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n] # Use mod to wrap around 
        if not is_ccw(a, b, c):
            return False
    return True

verts = [
    (60, 60),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))