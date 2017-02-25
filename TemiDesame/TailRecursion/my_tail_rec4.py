import sys
import time

class MyException(Exception):

    def __init__(self, args, kargs):
        self.args = args
        self.kargs = kargs


def tail_recursion(fun):
    def wrapper(*args, **kargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise MyException(args, kargs)
        while True:
            try:
                print(f)
                return fun(*args, **kargs)
            except MyException as me:
                args = me.args
                kargs = me.kargs
    return wrapper
