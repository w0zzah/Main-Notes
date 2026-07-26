class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def __mul__(self, scale):
        return Vec(self.x * scale, self.y * scale)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def lensq(self):
        return self.dot(self)
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

def signed_area(a, b, c):
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_ccw(a, b, c):
    area = signed_area(a, b, c)
    return area > 0

class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0

def simple_polygon(points):

    # find lowest point
    p0 = min(points, key=lambda p: (p.y, p.x))

    # sort rest by check for val against p
    others = [p for p in points if p!= 0]
    others.sort(key=lambda p: PointSortKey(p0, p))

    #
    return others