from Vector3 import Vector3

class Matrix:

    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def add(self, m1, m2):
        v1 = m1.v1.add(m1.v1, m2.v1)
        v2 = m1.v2.add(m1.v2, m2.v2)
        v3 = m1.v3.add(m1.v3, m2.v3)
        v4 = m1.v4.add(m1.v4, m2.v4)

        # return matrix
        return Matrix(v1,v2,v3,v4)
    
    def subtract(self, m1, m2):
        v1 = m1.v1.subtract(m1.v1, m2.v1)
        v2 = m1.v2.subtract(m1.v2, m2.v2)
        v3 = m1.v3.subtract(m1.v3, m2.v3)
        v4 = m1.v4.subtract(m1.v4, m2.v4)

        # return matrix
        return Matrix(v1,v2,v3,v4)
    
    def multiplyVM(self, v, m):
        mRows = self.getMatrixRows(m)
        a = v.dotProduct(v, mRows[0])
        b = v.dotProduct(v, mRows[1])
        c = v.dotProduct(v, mRows[2])
        d = v.dotProduct(v, mRows[3])

        # return vector
        return Vector3(a,b,c,d)
    
    def multiplyMM(self, m1, m2):
        m2Cols = [m2.v1, m2.v2, m2.v3, m2.v4]
        
        v1 = self.multiplyVM(m2Cols[0], m1)
        v2 = self.multiplyVM(m2Cols[1], m1)
        v3 = self.multiplyVM(m2Cols[2], m1)
        v4 = self.multiplyVM(m2Cols[3], m1)

        # return matrix
        return Matrix(v1,v2,v3,v4)

    def getMatrixRows(self, m1):
        r1 = Vector3(m1.v1.a, m1.v2.a, m1.v3.a, m1.v4.a)
        r2 = Vector3(m1.v1.b, m1.v2.b, m1.v3.b, m1.v4.b)
        r3 = Vector3(m1.v1.c, m1.v2.c, m1.v3.c, m1.v4.c)
        r4 = Vector3(m1.v1.d, m1.v2.d, m1.v3.d, m1.v4.d)
        return [r1,r2,r3,r4]


    def equal(self, m1, m2):
        v1 = m1.v1.eq(m2.v1)
        v2 = m1.v2.eq(m2.v2)
        v3 = m1.v3.eq(m2.v3)
        v4 = m1.v4.eq(m2.v4)

        # return boolean
        return v1 and v2 and v3 and v4
    
    