import sys

class MyException(Exception):

    def __init__(self, args, kargs):
        self.args = args
        self.kargs = kargs

def tail_recursion(fun):
    def wrapper(*args, **kargs):
        frame = sys._getframe()
        if frame.f_back and frame.f_back.f_back and frame.f_back.f_back.f_code == frame.f_code:
            raise MyException(args, kargs)
        while True:
            try:
                return fun(*args, **kargs)
            except MyException as mye:
                args = mye.args
                kargs = mye.kargs
    return wrapper
