import functools
import sys


def notmultipleOf3or5(x):
    return (x % 3 == 0) or (x % 5 == 0)


def sumdigit(sum, x):
    if x < 1:
        return sum
    else:
        sum = sum + (x % 10)
        x = int(x/10)
        return sumdigit(sum, x)


def numofdigit(sum, x):
    if x < 1:
        return sum
    else:
        sum = sum + 1
        x = x//10
        return numofdigit(sum, x)


def iterativenumofdigit(x):
    sum = 0
    while x >= 1:
        sum = sum + 1
        x = x // 10
    return sum


def fibonacci():
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c


def iteratorfibonacci():
    fibonacci1 = fibonacci()
    value = next(fibonacci1)
    while iterativenumofdigit(value) < 1000:
        value = next(fibonacci1)
    return value


def recfibonacci(a, b):
    if numofdigit(0, b) >= 1000:
        return b
    else:
        c = a + b
        b = c
        a = b
        return recfibonacci(a, b)


def isPrime(count, i, x):
    if(x % i == 0):
        count += 1
    i += 1
    if count > 1 and i > (x//2):
        return False
    elif count == 1 and i > (x//2):
        return True
    else:
        return isPrime(count, i, x)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    # 1 exercise
    print(sum(list(filter(notmultipleOf3or5, range(1, 1000)))))
    # 2 exercise
    print([(isPrime(0, 1, x), x) for x in range(2, 21)])
    print(list(filter(lambda x: isPrime(0, 1, x), range(2, 20))))
    print(functools.reduce(lambda z, y: z*y, filter(lambda x: isPrime(0, 1, x),
          range(2, 20))))
    # 3 exercise
    print(sumdigit(0, 2**1000))
    # 4 fibonacci
    first = recfibonacci(0, 1)
    second = iteratorfibonacci()
    print(numofdigit(0, 2**1000))
    print(recfibonacci(0, 1))
    print(iteratorfibonacci())
