from unittest import TestCase
from unittest import TestSuite
from itertools import product
from unittest import loader
from unittest import TestLoader
from unittest import TextTestRunner


def addDataToClass(Ring, i, z, add, mul):
    Ring.i = i
    Ring.z = z
    Ring.__add__ = add
    Ring.__mul__ = mul
    return Ring


def Zgen():
    count = 0
    yield Z(count)
    while True:
        count += 1
        yield Z(count)
        yield Z(-count)


class Z():

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def generateSet(num=50):
        return [Z(x) for x in range(-num, num+1)]

    def __repr__(self):
        return "Z({0})".format(self.value)

    def inSet(self):
        return (self in Zgen())


def GenerateTest(Ring, ringname):

    class TestRing(TestCase):
        ringset = Ring.generateSet()
        print(ringset)
        douples = product(ringset, repeat=2)
        douples = [elem for elem in douples]
        triples = product(ringset, repeat=3)
        triples = [elem for elem in triples]

        def testClosure(self):
            print("### Testing closure for {}".format(ringname))
            for x, y in self.douples:
                self.assertTrue((x+y).inSet())
                self.assertTrue((x*y).inSet())

        def testAssociativityAdd(self):
            print("### Testing add associativity for {}".format(ringname))
            for x, y, z in self.triples:
                self.assertEqual(((x+y)+z), (x+(y+z)))

        def testAssociativityMul(self):
            print("### Testing mul associativity for {}".format(ringname))
            for x, y, z in self.triples:
                self.assertEqual(((x*y)*z), (x*(y*z)))

        def testIdentityZero(self):
            print("### Testing identityZero add for {}".format(ringname))
            for x in self.ringset:
                self.assertEqual(x, (x+Ring.z))

        def testIdentityI(self):
            print("### Testing identityI mul for {}".format(ringname))
            for x in self.ringset:
                self.assertEqual(x, (x*Ring.i))

        def testInvertibility(self):
            print("### Testing invertibility add for {}".format(ringname))
            value = []
            for x, y in self.douples:
                value.append(x+y == Ring.z)
            self.assertTrue(any(value))

        def testCommutativity(self):
            print("### Testing commutativity add for {}".format(ringname))
            for x, y in self.douples:
                self.assertTrue(x+y == y+x)

        def testDistributivityLeft(self):
            print("### Testing distributivity left for {}".format(ringname))
            for x, y, z in self.triples:
                self.assertEqual(x*(y+z), (x*y)+(x*z))

        def testDistributivityRight(self):
            print("### Testing distributivity right for {}".format(ringname))
            for x, y, z in self.triples:
                self.assertEqual((y+z)*x, (y*x)+(z*x))




    return TestRing


ringz = addDataToClass(Z, Z(1), Z(0), (lambda x, y: Z(x.value + y.value)), (lambda x, y: Z(x.value * y.value)))
testz = GenerateTest(ringz, "Z ring")

tests = [testz]

if __name__ == '__main__':
    suite = TestSuite()
    for test_c in tests:
        suite.addTests(TestLoader().loadTestsFromTestCase(testz))
    TextTestRunner(verbosity=2).run(suite)
