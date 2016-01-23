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

    def getLenRow(self):
        return self.n

    def getLenColumn(self):
        return self.m

    def __add__(self, other):
        if self.getLenRow() == other.getLenRow() and self.getLenColumn() == other.getLenColumn():
            otherM = other.getMatrix()
            matrix = [[self.matrix[i][j] + otherM[i][j] for j in range(self.getLenColumn())] for i in range(self.getLenRow())]
            return Matrix(matrix)
        raise ValueError("Matrix are not compatible for the sum operation")

    def __mul__(self, other):
        if isinstance(other, int):
            return self._mul(other)
        if isinstance(other, Matrix):
            return self._mulM(other)
        raise ValueError("Stai moltiplicando per un valore non concesso")

    def _mul(self, other):
        return [[self.matrix[i][j] * other for j in range(self.getLenColumn())] for i in range(self.getLenRow())]

    def __eq__(self, othermatrix):
        return True if self.matrix == othermatrix.getMatrix() else False

    def __ne__(self, othermatrix):
        return True if not self.__eq__(othermatrix) else False

    def cp(self):
        matrixCp = copy.deepcopy(self.matrix)
        return Matrix(matrixCp)


if __name__ == '__main__':
    try:
        listOfRow = [[1, 2, 3], [2, 3, 6], [3, 6, 7]]
        matrix1 = Matrix(listOfRow)
        listOfRow = [[1, 2, 3], [2, 6], [3, 6, 7]]
        matrix2 = Matrix(listOfRow)
    except:
        pass
    matrix4 = Matrix([[1, 3, 4, 5], [1, 3, 4, 5]])
    print(matrix1.getMatrix())
    matrix3 = matrix1.cp()
    matrix = matrix3.getMatrix()
    matrix[1][0] = 3
    print(matrix)
    print(matrix1.getMatrix())
    print(matrix3.getMatrix())  # reference to matrix
    print((matrix3 + matrix1).getMatrix())
    print(matrix1 * 3)
