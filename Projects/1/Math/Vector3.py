
import math

class Vector3:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def crossProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c
        d = self.d * v.d

        return Vector3(a,b,c,d)
    
    def dotProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c
        d = self.d * v.d

        return a + b + c + d
    
    def angleBetween(self, v):
        # arccos(dot/mag1*mag2)
        dot = self.dotProduct(v)
        mag1 = self.magnitude(sqrt=True)
        mag2 = v.magnitude(sqrt=True)
        quo = (dot/(mag1*mag2))

        return math.acos(quo)
    
    def add(self, v):
        a = self.a + v.a
        b = self.b + v.b
        c = self.c + v.c
        d = self.d + v.d

        return Vector3(a,b,c,d)
    
    def subtract(self, v):
        a = self.a - v.a
        b = self.b - v.b
        c = self.c - v.c
        d = self.d - v.d

        return Vector3(a,b,c,d)
    
    def normalize(self):
        mag = self.magnitude(sqrt=True)
        a = self.a / mag
        b = self.b / mag
        c = self.c / mag
        d = self.d / mag

        return Vector3(a,b,c,d)
    
    # with and without squareroot
    def magnitude(self, sqrt):
        a_2 = self.a * self.a
        b_2 = self.b * self.b
        c_2 = self.c * self.c
        d_2 = self.d * self.d

        sum = a_2 + b_2 + c_2 + d_2
        return math.sqrt(sum) if sqrt else sum
    
    def eq(self, v):
        a = self.a == v.a
        b = self.b == v.b
        c = self.c == v.c
        d = self.d == v.d

        return a and b and c and d