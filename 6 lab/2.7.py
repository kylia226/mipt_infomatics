class Vector():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @classmethod
    def str_to_vector(self, str):
        x, y, z = [int(x) for x in str.split()]
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

    def perimeter(self, other1, other2):
        return abs(self - other1) + abs(self - other2) + abs(other1 - other2)

    def square(self, other1, other2):
        return (Vector.perimeter(self, other1, other2)
                *(Vector.perimeter(self, other1, other2) - abs(self))
                *(Vector.perimeter(self, other1, other2) - abs(other2))
                *(Vector.perimeter(self, other1, other2) - abs(other1)))**0.5



n = int(input())
point_1 = Vector.str_to_vector(input())
point_2 = Vector.str_to_vector(input())
point_3 = Vector.str_to_vector(input())

for i in range(n-3):
    point_4 = Vector.str_to_vector(input())
    if Vector.square(point_1, point_2, point_4) > Vector.square(point_1, point_2, point_3):
        point_3 = point_4
    elif Vector.square(point_1, point_3, point_4) > Vector.square(point_1, point_2, point_3):
        point_2 = point_4
    elif Vector.square(point_2, point_3, point_4) > Vector.square(point_1, point_2, point_3):
        point_1 = point_4

print(point_1)
print(point_2)
print(point_3)
print("Максимальная площадь треугольника:", int(Vector.square(point_1, point_2, point_3)))
