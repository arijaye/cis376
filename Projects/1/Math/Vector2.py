import math

""" Vector2 class; represents 3 point vector.

Attributes:
    a: x value of vector
    b: y value of vector
    c: z value of vector
"""
class Vector2:
    """Initializes Vector2
    Args:
        a: x value of vector
        b: y value of vector
        c: z value of vector

    Returns:
        a new Vector2 object
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    """Gets cross product of two Vector2s
    Args:
        v: Vector2 to multiply this by
    Returns:
        a new Vector2 object
    """
    def crossProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c

        # return vector
        return Vector2(a,b,c)
    

    """Gets dot product of two Vector2s
    Args:
        v: Vector2 to multiply this by
    Returns:
        a new Vector2 object
    """
    def dotProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c

        # return scalar
        return a + b + c
    

    """Gets angle between two Vector2s
    Args:
        v: Vector2 to get angle between
    Returns:
        angle in radians between this and v
    """
    def angleBetween(self, v):
        # arccos(dot/mag1*mag2)
        dot = self.dotProduct(v)
        mag1 = self.magnitude(sqrt=True)
        mag2 = v.magnitude(sqrt=True)
        quo = (dot/(mag1*mag2))

        return math.acos(quo)
    

    """Add two Vector2s
    Args:
        v: Vector2 to add
    Returns:
        a new Vector2 with sum
    """
    def add(self, v):
        a = self.a + v.a
        b = self.b + v.b
        c = self.c + v.c

        return Vector2(a,b,c)
    

    """Subtract two Vector2s
    Args:
        v: Vector2 to subtract
    Returns:
        a new Vector2 with difference
    """
    def subtract(self, v):
        a = self.a - v.a
        b = self.b - v.b
        c = self.c - v.c

        return Vector2(a,b,c)
    

    """Normalize this Vector2
    Returns:
        normalized version of this
    """
    def normalize(self):
        mag = self.magnitude(sqrt=True)
        a = self.a / mag
        b = self.b / mag
        c = self.c / mag

        return Vector2(a,b,c)
    

    """Get magintude of this Vector2
    Args:
        sqrt: boolean determining if square root is 
            included in returned maginitude
    Returns:
        magnitude of this
    """
    def magnitude(self, sqrt):
        a_2 = self.a * self.a
        b_2 = self.b * self.b
        c_2 = self.c * self.c

        sum = a_2 + b_2 + c_2
        return math.sqrt(sum) if sqrt else sum
    

    """Check if two vectors are equal
    Args:
        v: Vector2 to compare this to
    Returns:
        boolean; true if equal, false if not
    """
    def eq(self, v):
        a = self.a == v.a
        b = self.b == v.b
        c = self.c == v.c

        return a and b and c