def memoization(fun):
    fun.dict = {}
    def wrapper(*args):
        if args in fun.dict:
            print("### cached value for {0} --> {1}".format(args, fun.dict[args]))
            return fun.dict[args]
        fun.dict[args] = fun(*args)
        return fun.dict[args]
    return wrapper

@memoization
def sum(n1, n2):
    return n1 if n2==0 else sum(n1+1, n2-1)

@memoization
def fact(n):
    return 1 if n<=1 else n * fact(n-1)

@memoization
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)


if __name__ == '__main__':
    print(fact(0))
    print(fact(1))
    print(fact(2))
    print(fact(3))
    print(fact(4))
    print(fibo(0))
    print(fibo(1))
    print(fibo(2))
    print(fibo(3))
    print(fibo(4))
    print(fibo(5))
    print(fibo(6))
    print(fibo(7))
