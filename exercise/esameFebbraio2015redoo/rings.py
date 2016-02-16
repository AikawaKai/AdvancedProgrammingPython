from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader
from unittest import TextTestRunner
from itertools import permutations


def genRing(Ring, add, mul, i, z):
    Ring.__add__ = add
    Ring.__mul__ = mul
    Ring.i = i
    Ring.z = z
    return Ring


def Zgenerator():
    i = 0
    yield Z(i)
    while True:
        i += 1
        yield Z(i)
        yield Z(-i)


def Zngenerator():
    i = 0
    yield Zn(i)
    while True:
        i += 1
        yield Zn(i)
        yield Zn(-i)


class Z():
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def generateSET(n=100):
        iterator = Zgenerator()
        return [next(iterator) for i in range(n+1)]

    def inSet(self):
        return (self in Zgenerator())


class Zn():

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def generateSET(n=100):
        iterator = Zngenerator()
        return [next(iterator) for i in range(n+1)]

    def inSet(self):
        return (self in Zngenerator())


class Z4():

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def generateSET():
        return [Z4(x) for x in range(0, 4)]

    def inSet(self):
        return (self in Z4.generateSET())


class Bool():

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def generateSET():
        return [Bool(False), Bool(True)]

    def inSet(self):
        return (self in Bool.generateSET())



def generateTestCase(Ring, ringname):

    class TestRing(TestCase):

        def testingClosure(self):
            print("Test Closure: {0}".format(ringname))
            permut2 = permutations(Ring.generateSET(), 2)
            for x, y in permut2:
                self.assertTrue(Ring.inSet(x+y))
                self.assertTrue(Ring.inSet(x*y))

        def testAssociativityAdd(self):
            print("Test AssociativityAdd: {0}".format(ringname))
            permut3 = permutations(Ring.generateSET(), 3)
            for x, y, z in permut3:
                    self.assertEqual((x+y)+z, x+(y+z))

        def testAssociativityMul(self):
            print("Test AssociativityMul: {0}".format(ringname))
            permut3 = permutations(Ring.generateSET(), 3)
            for x, y, z in permut3:
                    self.assertEqual((x*y)*z, x*(y*z))

        def testIdentitySum(self):
            print("Test Identity Sum: {0}".format(ringname))
            for x in Ring.generateSET():
                self.assertEqual(x+Ring.z, x)

        def testIdentityMul(self):
            print("Test Identity Mul: {0}".format(ringname))
            for x in Ring.generateSET():
                self.assertEqual(x*Ring.i, x)

        def testInvertibility(self):
            print("Test Invertibility Sum: {0}".format(ringname))
            result = []
            for x in Ring.generateSET():
                setx = []
                for y in Ring.generateSET():
                    setx.append(x+y == Ring.z)
                result.append(setx)
            for setx in result:
                self.assertTrue(sum(setx) > 0)

        def testCommutativityAdd(self):
            print("Test Commutativity Sum: {0}".format(ringname))
            permut2 = permutations(Ring.generateSET(), 2)
            for x, y in permut2:
                self.assertTrue((x+y) == (y+x))

        def testDistributivityMuloverSum(self):
            print("Test Distributivity Mul over Sum: {0}".format(ringname))
            permut3 = permutations(Ring.generateSET(), 3)
            for x, y, z in permut3:
                self.assertEqual(x * (y + z), (x * y) + (x * z))
            for x, y, z in permut3:
                self.assertEqual((y + z) * x, (y * x) + (z * x))

    return TestRing


ringZ = genRing(Z, lambda x, y: Z(x.value+y.value), lambda x, y: Z(x.value*y.value), Z(1), Z(0))
testZ = generateTestCase(ringZ, "ring Z + x i=1 z=0")

ringZn = genRing(Zn, lambda x, y: Zn(x.value*y.value), lambda x, y: Zn(x.value+y.value), Zn(0), Zn(1))
testZn = generateTestCase(ringZn, "ring Zn x + i=0 z=1")

ringZ4 = genRing(Z4, lambda x, y: Z4((x.value+y.value) % 4), lambda x, y: Z4((x.value*y.value) % 4), Z4(1), Z4(0))
testZ4 = generateTestCase(ringZ4, "ring Z4 + x i=1 z=0")

ringBool = genRing(Bool, lambda x, y: Bool(x.value or y.value), lambda x, y: Bool(x.value and y.value), Bool(True), Bool(False))
testBool = generateTestCase(ringBool, "ring Bool or and i=True z=False")
tests = [testZ, testZn, testZ4, testBool]

if __name__ == '__main__':
    suite = TestSuite()
    testLoader = TestLoader()
    for test in tests:
        suite.addTest(testLoader.loadTestsFromTestCase(test))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
