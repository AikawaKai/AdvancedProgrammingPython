class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        c = self.a
        self.a = self.b
        self.b = self.b + c
        return fib


if __name__ == '__main__':
    fib = Fib(1000)
    for i in fib:
        print(i)
