def fact(n, acc):
    if n<=1:
        return acc
    else:
        return fact(n-1, acc*n)

def pi_series():
    yield 4
    num = 3
    curr = 4
    sign = 1
    while True:
        sign = (-1)*sign
        curr += (sign*4/num)
        num+=2
        yield curr

def e_series():
    yield 1
    num = 1
    curr = 1
    while True:
        next_ = 1/fact(num, 1)
        curr += next_
        num+=1
        yield curr



def euler_accelerator(g):
    curr = next(g)
    n = next(g)
    n_1 = next(g)
    yield n_1 - ((n_1 -n)**2)/(curr-(2*n)+n_1)
    while True:
        curr = n
        n = n_1
        n_1 = next(g)
        n_next = n_1 - ((n_1 -n)**2)/(curr-(2*n)+n_1)
        yield n_next
