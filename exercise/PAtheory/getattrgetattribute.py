class A():

    def __init__(self, attr):
        self.attr = attr

    def __getattribute__(self, attrname):
        print("Metodo di estrazione abituale")
        return object.__getattribute__(self, attrname)

    def __getattr__(self, attributename):
        print("attributo non definito")
        self.__dict__[attributename] = "nuovo valore"
        return self.__dict__[attributename]

if __name__ == '__main__':
    a = A(5)
    print(a.attr)
    print(a.attr2)
    print(getattr(a, "attr"))
