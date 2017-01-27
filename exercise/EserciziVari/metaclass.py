
class MetaOne(type):

    def __init__(meta, classname, supers, classdict):
        print("Sto inizializzando l'istanza...?")
        print(meta, classname, supers, classdict)
        return type.__init__(meta, classname, supers, classdict)

    def __new__(meta, classname, supers, classdict):
        print("Sto creando la classe....?")
        print(meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

class A(metaclass=MetaOne):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method(self):
        return self.a + self.b

if __name__ == '__main__':
    a = A(1, 2)
    print(a.method())
