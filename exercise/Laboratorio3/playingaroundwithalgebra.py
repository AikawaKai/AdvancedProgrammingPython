from itertools import permutations


class monoid():
    def __init__(self, S, add, i):
        self._S = S
        self._add = add
        self._i = i

    def checkIdentity(self):
        add = self._add
        for elem in self._S:
            if elem != add(elem, self._i):
                return False
        return True


class group(monoid):
    def checkClosure(self):
        pass

    def checkAssociativity(self):
        pass

    def checkInvertibility(self):
        pass


class ring():
    pass


class Zn():
    def __init__(self, max):
        self._max = max

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        zn = self._i
        self._i += 1
        if self._i > self._max:
            raise StopIteration
        return zn


def orAdd(elem1, elem2):
    return elem1 or elem2


def baseAdd(elem1, elem2):
    return elem1 + elem2


if __name__ == '__main__':
    # some tests
    print(list(permutations('RGB')))
    monoid1 = monoid({True, False}, orAdd, False)
    print("L'identità è stata verificata come {0}"
          .format(monoid1.checkIdentity()))
    zn = Zn(1000)
    monoid2 = monoid(zn, baseAdd, 0)
    print("L'identità è stata verificata come {0}"
          .format(monoid2.checkIdentity()))
