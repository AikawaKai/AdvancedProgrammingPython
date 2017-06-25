import sys

class TailException(Exception):

    def __init__(self, args, kargs):
        self.args = args
        self.kargs = kargs



def tail_recursion(fun):
    def wrapper(*args, **kargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailException(args, kargs)
        else:
            while True:
                try:
                    return fun(*args, **kargs)
                except TailException as te:
                    args = te.args
                    kargs = te.kargs
    return wrapper
