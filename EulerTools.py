#!/usr/bin/env python

## Functions that may come handy in some solutions

from gmpy import fac, is_prime, is_square, next_prime
from operator import mul
from subprocess import check_output

def aliquot_sum(n):
	return sum_of_divisors(n) - n

def hexagonal(n):
	return n*(2*n-1)

def is_palindrome(x):
	s = str(x)
	return s == s[::-1]

def is_pandigital(s,lowest=1,highest=9):
	return sorted(s) == map( str, range(lowest,highest+1) )

def is_triangle(t):
	n = int((2*t)**0.5)
	return triangle(n) == t

def number_of_divisors(n):
	exps = prime_factors_compact(n).values()
	return reduce( mul, [e+1 for e in exps], 1 )

def pentagonal(n):
	return (n*(3*n-1))//2

def prime_factors(n):
	output = check_output(["factor",str(n)])[:-1]
	factors = output.split(" ")[1:] 
	return map( int, factors )

def prime_factors_compact(n):
	factors = prime_factors(n)
	return dict( (p,factors.count(p)) for p in factors )

def sum_of_divisors(n):
	divisors = set([1,n])
	root = int(n**0.5)
	for d in xrange(2,root+1):
		if n%d == 0:
			divisors.add(d)
			divisors.add(n//d)
	return sum(divisors)

def triangle(n):
	return ( n * (n+1) ) // 2
