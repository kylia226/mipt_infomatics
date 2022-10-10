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


A = Vector.hello("7 2 6")
B = Vector(3, 6, 11)
C = A + B
D = A - B
F = A * B
print(C.x, C.y, C.z)
print(D.x, D.y, D.z)
print(F)
print(A)
