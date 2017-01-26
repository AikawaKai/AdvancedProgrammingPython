import time

def timer(fun):
    def wrapper(*args):
        start = time.time()
        result = fun(*args)
        print(time.time()-start)
        return result
    return wrapper

def classDecorator(cls):

    class Wrapper():

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print("Sto estraendo l'attributo: ", name)
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            print("Sto settando l'attributo: ", name, " con valore: ", value)
            if name == 'wrapped':
                self.__dict__[name] = value
            else:
                setattr(self.wrapped, name, value)
    return Wrapper

@timer
def comphrension(n):
    return [x for x in range(0, n)]

@classDecorator
class A():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    comphrension(10000)
    comphrension(100000)
    comphrension(1000000)
    comphrension(10000000)
    a = A(1, 2, 3)
    print(a.sum())
