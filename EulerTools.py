#!/usr/bin/env python

## Functions that may come handy in some solutions

from sys import hexversion

from gmpy import bincoef, fac, fib, gcd, is_prime, is_square, next_prime
from operator import mul
if hexversion >= 0x03000000:
	from subprocess import check_output
else:
	from commands import getoutput

def aliquot_sum(n):
	return sum_of_divisors(n) - n

def execute_command(cmd,args=""):
	if hexversion >= 0x03000000:
		return check_output([cmd,str(args)])
	else:
		return getoutput("%s %s"%(cmd,str(args)))
	
def heptagonal(n):
	return (n*(5*n-3))//2

def hexagonal(n):
	return n*(2*n-1)

def is_palindrome(x):
	s = str(x)
	return s == s[::-1]

def is_pandigital(x,lowest=1,highest=9):
	return sorted(str(x)) == map( str, range(lowest,highest+1) )

def is_power(n,e):
	return int(round(n**(1.0/e)))**e == n

def is_triangle(t):
	n = int((2*t)**0.5)
	return triangle(n) == t

def number_of_divisors(n):
	return sigma(0,n)

def octagonal(n):
	return n*(3*n-2)

def pentagonal(n):
	return (n*(3*n-1))//2

def polygonal(i,n):
	if i == 3: return triangle(n)
	if i == 4: return square(n)
	if i == 5: return pentagonal(n)
	if i == 6: return hexagonal(n)
	if i == 7: return heptagonal(n)
	if i == 8: return octagonal(n)
	return -1

def prime_factors(n):
	output = execute_command("factor", str(n))
	factors = output.split(" ")[1:]
	return map( int, factors )

def prime_factors_compact(n):
	factors = prime_factors(n)
	return dict( (p,factors.count(p)) for p in factors )

def sigma(x,n):
	factors = prime_factors_compact(n)
	sigmaValue = 1
	for p, e in factors.items():
		sigmaValue *= sum( [ p**(x*t) for t in xrange(0,e+1) ] )
	return sigmaValue

def sum_of_divisors(n):
	return sigma(1,n)

def square(n):
	return n**2

def totient(n):
	if is_prime(n): return n-1
	factors = prime_factors(n)
	phi = n
	for factor in set(factors):
		phi = ( phi * (factor-1) ) // factor
	return phi

def triangle(n):
	return ( n * (n+1) ) // 2
