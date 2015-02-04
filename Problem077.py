#!/usr/bin/env python

from EulerTools import next_prime

N = 0
ways = 0

def count_ways(arr):
	global ways
	if sum(arr) > N: return
	if sum(arr) == N:
		if len(arr) > 1:
			ways += 1
	else:
		p, pmax = 2, N
		if len(arr) != 0:
			p, pmax = max(arr), N-sum(arr)+1
		while p < pmax:
			count_ways(arr+[p])
			p = next_prime(p)

def get_ways(n):
	global N, ways
	N, ways = n, 0
	count_ways([])
	return ways

n = 4
while get_ways(n) <= 5000:
	n += 1
print n
