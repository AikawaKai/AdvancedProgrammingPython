def decorator(cls):
    class ClassDecorator(object):

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print("Sto recuperando il valore di {0}".format(name))
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            if name == "wrapped":
                self.__dict__[name] = value
            else:
                print("Sto settando {0} con il valore {1}".format(name, value))
                setattr(self.wrapped, name, value)

        def __str__(self):
            return str(self.wrapped)
    return ClassDecorator


@decorator
class ToDecorate(object):

    def __init__(self, stringa1, stringa2):
        self.stringa1 = stringa1
        self.stringa2 = stringa2

    def concatMyString(self):
        self.concat = self.stringa1 + " " + self.stringa2
        return self.concat

    def __str__(self):
        return "stringa1: {0}, stringa2: {1}".format(self.stringa1, self.stringa2)


if __name__ == '__main__':
    istance = ToDecorate("ciao", "marco")
    print(str(istance))
    print(istance.concatMyString())
    print(istance.stringa1, istance.stringa2)
    istance.stringa2 = "lore"
    print(istance.concatMyString())
