class GeometricObject:
    def __init__(self):
        pass

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line(GeometricObject):
    def __init__(self, slope, intercept):
        super().__init__()
        self.slope = slope
        self.intercept = intercept

    def __repr__(self):
        return f"Line(y = {self.slope}x + {self.intercept})"

class FlatShape(GeometricObject):
    def __init__(self):
        super().__init__()

class Ray(Point, Line):
    def __init__(self, x, y, slope, intercept):
        Point.__init__(self, x, y)
        Line.__init__(self, slope, intercept)

    def __repr__(self):
        return f"Ray starting at {Point.__repr__(self)} along {Line.__repr__(self)}"

class Segment(Point, Line):
    def __init__(self, x1, y1, x2, y2):
        Point.__init__(self, x1, y1)
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Segment({self.x}, {self.y}) to ({self.x2}, {self.y2})"

class Polygon(FlatShape):
    def __init__(self, vertices):
        super().__init__()
        self.vertices = vertices

    def __repr__(self):
        return f"Polygon with vertices {self.vertices}"

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([(0, 0), (width, 0), (width, height), (0, height)])
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square({self.width})"

# Пример использования:
p1 = Point(1, 2)
l1 = Line(1, 0)
r1 = Ray(0, 0, 1, 1)
s1 = Segment(0, 0, 3, 4)
poly = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
rect = Rectangle(4, 3)
sq = Square(2)

print(p1)
print(l1)
print(r1)
print(s1)
print(poly)
print(rect)
print(sq)
