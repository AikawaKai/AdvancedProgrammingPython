import functools
from types import FunctionType


def decorateAll(decorator):
    class MetaClassDecorator(type):

        def __new__(meta, classname, supers, classdict):
            for name, elem in classdict.items():
                if type(elem) is FunctionType:
                    classdict[name] = decorator(classdict[name])
            return type.__new__(meta, classname, supers, classdict)
    return MetaClassDecorator


class Counter(object):

    def __init__(self, fun):
        self.fun = fun
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("args:", self, *args, **kwargs)
        self.count += 1
        print("{0} Executed {1} times".format(self.fun.__name__, self.count))
        return self.fun(*args, **kwargs)

    def __get__(self, obj, cls=None):
        print('Simulating binding for {} and {}'.format(self.fun, obj))
        return functools.partial(self.fun, obj)


class Account(object, metaclass=decorateAll(Counter)):

    def __init__(self, initial_amount):
        self.amount = initial_amount

    def withdraw(self, towithdraw):
        self.amount -= towithdraw

    def deposit(self, todeposit):
        self.amount += todeposit

    def balance(self):
        return self.amount


a = Account(33.5)

print(a.balance())
