def classDecorator(cls):
    class WrapperClass():

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print(name)
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            if name == 'wrapped':
                print("sto settando l'istanza interna")
                self.__dict__[name] = value
            else:
                print("Setto ", name, " Value: ", value)
                setattr(self.wrapped, name, value)
    return WrapperClass

@classDecorator
class A():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def printMethod(self):
        print(self.a, self.b, self.c)

    def returnStringConcat(self):
        return str(self.a) + " " + str(self.b) + " " + str(self.c)

if __name__ == '__main__':
    a = A(5, 6, 7)
    print(a)
    a.printMethod()
