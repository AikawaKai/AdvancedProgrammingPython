from types import FunctionType


def decorateAll(decorator):
    class MetaClassDecorator(type):

        def __new__(meta, classname, supers, classdict):
            for name, elem in classdict.items():
                if type(elem) is FunctionType:
                    classdict[name] = decorator(classdict[name])
            return type.__new__(meta, classname, supers, classdict)
    return MetaClassDecorator


def printFormatFun(fun):
    def wrapper(*args):
        print("Funzione: {0} argomenti:{1}".format(fun.__name__, args))
        return fun(*args)
    return wrapper


class Counter():

    def __init__(self, fun):
        self.fun = fun
        self.count = 0

    def __call__(self, *args):
        self.count += 1
        print("{1} chiamata {0} volte".format(self.count, self.fun.__name__))
        return self.fun(*args)


def counter(fun):
    fun.count = 0
    def wrapper(*args):
        fun.count += 1
        print("{0} Eseguita {1} volte".format(fun.__name__, fun.count))
        return fun(*args)
    return wrapper


@Counter
def printer():
    print("Ciao")


if __name__ == '__main__':
    printer()
    printer()
