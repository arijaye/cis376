import math

class Vector2:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def crossProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c

        # return vector
        return Vector2(a,b,c)
    
    def dotProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c

        # return scalar
        return a + b + c
    
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

        return Vector2(a,b,c)
    
    def subtract(self, v):
        a = self.a - v.a
        b = self.b - v.b
        c = self.c - v.c

        return Vector2(a,b,c)
    
    def normalize(self):
        mag = self.magnitude(sqrt=True)
        a = self.a / mag
        b = self.b / mag
        c = self.c / mag

        return Vector2(a,b,c)
    
    # with and without squareroot
    def magnitude(self, sqrt):
        a_2 = self.a * self.a
        b_2 = self.b * self.b
        c_2 = self.c * self.c

        sum = a_2 + b_2 + c_2
        return math.sqrt(sum) if sqrt else sum
    
    def eq(self, v):
        a = self.a == v.a
        b = self.b == v.b
        c = self.c == v.c

        return a and b and c