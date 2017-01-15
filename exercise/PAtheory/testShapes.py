import unittest
from shapes import *
from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

shapes_ = [Rectangle, Square, Circle]


listOfValueToTestRectangle = [(Rectangle.__name__, Rectangle(i,j).area(), Rectangle(i,j).perimeter(), (i,j))for i,j in pairwise(range(1, 1000))]
listOfValueToTestSquare= [(Square.__name__, Square(i).area(), Square(i).perimeter(), (i,)) for i in range(1, 1000)]
listOfValueToTestCircle= [(Circle.__name__, Circle(i).area(), Circle(i).perimeter(), (i,)) for i in range(1, 1000)]


tot_list = listOfValueToTestCircle + listOfValueToTestSquare + listOfValueToTestRectangle

lambda_func_area = {"Square": (lambda x: x*x), "Circle": (lambda x: x**2*pi), "Rectangle": (lambda x,y: x*y)}
def TestingClasses(list_):
    class TestShape(unittest.TestCase):

        def testAreaIsCorrect(self):
            for class_name, area, perim, args in list_:
                print(class_name, area, perim, args)
                self.assertEqual(area, lambda_func_area[class_name](*args))

    return TestShape

if __name__ == '__main__':
    class_ = TestingClasses(tot_list)
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(class_))
    unittest.TextTestRunner(verbosity=2).run(suite)
