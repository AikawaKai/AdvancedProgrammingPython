import sys
from math import *
from functools import reduce


def recursiveSumFigureNum(number):
    if number < 1:
        return 0
    else:
        return recursiveSumFigureNum(number//10) + (number % 10)


def recursiveSumFigureNumAccum(acc, number):
    if number < 1:
        return acc
    else:
        newacc = acc + (number % 10)
        return recursiveSumFigureNumAccum(newacc, number//10)


def recursiveSumDigitNumAccum(acc, number):
    if number < 1:
        return acc
    else:
        newacc = acc + 1
        return recursiveSumDigitNumAccum(newacc, number//10)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fibacc(a, b, n):
    if n == 0:
        return b
    else:
        c = a + b
        return fibacc(b, c, n-1)

if __name__ == '__main__':
    sys.setrecursionlimit(5000)

    # 1
    func = lambda x: not(x % 3) or not(x % 5)
    multipleof3or5 = list(filter(func, [x for x in range(0, 1001)]))
    totalsum = sum(multipleof3or5)
    print(multipleof3or5, totalsum)

    # 2
    listOfUtilNumber = range(2, 21)
    # prime number
    for i in range(2, 10):
        listOfUtilNumber = list(filter((lambda x: x % i if x != i else True),
                                listOfUtilNumber))
    print(listOfUtilNumber)
    # max exponent for prime
    listOfUtilNumber = list(map(lambda x: int(pow(x, floor(log(20)/log(x)))),
                            listOfUtilNumber))
    print(listOfUtilNumber)
    print(reduce(lambda x, y: x*y, listOfUtilNumber))

    # 3
    print(recursiveSumFigureNum(11127))
    print(recursiveSumFigureNumAccum(0, 11127))
    print(recursiveSumDigitNumAccum(0, 111278))
    print(fib(7))
    numofdigit = 0
    num = 0
    while numofdigit != 1000:
        num += 1
        numofdigit = recursiveSumDigitNumAccum(0, fibacc(0, 1, num))
    print(num)
