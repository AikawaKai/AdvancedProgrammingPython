# decorando in questa maniera l'attributo instance resta.
class decoratorSingleton():

    def __init__(self, cls):
        self.wrapped = cls
        self.instance = None

    def __call__(self, *args):
        if self.instance == None:
            self.instance = self.wrapped(*args)
        return self.instance

# non va bene! Non crea un singleton, ma crea ogni volta una classe differente
def tryingFunSingleton(cls):
    class wrapper():

        def __init__(self, *args):
            self.instance = cls(*args)

        def __getattr__(self, name):
            print(name)
            return getattr(self.instance, name)

        def __setattr__(self, name, value):
            if name == 'instance':
                if "instance" not in self.__dict__:
                    self.__dict__[name] = value
            else:
                setattr(self.instance, name, value)
    return wrapper


@tryingFunSingleton
class Person():

    def __init__(self, name):
        self.name = name

    def print_(self):
        print(self.name)

if __name__ == '__main__':
    p = Person("marco")
    p.print_()
    print(p.instance)
    c = Person("mario")
    c.print_()
    print(c.instance)
