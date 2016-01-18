class MyMath(object):

    def fib(n):
        return 0 if n == 0 else (1 if n <= 2 else MyMath.fib(n-1) + MyMath.fib(n-2))

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

    #  factorial
    print(MyMath.fact(0))
    print(MyMath.fact(1))
    print(MyMath.fact(2))
    print(MyMath.fact(3))
    print(MyMath.fact(4))
    print(MyMath.fact(5))
    print(MyMath.fact(6))
    print(MyMath.fact(7))
