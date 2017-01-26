def funGen(value):
    print("stampo nell'output value: ", value, " e ritorno 1")
    return 1

def decorator(fun):
    def wrapper(*args):
        print("Sto decorando con una funzione")
        return fun(*args)
    return wrapper

class DecoratorClass():

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        print("Sto decorando con una classe")
        return self.fun(*args)

if __name__ == '__main__':
    value = 2
    decFun = decorator(funGen)
    print(decFun(value))
    decFunClass = DecoratorClass(funGen)
    print(decFunClass(value))
