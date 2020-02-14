# Helper script for movement calculation with vectors
import math


class Vector2D:
    """Class utilitity for Vector objects operations"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    def __str__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def from_points(p1, p2):
        """Returns a new vector2d object with the subtracted values of the
        given as parameters points"""
        return Vector2D(p2[0] - p1[0], p2[1] - p1[1])

    def get_magnitute(self):
        """Calculate the magnitute of the vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitute()
        try:
            self.x /= magnitude
            self.y /= magnitude
        except ZeroDivisionError:
            self.x = 0
            self.y = 0

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value


if __name__ == '__main__':
    point_a = (10, 20)
    point_b = (20, 30)
    vector_ab = Vector2D.from_points(point_a, point_b)
    step = vector_ab * 0.1
    position = Vector2D(*point_a)
    for n in range(10):
        position += step
        print(position)
