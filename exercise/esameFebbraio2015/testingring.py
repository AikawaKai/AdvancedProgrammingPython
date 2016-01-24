from unittest import TestCase
from unittest import main
from ring import *
import time


class Z(object):

    def __init__(self, maxN):
        self.max = maxN
        self.count = 0
        self.posNeg = [-1, 1]
        self.cache = [0]
        self.index = 0

    def __iter__(self):
        self.index = 0
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.max + 1:
            if self.index < len(self.cache):
                toReturn = self.cache[self.index]
                self.index += 1
                return toReturn
            else:
                raise StopIteration
        if self.index < len(self.cache):
            toReturn = self.cache[self.index]
            self.index += 1
            return toReturn
        toExtend = [s * self.count for s in self.posNeg]
        self.cache.extend(toExtend)
        self.count += 1
        toReturn = self.cache[self.index]
        self.index += 1
        return toReturn


def op1(a, b):
    return a + b


def op2(a, b):
    return a * b

z = Z(100)


class TestinRing(TestCase):

    def testingZset(self):
        set1 = set([elem for elem in z])
        set2 = set([elem for elem in z])
        set3 = set([elem for elem in z])
        self.assertEqual(201, len(set1))
        self.assertEqual(201, len(set2))
        self.assertEqual(201, len(set3))

    def testInitClass(self):
        z = Z(100)
        set1 = set([elem for elem in z])
        Ring(set1, op1, op2, i=1, z=0)


if __name__ == '__main__':
    main()
