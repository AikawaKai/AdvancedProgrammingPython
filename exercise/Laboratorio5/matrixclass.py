class SquareMatrix(object):

    def __init__(self, n):
        self.n = n
        self.matrix = [[0 if i != j else 1 for i in range(0, n)] for j in range(0, n)]

    def modifyPosition(self, i, j, value):
        self.matrix[i][j] = value

    def getMatrix(self):
        return self.matrix

    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]

    def sumByRow(self, i):
        return SquareMatrix._sumByRow(self.matrix, i)

    def sumByColumn(self, _j):
        return SquareMatrix._sumByColumn(self.matrix, _j)

    def _sumByRow(matrix, i):
        return sum(matrix[i])

    def _sumByColumn(matrix, _j):
        return sum([matrix[i][_j] for i in range(len(matrix))])

    def determ(self):
        return SquareMatrix._ricDeterm(self.matrix)

    def _ricDeterm(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return SquareMatrix._det2(matrix)
        elif len(matrix) == 3:
            return SquareMatrix._det3(matrix)
        else:
            for i in range(len(matrix)):
                if SquareMatrix._sumByRow(matrix, i) == 0 or SquareMatrix._sumByColumn(matrix, i) == 0:
                    return 0
            detsum = 0
            for i in range(len(matrix)):
                detsum += ((-1)**(i)) * matrix[0][i] * SquareMatrix._ricDeterm(SquareMatrix._subMatrix(matrix, 0, i))
            return detsum

    def _det2(matrix):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    def _det3(matrix):
        elem1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
        elem2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
        elem3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
        part1 = elem1 + elem2 + elem3
        elem1 = matrix[2][0]*matrix[1][1]*matrix[0][2]
        elem2 = matrix[2][1]*matrix[1][2]*matrix[0][0]
        elem3 = matrix[1][0]*matrix[0][1]*matrix[2][2]
        part2 = elem1 + elem2 + elem3
        return part1 - part2

    def _subMatrix(matrix, i, j):
        newmatrix = [matrix[_i] for _i in range(len(matrix)) if _i != i]
        newmatrix = [[newmatrix[_i][_j] for _j in range(len(newmatrix[_i])) if _j != j] for _i in range(len(newmatrix))]
        return newmatrix
