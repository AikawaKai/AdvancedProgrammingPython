class FiboIter():

    def __init__(self, max_):
        self.max = max_

    def __iter__(self):
        self.a = 1
        self.b = 1
        return self

    def __next__(self):
        to_return = self.a
        if to_return >= self.max : raise StopIteration
        c = self.a+self.b
        self.a = self.b
        self.b = c
        return to_return

if __name__ == '__main__':
    fib = FiboIter(100)
    for el in fib:
        print(el)
