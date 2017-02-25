from types import FunctionType

file_o = open("./cg.dot", 'w')
file_o.write("strict digraph cg {\n")
file_o.close()

class decoratorSingleton():

    def __init__(self, cls_):
        self.cls = cls_
        self.instance = None

    def __call__(self, *args, **kargs):
        if self.instance is not None:
            return self.instance
        else:
            self.instance = self.cls(*args, **kargs)
            return self.instance


@decoratorSingleton
class stack():

    def __init__(self):
        self.instance = ["main"]

    def push(self, value):
        self.instance.append(value)

    def pop(self):
        return self.instance.pop()

    def len(self):
        return len(self.instance)

    def getStack(self):
        return self.instance

@decoratorSingleton
class path_seen():

    def __init__(self):
        self.dict = {}

    def checkIfNotIn(self, path):
        if str(path) not in self.dict:
            return True

    def updateDict(self, paths):
        for i in range(len(paths)):
            if str(paths[:-i]) not in self.dict:
                self.dict[str(paths[:-i])] = 1

def decorator(fun, classname):
    def wrapper(*args, **kargs):
        s = stack()
        p = path_seen()
        string_ = '{}.{}{}'.format(classname, fun.__name__, tuple(list(args)+list(kargs)))
        s.push(string_)
        res = fun(*args, **kargs)
        st = s.getStack()
        if p.checkIfNotIn(st):
            file_o = open("./cg.dot", "a")
            file_o.write(" -> ".join(st)+"\n")
            file_o.close()
        p.updateDict(st)
        s.pop()
        if s.len() == 1:
            file_o = open("./cg.dot", "a")
            file_o.write("}")
            file_o.close()
        return res
    return wrapper

class CG(type):

    def __new__(meta, classname, supers, dict_):
        decorated = []
        for key, fun in dict_.items():
            if type(fun) is FunctionType:
                dict_[key]=decorator(fun, classname)
                decorated.append(fun)
        ma = type.__new__(meta, classname, supers, dict_)
        for decor in decorated:
            decor.__globals__[classname] = ma
        return ma

from ABC import *

A = CG("A", (), dict(A.__dict__))
B = CG("B", (), dict(B.__dict__))
C = CG("C", (), dict(C.__dict__))
