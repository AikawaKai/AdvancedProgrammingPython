from types import FunctionType


def decorateMultiTriggered(fun):
    fun.count = 0
    def wrapped(*args):
        fun.count += 1
        if fun.count == 2:
            fun.count = 0
            return fun(*args)
    return wrapped


class MultiTriggeredMethod(type):

    def __new__(meta, classname, supers, classdict):
        for name, elem in classdict.items():
            if type(elem) is FunctionType and name is not "__init__":
                classdict[name] = decorateMultiTriggered(classdict[name])
        return type.__new__(meta, classname, supers, classdict)


class NaiveClass(object, metaclass=MultiTriggeredMethod):

    def __init__(self, thing1, thing2):
        self.thing1 = thing1
        self.thing2 = thing2

    def doSomthing(self):
        return self.thing1 + self.thing2

    def doSomthing1(self):
        print("Naive Class")


if __name__ == '__main__':
    prima = NaiveClass(10, 12)
    seconda = NaiveClass(10, 12)
    print(prima.doSomthing(), prima.doSomthing())
    print(seconda.doSomthing(), seconda.doSomthing())
