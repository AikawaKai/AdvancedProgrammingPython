from math import sqrt


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
        if num > n:
            break
        listOfPrimeToN.append(num)
    print(listOfPrimeToN)


if __name__ == '__main__':
    print(list(filter(isPrime, [elem for elem in range(0, 100)])))
    goldbach(4)
    goldbach(6)
    goldbach(8)
    goldbach(10)
    goldbach(12)
