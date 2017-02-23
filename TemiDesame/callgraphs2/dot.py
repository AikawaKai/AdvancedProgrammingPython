from ABC import *

class CG(type):

    def __init__(self, classname, supers, dict_, *others):
        print(classname)
        return type.__init__(self, classname, supers, dict_, *others)


A = CG("A", (), dict(A.__dict__))
B = CG("B", (), dict(B.__dict__))
C = CG("C", (), dict(C.__dict__))
