from unittest import main
from unittest import TestCase
from pascaltriangle import *


class TestingPascalTriangle(TestCase):

    def testPascal(self):
        pascal = PascalTriangle()
        row = next(pascal)
        self.assertEqual([1], [elem for elem in row])


if __name__ == '__main__':
    main()
