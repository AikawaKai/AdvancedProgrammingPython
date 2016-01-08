class C:
    def __init__(self):
        self.class_attribute = "a value"

    def __str__(self):
        return self.class_attribute


def introspect(self):
    result = ""
    for k, v in self.__dict__.items():
        result += k+": "+v+"\n"
    return result

C.__str__ = introspect


class D():
    class_attribute = "a value"

    def f(self):
        return "a function"

    def __call__(self, integer):
        print("rendo l'istanza chiamabile come funzione {0}".format(integer))


class Desc(object):
    '''Un esempio di descrittore'''
    def __get__(self, obj, cls=None):
        print("{0}.__get__({1}, {2})".format(self, obj, cls))

    def __set__(self, obj, val):
        print("{0}.__set__({1}, {2})".format(self, obj, val))

    def __delete__(self, obj):
        print("{0}._delete__({1})".format(self, obj))


class C1(object):
    d = Desc()
