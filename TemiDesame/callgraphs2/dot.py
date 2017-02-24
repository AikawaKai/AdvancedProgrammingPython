from types import FunctionType, MethodType

path_seen = dict()
my_stack = ["main"]

file_o = open("./cg.dot", 'w')
file_o.write("strict digraph cg {\n")
file_o.close()

def decor(fun, classname):
    def wrapper(*args, **kargs):
        global my_stack
        string_ = classname+"."+fun.__name__+str(args)
        my_stack.append(string_)
        res = fun(*args, **kargs)
        if str(my_stack) not in path_seen:
            file_o = open("./cg.dot", 'a')
            newline ="\t"+" -> ".join(my_stack)+"\n"
            file_o.write(newline)
            file_o.close()
        for i in range(len(my_stack)):
            if str(my_stack[:-i]) not in path_seen:
                path_seen[str(my_stack[:-i])]= string_
        my_stack.pop()
        if len(my_stack)==1:
            file_o = open("./cg.dot", 'a')
            newline ="}"
            file_o.write(newline)
            file_o.close()
        return res
    return wrapper

class CG(type):

    def __new__(meta, classname, supers, dict_):
        changed = []
        for key, fun in dict_.items():
            if type(fun) == FunctionType:
                dict_[key] = decor(fun, classname)
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
