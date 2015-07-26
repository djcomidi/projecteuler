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


def is_triangle(t):
    n = int((2 * t) ** 0.5)
    return polygonal(3, n) == t


def polygonal(i, n):
    if i == 3:  # triangle
        return (n * (n + 1)) // 2
    if i == 4:  # square
        return n ** 2
    if i == 5:  # pentagonal
        return (n * (3 * n - 1)) // 2
    if i == 6:  # hexagonal
        return n * (2 * n - 1)
    if i == 7:  # heptagonal
        return (n * (5 * n - 3)) // 2
    if i == 8:  # octagonal
        return n * (3 * n - 2)
    return -1


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

