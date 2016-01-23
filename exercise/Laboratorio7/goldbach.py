from math import sqrt
from itertools import combinations_with_replacement as comb


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)+1), 2):  # sqrt+1 altrimenti mi perdo i quadrati perfetti
        if n % i == 0:
            return False
    return True


class GeneratePrime(object):

    def __init__(self, maximum):
        self.number = 0
        self.index = 0
        self.cache = []
        self.maximum = maximum

    def __iter__(self):
        self.index = 0
        return self

    def getCache(self):
        return self.cache

    def __next__(self):
        if self.number > self.maximum:
            raise StopIteration
        if len(self.cache) > self.index:
            toReturn = self.cache[self.index]
            self.index += 1
            return toReturn
        while(not isPrime(self.number)):
            self.number += 1
        toReturn = self.number
        self.cache.append(toReturn)
        self.number += 1
        self.index += 1
        return toReturn

iterator = GeneratePrime(100)


def goldbach(n):
    listOfPrimeToN = []
    for num in iterator:
        if num >= n:
            break
        listOfPrimeToN.append(num)
    listToCheck = list(comb(listOfPrimeToN, 2))
    for elem in listToCheck:
        if elem[0] + elem[1] == n:
            return elem


def goldbach_list(n, m):
    listOfEven = [num for num in range(n, m) if num % 2 == 0]
    dictGoldBach = dict()
    for elem in listOfEven:
        (num1, num2) = goldbach(elem)
        dictGoldBach[elem] = "{0} = {1} + {2}".format(elem, num1, num2)
    return dictGoldBach



if __name__ == '__main__':
    print(list(filter(isPrime, [elem for elem in range(0, 100)])))
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(12))
    print(goldbach_list(4, 100))
