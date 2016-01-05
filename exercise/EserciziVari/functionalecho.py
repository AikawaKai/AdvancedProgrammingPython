def monadic(stringa):
    print(stringa)
    return stringa


rececho = lambda: monadic(input("ECHO - ")) == 'quit' or rececho()


if __name__ == '__main__':
    rececho()
