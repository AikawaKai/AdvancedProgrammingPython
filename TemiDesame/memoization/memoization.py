def fact(n):
    return 1 if n<=1 else n * fact(n-1)

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
