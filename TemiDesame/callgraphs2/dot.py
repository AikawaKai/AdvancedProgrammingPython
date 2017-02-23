from ABC import *
from types import FunctionType

def decor(fun):
    def wrapper(*args):
        file_o = open("./cg.dot", "a")
        file_o.write(fun.__name__+str(args)+" -> ")
        file_o.close()
        res = fun(*args)
        return res
    return wrapper

class CG(type):

    def __init__(self, classname, supers, dict_, *others):
        print(classname)
        for key, fun in dict_.items():
            if type(fun) is FunctionType:
                dict_[key] = decor(fun)
        return type.__init__(self, classname, supers, dict_, *others)


A = CG("A", (), dict(A.__dict__))
B = CG("B", (), dict(B.__dict__))
C = CG("C", (), dict(C.__dict__))
