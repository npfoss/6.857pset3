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
    if b == 0:
        return 1
    elif b == 1:
        return a
    if b % 2 == 0:
        n = powmod(a, b // 2, m)
        return n * n % m
    return (a * powmod(a, b-1, m)) % m


def is_prime(p):
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
    if p < 4:
        return True
    elif p % 2 == 0 or p % 3 == 0:
        return False

    a = 2
    return powmod(a, p-1, p) == 1


def gen_prime(b):
    """ Returns a prime p with b bits

    >>> p = gen_prime(10)
    >>> p.bit_length()
    10
    >>> is_prime(p)
    True
    """
    candidate = randint(1 << (b-1), (1 << b) - 1)
    while not is_prime(candidate):
        candidate = randint(1 << (b-1), (1 << b) - 1)
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
    random_seed = randint(1, p)
    q_p = powmod(random_seed, 2, p)
    while random_seed != q_p and powmod(q_p, q_p, p) == q_p:
        random_seed = randint(1, p)
        q_p = powmod(random_seed, 2, p)
    return q_p


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

