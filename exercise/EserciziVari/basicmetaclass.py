import time
from types import FunctionType


def timer(fun):
    def wrapper(*args):
        start = time.time()
        result = fun(*args)
        print("{1} eseguita in {0:5.5} sec".format(time.time()-start, fun.__name__))
        return result
    return wrapper


class MineMetaClass(type):

    def __new__(meta, classname, supers, classdict):
        for elem, value in classdict.items():
            if type(value) is FunctionType:
                classdict[elem] = timer(classdict[elem])
        return type.__new__(meta, classname, supers, classdict)


class BasicClass(object, metaclass=MineMetaClass):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "a: {0} b: {1}".format(self.a, self.b)


if __name__ == '__main__':
    basic = BasicClass(5, 4)
    print(str(basic))
