def memoization(f):
    f.cache = dict()

    def wrapper(*args):
        if args in f.cache:
            print("cached value for {0} --> {1}".format(args, f.cache[args]))
            return f.cache[args]
        result = f(*args)
        f.cache[args] = result
        return result
    return wrapper


@memoization
def fact(n):
    return 1 if n == 1 else n * fact(n-1)


@memoization
def fibo(n):
    return n if n <= 1 else fibo(n-1) + fibo(n-2)


@memoization
def sum(a, b):
    return a if b == 0 else sum(a+1, b-1)

if __name__ == "__main__":
    print("sum({0},{1})  => {2}".format(9, 5, sum(9, 5)))
    print("sum({0},{1})  => {2}".format(7, 7, sum(7, 7)))
    print("sum({0},{1}) => {2}".format(10, 4, sum(10, 4)))
    print("sum({0},{1}) => {2}".format(1, 13, sum(1, 13)))
    print("sum({0},{1}) => {2}".format(7, 25, sum(7, 25)))

    print("fibo({0})   => {1}".format(5, fibo(5)))
    print("fibo({0})   => {1}".format(7, fibo(7)))
    print("fibo({0})  => {1}".format(25, fibo(25)))

    print("fact({0})   => {1}".format(5, fact(5)))
    print("fact({0})   => {1}".format(7, fact(7)))
    print("fact({0})  => {1}".format(10, fact(10)))
