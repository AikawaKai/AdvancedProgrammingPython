import time
import types

# timer
def decorator(fun):
    def wrapper(*args, **kargs):
        start = time.time()
        res = fun(*args, **kargs)
        end = time.time()
        print("Eseguito in "+str(end-start)+" sec")
        return res
    return wrapper


class MetaClass1(type):

    def __new__(cls, name, bases, namespace, **kwds):
        #print(cls, name, bases, namespace, **kwds)
        dict_ = dict(namespace)
        for key, value in dict_.items():
            if type(value) is types.FunctionType:
                dict_[key] = decorator(value)
        return type.__new__(cls, name, bases, dict_)


class MyClass(metaclass=MetaClass1):

    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def print_(self):
        print(self.__dict__)


if __name__ == '__main__':
    a = MyClass()
    a.print_()
