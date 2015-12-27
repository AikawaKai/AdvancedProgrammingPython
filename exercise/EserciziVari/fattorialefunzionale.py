from functools import reduce


def factFunct(p):
    return reduce(lambda x, y: x*y, range(1, p+1))


if __name__ == '__main__':
    print(factFunct(3), factFunct(4), factFunct(5))
