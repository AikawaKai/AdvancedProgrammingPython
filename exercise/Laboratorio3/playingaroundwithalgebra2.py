from iteratorRational import *


def genFunc(n):
    def func(a, b):
        return (a+b) % n
    return func


class NaturalIterator(object):

    def __init__(self, max):
        self.__max = max

    def __iter__(self):
        self.__num = 0
        return self

    def __next__(self):
        if self.__num <= self.__max:
            Num = self.__num
            self.__num += 1
            return Num
        else:
            raise StopIteration


class Monoid(object):

    def __init__(self, mset, add, i, checkValue):
        self.setMonoid(mset, add, i, checkValue)

    def getMonoid(self):
        return (self.__set, self.__add, self.__i, self.__checkValue)

    def checkIdentity(mset, add, i):
        for elem in mset:
            if elem != add(elem, i):
                print(elem)
                return False
        return True

    def checkClosure(mset, add, checkValue):
        couples = [(a, b) for a in mset for b in mset]
        for a, b in couples:
            if not checkValue(add(a, b)):
                return False
        return True

    def checkAssociativity(mset, add):
        triple = [(a, b, c) for a in mset for b in mset for c in mset]
        for a, b, c in triple:
            if add(add(a, b), c) != add(a, add(b, c)):
                return False
        return True

    def setMonoid(self, mset, add, i, checkValue):
        if not Monoid.checkIdentity(mset, add, i):
            raise ValueError("Non è un monoide: checkIdentity Failed")
        elif not Monoid.checkAssociativity(mset, add):
            raise ValueError("Non è un monoide: checkAssociativity Failed")
        elif not Monoid.checkClosure(mset, add, checkValue):
            raise ValueError("Non è un monoide: checkClosure")
        else:
            print("È un monoide")
            self.__set = mset
            self.__add = add
            self.__i = i
            self.__checkValue = checkValue


class Group(Monoid):

    def __init__(self, mset, add, i, checkValue):
        self.setGroup(mset, add, i, checkValue)

    def getGroup(self):
        return(self.__mset, self.__add, self.__i, self.__checkValue)

    def checkInvertibility():
        pass

    def setGroup(self, mset, add, i, checkValue):
        if not Group.checkIdentity(mset, add, i):
            raise ValueError("Non è un gruppo: checkIdentity Failed")
        elif not Group.checkAssociativity(mset, add):
            raise ValueError("Non è un gruppo: checkAssociativity Failed")
        elif not Group.checkClosure(mset, add, checkValue):
            raise ValueError("Non è un gruppo: checkClosure")
        elif not Group.checkInvertibility(mset, add, i):
            raise ValueError("Non è un gruppo: checkInvertibility Failed")
        else:
            print("È un gruppo")
            self.__set = mset
            self.__add = add
            self.__i = i
            self.__checkValue = checkValue


if __name__ == '__main__':
    Monoide = Monoid({True, False}, lambda x, y: x or y, False, lambda x:
                     isinstance(x, bool))
    integerSet = {i for i in NaturalIterator(100)}
    Monoide1 = Monoid(integerSet, genFunc(101), 0,
                      lambda x: isinstance(x, int))
