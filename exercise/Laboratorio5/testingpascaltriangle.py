from unittest import main
from unittest import TestCase
from pascaltriangle import *


class TestingPascalTriangle(TestCase):

    def testPascal(self):
        pascal = PascalTriangle(5)
        row = next(pascal)
        self.assertEqual([1], [elem for elem in row])
        self.assertEqual([1, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 2, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 3, 3, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 4, 6, 4, 1], [elem for elem in next(pascal)])
        self.assertRaises(StopIteration, next, pascal)

    def testPrev(self):
        pascal = PascalTriangle(5)
        row = next(pascal)
        self.assertEqual([1], [elem for elem in row])
        self.assertEqual([1, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 2, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 3, 3, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 4, 6, 4, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 4, 6, 4, 1], [elem for elem in pascal.prev()])
        self.assertEqual([1, 3, 3, 1], [elem for elem in pascal.prev()])
        self.assertEqual([1, 2, 1], [elem for elem in pascal.prev()])
        self.assertEqual([1, 1], [elem for elem in pascal.prev()])
        self.assertEqual([1], [elem for elem in pascal.prev()])
        self.assertEqual([], [elem for elem in pascal.prev()])
        self.assertRaises(StopIteration, pascal.prev)
        self.assertEqual([], [elem for elem in next(pascal)])
        self.assertEqual([1], [elem for elem in next(pascal)])
        self.assertEqual([1, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 2, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 3, 3, 1], [elem for elem in next(pascal)])
        self.assertEqual([1, 4, 6, 4, 1], [elem for elem in next(pascal)])
        self.assertRaises(StopIteration, next, pascal)

    def testPrevRow(self):
        row = Row([0], 0)
        self.assertEqual(1, next(row))
        self.assertRaises(StopIteration, next, row)
        self.assertEqual(1, row.prev())
        self.assertRaises(StopIteration, row.prev)
        row = Row([1], 1)
        self.assertEqual(1, next(row))
        self.assertEqual(1, next(row))
        self.assertRaises(StopIteration, next, row)
        self.assertEqual(1, row.prev())
        self.assertEqual(1, row.prev())
        self.assertRaises(StopIteration, row.prev)
        row = Row([1, 1], 2)
        self.assertEqual(1, next(row))
        self.assertEqual(2, next(row))
        self.assertEqual(1, next(row))
        self.assertRaises(StopIteration, next, row)
        self.assertEqual(1, row.prev())
        self.assertEqual(2, row.prev())
        self.assertEqual(1, row.prev())
        self.assertRaises(StopIteration, row.prev)
        row = Row([1, 2, 1], 3)
        self.assertEqual(1, next(row))
        self.assertEqual(3, next(row))
        self.assertEqual(3, next(row))
        self.assertEqual(1, next(row))
        self.assertRaises(StopIteration, next, row)
        self.assertEqual(1, row.prev())
        self.assertEqual(3, row.prev())
        self.assertEqual(3, row.prev())
        self.assertEqual(1, row.prev())
        self.assertRaises(StopIteration, row.prev)



if __name__ == '__main__':
    main()
