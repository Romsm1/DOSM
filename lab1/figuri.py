class GeometricObject:
    pass

class Point(GeometricObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(GeometricObject):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # первая точка
        self.y1 = y1
        self.x2 = x2  # вторая точка
        self.y2 = y2

class Ray(GeometricObject):
    def __init__(self, x, y, dx, dy):
        self.x = x      # начальная точка
        self.y = y
        self.dx = dx    # направление по X
        self.dy = dy    # направление по Y

class Segment(GeometricObject):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # начало
        self.y1 = y1
        self.x2 = x2  # конец
        self.y2 = y2

class FlatShape(GeometricObject):
    pass

class Polygon(FlatShape):
    def __init__(self, points):  # список точек (x, y)
        self.points = points  # например (1, 1)

class Rectangle(FlatShape):
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)
