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
    yield i
    while True:
        i += 1
        yield i
        yield -i


class Z():

    def generateSET(self, n=100):
        iterator = Zgenerator()
        self.set = [next(iterator) for i in range(n+1)]
        return self.set

    def inSet(self, value):
        return True if value in Zgenerator() else False


def generateTestCase(Ring, ringname):

    class TestRing(TestCase):

        def setUp(self):
            self.ring = Ring()
            self.ringset = self.ring.generateSET()
            self.ringname = ringname
            self.permut2 = permutations(self.ringset, 2)
            self.permut3 = permutations(self.ringset, 3)
            self.z = self.ring.z
            self.i = self.ring.i

        def testingClosure(self):
            print("Test Closure: {0}".format(self.ringname))
            for x, y in self.permut2:
                self.assertTrue(self.ring.inSet(x+y))
                self.assertTrue(self.ring.inSet(x*y))

        def testAssociativityAdd(self):
            print("Test AssociativityAdd: {0}".format(self.ringname))
            for x, y, z in self.permut3:
                    self.assertEqual((x+y)+z, x+(y+z))

        def testAssociativityMul(self):
            print("Test AssociativityMul: {0}".format(self.ringname))
            for x, y, z in self.permut3:
                    self.assertEqual((x*y)*z, x*(y*z))

        def testIdentitySum(self):
            print("Test Identity Sum: {0}".format(self.ringname))
            for x in self.ringset:
                self.assertEqual(x+self.z, x)

        def testIdentityMul(self):
            print("Test Identity Mul: {0}".format(self.ringname))
            for x in self.ringset:
                self.assertEqual(x*self.i, x)

        def testInvertibility(self):
            print("Test Invertibility Sum: {0}".format(self.ringname))
            result = []
            for x in self.ringset:
                setx = []
                for y in self.ringset:
                    setx.append(x+y == self.z)
                result.append(setx)
            for setx in result:
                self.assertTrue(sum(setx) > 0)

        def testCommutativityAdd(self):
            print("Test Commutativity Sum: {0}".format(self.ringname))
            for x, y in self.permut2:
                self.assertTrue((x+y) == (y+x))

        def testDistributivityMul(self):
            print("Test Distributivity Mul over Sum: {0}".format(self.ringname))
            for x, y, z in self.permut3:
                self.assertEqual(x * (y + z), (x * y) + (x * z))
            for x, y, z in self.permut3:
                self.assertEqual((y + z) * x, (y * x) + (z * x))



    return TestRing


ringZ = genRing(Z, lambda x, y: x+y, lambda x, y: x*y, 1, 0)
testZ = generateTestCase(ringZ, "ring Z + x i=1 z=0")

if __name__ == '__main__':
    suite = TestSuite()
    testLoader = TestLoader()
    suite.addTest(testLoader.loadTestsFromTestCase(testZ))
    runner = TextTestRunner()
    runner.run(suite)
