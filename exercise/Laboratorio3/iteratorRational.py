import random


class Rational():

    def __init__(self, num, den):
        self.setNum(num)
        self.setDen(den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def setNum(self, num):
        self.__num = num

    def setDen(self, den):
        if den == 0:
            self.__den = 1
        else:
            self.__den = den

    def __str__(self):
        return str(self.__num)+"/"+str(self.__den)

    num = property(getNum, setNum)
    den = property(getDen, setDen)


class RandomRational():

    def __init__(self, minvalue, maxvalue, seedvalue):
        self.__min = minvalue
        self.__max = maxvalue
        self.__seed = seedvalue

    def __iter__(self):
        random.seed(self.__seed)
        return self

    def __next__(self):
        randomIntegerNum = random.randint(self.__min, self.__max)
        randomIntegerDen = random.randint(self.__min, self.__max)
        return Rational(randomIntegerNum, randomIntegerDen)


if __name__ == '__main__':
    iteratorRational = RandomRational(1, 100, 1)
    for i in range(0, 100):
        RationalTemp = next(iteratorRational)
        print(RationalTemp)

    print(Rational(1, 0))
    Rat1 = Rational(5, 6)
    Rat1.den = 0
    print(Rat1)
