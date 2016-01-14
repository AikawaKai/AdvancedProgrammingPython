import sys


class Pascal(object):

    def __init__(self, _max):
        self.count = 0
        self.max = _max
        self.prevList = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.max:
            raise StopIteration
        else:
            retRow = Row(self.prevList, self.count)
            retRow1 = Row(self.prevList, self.count)
            self.prevList = [elem for elem in retRow]
            self.count += 1
            return retRow1


class Row(object):

    def __init__(self, prevList, n):
        self.n = n
        self.count = 0
        self.prevList = prevList

    def __iter__(self):
        self.index1 = -1
        self.index2 = 0
        return self

    def checkIndex(index, prevList):
        if index < 0:
            return 0
        elif index > len(prevList)-1:
            return 0
        else:
            return prevList[index]

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        elif len(self.prevList) == 0:
            self.count += 1
            return 1
        else:
            value1 = Row.checkIndex(self.index1, self.prevList)
            value2 = Row.checkIndex(self.index2, self.prevList)
            retValue = value1 + value2
            self.index1 += 1
            self.index2 += 1
            self.count += 1
            return retValue


if __name__ == '__main__':
    pascal = Pascal(int(sys.argv[1]))
    for iterator in pascal:
        for elem in iterator:
            print(elem, end=" ")
        print()
