class A(object):

    def do_stuff(self):
        print("I'm doing stuff")

class B(A):

    def do_stuff(self):
        A.ciao = "ciao"
        print(A.ciao)
        A.do_stuff(self)


class C(A):

    def do_stuff(self):
        A.ciao = "ciau"
        print(A.ciao)
        A.do_stuff(self)


class D(B,C):

    def do_stuff(self):
        B.do_stuff(self)
        C.do_stuff(self)

if __name__ == '__main__':

    d = D()
    d.do_stuff()
    d.do_stuff()
