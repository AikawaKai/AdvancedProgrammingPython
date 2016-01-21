from types import FunctionType


def decorator1(fun):
    def wrapper(*args):
        print("Sono il decorator1 e sto eseguendo la funzione {0}".format(fun.__name__))
        return fun(*args)
    return wrapper


def decorator2(fun):
    def wrapper(*args):
        print("Sono il decorator2 e sto eseguendo la funzione {0}".format(fun.__name__))
        return fun(*args)
    return wrapper


def decorateAll(decorator):
    class MetaClassDecorated(type):

        def __new__(meta, classname, supers, classdict):
            for elem, value in classdict.items():
                if type(value) is FunctionType:
                    classdict[elem] = decorator(classdict[elem])
            return type.__new__(meta, classname, supers, classdict)

    return MetaClassDecorated


class BasicClass1(metaclass=decorateAll(decorator1)):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "a: {0} b: {1}".format(self.a, self.b)


class BasicClass2(metaclass=decorateAll(decorator2)):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "a: {0} b: {1}".format(self.a, self.b)


if __name__ == '__main__':
    basic1 = BasicClass1(5, 4)
    basic2 = BasicClass2(2, 7)
    print(str(basic1), str(basic2))
