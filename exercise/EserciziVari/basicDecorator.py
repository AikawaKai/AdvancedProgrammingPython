# basic decorator

def decorator(f):
    def wrapper(*args):
        print("Funzione decorata")
        return f(*args)
    return wrapper

class decoratorClass():

    def __init__(self, f):
        self.decorated = f

    def __call__(self, *args):
        print("Funzione decorata con classe")
        return self.decorated(*args)


def toDecore(value):
    print("Printo value: ", value)

if __name__ == '__main__':
    basicD = decorator(toDecore)
    basicD(10)
    classD = decoratorClass(toDecore)
    classD(15)
