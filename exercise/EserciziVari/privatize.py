def privatize(*privates):
    def wrapping(cls):
        class Wrapper():

            def __init__(self, *args):
                self.wrapped = cls(*args)

            def __getattr__(self, name):
                if name not in privates:
                    return getattr(self.wrapped, name)
                else:
                    raise TypeError("Attributo privato")

            def __setattr__(self, name, value):
                if name == "wrapped":
                    self.__dict__[name] = value
                elif name not in privates:
                    setattr(self.wrapped, name, value)
                else:
                    raise TypeError("Attributo privato - non modificabile")
        return Wrapper
    return wrapping

@privatize('a', 'c')
class A():

    def __init__(self, a, b, c, d):
        print(self, a, b, c ,d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def getStr(self):
        return str(a) + str(b) + str(c) + str(d)


if __name__ == '__main__':
    a = A(1, 2, 3, 4)
    print(a.b, a.d)
    a.b = 1
    print(a.b, a.d)
