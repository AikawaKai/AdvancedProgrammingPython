'''trialdivision, lucaslehmer, littlefermat and is_prime '''
from math import sqrt

def getp_2el(p):
    cache = [4]
    yield cache[0]
    cur_index = 1;
    while True:
        prev_index = cur_index-1
        value = (cache[prev_index]**2) - 2
        cache.append(value)
        cur_index+=1
        yield value

def trialdivision(num):
    if num%2 == 0:
        return False
    top_value = int(sqrt(num))+1
    for i in range(3, top_value, 2):
        if num%i==0:
            return False
    return True

def lucaslehmer(num):
    '''Mp = 2^p - 1'''
    value = num + 1
    p = 0
    while True:
        if value == 1:
            break
        res = value%2
        if res == 1:
            return False
        value = value/2
        p+=1
    if not trialdivision(p):
        return False
    gen = getp_2el(p)
    count = 0
    si = next(gen)
    while count < p-2:
        count+=1
        si = next(gen)
    if si%num==0:
        return True
    else:
        return False



def littlefermat(num):
    # a^p -1 congruo 1 mod p
    # 0<a<p
    for a in range(2,100):
        if pow(a,num-1,num) != 1:
            return False
    return True

def is_prime(num):
    if num <= 10000:
        return trialdivision(num)
    if 10001 <= num <= 524280:
        return lucaslehmer(num)
    return littlefermat(num)
