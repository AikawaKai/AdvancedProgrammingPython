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
def TestingClasses(list_):
    class TestShape(unittest.TestCase):
        pass
