#!/usr/bin/env python

def dec_to_tri(n):
	if n < 3: return n
	q, r = divmod(n,3)
	return 10*dec_to_tri(q)+r

total = 0
# by observation and a bit of luck:
total += 12222 // 9
total += 1122222222 // 99
total += 111222222222222 // 999
total += 11112222222222222222 // 9999

toCheck = set(range(1,10001)) - set([9,99,999,9999])
k = 0
while len(toCheck) > 0:
	k += 1
	t = dec_to_tri(k)
	valids = [ n for n in toCheck if t % n == 0 ]
	total += sum( t//n for n in valids )
	toCheck -= set(valids)
print total
# ~12m45s
