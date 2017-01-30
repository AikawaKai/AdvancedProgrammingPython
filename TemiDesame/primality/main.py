'''To verify that a number is prime is considered a trivial task for a computer scientist.
This is true when the number to check is pretty small (let's say if it is below or equal
to 10000) but when the number to check grows larger the naïve approach (namely trial division)
tends to become slower and slower up to be intractable.

Fortunately in the years, several mathematicians proposed different algorithms to check the
primality of big numbers. Just to cite a few Lucas-Lehmer and Fermat's Little Theorem.

The Lucas–Lehmer test works as follows. Let Mp = 2p-1 be the Mersenne number to test with p
an odd prime. The primality of p can be efficiently checked with a simple algorithm like
trial division since p is exponentially smaller than Mp. Define a sequence { si } for all i≥0 by

s_i = 4 if i=0 else s_(i-1)^2


Then Mp is prime if and only if sp-2 ≡ 0 (mod Mp). The number sp-2 (mod Mp) is called the Lucas–Lehmer residue of p.

Fermat's little theorem states that if p is prime and 0<a<p, then ap-1≡1 (mod p). If we want to
test whether p is prime,
then we can pick random a's in the interval and see whether the equality holds. If the equality does not
hold for a value of a, then p is not prime. If the equality does hold for many values of a, then we can
say that p is probably prime.

As you can notice, neither the Lucas-Lehmer's primality test nor the Fermat's Little Theorem provide a
certain for all numbers. But in an case we can use them to define the number as probably prime or
surely not prime.

The exercise consists of implementing a module primality with (at least) 4 functions: trialdivision,
lucaslehmer, littlefermat and is_prime. Each of them is a predicate over an integer number (the one
that should be tested as prime). The first three functions should implement the described algorithms.
The last one is testing the primality of the input by applying one of the other algorithms according
to the following rules:

    if the input is smaller or equal to 10000 it will use the trial division algorithm.
    if the input is between 10001 and 524280 (extremes included) it will use the Lucas-Lehmar's algorithm
    (no check if the input is a Marsenne number).
    it will use the Fermat's little theorem otherwise (please use a reasonable (both in size and values)
    set of values for a).

Note that the given interfaces must be respected and your module should be compliant with the following
main and its execution.
'''
from primality import *

def test_primes(vl):
  if len(vl)>0:
     print("{:14d} :- {}".format(vl[0], is_prime(vl[0])))
     test_primes(vl[1:])

if __name__ == '__main__':
  test_primes([25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])
