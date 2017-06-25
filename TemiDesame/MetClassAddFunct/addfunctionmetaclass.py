import types

def myfunct(self):
    for key, el in self.__dict__.items():
        print(key, el)


class AddFunctionMeta(type):

    def __new__(cls, name, bases, namespace, **kwds):
        dict_ = dict(namespace)
        dict_["miafunzione"] = types.MethodType(myfunct, cls)
        return type.__new__(cls, name, bases, dict_, **kwds)


class Base(metaclass=AddFunctionMeta):

    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b


if __name__ == '__main__':
    a = Base()
    a.miafunzione()
