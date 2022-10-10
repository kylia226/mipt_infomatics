class Complex():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.y * other.x + other.y * self.x)

    def __truediv__(self, other):
        return Complex((self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2),
                       (self.y * other.x - other.y * self.x) / (other.x ** 2 + other.y ** 2))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

A = Complex(7, 2)
B = Complex(3, 6)
C = A + B
D = A - B
F = A * B
H = A / B
print(C.x, C.y)
print(D.x, D.y)
print(F.x, F.y)
print(H.x, H.y)
