from unittest import TestCase
from unittest import main


class SquareMatrix(object):

    def __init__(self, n):
        self.n = n
        self.matrix = [[0 if i != j else 1 for i in range(0, n)] for j in range(0, n)]
        print(self.matrix)

    def modifyPosition(self, i, j, value):
        self.matrix[i][j] = value

    def getMatrix(self):
        return self.matrix

    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]

    def sumByRow(self, i):
        return sum(self.matrix[i])

    def sumByColumn(self, _j):
        return sum([self.matrix[i][_j] for i in range(self.n)])


class testSquareMatrix(TestCase):

    def testInit(self):
        matrix = SquareMatrix(2)
        matrixArray = matrix.getMatrix()
        self.assertEqual(matrixArray, [[1, 0], [0, 1]])
        matrix = SquareMatrix(3)
        matrixArray = matrix.getMatrix()
        self.assertEqual(matrixArray, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def testTranspose(self):
        matrix = SquareMatrix(2)
        matrix.modifyPosition(1, 0, 2)
        matrix.transpose()
        matrixArray = matrix.getMatrix()
        self.assertEqual(matrixArray, [[1, 2], [0, 1]])
        matrix = SquareMatrix(3)
        matrix.modifyPosition(0, 1, 2)
        matrix.modifyPosition(0, 2, 8)
        matrix.modifyPosition(1, 0, 3)
        matrix.modifyPosition(1, 1, 4)
        matrix.modifyPosition(1, 2, 3)
        matrix.modifyPosition(2, 0, 5)
        matrix.modifyPosition(2, 1, 6)
        matrix.modifyPosition(2, 2, 1)
        matrix.transpose()
        matrixArray = matrix.getMatrix()
        self.assertEqual(matrixArray, [[1, 3, 5], [2, 4, 6], [8, 3, 1]])

    def testSumByRow(self):
        matrix = SquareMatrix(2)
        result = matrix.sumByRow(0)
        self.assertEqual(1, result)
        matrix = SquareMatrix(2)
        result = matrix.sumByColumn(0)
        self.assertEqual(1, result)
        matrix = SquareMatrix(2)
        result = matrix.sumByRow(1)
        self.assertEqual(1, result)
        matrix = SquareMatrix(2)
        result = matrix.sumByColumn(1)
        self.assertEqual(1, result)

if __name__ == '__main__':
    main()
