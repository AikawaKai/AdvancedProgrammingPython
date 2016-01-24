def decor(classname):
    def become(self, set1, set2):
        for fun in set1:
            self.__dict__[fun.__name__] = fun.__get__(self, classname)
        for fun in set2:
            if fun.__name__ in self.__dict__:
                del self.__dict__[fun.__name__]
    return become


def pop(self):
    self.top -= 1
    toReturn = self.data[self.top]
    del self.data[self.top]
    return toReturn


def push(self, elem):
    self.data.append(elem)
    self.top += 1


class Skin(type):

    def __new__(meta, classname, supers, classdict):
        classdict["become"] = decor(classname)
        return type.__new__(meta, classname, supers, classdict)


class stack(metaclass=Skin):

    def __init__(self, dim=10):
        self.dimension = dim
        self.top = 0
        self.data = []

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == (self.dimension-1)

    def __str__(self):
        return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}".format(self.top, self.dimension, self.data)
