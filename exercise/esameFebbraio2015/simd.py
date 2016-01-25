import functools
import threading


def split_and_merge(numthread, composeF):

    def funRes(fun):
        def funWithResult(res, *args):
            res.append(fun(*args))
        return funWithResult

    def decorator(fun):
        funWithResult = funRes(fun)
        def wrapper(*args):
            lista = args[0]
            partition = len(lista)//numthread
            setThreadList = []
            while partition < len(lista):
                plista = lista[:partition]
                lista = lista[partition:]
                setThreadList.append(plista)
            results = []
            for tlist in setThreadList:
                res = []
                threading.Thread(target=funWithResult, args=(res, tlist)).start()
                results.append(res[0])
            return composeF(results)
        return wrapper
    return decorator


@split_and_merge(11, lambda a: functools.reduce(lambda x, y: x*y, a))
def mul(l):
    return functools.reduce(lambda x, y: x*y, l)


@split_and_merge(5, lambda a: functools.reduce(lambda x, y: y+x, a))
def reverse(l):
    return l[::-1]

if __name__ == "__main__":
    print(mul(list(range(1, 101))))  # this computes 100!
    print(mul(list(range(1, 31))))  # this computes 30!
    print(reverse("She sells sea shells on the sea shore. If she sells sea shells on the sea shore, where are the sea shells she sells?"))
    print(reverse("Swan swam over the pond, Swim swan swim! Swan swam back again - Well swum swan!"))
