def authorizator(key):
    def decorator(fun):
        def wrapper(name, *args):
            if name == key:
                return fun(*args)
            else:
                print("Non sei autorizzato")
        return wrapper
    return decorator


@authorizator("marco")
def miaFun(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    print(miaFun("nicola", 1, 2))
    print(miaFun("geppetto", 1, 2))
    print(miaFun("marco", 1, 2))
