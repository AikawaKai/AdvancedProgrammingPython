class MyMath(object):

    def fib(n):
        return 1 if n <= 1 else MyMath.fib(n-1) + MyMath.fib(n-2)


if __name__ == '__main__':
    print(MyMath.fib(0))
    print(MyMath.fib(1))
    print(MyMath.fib(2))
    print(MyMath.fib(3))
    print(MyMath.fib(4))
    print(MyMath.fib(5))
    print(MyMath.fib(6))
    print(MyMath.fib(7))
