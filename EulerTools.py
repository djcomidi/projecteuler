########################################################################
# Imports
########################################################################

from functools import partial
from subprocess import check_output
from gmpy2 import is_prime
from gmpy2 import next_prime


########################################################################
# Functions
########################################################################

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def is_pandigital(x, lowest=1, highest=9):
    return sorted(str(x)) == [str(i) for i in range(lowest, highest + 1)]


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
    # p, primes = 1, []
    # while n > 1:
    #     p = next_prime(p)
    #     while n % p == 0:
    #         primes, n = primes + [int(p)], n // p
    # return primes


def prime_factors_dict(n):
    factors = prime_factors(n)
    return dict((p, factors.count(p)) for p in factors)


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
    factors = prime_factors_dict(n)
    sigmavalue = 1
    for p in factors:
        sigmavalue *= sum([p ** (x * t) for t in range(0, factors[p] + 1)])
    return sigmavalue


def totient(n):
    if is_prime(n):
        return n - 1
    phi = n
    for factor in prime_factors_dict(n):
        phi = (phi * (factor - 1)) // factor
    return phi


########################################################################
# Decorators
########################################################################

# http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class Memoize(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj):
        """Support instance methods."""
        return partial(self.__call__, obj)
