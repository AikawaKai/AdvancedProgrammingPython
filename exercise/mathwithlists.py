def notmultipleOf3or5(x):
    return (x % 3 == 0) or (x % 5 == 0)


def sumdigit(sum, x):
    if x < 1:
        return sum
    else:
        sum = sum + (x % 10)
        x = int(x/10)
        return sumdigit(sum, x)


def numofdigit(sum, x):
    if x < 1:
        return sum
    else:
        sum = sum + 1
        x = x//10
        return numofdigit(sum, x)


def iterativenumofdigit(x):
    sum = 0
    while x >= 1:
        sum = sum + 1
        x = x // 10
    return sum


def fibonacci():
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c


if __name__ == '__main__':
    # 1 exercise
    print(sum(list(filter(notmultipleOf3or5, range(1, 1000)))))
    # 2 exercise
    print([x*2 for x in range(1, 21)])
    # 3 exercise
    print(sumdigit(0, 2**1000))
    # 4 fibonacci
    print(numofdigit(0, 2**1000))
    fibonacci = fibonacci()
    value = next(fibonacci)
    while iterativenumofdigit(value) < 1000:
        value = next(fibonacci)
    print(value)
