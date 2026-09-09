from c import *

def simple_polygon(points):

    # find lowest point
    p0 = min(points, key=lambda p: (p.y, p.x))

    # sort rest by check for val against p
    others = [p for p in points if p!= 0]
    others.sort(key=lambda p: PointSortKey(p0, p))

    #
    return others

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]

i = 0
verts = simple_polygon(points)
for v in verts:
    print(f"point {i} at {v}")
    i += 1


import matplotlib.pyplot as plt

def plot_poly(points):
    """Plot the given set of points as a closed polygon"""
    plt.plot([v.x for v in points + [points[0]]], [v.y for v in points + [points[0]]])
    plt.show()

plot_poly(points)