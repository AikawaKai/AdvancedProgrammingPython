import copy


class Matrix(object):

    def __init__(self, listOfRow):
        n = len(listOfRow)
        if n == 0:
            raise ValueError("Matrice Vuota")
        rowLen = len(listOfRow[0])
        for i in range(1, len(listOfRow)):
            if len(listOfRow[i]) != rowLen:
                raise ValueError("Matrice non conforme")
        for row in listOfRow:
            for value in row:
                if not isinstance(value, int):
                    raise ValueError("Matrice con valore non interi")
        self.matrix = listOfRow
        self.n = n
        self.m = rowLen

    def getMatrix(self):
        return self.matrix

    def getNumRow(self):
        return self.n

    def getNumColumn(self):
        return self.m

    def __add__(self, other):
        if self.getNumRow() == other.getNumRow() and self.getNumColumn() == other.getNumColumn():
            otherM = other.getMatrix()
            matrix = [[self.matrix[i][j] + otherM[i][j] for j in range(self.getNumColumn())] for i in range(self.getNumRow())]
            return Matrix(matrix)
        raise ValueError("Matrix are not compatible for the sum operation")

    def __mul__(self, other):
        if isinstance(other, int):
            return self._mul(other)
        if isinstance(other, Matrix):
            return self._mulM(other)
        raise ValueError("Stai moltiplicando per un valore non concesso")

    def _mul(self, other):
        return Matrix([[self.matrix[i][j] * other for j in range(self.getNumColumn())] for i in range(self.getNumRow())])

    def _mulM(self, matrix):
        if not self.getNumColumn() == matrix.getNumRow():
            raise ValueError("Operazione non concessa")
        matrixO = matrix.getMatrix()
        gC = Matrix._getColumn
        mV = Matrix._mulTwoVectors
        return Matrix([[mV(self.matrix[i], gC(matrixO, j)) for j in
                      range(matrix.getNumColumn())] for i in
                      range(self.getNumRow())])

    def _getColumn(matrix, j):
        return [matrix[i][j] for i in range(len(matrix))]

    def _mulTwoVectors(vect1, vect2):
        return sum([vect1[i]*vect2[i] for i in range(len(vect1))])

    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(self.getNumRow())] for i in range(self.getNumColumn())])

    def matrix1norm(self):
        matrixAbs = [[abs(self.matrix[i][j]) for j in range(self.getNumColumn())] for i in range(self.getNumRow())]
        columns = [Matrix._getColumn(matrixAbs, j) for j in range(self.getNumColumn())]
        return max(sum(columns[i]) for i in range(self.getNumColumn()))

    def __eq__(self, othermatrix):
        return True if self.matrix == othermatrix.getMatrix() else False

    def __ne__(self, othermatrix):
        return True if not self.__eq__(othermatrix) else False

    def cp(self):
        matrixCp = copy.deepcopy(self.matrix)
        return Matrix(matrixCp)

    def __repr__(self):
        return "Matrix({0})".format(repr(self.matrix))


if __name__ == '__main__':
    try:
        listOfRow = [[1, 2, 3], [2, 3, 6], [3, 6, 7]]
        matrix1 = Matrix(listOfRow)
        listOfRow = [[1, 2, 3], [2, 6], [3, 6, 7]]
        matrix2 = Matrix(listOfRow)
    except:
        pass
    matrix4 = Matrix([[1, 3, 4, 5], [1, 3, 4, 5]])
    matrix5 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
    #  print(matrix1.getMatrix())
    matrix3 = matrix1.cp()
    matrix = matrix3.getMatrix()
    matrix[1][0] = 3
    # print(matrix)
    print(matrix1.getMatrix())
    print(matrix3.getMatrix())  # reference to matrix
    # print((matrix3 + matrix1).getMatrix())
    # print(matrix1 * 3)
    print((matrix1 * matrix3).getMatrix())  # ok
    print((matrix4 * matrix5).getMatrix())  # ok
    print((matrix5 * matrix4).getMatrix())  # ok
    #  print(matrix1 * matrix5) # ok
    print(matrix1.transpose().getMatrix())
    print(matrix4.transpose().getMatrix())
    print(matrix5.transpose().getMatrix())
    print((matrix5 * 2).getMatrix())
    print((matrix4 * 2).getMatrix())
    print(matrix4.matrix1norm())
    print(matrix5.matrix1norm())
    print(matrix1.matrix1norm())
    matrix6 = Matrix([[6, 7, 10], [5, 8, 3], [2, 4, 7], [3, 4, 3]])
    print(matrix6.matrix1norm())
    print(repr(matrix6))
    #  print(Matrix.getColumn(matrix1.getMatrix(), 0))
    #  print(matrix1 * 7.5)
