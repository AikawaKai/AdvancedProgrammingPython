def identity(size):
    return([[1 if x == y else 0 for x in range(size)] for y in range(size)])


def square(n):
    return [[x+y*n for x in range(1, n+1)] for y in range(0, n)]


def transpose(matrix):
    return [[matrix[y][x] for y in range(len(matrix))]
            for x in range(len(matrix[0]))]


def sumprodcolumn(column1, column2):
    return sum([column1[i] * column2[i] for i in range(len(column1))])


def multiply(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        matrix2t = transpose(matrix2)
        return [[sumprodcolumn(matrix1[i], matrix2t[j])
                 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    elif len(matrix2[0]) == len(matrix1):
        matrix1t = transpose(matrix1)
        return [[sumprodcolumn(matrix2[i], matrix1t[j])
                 for j in range(len(matrix1[0]))] for i in range(len(matrix2))]
    else:
        return []


if __name__ == '__main__':
    matA = [[1, 0, 2], [0, 3, -1]]
    matB = [[4, 1], [-2, 2], [0, 3]]
    column1 = [1, 1, 1, 1, 1]
    column2 = [1, 2, 3, 4, 5]
    identitymatrix = identity(10)
    squaren = square(11)
    M1 = [[1, 2, 3], [4, 5, 6]]
    M2 = [[7, 8], [9, 10], [11, 12]]
    for x in identitymatrix:
        print(x)
    for x in squaren:
        print(x)
    tran = transpose(squaren)
    for x in tran:
        print(x)
    tran1 = transpose(matA)
    for x in tran1:
        print(x)
    for x in matB:
        print(x)
    print(sumprodcolumn(column1, column2))
    multiplied = multiply(matA, matB)
    for x in multiplied:
        print(x)
    multiplied1 = multiply(matB, matA)
    for x in multiplied1:
        print(x)
    multiplied2 = multiply(M1, M2)
    for x in multiplied2:
        print(x)
    multiplied3 = multiply(M2, M1)
    for x in multiplied3:
        print(x)
