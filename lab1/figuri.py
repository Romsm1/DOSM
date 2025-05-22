class GeometricObject:
    def __init__(self, name="GeometricObject", color="black"):
        self.name = name
        self.color = color

class Point(GeometricObject):
    def __init__(self, x, y, name="Point", color="black"):
        super().__init__(name, color)
        self.x = x
        self.y = y

class Line(GeometricObject):
    def __init__(self, x1, y1, x2, y2, name="Line", color="black"):
        super().__init__(name, color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Ray(GeometricObject):
    def __init__(self, x, y, dx, dy, name="Ray", color="black"):
        super().__init__(name, color)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Segment(GeometricObject):
    def __init__(self, x1, y1, x2, y2, name="Segment", color="black"):
        super().__init__(name, color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class FlatShape(GeometricObject):
    def __init__(self, name="FlatShape", color="black"):
        super().__init__(name, color)

class Polygon(FlatShape):
    def __init__(self, points, name="Polygon", color="black"):
        super().__init__(name, color)
        self.points = points

class Rectangle(FlatShape):
    def __init__(self, x, y, width, height, name="Rectangle", color="black"):
        super().__init__(name, color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, x, y, side, name="Square", color="black"):
        super().__init__(x, y, side, side, name, color)
