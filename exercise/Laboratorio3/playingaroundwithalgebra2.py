from iteratorRational import *
from itertools import combinations


def genFunc(n):
    def func(a, b):
        return (a+b) % n
    return func


class NaturalIterator(object):

    def __init__(self, maxvalue):
        self.__max = maxvalue

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


class Ziterator(object):

    def __init__(self, minvalue, maxvalue, maxrandomvalue):
        self.__max = maxvalue
        self.__min = minvalue
        self.__maxrandomvalue = maxrandomvalue

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__count <= self.__maxrandomvalue:
            randint = random.randint(self.__min, self.__max)
            self.__count += 1
            return randint
        else:
            raise StopIteration


class Monoid(object):

    def __init__(self, mset, add, i):
        self.setMonoid(mset, add, i)

    def getMonoid(self):
        return (self.__set, self.__add, self.__i)

    def checkIdentity(mset, add, i):
        for elem in mset:
            if elem != add(elem, i):
                print(elem, add(elem, i), i)
                raise ValueError("checkIdentity Failed")

    def checkClosure(mset, add):
        couples = [(a, b) for a in mset for b in mset]
        for a, b in couples:
            if not isinstance(add(a, b), type(a)):
                raise ValueError("checkClosure Failed")

    def checkAssociativity(mset, add):
        triple = [(a, b, c) for a in mset for b in mset for c in mset]
        for a, b, c in triple:
            if add(add(a, b), c) != add(a, add(b, c)):
                raise ValueError("checkAssociativity Failed")

    def setMonoid(self, mset, add, i):
        Monoid.checkIdentity(mset, add, i)
        Monoid.checkAssociativity(mset, add)
        Monoid.checkClosure(mset, add)
        print("È un monoide")
        self.__set = mset
        self.__add = add
        self.__i = i


class Group(Monoid):

    def __init__(self, mset, add, i, invAdd):
        self.setGroup(mset, add, i, invAdd)

    def getGroup(self):
        return(self.__mset, self.__add, self.__i)

    def checkInvertibility(mset, invAdd, i):
        for elem in mset:
            if invAdd(elem) != i:
                return False
        return True

    def setGroup(self, mset, add, i, invAdd):
        Group.checkIdentity(mset, add, i)
        Group.checkAssociativity(mset, add)
        Group.checkClosure(mset, add)
        Group.checkInvertibility(mset, invAdd, i)
        print("È un gruppo")
        self.__set = mset
        self.__add = add
        self.__i = i


class Ring():

    def __init__(self, mset, add, i, invAdd, prod):
        self.setRing(mset, add, i, invAdd, prod)

    def getRing(self):
        return(self.__mset, self.__add, self.__i, self.__invAdd, self.__prod)

    def setRing(self, mset, add, i, invAdd, prod):
        print("Sono qui")
        self.__monoid = Monoid(mset, prod, i)
        print("Superato")
        Ring.checkCommutativity(mset, add)
        self.__group = Group(mset, add, i, invAdd)
        print("È un anello")
        self.__set = mset
        self.__add = add
        self.__i = i
        self.__invAdd = invAdd
        self.__prod = prod

    def checkCommutativity(mset, add):
        comb = combinations(mset, 2)
        for a, b in comb:
            if add(a, b) != add(b, a):
                raise ValueError("checkCommutativity Failed")


if __name__ == '__main__':
    Monoide = Monoid({True, False}, lambda x, y: x or y, False)
    integerSet = {i for i in NaturalIterator(100)}
    Monoide1 = Monoid(integerSet, genFunc(101), 0)
    iteratorRational = RandomRational(1, 100, 1, 100)
    rationals = {rat for rat in iteratorRational}
    prod = lambda x, y: Rational((x.getNum() * y.getNum()),
                                 (x.getDen() * y.getDen()))
    prodInv = lambda x: Rational((x.getNum() * x.getDen()),
                                 (x.getDen() * x.getNum()))
    Group1 = Group(rationals, prod, Rational(1, 1), prodInv)
    Ring0 = Ring({0}, lambda x, y: x+y, 0, lambda x: x-x, lambda x, y: x*y)
    iteratorZ = Ziterator(-100, 100, 100)
    zSet = {z for z in iteratorZ}
    print(zSet)
    #  Ring1 = Ring(zSet, lambda x, y: x+y, 0, lambda x: x-x, lambda x, y: x*y)
    # Ring1 not a Ring checkIdentity fails
    mset = {0, 1, 2, 3}
    add = lambda x, y: (x+y) % 4
    invAdd = lambda x: (x+(4-x)) % 4
    prod = lambda x, y: (x*y) % 4
    # Ring2 = Ring(mset, add, 0, invAdd, prod)
    # Ring2 not a Ring checkIdentity fails
