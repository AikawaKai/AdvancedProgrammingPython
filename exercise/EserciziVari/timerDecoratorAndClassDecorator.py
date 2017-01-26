import time

def timer(fun):
    def wrapper(*args):
        start = time.time()
        result = fun(*args)
        print(time.time()-start)
        return result
    return wrapper

@timer
def comphrension(n):
    return [x for x in range(0, n)]


if __name__ == '__main__':
    comphrension(10000)
    comphrension(100000)
    comphrension(1000000)
    comphrension(10000000)
