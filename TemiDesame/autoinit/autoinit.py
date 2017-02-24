import inspect


def decorInit(init):
    def wrapper(*args, **kargs):
        selfi = args[0]
        sig = list(inspect.signature(init).parameters)[1:]
        for i in range(len(sig)):
            setattr(selfi, sig[i], args[i+1])
    return wrapper



class autoinit(type):

    def __new__(meta, classname, supers, dict_):
        dict_["__init__"] = decorInit(dict_['__init__'])
        return type.__new__(meta, classname, supers, dict_)
