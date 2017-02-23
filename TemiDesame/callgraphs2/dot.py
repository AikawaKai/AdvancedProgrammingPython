from types import FunctionType, MethodType
import sys

file_o = open("./cg.dot", "w")
file_o.write("start\n")
file_o.close()


my_stack = []
path = dict()

def decor(fun):
    def wrapper(*args, **kargs):
        global my_stack
        global path
        string_ = fun.__name__+str(args)
        curr = string_
        my_stack.append(string_)
        res = fun(*args, **kargs)
        if fun.__name__ == 'cc':
            print(my_stack)
        next_ = ""
        while next_ != curr:
            next_ = my_stack.pop()
        return res
    return wrapper

class CG(type):

    def __new__(meta, classname, supers, dict_):
        changed = []
        for key, fun in dict_.items():
            if type(fun) == FunctionType:
                dict_[key] = decor(fun)
                dict_[key].func = fun
                changed.append(dict_[key])
        ma = type.__new__(meta, classname, supers, dict_)
        for decorated in changed:
            decorated.func.__globals__[classname] = ma
        return ma

import ABC
C = CG("C", (), dict(ABC.C.__dict__))
B = CG("B", (), dict(ABC.B.__dict__))
A = CG("A", (), dict(ABC.A.__dict__))
