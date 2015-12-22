#   INPUT MATRIX

#  0 0 0 0 1 1 1 1       #2 grey
#  0 0 0 0 1 1 1 1       #1 black
#  0 0 0 0 1 1 1 1       #0 white
#  0 0 0 0 1 1 1 1
#  0 0 1 1 0 0 0 0
#  0 1 1 1 1 1 0 0
#  0 1 1 1 1 0 0 0
#  0 0 1 1 1 1 0 0

#    QUADTREE
#                         [2]
#                       *
#                     *
#                   *
#                 *
#              [0]-------------------[1]-------------------[2]-------------------[2]
#                                                         *                      *
#                                                       *                      *
#                                                     *                      *
#                                                   *                      *
#                                                 [2]--[0]--[0]--[2]     [2]--[1]--[1]--[2]
#                                               *               *         *              *
#                                             *               *           *               *
#                                           *               *             *                *
#                                         *               *               *                 *
#                                       [0][0][1][1]   [1][0][1][1]      [0][0][1][0]       [0][1][0][0]


class quadtree:

    def __init__(self, value, son):
        self.value = value
        self.son = son

    def hasSon(self):
        if self.son is not None:
            return True
        else:
            return False

    def __str__(self):
        if self.son is not None:
            stringToPrint = "Value: " + str(self.value) + "\n1Child: " + str(self.son[0]) + " " + "2Child: " + str(self.son[1]) + " " + "3Child: " + str(self.son[2]) + " " + "4Child: " + str(self.son[3])
            return stringToPrint
        else:
            return "Value: " + str(self.value) + "\n"


def getMatrixFromVector(vector):
    n = int(pow(len(vector), 1/2))
    return [vector[size:size+n] for size in [n*i for i in range(n)]]


def getSubMatrixFromMatrix(matrix):
    n = len(matrix)
    matrix1 = [matrix[i][0:int(n/2)] for i in range(int(n/2))]
    matrix2 = [matrix[i][int(n/2):n] for i in range(int(n/2))]
    matrix3 = [matrix[i][0:int(n/2)] for i in range(int(n/2), n)]
    matrix4 = [matrix[i][int(n/2):n] for i in range(int(n/2), n)]
    return (matrix1, matrix2, matrix3, matrix4)


vector = [0, 0, 0, 0, 1, 1, 1, 1,
          0, 0, 0, 0, 1, 1, 1, 1,
          0, 0, 0, 0, 1, 1, 1, 1,
          0, 0, 0, 0, 1, 1, 1, 1,
          0, 0, 1, 1, 0, 0, 0, 0,
          0, 1, 1, 1, 1, 1, 0, 0,
          0, 1, 1, 1, 1, 0, 0, 0,
          0, 0, 1, 1, 1, 1, 0, 0]


def recursionQuadTree(matrix):
    if len(matrix) > 1:
        (matrix1, matrix2, matrix3, matrix4) = getSubMatrixFromMatrix(matrix)
        q1 = recursionQuadTree(matrix1)
        q2 = recursionQuadTree(matrix2)
        q3 = recursionQuadTree(matrix3)
        q4 = recursionQuadTree(matrix4)
        if q1.value == q2.value == q3. value == q4.value:
            return quadtree(q1.value, None)
        else:
            return quadtree(2, [q1, q2, q3, q4])
    else:
        return quadtree(matrix[0][0], None)


if __name__ == '__main__':
    matrix = getMatrixFromVector(vector)
    print(matrix)
    submatrix = getSubMatrixFromMatrix(matrix)
    print(submatrix)
    quadtreestruct = recursionQuadTree(matrix)
    print(quadtreestruct)
