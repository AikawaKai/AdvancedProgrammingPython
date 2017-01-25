def decorator(class_to_wrapp):
    class ClassWrapper:

        def __init__(self, *args):
            print("Inizializzo classe wrapper")
            self.wrapped = class_to_wrapp(*args)

        def __getattr__(self, name):
            print("prendo gli attributi della classe wrappata")
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            if name == 'wrapped':
                print(".. e gli inizializzo l'attributo interno self.wrapped")
                self.__dict__[name] = value
            else:
                print("setto gli attributi della classe wrappata")
                setattr(self.wrapped, name, value)
    return ClassWrapper

class A:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def printRoba(self):
        print(self.value)

if __name__ == '__main__':
    decA = decorator(A)
    a_instance = decA("ciaociao")
    print(a_instance.getValue())
