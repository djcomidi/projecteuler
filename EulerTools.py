#!/usr/bin/env python

########################################################################
## Imports
########################################################################

from sys import hexversion

from gmpy import bincoef
from gmpy import fac
from gmpy import fib
from gmpy import gcd
from gmpy import is_prime
from gmpy import is_square
from gmpy import next_prime
if hexversion >= 0x03000000:
	from subprocess import check_output
else:
	from commands import getoutput
from operator import mul

########################################################################
## Functions
########################################################################

def aliquot_sum(n):
	return sum_of_divisors(n) - n

def execute_command(cmd,args=""):
	if hexversion >= 0x03000000:
		return check_output([cmd,str(args)])
	else:
		return getoutput("%s %s"%(cmd,str(args)))
	
def is_palindrome(x):
	s = str(x)
	return s == s[::-1]

def is_pandigital(x,lowest=1,highest=9):
	return sorted(str(x)) == map( str, range(lowest,highest+1) )

def is_triangle(t):
	n = int((2*t)**0.5)
	return polygonal(3,n) == t

def number_of_divisors(n):
	return sigma(0,n)

def polygonal(i,n):
	if i == 3: # triangle
		return ( n * (n+1) ) // 2
	if i == 4: # square
		return n**2
	if i == 5: # pentagonal
		return (n*(3*n-1))//2
	if i == 6: # hexagonal
		return n*(2*n-1)
	if i == 7: # heptagonal
		return (n*(5*n-3))//2
	if i == 8: # octagonal
		return n*(3*n-2)
	return -1

def prime_factors(n):
	p, primes = 1, []
	while n > 1:
		p = next_prime(p)
		while n % p == 0:
			primes, n = primes+[int(p)], n//p
	return primes

def prime_factors_dict(n):
	factors = prime_factors(n)
	return dict( (p,factors.count(p)) for p in factors )

def sigma(x,n):
	factors = prime_factors_dict(n)
	sigmaValue = 1
	for p, e in factors.items():
		sigmaValue *= sum( [ p**(x*t) for t in xrange(0,e+1) ] )
	return sigmaValue

def sum_of_divisors(n):
	return sigma(1,n)

def totient(n):
	if is_prime(n): return n-1
	phi = n
	for factor in prime_factors_dict(n).keys():
		phi = ( phi * (factor-1) ) // factor
	return phi

########################################################################
## Decorators
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
	def __get__(self, obj, objtype):
		"""Support instance methods."""
		return functools.partial(self.__call__, obj)
