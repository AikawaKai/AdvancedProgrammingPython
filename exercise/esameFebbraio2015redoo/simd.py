from threading import Thread


def split_and_merge(numthread, reducefunc):
    def addparameter(fun):
        def wrapper(res, *args):
            res.append(fun(*args))
        return wrapper

    def decorator(fun):
        def wrapper(*args):
            funr = addparameter(fun)
            threads = []
            lista = args[0]
            lenlista = len(lista)
            offset = lenlista // numthread
            start = 0
            end = offset
            for i in range(numthread-1):
                res = []
                print("runner {0}".format(lista[start:end]))
                thread = Thread(target=funr, args=(res, lista[start:end]))
                start += offset
                end += offset
                threads.append((thread.start(), res))
            res = []
            thread = Thread(target=funr, args=(res, lista[start:]))
            print("runner {0}".format(lista[start:]))
            threads.append((thread.start(), res))
            map(lambda x: x[0].join(), threads)
            listares = [y[0] for x, y in threads]
            return reducefunc(listares)
        return wrapper
    return decorator
