class GeometricObject:
    def __init__(self):
        pass


class Point(GeometricObject):
    def __init__(self, x, y):
        GeometricObject.__init__(self)  # Явный вызов конструктора GeometricObject
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line(GeometricObject):
    def __init__(self, slope, intercept):
        GeometricObject.__init__(self)  # Явный вызов конструктора GeometricObject
        self.slope = slope
        self.intercept = intercept

    def __repr__(self):
        return f"Line(y = {self.slope}x + {self.intercept})"


class FlatShape(GeometricObject):
    def __init__(self):
        GeometricObject.__init__(self)  # Явный вызов конструктора GeometricObject


class Ray(Point, Line):
    def __init__(self, x, y, slope, intercept):
        # Явные вызовы конструкторов родительских классов
        Point.__init__(self, x, y)  # Для Point
        Line.__init__(self, slope, intercept)  # Для Line

    def __repr__(self):
        return f"Ray starting at {Point.__repr__(self)} along {Line.__repr__(self)}"


class Segment(Point, Line):
    def __init__(self, x1, y1, x2, y2):
        # Явный вызов конструктора Point
        Point.__init__(self, x1, y1)
        # Вычисляем slope (наклон) и intercept (смещение) для Line
        slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')  # Наклон
        intercept = y1 - slope * x1 if slope != float('inf') else None  # Смещение
        Line.__init__(self, slope, intercept)  # Для Line
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Segment from ({self.x}, {self.y}) to ({self.x2}, {self.y2})"


class Polygon(FlatShape):
    def __init__(self, vertices):
        FlatShape.__init__(self)  # Явный вызов конструктора FlatShape
        self.vertices = vertices

    def __repr__(self):
        return f"Polygon with vertices {self.vertices}"


class Rectangle(Polygon):
    def __init__(self, width, height):
        # Создаем вершины прямоугольника
        vertices = [(0, 0), (width, 0), (width, height), (0, height)]
        Polygon.__init__(self, vertices)  # Явный вызов конструктора Polygon
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height})"


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)  # Явный вызов конструктора Rectangle

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