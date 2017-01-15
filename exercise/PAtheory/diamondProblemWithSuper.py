class A(object):

    def do_stuff(self):
        print("do_stuff")
        print("A")


class B(A):

    def do_stuff(self):
        super(B,self).do_stuff()
        print("B")

class C(A):

    def do_stuff(self):
        super(C, self).do_stuff()
        print("C")

class D(B,C):

    def do_stuff(self):
        super(D, self).do_stuff()
        print("D")

if __name__ == '__main__':
    d = D()
    print(D.__mro__)
    d.do_stuff()
