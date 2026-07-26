from c import *

def graham_scan(points):
    # Get list from closest to furtehrest
    polygon = simple_polygon(points)
    stack = []
    for p in polygon:
        # for each point on the graph, find next closest point till end
        while len(stack) >= 2:

            a = stack[-2]
            b = stack[-1]
            cross = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x) # cross product shows if right turn or colinear
            if cross <= 0: # if its either then there is another point that has a shorter path
                stack.pop()
            else:
                break
        stack.append(p)
    
    return stack

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = graham_scan(points)
for v in verts:
    print(v)

import matplotlib.pyplot as plt

def plot_hull(points, hull):
    """Plot the given set of points and the computed convex hull"""
    plt.scatter([p.x for p in points], [p.y for p in points])
    plt.plot([v.x for v in hull + [hull[0]]], [v.y for v in hull + [hull[0]]])
    plt.show()

plot_hull(points, verts)