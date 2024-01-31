import numbers

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            pass
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Vector):
            pass
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            pass
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            pass
        self.x *= other
        self.y *= other

        return self