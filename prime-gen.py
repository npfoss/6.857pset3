"""
Skeleton code for prime generation (Python 2 or 3)

Running the module will run doctests, though doctests are definitely not
comprehensive (for instance, see gen_safe_prime). To turn them off, comment out
doctests in main(). To run verbose doctests, run with `python prime-gen.py -v`.
"""

from __future__ import print_function
from random import randint, randrange


def powmod(a, b, m):
    """ Returns the power a**b % m

    >>> powmod(3, 4, 7)
    4
    >>> powmod(123456789, 987654321, 1000000007)
    652541198
    """

    raise NotImplementedError


def is_prime(p, trials=10):
    """ Returns whether p is probably prime

    This should run enough iterations of the test to be reasonably confident
    that p is prime

    >>> is_prime(3)
    True
    >>> is_prime(9)
    False
    >>> is_prime(998244353)
    True
    >>> is_prime(998244357)
    False
    """

    for t in range(trials):
        a = randint(1, p-1)
        if powmod(a, p-1, p) != 1:
            return False
    return True


def gen_prime(b):
    """ Returns a prime p with b bits

    >>> p = gen_prime(10)
    >>> p.bit_length()
    10
    >>> is_prime(p)
    True
    """
    candidate = int("".join(str(randint(0, 1)) for _ in range(b)), 2)
    while not is_prime(candidate):
        candidate = int("".join(str(randint(0, 1)) for _ in range(b)), 2)
    return candidate


def gen_safe_prime(b):
    """ Return a safe prime p with b bits

    >>> p = gen_safe_prime(10)
    >>> p.bit_length()
    10
    """
    p = 4
    while not is_prime(2*p+1):
        p = gen_prime(b-1)

    return 2*p+1


def gen_safe_prime_generator(p):
    """ Returns a generator of a Q_p, for a safe prime p

    >>> p = gen_safe_prime(10)
    >>> g = gen_safe_prime_generator(p)
    """

    raise NotImplementedError


def el_gamal_is_qr(p, g, gx, gy, gxy_m):
    """ Returns whether m is a quadratic residue, given an ElGamal ciphertext over Z_p^*
    """

    raise NotImplementedError


def main():
    import doctest
    print(doctest.testmod(exclude_empty=True))

    print("Random prime:", gen_prime(128))

    p = gen_safe_prime(128)
    g = gen_safe_prime_generator(p)
    print("Safe prime and generator:", p, g)

    bit = el_gamal_get_bit(261559759947351029532457942104910865303,
        194286524128031642142474107184510601326,
        198945838169134496994751864693096545284,
        162960645829528127846175960244367199327,
        181937067363429702065627884694752413851)
    print("ElGamal message bit:", bit)


if __name__ == '__main__':
    main()
