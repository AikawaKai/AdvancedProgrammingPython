from unittest import TestCase
from unittest import main
from matrixclass import *


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

    def testDeterminante(self):
        matrix = SquareMatrix(3)
        matrix.modifyPosition(1, 1, 0)
        det = matrix.determ()
        self.assertEqual(0, det)
        matrix = SquareMatrix(3)
        det = matrix.determ()
        self.assertEqual(1, det)
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
        det = matrix.determ()
        self.assertEqual(-6, det)
        matrix = SquareMatrix(4)
        matrix.modifyPosition(1, 0, 3)
        matrix.modifyPosition(1, 2, 3)
        matrix.modifyPosition(2, 0, 2)
        matrix.modifyPosition(2, 3, 5)
        matrix.modifyPosition(0, 3, 3)
        matrix.modifyPosition(3, 0, 3)
        det = matrix.determ()
        self.assertEqual(-8, det)

if __name__ == '__main__':
    main()
    #  print(SquareMatrix.subMatrix([[1, 3, 5], [2, 4, 6], [8, 3, 1]], 0, 1))
