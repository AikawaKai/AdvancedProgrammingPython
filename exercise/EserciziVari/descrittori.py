class C:
    def __init__(self):
        self.class_attribute = "a value"

    def __str__(self):
        return self.class_attribute


def introspect(self):
    result = ""
    for k, v in self.__dict__.items():
        result += k+": "+v+"\n"
    return result

C.__str__ = introspect


class D():
    class_attribute = "a value"

    def f(self):
        return "a function"

    def __call__(self, integer):
        print("rendo l'istanza chiamabile come funzione {0}".format(integer))
