import time
from types import FunctionType

def timer(fun):
    def wrapper(*args, **kargs):
        start = time.time()
        result = fun(*args, **kargs)
        print("Tempo eseguito per {0}: {1}".format(fun,time.time()-start))
        return result
    return wrapper

class ClassDecorator(type):

    def __new__(meta, classname, supers, classdict):
        print(meta, "----", classname, "----", supers, "----", classdict)
        for key, value in classdict.items():
            if type(value) is FunctionType:
                classdict[key] = timer(value)
        return type.__new__(meta, classname, supers, classdict)



class A(metaclass=ClassDecorator):

    def __init__(self, n):
        self.n = n

    def getComphrension(self):
        return [x for x in range(0, self.n)]

    def getComphrension2(self):
        return [x**2 for x in range(0, self.n)]

if __name__ == '__main__':
    a = A(1000000)
    a.getComphrension()
    a.getComphrension2()
