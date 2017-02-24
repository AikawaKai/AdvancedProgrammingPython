from autoinit import *

class Person():

    def __init__(self, name, lastname):
        pass


class A():

    def __init__(self, a, b, c):
        pass


class Auto():

    def __init__(self, auto, matricola):
        pass

Person = autoinit("Person", (), dict(Person.__dict__))
A = autoinit("A", (), dict(A.__dict__))
Auto = autoinit("Auto", (), dict(Auto.__dict__))


if __name__ == '__main__':
    p = Person("Marco", "Odore")
    a = A(5, 6, 7)
    auto = Auto("Mazda", "zxrr578")
    print(p.name, p.lastname)
    print(a.a, a.b, a.c)
    print(auto.auto, auto.matricola)
