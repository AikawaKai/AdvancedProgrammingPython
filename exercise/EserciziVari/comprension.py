import math
import functools

def pow(x):
    return x**2
def sum(x,y):
    return x+y


if __name__ == '__main__':
    ##comprehensions
    print([i for i in range(0,11)])
    print([elem for elem in range(0,11) if elem%2==0])
    print([elem for elem in range (0,11) if elem%2==1])
    print([int(math.sqrt(elem**2)) for elem in range(0,11)])

    ##map
    print(list(map(pow,[elem for elem in range(1,10,3)])))

    ##reduce
    print (functools.reduce(lambda x,y: x+y,list(map(pow,[elem for elem in range(0,11)]))))
