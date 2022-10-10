class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def hello(self, str):
        x, y, z = [int(x) for x in str.split()]
        self.x = x
        self.y = y
        self.z = z
        return Vector(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return "Вектор с координатами x = {};".format(self.x) + " y = {};".format(self.y) + " z = {}".format(self.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (0.5)

    @staticmethod
    def isMax(self, last):
        return int(self) > int(last)

n = int(input())
l = 0
max_len = 0
for i in range(n):
    p = Vector.hello(input())
    if Vector.isMax(abs(p), max_len):
        max_len = abs(p)
        l = p
print(l)
