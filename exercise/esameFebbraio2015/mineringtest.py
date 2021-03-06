from unittest import TestCase
from itertools import product
from unittest import TestSuite
from unittest import TestLoader
from unittest import TextTestRunner


def createRing(ClassRing, i, z, add, mul):
    ClassRing.i = i
    ClassRing.z = z
    ClassRing.__add__ = add
    ClassRing.__mul__ = mul
    return ClassRing


def GenerateTest(nameRing, Class):
    class check_ring(TestCase):
        setToTest = Class.generateSet()
        print(setToTest)
        closureset = product(setToTest, repeat=2)
        associativityset = product(setToTest, repeat=3)

        def testClosure(self):
            print("checking closure for {}".format(nameRing))
            for elem1, elem2 in self.closureset:
                res1 = elem1 + elem2
                self.assertTrue(res1.inSet())
                res2 = elem1 * elem2
                self.assertTrue(res2.inSet())

        def testAssociativity(self):
            print("checking associativity for {}".format(nameRing))
            for x, y, z in self.associativityset:
                self.assertEqual(((x+y)+z), (x+(y+z)))
                self.assertEqual(((x*y)*z), (x*(y*z)))

        def testIdentity(self):
            print("checking identity for {}".format(nameRing))
            for x in self.setToTest:
                self.assertEqual(x, x+Class.z)
                self.assertEqual(x, x*Class.i)

        def testInvertibility(self):
            print("checking invertibility for {}".format(nameRing))
            checks = []
            for x in self.setToTest:
                checks += [any([(x+y) == Class.z for y in self.setToTest])]
            self.assertTrue(all(checks))

        def testCommutativity(self):
            print("checking commutativity for {}".format(nameRing))
            for x, y in self.closureset:
                self.assertEqual((x + y), (y + x))

        def testDistributivity(self):
            print("checking distributivity for {}".format(nameRing))
            for x, y, z in self.associativityset:
                self.assertEqual((x * (y + z)), (x * y) + (x * z))
                self.assertEqual(((y + z) * x), (x * y) + (x * z))
    return check_ring


class Z(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Z({0})".format(self.value)

    def generateSet(n=50):
        return [Z(x) for x in range(-n, n+1)]

    def inSet(self):
        return (self in Zn())


class nZ(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "nZ({0})".format(self.value)

    def generateSet(n=50):
        return [nZ(x) for x in range(-n, n+1)]

    def inSet(self):
        return (self in Zn())


class Z4(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Z4({0})".format(self.value)

    def generateSet():
        return [Z4(x) for x in range(0, 4)]

    def inSet(self):
        return (self in Z4.generateSet())


class Bool(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Bool({0})".format(self.value)

    def generateSet():
        return [Bool(True), Bool(False)]

    def inSet(self):
        return (self in Bool.generateSet())


def Zn():
    count = 0
    yield Z(count)
    while True:
        count += 1
        yield Z(count)
        yield Z(-count)


ringz = createRing(Z, Z(1), Z(0), lambda x, y: Z(x.value+y.value), lambda x, y: Z(x.value*y.value))
testz = GenerateTest("ringz", ringz)

ringnz = createRing(nZ, nZ(0), nZ(1), lambda x, y: nZ(x.value*y.value), lambda x, y: nZ(x.value+y.value))
testnz = GenerateTest("ringnz", ringnz)

ringz4 = createRing(Z4, Z4(1), Z4(0), lambda x, y: Z4((x.value + y.value) % 4), lambda x, y: Z4((x.value * y.value) % 4))
testz4 = GenerateTest("ringZ4", ringz4)

ringBool = createRing(Bool, Bool(True), Bool(False), lambda x, y: Bool(x.value or y.value), lambda x, y: Bool(x.value and y.value))
testBool = GenerateTest("ringBool", ringBool)

tests = [testz4, testz, testnz, testBool]

if __name__ == '__main__':
    suite = TestSuite()
    for test in tests:
        suite.addTests(TestLoader().loadTestsFromTestCase(test))
    TextTestRunner(verbosity=2).run(suite)
