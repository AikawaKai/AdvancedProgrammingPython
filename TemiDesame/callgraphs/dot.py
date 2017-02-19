import ABC
import main
from types import *
import sys
import inspect


file_o = open("./cg.dot", 'w')
file_o.write("strict digraph cg {\n")
file_o.close()

classes = [(key, value) for key, value in ABC.__dict__.items() if type(value) is type(object)]
dict_classes = {key:[val.__name__ for val in value.__dict__.values() if type(val) is FunctionType] for key, value in classes}
def decor(fun):
    def wrapper(*args, **kargs):
        res = fun(*args, **kargs)
        f = sys._getframe()
        if fun.__name__ == 'cc':
            curr_fun = fun.__name__
            args = "("+str(inspect.getargvalues(f)[3]['args'][0])+")"
            for key, value in dict_classes.items():
                if curr_fun in value:
                    curr_fun = key+"."+curr_fun
                    break;
            list_ = [curr_fun+args]
            while True:
                if f.f_back.f_back is not None:
                    curr_fun = inspect.getframeinfo(f).function
                    if(curr_fun != 'wrapper'):
                        for key, value in dict_classes.items():
                            if curr_fun in value:
                                curr_fun = key+"."+curr_fun
                                break;
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


C = ABC.C = MetaPath("C", (), dict(ABC.C.__dict__))
B = ABC.B =  MetaPath("B", (), dict(ABC.B.__dict__))
A = ABC.A =  MetaPath("A", (), dict(ABC.A.__dict__))
