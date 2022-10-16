class Vector():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def str_to_vector(self, str):
        x, y, z = [int(x) for x in str.split()]
        self.x = x
        self.y = y
        self.z = z
        return Vector(self.x, self.y, self.z)

    def volume (self, other1, other2):
        import numpy as np
        a = []
        a.append((self.x, self.y, self.z))
        a.append((other1.x, other1.y, other1.z))
        a.append((other2.x, other2.y, other2.z))
        return  np.linalg.det(a)

p = Vector.str_to_vector(input())
l = Vector.str_to_vector(input())
f = Vector.str_to_vector(input())

print(abs(int(Vector.volume(p, l, f))))
