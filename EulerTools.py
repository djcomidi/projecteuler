#!/usr/bin/env python

## Functions that may come handy in some solutions

from subprocess import check_output

def get_prime_factors(n):
	output = check_output(["factor",str(n)])[:-1]
	prime_factors = output.split(" ")[1:] 
	return map( int, prime_factors )

def get_prime_factors_dict(n):
	prime_factors = get_prime_factors(n)
	return dict( (x,prime_factors.count(x)) for x in prime_factors )

def is_palindrome(x):
	s = str(x)
	return s == s[::-1]

