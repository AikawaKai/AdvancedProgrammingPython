import threading


def split_and_merge(n_threads, reduce_f):
    def decorator(fun):
        def wrapper(*args):
            return fun(*args)
        return wrapper
    return decorator
