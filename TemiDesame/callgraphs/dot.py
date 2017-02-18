import ABC
from types import *

def decor(fun):
    def wrapper(*args, **kargs):
        print(fun.__name__, " ")
        res = fun(*args, **kargs)
        return res
    return wrapper

class MetaPath(type):

    def __new__(self, classname, supers, dict_, **kwds):
        for key, value in dict_.items():
            if type(value) is FunctionType:
                dict_[key]=decor(value)
        return type.__new__(self, classname, supers, dict_, **kwds)

ABC.C = MetaPath("C", (), dict(ABC.C.__dict__))
ABC.B = MetaPath("B", (), dict(ABC.B.__dict__))
ABC.A = MetaPath("A", (), dict(ABC.A.__dict__))
A = ABC.A
B = ABC.B
C = ABC.C
