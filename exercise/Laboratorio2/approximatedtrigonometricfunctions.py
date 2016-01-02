from math import sin


def factorialGen(x, count):
    while True:
        yield x
        count += 1
        x = x * count


def getArrayPosNeg(n):
    posneg = [1, -1]
    arrayposneg = []
    for i in range((n//2)+1):
        arrayposneg += posneg
    return arrayposneg


def senTaylor(number, n):
    arrayposneg = getArrayPosNeg(n)
    iterator = factorialGen(1, 0)
    TaylorSeries = [pow(number, x) for x in range(0, (n*2)) if x % 2 != 0]
    factorial = [next(iterator) for x in range(0, (n*2))]
    factorial = [factorial[i] for i in range(len(factorial)) if i % 2 != 0]
    TaylorSeries = [(TaylorSeries[i] * arrayposneg[i])/factorial[i]
                    for i in range(n)]
    return sum(TaylorSeries)


if __name__ == '__main__':
    num = float(input("Inserisci il numero da confrontare: "))
    numVal = int(input("numero di valori: "))
    print("Seno con taylor: {0} \
          Seno con Math: {1}".format(senTaylor(num, numVal), sin(num)))
