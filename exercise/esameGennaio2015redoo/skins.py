def addClassname(classname):
    def become(self, fun1, fun2):
        fun1 = fun1.pop()
        fun2 = fun2.pop()
        self.__dict__[fun1.__name__] = fun1.__get__(self, classname)
        if fun2.__name__ in self.__dict__:
            del self.__dict__[fun2.__name__]
    return become


class changeSkin(type):

    def __new__(meta, classname, supers, dictionary):
        dictionary['become'] = addClassname(classname)
        return type.__new__(meta, classname, supers, dictionary)
