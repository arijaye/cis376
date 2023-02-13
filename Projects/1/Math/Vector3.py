
import math

""" Vector3 class; represents 4 point vector.

Attributes:
    a: x value of vector
    b: y value of vector
    c: z value of vector
    d: w value of vector
"""
class Vector3:
    """Initializes Vector3
    Args:
        a: x value of vector
        b: y value of vector
        c: z value of vector
        d: w value of vector

    Returns:
        a new Vector3 object
    """
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    """Gets cross product of two Vector3s
    Args:
        v: Vector3 to multiply this by
    Returns:
        a new Vector3 object
    """
    def crossProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c
        d = self.d * v.d

        return Vector3(a,b,c,d)
    
  
    """Gets dot product of two Vector3s
    Args:
        v: Vector3 to multiply this by
    Returns:
        a new Vector3 object
    """
    def dotProduct(self, v):
        a = self.a * v.a
        b = self.b * v.b
        c = self.c * v.c
        d = self.d * v.d

        return a + b + c + d
    
    
    """Gets angle between two Vector3s
    Args:
        v: Vector3 to get angle between
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
    
   
    """Add two Vector3s
    Args:
        v: Vector3 to add
    Returns:
        a new Vector3 with sum
    """
    def add(self, v):
        a = self.a + v.a
        b = self.b + v.b
        c = self.c + v.c
        d = self.d + v.d

        return Vector3(a,b,c,d)
    
    
    """Subtract two Vector3s
    Args:
        v: Vector3 to subtract
    Returns:
        a new Vector3 with difference
    """
    def subtract(self, v):
        a = self.a - v.a
        b = self.b - v.b
        c = self.c - v.c
        d = self.d - v.d

        return Vector3(a,b,c,d)
    
    
    """Normalize this Vector3
    Returns:
        normalized version of this
    """
    def normalize(self):
        mag = self.magnitude(sqrt=True)
        a = self.a / mag
        b = self.b / mag
        c = self.c / mag
        d = self.d / mag

        return Vector3(a,b,c,d)
    
   
    """Get magintude of this Vector3
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
        d_2 = self.d * self.d

        sum = a_2 + b_2 + c_2 + d_2
        return math.sqrt(sum) if sqrt else sum
    

    """Check if two vectors are equal
    Args:
        v: Vector3 to compare this to
    Returns:
        boolean; true if equal, false if not
    """
    def eq(self, v):
        a = self.a == v.a
        b = self.b == v.b
        c = self.c == v.c
        d = self.d == v.d

        return a and b and c and d