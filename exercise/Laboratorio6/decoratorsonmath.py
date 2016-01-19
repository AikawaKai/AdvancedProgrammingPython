def memoization(f):
    cache = dict()

    def wrapper(*args):
        if args in cache.keys():
            print("uso la cache: ", end="")
            return cache[args]
        else:
            print("Non uso la cache: ", end="")
            result = f(*args)
            cache[args] = result
            return result
    return wrapper


class MyMath(object):

    @memoization
    def fibCaller(n):
        return MyMath.fib(n)

    def fib(n):
        return 0 if n == 0 else (1 if n <= 2 else MyMath.fib(n-1) + MyMath.fib(n-2))

    @memoization
    def factCaller(n):
        return MyMath.fact(n)

    def fact(n):
        return 1 if n <= 1 else n * MyMath.fact(n-1)


if __name__ == '__main__':
    #  fibonacci series
    print(MyMath.fibCaller(0))
    print(MyMath.fibCaller(1))
    print(MyMath.fibCaller(2))
    print(MyMath.fibCaller(3))
    print(MyMath.fibCaller(4))
    print(MyMath.fibCaller(5))
    print(MyMath.fibCaller(6))
    print(MyMath.fibCaller(7))

    print(MyMath.fibCaller(0))
    print(MyMath.fibCaller(1))
    print(MyMath.fibCaller(2))
    print(MyMath.fibCaller(3))
    print(MyMath.fibCaller(4))
    print(MyMath.fibCaller(5))
    print(MyMath.fibCaller(6))
    print(MyMath.fibCaller(7))

    #  factorial
    print(MyMath.factCaller(0))
    print(MyMath.factCaller(1))
    print(MyMath.factCaller(2))
    print(MyMath.factCaller(3))
    print(MyMath.factCaller(4))
    print(MyMath.factCaller(5))
    print(MyMath.factCaller(6))
    print(MyMath.factCaller(7))

    print(MyMath.factCaller(0))
    print(MyMath.factCaller(1))
    print(MyMath.factCaller(2))
    print(MyMath.factCaller(3))
    print(MyMath.factCaller(4))
    print(MyMath.factCaller(5))
    print(MyMath.factCaller(6))
    print(MyMath.factCaller(7))
    print(MyMath.factCaller(8))
