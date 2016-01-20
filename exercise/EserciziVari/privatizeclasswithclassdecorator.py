def privatize(*private):
    def customclass(cls):
        class Wrapper(object):

            def __init__(self, *args):
                self.wrapped = cls(*args)

            def __getattr__(self, name):
                if name not in private:
                    return getattr(self.wrapped, name)
                string = "You cannot get this attribute:'{0}' value".format(name)
                raise TypeError(string)

            def __setattr__(self, name, value):
                if name == 'wrapped':
                    self.__dict__[name] = value
                elif name not in private:
                    setattr(self.wrapped, name, value)
                else:
                    string = "You cannot set this attribute:'{0}' value".format(name)
                    raise TypeError(string)

            def __str__(self):
                return str(self.wrapped)
        return Wrapper
    return customclass


@privatize("c", "d", "print")
class MineClass(object):

    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def print(self):
        print("{0}{1}{2}{3}{4}".format(self.a, self.b, self.c, self.d, self.e))

    def __str__(self):
        return "{0}{1}{2}{3}{4}".format(self.a, self.b, self.c, self.d, self.e)


if __name__ == '__main__':
    mine = MineClass("a", "b", "c", "d", "e")
    print(str(mine))
    #  print(mine.c) #  private
    #  print(mine.d) #  private
    mine.print()
