def memoization(f):
    cache = dict()

    def wrapper(*args):
        if args in cache.keys():
            #  print("uso la cache: ", end="")
            return cache[args]
        else:
            #  print("Non uso la cache: ", end="")
            result = f(*args)
            cache[args] = result
            return result
    return wrapper


def stringPreparer(funcName, args):
    base = funcName + "("
    args = map(lambda x: str(x), args)
    content = ", ".join(args)
    return base + content + ")\n"


def logging(f):
    def wrapper(*args):
        out_file = open(f.__name__, "a")
        string = stringPreparer(f.__name__, args)
        out_file.write(string)
        return f(*args)
    return wrapper


def stack_trace(f):
    def wrapper(*args):
        string = stringPreparer(f.__name__, args)
        print(string, end="\n\t")
        return f(*args)
    return wrapper


class MyMath(object):

    #  @memoization
    #  @logging
    @stack_trace
    def fib(n):
        return 0 if n == 0 else (1 if n <= 2 else MyMath.fib(n-1) + MyMath.fib(n-2))

    #  @memoization
    #  @logging
    @stack_trace
    def fact(n):
        return 1 if n <= 1 else n * MyMath.fact(n-1)


if __name__ == '__main__':
    #  fibonacci series
    print(MyMath.fib(0))
    print(MyMath.fib(1))
    print(MyMath.fib(2))
    print(MyMath.fib(3))
    print(MyMath.fib(4))
    print(MyMath.fib(5))
    print(MyMath.fib(6))
    print(MyMath.fib(7))

    print(MyMath.fib(0))
    print(MyMath.fib(1))
    print(MyMath.fib(2))
    print(MyMath.fib(3))
    print(MyMath.fib(4))
    print(MyMath.fib(5))
    print(MyMath.fib(6))
    print(MyMath.fib(7))

    #  factorial
    print(MyMath.fact(0))
    print(MyMath.fact(1))
    print(MyMath.fact(2))
    print(MyMath.fact(3))
    print(MyMath.fact(4))
    print(MyMath.fact(5))
    print(MyMath.fact(6))
    print(MyMath.fact(7))

    print(MyMath.fact(0))
    print(MyMath.fact(1))
    print(MyMath.fact(2))
    print(MyMath.fact(3))
    print(MyMath.fact(4))
    print(MyMath.fact(5))
    print(MyMath.fact(6))
    print(MyMath.fact(7))
    print(MyMath.fact(8))
