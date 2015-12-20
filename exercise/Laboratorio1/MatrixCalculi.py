def identity(size):
    return([[1 if x==y else 0 for x in range(size)] for y in range(size)])


def square(n):
    return [[x+y*n for x in range(1, n+1)] for y in range(0, n)]

if __name__ == '__main__':
    print ([x*10 for x in range(10)])
    identitymatrix = identity(10)
    squaren = square(11)
    for x in identitymatrix:
        print(x)
    for x in squaren:
        print(x)
