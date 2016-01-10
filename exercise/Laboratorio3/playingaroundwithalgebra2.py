from iteratorRational import *


class Monoid(object):

    def __init__(self, mset, add, i):
        self.setMonoid(mset, add, i)

    def getMonoid(self):
        return (self.__set, self.__add, self.__i)

    def checkIdentity(mset, add, i):
        for elem in mset:
            if elem != add(elem, i):
                return False
        return True

    def checkAssociativity(mset, add):
        triple = [(a, b, c) for a in mset for b in mset for c in mset]
        for a, b, c in triple:
            if add(add(a, b), c) != add(a, add(b, c)):
                return False
        return True

    def setMonoid(self, mset, add, i):
        if not Monoid.checkIdentity(mset, add, i):
            raise ValueError("Non è un monoide: checkIdentity Failed")
        elif not Monoid.checkAssociativity(mset, add):
            raise ValueError("Non è un monoide: checkAssociativity Failed")
        else:
            print("È un monoide")
            self.__set = mset
            self.__add = add
            self.__i = i

    monoidProperty = property(getMonoid, setMonoid)

if __name__ == '__main__':
    Monoide = Monoid({True, False}, lambda x, y: x or y, False)
