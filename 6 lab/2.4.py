class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @classmethod
    def str_to_vector(self, str):
        x, y = [int(x) for x in str.split()]
        self.x = x
        self.y = y
        return Vector(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return "Вектор с координатами x = {};".format(self.x) + " y = {}".format(self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def sin_angle(self, other):
        return (1 - (self * other / (abs(self)) / (abs(other))) ** 2) ** 0.5

    def square(self, other):
        return Vector.sin_angle(self, other) * abs(self) * abs(other)


p = Vector.str_to_vector(input())
l = Vector.str_to_vector(input())

print(int(Vector.square(p, l)))
