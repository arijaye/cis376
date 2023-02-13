from Vector3 import Vector3

""" Matrix class; represents 4x4 matrix.

Attributes:
    v1: first vector of matrix (col 1)
    v2: second vector of matrix (col 2)
    v3: third vector of matrix (col 3)
    v4: fourth vector of matrix (col 4)
"""
class Matrix:
    """Initializes Matrix
    Args:
        v1: first vector of matrix (col 1)
        v2: second vector of matrix (col 2)
        v3: third vector of matrix (col 3)
        v4: fourth vector of matrix (col 4)

    Returns:
        a new Matrix object
    """
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4


    """Add two Matrices
    Args:
        m1: 1st Matrix to add
        m2: 2nd Matrix to add
    Returns:
        a new Matrix with sum
    """
    def add(self, m1, m2):
        v1 = m1.v1.add(m1.v1, m2.v1)
        v2 = m1.v2.add(m1.v2, m2.v2)
        v3 = m1.v3.add(m1.v3, m2.v3)
        v4 = m1.v4.add(m1.v4, m2.v4)

        # return matrix
        return Matrix(v1,v2,v3,v4)
    

    """Subtract two Matrices
    Args:
        m1: 1st Matrix to subtract
        m2: 2nd Matrix to subtract
    Returns:
        a new Matrix with difference
    """
    def subtract(self, m1, m2):
        v1 = m1.v1.subtract(m1.v1, m2.v1)
        v2 = m1.v2.subtract(m1.v2, m2.v2)
        v3 = m1.v3.subtract(m1.v3, m2.v3)
        v4 = m1.v4.subtract(m1.v4, m2.v4)

        # return matrix
        return Matrix(v1,v2,v3,v4)
    

    """Multiply Vector3 by Matrix
    Args:
        v: Vector3 to multiply
        m: Matrix to multiply
    Returns:
        a new Vector3 with product
    """
    def multiplyVM(self, v, m):
        mRows = self.getMatrixRows(m)
        a = v.dotProduct(v, mRows[0])
        b = v.dotProduct(v, mRows[1])
        c = v.dotProduct(v, mRows[2])
        d = v.dotProduct(v, mRows[3])

        # return vector
        return Vector3(a,b,c,d)
    

    """Multiply two Matrices
    Args:
        m1: 1st Matrix to multiply
        m2: 2nd Matrix to multiply
    Returns:
        a new Matrix with product
    """
    def multiplyMM(self, m1, m2):
        m2Cols = [m2.v1, m2.v2, m2.v3, m2.v4]
        
        v1 = self.multiplyVM(m2Cols[0], m1)
        v2 = self.multiplyVM(m2Cols[1], m1)
        v3 = self.multiplyVM(m2Cols[2], m1)
        v4 = self.multiplyVM(m2Cols[3], m1)

        # return matrix
        return Matrix(v1,v2,v3,v4)


    """Get rows of matrix
    Args:
        m: Matrix to extract rows from
    Returns:
        list of Vector3s representing rows
        of Matrix
    """
    def getMatrixRows(self, m):
        r1 = Vector3(m.v1.a, m.v2.a, m.v3.a, m.v4.a)
        r2 = Vector3(m.v1.b, m.v2.b, m.v3.b, m.v4.b)
        r3 = Vector3(m.v1.c, m.v2.c, m.v3.c, m.v4.c)
        r4 = Vector3(m.v1.d, m.v2.d, m.v3.d, m.v4.d)
        return [r1,r2,r3,r4]


    """Check if two Matrices are equal
    Args:
        m1: 1st Matrix to check
        m2: 2nd Matrix to check
    Returns:
        boolean; true if equal, false if not
    """
    def equal(self, m1, m2):
        v1 = m1.v1.eq(m2.v1)
        v2 = m1.v2.eq(m2.v2)
        v3 = m1.v3.eq(m2.v3)
        v4 = m1.v4.eq(m2.v4)

        # return boolean
        return v1 and v2 and v3 and v4
    
    