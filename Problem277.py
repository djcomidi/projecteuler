#!/usr/bin/env python

ops = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
rests = "DUd"

# find the last form backwards: (a*n+b)/c
a, b, c = 1, 0, 1
for op in ops:
	if op == "U":
		a, b, c = 4*a, 4*b+2*c, c*3
	if op == "D":
		a, b, c = a, b, c*3
	if op == "d":
		a, b, c = 2*a, 2*b-c, c*3

# x=(a*n+b)/c => n=(x*c-b)/a
x, sol = 0, 0
while sol < 10**15:
	x += 1
	nom = x*c-b
	if nom % a == 0:
		sol = nom//a
print sol
