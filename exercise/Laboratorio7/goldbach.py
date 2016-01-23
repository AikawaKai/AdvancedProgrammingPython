from math import sqrt


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)+1), 2):  # sqrt+1 altrimenti mi perdo i quadrati perfetti
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(list(filter(isPrime, [elem for elem in range(0, 100)])))
    print(isPrime(9))
