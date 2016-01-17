class PascalTriangle(object):

    def __init__(self, n):
        self.count = 0
        self.n = n
        self.prevlist = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        rowToNext = Row(self.prevlist, self.count)
        rowToSave = Row(self.prevlist, self.count)
        self.prevlist = [elem for elem in rowToSave]
        self.count += 1
        return rowToNext


class Row(object):

    def __init__(self, prevList, n):
        self.prevList = prevList
        self.n = n
        self.count = 0
        self.index1 = -1
        self.index2 = 0

    def __iter__(self):
        return self

    def _returnValueFromList(self, index):
        if index < 0:
            return 0
        if index > len(self.prevList)-1:
            return 0
        return self.prevList[index]

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        if self.n == 0:
            self.count += 1
            return 1
        valueToNext = self._returnValueFromList(self.index1) + self._returnValueFromList(self.index2)
        self.index1 += 1
        self.index2 += 1
        self.count += 1
        return valueToNext
