from eulero import *

def firstn(g, n):
   for i in range(n):
      yield next(g)

if __name__ == '__main__':
   print("exact value for π :- {0:.16}".format(3.14159265358979))
   print("old(π) :-", list(firstn(pi_series(), 7)))
   print("new(π) :-", list(firstn(euler_accelerator(pi_series()), 7)))
   print("exact value for ε :- {0:.16}".format(2.71828182845904))
   print("old(ε) :-", list(firstn(e_series(), 7)))
   print("new(ε) :-", list(firstn(euler_accelerator(e_series()), 7)))
