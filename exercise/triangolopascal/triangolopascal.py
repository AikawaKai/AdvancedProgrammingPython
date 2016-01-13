from functools import reduce


def fact(n):
    if n == 0 or n == 1:
        return 1
    prod = lambda x, y: x*y
    return reduce(prod, [x for x in range(1, n+1)])


def factRic(n):
    return fact(n-1) * n if n > 1 else 1


def binomiale(n, k):
    if n == 0:
        return 0
    nfatt = factRic(n)
    kfatt = factRic(k)
    nkfatt = factRic(n-k)
    return nfatt // (kfatt * nkfatt)


class Row():

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        else:
            k = self.count
            self.count += 1
            kvalue = binomiale(self.n, k)
            return kvalue

    def prev(self):
        if self.count<= 0:
            raise StopIteration
        self. count -= 1
        toRet = binomiale(self.n, self.count)
        return toRet


class Pascal():

    def __init__(self, maxrow):
        self.maxrow = maxrow

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.maxrow:
            raise StopIteration
        else:
            iterator = Row(self.count)
            self.count += 1
            return iterator


if __name__ == '__main__':
    print(binomiale(0, 1))
    print(binomiale(1, 1))
    print(binomiale(2, 1))
    print(binomiale(10, 2))
    print(binomiale(25, 4))
    pascal = Pascal(6)
    n = 6
    for row in pascal:
        for elem in row:
            print(" {0} ".format(elem), end="")
        print("")

    row = Row(4)
    elemInRow = [elem for elem in row]
    print(elemInRow)
    print(row.prev())
    print(row.prev())
    print(row.prev())
    print(row.prev())
    print(row.prev())
    print(row.prev())
