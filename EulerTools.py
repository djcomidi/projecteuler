########################################################################
# Imports
########################################################################

from subprocess import check_output
from gmpy2 import is_prime


########################################################################
# Functions
########################################################################

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def is_pandigital(x):
    return sorted(str(x)) == list("123456789")


def polygonal(sides, index):
    """
    The formulae for generating figurative numbers
    as specified in https://projecteuler.net/problem=61

    :param sides: the number of sides the polygon has [3-8]
    :param index: the index of the figurative number (starts with 1)
    :return: the figurative number
    """
    value = -1
    if sides == 3:  # triangle
        value = (index * (index + 1)) // 2
    if sides == 4:  # square
        value = index ** 2
    if sides == 5:  # pentagonal
        value = (index * (3 * index - 1)) // 2
    if sides == 6:  # hexagonal
        value = index * (2 * index - 1)
    if sides == 7:  # heptagonal
        value = (index * (5 * index - 3)) // 2
    if sides == 8:  # octagonal
        value = index * (3 * index - 2)
    return value


def prime_factors(n):
    output = check_output(["factor", str(n)]).decode()[:-1]
    primes = [int(p) for p in output.split(" ")[1:]]
    return primes


def prime_factors_exps(n):
    factors = prime_factors(n)
    return sorted([(p, factors.count(p)) for p in set(factors)])


def sigma(x, n):
    """
    The sum of the xth powers of the positive divisors of n.

    :param x: the power to which the positive divisors must be raised
    :param n: a positive number
    :return: when x=0, it returns the number of divisors d<=n
             when x=1, it returns the sum of all divisors d<=n
             when x=2, it returns the sum of squares of all divisors d<=n
             ... and so on
    """
    sigmavalue = 1
    for p, exp in prime_factors_exps(n):
        sigmavalue *= sum([p ** (x * t) for t in range(0, exp + 1)])
    return sigmavalue


def totient(n):
    if is_prime(n):
        return n - 1
    phi = n
    for factor in set(prime_factors(n)):
        phi = (phi * (factor - 1)) // factor
    return phi

