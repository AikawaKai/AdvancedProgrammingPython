from unittest import TestCase
from unittest import main
from ring import *


class Z(object):

    def __init__(self, maxN):
        self.max = maxN * 2
        self.count = 1
        self.posNeg = [1, -1]
        self.cache = [0]
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.count > (self.max * 2) + 1:
            raise StopIteration
        toExtend = [s * self.count for s in self.posNeg]
        self.cache.extend(toExtend)
        toReturn = self.cache[self.index]
        self.count += 1
        self.index += 1
        return toReturn


def op1(a, b):
    return a + b


def op2(a, b):
    return a * b


class TestinRing(TestCase):

    def testInitClass(self):
        z = Z(100)
        set1 = set(z)
        print(set1)
        ring = Ring(set1, op1, op2)


if __name__ == '__main__':
    main()
