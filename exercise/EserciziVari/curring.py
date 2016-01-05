
def fun1(x):
    return x


def fun2(x, y):
    return x+y


def fun3(x, y, z):
    return (x+y) % z


def currying(f):
    def fc(*args):
        return f(*args)
    return fc


if __name__ == '__main__':
    identita = currying(fun1)
    somma = currying(fun2)
    somma3 = currying(fun3)
    print(identita(1))
    print(somma(1, 2))
    print(somma3(1, 2, 3))
