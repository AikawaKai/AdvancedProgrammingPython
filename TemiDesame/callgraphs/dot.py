import ABC
from types import *
import sys
import inspect


file_o = open("./cg.dot", 'w')
file_o.write("strict digraph cg {\n")

file_o.close()

def decor(fun):
    def wrapper(*args, **kargs):
        res = fun(*args, **kargs)
        f = sys._getframe()
        if fun.__name__ == 'cc':
            args = "("+str(inspect.getargvalues(f)[3]['args'][0])+")"
            list_ = [fun.__name__+args]
            while True:
                if f.f_back.f_back is not None:
                    curr_fun = inspect.getframeinfo(f).function
                    if(curr_fun != 'wrapper'):
                        args = "("+str(inspect.getargvalues(f)[3]['i'])+")"
                        list_.append(curr_fun+args+" -> ")
                    f = f.f_back
                else:
                    curr_fun = inspect.getframeinfo(f).function
                    list_.append('main ->')
                    break;
            file_o = open("./cg.dot", 'a')
            file_o.write("\t"+("".join(list_[::-1])+"\n"))
            file_o.close()
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
