import time
import sys


def decorator(f):
    def wrapper(*args):
        print("Sto wrappando la funzione {0}".format(str(f)))
        return f(*args)
    return wrapper


def decoratorChangeA(f):
    def wrapper(a, *args):
        print("a prima era {0}".format(a))
        a = 2
        print("a adesso è {0}".format(a))
        return f(a, *args)
    return wrapper


def decoratorTimeCalculator(f):
    def wrapper(*args):
        timestart = time.time()
        result = f(*args)
        end = time.time()
        print("l'operazione è conclusa in {0}".format(end-timestart))
        return result
    return wrapper


@decorator
def miafunc(string):
    print("{0}".format(string))


@decoratorChangeA
def miafuncConA(a, b, c):
    return a + b + c


@decoratorTimeCalculator
def callFact(n):
    return fact(n)


def fact(n):
    return 1 if n <= 1 else n * fact(n-1)


@decoratorTimeCalculator
def callFactIter(n):
    return factIter(n, 1)


def factIter(n, acc):
    return acc if n <= 1 else factIter(n-1, acc * n)


class DecoratorLikeClass(object):

        def __init__(self, func):
            self.func = func

        def __call__(self, *args):
            print("sto chiamando la funzione {0}".format(self.func))
            return self.func(*args)


@DecoratorLikeClass
def anotherF(string):
    print("string: {0}".format(string))


def classDecorator(cls):
    class Wrapper(object):

        def __init__(self, *args):
            print("sto creando la classe")
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print("sto facendo una get su di un attributo: {0}".format(name))
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            print("sto settando l'attributo {0} con il valore {1}".format(name, value))
            if name == "wrapped":
                self.__dict__[name] = value
            else:
                setattr(self.wrapped, name, value)
    return Wrapper


@classDecorator
class ClassToExtend(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


if __name__ == '__main__':
    sys.setrecursionlimit = 100000000000
    miafunc("ciao")
    miafunc("prova")
    miafunc("prova1")
    print(miafuncConA(1, 2, 3))  # 7 invece che 6
    print(callFact(200))
    print(callFactIter(200))
    anotherF("stringa da stampare")
    ClassToExtend(10, 12)
