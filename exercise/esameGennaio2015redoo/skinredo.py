
def becomewithclassname(classname):
    def become(self, set1, set2):
        fun1 = set1.pop()
        fun2 = set2.pop()
        self.__dict__[fun1.__name__] = fun1.__get__(self, classname)
        if fun2.__name__ in self.__dict__:
            del self.__dict__[fun2.__name__]
    return become


class ChangeSkin(type):

    def __new__(meta, classname, supers, classdict):
        classdict["become"] = becomewithclassname(classname)
        return type.__new__(meta, classname, supers, classdict)
